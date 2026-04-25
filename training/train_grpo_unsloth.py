"""TRL + Unsloth GRPO trainer for OpenEnv-DDI (T4 budget friendly).

This script adapts the rollout-driven structure from sample-training-script.ipynb
to the DDI environment:
- builds prompts from live environment observations
- samples model actions via TRL OpenEnv rollout generation
- applies inference guardrails before stepping the environment
- logs multi-signal rewards from observation metadata
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from datasets import Dataset, load_dataset
from transformers import AutoTokenizer

from inference import (
    SYSTEM_PROMPT,
    apply_action_guardrails,
    heuristic_action,
    observation_to_prompt,
    parse_action,
)
from client import DdiEnv
from models import DdiAction
from server.ddi_environment import DdiEnvironment


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name", type=str, default="Qwen/Qwen2.5-14B-Instruct")
    parser.add_argument(
        "--sft_dataset",
        type=Path,
        default=Path("training/data/sft_warmstart_train.jsonl"),
    )
    parser.add_argument(
        "--output_dir",
        type=Path,
        default=Path("training/outputs/qwen25-14b-ddi-grpo"),
    )
    parser.add_argument("--train_steps", type=int, default=120)
    parser.add_argument("--warmup_steps", type=int, default=30)
    parser.add_argument("--max_turns", type=int, default=12)
    parser.add_argument("--dataset_size", type=int, default=256)
    parser.add_argument("--num_generations", type=int, default=2)
    parser.add_argument("--case_split", type=str, default="train", choices=["train", "validation"])
    parser.add_argument(
        "--task_sampling",
        type=str,
        default="mixed_seeded",
        choices=["curriculum", "mixed", "mixed_seeded", "mixed_shuffled"],
    )
    parser.add_argument("--learning_rate", type=float, default=2e-5)
    parser.add_argument("--lora_rank", type=int, default=16)
    parser.add_argument("--lora_alpha", type=int, default=32)
    parser.add_argument("--lora_dropout", type=float, default=0.05)
    parser.add_argument("--max_seq_length", type=int, default=2048)
    parser.add_argument("--seed", type=int, default=17)
    parser.add_argument(
        "--env_base_url",
        type=str,
        default="",
        help="Optional deployed env URL (e.g. HF Space). Empty uses local in-process env.",
    )
    return parser.parse_args()


class LocalEnvAdapter:
    def __init__(self, case_split: str, task_sampling: str) -> None:
        self._env = DdiEnvironment(case_split=case_split, task_sampling=task_sampling)

    def reset(self):
        return self._env.reset()

    def step(self, action: DdiAction):
        return self._env.step(action)

    def close(self) -> None:
        return None


class RemoteEnvAdapter:
    def __init__(self, base_url: str) -> None:
        self._env = DdiEnv(base_url=base_url)

    def reset(self):
        result = self._env.reset()
        return result.observation

    def step(self, action: DdiAction):
        result = self._env.step(action)
        return result.observation

    def close(self) -> None:
        self._env.close()


def _component_reward(observation) -> dict[str, float]:
    metadata = observation.metadata or {}
    components = metadata.get("reward_components", {})
    return {
        "triage_reward": float(components.get("triage_score", 0.0)),
        "regimen_reward": float(components.get("regimen_score", 0.0)),
        "risk_delta_reward": float(components.get("risk_delta_bonus", 0.0)),
        "invalid_penalty": float(components.get("invalid_action_penalty", 0.0)),
        "terminal_adjustment": float(components.get("terminal_adjustment", 0.0)),
        "final_score": float(observation.final_score or 0.0),
        "scalar_reward": float(observation.reward or 0.0),
    }


def _warmup_trace(env, warmup_steps: int) -> list[float]:
    obs = env.reset()
    reward_trace: list[float] = []
    decided: set[str] = set()
    suggested: set[str] = set()

    for _ in range(max(1, warmup_steps)):
        payload = heuristic_action(
            obs,
            decided_interactions=decided,
            suggested_regimens=suggested,
        )
        payload = apply_action_guardrails(
            payload,
            obs,
            decided_interactions=decided,
            suggested_regimens=suggested,
        )
        action = DdiAction(**payload)
        if action.interaction_id:
            decided.add(action.interaction_id)
        if action.suggested_regimen_id:
            suggested.add(action.suggested_regimen_id)

        obs = env.step(action)
        reward_trace.append(float(obs.reward or 0.0))
        if obs.done:
            obs = env.reset()
            decided.clear()
            suggested.clear()
    return reward_trace


def _build_dataset(args: argparse.Namespace) -> Dataset:
    if args.sft_dataset.exists():
        ds = load_dataset("json", data_files=str(args.sft_dataset), split="train")
        if "messages" in ds.column_names:
            prompts = []
            for row in ds:
                messages = row.get("messages") or []
                user_msg = next(
                    (message.get("content", "") for message in messages if message.get("role") == "user"),
                    "Perform safe DDI triage.",
                )
                prompts.append(user_msg)
            if prompts:
                return Dataset.from_dict({"prompt": prompts[: args.dataset_size]})

    return Dataset.from_dict(
        {"prompt": ["Perform safe DDI triage with strict JSON action output."] * args.dataset_size}
    )


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    try:
        from unsloth import FastLanguageModel  # type: ignore
        from trl import GRPOConfig, GRPOTrainer  # type: ignore
        from trl.experimental.openenv import generate_rollout_completions  # type: ignore
    except Exception as exc:  # pragma: no cover
        raise RuntimeError(
            "Missing training dependencies. Install with: uv pip install -e .[train]"
        ) from exc

    tokenizer = AutoTokenizer.from_pretrained(args.model_name, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model, _ = FastLanguageModel.from_pretrained(
        model_name=args.model_name,
        max_seq_length=args.max_seq_length,
        dtype=None,
        load_in_4bit=True,
    )
    model = FastLanguageModel.get_peft_model(
        model,
        r=args.lora_rank,
        lora_alpha=args.lora_alpha,
        lora_dropout=args.lora_dropout,
        target_modules=[
            "q_proj",
            "k_proj",
            "v_proj",
            "o_proj",
            "gate_proj",
            "up_proj",
            "down_proj",
        ],
        bias="none",
        use_gradient_checkpointing=True,
    )

    env = (
        RemoteEnvAdapter(args.env_base_url)
        if args.env_base_url
        else LocalEnvAdapter(args.case_split, args.task_sampling)
    )
    reward_trace = _warmup_trace(env, args.warmup_steps)
    dataset = _build_dataset(args)

    grpo_config = GRPOConfig(
        output_dir=str(args.output_dir),
        learning_rate=args.learning_rate,
        per_device_train_batch_size=1,
        gradient_accumulation_steps=8,
        warmup_steps=max(1, min(20, args.train_steps // 6)),
        num_generations=args.num_generations,
        max_completion_length=96,
        logging_steps=5,
        save_steps=max(20, args.train_steps // 3),
        max_steps=args.train_steps,
        gradient_checkpointing=True,
        gradient_checkpointing_kwargs={"use_reentrant": False},
        bf16=False,
        fp16=True,
        seed=args.seed,
    )

    def rollout_once(trainer: Any, dataset_prompt: str) -> dict[str, Any]:
        result = env.reset()
        observation = result

        prompt_ids = []
        completion_ids = []
        logprobs = []
        triage_rewards = []
        regimen_rewards = []
        risk_delta_rewards = []
        invalid_penalties = []
        final_scores = []

        decided: set[str] = set()
        suggested: set[str] = set()

        for _ in range(args.max_turns):
            if observation.done:
                break

            prompt_payload = observation_to_prompt(observation, history=[])
            user_prompt = dataset_prompt if dataset_prompt else prompt_payload
            messages = [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ]
            prompt_text = tokenizer.apply_chat_template(
                messages,
                add_generation_prompt=True,
                tokenize=False,
            )

            rollout_outputs = generate_rollout_completions(trainer, [prompt_text])[0]
            prompt_ids.extend(rollout_outputs.get("prompt_ids", []))
            completion_ids.extend(rollout_outputs.get("completion_ids", []))
            logprobs.extend(rollout_outputs.get("logprobs", []))
            completion_text = rollout_outputs.get("text") or tokenizer.decode(
                rollout_outputs.get("completion_ids", []), skip_special_tokens=True
            )

            raw_payload = parse_action(completion_text, observation)
            payload = apply_action_guardrails(
                raw_payload,
                observation,
                decided_interactions=decided,
                suggested_regimens=suggested,
            )
            action = DdiAction(**payload)
            if action.interaction_id:
                decided.add(action.interaction_id)
            if action.suggested_regimen_id:
                suggested.add(action.suggested_regimen_id)

            observation = env.step(action)
            comp = _component_reward(observation)
            triage_rewards.append(comp["triage_reward"])
            regimen_rewards.append(comp["regimen_reward"])
            risk_delta_rewards.append(comp["risk_delta_reward"])
            invalid_penalties.append(comp["invalid_penalty"])
            final_scores.append(comp["final_score"])

        return {
            "prompt_ids": prompt_ids,
            "completion_ids": completion_ids,
            "logprobs": logprobs,
            "triage_reward": triage_rewards[-1] if triage_rewards else 0.0,
            "regimen_reward": regimen_rewards[-1] if regimen_rewards else 0.0,
            "risk_delta_reward": risk_delta_rewards[-1] if risk_delta_rewards else 0.0,
            "invalid_penalty": invalid_penalties[-1] if invalid_penalties else 0.0,
            "final_score_reward": final_scores[-1] if final_scores else 0.0,
        }

    def rollout_func(prompts, trainer=None):  # type: ignore[no-untyped-def]
        episode_prompt_ids = []
        episode_completion_ids = []
        episode_logprobs = []
        triage_rewards = []
        regimen_rewards = []
        risk_delta_rewards = []
        invalid_penalties = []
        final_score_rewards = []

        for prompt_text in prompts:
            episode = rollout_once(trainer=trainer, dataset_prompt=prompt_text)
            episode_prompt_ids.append(episode["prompt_ids"])
            episode_completion_ids.append(episode["completion_ids"])
            episode_logprobs.append(episode["logprobs"])
            triage_rewards.append(episode["triage_reward"])
            regimen_rewards.append(episode["regimen_reward"])
            risk_delta_rewards.append(episode["risk_delta_reward"])
            invalid_penalties.append(episode["invalid_penalty"])
            final_score_rewards.append(episode["final_score_reward"])

        return {
            "prompt_ids": episode_prompt_ids,
            "completion_ids": episode_completion_ids,
            "logprobs": episode_logprobs,
            "triage_reward": triage_rewards,
            "regimen_reward": regimen_rewards,
            "risk_delta_reward": risk_delta_rewards,
            "invalid_penalty": invalid_penalties,
            "final_score_reward": final_score_rewards,
        }

    def reward_triage(completions, **kwargs):  # type: ignore[no-untyped-def]
        rewards = kwargs.get("triage_reward")
        return [float(r) for r in rewards] if rewards else [0.0] * len(completions)

    def reward_regimen(completions, **kwargs):  # type: ignore[no-untyped-def]
        rewards = kwargs.get("regimen_reward")
        return [float(r) for r in rewards] if rewards else [0.0] * len(completions)

    def reward_risk_delta(completions, **kwargs):  # type: ignore[no-untyped-def]
        rewards = kwargs.get("risk_delta_reward")
        return [float(r) for r in rewards] if rewards else [0.0] * len(completions)

    def reward_invalid_penalty(completions, **kwargs):  # type: ignore[no-untyped-def]
        rewards = kwargs.get("invalid_penalty")
        return [float(r) for r in rewards] if rewards else [0.0] * len(completions)

    def reward_final_score(completions, **kwargs):  # type: ignore[no-untyped-def]
        rewards = kwargs.get("final_score_reward")
        return [float(r) for r in rewards] if rewards else [0.0] * len(completions)

    trainer = GRPOTrainer(
        model=model,
        processing_class=tokenizer,
        reward_funcs=[
            reward_triage,
            reward_regimen,
            reward_risk_delta,
            reward_invalid_penalty,
            reward_final_score,
        ],
        train_dataset=dataset,
        args=grpo_config,
        rollout_func=rollout_func,
    )

    try:
        stats = trainer.train()
        trainer.save_model(str(args.output_dir))
        tokenizer.save_pretrained(str(args.output_dir))

        (args.output_dir / "warmup_reward_trace.json").write_text(
            json.dumps({"warmup_rewards": reward_trace}, indent=2),
            encoding="utf-8",
        )
        (args.output_dir / "train_metrics.json").write_text(
            json.dumps(stats.metrics if hasattr(stats, "metrics") else {}, indent=2),
            encoding="utf-8",
        )
        print(f"Training complete. Artifacts saved to: {args.output_dir}")
    finally:
        env.close()


if __name__ == "__main__":
    main()

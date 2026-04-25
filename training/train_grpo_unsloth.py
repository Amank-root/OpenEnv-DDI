"""GRPO fine-tuning script for OpenEnv-DDI using TRL + Unsloth.

This training script follows the same staged flow as the sample notebook:
1) initialize environment
2) initialize model/tokenizer
3) define helper functions
4) define rollout function
5) define reward functions
6) create dataset
7) configure trainer
8) train and save artifacts
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Callable, Protocol

from datasets import Dataset, load_dataset
from transformers import AutoTokenizer

from client import DdiEnv
from inference import (
    SYSTEM_PROMPT,
    apply_action_guardrails,
    heuristic_action,
    observation_to_prompt,
    parse_action,
)
from models import DdiAction, DdiObservation
from server.ddi_environment import DdiEnvironment

DEFAULT_DATASET_PROMPT = "Perform safe DDI triage with strict JSON action output."
LORA_TARGET_MODULES = [
    "q_proj",
    "k_proj",
    "v_proj",
    "o_proj",
    "gate_proj",
    "up_proj",
    "down_proj",
]


class EnvAdapter(Protocol):
    def reset(self) -> DdiObservation:
        ...

    def step(self, action: DdiAction) -> DdiObservation:
        ...

    def close(self) -> None:
        ...


class LocalEnvAdapter:
    """Use in-process DDI environment for local GRPO rollouts."""

    def __init__(self, case_split: str, task_sampling: str) -> None:
        self._env = DdiEnvironment(case_split=case_split, task_sampling=task_sampling)

    def reset(self) -> DdiObservation:
        return self._env.reset()

    def step(self, action: DdiAction) -> DdiObservation:
        return self._env.step(action)

    def close(self) -> None:
        return None


class RemoteEnvAdapter:
    """Use deployed OpenEnv endpoint for GRPO rollouts."""

    def __init__(self, base_url: str) -> None:
        self._env = DdiEnv(base_url=base_url)

    def reset(self) -> DdiObservation:
        result = self._env.reset()
        return result.observation

    def step(self, action: DdiAction) -> DdiObservation:
        result = self._env.step(action)
        return result.observation

    def close(self) -> None:
        self._env.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fine-tune a DDI triage policy with GRPO (TRL + Unsloth)."
    )
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
    parser.add_argument(
        "--case_split",
        type=str,
        default="train",
        choices=["train", "validation"],
    )
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
        help="Optional deployed env URL (for example an HF Space URL).",
    )
    return parser.parse_args()


def create_environment(args: argparse.Namespace) -> EnvAdapter:
    if args.env_base_url:
        return RemoteEnvAdapter(args.env_base_url)
    return LocalEnvAdapter(args.case_split, args.task_sampling)


def initialize_model_and_tokenizer(args: argparse.Namespace, fast_language_model: Any):
    tokenizer = AutoTokenizer.from_pretrained(args.model_name, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model, _ = fast_language_model.from_pretrained(
        model_name=args.model_name,
        max_seq_length=args.max_seq_length,
        dtype=None,
        load_in_4bit=True,
    )
    model = fast_language_model.get_peft_model(
        model,
        r=args.lora_rank,
        lora_alpha=args.lora_alpha,
        lora_dropout=args.lora_dropout,
        target_modules=LORA_TARGET_MODULES,
        bias="none",
        use_gradient_checkpointing=True,
    )
    return model, tokenizer


def build_dataset(args: argparse.Namespace) -> Dataset:
    if args.sft_dataset.exists():
        ds = load_dataset("json", data_files=str(args.sft_dataset), split="train")
        if "messages" in ds.column_names:
            prompts: list[str] = []
            for row in ds:
                messages = row.get("messages") or []
                user_prompt = next(
                    (
                        message.get("content", "")
                        for message in messages
                        if message.get("role") == "user"
                    ),
                    DEFAULT_DATASET_PROMPT,
                )
                prompts.append(user_prompt)
            if prompts:
                return Dataset.from_dict({"prompt": prompts[: args.dataset_size]})

    return Dataset.from_dict(
        {"prompt": [DEFAULT_DATASET_PROMPT] * args.dataset_size}
    )


def make_user_prompt(dataset_prompt: str, observation: DdiObservation) -> str:
    env_prompt = observation_to_prompt(observation, history=[])
    base_instruction = dataset_prompt.strip() or DEFAULT_DATASET_PROMPT
    return (
        f"Task instruction:\n{base_instruction}\n\n"
        f"Current patient context:\n{env_prompt}\n\n"
        "Output exactly one JSON action object."
    )


def extract_component_reward(observation: DdiObservation) -> dict[str, float]:
    metadata = observation.metadata or {}
    components = metadata.get("reward_components", {})
    return {
        "triage_reward": float(components.get("triage_score", 0.0)),
        "regimen_reward": float(components.get("regimen_score", 0.0)),
        "risk_delta_reward": float(components.get("risk_delta_bonus", 0.0)),
        "invalid_penalty": float(components.get("invalid_action_penalty", 0.0)),
        "final_score_reward": float(observation.final_score or 0.0),
    }


def warmup_with_heuristic(env: EnvAdapter, warmup_steps: int) -> list[float]:
    observation = env.reset()
    reward_trace: list[float] = []
    decided_interactions: set[str] = set()
    suggested_regimens: set[str] = set()

    for _ in range(max(1, warmup_steps)):
        payload = heuristic_action(
            observation,
            decided_interactions=decided_interactions,
            suggested_regimens=suggested_regimens,
        )
        payload = apply_action_guardrails(
            payload,
            observation,
            decided_interactions=decided_interactions,
            suggested_regimens=suggested_regimens,
        )

        action = DdiAction(**payload)
        if action.interaction_id:
            decided_interactions.add(action.interaction_id)
        if action.suggested_regimen_id:
            suggested_regimens.add(action.suggested_regimen_id)

        observation = env.step(action)
        reward_trace.append(float(observation.reward or 0.0))

        if observation.done:
            observation = env.reset()
            decided_interactions.clear()
            suggested_regimens.clear()

    return reward_trace


def rollout_once(
    *,
    trainer: Any,
    env: EnvAdapter,
    tokenizer: Any,
    dataset_prompt: str,
    max_turns: int,
    generate_rollout_completions: Callable[..., Any],
) -> dict[str, Any]:
    observation = env.reset()

    prompt_ids: list[int] = []
    completion_ids: list[int] = []
    logprobs: list[float] = []

    triage_rewards: list[float] = []
    regimen_rewards: list[float] = []
    risk_delta_rewards: list[float] = []
    invalid_penalties: list[float] = []
    final_score_rewards: list[float] = []

    decided_interactions: set[str] = set()
    suggested_regimens: set[str] = set()

    for _ in range(max_turns):
        if observation.done:
            break

        user_prompt = make_user_prompt(dataset_prompt, observation)
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

        completion_text = rollout_outputs.get("text")
        if not completion_text:
            completion_text = tokenizer.decode(
                rollout_outputs.get("completion_ids", []),
                skip_special_tokens=True,
            )

        raw_payload = parse_action(completion_text, observation)
        payload = apply_action_guardrails(
            raw_payload,
            observation,
            decided_interactions=decided_interactions,
            suggested_regimens=suggested_regimens,
        )

        action = DdiAction(**payload)
        if action.interaction_id:
            decided_interactions.add(action.interaction_id)
        if action.suggested_regimen_id:
            suggested_regimens.add(action.suggested_regimen_id)

        observation = env.step(action)
        component_reward = extract_component_reward(observation)

        triage_rewards.append(component_reward["triage_reward"])
        regimen_rewards.append(component_reward["regimen_reward"])
        risk_delta_rewards.append(component_reward["risk_delta_reward"])
        invalid_penalties.append(component_reward["invalid_penalty"])
        final_score_rewards.append(component_reward["final_score_reward"])

    return {
        "prompt_ids": prompt_ids,
        "completion_ids": completion_ids,
        "logprobs": logprobs,
        "triage_reward": triage_rewards[-1] if triage_rewards else 0.0,
        "regimen_reward": regimen_rewards[-1] if regimen_rewards else 0.0,
        "risk_delta_reward": risk_delta_rewards[-1] if risk_delta_rewards else 0.0,
        "invalid_penalty": invalid_penalties[-1] if invalid_penalties else 0.0,
        "final_score_reward": final_score_rewards[-1] if final_score_rewards else 0.0,
    }


def build_rollout_func(
    *,
    env: EnvAdapter,
    tokenizer: Any,
    max_turns: int,
    generate_rollout_completions: Callable[..., Any],
):
    def rollout_func(prompts, trainer=None):  # type: ignore[no-untyped-def]
        if trainer is None:
            raise RuntimeError("GRPO rollout_func received no trainer instance.")

        episode_prompt_ids = []
        episode_completion_ids = []
        episode_logprobs = []
        triage_rewards = []
        regimen_rewards = []
        risk_delta_rewards = []
        invalid_penalties = []
        final_score_rewards = []

        for dataset_prompt in prompts:
            episode = rollout_once(
                trainer=trainer,
                env=env,
                tokenizer=tokenizer,
                dataset_prompt=dataset_prompt,
                max_turns=max_turns,
                generate_rollout_completions=generate_rollout_completions,
            )

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

    return rollout_func


def _reward_vector(reward_key: str, completions: list[Any], kwargs: dict[str, Any]) -> list[float]:
    rewards = kwargs.get(reward_key)
    if rewards:
        return [float(r) for r in rewards]
    return [0.0] * len(completions)


def reward_triage(completions, **kwargs):  # type: ignore[no-untyped-def]
    return _reward_vector("triage_reward", completions, kwargs)


def reward_regimen(completions, **kwargs):  # type: ignore[no-untyped-def]
    return _reward_vector("regimen_reward", completions, kwargs)


def reward_risk_delta(completions, **kwargs):  # type: ignore[no-untyped-def]
    return _reward_vector("risk_delta_reward", completions, kwargs)


def reward_invalid_penalty(completions, **kwargs):  # type: ignore[no-untyped-def]
    return _reward_vector("invalid_penalty", completions, kwargs)


def reward_final_score(completions, **kwargs):  # type: ignore[no-untyped-def]
    return _reward_vector("final_score_reward", completions, kwargs)


def build_grpo_config(args: argparse.Namespace, grpo_config_cls: Any):
    return grpo_config_cls(
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


def save_artifacts(
    *,
    output_dir: Path,
    trainer: Any,
    tokenizer: Any,
    stats: Any,
    warmup_reward_trace: list[float],
) -> None:
    trainer.save_model(str(output_dir))
    tokenizer.save_pretrained(str(output_dir))

    (output_dir / "warmup_reward_trace.json").write_text(
        json.dumps({"warmup_rewards": warmup_reward_trace}, indent=2),
        encoding="utf-8",
    )

    metrics = stats.metrics if hasattr(stats, "metrics") else {}
    (output_dir / "train_metrics.json").write_text(
        json.dumps(metrics, indent=2),
        encoding="utf-8",
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

    model, tokenizer = initialize_model_and_tokenizer(args, FastLanguageModel)
    env = create_environment(args)

    warmup_reward_trace = warmup_with_heuristic(env, args.warmup_steps)
    dataset = build_dataset(args)

    rollout_func = build_rollout_func(
        env=env,
        tokenizer=tokenizer,
        max_turns=args.max_turns,
        generate_rollout_completions=generate_rollout_completions,
    )

    grpo_config = build_grpo_config(args, GRPOConfig)

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
        save_artifacts(
            output_dir=args.output_dir,
            trainer=trainer,
            tokenizer=tokenizer,
            stats=stats,
            warmup_reward_trace=warmup_reward_trace,
        )
        print(f"Training complete. Artifacts saved to: {args.output_dir}")
    finally:
        env.close()


if __name__ == "__main__":
    main()

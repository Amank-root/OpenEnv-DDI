"""Minimal TRL + Unsloth GRPO training entrypoint for T4-budget experiments."""

from __future__ import annotations

import argparse
from pathlib import Path
import random

from datasets import load_dataset

from models import DdiAction
from server.ddi_environment import DdiEnvironment


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name", type=str, default="Qwen/Qwen2.5-14B-Instruct")
    parser.add_argument("--sft_dataset", type=Path, default=Path("training/data/sft_warmstart_train.jsonl"))
    parser.add_argument("--output_dir", type=Path, default=Path("training/outputs/qwen25-14b-ddi-grpo"))
    parser.add_argument("--warmup_steps", type=int, default=40)
    parser.add_argument("--train_steps", type=int, default=120)
    parser.add_argument("--case_split", type=str, default="train", choices=["train", "validation"])
    return parser.parse_args()


def _sample_action(observation) -> DdiAction:
    # Placeholder policy action for smoke-run reward function integration.
    unresolved = list(observation.metadata.get("unresolved_interaction_ids", []))
    if unresolved:
        return DdiAction(
            action_type="flag_interaction",
            interaction_id=unresolved[0],
            rationale="grpo_sample",
        )
    if observation.task_level == "hard":
        pending = list(observation.metadata.get("remaining_required_regimens", []))
        if pending:
            return DdiAction(
                action_type="suggest_alternative",
                suggested_regimen_id=pending[0],
                rationale="grpo_sample",
            )
    return DdiAction(action_type="finish", rationale="grpo_sample")


def _reward_from_observation(observation) -> float:
    components = observation.metadata.get("reward_components", {})
    triage = float(components.get("triage_score", 0.0))
    regimen = float(components.get("regimen_score", 0.0))
    risk_delta = float(components.get("risk_delta_bonus", 0.0))
    invalid = float(components.get("invalid_action_penalty", 0.0))
    return triage + regimen + risk_delta + invalid


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    try:
        from unsloth import FastLanguageModel  # type: ignore
        from trl import GRPOConfig, GRPOTrainer  # type: ignore
    except Exception as exc:  # pragma: no cover - dependency guidance
        raise RuntimeError(
            "Training deps missing. Install with: uv pip install -e .[train]"
        ) from exc

    # Load SFT warm-start examples (not fully consumed in this minimal script).
    if args.sft_dataset.exists():
        _ = load_dataset("json", data_files=str(args.sft_dataset), split="train")

    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=args.model_name,
        max_seq_length=2048,
        dtype=None,
        load_in_4bit=True,
    )
    model = FastLanguageModel.get_peft_model(
        model,
        r=16,
        lora_alpha=32,
        lora_dropout=0.05,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
        bias="none",
        use_gradient_checkpointing=True,
    )

    env = DdiEnvironment(case_split=args.case_split, task_sampling="mixed_seeded")
    random.seed(17)

    # Smoke-run reward traces used as a tiny training bootstrap artifact.
    reward_trace: list[float] = []
    obs = env.reset()
    for step_idx in range(max(1, args.warmup_steps)):
        action = _sample_action(obs)
        obs = env.step(action)
        reward_trace.append(_reward_from_observation(obs))
        if obs.done:
            obs = env.reset()
        if step_idx >= args.train_steps:
            break

    config = GRPOConfig(
        output_dir=str(args.output_dir),
        learning_rate=2e-5,
        per_device_train_batch_size=1,
        gradient_accumulation_steps=8,
        max_steps=args.train_steps,
        logging_steps=10,
        save_steps=max(20, args.train_steps // 3),
        bf16=False,
        fp16=True,
    )

    trainer = GRPOTrainer(
        model=model,
        args=config,
        processing_class=tokenizer,
        train_dataset=[{"prompt": "ddi triage", "completion": "finish"}] * 8,
    )
    trainer.train()

    model.save_pretrained(str(args.output_dir / "adapters"))
    tokenizer.save_pretrained(str(args.output_dir / "adapters"))
    with (args.output_dir / "reward_trace.txt").open("w", encoding="utf-8") as handle:
        handle.write("\n".join(f"{idx},{val:.4f}" for idx, val in enumerate(reward_trace)))

    print(f"Saved adapters and reward trace to {args.output_dir}")


if __name__ == "__main__":
    main()

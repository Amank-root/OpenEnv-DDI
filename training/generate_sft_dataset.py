"""Generate a small SFT warm-start dataset from the deterministic heuristic policy."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from models import DdiAction, DdiObservation
from server.ddi_environment import DdiEnvironment

try:
    from inference import apply_action_guardrails, heuristic_action, observation_to_prompt
except ImportError as exc:  # pragma: no cover - defensive import guard
    raise RuntimeError("Unable to import helper functions from inference.py") from exc


def _to_record(observation: DdiObservation, action: dict[str, Any]) -> dict[str, Any]:
    return {
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a clinical medication safety triage assistant. "
                    "Return one JSON object with action_type, interaction_id, "
                    "suggested_regimen_id, rationale."
                ),
            },
            {"role": "user", "content": observation_to_prompt(observation, history=[])},
            {"role": "assistant", "content": json.dumps(action, ensure_ascii=True)},
        ],
        "task_level": observation.task_level,
        "patient_id": observation.patient_id,
    }


def generate_records(episodes: int, split: str) -> list[dict[str, Any]]:
    env = DdiEnvironment(case_split=split, task_sampling="mixed_seeded")
    records: list[dict[str, Any]] = []

    for _ in range(max(1, episodes)):
        obs = env.reset()
        done = False
        guard_decided: set[str] = set()
        guard_suggested: set[str] = set()

        while not done:
            raw_action = heuristic_action(
                obs,
                decided_interactions=guard_decided,
                suggested_regimens=guard_suggested,
            )
            action_payload = apply_action_guardrails(
                raw_action,
                obs,
                decided_interactions=guard_decided,
                suggested_regimens=guard_suggested,
            )
            records.append(_to_record(obs, action_payload))

            action = DdiAction(**action_payload)
            if action.interaction_id:
                guard_decided.add(action.interaction_id)
            if action.suggested_regimen_id:
                guard_suggested.add(action.suggested_regimen_id)

            obs = env.step(action)
            done = bool(obs.done)

    return records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--episodes", type=int, default=48)
    parser.add_argument("--split", type=str, default="train", choices=["train", "validation"])
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("training/data/sft_warmstart_train.jsonl"),
    )
    args = parser.parse_args()

    records = generate_records(episodes=args.episodes, split=args.split)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8") as handle:
        for row in records:
            handle.write(json.dumps(row, ensure_ascii=True) + "\n")

    print(
        f"Wrote {len(records)} records to {args.out} "
        f"(episodes={args.episodes}, split={args.split})"
    )


if __name__ == "__main__":
    main()

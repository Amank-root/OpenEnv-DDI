"""Build baseline-vs-policy demo artifacts with reward curves and transcripts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import mean

from models import DdiAction
from server.ddi_environment import DdiEnvironment
from inference import heuristic_action


def random_policy(observation):
    unresolved = observation.metadata.get("unresolved_interaction_ids", [])
    if unresolved:
        return DdiAction(
            action_type="monitor",
            interaction_id=unresolved[0],
            rationale="baseline_monitor_only",
        )
    return DdiAction(action_type="finish", rationale="baseline_finish")


def heuristic_policy(observation):
    payload = heuristic_action(observation)
    return DdiAction(**payload)


def run_episodes(policy_name: str, episodes: int, split: str):
    env = DdiEnvironment(case_split=split, task_sampling="mixed_seeded")
    curve: list[float] = []
    transcripts: list[dict] = []

    for episode_idx in range(episodes):
        obs = env.reset()
        done = False
        rewards = []
        action_log = []
        while not done:
            action = random_policy(obs) if policy_name == "baseline" else heuristic_policy(obs)
            obs = env.step(action)
            rewards.append(float(obs.reward or 0.0))
            action_log.append(
                {
                    "action_type": action.action_type,
                    "interaction_id": action.interaction_id,
                    "suggested_regimen_id": action.suggested_regimen_id,
                    "reward": float(obs.reward or 0.0),
                    "done": bool(obs.done),
                }
            )
            done = bool(obs.done)

        curve.append(sum(rewards))
        transcripts.append(
            {
                "episode": episode_idx,
                "task_level": obs.task_level,
                "patient_id": obs.patient_id,
                "final_score": float(obs.final_score or 0.0),
                "episode_reward": sum(rewards),
                "actions": action_log,
            }
        )
    return curve, transcripts


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--episodes", type=int, default=18)
    parser.add_argument("--split", type=str, default="validation", choices=["train", "validation", "all"])
    parser.add_argument("--out_dir", type=Path, default=Path("training/demo_artifacts"))
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    baseline_curve, baseline_transcripts = run_episodes("baseline", args.episodes, args.split)
    trained_curve, trained_transcripts = run_episodes("trained", args.episodes, args.split)

    summary = {
        "split": args.split,
        "episodes": args.episodes,
        "baseline_reward_mean": mean(baseline_curve),
        "trained_reward_mean": mean(trained_curve),
        "baseline_curve": baseline_curve,
        "trained_curve": trained_curve,
    }

    (args.out_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    (args.out_dir / "baseline_transcripts.json").write_text(
        json.dumps(baseline_transcripts, indent=2), encoding="utf-8"
    )
    (args.out_dir / "trained_transcripts.json").write_text(
        json.dumps(trained_transcripts, indent=2), encoding="utf-8"
    )
    print(f"Wrote demo artifacts to {args.out_dir}")


if __name__ == "__main__":
    main()

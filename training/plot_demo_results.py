"""Render judge-friendly PNG plots from demo artifacts summary.json."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--summary",
        type=Path,
        default=Path("training/demo_artifacts/summary.json"),
    )
    parser.add_argument(
        "--out_dir",
        type=Path,
        default=Path("assets/plots"),
    )
    args = parser.parse_args()

    try:
        import matplotlib.pyplot as plt  # type: ignore
    except Exception as exc:  # pragma: no cover
        raise RuntimeError(
            "matplotlib is required for plotting. Install with: uv pip install matplotlib"
        ) from exc

    if not args.summary.exists():
        raise FileNotFoundError(
            f"Missing summary file at {args.summary}. "
            "Run: python training/build_demo_artifacts.py"
        )

    summary = json.loads(args.summary.read_text(encoding="utf-8"))
    args.out_dir.mkdir(parents=True, exist_ok=True)

    baseline_curve = summary.get("baseline_curve", [])
    trained_curve = summary.get("trained_curve", [])
    baseline_score_curve = summary.get("baseline_score_curve", [])
    trained_score_curve = summary.get("trained_score_curve", [])
    baseline_invalid_curve = summary.get("baseline_invalid_action_rate_curve", [])
    trained_invalid_curve = summary.get("trained_invalid_action_rate_curve", [])

    episodes = list(range(1, max(len(baseline_curve), len(trained_curve)) + 1))

    # Plot 1: Episode reward curve
    plt.figure(figsize=(9, 5))
    plt.plot(episodes[: len(baseline_curve)], baseline_curve, label="Baseline", marker="o")
    plt.plot(episodes[: len(trained_curve)], trained_curve, label="Trained", marker="o")
    plt.title("Baseline vs Trained Episode Reward")
    plt.xlabel("Episode")
    plt.ylabel("Total Episode Reward")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(args.out_dir / "reward_curve.png", dpi=180)
    plt.close()

    # Plot 2: Final score curve
    plt.figure(figsize=(9, 5))
    plt.plot(
        episodes[: len(baseline_score_curve)],
        baseline_score_curve,
        label="Baseline",
        marker="o",
    )
    plt.plot(
        episodes[: len(trained_score_curve)],
        trained_score_curve,
        label="Trained",
        marker="o",
    )
    plt.title("Baseline vs Trained Final Score")
    plt.xlabel("Episode")
    plt.ylabel("Final Score (0-1)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(args.out_dir / "baseline_vs_trained.png", dpi=180)
    plt.close()

    # Plot 3: Invalid-action rate (proxy safety metric)
    plt.figure(figsize=(9, 5))
    plt.plot(
        episodes[: len(baseline_invalid_curve)],
        baseline_invalid_curve,
        label="Baseline",
        marker="o",
    )
    plt.plot(
        episodes[: len(trained_invalid_curve)],
        trained_invalid_curve,
        label="Trained",
        marker="o",
    )
    plt.title("Invalid Action Rate per Episode")
    plt.xlabel("Episode")
    plt.ylabel("Invalid Action Rate")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(args.out_dir / "invalid_action_rate.png", dpi=180)
    plt.close()

    print(f"Wrote plots to {args.out_dir}")


if __name__ == "__main__":
    main()

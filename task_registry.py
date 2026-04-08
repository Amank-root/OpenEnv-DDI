"""Task configuration registry for DDI triage environment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class TaskConfig:
    level: str
    title: str
    objective: str
    step_budget: int
    grader_name: str
    positive_reward_scale: float
    penalty_reward_scale: float


TASK_CONFIGS: Dict[str, TaskConfig] = {
    "easy": TaskConfig(
        level="easy",
        title="Severe DDI detection in 5-drug profile",
        objective="Flag severe (contraindicated/major) interactions in a short medication list.",
        step_budget=8,
        grader_name="grade_easy",
        positive_reward_scale=0.9,
        penalty_reward_scale=0.85,
    ),
    "medium": TaskConfig(
        level="medium",
        title="Risk-prioritized triage with patient context",
        objective="Prioritize interactions by severity with age/renal-risk modifiers and choose flag/monitor/ignore.",
        step_budget=12,
        grader_name="grade_medium",
        positive_reward_scale=1.0,
        penalty_reward_scale=1.0,
    ),
    "hard": TaskConfig(
        level="hard",
        title="Deprescribing-aware risk minimization",
        objective="Triages interactions and suggests alternatives that reduce risk while preserving treatment intent.",
        step_budget=16,
        grader_name="grade_hard",
        positive_reward_scale=1.1,
        penalty_reward_scale=1.15,
    ),
}

TASK_ORDER = ["easy", "medium", "hard"]

"""Deterministic synthetic DDI datasets for polypharmacy triage tasks."""

from __future__ import annotations

from typing import Dict, List

SEVERITY_WEIGHTS: Dict[str, float] = {
    "contraindicated": 1.0,
    "major": 0.8,
    "moderate": 0.45,
    "minor": 0.2,
}

INTERACTION_RECOMMENDATIONS: Dict[str, str] = {
    "contraindicated": "flag_interaction",
    "major": "flag_interaction",
    "moderate": "monitor",
    "minor": "ignore",
}

try:
    from .task_cases import EASY_CASES, HARD_CASES, MEDIUM_CASES
except ImportError:
    from task_cases import EASY_CASES, HARD_CASES, MEDIUM_CASES

TASK_CASES: Dict[str, List[Dict]] = {
    "easy": EASY_CASES,
    "medium": MEDIUM_CASES,
    "hard": HARD_CASES,
}

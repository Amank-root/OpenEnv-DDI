"""Deterministic synthetic DDI datasets for polypharmacy triage tasks."""

from __future__ import annotations

from typing import Dict, List, Literal

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

CaseSplit = Literal["train", "validation", "all"]


def case_split(case: Dict) -> str:
    """Return case split assignment; defaults to train for backward compatibility."""
    return str(case.get("split", "train"))


def case_template_family(case: Dict) -> str:
    """Return stable template family key used to prevent train/validation leakage."""
    case_id = str(case.get("case_id", "unknown"))
    return str(case.get("template_family", f"legacy::{case_id}"))


def get_task_cases(split: CaseSplit = "all") -> Dict[str, List[Dict]]:
    """Get task cases for a specific split while preserving deterministic order."""
    if split not in {"train", "validation", "all"}:
        raise ValueError(f"Unsupported split '{split}'. Use train, validation, or all.")

    if split == "all":
        return {level: list(cases) for level, cases in TASK_CASES.items()}

    return {
        level: [case for case in cases if case_split(case) == split]
        for level, cases in TASK_CASES.items()
    }


def _assert_split_leakage_free() -> None:
    """Verify template families do not overlap between train and validation sets."""
    train_cases = get_task_cases("train")
    validation_cases = get_task_cases("validation")

    for level in TASK_CASES:
        train_families = {case_template_family(case) for case in train_cases[level]}
        validation_families = {
            case_template_family(case) for case in validation_cases[level]
        }
        overlap = train_families & validation_families
        if overlap:
            overlap_joined = ", ".join(sorted(overlap))
            raise ValueError(
                f"Template-family leakage detected for level={level}: {overlap_joined}"
            )


_assert_split_leakage_free()

TRAIN_TASK_CASES = get_task_cases("train")
VALIDATION_TASK_CASES = get_task_cases("validation")

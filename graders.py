"""Deterministic graders for DDI triage tasks."""

from __future__ import annotations

from typing import Callable, Dict, Iterable, Set


# Scores must be strictly within (0, 1) for submission evaluation.
SCORE_EPSILON = 1e-3


def _strict_unit_interval(value: float) -> float:
    return min(1.0 - SCORE_EPSILON, max(SCORE_EPSILON, value))

try:
    from .ddi_data import INTERACTION_RECOMMENDATIONS, SEVERITY_WEIGHTS
except ImportError:
    from ddi_data import INTERACTION_RECOMMENDATIONS, SEVERITY_WEIGHTS


def expected_decision(interaction: Dict, patient: Dict, task_level: str) -> str:
    """Return the expected triage decision for a DDI candidate."""
    severity = interaction["severity"]
    default_decision = INTERACTION_RECOMMENDATIONS[severity]

    if task_level == "easy":
        return default_decision

    if task_level in {"medium", "hard"}:
        age = patient["age"]
        egfr = patient["labs"].get("egfr", 90.0)
        alt = patient["labs"].get("alt", 30.0)
        ast = patient["labs"].get("ast", 30.0)
        hepatic_stress = alt >= 120 or ast >= 120
        if severity == "moderate" and (age >= 80 or egfr < 45 or hepatic_stress):
            return "flag_interaction"
        if severity == "minor" and (age >= 85 or egfr < 30 or alt >= 150):
            return "monitor"
        return default_decision

    return default_decision


def interaction_criticality(interaction: Dict, patient: Dict, task_level: str) -> float:
    """Compute deterministic criticality weight for an interaction."""
    base = SEVERITY_WEIGHTS[interaction["severity"]]
    if task_level == "easy":
        return base

    age = patient["age"]
    egfr = patient["labs"].get("egfr", 90.0)
    alt = patient["labs"].get("alt", 30.0)
    ast = patient["labs"].get("ast", 30.0)
    age_factor = 0.2 if age >= 80 else 0.0
    renal_factor = 0.25 if egfr < 45 else 0.0
    hepatic_factor = 0.2 if (alt >= 120 or ast >= 120) else 0.0
    return min(1.2, base + age_factor + renal_factor + hepatic_factor)


def score_interaction_decisions(
    *,
    interactions: Iterable[Dict],
    decisions: Dict[str, str],
    patient: Dict,
    task_level: str,
) -> float:
    """Score interaction decisions and normalize to 0..1."""
    total_possible = 0.0
    score = 0.0

    for interaction in interactions:
        interaction_id = interaction["interaction_id"]
        expected = expected_decision(interaction, patient, task_level)
        decision = decisions.get(interaction_id)
        weight = interaction_criticality(interaction, patient, task_level)

        total_possible += weight

        if decision is None:
            if expected == "flag_interaction":
                score -= 0.6 * weight
            else:
                score -= 0.2 * weight
            continue

        if decision == expected:
            score += weight
            continue

        if expected == "flag_interaction" and decision in {"monitor", "ignore"}:
            score -= 0.7 * weight
        elif decision == "flag_interaction" and expected != "flag_interaction":
            score -= 0.45 * weight
        else:
            score -= 0.25 * weight

    if total_possible <= 0:
        return SCORE_EPSILON

    normalized = (score / total_possible + 1.0) / 2.0
    return _strict_unit_interval(normalized)


def score_regimen_suggestions(required_regimens: Iterable[str], suggested: Set[str]) -> float:
    """Score suggested alternatives against required regimen IDs."""
    req = list(required_regimens)
    if not req:
        return 1.0 - SCORE_EPSILON

    matched = sum(1 for regimen_id in req if regimen_id in suggested)
    missed = len(req) - matched
    overcalls = max(0, len(suggested) - matched)

    raw = (matched - 0.5 * missed - 0.2 * overcalls) / len(req)
    return _strict_unit_interval(raw)


def grade_easy(*, interactions: Iterable[Dict], decisions: Dict[str, str], patient: Dict) -> float:
    return score_interaction_decisions(
        interactions=interactions,
        decisions=decisions,
        patient=patient,
        task_level="easy",
    )


def grade_medium(*, interactions: Iterable[Dict], decisions: Dict[str, str], patient: Dict) -> float:
    return score_interaction_decisions(
        interactions=interactions,
        decisions=decisions,
        patient=patient,
        task_level="medium",
    )


def grade_hard(
    *,
    interactions: Iterable[Dict],
    decisions: Dict[str, str],
    patient: Dict,
    required_regimens: Iterable[str],
    suggested_regimens: Set[str],
) -> float:
    interaction_score = score_interaction_decisions(
        interactions=interactions,
        decisions=decisions,
        patient=patient,
        task_level="hard",
    )
    regimen_score = score_regimen_suggestions(required_regimens, suggested_regimens)
    combined = 0.7 * interaction_score + 0.3 * regimen_score
    return _strict_unit_interval(combined)


# Explicit task->grader registry used by environment and validation checks.
TASK_GRADERS: Dict[str, Callable[..., float]] = {
    "easy": grade_easy,
    "medium": grade_medium,
    "hard": grade_hard,
}


def grade_task(task_level: str, **kwargs) -> float:
    """Route scoring to the registered grader for a task level."""
    grader = TASK_GRADERS.get(task_level)
    if grader is None:
        raise ValueError(f"No grader registered for task level: {task_level}")
    return grader(**kwargs)

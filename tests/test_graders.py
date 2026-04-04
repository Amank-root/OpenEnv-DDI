"""Tests for deterministic grader outputs."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

try:
    from ddi_data import TASK_CASES  # type: ignore[import-not-found]
    from graders import (  # type: ignore[import-not-found]
        expected_decision,
        grade_easy,
        grade_hard,
        grade_medium,
        score_regimen_suggestions,
    )
except ImportError:
    from ddi.ddi_data import TASK_CASES  # type: ignore[import-not-found]
    from ddi.graders import (  # type: ignore[import-not-found]
        expected_decision,
        grade_easy,
        grade_hard,
        grade_medium,
        score_regimen_suggestions,
    )


def test_grade_ranges() -> None:
    easy_case = TASK_CASES["easy"][0]
    medium_case = TASK_CASES["medium"][0]
    hard_case = TASK_CASES["hard"][0]

    easy_score = grade_easy(
        interactions=easy_case["interactions"],
        decisions={"INT-E1": "flag_interaction"},
        patient=easy_case,
    )
    medium_score = grade_medium(
        interactions=medium_case["interactions"],
        decisions={"INT-M1": "flag_interaction", "INT-M2": "monitor"},
        patient=medium_case,
    )
    hard_score = grade_hard(
        interactions=hard_case["interactions"],
        decisions={"INT-H1": "flag_interaction"},
        patient=hard_case,
        required_regimens=hard_case["required_regimens"],
        suggested_regimens={"REG-H1"},
    )

    assert 0.0 <= easy_score <= 1.0
    assert 0.0 <= medium_score <= 1.0
    assert 0.0 <= hard_score <= 1.0


def test_grade_determinism() -> None:
    hard_case = TASK_CASES["hard"][0]
    decisions = {
        "INT-H1": "flag_interaction",
        "INT-H2": "flag_interaction",
        "INT-H3": "monitor",
        "INT-H4": "flag_interaction",
        "INT-H5": "flag_interaction",
    }
    suggested = {"REG-H1", "REG-H2", "REG-H3"}

    score_1 = grade_hard(
        interactions=hard_case["interactions"],
        decisions=decisions,
        patient=hard_case,
        required_regimens=hard_case["required_regimens"],
        suggested_regimens=suggested,
    )
    score_2 = grade_hard(
        interactions=hard_case["interactions"],
        decisions=decisions,
        patient=hard_case,
        required_regimens=hard_case["required_regimens"],
        suggested_regimens=suggested,
    )

    assert score_1 == score_2


def test_missing_decisions_are_penalized() -> None:
    easy_case = TASK_CASES["easy"][0]

    score_no_decisions = grade_easy(
        interactions=easy_case["interactions"],
        decisions={},
        patient=easy_case,
    )
    score_partial = grade_easy(
        interactions=easy_case["interactions"],
        decisions={"INT-E1": "flag_interaction"},
        patient=easy_case,
    )

    assert score_no_decisions < score_partial
    assert score_no_decisions < 0.5


def test_case_pool_size_per_level() -> None:
    assert len(TASK_CASES["easy"]) >= 6
    assert len(TASK_CASES["medium"]) >= 6
    assert len(TASK_CASES["hard"]) >= 6


def test_moderate_threshold_behavior_medium() -> None:
    interaction = {"severity": "moderate"}

    patient_baseline = {"age": 79, "labs": {"egfr": 45.0}}
    patient_age_trigger = {"age": 80, "labs": {"egfr": 45.0}}
    patient_renal_trigger = {"age": 79, "labs": {"egfr": 44.0}}

    assert expected_decision(interaction, patient_baseline, "medium") == "monitor"
    assert (
        expected_decision(interaction, patient_age_trigger, "medium")
        == "flag_interaction"
    )
    assert (
        expected_decision(interaction, patient_renal_trigger, "medium")
        == "flag_interaction"
    )


def test_minor_escalation_in_high_risk_medium() -> None:
    interaction = {"severity": "minor"}

    patient_lower_risk = {"age": 84, "labs": {"egfr": 30.0}}
    patient_higher_risk = {"age": 86, "labs": {"egfr": 29.0}}

    assert expected_decision(interaction, patient_lower_risk, "medium") == "ignore"
    assert expected_decision(interaction, patient_higher_risk, "medium") == "monitor"


def test_over_suggestion_penalized() -> None:
    required = ["REG-1", "REG-2", "REG-3"]

    score_exact = score_regimen_suggestions(required, {"REG-1", "REG-2", "REG-3"})
    score_over = score_regimen_suggestions(
        required, {"REG-1", "REG-2", "REG-3", "REG-4"}
    )

    assert score_exact > score_over

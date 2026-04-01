"""Tests for deterministic grader outputs."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

try:
    from ddi.ddi_data import TASK_CASES
    from ddi.graders import grade_easy, grade_hard, grade_medium
except ImportError:
    from ddi_data import TASK_CASES
    from graders import grade_easy, grade_hard, grade_medium


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

"""Accuracy-oriented behavioral tests for DDI environment scoring and rewards."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

try:
    from models import DdiAction  # type: ignore[import-not-found]
    from server.ddi_environment import DdiEnvironment  # type: ignore[import-not-found]
except ImportError:
    from ddi import DdiAction  # type: ignore[import-not-found]
    from ddi.server.ddi_environment import DdiEnvironment  # type: ignore[import-not-found]


def test_easy_perfect_policy_scores_high() -> None:
    env = DdiEnvironment()
    env.reset()

    env.step(DdiAction(action_type="flag_interaction", interaction_id="INT-E1", rationale="critical"))
    env.step(DdiAction(action_type="flag_interaction", interaction_id="INT-E2", rationale="major"))
    final = env.step(DdiAction(action_type="monitor", interaction_id="INT-E3", rationale="moderate"))

    assert final.done is True
    assert final.final_score is not None
    assert final.final_score >= 0.95


def test_easy_consistently_wrong_policy_scores_low() -> None:
    env = DdiEnvironment()
    env.reset()

    env.step(DdiAction(action_type="ignore", interaction_id="INT-E1", rationale="wrong"))
    env.step(DdiAction(action_type="ignore", interaction_id="INT-E2", rationale="wrong"))
    final = env.step(DdiAction(action_type="ignore", interaction_id="INT-E3", rationale="wrong"))

    assert final.done is True
    assert final.final_score is not None
    assert final.final_score <= 0.35


def test_hard_requires_regimen_suggestions_before_auto_finish() -> None:
    env = DdiEnvironment()
    env.reset()  # easy
    env.reset()  # medium
    hard_obs = env.reset()  # hard
    assert hard_obs.task_level == "hard"

    # In hard mode for this case, all moderate interactions become flag_interaction
    after_triage = env.step(
        DdiAction(action_type="flag_interaction", interaction_id="INT-H1", rationale="critical")
    )
    after_triage = env.step(
        DdiAction(action_type="flag_interaction", interaction_id="INT-H2", rationale="major")
    )
    after_triage = env.step(
        DdiAction(action_type="flag_interaction", interaction_id="INT-H3", rationale="risk-amplified")
    )
    after_triage = env.step(
        DdiAction(action_type="flag_interaction", interaction_id="INT-H4", rationale="risk-amplified")
    )
    after_triage = env.step(
        DdiAction(action_type="flag_interaction", interaction_id="INT-H5", rationale="major")
    )

    assert after_triage.done is False

    env.step(DdiAction(action_type="suggest_alternative", suggested_regimen_id="REG-H1", rationale="required"))
    env.step(DdiAction(action_type="suggest_alternative", suggested_regimen_id="REG-H2", rationale="required"))
    final = env.step(
        DdiAction(action_type="suggest_alternative", suggested_regimen_id="REG-H3", rationale="required")
    )

    assert final.done is True
    assert final.final_score is not None
    assert final.final_score >= 0.9


def test_reward_directionality_for_easy_critical_vs_wrong_actions() -> None:
    env_good = DdiEnvironment()
    env_good.reset()
    good = env_good.step(
        DdiAction(action_type="flag_interaction", interaction_id="INT-E1", rationale="critical")
    )

    env_false_positive = DdiEnvironment()
    env_false_positive.reset()
    false_positive = env_false_positive.step(
        DdiAction(action_type="flag_interaction", interaction_id="INT-E3", rationale="incorrectly critical")
    )

    env_missed_critical = DdiEnvironment()
    env_missed_critical.reset()
    missed_critical = env_missed_critical.step(
        DdiAction(action_type="ignore", interaction_id="INT-E1", rationale="missed")
    )

    assert good.reward is not None
    assert false_positive.reward is not None
    assert missed_critical.reward is not None
    assert good.reward > false_positive.reward
    assert false_positive.reward > missed_critical.reward

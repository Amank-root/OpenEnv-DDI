"""Tests for deterministic DDI environment behavior."""

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


def test_task_cycle_order() -> None:
    env = DdiEnvironment()

    levels = []
    for _ in range(3):
        obs = env.reset()
        levels.append(obs.task_level)

    assert levels == ["easy", "medium", "hard"]


def test_final_score_bounded() -> None:
    env = DdiEnvironment()
    env.reset()

    result = env.step(DdiAction(action_type="finish", rationale="done"))

    assert result.done is True
    assert result.final_score is not None
    assert 0.0 <= result.final_score <= 1.0


def test_premature_finish_is_penalized() -> None:
    env = DdiEnvironment()
    env.reset()

    result = env.step(DdiAction(action_type="finish", rationale="early exit"))

    assert result.done is True
    assert result.reward is not None
    assert result.reward < 0.0


def test_deterministic_trajectory() -> None:
    env_a = DdiEnvironment()
    env_b = DdiEnvironment()

    obs_a = env_a.reset()
    obs_b = env_b.reset()

    assert obs_a.patient_id == obs_b.patient_id

    sequence = [
        DdiAction(action_type="flag_interaction", interaction_id="INT-E1", rationale="critical"),
        DdiAction(action_type="flag_interaction", interaction_id="INT-E2", rationale="major"),
        DdiAction(action_type="monitor", interaction_id="INT-E3", rationale="monitor"),
    ]

    last_a = None
    last_b = None

    for action in sequence:
        last_a = env_a.step(action)
        last_b = env_b.step(action)

    assert last_a is not None
    assert last_b is not None
    assert last_a.done is True
    assert last_b.done is True
    assert last_a.final_score == last_b.final_score

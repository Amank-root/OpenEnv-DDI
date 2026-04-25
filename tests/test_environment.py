"""Tests for deterministic DDI environment behavior."""

from collections import Counter
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


def test_mixed_task_sampling_keeps_curriculum_then_mixes() -> None:
    env = DdiEnvironment(task_sampling="mixed")

    levels = [env.reset().task_level for _ in range(9)]

    assert levels[:3] == ["easy", "medium", "hard"]
    assert set(levels[3:]) == {"easy", "medium", "hard"}
    assert levels[3:] != ["easy", "medium", "hard", "easy", "medium", "hard"]


def test_mixed_seeded_sampling_is_reproducible() -> None:
    env_a = DdiEnvironment(task_sampling="mixed_seeded")
    env_b = DdiEnvironment(task_sampling="mixed_seeded")

    levels_a = [env_a.reset().task_level for _ in range(15)]
    levels_b = [env_b.reset().task_level for _ in range(15)]

    assert levels_a == levels_b
    assert levels_a[:3] == ["easy", "medium", "hard"]

    shuffled_window = levels_a[3:9]
    assert Counter(shuffled_window) == Counter({"easy": 2, "medium": 2, "hard": 2})


def test_validation_split_selects_validation_cases() -> None:
    env = DdiEnvironment(case_split="validation", task_sampling="curriculum")

    obs_easy = env.reset()
    obs_medium = env.reset()
    obs_hard = env.reset()

    for obs in (obs_easy, obs_medium, obs_hard):
        assert obs.metadata["case_split"] == "validation"
        assert obs.metadata["case_split_assignment"] == "validation"
        assert str(obs.metadata["template_family"]).startswith("validation::")
        assert obs.metadata["grader_name"] in {
            "grade_easy",
            "grade_medium",
            "grade_hard",
        }


def test_observation_metadata_exposes_action_hints() -> None:
    env = DdiEnvironment(task_sampling="curriculum")
    obs_easy = env.reset()

    unresolved_easy = obs_easy.metadata.get("unresolved_interaction_ids", [])
    assert isinstance(unresolved_easy, list)
    assert len(unresolved_easy) == len(obs_easy.ddi_candidates)
    assert obs_easy.metadata.get("remaining_required_regimens") == []

    env.reset()  # medium
    obs_hard = env.reset()  # hard
    remaining_required = obs_hard.metadata.get("remaining_required_regimens", [])
    assert isinstance(remaining_required, list)
    assert len(remaining_required) > 0


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
        DdiAction(
            action_type="flag_interaction",
            interaction_id="INT-E1",
            rationale="critical",
        ),
        DdiAction(
            action_type="flag_interaction", interaction_id="INT-E2", rationale="major"
        ),
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


def test_invalid_interaction_id_penalized() -> None:
    env = DdiEnvironment()
    env.reset()

    result = env.step(
        DdiAction(
            action_type="flag_interaction",
            interaction_id="INT-UNKNOWN",
            rationale="invalid",
        )
    )

    assert result.done is False
    assert result.reward is not None
    assert result.reward < 0.0


def test_state_progression_tracks_steps() -> None:
    env = DdiEnvironment()
    env.reset()
    assert env.state.step_count == 0

    env.step(
        DdiAction(
            action_type="flag_interaction",
            interaction_id="INT-E1",
            rationale="critical",
        )
    )
    assert env.state.step_count == 1


def test_step_budget_forces_termination() -> None:
    env = DdiEnvironment()
    obs = env.reset()

    # Repeat a duplicate decision to consume budget without satisfying objective.
    result = None
    for _ in range(obs.step_budget):
        result = env.step(
            DdiAction(
                action_type="flag_interaction",
                interaction_id="INT-E1",
                rationale="consume budget",
            )
        )
        if result.done:
            break

    assert result is not None
    assert result.done is True
    assert result.steps_used == obs.step_budget


def test_false_positive_flag_penalty_exceeds_correct_monitor_reward() -> None:
    env_bad = DdiEnvironment()
    env_good = DdiEnvironment()

    env_bad.reset()
    env_good.reset()

    bad = env_bad.step(
        DdiAction(
            action_type="flag_interaction",
            interaction_id="INT-E3",
            rationale="over-flag",
        )
    )
    good = env_good.step(
        DdiAction(action_type="monitor", interaction_id="INT-E3", rationale="expected")
    )

    assert bad.done is False
    assert good.done is False
    assert bad.reward is not None
    assert good.reward is not None
    assert bad.reward < 0.0
    assert good.reward > 0.0
    assert bad.reward < good.reward


def test_task_reward_scales_make_hard_penalties_stronger_than_easy() -> None:
    env_easy = DdiEnvironment()
    env_hard = DdiEnvironment()

    env_easy.reset()  # easy
    easy_penalty = env_easy.step(
        DdiAction(action_type="ignore", interaction_id="INT-E1", rationale="miss")
    )

    env_hard.reset()  # easy
    env_hard.reset()  # medium
    env_hard.reset()  # hard
    hard_penalty = env_hard.step(
        DdiAction(action_type="ignore", interaction_id="INT-H1", rationale="miss")
    )

    assert easy_penalty.reward is not None
    assert hard_penalty.reward is not None
    assert abs(hard_penalty.reward) > abs(easy_penalty.reward)


def test_low_impact_optional_regimen_discouraged_in_hard_task() -> None:
    env = DdiEnvironment()

    # Advance deterministic cycle to hard task.
    env.reset()  # easy
    env.reset()  # medium
    hard_obs = env.reset()  # hard

    optional_low_impact = None
    case_required = set(getattr(env, "_patient_case", {}).get("required_regimens", []))
    for option in hard_obs.substitution_options:
        if option.regimen_id not in case_required and option.expected_risk_delta < 0.5:
            optional_low_impact = option.regimen_id
            break

    assert optional_low_impact is not None

    result = env.step(
        DdiAction(
            action_type="suggest_alternative",
            suggested_regimen_id=optional_low_impact,
            rationale="test low-impact optional",
        )
    )

    assert result.done is False
    assert result.reward is not None
    assert result.reward < 0.0


def test_reward_components_present_in_metadata() -> None:
    env = DdiEnvironment()
    obs = env.reset()
    obs = env.step(
        DdiAction(
            action_type="flag_interaction",
            interaction_id="INT-E1",
            rationale="component-check",
        )
    )
    components = obs.metadata.get("reward_components", {})
    assert isinstance(components, dict)
    for key in (
        "triage_score",
        "regimen_score",
        "risk_delta_bonus",
        "invalid_action_penalty",
        "terminal_adjustment",
    ):
        assert key in components


def test_action_after_done_gets_repeat_finish_penalty() -> None:
    env = DdiEnvironment()
    env.reset()
    done_obs = env.step(DdiAction(action_type="finish", rationale="premature done"))
    assert done_obs.done is True

    post_done = env.step(DdiAction(action_type="finish", rationale="repeat finish"))
    assert post_done.done is True
    assert post_done.reward is not None
    assert post_done.reward < 0.0
    components = post_done.metadata.get("reward_components", {})
    assert float(components.get("invalid_action_penalty", 0.0)) < 0.0

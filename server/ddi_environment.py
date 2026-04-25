# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

"""DDI triage environment implementation for polypharmacy safety tasks."""

from __future__ import annotations

from copy import deepcopy
import os
import random
from uuid import uuid4

from openenv.core.env_server.interfaces import Environment
from openenv.core.env_server.types import State

try:
    from ..ddi_data import get_task_cases
    from ..graders import (
        expected_decision,
        grade_task,
        interaction_criticality,
    )
    from ..models import DdiAction, DdiCandidate, DdiObservation, SubstitutionOption
    from ..task_registry import TASK_CONFIGS, TASK_ORDER
except ImportError:
    from ddi_data import get_task_cases
    from graders import (
        expected_decision,
        grade_task,
        interaction_criticality,
    )
    from models import DdiAction, DdiCandidate, DdiObservation, SubstitutionOption
    from task_registry import TASK_CONFIGS, TASK_ORDER


# Reward calibration constants.
REWARD_CORRECT_FLAG = 1.0
REWARD_CORRECT_NON_FLAG = 0.65
PENALTY_MISSED_CRITICAL = 1.2
PENALTY_FALSE_POSITIVE_FLAG = 0.85
PENALTY_SUBOPTIMAL = 0.3
PENALTY_INVALID_INTERACTION_ID = 0.4
PENALTY_DUPLICATE_DECISION = 0.1
PENALTY_INVALID_SUBSTITUTION = 0.45
PENALTY_DUPLICATE_SUBSTITUTION = 0.1
PENALTY_OUT_OF_TASK_SUBSTITUTION = 0.3
PENALTY_UNSUPPORTED_ACTION = 0.2
PENALTY_REPEAT_FINISH_AFTER_DONE = 0.35

REWARD_REQUIRED_REGIMEN = 0.9
REWARD_OPTIONAL_HIGH_IMPACT = 0.12
PENALTY_OPTIONAL_LOW_IMPACT = 0.05
HIGH_IMPACT_REGIMEN_DELTA = 0.5

TERMINAL_SCORE_WEIGHT = 0.75
RISK_DELTA_SHAPING_WEIGHT = 0.08
MAX_ABS_RISK_DELTA = 1.0


class DdiEnvironment(Environment):
    """Environment for DDI triage in elderly patients with polypharmacy."""

    # Enable concurrent WebSocket sessions.
    # Set to True if your environment isolates state between instances.
    # When True, multiple WebSocket clients can connect simultaneously, each
    # getting their own environment instance (when using factory mode in app.py).
    SUPPORTS_CONCURRENT_SESSIONS: bool = True

    def __init__(self, case_split: str | None = None, task_sampling: str | None = None):
        """Initialize deterministic episode state."""
        self._state = State(episode_id=str(uuid4()), step_count=0)
        self._reset_count = 0
        self._task_cursor = 0
        self._case_cursor = {"easy": 0, "medium": 0, "hard": 0}

        self._case_split = (case_split or os.getenv("DDI_CASE_SPLIT", "all")).lower()
        self._task_sampling = (
            task_sampling or os.getenv("DDI_TASK_SAMPLING", "curriculum")
        ).lower()
        self._cases_by_level = get_task_cases(self._case_split)  # train|validation|all
        self._mixed_task_pattern = ["easy", "hard", "medium", "hard", "easy", "medium"]
        self._task_shuffle_seed = int(os.getenv("DDI_TASK_SHUFFLE_SEED", "17"))
        self._task_shuffle_window = max(
            len(TASK_ORDER), int(os.getenv("DDI_TASK_SHUFFLE_WINDOW", "6"))
        )
        self._task_rng = random.Random(self._task_shuffle_seed)
        self._task_shuffle_buffer: list[str] = []

        self._task_level = "easy"
        self._task_config = TASK_CONFIGS[self._task_level]
        self._patient_case = {}
        self._decisions = {}
        self._suggested_regimens = set()
        self._decision_log = []
        self._episode_done = False
        self._last_reward_components = {
            "triage_score": 0.0,
            "regimen_score": 0.0,
            "risk_delta_bonus": 0.0,
            "invalid_action_penalty": 0.0,
            "terminal_adjustment": 0.0,
        }

    def _refill_shuffled_task_buffer(self) -> None:
        # Build a deterministic shuffled window that still covers all task levels.
        repeats = (self._task_shuffle_window + len(TASK_ORDER) - 1) // len(TASK_ORDER)
        window = (TASK_ORDER * repeats)[: self._task_shuffle_window]
        self._task_rng.shuffle(window)
        self._task_shuffle_buffer = window

    def _scale_reward(self, delta: float) -> float:
        if delta >= 0:
            return delta * self._task_config.positive_reward_scale
        return delta * self._task_config.penalty_reward_scale

    def _next_task_level(self) -> str:
        if self._task_sampling == "mixed":
            # Keep one curriculum warmup cycle, then switch to a deterministic mixed pattern.
            if self._task_cursor < len(TASK_ORDER):
                task_level = TASK_ORDER[self._task_cursor]
            else:
                mixed_idx = (self._task_cursor - len(TASK_ORDER)) % len(
                    self._mixed_task_pattern
                )
                task_level = self._mixed_task_pattern[mixed_idx]
        elif self._task_sampling in {"mixed_shuffled", "mixed_seeded"}:
            # Keep one curriculum warmup cycle, then use seeded shuffled windows.
            if self._task_cursor < len(TASK_ORDER):
                task_level = TASK_ORDER[self._task_cursor]
            else:
                if not self._task_shuffle_buffer:
                    self._refill_shuffled_task_buffer()
                task_level = self._task_shuffle_buffer.pop(0)
        else:
            task_level = TASK_ORDER[self._task_cursor % len(TASK_ORDER)]

        self._task_cursor += 1
        return task_level

    def _select_case(self) -> None:
        self._task_level = self._next_task_level()
        self._task_config = TASK_CONFIGS[self._task_level]

        cases = self._cases_by_level[self._task_level]
        if not cases:
            raise ValueError(
                f"No cases found for split={self._case_split}, level={self._task_level}"
            )
        case_idx = self._case_cursor[self._task_level] % len(cases)
        self._case_cursor[self._task_level] += 1
        self._patient_case = deepcopy(cases[case_idx])

        self._decisions = {}
        self._suggested_regimens = set()
        self._decision_log = []
        self._episode_done = False

    def _remaining_critical(self) -> int:
        remaining = 0
        for interaction in self._patient_case["interactions"]:
            interaction_id = interaction["interaction_id"]
            expected = expected_decision(
                interaction, self._patient_case, self._task_level
            )
            decision = self._decisions.get(interaction_id)
            if expected == "flag_interaction" and decision != "flag_interaction":
                remaining += 1
        return remaining

    def _risk_score(self) -> float:
        base_risk = 0.0
        mitigated = 0.0

        for interaction in self._patient_case["interactions"]:
            interaction_id = interaction["interaction_id"]
            criticality = interaction_criticality(
                interaction,
                self._patient_case,
                self._task_level,
            )
            if (
                expected_decision(interaction, self._patient_case, self._task_level)
                == "flag_interaction"
            ):
                base_risk += criticality
                if self._decisions.get(interaction_id) == "flag_interaction":
                    mitigated += criticality

        option_by_id = {
            option["regimen_id"]: option
            for option in self._patient_case.get("substitution_options", [])
        }
        for regimen_id in self._suggested_regimens:
            option = option_by_id.get(regimen_id)
            if option:
                mitigated += option["expected_risk_delta"]

        return max(0.0, round(base_risk - mitigated, 3))

    def _remaining_required_regimens(self) -> list[str]:
        required = set(self._patient_case.get("required_regimens", []))
        return sorted(required - self._suggested_regimens)

    def _remaining_high_impact_regimens(self) -> list[str]:
        option_by_id = {
            option["regimen_id"]: option
            for option in self._patient_case.get("substitution_options", [])
        }
        remaining = []
        for regimen_id, option in option_by_id.items():
            if regimen_id in self._suggested_regimens:
                continue
            if option["expected_risk_delta"] >= HIGH_IMPACT_REGIMEN_DELTA:
                remaining.append(regimen_id)
        return sorted(remaining)

    def _unresolved_interaction_ids(self) -> list[str]:
        unresolved = []
        for interaction in self._patient_case["interactions"]:
            interaction_id = interaction["interaction_id"]
            if interaction_id not in self._decisions:
                unresolved.append(interaction_id)
        return unresolved

    def _risk_delta_bonus(self, previous_risk: float) -> float:
        current_risk = self._risk_score()
        delta = previous_risk - current_risk
        bounded_delta = max(-MAX_ABS_RISK_DELTA, min(MAX_ABS_RISK_DELTA, delta))
        return round(RISK_DELTA_SHAPING_WEIGHT * bounded_delta, 4)

    def _final_score(self) -> float:
        interactions = self._patient_case["interactions"]
        grade_kwargs = {
            "interactions": interactions,
            "decisions": self._decisions,
            "patient": self._patient_case,
        }
        if self._task_level == "hard":
            grade_kwargs["required_regimens"] = self._patient_case.get(
                "required_regimens", []
            )
            grade_kwargs["suggested_regimens"] = self._suggested_regimens

        return grade_task(self._task_level, **grade_kwargs)

    def _should_auto_finish(self) -> bool:
        all_interactions_decided = len(self._decisions) >= len(
            self._patient_case["interactions"]
        )
        if self._task_level != "hard":
            return all_interactions_decided

        required = set(self._patient_case.get("required_regimens", []))
        return all_interactions_decided and required.issubset(self._suggested_regimens)

    def _build_observation(
        self,
        *,
        done: bool,
        reward: float,
        final_score: float | None = None,
    ) -> DdiObservation:
        candidates = [
            DdiCandidate(**item) for item in self._patient_case["interactions"]
        ]
        substitutions = [
            SubstitutionOption(**item)
            for item in self._patient_case.get("substitution_options", [])
        ]

        return DdiObservation(
            task_level=self._task_level,
            task_title=self._task_config.title,
            objective=self._task_config.objective,
            patient_id=self._patient_case["case_id"],
            age=self._patient_case["age"],
            medications=self._patient_case["medications"],
            diagnoses=self._patient_case["diagnoses"],
            labs=self._patient_case["labs"],
            ddi_candidates=candidates,
            substitution_options=substitutions,
            decision_log=self._decision_log,
            remaining_critical_ddis=self._remaining_critical(),
            current_risk_score=self._risk_score(),
            step_budget=self._task_config.step_budget,
            steps_used=self._state.step_count,
            done=done,
            reward=reward,
            final_score=final_score,
            metadata={
                "decisions": self._decisions,
                "suggested_regimens": sorted(self._suggested_regimens),
                "grader_name": self._task_config.grader_name,
                "unresolved_interaction_ids": self._unresolved_interaction_ids(),
                "remaining_required_regimens": self._remaining_required_regimens(),
                "remaining_high_impact_regimens": self._remaining_high_impact_regimens(),
                "can_finish": self._should_auto_finish(),
                "case_split": self._case_split,
                "task_sampling": self._task_sampling,
                "template_family": self._patient_case.get(
                    "template_family", f"legacy::{self._patient_case['case_id']}"
                ),
                "case_split_assignment": self._patient_case.get("split", "train"),
                "reward_components": dict(self._last_reward_components),
            },
        )

    def reset(self) -> DdiObservation:
        """Reset the environment and emit a new deterministic patient case."""
        self._state = State(episode_id=str(uuid4()), step_count=0)
        self._reset_count += 1
        self._select_case()

        self._decision_log.append(
            f"Episode started for task={self._task_level}, patient={self._patient_case['case_id']}"
        )

        return self._build_observation(done=False, reward=0.0)

    def _find_interaction(self, interaction_id: str | None) -> dict | None:
        for item in self._patient_case["interactions"]:
            if item["interaction_id"] == interaction_id:
                return item
        return None

    def _apply_triage_action(self, action: DdiAction) -> float:
        interaction = self._find_interaction(action.interaction_id)
        if not interaction:
            self._decision_log.append(
                f"Invalid interaction id: {action.interaction_id}"
            )
            return -PENALTY_INVALID_INTERACTION_ID

        interaction_id = interaction["interaction_id"]
        if interaction_id in self._decisions:
            self._decision_log.append(f"Duplicate decision for {interaction_id}")
            return -PENALTY_DUPLICATE_DECISION

        expected = expected_decision(interaction, self._patient_case, self._task_level)
        action_type = action.action_type
        self._decisions[interaction_id] = action_type

        if action_type == expected:
            self._decision_log.append(
                f"Correct triage for {interaction_id}: {action_type}"
            )
            return (
                REWARD_CORRECT_FLAG
                if expected == "flag_interaction"
                else REWARD_CORRECT_NON_FLAG
            )

        if expected == "flag_interaction" and action_type != expected:
            self._decision_log.append(
                f"Missed critical DDI {interaction_id} with {action_type}"
            )
            return -PENALTY_MISSED_CRITICAL

        if action_type == "flag_interaction" and expected != action_type:
            self._decision_log.append(
                f"False-positive critical flag on {interaction_id}"
            )
            return -PENALTY_FALSE_POSITIVE_FLAG

        self._decision_log.append(
            f"Suboptimal triage for {interaction_id}: chose {action_type}, expected {expected}"
        )
        return -PENALTY_SUBOPTIMAL

    def _apply_substitution_action(self, action: DdiAction) -> float:
        if self._task_level != "hard":
            self._decision_log.append("Alternative suggestion used outside hard task")
            return -PENALTY_OUT_OF_TASK_SUBSTITUTION

        option_by_id = {
            option["regimen_id"]: option
            for option in self._patient_case.get("substitution_options", [])
        }
        regimen_id = action.suggested_regimen_id
        option = option_by_id.get(regimen_id)

        if not option:
            self._decision_log.append(f"Invalid substitution option: {regimen_id}")
            return -PENALTY_INVALID_SUBSTITUTION

        if regimen_id in self._suggested_regimens:
            self._decision_log.append(
                f"Duplicate substitution suggestion: {regimen_id}"
            )
            return -PENALTY_DUPLICATE_SUBSTITUTION

        self._suggested_regimens.add(regimen_id)
        required = set(self._patient_case.get("required_regimens", []))

        if regimen_id in required:
            self._decision_log.append(f"High-value alternative accepted: {regimen_id}")
            return REWARD_REQUIRED_REGIMEN

        if option["expected_risk_delta"] >= HIGH_IMPACT_REGIMEN_DELTA:
            self._decision_log.append(
                f"Optional high-impact alternative accepted: {regimen_id}"
            )
            return REWARD_OPTIONAL_HIGH_IMPACT

        self._decision_log.append(f"Low-impact alternative discouraged: {regimen_id}")
        return -PENALTY_OPTIONAL_LOW_IMPACT

    def _apply_finish_action(self) -> tuple[float, bool]:
        remaining_critical = self._remaining_critical()
        missing_required = 0
        if self._task_level == "hard":
            required = set(self._patient_case.get("required_regimens", []))
            missing_required = len(required - self._suggested_regimens)

        if remaining_critical > 0 or missing_required > 0:
            self._decision_log.append(
                "Agent requested premature finish before completing objectives"
            )
            return -(0.2 + 0.15 * remaining_critical + 0.1 * missing_required), True

        self._decision_log.append("Agent requested episode finish")
        return 0.15, True

    def step(self, action: DdiAction) -> DdiObservation:  # type: ignore[override]
        """Execute one triage action and return shaped reward feedback."""
        if self._episode_done:
            self._state.step_count += 1
            invalid_penalty = self._scale_reward(-PENALTY_REPEAT_FINISH_AFTER_DONE)
            self._last_reward_components = {
                "triage_score": 0.0,
                "regimen_score": 0.0,
                "risk_delta_bonus": 0.0,
                "invalid_action_penalty": round(invalid_penalty, 4),
                "terminal_adjustment": 0.0,
            }
            self._decision_log.append(
                "Action received after episode completion; apply anti-hacking penalty"
            )
            return self._build_observation(
                done=True,
                reward=round(invalid_penalty, 4),
                final_score=round(self._final_score(), 4),
            )

        self._state.step_count += 1
        previous_risk = self._risk_score()
        reward = 0.0
        done = False
        triage_score = 0.0
        regimen_score = 0.0
        invalid_action_penalty = 0.0

        action_type = action.action_type

        if action_type in {"flag_interaction", "monitor", "ignore"}:
            triage_score = self._scale_reward(self._apply_triage_action(action))
            reward += triage_score

        elif action_type == "suggest_alternative":
            regimen_score = self._scale_reward(self._apply_substitution_action(action))
            reward += regimen_score

        elif action_type == "finish":
            finish_reward, done = self._apply_finish_action()
            triage_score = self._scale_reward(finish_reward)
            reward += triage_score

        else:
            invalid_action_penalty = self._scale_reward(-PENALTY_UNSUPPORTED_ACTION)
            reward += invalid_action_penalty
            self._decision_log.append(f"Unsupported action type: {action_type}")

        risk_bonus = self._scale_reward(self._risk_delta_bonus(previous_risk))
        reward += risk_bonus
        if risk_bonus != 0:
            self._decision_log.append(f"Risk-delta shaping applied: {risk_bonus:+.3f}")

        self._last_reward_components = {
            "triage_score": round(triage_score, 4),
            "regimen_score": round(regimen_score, 4),
            "risk_delta_bonus": round(risk_bonus, 4),
            "invalid_action_penalty": round(invalid_action_penalty, 4),
            "terminal_adjustment": 0.0,
        }

        if self._state.step_count >= self._task_config.step_budget:
            done = True
            self._decision_log.append("Step budget reached")

        if self._should_auto_finish():
            done = True
            self._decision_log.append("Task objective conditions satisfied")

        if done:
            final_score = self._final_score()
            terminal_adjustment = TERMINAL_SCORE_WEIGHT * (final_score - 0.5)
            terminal_reward = self._scale_reward(terminal_adjustment)
            reward += terminal_reward
            self._last_reward_components["terminal_adjustment"] = round(
                terminal_reward, 4
            )
            self._episode_done = True
            return self._build_observation(
                done=True,
                reward=round(reward, 4),
                final_score=round(final_score, 4),
            )

        return self._build_observation(done=False, reward=round(reward, 4))

    @property
    def state(self) -> State:
        """
        Get the current environment state.

        Returns:
            Current State with episode_id and step_count
        """
        return self._state

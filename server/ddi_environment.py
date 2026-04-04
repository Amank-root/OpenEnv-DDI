# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

"""DDI triage environment implementation for polypharmacy safety tasks."""

from __future__ import annotations

from copy import deepcopy
from uuid import uuid4

from openenv.core.env_server.interfaces import Environment
from openenv.core.env_server.types import State

try:
    from ..ddi_data import TASK_CASES
    from ..graders import (
        expected_decision,
        grade_easy,
        grade_hard,
        grade_medium,
        interaction_criticality,
    )
    from ..models import DdiAction, DdiCandidate, DdiObservation, SubstitutionOption
    from ..task_registry import TASK_CONFIGS, TASK_ORDER
except ImportError:
    from ddi_data import TASK_CASES
    from graders import (
        expected_decision,
        grade_easy,
        grade_hard,
        grade_medium,
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

REWARD_REQUIRED_REGIMEN = 0.9
REWARD_OPTIONAL_HIGH_IMPACT = 0.12
PENALTY_OPTIONAL_LOW_IMPACT = 0.05
HIGH_IMPACT_REGIMEN_DELTA = 0.5

TERMINAL_SCORE_WEIGHT = 0.75


class DdiEnvironment(Environment):
    """Environment for DDI triage in elderly patients with polypharmacy."""

    # Enable concurrent WebSocket sessions.
    # Set to True if your environment isolates state between instances.
    # When True, multiple WebSocket clients can connect simultaneously, each
    # getting their own environment instance (when using factory mode in app.py).
    SUPPORTS_CONCURRENT_SESSIONS: bool = True

    def __init__(self):
        """Initialize deterministic episode state."""
        self._state = State(episode_id=str(uuid4()), step_count=0)
        self._reset_count = 0
        self._task_cursor = 0
        self._case_cursor = {"easy": 0, "medium": 0, "hard": 0}

        self._task_level = "easy"
        self._task_config = TASK_CONFIGS[self._task_level]
        self._patient_case = {}
        self._decisions = {}
        self._suggested_regimens = set()
        self._decision_log = []

    def _select_case(self) -> None:
        self._task_level = TASK_ORDER[self._task_cursor % len(TASK_ORDER)]
        self._task_cursor += 1
        self._task_config = TASK_CONFIGS[self._task_level]

        cases = TASK_CASES[self._task_level]
        case_idx = self._case_cursor[self._task_level] % len(cases)
        self._case_cursor[self._task_level] += 1
        self._patient_case = deepcopy(cases[case_idx])

        self._decisions = {}
        self._suggested_regimens = set()
        self._decision_log = []

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

    def _final_score(self) -> float:
        interactions = self._patient_case["interactions"]
        if self._task_level == "easy":
            return grade_easy(
                interactions=interactions,
                decisions=self._decisions,
                patient=self._patient_case,
            )
        if self._task_level == "medium":
            return grade_medium(
                interactions=interactions,
                decisions=self._decisions,
                patient=self._patient_case,
            )
        return grade_hard(
            interactions=interactions,
            decisions=self._decisions,
            patient=self._patient_case,
            required_regimens=self._patient_case.get("required_regimens", []),
            suggested_regimens=self._suggested_regimens,
        )

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
            return -0.4

        interaction_id = interaction["interaction_id"]
        if interaction_id in self._decisions:
            self._decision_log.append(f"Duplicate decision for {interaction_id}")
            return -0.1

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
            return -0.3

        option_by_id = {
            option["regimen_id"]: option
            for option in self._patient_case.get("substitution_options", [])
        }
        regimen_id = action.suggested_regimen_id
        option = option_by_id.get(regimen_id)

        if not option:
            self._decision_log.append(f"Invalid substitution option: {regimen_id}")
            return -0.45

        if regimen_id in self._suggested_regimens:
            self._decision_log.append(
                f"Duplicate substitution suggestion: {regimen_id}"
            )
            return -0.1

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
        self._state.step_count += 1
        reward = 0.0
        done = False

        action_type = action.action_type

        if action_type in {"flag_interaction", "monitor", "ignore"}:
            reward += self._apply_triage_action(action)

        elif action_type == "suggest_alternative":
            reward += self._apply_substitution_action(action)

        elif action_type == "finish":
            finish_reward, done = self._apply_finish_action()
            reward += finish_reward

        else:
            reward -= 0.2
            self._decision_log.append(f"Unsupported action type: {action_type}")

        if self._state.step_count >= self._task_config.step_budget:
            done = True
            self._decision_log.append("Step budget reached")

        if self._should_auto_finish():
            done = True
            self._decision_log.append("Task objective conditions satisfied")

        if done:
            final_score = self._final_score()
            reward += TERMINAL_SCORE_WEIGHT * (final_score - 0.5)
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

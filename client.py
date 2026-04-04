# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

"""Ddi Environment Client."""

from typing import Dict

from openenv.core import EnvClient
from openenv.core.client_types import StepResult
from openenv.core.env_server.types import State

try:
    from .models import DdiAction, DdiObservation
except ImportError:
    from models import DdiAction, DdiObservation


class DdiEnv(EnvClient[DdiAction, DdiObservation, State]):
    """
    Client for the Ddi Environment.

    This client maintains a persistent WebSocket connection to the environment server,
    enabling efficient multi-step interactions with lower latency.
    Each client instance has its own dedicated environment session on the server.

    Example:
        >>> # Connect to a running server
        >>> with DdiEnv(base_url="http://localhost:8000") as client:
        ...     result = client.reset()
        ...     print(result.observation.task_level)
        ...
        ...     action = DdiAction(action_type="finish", rationale="done")
        ...     result = client.step(action)
        ...     print(result.observation.final_score)

    Example with Docker:
        >>> # Automatically start container and connect
        >>> client = DdiEnv.from_docker_image("ddi-env:latest")
        >>> try:
        ...     result = client.reset()
        ...     result = client.step(DdiAction(action_type="finish"))
        ... finally:
        ...     client.close()
    """

    def _step_payload(self, action: DdiAction) -> Dict:
        """
        Convert DdiAction to JSON payload for step message.

        Args:
            action: DdiAction instance

        Returns:
            Dictionary representation suitable for JSON encoding
        """
        return {
            "action_type": action.action_type,
            "interaction_id": action.interaction_id,
            "suggested_regimen_id": action.suggested_regimen_id,
            "rationale": action.rationale,
        }

    def _parse_result(self, payload: Dict) -> StepResult[DdiObservation]:
        """
        Parse server response into StepResult[DdiObservation].

        Args:
            payload: JSON response data from server

        Returns:
            StepResult with DdiObservation
        """
        obs_data = payload.get("observation", {})
        observation = DdiObservation(
            task_level=obs_data.get("task_level", "easy"),
            task_title=obs_data.get("task_title", ""),
            objective=obs_data.get("objective", ""),
            patient_id=obs_data.get("patient_id", ""),
            age=obs_data.get("age", 0),
            medications=obs_data.get("medications", []),
            diagnoses=obs_data.get("diagnoses", []),
            labs=obs_data.get("labs", {}),
            ddi_candidates=obs_data.get("ddi_candidates", []),
            substitution_options=obs_data.get("substitution_options", []),
            decision_log=obs_data.get("decision_log", []),
            remaining_critical_ddis=obs_data.get("remaining_critical_ddis", 0),
            current_risk_score=obs_data.get("current_risk_score", 0.0),
            step_budget=obs_data.get("step_budget", 0),
            steps_used=obs_data.get("steps_used", 0),
            final_score=obs_data.get("final_score"),
            done=payload.get("done", False),
            reward=payload.get("reward"),
            metadata=obs_data.get("metadata", {}),
        )

        return StepResult(
            observation=observation,
            reward=payload.get("reward"),
            done=payload.get("done", False),
        )

    def _parse_state(self, payload: Dict) -> State:
        """
        Parse server response into State object.

        Args:
            payload: JSON response from state request

        Returns:
            State object with episode_id and step_count
        """
        return State(
            episode_id=payload.get("episode_id"),
            step_count=payload.get("step_count", 0),
        )

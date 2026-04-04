# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

"""Data models for the DDI triage environment."""

from typing import Dict, List, Literal, Optional

from openenv.core.env_server.types import Action, Observation
from pydantic import BaseModel, Field, model_validator


class DdiCandidate(BaseModel):
    """Candidate interaction presented to the agent for triage."""

    interaction_id: str = Field(..., description="Stable identifier for a DDI edge")
    drug_a: str = Field(..., description="First drug in the interaction pair")
    drug_b: str = Field(..., description="Second drug in the interaction pair")
    severity: Literal["contraindicated", "major", "moderate", "minor"]
    evidence: str = Field(
        ..., description="Short clinical rationale for the interaction"
    )


class SubstitutionOption(BaseModel):
    """Cataloged therapeutic substitution option for hard task."""

    regimen_id: str
    replace_drug: str
    with_drug: str
    target_condition: str
    expected_risk_delta: float = Field(
        ..., description="Estimated relative risk reduction if selected"
    )
    rationale: str


class DdiAction(Action):
    """Structured action schema for DDI triage."""

    action_type: Literal[
        "flag_interaction",
        "monitor",
        "suggest_alternative",
        "ignore",
        "finish",
    ]
    interaction_id: Optional[str] = Field(
        default=None,
        description="Required for interaction triage actions",
    )
    suggested_regimen_id: Optional[str] = Field(
        default=None,
        description="Required for suggest_alternative action",
    )
    rationale: str = Field(default="", description="Short decision reasoning")

    @model_validator(mode="after")
    def validate_payload(self) -> "DdiAction":
        triage_actions = {"flag_interaction", "monitor", "ignore"}
        if self.action_type in triage_actions and not self.interaction_id:
            raise ValueError("interaction_id is required for triage actions")
        if self.action_type == "suggest_alternative" and not self.suggested_regimen_id:
            raise ValueError("suggested_regimen_id is required for suggest_alternative")
        return self


class DdiObservation(Observation):
    """Observation payload for one patient triage episode."""

    task_level: Literal["easy", "medium", "hard"]
    task_title: str
    objective: str
    patient_id: str
    age: int
    medications: List[str]
    diagnoses: List[str]
    labs: Dict[str, float]
    ddi_candidates: List[DdiCandidate]
    substitution_options: List[SubstitutionOption] = Field(default_factory=list)
    decision_log: List[str] = Field(default_factory=list)
    remaining_critical_ddis: int = 0
    current_risk_score: float = 0.0
    step_budget: int = 0
    steps_used: int = 0
    final_score: Optional[float] = Field(
        default=None,
        description="Task score in range 0.0-1.0 populated when done=True",
    )

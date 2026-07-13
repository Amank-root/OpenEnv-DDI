"""
Converts all DDI cases (original + synthetic) into a supervised fine-tuning
dataset for Unsloth / HuggingFace TRL.

Each training row = one agent STEP inside one episode:
  - input:  the observation at that step (JSON, same format as inference.py)
  - output: the ground-truth action the grader expects (JSON)

Why step-level, not episode-level?
  The model is trained to produce ONE action per call. Converting each
  interaction in a case into its own training row maximises data volume and
  gives the model dense supervision on every decision, not just the final score.

Output
------
  ddi_train.jsonl   - training set  (~2 500 rows)
  ddi_val.jsonl     - validation set (~500 rows)

Each JSONL row has fields:
  {
    "messages": [
       {"role": "system",  "content": "<SYSTEM_PROMPT>"},
       {"role": "user",    "content": "<observation_json>"},
       {"role": "assistant","content": "<action_json>"}
    ],
    "task_level": "easy|medium|hard",
    "step_type":  "triage|suggest_alternative|finish"
  }

Usage
-----
  python build_sft_dataset.py \\
      --synth-dir synthetic_cases \\
      --orig-dir  /path/to/OpenEnv-DDI/  \\
      --out-dir   dataset/
"""

from __future__ import annotations
import argparse
import json
import os
import sys
from typing import Any, Dict, List, Optional, Tuple

# ── System prompt (mirrors inference.py SYSTEM_PROMPT exactly) ─────────────────
SYSTEM_PROMPT = (
    "You are a clinical medication safety triage assistant. "
    "Return exactly one valid JSON object and nothing else. "
    "Do not output markdown, code fences, or extra text. "
    "Required keys: action_type, interaction_id, suggested_regimen_id, rationale. "
    "Allowed action_type values: flag_interaction, monitor, suggest_alternative, ignore, finish. "
    "Field rules: "
    "for flag_interaction/monitor/ignore -> interaction_id must be a valid unresolved interaction_id and suggested_regimen_id must be null; "
    "for suggest_alternative -> suggested_regimen_id must be a valid unsuggested regimen_id and interaction_id must be null; "
    "for finish -> interaction_id and suggested_regimen_id must both be null. "
    "Decision policy: prioritize contraindicated and major interactions first; "
    "in medium/hard, treat moderate interactions as higher risk when age/renal/hepatic risk is elevated; "
    "in hard, propose high-impact alternatives before finish when pending. "
    "Never duplicate an already decided interaction or already suggested regimen. "
    "Set rationale to one short sentence."
)

# ── Replicate grader logic to compute ground-truth decisions ───────────────────

INTERACTION_RECOMMENDATIONS: Dict[str, str] = {
    "contraindicated": "flag_interaction",
    "major":           "flag_interaction",
    "moderate":        "monitor",
    "minor":           "ignore",
}

SEVERITY_WEIGHTS: Dict[str, float] = {
    "contraindicated": 1.0,
    "major":           0.8,
    "moderate":        0.45,
    "minor":           0.2,
}

HIGH_IMPACT_REGIMEN_DELTA = 0.5


def expected_decision(interaction: Dict, case: Dict, task_level: str) -> str:
    severity = interaction["severity"]
    default = INTERACTION_RECOMMENDATIONS[severity]

    if task_level == "easy":
        return default

    age  = case["age"]
    labs = case["labs"]
    egfr = labs.get("egfr", 90.0)
    alt  = labs.get("alt", 30.0)
    ast  = labs.get("ast", 30.0)
    hepatic_stress = alt >= 120 or ast >= 120

    if severity == "moderate" and (age >= 80 or egfr < 45 or hepatic_stress):
        return "flag_interaction"
    if severity == "minor" and (age >= 85 or egfr < 30 or alt >= 150):
        return "monitor"
    return default


def severity_priority(sev: str) -> int:
    return {"contraindicated": 0, "major": 1, "moderate": 2, "minor": 3}[sev]


def sort_interactions(interactions: List[Dict], case: Dict,
                      task_level: str) -> List[Dict]:
    """Sort so contraindicated/major come first; within same severity,
    flag_interaction (after patient modifiers) comes before monitor/ignore."""
    def key(i):
        exp = expected_decision(i, case, task_level)
        return (
            severity_priority(i["severity"]),
            0 if exp == "flag_interaction" else 1,
        )
    return sorted(interactions, key=key)


def build_observation_json(
    case: Dict,
    task_level: str,
    decided: Dict[str, str],       # interaction_id → action_type taken so far
    suggested_regimens: List[str], # regimen_ids suggested so far
    steps_used: int,
    step_budget: int,
) -> str:
    """Build the same JSON payload that inference.py's observation_to_prompt produces."""
    undecided_candidates = [
        {
            "interaction_id": i["interaction_id"],
            "drug_a": i["drug_a"],
            "drug_b": i["drug_b"],
            "severity": i["severity"],
            "evidence": i["evidence"],
        }
        for i in case["interactions"]
        if i["interaction_id"] not in decided
    ]

    all_regimen_ids = {
        o["regimen_id"] for o in case.get("substitution_options", [])
    }
    unsuggested_options = [
        {
            "regimen_id": o["regimen_id"],
            "replace_drug": o["replace_drug"],
            "with_drug": o["with_drug"],
            "expected_risk_delta": o["expected_risk_delta"],
        }
        for o in case.get("substitution_options", [])
        if o["regimen_id"] not in suggested_regimens
    ]

    # Compute remaining_critical
    remaining_critical = sum(
        1 for i in case["interactions"]
        if i["interaction_id"] not in decided
        and expected_decision(i, case, task_level) == "flag_interaction"
    )

    # Simple risk score proxy (matches environment logic closely enough)
    current_risk = round(
        sum(
            SEVERITY_WEIGHTS[i["severity"]]
            for i in case["interactions"]
            if i["interaction_id"] not in decided
        ),
        3,
    )

    payload = {
        "task_level": task_level,
        "objective": {
            "easy":   "Flag severe (contraindicated/major) interactions.",
            "medium": "Prioritize interactions by severity with patient-risk modifiers.",
            "hard":   "Triage interactions and suggest alternatives to reduce risk.",
        }[task_level],
        "patient_id": case["case_id"],
        "age": case["age"],
        "labs": case["labs"],
        "diagnoses": case["diagnoses"],
        "medications": case["medications"],
        "remaining_critical_ddis": remaining_critical,
        "current_risk_score": current_risk,
        "steps_used": steps_used,
        "step_budget": step_budget,
        "ddi_candidates": undecided_candidates,
        "substitution_options": unsuggested_options,
        "decision_log_tail": [],   # empty for SFT (no history needed)
        "history_tail": [],
    }
    return json.dumps(payload, indent=2)


STEP_BUDGETS = {"easy": 8, "medium": 12, "hard": 16}


def case_to_sft_rows(case: Dict, task_level: str) -> List[Dict]:
    """
    Unroll a single case into a sequence of (observation → action) SFT rows.
    Simulates an optimal agent that always picks the correct action.
    """
    rows: List[Dict] = []
    decided: Dict[str, str] = {}
    suggested_regimens: List[str] = []
    step_budget = STEP_BUDGETS[task_level]
    step = 0

    # Determine required regimens for hard tasks
    required_set = set(case.get("required_regimens", []))

    # Sort interactions so the model sees them in priority order during training
    sorted_interactions = sort_interactions(case["interactions"], case, task_level)

    for interaction in sorted_interactions:
        iid = interaction["interaction_id"]
        action_type = expected_decision(interaction, case, task_level)
        rationale = f"{interaction['severity']} interaction: {interaction['evidence'][:60]}"

        obs_json = build_observation_json(
            case, task_level, decided, suggested_regimens, step, step_budget
        )
        action_json = json.dumps({
            "action_type": action_type,
            "interaction_id": iid,
            "suggested_regimen_id": None,
            "rationale": rationale,
        })

        rows.append({
            "messages": [
                {"role": "system",    "content": SYSTEM_PROMPT},
                {"role": "user",      "content": obs_json},
                {"role": "assistant", "content": action_json},
            ],
            "task_level": task_level,
            "step_type": "triage",
        })

        decided[iid] = action_type
        step += 1

    # For hard tasks: suggest required alternatives in order of risk_delta (desc)
    if task_level == "hard":
        options_by_id = {
            o["regimen_id"]: o
            for o in case.get("substitution_options", [])
        }
        # Sort by required first, then by risk_delta desc
        all_option_ids = [o["regimen_id"] for o in case.get("substitution_options", [])]
        required_options = [
            options_by_id[rid] for rid in all_option_ids
            if rid in required_set
        ]
        required_options.sort(key=lambda o: o["expected_risk_delta"], reverse=True)

        for opt in required_options:
            obs_json = build_observation_json(
                case, task_level, decided, suggested_regimens, step, step_budget
            )
            action_json = json.dumps({
                "action_type": "suggest_alternative",
                "interaction_id": None,
                "suggested_regimen_id": opt["regimen_id"],
                "rationale": opt["rationale"][:80],
            })
            rows.append({
                "messages": [
                    {"role": "system",    "content": SYSTEM_PROMPT},
                    {"role": "user",      "content": obs_json},
                    {"role": "assistant", "content": action_json},
                ],
                "task_level": task_level,
                "step_type": "suggest_alternative",
            })
            suggested_regimens.append(opt["regimen_id"])
            step += 1

    # Final finish step
    obs_json = build_observation_json(
        case, task_level, decided, suggested_regimens, step, step_budget
    )
    action_json = json.dumps({
        "action_type": "finish",
        "interaction_id": None,
        "suggested_regimen_id": None,
        "rationale": "triage complete",
    })
    rows.append({
        "messages": [
            {"role": "system",    "content": SYSTEM_PROMPT},
            {"role": "user",      "content": obs_json},
            {"role": "assistant", "content": action_json},
        ],
        "task_level": task_level,
        "step_type": "finish",
    })

    return rows


def build_dataset(orig_dir: str, synth_dir: str, out_dir: str) -> None:
    # ── Load original cases ────────────────────────────────────────────────────
    sys.path.insert(0, orig_dir)
    from task_cases import EASY_CASES, MEDIUM_CASES, HARD_CASES

    # ── Load synthetic cases ───────────────────────────────────────────────────
    sys.path.insert(0, synth_dir)
    from synthetic_easy_cases   import SYNTHETIC_EASY_CASES
    from synthetic_medium_cases import SYNTHETIC_MEDIUM_CASES
    from synthetic_hard_cases   import SYNTHETIC_HARD_CASES

    level_map = {
        "easy":   EASY_CASES   + SYNTHETIC_EASY_CASES,
        "medium": MEDIUM_CASES + SYNTHETIC_MEDIUM_CASES,
        "hard":   HARD_CASES   + SYNTHETIC_HARD_CASES,
    }

    os.makedirs(out_dir, exist_ok=True)
    train_rows: List[Dict] = []
    val_rows:   List[Dict] = []

    for level, all_cases in level_map.items():
        for case in all_cases:
            split = case.get("split", "train")
            rows = case_to_sft_rows(case, level)
            if split == "train":
                train_rows.extend(rows)
            else:
                val_rows.extend(rows)

    # Shuffle training rows so level/difficulty aren't grouped
    import random
    rng = random.Random(99)
    rng.shuffle(train_rows)

    def write_jsonl(rows: List[Dict], path: str) -> None:
        with open(path, "w") as f:
            for row in rows:
                f.write(json.dumps(row) + "\n")

    train_path = os.path.join(out_dir, "ddi_train.jsonl")
    val_path   = os.path.join(out_dir, "ddi_val.jsonl")
    write_jsonl(train_rows, train_path)
    write_jsonl(val_rows,   val_path)

    # Print stats per step_type
    from collections import Counter
    train_types = Counter(r["step_type"] for r in train_rows)
    val_types   = Counter(r["step_type"] for r in val_rows)
    train_levels = Counter(r["task_level"] for r in train_rows)

    print(f"\n{'='*50}")
    print(f"  ddi_train.jsonl  → {len(train_rows):>5} rows")
    print(f"    by step_type:   {dict(train_types)}")
    print(f"    by task_level:  {dict(train_levels)}")
    print(f"  ddi_val.jsonl    → {len(val_rows):>5} rows")
    print(f"    by step_type:   {dict(val_types)}")
    print(f"{'='*50}")
    print(f"\nFiles written to: {out_dir}/")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--orig-dir",  default=os.path.abspath(os.path.join(os.path.dirname(__file__), "..")),
                   help="Path to OpenEnv-DDI repo (for original cases)")
    p.add_argument("--synth-dir", default="synthetic_cases",
                   help="Directory containing the synthetic_*_cases.py files")
    p.add_argument("--out-dir",   default="dataset",
                   help="Where to write ddi_train.jsonl and ddi_val.jsonl")
    args = p.parse_args()
    build_dataset(orig_dir=args.orig_dir, synth_dir=args.synth_dir, out_dir=args.out_dir)

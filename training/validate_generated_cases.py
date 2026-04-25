"""Validate AI-generated synthetic DDI cases before merging into task pools.

Supports either:
1) JSONL where each row is one case with a required "task_level" field, or
2) JSON object with {"easy": [...], "medium": [...], "hard": [...]}.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import sys
from typing import Any

# Allow execution as a file path: uv run training/validate_generated_cases.py ...
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from ddi_data import TASK_CASES, case_template_family
from graders import expected_decision

ALLOWED_LEVELS = {"easy", "medium", "hard"}
ALLOWED_SPLITS = {"train", "validation"}
ALLOWED_SEVERITIES = {"contraindicated", "major", "moderate", "minor"}


def _load_candidates(path: Path) -> dict[str, list[dict[str, Any]]]:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    if path.suffix.lower() == ".jsonl":
        grouped: dict[str, list[dict[str, Any]]] = {
            "easy": [],
            "medium": [],
            "hard": [],
        }
        with path.open("r", encoding="utf-8") as handle:
            for line_no, line in enumerate(handle, start=1):
                line = line.strip()
                if not line:
                    continue
                try:
                    row = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise ValueError(f"Invalid JSONL at line {line_no}: {exc}") from exc
                level = row.get("task_level")
                if level not in ALLOWED_LEVELS:
                    raise ValueError(
                        f"JSONL row {line_no} missing valid task_level in {ALLOWED_LEVELS}"
                    )
                row = dict(row)
                row.pop("task_level", None)
                grouped[level].append(row)
        return grouped

    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("JSON input must be an object with easy/medium/hard keys")
    output = {level: list(data.get(level, [])) for level in ("easy", "medium", "hard")}
    return output


def _validate_required_case_fields(case: dict[str, Any], level: str, idx: int) -> list[str]:
    errors: list[str] = []
    required = [
        "case_id",
        "template_family",
        "split",
        "age",
        "labs",
        "diagnoses",
        "medications",
        "interactions",
        "required_regimens",
        "substitution_options",
    ]
    missing = [field for field in required if field not in case]
    if missing:
        errors.append(f"{level}[{idx}] missing fields: {missing}")
        return errors

    if case["split"] not in ALLOWED_SPLITS:
        errors.append(f"{level}[{idx}] invalid split={case['split']!r}")
    if not isinstance(case["case_id"], str) or not case["case_id"]:
        errors.append(f"{level}[{idx}] invalid case_id")
    if not isinstance(case["template_family"], str) or "::" not in case["template_family"]:
        errors.append(
            f"{level}[{idx}] template_family must be namespaced like train::... or validation::..."
        )
    if not isinstance(case["age"], int) or case["age"] < 18 or case["age"] > 110:
        errors.append(f"{level}[{idx}] age out of expected range")
    if not isinstance(case["labs"], dict) or not case["labs"]:
        errors.append(f"{level}[{idx}] labs must be a non-empty object")
    if not isinstance(case["diagnoses"], list) or len(case["diagnoses"]) < 2:
        errors.append(f"{level}[{idx}] diagnoses must contain at least 2 entries")
    if not isinstance(case["medications"], list) or len(case["medications"]) < 4:
        errors.append(f"{level}[{idx}] medications must contain at least 4 entries")
    if not isinstance(case["interactions"], list) or len(case["interactions"]) < 3:
        errors.append(f"{level}[{idx}] interactions must contain at least 3 entries")
    if not isinstance(case["required_regimens"], list):
        errors.append(f"{level}[{idx}] required_regimens must be a list")
    if not isinstance(case["substitution_options"], list):
        errors.append(f"{level}[{idx}] substitution_options must be a list")

    if level == "hard":
        if len(case["required_regimens"]) < 2:
            errors.append(f"{level}[{idx}] hard case requires at least 2 required_regimens")
        if len(case["substitution_options"]) < 3:
            errors.append(f"{level}[{idx}] hard case requires at least 3 substitution_options")
    else:
        if case["required_regimens"]:
            errors.append(f"{level}[{idx}] non-hard case should not define required_regimens")
        if case["substitution_options"]:
            errors.append(f"{level}[{idx}] non-hard case should not define substitution_options")

    return errors


def _validate_interactions(case: dict[str, Any], level: str, idx: int) -> list[str]:
    errors: list[str] = []
    interactions = case.get("interactions", [])
    seen_ids: set[str] = set()
    severe_count = 0
    for j, interaction in enumerate(interactions):
        for field in ("interaction_id", "drug_a", "drug_b", "severity", "evidence"):
            if field not in interaction:
                errors.append(f"{level}[{idx}].interactions[{j}] missing {field}")
        interaction_id = interaction.get("interaction_id")
        if interaction_id in seen_ids:
            errors.append(f"{level}[{idx}] duplicate interaction_id {interaction_id!r}")
        if isinstance(interaction_id, str):
            seen_ids.add(interaction_id)
        severity = interaction.get("severity")
        if severity not in ALLOWED_SEVERITIES:
            errors.append(f"{level}[{idx}] invalid severity={severity!r}")
        if severity in {"contraindicated", "major"}:
            severe_count += 1

    if severe_count == 0:
        errors.append(f"{level}[{idx}] must include at least one contraindicated/major interaction")
    return errors


def _validate_regimens(case: dict[str, Any], level: str, idx: int) -> list[str]:
    errors: list[str] = []
    if level != "hard":
        return errors

    required = set(case.get("required_regimens", []))
    options = case.get("substitution_options", [])
    option_ids = set()
    for j, option in enumerate(options):
        for field in (
            "regimen_id",
            "replace_drug",
            "with_drug",
            "target_condition",
            "expected_risk_delta",
            "rationale",
        ):
            if field not in option:
                errors.append(f"{level}[{idx}].substitution_options[{j}] missing {field}")
        regimen_id = option.get("regimen_id")
        if regimen_id in option_ids:
            errors.append(f"{level}[{idx}] duplicate regimen_id {regimen_id!r}")
        if isinstance(regimen_id, str):
            option_ids.add(regimen_id)
        delta = option.get("expected_risk_delta")
        if not isinstance(delta, (int, float)) or not (0.0 <= float(delta) <= 1.5):
            errors.append(
                f"{level}[{idx}] expected_risk_delta out of range for {regimen_id!r}: {delta!r}"
            )

    missing = required - option_ids
    if missing:
        errors.append(
            f"{level}[{idx}] required_regimens missing substitution_options: {sorted(missing)}"
        )
    return errors


def _case_signature(case: dict[str, Any]) -> tuple[Any, ...]:
    interactions = sorted(
        (
            str(item.get("drug_a", "")),
            str(item.get("drug_b", "")),
            str(item.get("severity", "")),
        )
        for item in case.get("interactions", [])
    )
    required = tuple(sorted(str(x) for x in case.get("required_regimens", [])))
    meds = tuple(sorted(str(x) for x in case.get("medications", [])))
    return (
        int(case.get("age", -1)),
        tuple(interactions),
        required,
        meds,
    )


def _validate_decision_coverage(case: dict[str, Any], level: str, idx: int) -> list[str]:
    """Ensure generated cases are not degenerate w.r.t. expected decisions."""
    errors: list[str] = []
    decisions = [
        expected_decision(interaction, case, level)
        for interaction in case.get("interactions", [])
    ]
    if not decisions:
        return errors
    if len(set(decisions)) == 1 and decisions[0] == "ignore":
        errors.append(f"{level}[{idx}] degenerate case: all expected decisions are ignore")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        type=Path,
        required=True,
        help="Path to generated cases (.json or .jsonl).",
    )
    parser.add_argument(
        "--min_new_per_level",
        type=int,
        default=20,
        help="Minimum accepted synthetic cases required per level.",
    )
    parser.add_argument(
        "--max_near_duplicate_ratio",
        type=float,
        default=0.1,
        help="Fail if near-duplicate signatures exceed this ratio per level.",
    )
    args = parser.parse_args()

    candidates_by_level = _load_candidates(args.input)

    errors: list[str] = []
    warnings: list[str] = []

    existing_case_ids = {
        level: {str(case.get("case_id")) for case in TASK_CASES[level]}
        for level in ALLOWED_LEVELS
    }
    existing_families_by_split = {
        level: {
            "train": set(),
            "validation": set(),
        }
        for level in ALLOWED_LEVELS
    }
    for level, cases in TASK_CASES.items():
        for case in cases:
            split = str(case.get("split", "train"))
            if split in {"train", "validation"}:
                existing_families_by_split[level][split].add(case_template_family(case))

    for level in ("easy", "medium", "hard"):
        generated = candidates_by_level.get(level, [])
        if len(generated) < args.min_new_per_level:
            errors.append(
                f"{level}: expected at least {args.min_new_per_level} new cases, got {len(generated)}"
            )

        seen_case_ids: set[str] = set()
        seen_families_by_split = {"train": set(), "validation": set()}
        signatures: list[tuple[Any, ...]] = []

        for idx, case in enumerate(generated):
            case_id = str(case.get("case_id", ""))
            split = str(case.get("split", "train"))
            family = str(case.get("template_family", ""))

            errors.extend(_validate_required_case_fields(case, level, idx))
            errors.extend(_validate_interactions(case, level, idx))
            errors.extend(_validate_regimens(case, level, idx))
            errors.extend(_validate_decision_coverage(case, level, idx))

            if case_id in existing_case_ids[level]:
                errors.append(f"{level}[{idx}] case_id collides with existing pool: {case_id}")
            if case_id in seen_case_ids:
                errors.append(f"{level}[{idx}] duplicate generated case_id: {case_id}")
            seen_case_ids.add(case_id)

            if split in {"train", "validation"} and family:
                if family in existing_families_by_split[level][split]:
                    errors.append(
                        f"{level}[{idx}] template_family collides with existing {split} family: {family}"
                    )
                if family in seen_families_by_split[split]:
                    errors.append(
                        f"{level}[{idx}] repeated generated template_family in {split}: {family}"
                    )
                seen_families_by_split[split].add(family)

            signatures.append(_case_signature(case))

        signature_counts = Counter(signatures)
        duplicate_signature_items = sum(count - 1 for count in signature_counts.values() if count > 1)
        duplicate_ratio = (duplicate_signature_items / len(signatures)) if signatures else 0.0
        if duplicate_ratio > args.max_near_duplicate_ratio:
            errors.append(
                f"{level}: near-duplicate ratio {duplicate_ratio:.2%} exceeds "
                f"limit {args.max_near_duplicate_ratio:.2%}"
            )
        elif duplicate_signature_items > 0:
            warnings.append(
                f"{level}: near-duplicate signatures detected ({duplicate_signature_items} extra)"
            )

        split_counts = defaultdict(int)
        for case in generated:
            split_counts[str(case.get("split", "train"))] += 1
        if split_counts["validation"] == 0:
            warnings.append(f"{level}: no validation cases in generated set")

    if warnings:
        print("WARNINGS:")
        for message in warnings:
            print(f"- {message}")

    if errors:
        print("VALIDATION FAILED:")
        for message in errors:
            print(f"- {message}")
        raise SystemExit(1)

    print("VALIDATION PASSED: generated cases are safe to review/merge.")


if __name__ == "__main__":
    main()

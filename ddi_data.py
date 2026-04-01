"""Deterministic synthetic DDI datasets for polypharmacy triage tasks."""

from __future__ import annotations

from typing import Dict, List

SEVERITY_WEIGHTS: Dict[str, float] = {
    "contraindicated": 1.0,
    "major": 0.8,
    "moderate": 0.45,
    "minor": 0.2,
}

INTERACTION_RECOMMENDATIONS: Dict[str, str] = {
    "contraindicated": "flag_interaction",
    "major": "flag_interaction",
    "moderate": "monitor",
    "minor": "ignore",
}

TASK_CASES: Dict[str, List[Dict]] = {
    "easy": [
        {
            "case_id": "E-001",
            "age": 74,
            "labs": {"egfr": 68.0, "creatinine": 1.0, "potassium": 4.4, "inr": 2.4},
            "diagnoses": ["atrial_fibrillation", "hypertension", "dyslipidemia"],
            "medications": [
                "warfarin",
                "trimethoprim_sulfamethoxazole",
                "simvastatin",
                "amlodipine",
                "aspirin",
            ],
            "interactions": [
                {
                    "interaction_id": "INT-E1",
                    "drug_a": "warfarin",
                    "drug_b": "trimethoprim_sulfamethoxazole",
                    "severity": "contraindicated",
                    "evidence": "increased INR and major bleeding risk",
                },
                {
                    "interaction_id": "INT-E2",
                    "drug_a": "warfarin",
                    "drug_b": "aspirin",
                    "severity": "major",
                    "evidence": "additive anticoagulation and bleeding",
                },
                {
                    "interaction_id": "INT-E3",
                    "drug_a": "simvastatin",
                    "drug_b": "amlodipine",
                    "severity": "moderate",
                    "evidence": "higher statin exposure and myopathy risk",
                },
            ],
            "required_regimens": [],
            "substitution_options": [],
        }
    ],
    "medium": [
        {
            "case_id": "M-001",
            "age": 83,
            "labs": {"egfr": 31.0, "creatinine": 2.0, "potassium": 5.4, "inr": 2.1},
            "diagnoses": [
                "heart_failure",
                "atrial_fibrillation",
                "type_2_diabetes",
                "chronic_kidney_disease",
            ],
            "medications": [
                "warfarin",
                "amiodarone",
                "spironolactone",
                "lisinopril",
                "furosemide",
                "metformin",
                "insulin_glargine",
                "atorvastatin",
                "omeprazole",
                "sertraline",
                "trimethoprim_sulfamethoxazole",
            ],
            "interactions": [
                {
                    "interaction_id": "INT-M1",
                    "drug_a": "warfarin",
                    "drug_b": "amiodarone",
                    "severity": "major",
                    "evidence": "CYP inhibition elevates warfarin exposure",
                },
                {
                    "interaction_id": "INT-M2",
                    "drug_a": "spironolactone",
                    "drug_b": "lisinopril",
                    "severity": "moderate",
                    "evidence": "hyperkalemia risk with renal impairment",
                },
                {
                    "interaction_id": "INT-M3",
                    "drug_a": "metformin",
                    "drug_b": "furosemide",
                    "severity": "moderate",
                    "evidence": "reduced renal clearance can increase lactic acidosis risk",
                },
                {
                    "interaction_id": "INT-M4",
                    "drug_a": "warfarin",
                    "drug_b": "trimethoprim_sulfamethoxazole",
                    "severity": "contraindicated",
                    "evidence": "marked INR elevation and bleeding",
                },
            ],
            "required_regimens": [],
            "substitution_options": [],
        }
    ],
    "hard": [
        {
            "case_id": "H-001",
            "age": 87,
            "labs": {"egfr": 26.0, "creatinine": 2.4, "potassium": 5.2, "inr": 2.6},
            "diagnoses": [
                "atrial_fibrillation",
                "coronary_artery_disease",
                "type_2_diabetes",
                "chronic_kidney_disease",
                "hypertension",
                "depression",
            ],
            "medications": [
                "warfarin",
                "trimethoprim_sulfamethoxazole",
                "clopidogrel",
                "omeprazole",
                "simvastatin",
                "amlodipine",
                "spironolactone",
                "lisinopril",
                "metformin",
                "insulin_glargine",
                "sertraline",
                "ibuprofen",
            ],
            "interactions": [
                {
                    "interaction_id": "INT-H1",
                    "drug_a": "warfarin",
                    "drug_b": "trimethoprim_sulfamethoxazole",
                    "severity": "contraindicated",
                    "evidence": "severe bleeding risk due to INR elevation",
                },
                {
                    "interaction_id": "INT-H2",
                    "drug_a": "clopidogrel",
                    "drug_b": "omeprazole",
                    "severity": "major",
                    "evidence": "reduced clopidogrel activation and antiplatelet efficacy",
                },
                {
                    "interaction_id": "INT-H3",
                    "drug_a": "simvastatin",
                    "drug_b": "amlodipine",
                    "severity": "moderate",
                    "evidence": "myopathy risk from increased simvastatin exposure",
                },
                {
                    "interaction_id": "INT-H4",
                    "drug_a": "spironolactone",
                    "drug_b": "lisinopril",
                    "severity": "moderate",
                    "evidence": "hyperkalemia risk in CKD",
                },
                {
                    "interaction_id": "INT-H5",
                    "drug_a": "warfarin",
                    "drug_b": "ibuprofen",
                    "severity": "major",
                    "evidence": "substantial GI and systemic bleeding risk",
                },
            ],
            "required_regimens": ["REG-H1", "REG-H2", "REG-H3"],
            "substitution_options": [
                {
                    "regimen_id": "REG-H1",
                    "replace_drug": "trimethoprim_sulfamethoxazole",
                    "with_drug": "cephalexin",
                    "target_condition": "infection",
                    "expected_risk_delta": 0.85,
                    "rationale": "reduces anticoagulation interaction burden",
                },
                {
                    "regimen_id": "REG-H2",
                    "replace_drug": "omeprazole",
                    "with_drug": "pantoprazole",
                    "target_condition": "gi_protection",
                    "expected_risk_delta": 0.55,
                    "rationale": "lower impact on clopidogrel activation",
                },
                {
                    "regimen_id": "REG-H3",
                    "replace_drug": "ibuprofen",
                    "with_drug": "acetaminophen",
                    "target_condition": "pain",
                    "expected_risk_delta": 0.6,
                    "rationale": "reduces additive bleeding risk with warfarin",
                },
                {
                    "regimen_id": "REG-H4",
                    "replace_drug": "simvastatin",
                    "with_drug": "pravastatin",
                    "target_condition": "dyslipidemia",
                    "expected_risk_delta": 0.35,
                    "rationale": "less CYP3A4 interaction with amlodipine",
                },
            ],
        }
    ],
}

"""Deterministic DDI cases for the easy task level."""

from typing import Any, Dict, List

Case = Dict[str, Any]

EASY_CASES: List[Case] = [
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
    },
    {
        "case_id": "E-002",
        "age": 71,
        "labs": {"egfr": 74.0, "creatinine": 0.9, "potassium": 4.1, "inr": 1.1},
        "diagnoses": ["angina", "hypertension", "atrial_fibrillation"],
        "medications": [
            "nitroglycerin",
            "sildenafil",
            "apixaban",
            "clarithromycin",
            "metoprolol",
            "verapamil",
        ],
        "interactions": [
            {
                "interaction_id": "INT-E21",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation",
            },
            {
                "interaction_id": "INT-E22",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased apixaban exposure and bleeding risk",
            },
            {
                "interaction_id": "INT-E23",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia",
            },
        ],
        "required_regimens": [],
        "substitution_options": [],
    },
    {
        "case_id": "E-003",
        "age": 79,
        "labs": {"egfr": 45.0, "creatinine": 1.2, "potassium": 4.5, "inr": 1.0},
        "diagnoses": ["dyslipidemia", "hypertension", "hypothyroidism"],
        "medications": [
            "atorvastatin",
            "diltiazem",
            "dabigatran",
            "ketoconazole",
            "levothyroxine",
            "calcium_carbonate",
        ],
        "interactions": [
            {
                "interaction_id": "INT-E31",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "strong P-gp inhibition increases dabigatran exposure",
            },
            {
                "interaction_id": "INT-E32",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk",
            },
            {
                "interaction_id": "INT-E33",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "reduced levothyroxine absorption with coadministration",
            },
        ],
        "required_regimens": [],
        "substitution_options": [],
    },
    {
        "case_id": "E-004",
        "age": 66,
        "labs": {"egfr": 92.0, "creatinine": 0.8, "potassium": 4.2, "inr": 1.0},
        "diagnoses": ["depression", "hypertension", "iron_deficiency"],
        "medications": [
            "linezolid",
            "sertraline",
            "metoprolol",
            "paroxetine",
            "ferrous_sulfate",
            "levothyroxine",
        ],
        "interactions": [
            {
                "interaction_id": "INT-E41",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonergic toxicity risk from MAOI activity",
            },
            {
                "interaction_id": "INT-E42",
                "drug_a": "metoprolol",
                "drug_b": "paroxetine",
                "severity": "moderate",
                "evidence": "CYP2D6 inhibition may increase beta-blocker effect",
            },
            {
                "interaction_id": "INT-E43",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "reduced thyroid hormone absorption",
            },
        ],
        "required_regimens": [],
        "substitution_options": [],
    },
    {
        "case_id": "E-005",
        "age": 84,
        "labs": {"egfr": 58.0, "creatinine": 1.3, "potassium": 4.8, "inr": 1.1},
        "diagnoses": ["angina", "heart_failure", "depression"],
        "medications": [
            "isosorbide_mononitrate",
            "sildenafil",
            "spironolactone",
            "losartan",
            "aspirin",
            "sertraline",
        ],
        "interactions": [
            {
                "interaction_id": "INT-E51",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension from additive vasodilation",
            },
            {
                "interaction_id": "INT-E52",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "additive potassium retention",
            },
            {
                "interaction_id": "INT-E53",
                "drug_a": "aspirin",
                "drug_b": "sertraline",
                "severity": "minor",
                "evidence": "mildly increased bleeding tendency",
            },
        ],
        "required_regimens": [],
        "substitution_options": [],
    },
    {
        "case_id": "E-006",
        "age": 72,
        "labs": {"egfr": 76.0, "creatinine": 0.9, "potassium": 4.3, "inr": 1.9},
        "diagnoses": ["atrial_fibrillation", "dyslipidemia", "infection"],
        "medications": [
            "apixaban",
            "clarithromycin",
            "simvastatin",
            "amlodipine",
            "cetirizine",
        ],
        "interactions": [
            {
                "interaction_id": "INT-E61",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk",
            },
            {
                "interaction_id": "INT-E62",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher simvastatin exposure with myopathy risk",
            },
            {
                "interaction_id": "INT-E63",
                "drug_a": "cetirizine",
                "drug_b": "amlodipine",
                "severity": "minor",
                "evidence": "possible additive dizziness in sensitive patients",
            },
        ],
        "required_regimens": [],
        "substitution_options": [],
    },
    {
        "case_id": "E-007",
        "template_family": "validation::hepatic-qtc-polypharmacy",
        "split": "validation",
        "age": 68,
        "labs": {
            "egfr": 88.0,
            "creatinine": 0.8,
            "potassium": 4.1,
            "inr": 1.0,
            "alt": 132.0,
            "ast": 128.0,
        },
        "diagnoses": ["copd", "depression", "fatty_liver_disease"],
        "medications": [
            "citalopram",
            "azithromycin",
            "atorvastatin",
            "diltiazem",
            "prednisone",
        ],
        "interactions": [
            {
                "interaction_id": "INT-E71",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "additive QT prolongation risk",
            },
            {
                "interaction_id": "INT-E72",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "CYP3A4 inhibition can increase statin exposure",
            },
            {
                "interaction_id": "INT-E73",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "possible additive GI intolerance",
            },
        ],
        "required_regimens": [],
        "substitution_options": [],
    },
    {
        "case_id": "E-008",
        "template_family": "validation::borderline-renal-anticoag",
        "split": "validation",
        "age": 79,
        "labs": {
            "egfr": 45.0,
            "creatinine": 1.2,
            "potassium": 4.5,
            "inr": 2.0,
            "alt": 38.0,
            "ast": 34.0,
        },
        "diagnoses": ["atrial_fibrillation", "coronary_artery_disease", "gout"],
        "medications": [
            "warfarin",
            "metronidazole",
            "allopurinol",
            "furosemide",
            "metoprolol",
        ],
        "interactions": [
            {
                "interaction_id": "INT-E81",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR elevation and severe bleeding risk",
            },
            {
                "interaction_id": "INT-E82",
                "drug_a": "allopurinol",
                "drug_b": "warfarin",
                "severity": "moderate",
                "evidence": "possible potentiation of anticoagulant effect",
            },
            {
                "interaction_id": "INT-E83",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "possible orthostatic symptoms in dehydration",
            },
        ],
        "required_regimens": [],
        "substitution_options": [],
    },
    {
        "case_id": "E-009",
        "template_family": "train::elderly-hepatic-qtc-easy",
        "split": "train",
        "age": 88,
        "labs": {
            "egfr": 57.0,
            "creatinine": 1.1,
            "potassium": 4.6,
            "inr": 1.0,
            "alt": 158.0,
            "ast": 141.0,
        },
        "diagnoses": ["depression", "copd", "chronic_liver_disease"],
        "medications": [
            "citalopram",
            "clarithromycin",
            "warfarin",
            "metronidazole",
            "furosemide",
        ],
        "interactions": [
            {
                "interaction_id": "INT-E91",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "pronounced INR elevation with severe bleeding risk",
            },
            {
                "interaction_id": "INT-E92",
                "drug_a": "citalopram",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "additive QT prolongation risk",
            },
            {
                "interaction_id": "INT-E93",
                "drug_a": "clarithromycin",
                "drug_b": "furosemide",
                "severity": "minor",
                "evidence": "potential dehydration-related dizziness",
            },
        ],
        "required_regimens": [],
        "substitution_options": [],
    },
    {
        "case_id": "E-010",
        "template_family": "validation::renal-edge-anticoag-easy",
        "split": "validation",
        "age": 82,
        "labs": {
            "egfr": 42.0,
            "creatinine": 1.6,
            "potassium": 4.9,
            "inr": 2.3,
            "alt": 42.0,
            "ast": 35.0,
        },
        "diagnoses": ["atrial_fibrillation", "chronic_kidney_disease", "hypertension"],
        "medications": [
            "warfarin",
            "trimethoprim_sulfamethoxazole",
            "spironolactone",
            "losartan",
            "pantoprazole",
        ],
        "interactions": [
            {
                "interaction_id": "INT-E101",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "large INR increase with severe bleeding risk",
            },
            {
                "interaction_id": "INT-E102",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention",
            },
            {
                "interaction_id": "INT-E103",
                "drug_a": "pantoprazole",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive orthostatic symptoms",
            },
        ],
        "required_regimens": [],
        "substitution_options": [],
    },
]


def _generate_easy_expansion(count: int = 36, start_idx: int = 200) -> List[Case]:
    generated: List[Case] = []
    for offset in range(count):
        idx = start_idx + offset
        split = "validation" if offset % 5 == 4 else "train"
        template_family = f"{split}::bulk-easy-{idx}"
        case_id = f"E-{idx}"
        interaction_prefix = f"INT-E{idx}"

        severe_pair = (
            ("warfarin", "metronidazole", "contraindicated", "severe INR elevation and bleeding risk")
            if offset % 2 == 0
            else ("nitroglycerin", "sildenafil", "contraindicated", "profound hypotension risk")
        )
        major_pair = (
            ("apixaban", "clarithromycin", "major", "increased anticoagulant exposure")
            if offset % 3 == 0
            else ("citalopram", "azithromycin", "major", "additive QT prolongation risk")
        )
        moderate_pair = (
            ("spironolactone", "losartan", "moderate", "combined potassium retention risk")
            if offset % 2 == 0
            else ("simvastatin", "amlodipine", "moderate", "higher statin exposure and myopathy risk")
        )

        medications = sorted(
            {
                severe_pair[0],
                severe_pair[1],
                major_pair[0],
                major_pair[1],
                moderate_pair[0],
                moderate_pair[1],
                "furosemide",
                "metoprolol",
            }
        )

        generated.append(
            {
                "case_id": case_id,
                "template_family": template_family,
                "split": split,
                "age": 68 + (offset % 24),
                "labs": {
                    "egfr": float(38 + (offset % 44)),
                    "creatinine": round(0.9 + (offset % 8) * 0.12, 2),
                    "potassium": round(4.0 + (offset % 7) * 0.14, 2),
                    "inr": round(1.1 + (offset % 7) * 0.2, 2),
                    "alt": float(42 + (offset % 6) * 14),
                    "ast": float(39 + (offset % 6) * 13),
                },
                "diagnoses": [
                    "atrial_fibrillation",
                    "hypertension",
                    "chronic_kidney_disease" if offset % 2 == 0 else "coronary_artery_disease",
                ],
                "medications": medications,
                "interactions": [
                    {
                        "interaction_id": f"{interaction_prefix}1",
                        "drug_a": severe_pair[0],
                        "drug_b": severe_pair[1],
                        "severity": severe_pair[2],
                        "evidence": severe_pair[3],
                    },
                    {
                        "interaction_id": f"{interaction_prefix}2",
                        "drug_a": major_pair[0],
                        "drug_b": major_pair[1],
                        "severity": major_pair[2],
                        "evidence": major_pair[3],
                    },
                    {
                        "interaction_id": f"{interaction_prefix}3",
                        "drug_a": moderate_pair[0],
                        "drug_b": moderate_pair[1],
                        "severity": moderate_pair[2],
                        "evidence": moderate_pair[3],
                    },
                ],
                "required_regimens": [],
                "substitution_options": [],
            }
        )
    return generated


EASY_CASES.extend(_generate_easy_expansion())

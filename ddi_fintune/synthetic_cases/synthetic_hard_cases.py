"""Synthetic DDI cases for the hard task level."""

from typing import Any, Dict, List

Case = Dict[str, Any]

SYNTHETIC_HARD_CASES: List[Case] = [
    {
        "case_id": "SYN-H-0001",
        "age": 92,
        "labs": {
            "egfr": 43.2,
            "creatinine": 2.5,
            "potassium": 5.0,
            "inr": 3.1,
            "alt": 124.4,
            "ast": 123.0
        },
        "diagnoses": [
            "nonalcoholic_steatohepatitis",
            "heart_failure",
            "peripheral_artery_disease",
            "type_2_diabetes"
        ],
        "medications": [
            "amiodarone",
            "aspirin",
            "ciprofloxacin",
            "clopidogrel",
            "digoxin",
            "furosemide",
            "metoprolol",
            "omeprazole",
            "sertraline",
            "ticagrelor",
            "trimethoprim_sulfamethoxazole",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0001-1",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0001-2",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-H-0001-3",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            },
            {
                "interaction_id": "INT-SYN-H-0001-4",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0001-5",
                "drug_a": "aspirin",
                "drug_b": "sertraline",
                "severity": "minor",
                "evidence": "increased bleeding tendency, amplified in frailty"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0001-1",
            "REG-SYN-H-0001-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0001-1",
                "replace_drug": "trimethoprim_sulfamethoxazole",
                "with_drug": "cephalexin",
                "target_condition": "infection",
                "expected_risk_delta": 0.87,
                "rationale": "reduces interaction burden from trimethoprim_sulfamethoxazole"
            },
            {
                "regimen_id": "REG-SYN-H-0001-2",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.87,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0002",
        "age": 92,
        "labs": {
            "egfr": 25.5,
            "creatinine": 2.3,
            "potassium": 5.0,
            "inr": 2.6,
            "alt": 116.7,
            "ast": 106.3
        },
        "diagnoses": [
            "osteoarthritis",
            "nonalcoholic_steatohepatitis",
            "chronic_pain",
            "peripheral_artery_disease",
            "anxiety"
        ],
        "medications": [
            "amiodarone",
            "calcium_carbonate",
            "isosorbide_mononitrate",
            "linezolid",
            "metoprolol",
            "omeprazole",
            "paroxetine",
            "rivaroxaban",
            "sildenafil",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0002-1",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0002-2",
                "drug_a": "metoprolol",
                "drug_b": "paroxetine",
                "severity": "moderate",
                "evidence": "CYP2D6 inhibition raises metoprolol exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0002-3",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-H-0002-4",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0002-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0002-2",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.74,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0003",
        "age": 87,
        "labs": {
            "egfr": 43.9,
            "creatinine": 2.5,
            "potassium": 5.3,
            "inr": 2.2,
            "alt": 199.4,
            "ast": 152.5
        },
        "diagnoses": [
            "heart_failure",
            "anxiety",
            "chronic_kidney_disease"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "clarithromycin",
            "furosemide",
            "lisinopril",
            "metronidazole",
            "simvastatin",
            "spironolactone",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0003-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0003-2",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0003-3",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-H-0003-4",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0003-1",
            "REG-SYN-H-0003-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0003-1",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.55,
                "rationale": "reduces interaction burden from clarithromycin"
            },
            {
                "regimen_id": "REG-SYN-H-0003-2",
                "replace_drug": "metronidazole",
                "with_drug": "doxycycline",
                "target_condition": "infection",
                "expected_risk_delta": 0.9,
                "rationale": "reduces interaction burden from metronidazole"
            },
            {
                "regimen_id": "REG-SYN-H-0003-3",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.37,
                "rationale": "modest risk reduction by replacing simvastatin"
            },
            {
                "regimen_id": "REG-SYN-H-0003-4",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.38,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0004",
        "age": 93,
        "labs": {
            "egfr": 31.5,
            "creatinine": 2.3,
            "potassium": 5.5,
            "inr": 2.5,
            "alt": 128.5,
            "ast": 100.6
        },
        "diagnoses": [
            "atrial_fibrillation",
            "chronic_kidney_disease",
            "anemia",
            "peripheral_artery_disease",
            "osteoarthritis"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "ciprofloxacin",
            "clarithromycin",
            "diclofenac",
            "isosorbide_mononitrate",
            "metronidazole",
            "naproxen",
            "sildenafil",
            "simvastatin",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0004-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0004-2",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-H-0004-3",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            },
            {
                "interaction_id": "INT-SYN-H-0004-4",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0004-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0004-1",
                "replace_drug": "metronidazole",
                "with_drug": "doxycycline",
                "target_condition": "infection",
                "expected_risk_delta": 0.72,
                "rationale": "reduces interaction burden from metronidazole"
            },
            {
                "regimen_id": "REG-SYN-H-0004-2",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.3,
                "rationale": "modest risk reduction by replacing simvastatin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0005",
        "age": 93,
        "labs": {
            "egfr": 29.3,
            "creatinine": 2.2,
            "potassium": 5.1,
            "inr": 3.0,
            "alt": 118.5,
            "ast": 115.6
        },
        "diagnoses": [
            "gout",
            "dyslipidemia",
            "nonalcoholic_steatohepatitis",
            "anxiety",
            "hypertension"
        ],
        "medications": [
            "allopurinol",
            "amlodipine",
            "cetirizine",
            "dabigatran",
            "ferrous_sulfate",
            "furosemide",
            "isosorbide_mononitrate",
            "ketoconazole",
            "levothyroxine",
            "linezolid",
            "nitroglycerin",
            "sildenafil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0005-1",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-H-0005-2",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-H-0005-3",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0005-4",
                "drug_a": "furosemide",
                "drug_b": "warfarin",
                "severity": "minor",
                "evidence": "volume changes may alter INR stability"
            },
            {
                "interaction_id": "INT-SYN-H-0005-5",
                "drug_a": "cetirizine",
                "drug_b": "amlodipine",
                "severity": "minor",
                "evidence": "possible additive sedation in elderly"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0006",
        "age": 94,
        "labs": {
            "egfr": 37.0,
            "creatinine": 2.6,
            "potassium": 5.3,
            "inr": 2.8
        },
        "diagnoses": [
            "coronary_artery_disease",
            "gout",
            "chronic_pain"
        ],
        "medications": [
            "amiodarone",
            "aspirin",
            "atorvastatin",
            "azithromycin",
            "dabigatran",
            "digoxin",
            "diltiazem",
            "ferrous_sulfate",
            "furosemide",
            "ketoconazole",
            "metoprolol",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0006-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0006-2",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0006-3",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            },
            {
                "interaction_id": "INT-SYN-H-0006-4",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "CYP3A4 inhibition raises statin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0006-5",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0006-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0006-1",
                "replace_drug": "metoprolol",
                "with_drug": "bisoprolol",
                "target_condition": "rate_control",
                "expected_risk_delta": 0.31,
                "rationale": "modest risk reduction by replacing metoprolol"
            },
            {
                "regimen_id": "REG-SYN-H-0006-2",
                "replace_drug": "atorvastatin",
                "with_drug": "rosuvastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.29,
                "rationale": "modest risk reduction by replacing atorvastatin"
            },
            {
                "regimen_id": "REG-SYN-H-0006-3",
                "replace_drug": "aspirin",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.8,
                "rationale": "reduces interaction burden from aspirin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0007",
        "age": 92,
        "labs": {
            "egfr": 33.1,
            "creatinine": 1.9,
            "potassium": 5.5,
            "inr": 2.6,
            "alt": 111.7,
            "ast": 112.3
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "chronic_liver_disease",
            "atrial_fibrillation",
            "depression"
        ],
        "medications": [
            "allopurinol",
            "apixaban",
            "diclofenac",
            "furosemide",
            "glipizide",
            "metoprolol",
            "metronidazole",
            "naproxen",
            "nitroglycerin",
            "rivaroxaban",
            "sildenafil",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0007-1",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0007-2",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            },
            {
                "interaction_id": "INT-SYN-H-0007-3",
                "drug_a": "allopurinol",
                "drug_b": "warfarin",
                "severity": "moderate",
                "evidence": "allopurinol may enhance warfarin anticoagulation"
            },
            {
                "interaction_id": "INT-SYN-H-0007-4",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0007-5",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0007-1",
            "REG-SYN-H-0007-4"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0007-1",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.78,
                "rationale": "reduces interaction burden from diclofenac"
            },
            {
                "regimen_id": "REG-SYN-H-0007-2",
                "replace_drug": "metoprolol",
                "with_drug": "bisoprolol",
                "target_condition": "rate_control",
                "expected_risk_delta": 0.3,
                "rationale": "modest risk reduction by replacing metoprolol"
            },
            {
                "regimen_id": "REG-SYN-H-0007-4",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.75,
                "rationale": "reduces interaction burden from naproxen"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0008",
        "age": 91,
        "labs": {
            "egfr": 31.6,
            "creatinine": 2.5,
            "potassium": 5.5,
            "inr": 2.6,
            "alt": 169.8,
            "ast": 147.3
        },
        "diagnoses": [
            "dyslipidemia",
            "depression",
            "anemia",
            "gout",
            "chronic_pain"
        ],
        "medications": [
            "amiodarone",
            "amlodipine",
            "cetirizine",
            "ciprofloxacin",
            "clarithromycin",
            "dabigatran",
            "diclofenac",
            "glipizide",
            "ketoconazole",
            "lisinopril",
            "metoprolol",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0008-1",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0008-2",
                "drug_a": "cetirizine",
                "drug_b": "amlodipine",
                "severity": "minor",
                "evidence": "possible additive sedation in elderly"
            },
            {
                "interaction_id": "INT-SYN-H-0008-3",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0008-4",
                "drug_a": "glipizide",
                "drug_b": "ciprofloxacin",
                "severity": "moderate",
                "evidence": "dysglycemia risk from fluoroquinolone-sulfonylurea combination"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0009",
        "age": 87,
        "labs": {
            "egfr": 35.0,
            "creatinine": 2.0,
            "potassium": 5.1,
            "inr": 2.1,
            "alt": 128.3,
            "ast": 121.0
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "chronic_pain",
            "peripheral_artery_disease"
        ],
        "medications": [
            "aspirin",
            "calcium_carbonate",
            "isosorbide_mononitrate",
            "levothyroxine",
            "lisinopril",
            "losartan",
            "naproxen",
            "rivaroxaban",
            "sildenafil",
            "simvastatin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0009-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0009-2",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0009-3",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-H-0009-4",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0009-1",
            "REG-SYN-H-0009-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0009-1",
                "replace_drug": "aspirin",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.73,
                "rationale": "reduces interaction burden from aspirin"
            },
            {
                "regimen_id": "REG-SYN-H-0009-2",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.69,
                "rationale": "reduces interaction burden from naproxen"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0010",
        "age": 91,
        "labs": {
            "egfr": 35.2,
            "creatinine": 2.0,
            "potassium": 5.4,
            "inr": 2.9
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "hypertension",
            "osteoarthritis",
            "anemia",
            "chronic_liver_disease"
        ],
        "medications": [
            "apixaban",
            "azithromycin",
            "citalopram",
            "diclofenac",
            "ketoconazole",
            "losartan",
            "naproxen",
            "omeprazole",
            "rivaroxaban",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0010-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0010-2",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            },
            {
                "interaction_id": "INT-SYN-H-0010-3",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0010-4",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0010-1",
            "REG-SYN-H-0010-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0010-1",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.56,
                "rationale": "reduces interaction burden from diclofenac"
            },
            {
                "regimen_id": "REG-SYN-H-0010-2",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.63,
                "rationale": "reduces interaction burden from naproxen"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0011",
        "age": 85,
        "labs": {
            "egfr": 29.6,
            "creatinine": 2.1,
            "potassium": 5.3,
            "inr": 3.1,
            "alt": 177.7,
            "ast": 158.1
        },
        "diagnoses": [
            "chronic_pain",
            "type_2_diabetes",
            "peripheral_artery_disease",
            "chronic_liver_disease"
        ],
        "medications": [
            "ciprofloxacin",
            "citalopram",
            "clopidogrel",
            "diltiazem",
            "losartan",
            "metronidazole",
            "nitroglycerin",
            "sildenafil",
            "simvastatin",
            "spironolactone",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0011-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0011-2",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-H-0011-3",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            },
            {
                "interaction_id": "INT-SYN-H-0011-4",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0011-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0011-1",
                "replace_drug": "metronidazole",
                "with_drug": "doxycycline",
                "target_condition": "infection",
                "expected_risk_delta": 0.78,
                "rationale": "reduces interaction burden from metronidazole"
            },
            {
                "regimen_id": "REG-SYN-H-0011-2",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.36,
                "rationale": "modest risk reduction by replacing simvastatin"
            },
            {
                "regimen_id": "REG-SYN-H-0011-3",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.32,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0012",
        "age": 88,
        "labs": {
            "egfr": 31.0,
            "creatinine": 2.1,
            "potassium": 4.9,
            "inr": 2.1,
            "alt": 125.5,
            "ast": 119.7
        },
        "diagnoses": [
            "hypothyroidism",
            "depression",
            "type_2_diabetes"
        ],
        "medications": [
            "azithromycin",
            "ciprofloxacin",
            "citalopram",
            "clopidogrel",
            "dabigatran",
            "ferrous_sulfate",
            "ibuprofen",
            "ketoconazole",
            "naproxen",
            "omeprazole",
            "spironolactone",
            "valsartan"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0012-1",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-H-0012-2",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            },
            {
                "interaction_id": "INT-SYN-H-0012-3",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-H-0012-4",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0012-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0012-1",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.49,
                "rationale": "modest risk reduction by replacing spironolactone"
            },
            {
                "regimen_id": "REG-SYN-H-0012-2",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.59,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0013",
        "age": 95,
        "labs": {
            "egfr": 38.8,
            "creatinine": 2.2,
            "potassium": 5.1,
            "inr": 2.5,
            "alt": 189.7,
            "ast": 157.5
        },
        "diagnoses": [
            "osteoarthritis",
            "hypothyroidism",
            "coronary_artery_disease",
            "dyslipidemia"
        ],
        "medications": [
            "allopurinol",
            "amlodipine",
            "apixaban",
            "azithromycin",
            "citalopram",
            "clopidogrel",
            "isosorbide_mononitrate",
            "metoprolol",
            "paroxetine",
            "sildenafil",
            "simvastatin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0013-1",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-H-0013-2",
                "drug_a": "metoprolol",
                "drug_b": "paroxetine",
                "severity": "moderate",
                "evidence": "CYP2D6 inhibition raises metoprolol exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0013-3",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-H-0013-4",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0013-2",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.31,
                "rationale": "modest risk reduction by replacing simvastatin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0014",
        "age": 95,
        "labs": {
            "egfr": 30.2,
            "creatinine": 2.3,
            "potassium": 5.2,
            "inr": 3.1,
            "alt": 170.6,
            "ast": 155.1
        },
        "diagnoses": [
            "nonalcoholic_steatohepatitis",
            "dyslipidemia",
            "gout",
            "anxiety"
        ],
        "medications": [
            "apixaban",
            "ciprofloxacin",
            "clarithromycin",
            "clopidogrel",
            "dabigatran",
            "ferrous_sulfate",
            "ketoconazole",
            "levothyroxine",
            "metronidazole",
            "naproxen",
            "omeprazole",
            "rivaroxaban",
            "sertraline",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0014-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0014-2",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0014-3",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0014-4",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0014-5",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0014-1",
            "REG-SYN-H-0014-2",
            "REG-SYN-H-0014-3",
            "REG-SYN-H-0014-4"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0014-1",
                "replace_drug": "metronidazole",
                "with_drug": "doxycycline",
                "target_condition": "infection",
                "expected_risk_delta": 0.63,
                "rationale": "reduces interaction burden from metronidazole"
            },
            {
                "regimen_id": "REG-SYN-H-0014-2",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.58,
                "rationale": "reduces interaction burden from clarithromycin"
            },
            {
                "regimen_id": "REG-SYN-H-0014-3",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.73,
                "rationale": "reduces interaction burden from naproxen"
            },
            {
                "regimen_id": "REG-SYN-H-0014-4",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.6,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0015",
        "age": 88,
        "labs": {
            "egfr": 34.4,
            "creatinine": 2.3,
            "potassium": 5.2,
            "inr": 2.8
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "coronary_artery_disease",
            "heart_failure",
            "gout",
            "type_2_diabetes"
        ],
        "medications": [
            "apixaban",
            "aspirin",
            "clarithromycin",
            "dabigatran",
            "diltiazem",
            "ferrous_sulfate",
            "isosorbide_mononitrate",
            "ketoconazole",
            "levothyroxine",
            "sertraline",
            "spironolactone",
            "valsartan"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0015-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0015-2",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0015-3",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            },
            {
                "interaction_id": "INT-SYN-H-0015-4",
                "drug_a": "aspirin",
                "drug_b": "sertraline",
                "severity": "minor",
                "evidence": "increased bleeding tendency, amplified in frailty"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0015-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0015-1",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.7,
                "rationale": "reduces interaction burden from clarithromycin"
            },
            {
                "regimen_id": "REG-SYN-H-0015-2",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.39,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0016",
        "age": 94,
        "labs": {
            "egfr": 25.7,
            "creatinine": 2.5,
            "potassium": 5.1,
            "inr": 2.1,
            "alt": 167.4,
            "ast": 175.5
        },
        "diagnoses": [
            "chronic_pain",
            "chronic_liver_disease",
            "dyslipidemia",
            "coronary_artery_disease",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "amlodipine",
            "clopidogrel",
            "ferrous_sulfate",
            "glipizide",
            "ibuprofen",
            "levothyroxine",
            "losartan",
            "omeprazole",
            "prednisone",
            "simvastatin",
            "trimethoprim_sulfamethoxazole",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0016-1",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0016-2",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-H-0016-3",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-H-0016-4",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            },
            {
                "interaction_id": "INT-SYN-H-0016-5",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0016-1",
            "REG-SYN-H-0016-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0016-1",
                "replace_drug": "trimethoprim_sulfamethoxazole",
                "with_drug": "cephalexin",
                "target_condition": "infection",
                "expected_risk_delta": 0.84,
                "rationale": "reduces interaction burden from trimethoprim_sulfamethoxazole"
            },
            {
                "regimen_id": "REG-SYN-H-0016-2",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.75,
                "rationale": "reduces interaction burden from omeprazole"
            },
            {
                "regimen_id": "REG-SYN-H-0016-3",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.38,
                "rationale": "modest risk reduction by replacing simvastatin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0017",
        "age": 85,
        "labs": {
            "egfr": 34.8,
            "creatinine": 2.6,
            "potassium": 5.4,
            "inr": 3.2
        },
        "diagnoses": [
            "chronic_pain",
            "osteoarthritis",
            "anxiety",
            "depression"
        ],
        "medications": [
            "amiodarone",
            "amlodipine",
            "ciprofloxacin",
            "digoxin",
            "ferrous_sulfate",
            "ibuprofen",
            "isosorbide_mononitrate",
            "omeprazole",
            "simvastatin",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0017-1",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-H-0017-2",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0017-3",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0017-4",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0017-1",
            "REG-SYN-H-0017-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0017-1",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.62,
                "rationale": "reduces interaction burden from omeprazole"
            },
            {
                "regimen_id": "REG-SYN-H-0017-2",
                "replace_drug": "ibuprofen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.85,
                "rationale": "reduces interaction burden from ibuprofen"
            },
            {
                "regimen_id": "REG-SYN-H-0017-3",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.29,
                "rationale": "modest risk reduction by replacing simvastatin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0018",
        "age": 93,
        "labs": {
            "egfr": 33.4,
            "creatinine": 2.7,
            "potassium": 5.3,
            "inr": 2.1,
            "alt": 192.9,
            "ast": 167.2
        },
        "diagnoses": [
            "chronic_pain",
            "nonalcoholic_steatohepatitis",
            "coronary_artery_disease",
            "atrial_fibrillation"
        ],
        "medications": [
            "amiodarone",
            "apixaban",
            "aspirin",
            "clarithromycin",
            "dabigatran",
            "digoxin",
            "furosemide",
            "ketoconazole",
            "metoprolol",
            "nitroglycerin",
            "prednisone",
            "sildenafil",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0018-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0018-2",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            },
            {
                "interaction_id": "INT-SYN-H-0018-3",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-H-0018-4",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0018-5",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0018-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0018-1",
                "replace_drug": "metoprolol",
                "with_drug": "bisoprolol",
                "target_condition": "rate_control",
                "expected_risk_delta": 0.26,
                "rationale": "modest risk reduction by replacing metoprolol"
            },
            {
                "regimen_id": "REG-SYN-H-0018-2",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.63,
                "rationale": "reduces interaction burden from clarithromycin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0019",
        "age": 92,
        "labs": {
            "egfr": 32.6,
            "creatinine": 2.3,
            "potassium": 4.9,
            "inr": 2.5,
            "alt": 115.5,
            "ast": 110.8
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "depression",
            "chronic_liver_disease",
            "chronic_pain",
            "coronary_artery_disease"
        ],
        "medications": [
            "amlodipine",
            "azithromycin",
            "cetirizine",
            "ciprofloxacin",
            "clopidogrel",
            "ferrous_sulfate",
            "omeprazole",
            "prednisone",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0019-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-H-0019-2",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            },
            {
                "interaction_id": "INT-SYN-H-0019-3",
                "drug_a": "amlodipine",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive hypotension in frail adults"
            },
            {
                "interaction_id": "INT-SYN-H-0019-4",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0019-1",
            "REG-SYN-H-0019-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0019-1",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.73,
                "rationale": "reduces interaction burden from omeprazole"
            },
            {
                "regimen_id": "REG-SYN-H-0019-2",
                "replace_drug": "trimethoprim_sulfamethoxazole",
                "with_drug": "cephalexin",
                "target_condition": "infection",
                "expected_risk_delta": 0.66,
                "rationale": "reduces interaction burden from trimethoprim_sulfamethoxazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0020",
        "age": 95,
        "labs": {
            "egfr": 34.4,
            "creatinine": 2.1,
            "potassium": 5.3,
            "inr": 2.9,
            "alt": 110.2,
            "ast": 100.3
        },
        "diagnoses": [
            "depression",
            "gout",
            "chronic_kidney_disease",
            "atrial_fibrillation",
            "type_2_diabetes"
        ],
        "medications": [
            "allopurinol",
            "amiodarone",
            "atorvastatin",
            "citalopram",
            "digoxin",
            "diltiazem",
            "isosorbide_mononitrate",
            "lisinopril",
            "omeprazole",
            "simvastatin",
            "spironolactone",
            "ticagrelor",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0020-1",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-H-0020-2",
                "drug_a": "allopurinol",
                "drug_b": "warfarin",
                "severity": "moderate",
                "evidence": "allopurinol may enhance warfarin anticoagulation"
            },
            {
                "interaction_id": "INT-SYN-H-0020-3",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            },
            {
                "interaction_id": "INT-SYN-H-0020-4",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0020-5",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0020-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0020-1",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.74,
                "rationale": "reduces interaction burden from omeprazole"
            },
            {
                "regimen_id": "REG-SYN-H-0020-3",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.42,
                "rationale": "modest risk reduction by replacing spironolactone"
            },
            {
                "regimen_id": "REG-SYN-H-0020-4",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.31,
                "rationale": "modest risk reduction by replacing simvastatin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0021",
        "age": 92,
        "labs": {
            "egfr": 36.0,
            "creatinine": 2.4,
            "potassium": 4.8,
            "inr": 2.7
        },
        "diagnoses": [
            "type_2_diabetes",
            "chronic_pain",
            "gout",
            "hypothyroidism"
        ],
        "medications": [
            "allopurinol",
            "furosemide",
            "isosorbide_mononitrate",
            "ketoconazole",
            "losartan",
            "metformin",
            "naproxen",
            "nitroglycerin",
            "rivaroxaban",
            "sildenafil",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0021-1",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0021-2",
                "drug_a": "metformin",
                "drug_b": "furosemide",
                "severity": "moderate",
                "evidence": "reduced renal clearance can increase lactic acidosis risk"
            },
            {
                "interaction_id": "INT-SYN-H-0021-3",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-H-0021-4",
                "drug_a": "allopurinol",
                "drug_b": "warfarin",
                "severity": "moderate",
                "evidence": "allopurinol may enhance warfarin anticoagulation"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0021-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0021-1",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.86,
                "rationale": "reduces interaction burden from naproxen"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0022",
        "age": 92,
        "labs": {
            "egfr": 42.7,
            "creatinine": 2.6,
            "potassium": 5.5,
            "inr": 2.4,
            "alt": 166.6,
            "ast": 151.6
        },
        "diagnoses": [
            "gout",
            "hypothyroidism",
            "peripheral_artery_disease"
        ],
        "medications": [
            "allopurinol",
            "apixaban",
            "azithromycin",
            "calcium_carbonate",
            "citalopram",
            "clopidogrel",
            "levothyroxine",
            "metronidazole",
            "naproxen",
            "omeprazole",
            "prednisone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0022-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-H-0022-2",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0022-3",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0022-4",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            },
            {
                "interaction_id": "INT-SYN-H-0022-5",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0022-1",
            "REG-SYN-H-0022-2",
            "REG-SYN-H-0022-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0022-1",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.55,
                "rationale": "reduces interaction burden from omeprazole"
            },
            {
                "regimen_id": "REG-SYN-H-0022-2",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.62,
                "rationale": "reduces interaction burden from naproxen"
            },
            {
                "regimen_id": "REG-SYN-H-0022-3",
                "replace_drug": "metronidazole",
                "with_drug": "doxycycline",
                "target_condition": "infection",
                "expected_risk_delta": 0.76,
                "rationale": "reduces interaction burden from metronidazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0023",
        "age": 91,
        "labs": {
            "egfr": 41.7,
            "creatinine": 2.8,
            "potassium": 5.4,
            "inr": 3.0,
            "alt": 113.6,
            "ast": 109.0
        },
        "diagnoses": [
            "hypothyroidism",
            "peripheral_artery_disease",
            "osteoarthritis",
            "depression",
            "chronic_liver_disease"
        ],
        "medications": [
            "ciprofloxacin",
            "clopidogrel",
            "ferrous_sulfate",
            "furosemide",
            "glipizide",
            "levothyroxine",
            "metformin",
            "naproxen",
            "rivaroxaban",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0023-1",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0023-2",
                "drug_a": "metformin",
                "drug_b": "furosemide",
                "severity": "moderate",
                "evidence": "reduced renal clearance can increase lactic acidosis risk"
            },
            {
                "interaction_id": "INT-SYN-H-0023-3",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-H-0023-4",
                "drug_a": "glipizide",
                "drug_b": "ciprofloxacin",
                "severity": "moderate",
                "evidence": "dysglycemia risk from fluoroquinolone-sulfonylurea combination"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0023-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0023-1",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.63,
                "rationale": "reduces interaction burden from naproxen"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0024",
        "age": 87,
        "labs": {
            "egfr": 32.9,
            "creatinine": 2.7,
            "potassium": 4.9,
            "inr": 2.9,
            "alt": 158.0,
            "ast": 156.1
        },
        "diagnoses": [
            "hypertension",
            "anemia",
            "chronic_liver_disease",
            "heart_failure",
            "peripheral_artery_disease"
        ],
        "medications": [
            "allopurinol",
            "amiodarone",
            "calcium_carbonate",
            "glipizide",
            "levothyroxine",
            "losartan",
            "naproxen",
            "nitroglycerin",
            "paroxetine",
            "sildenafil",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0024-1",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-H-0024-2",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0024-3",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            },
            {
                "interaction_id": "INT-SYN-H-0024-4",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            }
        ],
        "required_regimens": [],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0024-1",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.47,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0025",
        "age": 89,
        "labs": {
            "egfr": 29.2,
            "creatinine": 1.8,
            "potassium": 5.2,
            "inr": 2.8,
            "alt": 189.1,
            "ast": 130.8
        },
        "diagnoses": [
            "hypothyroidism",
            "osteoarthritis",
            "anemia",
            "atrial_fibrillation",
            "depression"
        ],
        "medications": [
            "apixaban",
            "atorvastatin",
            "clarithromycin",
            "dabigatran",
            "diltiazem",
            "furosemide",
            "isosorbide_mononitrate",
            "losartan",
            "metoprolol",
            "sildenafil",
            "simvastatin",
            "spironolactone"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0025-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0025-2",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "CYP3A4 inhibition raises statin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0025-3",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-H-0025-4",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-H-0025-5",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0025-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0025-1",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.76,
                "rationale": "reduces interaction burden from clarithromycin"
            },
            {
                "regimen_id": "REG-SYN-H-0025-2",
                "replace_drug": "atorvastatin",
                "with_drug": "rosuvastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.37,
                "rationale": "modest risk reduction by replacing atorvastatin"
            },
            {
                "regimen_id": "REG-SYN-H-0025-3",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.43,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0026",
        "age": 89,
        "labs": {
            "egfr": 38.9,
            "creatinine": 2.8,
            "potassium": 5.4,
            "inr": 2.4,
            "alt": 192.7,
            "ast": 156.3
        },
        "diagnoses": [
            "type_2_diabetes",
            "chronic_kidney_disease",
            "osteoarthritis",
            "hypothyroidism",
            "heart_failure"
        ],
        "medications": [
            "amiodarone",
            "azithromycin",
            "ciprofloxacin",
            "citalopram",
            "clopidogrel",
            "digoxin",
            "ibuprofen",
            "lisinopril",
            "metoprolol",
            "omeprazole",
            "rivaroxaban",
            "sertraline",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0026-1",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0026-2",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-H-0026-3",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            },
            {
                "interaction_id": "INT-SYN-H-0026-4",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-H-0026-5",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0026-1",
            "REG-SYN-H-0026-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0026-1",
                "replace_drug": "ibuprofen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.74,
                "rationale": "reduces interaction burden from ibuprofen"
            },
            {
                "regimen_id": "REG-SYN-H-0026-2",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.31,
                "rationale": "modest risk reduction by replacing spironolactone"
            },
            {
                "regimen_id": "REG-SYN-H-0026-3",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.7,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0027",
        "age": 87,
        "labs": {
            "egfr": 43.4,
            "creatinine": 1.9,
            "potassium": 5.0,
            "inr": 3.2
        },
        "diagnoses": [
            "type_2_diabetes",
            "depression",
            "chronic_pain"
        ],
        "medications": [
            "amiodarone",
            "apixaban",
            "isosorbide_mononitrate",
            "metoprolol",
            "naproxen",
            "paroxetine",
            "sildenafil",
            "trimethoprim_sulfamethoxazole",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0027-1",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0027-2",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-H-0027-3",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            },
            {
                "interaction_id": "INT-SYN-H-0027-4",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0027-1",
            "REG-SYN-H-0027-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0027-1",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.71,
                "rationale": "reduces interaction burden from naproxen"
            },
            {
                "regimen_id": "REG-SYN-H-0027-2",
                "replace_drug": "metoprolol",
                "with_drug": "bisoprolol",
                "target_condition": "rate_control",
                "expected_risk_delta": 0.37,
                "rationale": "modest risk reduction by replacing metoprolol"
            },
            {
                "regimen_id": "REG-SYN-H-0027-3",
                "replace_drug": "trimethoprim_sulfamethoxazole",
                "with_drug": "cephalexin",
                "target_condition": "infection",
                "expected_risk_delta": 0.72,
                "rationale": "reduces interaction burden from trimethoprim_sulfamethoxazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0028",
        "age": 89,
        "labs": {
            "egfr": 30.4,
            "creatinine": 2.5,
            "potassium": 5.5,
            "inr": 2.0,
            "alt": 151.9,
            "ast": 178.6
        },
        "diagnoses": [
            "anemia",
            "coronary_artery_disease",
            "hypothyroidism",
            "nonalcoholic_steatohepatitis",
            "type_2_diabetes"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "azithromycin",
            "calcium_carbonate",
            "cetirizine",
            "citalopram",
            "fluconazole",
            "metoprolol",
            "naproxen",
            "omeprazole",
            "paroxetine",
            "ticagrelor",
            "trimethoprim_sulfamethoxazole"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0028-1",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-H-0028-2",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0028-3",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-H-0028-4",
                "drug_a": "cetirizine",
                "drug_b": "amlodipine",
                "severity": "minor",
                "evidence": "possible additive sedation in elderly"
            },
            {
                "interaction_id": "INT-SYN-H-0028-5",
                "drug_a": "metoprolol",
                "drug_b": "paroxetine",
                "severity": "moderate",
                "evidence": "CYP2D6 inhibition raises metoprolol exposure"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0028-1",
            "REG-SYN-H-0028-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0028-1",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.79,
                "rationale": "reduces interaction burden from omeprazole"
            },
            {
                "regimen_id": "REG-SYN-H-0028-2",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.59,
                "rationale": "reduces interaction burden from naproxen"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0029",
        "age": 94,
        "labs": {
            "egfr": 33.1,
            "creatinine": 2.7,
            "potassium": 5.4,
            "inr": 2.6,
            "alt": 118.1,
            "ast": 113.8
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "osteoarthritis",
            "anemia",
            "chronic_liver_disease"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "atorvastatin",
            "azithromycin",
            "citalopram",
            "furosemide",
            "ketoconazole",
            "metoprolol",
            "naproxen",
            "simvastatin",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0029-1",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0029-2",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0029-3",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-H-0029-4",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-H-0029-5",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0029-1",
            "REG-SYN-H-0029-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0029-1",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.77,
                "rationale": "reduces interaction burden from naproxen"
            },
            {
                "regimen_id": "REG-SYN-H-0029-2",
                "replace_drug": "trimethoprim_sulfamethoxazole",
                "with_drug": "cephalexin",
                "target_condition": "infection",
                "expected_risk_delta": 0.84,
                "rationale": "reduces interaction burden from trimethoprim_sulfamethoxazole"
            },
            {
                "regimen_id": "REG-SYN-H-0029-3",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.4,
                "rationale": "modest risk reduction by replacing simvastatin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0030",
        "age": 85,
        "labs": {
            "egfr": 32.1,
            "creatinine": 2.1,
            "potassium": 5.2,
            "inr": 2.7,
            "alt": 153.0,
            "ast": 166.5
        },
        "diagnoses": [
            "hypothyroidism",
            "chronic_kidney_disease",
            "coronary_artery_disease"
        ],
        "medications": [
            "allopurinol",
            "apixaban",
            "aspirin",
            "atorvastatin",
            "cetirizine",
            "clarithromycin",
            "diltiazem",
            "ibuprofen",
            "losartan",
            "metformin",
            "omeprazole",
            "spironolactone",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0030-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0030-2",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "CYP3A4 inhibition raises statin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0030-3",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-H-0030-4",
                "drug_a": "allopurinol",
                "drug_b": "warfarin",
                "severity": "moderate",
                "evidence": "allopurinol may enhance warfarin anticoagulation"
            },
            {
                "interaction_id": "INT-SYN-H-0030-5",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0030-1",
            "REG-SYN-H-0030-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0030-1",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.71,
                "rationale": "reduces interaction burden from clarithromycin"
            },
            {
                "regimen_id": "REG-SYN-H-0030-2",
                "replace_drug": "atorvastatin",
                "with_drug": "rosuvastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.39,
                "rationale": "modest risk reduction by replacing atorvastatin"
            },
            {
                "regimen_id": "REG-SYN-H-0030-3",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.62,
                "rationale": "reduces interaction burden from omeprazole"
            },
            {
                "regimen_id": "REG-SYN-H-0030-5",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.47,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0031",
        "age": 92,
        "labs": {
            "egfr": 34.0,
            "creatinine": 2.3,
            "potassium": 5.4,
            "inr": 2.8,
            "alt": 168.2,
            "ast": 155.9
        },
        "diagnoses": [
            "anemia",
            "hypertension",
            "depression"
        ],
        "medications": [
            "aspirin",
            "azithromycin",
            "clopidogrel",
            "fluconazole",
            "lisinopril",
            "naproxen",
            "omeprazole",
            "prednisone",
            "rivaroxaban",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0031-1",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0031-2",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            },
            {
                "interaction_id": "INT-SYN-H-0031-3",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0031-4",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0031-1",
            "REG-SYN-H-0031-2",
            "REG-SYN-H-0031-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0031-1",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.86,
                "rationale": "reduces interaction burden from naproxen"
            },
            {
                "regimen_id": "REG-SYN-H-0031-2",
                "replace_drug": "fluconazole",
                "with_drug": "micafungin",
                "target_condition": "infection",
                "expected_risk_delta": 0.69,
                "rationale": "reduces interaction burden from fluconazole"
            },
            {
                "regimen_id": "REG-SYN-H-0031-3",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.58,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0032",
        "age": 89,
        "labs": {
            "egfr": 33.4,
            "creatinine": 2.2,
            "potassium": 5.3,
            "inr": 2.1,
            "alt": 156.1,
            "ast": 178.4
        },
        "diagnoses": [
            "osteoarthritis",
            "atrial_fibrillation",
            "chronic_kidney_disease",
            "anemia"
        ],
        "medications": [
            "amlodipine",
            "ciprofloxacin",
            "diltiazem",
            "losartan",
            "metronidazole",
            "paroxetine",
            "sertraline",
            "simvastatin",
            "spironolactone",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0032-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0032-2",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-H-0032-3",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            },
            {
                "interaction_id": "INT-SYN-H-0032-4",
                "drug_a": "amlodipine",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive hypotension in frail adults"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0032-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0032-1",
                "replace_drug": "metronidazole",
                "with_drug": "doxycycline",
                "target_condition": "infection",
                "expected_risk_delta": 0.9,
                "rationale": "reduces interaction burden from metronidazole"
            },
            {
                "regimen_id": "REG-SYN-H-0032-2",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.46,
                "rationale": "modest risk reduction by replacing simvastatin"
            },
            {
                "regimen_id": "REG-SYN-H-0032-3",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.38,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0033",
        "age": 90,
        "labs": {
            "egfr": 30.2,
            "creatinine": 2.3,
            "potassium": 5.3,
            "inr": 2.9
        },
        "diagnoses": [
            "depression",
            "hypertension",
            "anxiety"
        ],
        "medications": [
            "allopurinol",
            "amlodipine",
            "apixaban",
            "ciprofloxacin",
            "dabigatran",
            "diclofenac",
            "ferrous_sulfate",
            "furosemide",
            "ketoconazole",
            "metformin",
            "naproxen",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0033-1",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0033-2",
                "drug_a": "amlodipine",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive hypotension in frail adults"
            },
            {
                "interaction_id": "INT-SYN-H-0033-3",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0033-4",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0033-1",
            "REG-SYN-H-0033-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0033-1",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.81,
                "rationale": "reduces interaction burden from naproxen"
            },
            {
                "regimen_id": "REG-SYN-H-0033-2",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.72,
                "rationale": "reduces interaction burden from diclofenac"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0034",
        "age": 94,
        "labs": {
            "egfr": 31.2,
            "creatinine": 2.1,
            "potassium": 5.1,
            "inr": 3.0,
            "alt": 115.2,
            "ast": 112.5
        },
        "diagnoses": [
            "heart_failure",
            "coronary_artery_disease",
            "hypothyroidism",
            "chronic_pain"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "ciprofloxacin",
            "digoxin",
            "furosemide",
            "glipizide",
            "metformin",
            "metoprolol",
            "metronidazole",
            "naproxen",
            "simvastatin",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0034-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0034-2",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-H-0034-3",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            },
            {
                "interaction_id": "INT-SYN-H-0034-4",
                "drug_a": "glipizide",
                "drug_b": "ciprofloxacin",
                "severity": "moderate",
                "evidence": "dysglycemia risk from fluoroquinolone-sulfonylurea combination"
            },
            {
                "interaction_id": "INT-SYN-H-0034-5",
                "drug_a": "metformin",
                "drug_b": "furosemide",
                "severity": "moderate",
                "evidence": "reduced renal clearance can increase lactic acidosis risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0034-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0034-1",
                "replace_drug": "metronidazole",
                "with_drug": "doxycycline",
                "target_condition": "infection",
                "expected_risk_delta": 0.7,
                "rationale": "reduces interaction burden from metronidazole"
            },
            {
                "regimen_id": "REG-SYN-H-0034-2",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.33,
                "rationale": "modest risk reduction by replacing simvastatin"
            },
            {
                "regimen_id": "REG-SYN-H-0034-3",
                "replace_drug": "metoprolol",
                "with_drug": "bisoprolol",
                "target_condition": "rate_control",
                "expected_risk_delta": 0.36,
                "rationale": "modest risk reduction by replacing metoprolol"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0035",
        "age": 86,
        "labs": {
            "egfr": 27.9,
            "creatinine": 2.4,
            "potassium": 5.3,
            "inr": 2.3,
            "alt": 121.7,
            "ast": 108.6
        },
        "diagnoses": [
            "dyslipidemia",
            "type_2_diabetes",
            "hypothyroidism",
            "peripheral_artery_disease"
        ],
        "medications": [
            "apixaban",
            "azithromycin",
            "calcium_carbonate",
            "cetirizine",
            "citalopram",
            "clarithromycin",
            "ferrous_sulfate",
            "levothyroxine",
            "losartan",
            "omeprazole",
            "spironolactone",
            "valsartan"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0035-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0035-2",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            },
            {
                "interaction_id": "INT-SYN-H-0035-3",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-H-0035-4",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0035-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0035-1",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.86,
                "rationale": "reduces interaction burden from clarithromycin"
            },
            {
                "regimen_id": "REG-SYN-H-0035-2",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.34,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0036",
        "age": 93,
        "labs": {
            "egfr": 32.3,
            "creatinine": 2.4,
            "potassium": 5.4,
            "inr": 2.9
        },
        "diagnoses": [
            "atrial_fibrillation",
            "osteoarthritis",
            "depression",
            "hypothyroidism"
        ],
        "medications": [
            "atorvastatin",
            "azithromycin",
            "diclofenac",
            "diltiazem",
            "glipizide",
            "losartan",
            "naproxen",
            "rivaroxaban",
            "spironolactone",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0036-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0036-2",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0036-3",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            },
            {
                "interaction_id": "INT-SYN-H-0036-4",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "CYP3A4 inhibition raises statin concentration"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0036-1",
            "REG-SYN-H-0036-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0036-1",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.87,
                "rationale": "reduces interaction burden from diclofenac"
            },
            {
                "regimen_id": "REG-SYN-H-0036-2",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.78,
                "rationale": "reduces interaction burden from naproxen"
            },
            {
                "regimen_id": "REG-SYN-H-0036-3",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.46,
                "rationale": "modest risk reduction by replacing spironolactone"
            },
            {
                "regimen_id": "REG-SYN-H-0036-4",
                "replace_drug": "atorvastatin",
                "with_drug": "rosuvastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.38,
                "rationale": "modest risk reduction by replacing atorvastatin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0037",
        "age": 92,
        "labs": {
            "egfr": 36.4,
            "creatinine": 2.0,
            "potassium": 5.5,
            "inr": 2.9,
            "alt": 118.1,
            "ast": 111.1
        },
        "diagnoses": [
            "gout",
            "hypothyroidism",
            "depression",
            "osteoarthritis"
        ],
        "medications": [
            "azithromycin",
            "calcium_carbonate",
            "dabigatran",
            "ferrous_sulfate",
            "furosemide",
            "ketoconazole",
            "levothyroxine",
            "metformin",
            "metoprolol",
            "omeprazole",
            "prednisone",
            "sertraline",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0037-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0037-2",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-H-0037-3",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            },
            {
                "interaction_id": "INT-SYN-H-0037-4",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            },
            {
                "interaction_id": "INT-SYN-H-0037-5",
                "drug_a": "metformin",
                "drug_b": "furosemide",
                "severity": "moderate",
                "evidence": "reduced renal clearance can increase lactic acidosis risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0037-1",
                "replace_drug": "metoprolol",
                "with_drug": "bisoprolol",
                "target_condition": "rate_control",
                "expected_risk_delta": 0.43,
                "rationale": "modest risk reduction by replacing metoprolol"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0038",
        "age": 90,
        "labs": {
            "egfr": 36.1,
            "creatinine": 2.5,
            "potassium": 5.2,
            "inr": 3.1,
            "alt": 188.0,
            "ast": 174.5
        },
        "diagnoses": [
            "coronary_artery_disease",
            "dyslipidemia",
            "chronic_liver_disease",
            "type_2_diabetes"
        ],
        "medications": [
            "apixaban",
            "ciprofloxacin",
            "clarithromycin",
            "clopidogrel",
            "dabigatran",
            "diclofenac",
            "glipizide",
            "isosorbide_mononitrate",
            "ketoconazole",
            "linezolid",
            "naproxen",
            "omeprazole",
            "sertraline",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0038-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0038-2",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0038-3",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            },
            {
                "interaction_id": "INT-SYN-H-0038-4",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-H-0038-5",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0038-1",
            "REG-SYN-H-0038-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0038-1",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.65,
                "rationale": "reduces interaction burden from clarithromycin"
            },
            {
                "regimen_id": "REG-SYN-H-0038-2",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.58,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0039",
        "age": 91,
        "labs": {
            "egfr": 32.8,
            "creatinine": 2.2,
            "potassium": 5.1,
            "inr": 3.0
        },
        "diagnoses": [
            "depression",
            "type_2_diabetes",
            "anemia",
            "coronary_artery_disease"
        ],
        "medications": [
            "allopurinol",
            "apixaban",
            "calcium_carbonate",
            "cetirizine",
            "clarithromycin",
            "clopidogrel",
            "furosemide",
            "levothyroxine",
            "lisinopril",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0039-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0039-2",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-H-0039-3",
                "drug_a": "allopurinol",
                "drug_b": "warfarin",
                "severity": "moderate",
                "evidence": "allopurinol may enhance warfarin anticoagulation"
            },
            {
                "interaction_id": "INT-SYN-H-0039-4",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0039-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0039-1",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.63,
                "rationale": "reduces interaction burden from clarithromycin"
            },
            {
                "regimen_id": "REG-SYN-H-0039-3",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.37,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0040",
        "age": 87,
        "labs": {
            "egfr": 29.2,
            "creatinine": 2.5,
            "potassium": 5.4,
            "inr": 2.8,
            "alt": 111.7,
            "ast": 110.3
        },
        "diagnoses": [
            "nonalcoholic_steatohepatitis",
            "osteoarthritis",
            "coronary_artery_disease"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "aspirin",
            "calcium_carbonate",
            "dabigatran",
            "diclofenac",
            "ketoconazole",
            "levothyroxine",
            "losartan",
            "omeprazole",
            "simvastatin",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0040-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0040-2",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            },
            {
                "interaction_id": "INT-SYN-H-0040-3",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-H-0040-4",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-H-0040-5",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0040-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0040-1",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.89,
                "rationale": "reduces interaction burden from diclofenac"
            },
            {
                "regimen_id": "REG-SYN-H-0040-2",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.27,
                "rationale": "modest risk reduction by replacing spironolactone"
            },
            {
                "regimen_id": "REG-SYN-H-0040-3",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.38,
                "rationale": "modest risk reduction by replacing simvastatin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0041",
        "age": 95,
        "labs": {
            "egfr": 31.3,
            "creatinine": 2.8,
            "potassium": 5.3,
            "inr": 2.9
        },
        "diagnoses": [
            "depression",
            "atrial_fibrillation",
            "nonalcoholic_steatohepatitis",
            "peripheral_artery_disease",
            "hypertension"
        ],
        "medications": [
            "allopurinol",
            "dabigatran",
            "diclofenac",
            "furosemide",
            "metformin",
            "metoprolol",
            "omeprazole",
            "sertraline",
            "sildenafil",
            "ticagrelor",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0041-1",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-H-0041-2",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            },
            {
                "interaction_id": "INT-SYN-H-0041-3",
                "drug_a": "allopurinol",
                "drug_b": "warfarin",
                "severity": "moderate",
                "evidence": "allopurinol may enhance warfarin anticoagulation"
            },
            {
                "interaction_id": "INT-SYN-H-0041-4",
                "drug_a": "metformin",
                "drug_b": "furosemide",
                "severity": "moderate",
                "evidence": "reduced renal clearance can increase lactic acidosis risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0041-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0041-1",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.63,
                "rationale": "reduces interaction burden from omeprazole"
            },
            {
                "regimen_id": "REG-SYN-H-0041-2",
                "replace_drug": "metoprolol",
                "with_drug": "bisoprolol",
                "target_condition": "rate_control",
                "expected_risk_delta": 0.47,
                "rationale": "modest risk reduction by replacing metoprolol"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0042",
        "age": 94,
        "labs": {
            "egfr": 26.6,
            "creatinine": 2.7,
            "potassium": 5.4,
            "inr": 2.1,
            "alt": 122.1,
            "ast": 113.7
        },
        "diagnoses": [
            "gout",
            "anxiety",
            "depression",
            "chronic_liver_disease",
            "anemia"
        ],
        "medications": [
            "amlodipine",
            "aspirin",
            "azithromycin",
            "cetirizine",
            "citalopram",
            "furosemide",
            "nitroglycerin",
            "prednisone",
            "sertraline",
            "sildenafil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0042-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0042-2",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-H-0042-3",
                "drug_a": "cetirizine",
                "drug_b": "amlodipine",
                "severity": "minor",
                "evidence": "possible additive sedation in elderly"
            },
            {
                "interaction_id": "INT-SYN-H-0042-4",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0042-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0042-1",
                "replace_drug": "aspirin",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.71,
                "rationale": "reduces interaction burden from aspirin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0043",
        "age": 95,
        "labs": {
            "egfr": 36.2,
            "creatinine": 2.0,
            "potassium": 5.4,
            "inr": 3.1
        },
        "diagnoses": [
            "hypertension",
            "type_2_diabetes",
            "chronic_pain"
        ],
        "medications": [
            "allopurinol",
            "amiodarone",
            "amlodipine",
            "azithromycin",
            "dabigatran",
            "diclofenac",
            "ketoconazole",
            "linezolid",
            "prednisone",
            "sertraline",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0043-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0043-2",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            },
            {
                "interaction_id": "INT-SYN-H-0043-3",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0043-4",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0043-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0043-1",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.71,
                "rationale": "reduces interaction burden from diclofenac"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0044",
        "age": 91,
        "labs": {
            "egfr": 37.2,
            "creatinine": 1.9,
            "potassium": 4.9,
            "inr": 2.4
        },
        "diagnoses": [
            "anxiety",
            "chronic_pain",
            "chronic_kidney_disease"
        ],
        "medications": [
            "amiodarone",
            "amlodipine",
            "ciprofloxacin",
            "clopidogrel",
            "diclofenac",
            "furosemide",
            "isosorbide_mononitrate",
            "linezolid",
            "metformin",
            "sertraline",
            "simvastatin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0044-1",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-H-0044-2",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0044-3",
                "drug_a": "metformin",
                "drug_b": "furosemide",
                "severity": "moderate",
                "evidence": "reduced renal clearance can increase lactic acidosis risk"
            },
            {
                "interaction_id": "INT-SYN-H-0044-4",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0044-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0044-1",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.72,
                "rationale": "reduces interaction burden from diclofenac"
            },
            {
                "regimen_id": "REG-SYN-H-0044-3",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.29,
                "rationale": "modest risk reduction by replacing simvastatin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0045",
        "age": 89,
        "labs": {
            "egfr": 37.2,
            "creatinine": 2.6,
            "potassium": 5.5,
            "inr": 2.1
        },
        "diagnoses": [
            "hypothyroidism",
            "coronary_artery_disease",
            "osteoarthritis",
            "heart_failure"
        ],
        "medications": [
            "amlodipine",
            "atorvastatin",
            "azithromycin",
            "ciprofloxacin",
            "levothyroxine",
            "linezolid",
            "metoprolol",
            "paroxetine",
            "prednisone",
            "sertraline",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0045-1",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-H-0045-2",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            },
            {
                "interaction_id": "INT-SYN-H-0045-3",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            },
            {
                "interaction_id": "INT-SYN-H-0045-4",
                "drug_a": "metoprolol",
                "drug_b": "paroxetine",
                "severity": "moderate",
                "evidence": "CYP2D6 inhibition raises metoprolol exposure"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0046",
        "age": 86,
        "labs": {
            "egfr": 31.2,
            "creatinine": 1.9,
            "potassium": 5.0,
            "inr": 2.2,
            "alt": 110.8,
            "ast": 104.7
        },
        "diagnoses": [
            "gout",
            "hypothyroidism",
            "heart_failure"
        ],
        "medications": [
            "amiodarone",
            "amlodipine",
            "apixaban",
            "azithromycin",
            "ciprofloxacin",
            "citalopram",
            "diclofenac",
            "diltiazem",
            "lisinopril",
            "naproxen",
            "prednisone",
            "rivaroxaban",
            "sildenafil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0046-1",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0046-2",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-H-0046-3",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0046-4",
                "drug_a": "amlodipine",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive hypotension in frail adults"
            },
            {
                "interaction_id": "INT-SYN-H-0046-5",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0046-1",
            "REG-SYN-H-0046-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0046-1",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.72,
                "rationale": "reduces interaction burden from diclofenac"
            },
            {
                "regimen_id": "REG-SYN-H-0046-2",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.57,
                "rationale": "reduces interaction burden from naproxen"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0047",
        "age": 91,
        "labs": {
            "egfr": 31.8,
            "creatinine": 1.9,
            "potassium": 5.3,
            "inr": 2.5
        },
        "diagnoses": [
            "heart_failure",
            "anxiety",
            "type_2_diabetes",
            "nonalcoholic_steatohepatitis",
            "chronic_pain"
        ],
        "medications": [
            "azithromycin",
            "calcium_carbonate",
            "clopidogrel",
            "glipizide",
            "levothyroxine",
            "losartan",
            "metformin",
            "metronidazole",
            "omeprazole",
            "prednisone",
            "trimethoprim_sulfamethoxazole",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0047-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-H-0047-2",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            },
            {
                "interaction_id": "INT-SYN-H-0047-3",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            },
            {
                "interaction_id": "INT-SYN-H-0047-4",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0047-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0047-1",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.87,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0048",
        "age": 95,
        "labs": {
            "egfr": 31.2,
            "creatinine": 2.0,
            "potassium": 4.8,
            "inr": 2.9,
            "alt": 197.1,
            "ast": 175.7
        },
        "diagnoses": [
            "atrial_fibrillation",
            "depression",
            "chronic_liver_disease"
        ],
        "medications": [
            "amiodarone",
            "amlodipine",
            "atorvastatin",
            "calcium_carbonate",
            "ciprofloxacin",
            "dabigatran",
            "diltiazem",
            "glipizide",
            "isosorbide_mononitrate",
            "metformin",
            "metoprolol",
            "paroxetine",
            "sildenafil",
            "simvastatin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0048-1",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-H-0048-2",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-H-0048-3",
                "drug_a": "glipizide",
                "drug_b": "ciprofloxacin",
                "severity": "moderate",
                "evidence": "dysglycemia risk from fluoroquinolone-sulfonylurea combination"
            },
            {
                "interaction_id": "INT-SYN-H-0048-4",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "CYP3A4 inhibition raises statin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0048-5",
                "drug_a": "metoprolol",
                "drug_b": "paroxetine",
                "severity": "moderate",
                "evidence": "CYP2D6 inhibition raises metoprolol exposure"
            }
        ],
        "required_regimens": [],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0048-1",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.31,
                "rationale": "modest risk reduction by replacing simvastatin"
            },
            {
                "regimen_id": "REG-SYN-H-0048-3",
                "replace_drug": "atorvastatin",
                "with_drug": "rosuvastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.43,
                "rationale": "modest risk reduction by replacing atorvastatin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0049",
        "age": 86,
        "labs": {
            "egfr": 25.4,
            "creatinine": 2.3,
            "potassium": 4.8,
            "inr": 2.7,
            "alt": 188.9,
            "ast": 167.7
        },
        "diagnoses": [
            "anemia",
            "atrial_fibrillation",
            "depression"
        ],
        "medications": [
            "allopurinol",
            "amlodipine",
            "apixaban",
            "azithromycin",
            "diclofenac",
            "furosemide",
            "linezolid",
            "metoprolol",
            "metronidazole",
            "sertraline",
            "simvastatin",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0049-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0049-2",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-H-0049-3",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0049-4",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-H-0049-5",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0049-1",
            "REG-SYN-H-0049-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0049-1",
                "replace_drug": "metronidazole",
                "with_drug": "doxycycline",
                "target_condition": "infection",
                "expected_risk_delta": 0.82,
                "rationale": "reduces interaction burden from metronidazole"
            },
            {
                "regimen_id": "REG-SYN-H-0049-2",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.71,
                "rationale": "reduces interaction burden from diclofenac"
            },
            {
                "regimen_id": "REG-SYN-H-0049-3",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.41,
                "rationale": "modest risk reduction by replacing simvastatin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0050",
        "age": 89,
        "labs": {
            "egfr": 35.8,
            "creatinine": 2.3,
            "potassium": 5.2,
            "inr": 3.1,
            "alt": 174.7,
            "ast": 160.6
        },
        "diagnoses": [
            "coronary_artery_disease",
            "chronic_kidney_disease",
            "type_2_diabetes"
        ],
        "medications": [
            "calcium_carbonate",
            "ciprofloxacin",
            "fluconazole",
            "furosemide",
            "glipizide",
            "ibuprofen",
            "levothyroxine",
            "losartan",
            "metformin",
            "metoprolol",
            "metronidazole",
            "spironolactone",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0050-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0050-2",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-H-0050-3",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-H-0050-4",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            },
            {
                "interaction_id": "INT-SYN-H-0050-5",
                "drug_a": "glipizide",
                "drug_b": "ciprofloxacin",
                "severity": "moderate",
                "evidence": "dysglycemia risk from fluoroquinolone-sulfonylurea combination"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0050-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0050-1",
                "replace_drug": "metronidazole",
                "with_drug": "doxycycline",
                "target_condition": "infection",
                "expected_risk_delta": 0.75,
                "rationale": "reduces interaction burden from metronidazole"
            },
            {
                "regimen_id": "REG-SYN-H-0050-2",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.3,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0051",
        "age": 93,
        "labs": {
            "egfr": 40.5,
            "creatinine": 2.4,
            "potassium": 5.3,
            "inr": 2.3,
            "alt": 183.5,
            "ast": 167.5
        },
        "diagnoses": [
            "atrial_fibrillation",
            "osteoarthritis",
            "chronic_kidney_disease"
        ],
        "medications": [
            "apixaban",
            "diclofenac",
            "ferrous_sulfate",
            "ibuprofen",
            "isosorbide_mononitrate",
            "ketoconazole",
            "levothyroxine",
            "losartan",
            "metronidazole",
            "naproxen",
            "rivaroxaban",
            "valsartan",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0051-1",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0051-2",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            },
            {
                "interaction_id": "INT-SYN-H-0051-3",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0051-4",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-H-0051-5",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0051-1",
            "REG-SYN-H-0051-2",
            "REG-SYN-H-0051-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0051-1",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.8,
                "rationale": "reduces interaction burden from diclofenac"
            },
            {
                "regimen_id": "REG-SYN-H-0051-2",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.65,
                "rationale": "reduces interaction burden from naproxen"
            },
            {
                "regimen_id": "REG-SYN-H-0051-3",
                "replace_drug": "metronidazole",
                "with_drug": "doxycycline",
                "target_condition": "infection",
                "expected_risk_delta": 0.88,
                "rationale": "reduces interaction burden from metronidazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0052",
        "age": 88,
        "labs": {
            "egfr": 30.8,
            "creatinine": 2.4,
            "potassium": 5.3,
            "inr": 2.6
        },
        "diagnoses": [
            "anxiety",
            "depression",
            "heart_failure",
            "hypertension",
            "osteoarthritis"
        ],
        "medications": [
            "azithromycin",
            "citalopram",
            "clopidogrel",
            "ketoconazole",
            "lisinopril",
            "metoprolol",
            "sertraline",
            "spironolactone",
            "ticagrelor",
            "trimethoprim_sulfamethoxazole",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0052-1",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0052-2",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            },
            {
                "interaction_id": "INT-SYN-H-0052-3",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            },
            {
                "interaction_id": "INT-SYN-H-0052-4",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0052-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0052-1",
                "replace_drug": "trimethoprim_sulfamethoxazole",
                "with_drug": "cephalexin",
                "target_condition": "infection",
                "expected_risk_delta": 0.7,
                "rationale": "reduces interaction burden from trimethoprim_sulfamethoxazole"
            },
            {
                "regimen_id": "REG-SYN-H-0052-2",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.43,
                "rationale": "modest risk reduction by replacing spironolactone"
            },
            {
                "regimen_id": "REG-SYN-H-0052-3",
                "replace_drug": "metoprolol",
                "with_drug": "bisoprolol",
                "target_condition": "rate_control",
                "expected_risk_delta": 0.47,
                "rationale": "modest risk reduction by replacing metoprolol"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0053",
        "age": 94,
        "labs": {
            "egfr": 37.5,
            "creatinine": 2.2,
            "potassium": 5.4,
            "inr": 2.4,
            "alt": 124.6,
            "ast": 101.0
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "dyslipidemia",
            "heart_failure"
        ],
        "medications": [
            "apixaban",
            "aspirin",
            "azithromycin",
            "ciprofloxacin",
            "ferrous_sulfate",
            "furosemide",
            "glipizide",
            "metformin",
            "metronidazole",
            "prednisone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0053-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0053-2",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            },
            {
                "interaction_id": "INT-SYN-H-0053-3",
                "drug_a": "metformin",
                "drug_b": "furosemide",
                "severity": "moderate",
                "evidence": "reduced renal clearance can increase lactic acidosis risk"
            },
            {
                "interaction_id": "INT-SYN-H-0053-4",
                "drug_a": "glipizide",
                "drug_b": "ciprofloxacin",
                "severity": "moderate",
                "evidence": "dysglycemia risk from fluoroquinolone-sulfonylurea combination"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0053-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0053-1",
                "replace_drug": "metronidazole",
                "with_drug": "doxycycline",
                "target_condition": "infection",
                "expected_risk_delta": 0.75,
                "rationale": "reduces interaction burden from metronidazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0054",
        "age": 92,
        "labs": {
            "egfr": 35.2,
            "creatinine": 1.9,
            "potassium": 5.2,
            "inr": 2.9
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "gout",
            "anxiety",
            "hypothyroidism",
            "anemia"
        ],
        "medications": [
            "allopurinol",
            "apixaban",
            "azithromycin",
            "calcium_carbonate",
            "ciprofloxacin",
            "clarithromycin",
            "dabigatran",
            "glipizide",
            "ketoconazole",
            "metoprolol",
            "prednisone"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0054-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0054-2",
                "drug_a": "glipizide",
                "drug_b": "ciprofloxacin",
                "severity": "moderate",
                "evidence": "dysglycemia risk from fluoroquinolone-sulfonylurea combination"
            },
            {
                "interaction_id": "INT-SYN-H-0054-3",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            },
            {
                "interaction_id": "INT-SYN-H-0054-4",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0054-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0054-2",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.81,
                "rationale": "reduces interaction burden from clarithromycin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0055",
        "age": 89,
        "labs": {
            "egfr": 29.7,
            "creatinine": 2.4,
            "potassium": 5.4,
            "inr": 2.4
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "hypothyroidism",
            "anemia",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "apixaban",
            "atorvastatin",
            "azithromycin",
            "citalopram",
            "dabigatran",
            "diltiazem",
            "ketoconazole",
            "metformin",
            "metoprolol",
            "naproxen",
            "ticagrelor",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0055-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0055-2",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            },
            {
                "interaction_id": "INT-SYN-H-0055-3",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "CYP3A4 inhibition raises statin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0055-4",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0055-5",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0055-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0055-1",
                "replace_drug": "metoprolol",
                "with_drug": "bisoprolol",
                "target_condition": "rate_control",
                "expected_risk_delta": 0.39,
                "rationale": "modest risk reduction by replacing metoprolol"
            },
            {
                "regimen_id": "REG-SYN-H-0055-2",
                "replace_drug": "atorvastatin",
                "with_drug": "rosuvastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.47,
                "rationale": "modest risk reduction by replacing atorvastatin"
            },
            {
                "regimen_id": "REG-SYN-H-0055-3",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.56,
                "rationale": "reduces interaction burden from naproxen"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0056",
        "age": 87,
        "labs": {
            "egfr": 32.8,
            "creatinine": 2.2,
            "potassium": 5.0,
            "inr": 2.6,
            "alt": 145.1,
            "ast": 143.8
        },
        "diagnoses": [
            "heart_failure",
            "anxiety",
            "dyslipidemia",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "amiodarone",
            "amlodipine",
            "calcium_carbonate",
            "diclofenac",
            "levothyroxine",
            "lisinopril",
            "metoprolol",
            "naproxen",
            "omeprazole",
            "simvastatin",
            "spironolactone",
            "ticagrelor",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0056-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0056-2",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            },
            {
                "interaction_id": "INT-SYN-H-0056-3",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            },
            {
                "interaction_id": "INT-SYN-H-0056-4",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-H-0056-5",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0056-1",
            "REG-SYN-H-0056-4"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0056-1",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.58,
                "rationale": "reduces interaction burden from diclofenac"
            },
            {
                "regimen_id": "REG-SYN-H-0056-2",
                "replace_drug": "metoprolol",
                "with_drug": "bisoprolol",
                "target_condition": "rate_control",
                "expected_risk_delta": 0.41,
                "rationale": "modest risk reduction by replacing metoprolol"
            },
            {
                "regimen_id": "REG-SYN-H-0056-3",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.46,
                "rationale": "modest risk reduction by replacing spironolactone"
            },
            {
                "regimen_id": "REG-SYN-H-0056-4",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.84,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0057",
        "age": 88,
        "labs": {
            "egfr": 39.9,
            "creatinine": 2.5,
            "potassium": 5.1,
            "inr": 2.7,
            "alt": 161.1,
            "ast": 162.6
        },
        "diagnoses": [
            "hypothyroidism",
            "chronic_pain",
            "anemia",
            "peripheral_artery_disease"
        ],
        "medications": [
            "allopurinol",
            "amiodarone",
            "apixaban",
            "clopidogrel",
            "diclofenac",
            "digoxin",
            "diltiazem",
            "furosemide",
            "isosorbide_mononitrate",
            "metoprolol",
            "omeprazole",
            "prednisone",
            "sildenafil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0057-1",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-H-0057-2",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-H-0057-3",
                "drug_a": "allopurinol",
                "drug_b": "warfarin",
                "severity": "moderate",
                "evidence": "allopurinol may enhance warfarin anticoagulation"
            },
            {
                "interaction_id": "INT-SYN-H-0057-4",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0057-5",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0057-2",
            "REG-SYN-H-0057-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0057-2",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.79,
                "rationale": "reduces interaction burden from diclofenac"
            },
            {
                "regimen_id": "REG-SYN-H-0057-3",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.82,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0058",
        "age": 92,
        "labs": {
            "egfr": 38.9,
            "creatinine": 1.9,
            "potassium": 4.8,
            "inr": 2.5
        },
        "diagnoses": [
            "dyslipidemia",
            "type_2_diabetes",
            "chronic_liver_disease",
            "gout"
        ],
        "medications": [
            "allopurinol",
            "apixaban",
            "aspirin",
            "clarithromycin",
            "fluconazole",
            "furosemide",
            "isosorbide_mononitrate",
            "metoprolol",
            "paroxetine",
            "sertraline",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0058-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0058-2",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-H-0058-3",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0058-4",
                "drug_a": "aspirin",
                "drug_b": "sertraline",
                "severity": "minor",
                "evidence": "increased bleeding tendency, amplified in frailty"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0058-1",
            "REG-SYN-H-0058-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0058-1",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.89,
                "rationale": "reduces interaction burden from clarithromycin"
            },
            {
                "regimen_id": "REG-SYN-H-0058-2",
                "replace_drug": "fluconazole",
                "with_drug": "micafungin",
                "target_condition": "infection",
                "expected_risk_delta": 0.67,
                "rationale": "reduces interaction burden from fluconazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0059",
        "age": 92,
        "labs": {
            "egfr": 33.4,
            "creatinine": 2.0,
            "potassium": 4.9,
            "inr": 2.4
        },
        "diagnoses": [
            "hypothyroidism",
            "chronic_liver_disease",
            "nonalcoholic_steatohepatitis",
            "atrial_fibrillation",
            "type_2_diabetes"
        ],
        "medications": [
            "amlodipine",
            "azithromycin",
            "furosemide",
            "losartan",
            "metoprolol",
            "metronidazole",
            "naproxen",
            "rivaroxaban",
            "simvastatin",
            "spironolactone",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0059-1",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0059-2",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-H-0059-3",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-H-0059-4",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            },
            {
                "interaction_id": "INT-SYN-H-0059-5",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0059-1",
            "REG-SYN-H-0059-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0059-1",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.86,
                "rationale": "reduces interaction burden from naproxen"
            },
            {
                "regimen_id": "REG-SYN-H-0059-2",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.32,
                "rationale": "modest risk reduction by replacing simvastatin"
            },
            {
                "regimen_id": "REG-SYN-H-0059-3",
                "replace_drug": "metronidazole",
                "with_drug": "doxycycline",
                "target_condition": "infection",
                "expected_risk_delta": 0.58,
                "rationale": "reduces interaction burden from metronidazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0060",
        "age": 94,
        "labs": {
            "egfr": 42.2,
            "creatinine": 2.2,
            "potassium": 5.3,
            "inr": 3.1,
            "alt": 171.0,
            "ast": 153.2
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "anemia",
            "anxiety"
        ],
        "medications": [
            "amiodarone",
            "amlodipine",
            "apixaban",
            "ciprofloxacin",
            "clarithromycin",
            "dabigatran",
            "digoxin",
            "ibuprofen",
            "ketoconazole",
            "linezolid",
            "sertraline",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0060-1",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0060-2",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0060-3",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0060-4",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-H-0060-5",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0060-1",
            "REG-SYN-H-0060-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0060-1",
                "replace_drug": "ibuprofen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.81,
                "rationale": "reduces interaction burden from ibuprofen"
            },
            {
                "regimen_id": "REG-SYN-H-0060-2",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.66,
                "rationale": "reduces interaction burden from clarithromycin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0061",
        "age": 94,
        "labs": {
            "egfr": 41.5,
            "creatinine": 1.9,
            "potassium": 5.1,
            "inr": 2.6,
            "alt": 194.3,
            "ast": 135.3
        },
        "diagnoses": [
            "hypothyroidism",
            "anemia",
            "hypertension"
        ],
        "medications": [
            "apixaban",
            "aspirin",
            "azithromycin",
            "clarithromycin",
            "diltiazem",
            "ferrous_sulfate",
            "isosorbide_mononitrate",
            "levothyroxine",
            "linezolid",
            "losartan",
            "prednisone",
            "sertraline",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0061-1",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-H-0061-2",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            },
            {
                "interaction_id": "INT-SYN-H-0061-3",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            },
            {
                "interaction_id": "INT-SYN-H-0061-4",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0061-5",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0061-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0061-1",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.62,
                "rationale": "reduces interaction burden from clarithromycin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0062",
        "age": 87,
        "labs": {
            "egfr": 43.8,
            "creatinine": 2.5,
            "potassium": 5.0,
            "inr": 2.4
        },
        "diagnoses": [
            "anemia",
            "chronic_pain",
            "chronic_liver_disease",
            "atrial_fibrillation"
        ],
        "medications": [
            "amlodipine",
            "cetirizine",
            "fluconazole",
            "furosemide",
            "glipizide",
            "losartan",
            "metoprolol",
            "omeprazole",
            "paroxetine",
            "sertraline",
            "ticagrelor",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0062-1",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-H-0062-2",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            },
            {
                "interaction_id": "INT-SYN-H-0062-3",
                "drug_a": "cetirizine",
                "drug_b": "amlodipine",
                "severity": "minor",
                "evidence": "possible additive sedation in elderly"
            },
            {
                "interaction_id": "INT-SYN-H-0062-4",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0062-5",
                "drug_a": "metoprolol",
                "drug_b": "paroxetine",
                "severity": "moderate",
                "evidence": "CYP2D6 inhibition raises metoprolol exposure"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0062-1",
            "REG-SYN-H-0062-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0062-1",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.85,
                "rationale": "reduces interaction burden from omeprazole"
            },
            {
                "regimen_id": "REG-SYN-H-0062-2",
                "replace_drug": "fluconazole",
                "with_drug": "micafungin",
                "target_condition": "infection",
                "expected_risk_delta": 0.83,
                "rationale": "reduces interaction burden from fluconazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0063",
        "age": 93,
        "labs": {
            "egfr": 33.3,
            "creatinine": 2.7,
            "potassium": 5.2,
            "inr": 2.5
        },
        "diagnoses": [
            "anemia",
            "chronic_liver_disease",
            "coronary_artery_disease",
            "anxiety"
        ],
        "medications": [
            "apixaban",
            "atorvastatin",
            "diclofenac",
            "digoxin",
            "diltiazem",
            "fluconazole",
            "levothyroxine",
            "simvastatin",
            "spironolactone",
            "trimethoprim_sulfamethoxazole",
            "valsartan",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0063-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0063-2",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "CYP3A4 inhibition raises statin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0063-3",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0063-4",
                "drug_a": "digoxin",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "P-gp inhibition can raise digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0063-5",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0063-1",
            "REG-SYN-H-0063-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0063-1",
                "replace_drug": "fluconazole",
                "with_drug": "micafungin",
                "target_condition": "infection",
                "expected_risk_delta": 0.85,
                "rationale": "reduces interaction burden from fluconazole"
            },
            {
                "regimen_id": "REG-SYN-H-0063-2",
                "replace_drug": "atorvastatin",
                "with_drug": "rosuvastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.28,
                "rationale": "modest risk reduction by replacing atorvastatin"
            },
            {
                "regimen_id": "REG-SYN-H-0063-3",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.79,
                "rationale": "reduces interaction burden from diclofenac"
            },
            {
                "regimen_id": "REG-SYN-H-0063-4",
                "replace_drug": "digoxin",
                "with_drug": "bisoprolol",
                "target_condition": "rate_control",
                "expected_risk_delta": 0.32,
                "rationale": "modest risk reduction by replacing digoxin"
            },
            {
                "regimen_id": "REG-SYN-H-0063-5",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.32,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0064",
        "age": 93,
        "labs": {
            "egfr": 31.7,
            "creatinine": 2.3,
            "potassium": 5.1,
            "inr": 2.6
        },
        "diagnoses": [
            "nonalcoholic_steatohepatitis",
            "peripheral_artery_disease",
            "heart_failure"
        ],
        "medications": [
            "clarithromycin",
            "dabigatran",
            "ferrous_sulfate",
            "furosemide",
            "ibuprofen",
            "ketoconazole",
            "levothyroxine",
            "metformin",
            "nitroglycerin",
            "omeprazole",
            "sildenafil",
            "spironolactone",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0064-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0064-2",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0064-3",
                "drug_a": "metformin",
                "drug_b": "furosemide",
                "severity": "moderate",
                "evidence": "reduced renal clearance can increase lactic acidosis risk"
            },
            {
                "interaction_id": "INT-SYN-H-0064-4",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-H-0064-5",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0064-1",
            "REG-SYN-H-0064-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0064-1",
                "replace_drug": "ibuprofen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.86,
                "rationale": "reduces interaction burden from ibuprofen"
            },
            {
                "regimen_id": "REG-SYN-H-0064-3",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.84,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0065",
        "age": 90,
        "labs": {
            "egfr": 32.1,
            "creatinine": 2.7,
            "potassium": 4.9,
            "inr": 3.2,
            "alt": 157.4,
            "ast": 137.7
        },
        "diagnoses": [
            "anemia",
            "hypertension",
            "gout",
            "chronic_liver_disease"
        ],
        "medications": [
            "amiodarone",
            "amlodipine",
            "apixaban",
            "calcium_carbonate",
            "cetirizine",
            "digoxin",
            "levothyroxine",
            "sertraline",
            "spironolactone",
            "trimethoprim_sulfamethoxazole",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0065-1",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0065-2",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0065-3",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            },
            {
                "interaction_id": "INT-SYN-H-0065-4",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-H-0065-5",
                "drug_a": "cetirizine",
                "drug_b": "amlodipine",
                "severity": "minor",
                "evidence": "possible additive sedation in elderly"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0065-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0065-1",
                "replace_drug": "trimethoprim_sulfamethoxazole",
                "with_drug": "cephalexin",
                "target_condition": "infection",
                "expected_risk_delta": 0.71,
                "rationale": "reduces interaction burden from trimethoprim_sulfamethoxazole"
            },
            {
                "regimen_id": "REG-SYN-H-0065-2",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.38,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0066",
        "age": 92,
        "labs": {
            "egfr": 40.5,
            "creatinine": 2.1,
            "potassium": 5.0,
            "inr": 2.9,
            "alt": 185.5,
            "ast": 164.0
        },
        "diagnoses": [
            "hypertension",
            "anxiety",
            "atrial_fibrillation",
            "type_2_diabetes",
            "heart_failure"
        ],
        "medications": [
            "amiodarone",
            "amlodipine",
            "azithromycin",
            "ciprofloxacin",
            "digoxin",
            "furosemide",
            "linezolid",
            "naproxen",
            "nitroglycerin",
            "prednisone",
            "rivaroxaban",
            "sertraline"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0066-1",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0066-2",
                "drug_a": "amlodipine",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive hypotension in frail adults"
            },
            {
                "interaction_id": "INT-SYN-H-0066-3",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-H-0066-4",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0066-5",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0066-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0066-1",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.68,
                "rationale": "reduces interaction burden from naproxen"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0067",
        "age": 86,
        "labs": {
            "egfr": 25.5,
            "creatinine": 2.0,
            "potassium": 5.4,
            "inr": 2.4,
            "alt": 140.7,
            "ast": 154.2
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "heart_failure",
            "depression",
            "dyslipidemia",
            "chronic_pain"
        ],
        "medications": [
            "amlodipine",
            "azithromycin",
            "glipizide",
            "linezolid",
            "nitroglycerin",
            "prednisone",
            "sertraline",
            "sildenafil",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0067-1",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-H-0067-2",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-H-0067-3",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0067-4",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0067-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0067-1",
                "replace_drug": "trimethoprim_sulfamethoxazole",
                "with_drug": "cephalexin",
                "target_condition": "infection",
                "expected_risk_delta": 0.61,
                "rationale": "reduces interaction burden from trimethoprim_sulfamethoxazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0068",
        "age": 92,
        "labs": {
            "egfr": 37.7,
            "creatinine": 2.0,
            "potassium": 5.4,
            "inr": 3.0
        },
        "diagnoses": [
            "osteoarthritis",
            "chronic_liver_disease",
            "hypothyroidism",
            "chronic_kidney_disease"
        ],
        "medications": [
            "amlodipine",
            "ciprofloxacin",
            "dabigatran",
            "diclofenac",
            "losartan",
            "naproxen",
            "rivaroxaban",
            "simvastatin",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0068-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0068-2",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-H-0068-3",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            },
            {
                "interaction_id": "INT-SYN-H-0068-4",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0068-1",
            "REG-SYN-H-0068-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0068-1",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.73,
                "rationale": "reduces interaction burden from diclofenac"
            },
            {
                "regimen_id": "REG-SYN-H-0068-2",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.45,
                "rationale": "modest risk reduction by replacing simvastatin"
            },
            {
                "regimen_id": "REG-SYN-H-0068-3",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.73,
                "rationale": "reduces interaction burden from naproxen"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0069",
        "age": 90,
        "labs": {
            "egfr": 37.3,
            "creatinine": 2.0,
            "potassium": 5.2,
            "inr": 2.1,
            "alt": 164.8,
            "ast": 173.2
        },
        "diagnoses": [
            "type_2_diabetes",
            "depression",
            "nonalcoholic_steatohepatitis",
            "anemia",
            "gout"
        ],
        "medications": [
            "amiodarone",
            "azithromycin",
            "citalopram",
            "diclofenac",
            "digoxin",
            "furosemide",
            "losartan",
            "metoprolol",
            "omeprazole",
            "trimethoprim_sulfamethoxazole",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0069-1",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0069-2",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-H-0069-3",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0069-4",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-H-0069-5",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0069-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0069-1",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.73,
                "rationale": "reduces interaction burden from diclofenac"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0070",
        "age": 94,
        "labs": {
            "egfr": 39.8,
            "creatinine": 2.3,
            "potassium": 5.4,
            "inr": 2.9,
            "alt": 122.8,
            "ast": 103.7
        },
        "diagnoses": [
            "chronic_pain",
            "chronic_liver_disease",
            "anxiety"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "azithromycin",
            "ciprofloxacin",
            "clarithromycin",
            "ferrous_sulfate",
            "isosorbide_mononitrate",
            "levothyroxine",
            "linezolid",
            "metoprolol",
            "sertraline"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0070-1",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-H-0070-2",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0070-3",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-H-0070-4",
                "drug_a": "amlodipine",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive hypotension in frail adults"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0070-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0070-1",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.89,
                "rationale": "reduces interaction burden from clarithromycin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0071",
        "age": 92,
        "labs": {
            "egfr": 43.3,
            "creatinine": 1.8,
            "potassium": 5.3,
            "inr": 2.3,
            "alt": 180.9,
            "ast": 153.4
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "peripheral_artery_disease",
            "type_2_diabetes"
        ],
        "medications": [
            "apixaban",
            "aspirin",
            "dabigatran",
            "diclofenac",
            "ketoconazole",
            "levothyroxine",
            "naproxen",
            "omeprazole",
            "paroxetine",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0071-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0071-2",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0071-3",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-H-0071-4",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0071-1",
            "REG-SYN-H-0071-2",
            "REG-SYN-H-0071-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0071-1",
                "replace_drug": "aspirin",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.7,
                "rationale": "reduces interaction burden from aspirin"
            },
            {
                "regimen_id": "REG-SYN-H-0071-2",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.58,
                "rationale": "reduces interaction burden from naproxen"
            },
            {
                "regimen_id": "REG-SYN-H-0071-3",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.78,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0072",
        "age": 86,
        "labs": {
            "egfr": 31.9,
            "creatinine": 2.7,
            "potassium": 5.5,
            "inr": 2.2
        },
        "diagnoses": [
            "depression",
            "atrial_fibrillation",
            "chronic_liver_disease"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "atorvastatin",
            "cetirizine",
            "clarithromycin",
            "diltiazem",
            "fluconazole",
            "losartan",
            "sildenafil",
            "spironolactone",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0072-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0072-2",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "CYP3A4 inhibition raises statin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0072-3",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            },
            {
                "interaction_id": "INT-SYN-H-0072-4",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0072-5",
                "drug_a": "cetirizine",
                "drug_b": "amlodipine",
                "severity": "minor",
                "evidence": "possible additive sedation in elderly"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0072-1",
            "REG-SYN-H-0072-4"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0072-1",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.68,
                "rationale": "reduces interaction burden from clarithromycin"
            },
            {
                "regimen_id": "REG-SYN-H-0072-2",
                "replace_drug": "atorvastatin",
                "with_drug": "rosuvastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.33,
                "rationale": "modest risk reduction by replacing atorvastatin"
            },
            {
                "regimen_id": "REG-SYN-H-0072-3",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.48,
                "rationale": "modest risk reduction by replacing spironolactone"
            },
            {
                "regimen_id": "REG-SYN-H-0072-4",
                "replace_drug": "fluconazole",
                "with_drug": "micafungin",
                "target_condition": "infection",
                "expected_risk_delta": 0.62,
                "rationale": "reduces interaction burden from fluconazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0073",
        "age": 95,
        "labs": {
            "egfr": 38.6,
            "creatinine": 1.8,
            "potassium": 5.4,
            "inr": 2.1,
            "alt": 146.8,
            "ast": 171.9
        },
        "diagnoses": [
            "coronary_artery_disease",
            "atrial_fibrillation",
            "heart_failure",
            "hypothyroidism"
        ],
        "medications": [
            "amlodipine",
            "cetirizine",
            "citalopram",
            "dabigatran",
            "diltiazem",
            "ferrous_sulfate",
            "levothyroxine",
            "metoprolol",
            "nitroglycerin",
            "paroxetine",
            "sildenafil",
            "simvastatin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0073-1",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-H-0073-2",
                "drug_a": "cetirizine",
                "drug_b": "amlodipine",
                "severity": "minor",
                "evidence": "possible additive sedation in elderly"
            },
            {
                "interaction_id": "INT-SYN-H-0073-3",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-H-0073-4",
                "drug_a": "metoprolol",
                "drug_b": "paroxetine",
                "severity": "moderate",
                "evidence": "CYP2D6 inhibition raises metoprolol exposure"
            }
        ],
        "required_regimens": [],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0073-1",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.27,
                "rationale": "modest risk reduction by replacing simvastatin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0074",
        "age": 93,
        "labs": {
            "egfr": 30.3,
            "creatinine": 2.8,
            "potassium": 5.4,
            "inr": 2.9
        },
        "diagnoses": [
            "anemia",
            "osteoarthritis",
            "chronic_liver_disease"
        ],
        "medications": [
            "apixaban",
            "azithromycin",
            "citalopram",
            "clarithromycin",
            "fluconazole",
            "lisinopril",
            "naproxen",
            "nitroglycerin",
            "sildenafil",
            "spironolactone",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0074-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0074-2",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            },
            {
                "interaction_id": "INT-SYN-H-0074-3",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-H-0074-4",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0074-5",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0074-1",
            "REG-SYN-H-0074-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0074-1",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.72,
                "rationale": "reduces interaction burden from clarithromycin"
            },
            {
                "regimen_id": "REG-SYN-H-0074-2",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.29,
                "rationale": "modest risk reduction by replacing spironolactone"
            },
            {
                "regimen_id": "REG-SYN-H-0074-3",
                "replace_drug": "fluconazole",
                "with_drug": "micafungin",
                "target_condition": "infection",
                "expected_risk_delta": 0.61,
                "rationale": "reduces interaction burden from fluconazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0075",
        "age": 92,
        "labs": {
            "egfr": 25.9,
            "creatinine": 2.3,
            "potassium": 5.0,
            "inr": 2.9,
            "alt": 115.4,
            "ast": 108.8
        },
        "diagnoses": [
            "dyslipidemia",
            "osteoarthritis",
            "anemia",
            "chronic_pain",
            "anxiety"
        ],
        "medications": [
            "apixaban",
            "aspirin",
            "clarithromycin",
            "diclofenac",
            "ferrous_sulfate",
            "ibuprofen",
            "isosorbide_mononitrate",
            "levothyroxine",
            "metoprolol",
            "naproxen",
            "sildenafil",
            "spironolactone",
            "valsartan",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0075-1",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-H-0075-2",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0075-3",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-H-0075-4",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            },
            {
                "interaction_id": "INT-SYN-H-0075-5",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0075-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0075-1",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.64,
                "rationale": "reduces interaction burden from clarithromycin"
            },
            {
                "regimen_id": "REG-SYN-H-0075-2",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.35,
                "rationale": "modest risk reduction by replacing spironolactone"
            },
            {
                "regimen_id": "REG-SYN-H-0075-3",
                "replace_drug": "metoprolol",
                "with_drug": "bisoprolol",
                "target_condition": "rate_control",
                "expected_risk_delta": 0.26,
                "rationale": "modest risk reduction by replacing metoprolol"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0076",
        "age": 92,
        "labs": {
            "egfr": 28.3,
            "creatinine": 2.1,
            "potassium": 5.1,
            "inr": 2.9,
            "alt": 129.1,
            "ast": 115.5
        },
        "diagnoses": [
            "anxiety",
            "hypertension",
            "heart_failure",
            "gout"
        ],
        "medications": [
            "clopidogrel",
            "furosemide",
            "levothyroxine",
            "losartan",
            "metformin",
            "omeprazole",
            "sertraline",
            "spironolactone",
            "valsartan",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0076-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-H-0076-2",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            },
            {
                "interaction_id": "INT-SYN-H-0076-3",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            },
            {
                "interaction_id": "INT-SYN-H-0076-4",
                "drug_a": "metformin",
                "drug_b": "furosemide",
                "severity": "moderate",
                "evidence": "reduced renal clearance can increase lactic acidosis risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0076-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0076-1",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.61,
                "rationale": "reduces interaction burden from omeprazole"
            },
            {
                "regimen_id": "REG-SYN-H-0076-2",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.48,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0077",
        "age": 95,
        "labs": {
            "egfr": 42.9,
            "creatinine": 2.5,
            "potassium": 5.6,
            "inr": 2.0
        },
        "diagnoses": [
            "anxiety",
            "dyslipidemia",
            "heart_failure",
            "anemia"
        ],
        "medications": [
            "apixaban",
            "azithromycin",
            "ibuprofen",
            "linezolid",
            "lisinopril",
            "metronidazole",
            "naproxen",
            "prednisone",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0077-1",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0077-2",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            },
            {
                "interaction_id": "INT-SYN-H-0077-3",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0077-4",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0077-1",
            "REG-SYN-H-0077-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0077-1",
                "replace_drug": "ibuprofen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.61,
                "rationale": "reduces interaction burden from ibuprofen"
            },
            {
                "regimen_id": "REG-SYN-H-0077-2",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.39,
                "rationale": "modest risk reduction by replacing spironolactone"
            },
            {
                "regimen_id": "REG-SYN-H-0077-3",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.73,
                "rationale": "reduces interaction burden from naproxen"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0078",
        "age": 93,
        "labs": {
            "egfr": 26.7,
            "creatinine": 2.4,
            "potassium": 5.0,
            "inr": 2.3,
            "alt": 118.1,
            "ast": 107.5
        },
        "diagnoses": [
            "anxiety",
            "osteoarthritis",
            "type_2_diabetes",
            "atrial_fibrillation",
            "chronic_liver_disease"
        ],
        "medications": [
            "apixaban",
            "aspirin",
            "ciprofloxacin",
            "clarithromycin",
            "linezolid",
            "losartan",
            "sertraline",
            "ticagrelor",
            "trimethoprim_sulfamethoxazole",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0078-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0078-2",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            },
            {
                "interaction_id": "INT-SYN-H-0078-3",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-H-0078-4",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0078-1",
            "REG-SYN-H-0078-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0078-1",
                "replace_drug": "aspirin",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.67,
                "rationale": "reduces interaction burden from aspirin"
            },
            {
                "regimen_id": "REG-SYN-H-0078-2",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.55,
                "rationale": "reduces interaction burden from clarithromycin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0079",
        "age": 89,
        "labs": {
            "egfr": 27.6,
            "creatinine": 2.3,
            "potassium": 4.9,
            "inr": 2.2,
            "alt": 110.3,
            "ast": 111.9
        },
        "diagnoses": [
            "type_2_diabetes",
            "hypertension",
            "anemia"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "aspirin",
            "calcium_carbonate",
            "cetirizine",
            "diclofenac",
            "levothyroxine",
            "metoprolol",
            "sertraline",
            "spironolactone",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0079-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0079-2",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-H-0079-3",
                "drug_a": "aspirin",
                "drug_b": "sertraline",
                "severity": "minor",
                "evidence": "increased bleeding tendency, amplified in frailty"
            },
            {
                "interaction_id": "INT-SYN-H-0079-4",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            },
            {
                "interaction_id": "INT-SYN-H-0079-5",
                "drug_a": "cetirizine",
                "drug_b": "amlodipine",
                "severity": "minor",
                "evidence": "possible additive sedation in elderly"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0079-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0079-1",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.56,
                "rationale": "reduces interaction burden from diclofenac"
            },
            {
                "regimen_id": "REG-SYN-H-0079-2",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.39,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0080",
        "age": 87,
        "labs": {
            "egfr": 32.2,
            "creatinine": 1.9,
            "potassium": 5.3,
            "inr": 2.1,
            "alt": 157.1,
            "ast": 135.2
        },
        "diagnoses": [
            "hypertension",
            "osteoarthritis",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "amiodarone",
            "azithromycin",
            "clopidogrel",
            "diclofenac",
            "ferrous_sulfate",
            "linezolid",
            "losartan",
            "omeprazole",
            "prednisone",
            "sertraline",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0080-1",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-H-0080-2",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0080-3",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-H-0080-4",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0080-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0080-1",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.61,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0081",
        "age": 87,
        "labs": {
            "egfr": 30.4,
            "creatinine": 2.0,
            "potassium": 5.5,
            "inr": 2.0,
            "alt": 121.3,
            "ast": 108.0
        },
        "diagnoses": [
            "anemia",
            "hypertension",
            "peripheral_artery_disease"
        ],
        "medications": [
            "amiodarone",
            "azithromycin",
            "ciprofloxacin",
            "citalopram",
            "ibuprofen",
            "lisinopril",
            "metoprolol",
            "naproxen",
            "paroxetine",
            "spironolactone",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0081-1",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0081-2",
                "drug_a": "metoprolol",
                "drug_b": "paroxetine",
                "severity": "moderate",
                "evidence": "CYP2D6 inhibition raises metoprolol exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0081-3",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            },
            {
                "interaction_id": "INT-SYN-H-0081-4",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            },
            {
                "interaction_id": "INT-SYN-H-0081-5",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0081-2",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.41,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0082",
        "age": 88,
        "labs": {
            "egfr": 42.7,
            "creatinine": 2.7,
            "potassium": 5.2,
            "inr": 2.1,
            "alt": 124.5,
            "ast": 118.1
        },
        "diagnoses": [
            "heart_failure",
            "anxiety",
            "peripheral_artery_disease",
            "chronic_liver_disease"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "aspirin",
            "cetirizine",
            "diclofenac",
            "diltiazem",
            "ibuprofen",
            "isosorbide_mononitrate",
            "lisinopril",
            "rivaroxaban",
            "sildenafil",
            "simvastatin",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0082-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0082-2",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-H-0082-3",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0082-4",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-H-0082-5",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0082-1",
            "REG-SYN-H-0082-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0082-1",
                "replace_drug": "aspirin",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.78,
                "rationale": "reduces interaction burden from aspirin"
            },
            {
                "regimen_id": "REG-SYN-H-0082-2",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.46,
                "rationale": "modest risk reduction by replacing simvastatin"
            },
            {
                "regimen_id": "REG-SYN-H-0082-3",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.62,
                "rationale": "reduces interaction burden from diclofenac"
            },
            {
                "regimen_id": "REG-SYN-H-0082-4",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.41,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0083",
        "age": 94,
        "labs": {
            "egfr": 30.4,
            "creatinine": 2.5,
            "potassium": 4.8,
            "inr": 2.8,
            "alt": 121.3,
            "ast": 120.6
        },
        "diagnoses": [
            "hypothyroidism",
            "hypertension",
            "peripheral_artery_disease",
            "type_2_diabetes",
            "osteoarthritis"
        ],
        "medications": [
            "amiodarone",
            "amlodipine",
            "calcium_carbonate",
            "ciprofloxacin",
            "diclofenac",
            "digoxin",
            "furosemide",
            "levothyroxine",
            "nitroglycerin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0083-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0083-2",
                "drug_a": "amlodipine",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive hypotension in frail adults"
            },
            {
                "interaction_id": "INT-SYN-H-0083-3",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-H-0083-4",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0083-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0083-1",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.6,
                "rationale": "reduces interaction burden from diclofenac"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0084",
        "age": 95,
        "labs": {
            "egfr": 26.5,
            "creatinine": 2.1,
            "potassium": 5.1,
            "inr": 2.1,
            "alt": 128.0,
            "ast": 100.8
        },
        "diagnoses": [
            "hypothyroidism",
            "chronic_liver_disease",
            "chronic_kidney_disease",
            "type_2_diabetes",
            "anemia"
        ],
        "medications": [
            "apixaban",
            "aspirin",
            "clopidogrel",
            "isosorbide_mononitrate",
            "metformin",
            "metronidazole",
            "naproxen",
            "omeprazole",
            "sertraline",
            "spironolactone",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0084-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0084-2",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            },
            {
                "interaction_id": "INT-SYN-H-0084-3",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0084-4",
                "drug_a": "aspirin",
                "drug_b": "sertraline",
                "severity": "minor",
                "evidence": "increased bleeding tendency, amplified in frailty"
            },
            {
                "interaction_id": "INT-SYN-H-0084-5",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0084-1",
            "REG-SYN-H-0084-3",
            "REG-SYN-H-0084-4"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0084-1",
                "replace_drug": "metronidazole",
                "with_drug": "doxycycline",
                "target_condition": "infection",
                "expected_risk_delta": 0.7,
                "rationale": "reduces interaction burden from metronidazole"
            },
            {
                "regimen_id": "REG-SYN-H-0084-2",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.46,
                "rationale": "modest risk reduction by replacing spironolactone"
            },
            {
                "regimen_id": "REG-SYN-H-0084-3",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.73,
                "rationale": "reduces interaction burden from naproxen"
            },
            {
                "regimen_id": "REG-SYN-H-0084-4",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.73,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0085",
        "age": 87,
        "labs": {
            "egfr": 32.1,
            "creatinine": 2.4,
            "potassium": 5.0,
            "inr": 2.9,
            "alt": 164.2,
            "ast": 159.7
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "anemia",
            "depression",
            "dyslipidemia",
            "coronary_artery_disease"
        ],
        "medications": [
            "aspirin",
            "atorvastatin",
            "azithromycin",
            "citalopram",
            "diclofenac",
            "digoxin",
            "furosemide",
            "metronidazole",
            "naproxen",
            "rivaroxaban",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0085-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0085-2",
                "drug_a": "digoxin",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "P-gp inhibition can raise digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0085-3",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-H-0085-4",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0085-1",
            "REG-SYN-H-0085-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0085-1",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.63,
                "rationale": "reduces interaction burden from diclofenac"
            },
            {
                "regimen_id": "REG-SYN-H-0085-2",
                "replace_drug": "digoxin",
                "with_drug": "bisoprolol",
                "target_condition": "rate_control",
                "expected_risk_delta": 0.48,
                "rationale": "modest risk reduction by replacing digoxin"
            },
            {
                "regimen_id": "REG-SYN-H-0085-3",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.6,
                "rationale": "reduces interaction burden from naproxen"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0086",
        "age": 93,
        "labs": {
            "egfr": 30.9,
            "creatinine": 2.2,
            "potassium": 5.1,
            "inr": 2.8
        },
        "diagnoses": [
            "osteoarthritis",
            "atrial_fibrillation",
            "chronic_liver_disease",
            "chronic_kidney_disease",
            "depression"
        ],
        "medications": [
            "amiodarone",
            "aspirin",
            "cetirizine",
            "clopidogrel",
            "dabigatran",
            "diclofenac",
            "digoxin",
            "diltiazem",
            "ketoconazole",
            "levothyroxine",
            "simvastatin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0086-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0086-2",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-H-0086-3",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0086-4",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0086-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0086-1",
                "replace_drug": "aspirin",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.58,
                "rationale": "reduces interaction burden from aspirin"
            },
            {
                "regimen_id": "REG-SYN-H-0086-2",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.47,
                "rationale": "modest risk reduction by replacing simvastatin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0087",
        "age": 95,
        "labs": {
            "egfr": 39.1,
            "creatinine": 2.6,
            "potassium": 5.6,
            "inr": 3.1,
            "alt": 152.1,
            "ast": 165.5
        },
        "diagnoses": [
            "chronic_liver_disease",
            "hypothyroidism",
            "anemia",
            "dyslipidemia",
            "atrial_fibrillation"
        ],
        "medications": [
            "amiodarone",
            "amlodipine",
            "apixaban",
            "aspirin",
            "diclofenac",
            "digoxin",
            "fluconazole",
            "ibuprofen",
            "naproxen",
            "simvastatin",
            "spironolactone",
            "valsartan",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0087-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0087-2",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0087-3",
                "drug_a": "digoxin",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "P-gp inhibition can raise digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0087-4",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-H-0087-5",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0087-1",
            "REG-SYN-H-0087-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0087-1",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.71,
                "rationale": "reduces interaction burden from diclofenac"
            },
            {
                "regimen_id": "REG-SYN-H-0087-2",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.72,
                "rationale": "reduces interaction burden from naproxen"
            },
            {
                "regimen_id": "REG-SYN-H-0087-3",
                "replace_drug": "digoxin",
                "with_drug": "bisoprolol",
                "target_condition": "rate_control",
                "expected_risk_delta": 0.31,
                "rationale": "modest risk reduction by replacing digoxin"
            },
            {
                "regimen_id": "REG-SYN-H-0087-4",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.27,
                "rationale": "modest risk reduction by replacing simvastatin"
            },
            {
                "regimen_id": "REG-SYN-H-0087-5",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.35,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0088",
        "age": 94,
        "labs": {
            "egfr": 41.2,
            "creatinine": 2.6,
            "potassium": 5.0,
            "inr": 2.3,
            "alt": 162.1,
            "ast": 147.3
        },
        "diagnoses": [
            "hypertension",
            "hypothyroidism",
            "heart_failure",
            "coronary_artery_disease"
        ],
        "medications": [
            "amiodarone",
            "atorvastatin",
            "clopidogrel",
            "digoxin",
            "furosemide",
            "isosorbide_mononitrate",
            "ketoconazole",
            "metformin",
            "metoprolol",
            "omeprazole",
            "paroxetine",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0088-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-H-0088-2",
                "drug_a": "digoxin",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "P-gp inhibition can raise digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0088-3",
                "drug_a": "metformin",
                "drug_b": "furosemide",
                "severity": "moderate",
                "evidence": "reduced renal clearance can increase lactic acidosis risk"
            },
            {
                "interaction_id": "INT-SYN-H-0088-4",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0088-5",
                "drug_a": "metoprolol",
                "drug_b": "paroxetine",
                "severity": "moderate",
                "evidence": "CYP2D6 inhibition raises metoprolol exposure"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0088-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0088-1",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.88,
                "rationale": "reduces interaction burden from omeprazole"
            },
            {
                "regimen_id": "REG-SYN-H-0088-2",
                "replace_drug": "digoxin",
                "with_drug": "bisoprolol",
                "target_condition": "rate_control",
                "expected_risk_delta": 0.27,
                "rationale": "modest risk reduction by replacing digoxin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0089",
        "age": 91,
        "labs": {
            "egfr": 29.8,
            "creatinine": 1.9,
            "potassium": 5.6,
            "inr": 2.4,
            "alt": 140.3,
            "ast": 177.3
        },
        "diagnoses": [
            "gout",
            "depression",
            "type_2_diabetes"
        ],
        "medications": [
            "allopurinol",
            "atorvastatin",
            "calcium_carbonate",
            "cetirizine",
            "ciprofloxacin",
            "dabigatran",
            "diltiazem",
            "glipizide",
            "ketoconazole",
            "losartan",
            "spironolactone",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0089-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0089-2",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            },
            {
                "interaction_id": "INT-SYN-H-0089-3",
                "drug_a": "allopurinol",
                "drug_b": "warfarin",
                "severity": "moderate",
                "evidence": "allopurinol may enhance warfarin anticoagulation"
            },
            {
                "interaction_id": "INT-SYN-H-0089-4",
                "drug_a": "glipizide",
                "drug_b": "ciprofloxacin",
                "severity": "moderate",
                "evidence": "dysglycemia risk from fluoroquinolone-sulfonylurea combination"
            },
            {
                "interaction_id": "INT-SYN-H-0089-5",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "CYP3A4 inhibition raises statin concentration"
            }
        ],
        "required_regimens": [],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0089-1",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.4,
                "rationale": "modest risk reduction by replacing spironolactone"
            },
            {
                "regimen_id": "REG-SYN-H-0089-4",
                "replace_drug": "atorvastatin",
                "with_drug": "rosuvastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.26,
                "rationale": "modest risk reduction by replacing atorvastatin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0090",
        "age": 87,
        "labs": {
            "egfr": 42.7,
            "creatinine": 2.7,
            "potassium": 4.9,
            "inr": 2.6,
            "alt": 178.2,
            "ast": 162.7
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "depression",
            "gout",
            "chronic_liver_disease"
        ],
        "medications": [
            "apixaban",
            "atorvastatin",
            "clopidogrel",
            "diltiazem",
            "ibuprofen",
            "linezolid",
            "metoprolol",
            "naproxen",
            "sertraline",
            "simvastatin",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0090-1",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0090-2",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            },
            {
                "interaction_id": "INT-SYN-H-0090-3",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-H-0090-4",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0090-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0090-1",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.86,
                "rationale": "reduces interaction burden from naproxen"
            },
            {
                "regimen_id": "REG-SYN-H-0090-2",
                "replace_drug": "metoprolol",
                "with_drug": "bisoprolol",
                "target_condition": "rate_control",
                "expected_risk_delta": 0.44,
                "rationale": "modest risk reduction by replacing metoprolol"
            },
            {
                "regimen_id": "REG-SYN-H-0090-3",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.45,
                "rationale": "modest risk reduction by replacing simvastatin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0091",
        "age": 91,
        "labs": {
            "egfr": 26.1,
            "creatinine": 2.6,
            "potassium": 4.9,
            "inr": 2.1,
            "alt": 126.6,
            "ast": 110.1
        },
        "diagnoses": [
            "gout",
            "peripheral_artery_disease",
            "hypertension"
        ],
        "medications": [
            "allopurinol",
            "amiodarone",
            "apixaban",
            "ciprofloxacin",
            "clopidogrel",
            "digoxin",
            "furosemide",
            "isosorbide_mononitrate",
            "metoprolol",
            "metronidazole",
            "naproxen",
            "omeprazole",
            "sertraline",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0091-1",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0091-2",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0091-3",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-H-0091-4",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            },
            {
                "interaction_id": "INT-SYN-H-0091-5",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0091-1",
            "REG-SYN-H-0091-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0091-1",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.68,
                "rationale": "reduces interaction burden from naproxen"
            },
            {
                "regimen_id": "REG-SYN-H-0091-2",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.67,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0092",
        "age": 91,
        "labs": {
            "egfr": 34.1,
            "creatinine": 2.6,
            "potassium": 5.6,
            "inr": 3.2
        },
        "diagnoses": [
            "osteoarthritis",
            "anemia",
            "coronary_artery_disease",
            "peripheral_artery_disease"
        ],
        "medications": [
            "amiodarone",
            "aspirin",
            "atorvastatin",
            "dabigatran",
            "digoxin",
            "furosemide",
            "losartan",
            "metoprolol",
            "omeprazole",
            "sertraline",
            "ticagrelor",
            "valsartan",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0092-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0092-2",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            },
            {
                "interaction_id": "INT-SYN-H-0092-3",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-H-0092-4",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-H-0092-5",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0092-1",
            "REG-SYN-H-0092-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0092-1",
                "replace_drug": "aspirin",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.85,
                "rationale": "reduces interaction burden from aspirin"
            },
            {
                "regimen_id": "REG-SYN-H-0092-2",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.82,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0093",
        "age": 95,
        "labs": {
            "egfr": 33.9,
            "creatinine": 2.3,
            "potassium": 4.9,
            "inr": 2.6
        },
        "diagnoses": [
            "heart_failure",
            "peripheral_artery_disease",
            "atrial_fibrillation"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "atorvastatin",
            "azithromycin",
            "cetirizine",
            "citalopram",
            "diltiazem",
            "fluconazole",
            "losartan",
            "naproxen",
            "simvastatin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0093-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0093-2",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0093-3",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "CYP3A4 inhibition raises statin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0093-4",
                "drug_a": "cetirizine",
                "drug_b": "amlodipine",
                "severity": "minor",
                "evidence": "possible additive sedation in elderly"
            },
            {
                "interaction_id": "INT-SYN-H-0093-5",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0093-1",
            "REG-SYN-H-0093-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0093-1",
                "replace_drug": "fluconazole",
                "with_drug": "micafungin",
                "target_condition": "infection",
                "expected_risk_delta": 0.74,
                "rationale": "reduces interaction burden from fluconazole"
            },
            {
                "regimen_id": "REG-SYN-H-0093-2",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.74,
                "rationale": "reduces interaction burden from naproxen"
            },
            {
                "regimen_id": "REG-SYN-H-0093-3",
                "replace_drug": "atorvastatin",
                "with_drug": "rosuvastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.47,
                "rationale": "modest risk reduction by replacing atorvastatin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0094",
        "age": 93,
        "labs": {
            "egfr": 31.0,
            "creatinine": 2.4,
            "potassium": 5.2,
            "inr": 3.1,
            "alt": 129.2,
            "ast": 105.3
        },
        "diagnoses": [
            "chronic_pain",
            "atrial_fibrillation",
            "osteoarthritis"
        ],
        "medications": [
            "amlodipine",
            "atorvastatin",
            "azithromycin",
            "calcium_carbonate",
            "cetirizine",
            "citalopram",
            "fluconazole",
            "furosemide",
            "ibuprofen",
            "ketoconazole",
            "levothyroxine",
            "metoprolol",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0094-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0094-2",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-H-0094-3",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-H-0094-4",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-H-0094-5",
                "drug_a": "cetirizine",
                "drug_b": "amlodipine",
                "severity": "minor",
                "evidence": "possible additive sedation in elderly"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0094-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0094-1",
                "replace_drug": "fluconazole",
                "with_drug": "micafungin",
                "target_condition": "infection",
                "expected_risk_delta": 0.88,
                "rationale": "reduces interaction burden from fluconazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0095",
        "age": 91,
        "labs": {
            "egfr": 27.9,
            "creatinine": 2.1,
            "potassium": 5.5,
            "inr": 2.8,
            "alt": 161.1,
            "ast": 168.2
        },
        "diagnoses": [
            "anxiety",
            "chronic_kidney_disease",
            "heart_failure",
            "osteoarthritis"
        ],
        "medications": [
            "apixaban",
            "aspirin",
            "ciprofloxacin",
            "clarithromycin",
            "clopidogrel",
            "ferrous_sulfate",
            "glipizide",
            "levothyroxine",
            "nitroglycerin",
            "omeprazole",
            "simvastatin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0095-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-H-0095-2",
                "drug_a": "glipizide",
                "drug_b": "ciprofloxacin",
                "severity": "moderate",
                "evidence": "dysglycemia risk from fluoroquinolone-sulfonylurea combination"
            },
            {
                "interaction_id": "INT-SYN-H-0095-3",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0095-4",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0095-1",
            "REG-SYN-H-0095-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0095-1",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.69,
                "rationale": "reduces interaction burden from omeprazole"
            },
            {
                "regimen_id": "REG-SYN-H-0095-3",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.74,
                "rationale": "reduces interaction burden from clarithromycin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0096",
        "age": 86,
        "labs": {
            "egfr": 34.5,
            "creatinine": 2.2,
            "potassium": 5.0,
            "inr": 2.1
        },
        "diagnoses": [
            "atrial_fibrillation",
            "coronary_artery_disease",
            "chronic_kidney_disease",
            "gout",
            "osteoarthritis"
        ],
        "medications": [
            "ciprofloxacin",
            "citalopram",
            "clopidogrel",
            "furosemide",
            "glipizide",
            "metoprolol",
            "naproxen",
            "omeprazole",
            "paroxetine",
            "rivaroxaban",
            "spironolactone",
            "ticagrelor",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0096-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-H-0096-2",
                "drug_a": "glipizide",
                "drug_b": "ciprofloxacin",
                "severity": "moderate",
                "evidence": "dysglycemia risk from fluoroquinolone-sulfonylurea combination"
            },
            {
                "interaction_id": "INT-SYN-H-0096-3",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0096-4",
                "drug_a": "furosemide",
                "drug_b": "warfarin",
                "severity": "minor",
                "evidence": "volume changes may alter INR stability"
            },
            {
                "interaction_id": "INT-SYN-H-0096-5",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0096-1",
            "REG-SYN-H-0096-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0096-1",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.72,
                "rationale": "reduces interaction burden from omeprazole"
            },
            {
                "regimen_id": "REG-SYN-H-0096-3",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.8,
                "rationale": "reduces interaction burden from naproxen"
            },
            {
                "regimen_id": "REG-SYN-H-0096-4",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.32,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0097",
        "age": 93,
        "labs": {
            "egfr": 32.8,
            "creatinine": 2.6,
            "potassium": 5.3,
            "inr": 2.7
        },
        "diagnoses": [
            "heart_failure",
            "peripheral_artery_disease",
            "chronic_liver_disease",
            "anxiety",
            "type_2_diabetes"
        ],
        "medications": [
            "apixaban",
            "aspirin",
            "azithromycin",
            "calcium_carbonate",
            "cetirizine",
            "diclofenac",
            "fluconazole",
            "losartan",
            "prednisone",
            "rivaroxaban",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0097-1",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0097-2",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            },
            {
                "interaction_id": "INT-SYN-H-0097-3",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0097-4",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0097-1",
            "REG-SYN-H-0097-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0097-1",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.62,
                "rationale": "reduces interaction burden from diclofenac"
            },
            {
                "regimen_id": "REG-SYN-H-0097-2",
                "replace_drug": "fluconazole",
                "with_drug": "micafungin",
                "target_condition": "infection",
                "expected_risk_delta": 0.64,
                "rationale": "reduces interaction burden from fluconazole"
            },
            {
                "regimen_id": "REG-SYN-H-0097-3",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.34,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0098",
        "age": 89,
        "labs": {
            "egfr": 25.1,
            "creatinine": 2.2,
            "potassium": 5.5,
            "inr": 2.7
        },
        "diagnoses": [
            "type_2_diabetes",
            "chronic_pain",
            "dyslipidemia",
            "chronic_liver_disease",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "amiodarone",
            "azithromycin",
            "citalopram",
            "diltiazem",
            "naproxen",
            "rivaroxaban",
            "simvastatin",
            "spironolactone",
            "trimethoprim_sulfamethoxazole",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0098-1",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0098-2",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-H-0098-3",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0098-4",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0098-1",
            "REG-SYN-H-0098-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0098-1",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.55,
                "rationale": "reduces interaction burden from naproxen"
            },
            {
                "regimen_id": "REG-SYN-H-0098-2",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.48,
                "rationale": "modest risk reduction by replacing simvastatin"
            },
            {
                "regimen_id": "REG-SYN-H-0098-3",
                "replace_drug": "trimethoprim_sulfamethoxazole",
                "with_drug": "cephalexin",
                "target_condition": "infection",
                "expected_risk_delta": 0.82,
                "rationale": "reduces interaction burden from trimethoprim_sulfamethoxazole"
            },
            {
                "regimen_id": "REG-SYN-H-0098-4",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.34,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0099",
        "age": 92,
        "labs": {
            "egfr": 29.4,
            "creatinine": 2.1,
            "potassium": 5.6,
            "inr": 2.9,
            "alt": 111.9,
            "ast": 123.2
        },
        "diagnoses": [
            "gout",
            "chronic_pain",
            "hypertension",
            "peripheral_artery_disease",
            "chronic_liver_disease"
        ],
        "medications": [
            "apixaban",
            "azithromycin",
            "cetirizine",
            "citalopram",
            "fluconazole",
            "isosorbide_mononitrate",
            "naproxen",
            "sertraline",
            "sildenafil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0099-1",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0099-2",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-H-0099-3",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0099-4",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0099-1",
            "REG-SYN-H-0099-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0099-1",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.71,
                "rationale": "reduces interaction burden from naproxen"
            },
            {
                "regimen_id": "REG-SYN-H-0099-2",
                "replace_drug": "fluconazole",
                "with_drug": "micafungin",
                "target_condition": "infection",
                "expected_risk_delta": 0.63,
                "rationale": "reduces interaction burden from fluconazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0100",
        "age": 90,
        "labs": {
            "egfr": 28.7,
            "creatinine": 2.7,
            "potassium": 5.5,
            "inr": 2.4,
            "alt": 153.6,
            "ast": 165.3
        },
        "diagnoses": [
            "depression",
            "anemia",
            "anxiety",
            "hypertension"
        ],
        "medications": [
            "allopurinol",
            "apixaban",
            "clarithromycin",
            "dabigatran",
            "fluconazole",
            "ketoconazole",
            "losartan",
            "metformin",
            "omeprazole",
            "prednisone",
            "rivaroxaban",
            "ticagrelor",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0100-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0100-2",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            },
            {
                "interaction_id": "INT-SYN-H-0100-3",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0100-4",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0100-5",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0100-1",
            "REG-SYN-H-0100-2",
            "REG-SYN-H-0100-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0100-1",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.89,
                "rationale": "reduces interaction burden from clarithromycin"
            },
            {
                "regimen_id": "REG-SYN-H-0100-2",
                "replace_drug": "fluconazole",
                "with_drug": "micafungin",
                "target_condition": "infection",
                "expected_risk_delta": 0.56,
                "rationale": "reduces interaction burden from fluconazole"
            },
            {
                "regimen_id": "REG-SYN-H-0100-3",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.82,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0101",
        "age": 94,
        "labs": {
            "egfr": 39.2,
            "creatinine": 2.8,
            "potassium": 5.0,
            "inr": 2.6
        },
        "diagnoses": [
            "depression",
            "type_2_diabetes",
            "dyslipidemia",
            "osteoarthritis",
            "heart_failure"
        ],
        "medications": [
            "amlodipine",
            "ciprofloxacin",
            "clopidogrel",
            "ferrous_sulfate",
            "ibuprofen",
            "isosorbide_mononitrate",
            "sildenafil",
            "simvastatin",
            "valsartan",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0101-1",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0101-2",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            },
            {
                "interaction_id": "INT-SYN-H-0101-3",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-H-0101-4",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0101-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0101-1",
                "replace_drug": "ibuprofen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.9,
                "rationale": "reduces interaction burden from ibuprofen"
            },
            {
                "regimen_id": "REG-SYN-H-0101-2",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.43,
                "rationale": "modest risk reduction by replacing simvastatin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0102",
        "age": 90,
        "labs": {
            "egfr": 33.0,
            "creatinine": 2.7,
            "potassium": 4.8,
            "inr": 2.5,
            "alt": 117.7,
            "ast": 111.7
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "dyslipidemia",
            "chronic_pain"
        ],
        "medications": [
            "apixaban",
            "ciprofloxacin",
            "diclofenac",
            "ibuprofen",
            "losartan",
            "naproxen",
            "omeprazole",
            "rivaroxaban",
            "spironolactone",
            "ticagrelor",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0102-1",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0102-2",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-H-0102-3",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0102-4",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0102-1",
            "REG-SYN-H-0102-2",
            "REG-SYN-H-0102-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0102-1",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.89,
                "rationale": "reduces interaction burden from diclofenac"
            },
            {
                "regimen_id": "REG-SYN-H-0102-2",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.65,
                "rationale": "reduces interaction burden from omeprazole"
            },
            {
                "regimen_id": "REG-SYN-H-0102-3",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.67,
                "rationale": "reduces interaction burden from naproxen"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0103",
        "age": 92,
        "labs": {
            "egfr": 41.9,
            "creatinine": 1.9,
            "potassium": 5.2,
            "inr": 2.3,
            "alt": 115.8,
            "ast": 103.2
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "dyslipidemia",
            "chronic_pain",
            "peripheral_artery_disease",
            "depression"
        ],
        "medications": [
            "amiodarone",
            "ciprofloxacin",
            "dabigatran",
            "diclofenac",
            "glipizide",
            "ketoconazole",
            "lisinopril",
            "rivaroxaban",
            "spironolactone",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0103-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0103-2",
                "drug_a": "glipizide",
                "drug_b": "ciprofloxacin",
                "severity": "moderate",
                "evidence": "dysglycemia risk from fluoroquinolone-sulfonylurea combination"
            },
            {
                "interaction_id": "INT-SYN-H-0103-3",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0103-4",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            }
        ],
        "required_regimens": [],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0103-2",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.46,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0104",
        "age": 93,
        "labs": {
            "egfr": 36.4,
            "creatinine": 2.5,
            "potassium": 5.3,
            "inr": 3.0,
            "alt": 155.1,
            "ast": 152.4
        },
        "diagnoses": [
            "osteoarthritis",
            "gout",
            "chronic_pain",
            "peripheral_artery_disease"
        ],
        "medications": [
            "apixaban",
            "ciprofloxacin",
            "clopidogrel",
            "diclofenac",
            "furosemide",
            "metoprolol",
            "metronidazole",
            "omeprazole",
            "ticagrelor",
            "valsartan",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0104-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0104-2",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0104-3",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-H-0104-4",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            },
            {
                "interaction_id": "INT-SYN-H-0104-5",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0104-1",
            "REG-SYN-H-0104-2",
            "REG-SYN-H-0104-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0104-1",
                "replace_drug": "metronidazole",
                "with_drug": "doxycycline",
                "target_condition": "infection",
                "expected_risk_delta": 0.89,
                "rationale": "reduces interaction burden from metronidazole"
            },
            {
                "regimen_id": "REG-SYN-H-0104-2",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.73,
                "rationale": "reduces interaction burden from diclofenac"
            },
            {
                "regimen_id": "REG-SYN-H-0104-3",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.84,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0105",
        "age": 91,
        "labs": {
            "egfr": 25.1,
            "creatinine": 1.9,
            "potassium": 4.9,
            "inr": 2.5,
            "alt": 148.9,
            "ast": 142.2
        },
        "diagnoses": [
            "anemia",
            "peripheral_artery_disease",
            "chronic_pain",
            "osteoarthritis",
            "chronic_liver_disease"
        ],
        "medications": [
            "apixaban",
            "aspirin",
            "azithromycin",
            "ciprofloxacin",
            "citalopram",
            "clopidogrel",
            "glipizide",
            "naproxen",
            "sertraline",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0105-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0105-2",
                "drug_a": "glipizide",
                "drug_b": "ciprofloxacin",
                "severity": "moderate",
                "evidence": "dysglycemia risk from fluoroquinolone-sulfonylurea combination"
            },
            {
                "interaction_id": "INT-SYN-H-0105-3",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0105-4",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0105-1",
            "REG-SYN-H-0105-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0105-1",
                "replace_drug": "aspirin",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.85,
                "rationale": "reduces interaction burden from aspirin"
            },
            {
                "regimen_id": "REG-SYN-H-0105-3",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.9,
                "rationale": "reduces interaction burden from naproxen"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0106",
        "age": 91,
        "labs": {
            "egfr": 32.1,
            "creatinine": 2.5,
            "potassium": 4.8,
            "inr": 2.0,
            "alt": 151.8,
            "ast": 148.5
        },
        "diagnoses": [
            "heart_failure",
            "hypertension",
            "peripheral_artery_disease",
            "anemia",
            "chronic_liver_disease"
        ],
        "medications": [
            "amiodarone",
            "aspirin",
            "dabigatran",
            "fluconazole",
            "furosemide",
            "ketoconazole",
            "linezolid",
            "metoprolol",
            "naproxen",
            "sertraline",
            "simvastatin",
            "spironolactone",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0106-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0106-2",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            },
            {
                "interaction_id": "INT-SYN-H-0106-3",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-H-0106-4",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-H-0106-5",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0106-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0106-1",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.43,
                "rationale": "modest risk reduction by replacing spironolactone"
            },
            {
                "regimen_id": "REG-SYN-H-0106-2",
                "replace_drug": "fluconazole",
                "with_drug": "micafungin",
                "target_condition": "infection",
                "expected_risk_delta": 0.78,
                "rationale": "reduces interaction burden from fluconazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0107",
        "age": 88,
        "labs": {
            "egfr": 34.7,
            "creatinine": 2.8,
            "potassium": 5.5,
            "inr": 2.8
        },
        "diagnoses": [
            "hypertension",
            "nonalcoholic_steatohepatitis",
            "chronic_pain",
            "peripheral_artery_disease"
        ],
        "medications": [
            "amlodipine",
            "aspirin",
            "azithromycin",
            "cetirizine",
            "citalopram",
            "fluconazole",
            "linezolid",
            "sertraline",
            "spironolactone",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0107-1",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-H-0107-2",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-H-0107-3",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0107-4",
                "drug_a": "cetirizine",
                "drug_b": "amlodipine",
                "severity": "minor",
                "evidence": "possible additive sedation in elderly"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0107-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0107-1",
                "replace_drug": "trimethoprim_sulfamethoxazole",
                "with_drug": "cephalexin",
                "target_condition": "infection",
                "expected_risk_delta": 0.78,
                "rationale": "reduces interaction burden from trimethoprim_sulfamethoxazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0108",
        "age": 87,
        "labs": {
            "egfr": 35.0,
            "creatinine": 1.9,
            "potassium": 5.2,
            "inr": 2.7
        },
        "diagnoses": [
            "hypertension",
            "nonalcoholic_steatohepatitis",
            "type_2_diabetes",
            "dyslipidemia"
        ],
        "medications": [
            "apixaban",
            "azithromycin",
            "furosemide",
            "ibuprofen",
            "isosorbide_mononitrate",
            "metformin",
            "naproxen",
            "rivaroxaban",
            "sildenafil",
            "ticagrelor",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0108-1",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0108-2",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0108-3",
                "drug_a": "metformin",
                "drug_b": "furosemide",
                "severity": "moderate",
                "evidence": "reduced renal clearance can increase lactic acidosis risk"
            },
            {
                "interaction_id": "INT-SYN-H-0108-4",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0108-1",
            "REG-SYN-H-0108-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0108-1",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.58,
                "rationale": "reduces interaction burden from naproxen"
            },
            {
                "regimen_id": "REG-SYN-H-0108-2",
                "replace_drug": "trimethoprim_sulfamethoxazole",
                "with_drug": "cephalexin",
                "target_condition": "infection",
                "expected_risk_delta": 0.65,
                "rationale": "reduces interaction burden from trimethoprim_sulfamethoxazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0109",
        "age": 86,
        "labs": {
            "egfr": 29.8,
            "creatinine": 2.8,
            "potassium": 5.3,
            "inr": 2.6,
            "alt": 186.0,
            "ast": 168.1
        },
        "diagnoses": [
            "chronic_liver_disease",
            "type_2_diabetes",
            "hypothyroidism"
        ],
        "medications": [
            "atorvastatin",
            "azithromycin",
            "diclofenac",
            "fluconazole",
            "levothyroxine",
            "linezolid",
            "naproxen",
            "nitroglycerin",
            "omeprazole",
            "prednisone",
            "rivaroxaban",
            "sildenafil",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0109-1",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-H-0109-2",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            },
            {
                "interaction_id": "INT-SYN-H-0109-3",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-H-0109-4",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0109-5",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0109-1",
            "REG-SYN-H-0109-2",
            "REG-SYN-H-0109-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0109-1",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.85,
                "rationale": "reduces interaction burden from omeprazole"
            },
            {
                "regimen_id": "REG-SYN-H-0109-2",
                "replace_drug": "fluconazole",
                "with_drug": "micafungin",
                "target_condition": "infection",
                "expected_risk_delta": 0.64,
                "rationale": "reduces interaction burden from fluconazole"
            },
            {
                "regimen_id": "REG-SYN-H-0109-3",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.82,
                "rationale": "reduces interaction burden from naproxen"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0110",
        "age": 89,
        "labs": {
            "egfr": 43.9,
            "creatinine": 2.2,
            "potassium": 5.1,
            "inr": 2.9,
            "alt": 127.7,
            "ast": 124.5
        },
        "diagnoses": [
            "coronary_artery_disease",
            "atrial_fibrillation",
            "anemia",
            "hypothyroidism"
        ],
        "medications": [
            "amiodarone",
            "calcium_carbonate",
            "ciprofloxacin",
            "dabigatran",
            "ferrous_sulfate",
            "glipizide",
            "ibuprofen",
            "levothyroxine",
            "losartan",
            "spironolactone",
            "valsartan",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0110-1",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0110-2",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            },
            {
                "interaction_id": "INT-SYN-H-0110-3",
                "drug_a": "glipizide",
                "drug_b": "ciprofloxacin",
                "severity": "moderate",
                "evidence": "dysglycemia risk from fluoroquinolone-sulfonylurea combination"
            },
            {
                "interaction_id": "INT-SYN-H-0110-4",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            },
            {
                "interaction_id": "INT-SYN-H-0110-5",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0110-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0110-1",
                "replace_drug": "ibuprofen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.61,
                "rationale": "reduces interaction burden from ibuprofen"
            },
            {
                "regimen_id": "REG-SYN-H-0110-2",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.42,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0111",
        "age": 86,
        "labs": {
            "egfr": 40.1,
            "creatinine": 1.9,
            "potassium": 4.9,
            "inr": 2.7
        },
        "diagnoses": [
            "chronic_pain",
            "type_2_diabetes",
            "dyslipidemia",
            "depression",
            "chronic_liver_disease"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "ciprofloxacin",
            "dabigatran",
            "diclofenac",
            "ferrous_sulfate",
            "fluconazole",
            "furosemide",
            "isosorbide_mononitrate",
            "ketoconazole",
            "sertraline",
            "sildenafil",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0111-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0111-2",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-H-0111-3",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0111-4",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0111-5",
                "drug_a": "amlodipine",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive hypotension in frail adults"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0111-1",
            "REG-SYN-H-0111-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0111-1",
                "replace_drug": "fluconazole",
                "with_drug": "micafungin",
                "target_condition": "infection",
                "expected_risk_delta": 0.73,
                "rationale": "reduces interaction burden from fluconazole"
            },
            {
                "regimen_id": "REG-SYN-H-0111-2",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.75,
                "rationale": "reduces interaction burden from diclofenac"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0112",
        "age": 86,
        "labs": {
            "egfr": 35.0,
            "creatinine": 1.8,
            "potassium": 4.8,
            "inr": 3.1
        },
        "diagnoses": [
            "atrial_fibrillation",
            "hypothyroidism",
            "osteoarthritis"
        ],
        "medications": [
            "amlodipine",
            "azithromycin",
            "citalopram",
            "dabigatran",
            "diclofenac",
            "digoxin",
            "ketoconazole",
            "losartan",
            "metoprolol",
            "simvastatin",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0112-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0112-2",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-H-0112-3",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0112-4",
                "drug_a": "digoxin",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "P-gp inhibition can raise digoxin concentration"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0112-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0112-1",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.67,
                "rationale": "reduces interaction burden from diclofenac"
            },
            {
                "regimen_id": "REG-SYN-H-0112-2",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.47,
                "rationale": "modest risk reduction by replacing simvastatin"
            },
            {
                "regimen_id": "REG-SYN-H-0112-3",
                "replace_drug": "digoxin",
                "with_drug": "bisoprolol",
                "target_condition": "rate_control",
                "expected_risk_delta": 0.41,
                "rationale": "modest risk reduction by replacing digoxin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0113",
        "age": 93,
        "labs": {
            "egfr": 41.9,
            "creatinine": 2.4,
            "potassium": 4.9,
            "inr": 2.9,
            "alt": 119.7,
            "ast": 112.3
        },
        "diagnoses": [
            "atrial_fibrillation",
            "hypothyroidism",
            "chronic_pain",
            "hypertension"
        ],
        "medications": [
            "amiodarone",
            "amlodipine",
            "ciprofloxacin",
            "digoxin",
            "ferrous_sulfate",
            "fluconazole",
            "furosemide",
            "isosorbide_mononitrate",
            "levothyroxine",
            "metoprolol",
            "omeprazole",
            "sildenafil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0113-1",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0113-2",
                "drug_a": "amlodipine",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive hypotension in frail adults"
            },
            {
                "interaction_id": "INT-SYN-H-0113-3",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-H-0113-4",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-H-0113-5",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0114",
        "age": 92,
        "labs": {
            "egfr": 43.6,
            "creatinine": 2.0,
            "potassium": 5.1,
            "inr": 3.0
        },
        "diagnoses": [
            "osteoarthritis",
            "chronic_pain",
            "anxiety"
        ],
        "medications": [
            "atorvastatin",
            "azithromycin",
            "citalopram",
            "clarithromycin",
            "clopidogrel",
            "digoxin",
            "diltiazem",
            "glipizide",
            "naproxen",
            "rivaroxaban",
            "spironolactone",
            "trimethoprim_sulfamethoxazole",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0114-1",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-H-0114-2",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "CYP3A4 inhibition raises statin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0114-3",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0114-4",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            },
            {
                "interaction_id": "INT-SYN-H-0114-5",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0114-2",
            "REG-SYN-H-0114-4"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0114-1",
                "replace_drug": "atorvastatin",
                "with_drug": "rosuvastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.32,
                "rationale": "modest risk reduction by replacing atorvastatin"
            },
            {
                "regimen_id": "REG-SYN-H-0114-2",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.71,
                "rationale": "reduces interaction burden from naproxen"
            },
            {
                "regimen_id": "REG-SYN-H-0114-3",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.34,
                "rationale": "modest risk reduction by replacing spironolactone"
            },
            {
                "regimen_id": "REG-SYN-H-0114-4",
                "replace_drug": "trimethoprim_sulfamethoxazole",
                "with_drug": "cephalexin",
                "target_condition": "infection",
                "expected_risk_delta": 0.87,
                "rationale": "reduces interaction burden from trimethoprim_sulfamethoxazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0115",
        "age": 92,
        "labs": {
            "egfr": 27.0,
            "creatinine": 2.2,
            "potassium": 4.8,
            "inr": 2.7
        },
        "diagnoses": [
            "gout",
            "dyslipidemia",
            "anemia",
            "heart_failure"
        ],
        "medications": [
            "aspirin",
            "ciprofloxacin",
            "clopidogrel",
            "digoxin",
            "glipizide",
            "isosorbide_mononitrate",
            "levothyroxine",
            "omeprazole",
            "sildenafil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0115-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0115-2",
                "drug_a": "glipizide",
                "drug_b": "ciprofloxacin",
                "severity": "moderate",
                "evidence": "dysglycemia risk from fluoroquinolone-sulfonylurea combination"
            },
            {
                "interaction_id": "INT-SYN-H-0115-3",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-H-0115-4",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0115-1",
            "REG-SYN-H-0115-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0115-1",
                "replace_drug": "aspirin",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.63,
                "rationale": "reduces interaction burden from aspirin"
            },
            {
                "regimen_id": "REG-SYN-H-0115-3",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.73,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0116",
        "age": 95,
        "labs": {
            "egfr": 26.5,
            "creatinine": 2.7,
            "potassium": 5.1,
            "inr": 2.2,
            "alt": 118.5,
            "ast": 103.0
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "anemia",
            "gout",
            "atrial_fibrillation"
        ],
        "medications": [
            "amlodipine",
            "calcium_carbonate",
            "ibuprofen",
            "levothyroxine",
            "linezolid",
            "losartan",
            "metoprolol",
            "sertraline",
            "simvastatin",
            "spironolactone",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0116-1",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-H-0116-2",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0116-3",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            },
            {
                "interaction_id": "INT-SYN-H-0116-4",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-H-0116-5",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0116-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0116-1",
                "replace_drug": "ibuprofen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.56,
                "rationale": "reduces interaction burden from ibuprofen"
            },
            {
                "regimen_id": "REG-SYN-H-0116-2",
                "replace_drug": "metoprolol",
                "with_drug": "bisoprolol",
                "target_condition": "rate_control",
                "expected_risk_delta": 0.36,
                "rationale": "modest risk reduction by replacing metoprolol"
            },
            {
                "regimen_id": "REG-SYN-H-0116-3",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.42,
                "rationale": "modest risk reduction by replacing simvastatin"
            },
            {
                "regimen_id": "REG-SYN-H-0116-4",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.26,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0117",
        "age": 85,
        "labs": {
            "egfr": 40.7,
            "creatinine": 2.6,
            "potassium": 5.5,
            "inr": 2.1,
            "alt": 162.3,
            "ast": 140.8
        },
        "diagnoses": [
            "gout",
            "chronic_kidney_disease",
            "coronary_artery_disease"
        ],
        "medications": [
            "calcium_carbonate",
            "cetirizine",
            "clopidogrel",
            "diltiazem",
            "lisinopril",
            "metoprolol",
            "metronidazole",
            "nitroglycerin",
            "omeprazole",
            "sildenafil",
            "simvastatin",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0117-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0117-2",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-H-0117-3",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            },
            {
                "interaction_id": "INT-SYN-H-0117-4",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-H-0117-5",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0117-1",
            "REG-SYN-H-0117-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0117-1",
                "replace_drug": "metronidazole",
                "with_drug": "doxycycline",
                "target_condition": "infection",
                "expected_risk_delta": 0.89,
                "rationale": "reduces interaction burden from metronidazole"
            },
            {
                "regimen_id": "REG-SYN-H-0117-2",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.65,
                "rationale": "reduces interaction burden from omeprazole"
            },
            {
                "regimen_id": "REG-SYN-H-0117-3",
                "replace_drug": "metoprolol",
                "with_drug": "bisoprolol",
                "target_condition": "rate_control",
                "expected_risk_delta": 0.29,
                "rationale": "modest risk reduction by replacing metoprolol"
            },
            {
                "regimen_id": "REG-SYN-H-0117-4",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.42,
                "rationale": "modest risk reduction by replacing simvastatin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0118",
        "age": 95,
        "labs": {
            "egfr": 32.0,
            "creatinine": 2.4,
            "potassium": 4.9,
            "inr": 2.5,
            "alt": 129.4,
            "ast": 102.2
        },
        "diagnoses": [
            "chronic_pain",
            "atrial_fibrillation",
            "hypothyroidism"
        ],
        "medications": [
            "apixaban",
            "clarithromycin",
            "digoxin",
            "furosemide",
            "naproxen",
            "rivaroxaban",
            "simvastatin",
            "spironolactone",
            "ticagrelor",
            "trimethoprim_sulfamethoxazole",
            "valsartan",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0118-1",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0118-2",
                "drug_a": "digoxin",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "P-gp inhibition can raise digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0118-3",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0118-4",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            },
            {
                "interaction_id": "INT-SYN-H-0118-5",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0118-1",
            "REG-SYN-H-0118-3",
            "REG-SYN-H-0118-5"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0118-1",
                "replace_drug": "trimethoprim_sulfamethoxazole",
                "with_drug": "cephalexin",
                "target_condition": "infection",
                "expected_risk_delta": 0.65,
                "rationale": "reduces interaction burden from trimethoprim_sulfamethoxazole"
            },
            {
                "regimen_id": "REG-SYN-H-0118-2",
                "replace_drug": "digoxin",
                "with_drug": "bisoprolol",
                "target_condition": "rate_control",
                "expected_risk_delta": 0.28,
                "rationale": "modest risk reduction by replacing digoxin"
            },
            {
                "regimen_id": "REG-SYN-H-0118-3",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.61,
                "rationale": "reduces interaction burden from clarithromycin"
            },
            {
                "regimen_id": "REG-SYN-H-0118-4",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.34,
                "rationale": "modest risk reduction by replacing spironolactone"
            },
            {
                "regimen_id": "REG-SYN-H-0118-5",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.82,
                "rationale": "reduces interaction burden from naproxen"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0119",
        "age": 94,
        "labs": {
            "egfr": 36.0,
            "creatinine": 2.1,
            "potassium": 4.9,
            "inr": 2.2,
            "alt": 114.2,
            "ast": 112.4
        },
        "diagnoses": [
            "hypothyroidism",
            "hypertension",
            "chronic_liver_disease",
            "heart_failure"
        ],
        "medications": [
            "amiodarone",
            "apixaban",
            "digoxin",
            "diltiazem",
            "furosemide",
            "metoprolol",
            "naproxen",
            "trimethoprim_sulfamethoxazole",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0119-1",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0119-2",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0119-3",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-H-0119-4",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0119-1",
            "REG-SYN-H-0119-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0119-1",
                "replace_drug": "trimethoprim_sulfamethoxazole",
                "with_drug": "cephalexin",
                "target_condition": "infection",
                "expected_risk_delta": 0.7,
                "rationale": "reduces interaction burden from trimethoprim_sulfamethoxazole"
            },
            {
                "regimen_id": "REG-SYN-H-0119-2",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.76,
                "rationale": "reduces interaction burden from naproxen"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0120",
        "age": 89,
        "labs": {
            "egfr": 30.4,
            "creatinine": 2.4,
            "potassium": 5.2,
            "inr": 2.2,
            "alt": 123.6,
            "ast": 112.5
        },
        "diagnoses": [
            "nonalcoholic_steatohepatitis",
            "hypertension",
            "osteoarthritis",
            "heart_failure"
        ],
        "medications": [
            "apixaban",
            "ciprofloxacin",
            "furosemide",
            "glipizide",
            "naproxen",
            "omeprazole",
            "rivaroxaban",
            "spironolactone",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0120-1",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0120-2",
                "drug_a": "furosemide",
                "drug_b": "warfarin",
                "severity": "minor",
                "evidence": "volume changes may alter INR stability"
            },
            {
                "interaction_id": "INT-SYN-H-0120-3",
                "drug_a": "glipizide",
                "drug_b": "ciprofloxacin",
                "severity": "moderate",
                "evidence": "dysglycemia risk from fluoroquinolone-sulfonylurea combination"
            },
            {
                "interaction_id": "INT-SYN-H-0120-4",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0120-1",
            "REG-SYN-H-0120-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0120-1",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.7,
                "rationale": "reduces interaction burden from naproxen"
            },
            {
                "regimen_id": "REG-SYN-H-0120-3",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.86,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0121",
        "age": 85,
        "labs": {
            "egfr": 33.3,
            "creatinine": 2.8,
            "potassium": 5.6,
            "inr": 2.9,
            "alt": 111.4,
            "ast": 109.8
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "hypothyroidism",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "allopurinol",
            "amlodipine",
            "azithromycin",
            "calcium_carbonate",
            "cetirizine",
            "citalopram",
            "furosemide",
            "linezolid",
            "metformin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0121-1",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-H-0121-2",
                "drug_a": "allopurinol",
                "drug_b": "warfarin",
                "severity": "moderate",
                "evidence": "allopurinol may enhance warfarin anticoagulation"
            },
            {
                "interaction_id": "INT-SYN-H-0121-3",
                "drug_a": "cetirizine",
                "drug_b": "amlodipine",
                "severity": "minor",
                "evidence": "possible additive sedation in elderly"
            },
            {
                "interaction_id": "INT-SYN-H-0121-4",
                "drug_a": "metformin",
                "drug_b": "furosemide",
                "severity": "moderate",
                "evidence": "reduced renal clearance can increase lactic acidosis risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0122",
        "age": 93,
        "labs": {
            "egfr": 25.3,
            "creatinine": 2.4,
            "potassium": 5.3,
            "inr": 2.8,
            "alt": 118.1,
            "ast": 113.5
        },
        "diagnoses": [
            "gout",
            "type_2_diabetes",
            "atrial_fibrillation"
        ],
        "medications": [
            "amiodarone",
            "amlodipine",
            "ciprofloxacin",
            "ferrous_sulfate",
            "furosemide",
            "glipizide",
            "metoprolol",
            "simvastatin",
            "spironolactone",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0122-1",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0122-2",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-H-0122-3",
                "drug_a": "glipizide",
                "drug_b": "ciprofloxacin",
                "severity": "moderate",
                "evidence": "dysglycemia risk from fluoroquinolone-sulfonylurea combination"
            },
            {
                "interaction_id": "INT-SYN-H-0122-4",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0122-2",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.32,
                "rationale": "modest risk reduction by replacing simvastatin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0123",
        "age": 87,
        "labs": {
            "egfr": 41.5,
            "creatinine": 2.3,
            "potassium": 4.8,
            "inr": 2.6,
            "alt": 120.6,
            "ast": 110.5
        },
        "diagnoses": [
            "nonalcoholic_steatohepatitis",
            "chronic_pain",
            "dyslipidemia",
            "anemia",
            "heart_failure"
        ],
        "medications": [
            "amiodarone",
            "azithromycin",
            "ciprofloxacin",
            "digoxin",
            "diltiazem",
            "ferrous_sulfate",
            "isosorbide_mononitrate",
            "nitroglycerin",
            "prednisone",
            "sildenafil",
            "simvastatin",
            "trimethoprim_sulfamethoxazole",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0123-1",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0123-2",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            },
            {
                "interaction_id": "INT-SYN-H-0123-3",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-H-0123-4",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-H-0123-5",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            }
        ],
        "required_regimens": [],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0123-1",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.37,
                "rationale": "modest risk reduction by replacing simvastatin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0124",
        "age": 95,
        "labs": {
            "egfr": 40.8,
            "creatinine": 2.1,
            "potassium": 5.5,
            "inr": 3.1,
            "alt": 150.4,
            "ast": 179.1
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "nonalcoholic_steatohepatitis",
            "hypertension"
        ],
        "medications": [
            "amlodipine",
            "atorvastatin",
            "azithromycin",
            "ciprofloxacin",
            "clopidogrel",
            "digoxin",
            "diltiazem",
            "furosemide",
            "metoprolol",
            "nitroglycerin",
            "omeprazole",
            "sildenafil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0124-1",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-H-0124-2",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-H-0124-3",
                "drug_a": "amlodipine",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive hypotension in frail adults"
            },
            {
                "interaction_id": "INT-SYN-H-0124-4",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-H-0124-5",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "CYP3A4 inhibition raises statin concentration"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0124-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0124-1",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.63,
                "rationale": "reduces interaction burden from omeprazole"
            },
            {
                "regimen_id": "REG-SYN-H-0124-2",
                "replace_drug": "atorvastatin",
                "with_drug": "rosuvastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.44,
                "rationale": "modest risk reduction by replacing atorvastatin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0125",
        "age": 88,
        "labs": {
            "egfr": 27.0,
            "creatinine": 2.4,
            "potassium": 5.0,
            "inr": 2.6
        },
        "diagnoses": [
            "anxiety",
            "chronic_kidney_disease",
            "coronary_artery_disease",
            "chronic_liver_disease",
            "peripheral_artery_disease"
        ],
        "medications": [
            "allopurinol",
            "apixaban",
            "atorvastatin",
            "ciprofloxacin",
            "diclofenac",
            "fluconazole",
            "glipizide",
            "isosorbide_mononitrate",
            "sildenafil",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0125-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0125-2",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-H-0125-3",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            },
            {
                "interaction_id": "INT-SYN-H-0125-4",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0125-1",
            "REG-SYN-H-0125-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0125-1",
                "replace_drug": "fluconazole",
                "with_drug": "micafungin",
                "target_condition": "infection",
                "expected_risk_delta": 0.82,
                "rationale": "reduces interaction burden from fluconazole"
            },
            {
                "regimen_id": "REG-SYN-H-0125-2",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.68,
                "rationale": "reduces interaction burden from diclofenac"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0126",
        "age": 86,
        "labs": {
            "egfr": 31.0,
            "creatinine": 2.7,
            "potassium": 5.2,
            "inr": 3.0
        },
        "diagnoses": [
            "nonalcoholic_steatohepatitis",
            "hypertension",
            "peripheral_artery_disease"
        ],
        "medications": [
            "amiodarone",
            "apixaban",
            "ciprofloxacin",
            "clopidogrel",
            "isosorbide_mononitrate",
            "metoprolol",
            "naproxen",
            "nitroglycerin",
            "omeprazole",
            "paroxetine",
            "sildenafil",
            "simvastatin",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0126-1",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0126-2",
                "drug_a": "metoprolol",
                "drug_b": "paroxetine",
                "severity": "moderate",
                "evidence": "CYP2D6 inhibition raises metoprolol exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0126-3",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-H-0126-4",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-H-0126-5",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0126-1",
            "REG-SYN-H-0126-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0126-1",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.69,
                "rationale": "reduces interaction burden from naproxen"
            },
            {
                "regimen_id": "REG-SYN-H-0126-3",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.71,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0127",
        "age": 87,
        "labs": {
            "egfr": 41.2,
            "creatinine": 2.2,
            "potassium": 4.9,
            "inr": 3.0
        },
        "diagnoses": [
            "chronic_liver_disease",
            "hypothyroidism",
            "depression",
            "peripheral_artery_disease"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "aspirin",
            "azithromycin",
            "dabigatran",
            "diclofenac",
            "ferrous_sulfate",
            "isosorbide_mononitrate",
            "ketoconazole",
            "naproxen",
            "prednisone",
            "sertraline"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0127-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0127-2",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0127-3",
                "drug_a": "aspirin",
                "drug_b": "sertraline",
                "severity": "minor",
                "evidence": "increased bleeding tendency, amplified in frailty"
            },
            {
                "interaction_id": "INT-SYN-H-0127-4",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0127-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0127-1",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.69,
                "rationale": "reduces interaction burden from diclofenac"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0128",
        "age": 93,
        "labs": {
            "egfr": 29.3,
            "creatinine": 1.8,
            "potassium": 5.4,
            "inr": 2.9
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "type_2_diabetes",
            "chronic_pain",
            "dyslipidemia",
            "heart_failure"
        ],
        "medications": [
            "amiodarone",
            "apixaban",
            "aspirin",
            "atorvastatin",
            "clopidogrel",
            "diclofenac",
            "diltiazem",
            "furosemide",
            "ibuprofen",
            "omeprazole",
            "prednisone",
            "sertraline",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0128-1",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0128-2",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0128-3",
                "drug_a": "aspirin",
                "drug_b": "sertraline",
                "severity": "minor",
                "evidence": "increased bleeding tendency, amplified in frailty"
            },
            {
                "interaction_id": "INT-SYN-H-0128-4",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "CYP3A4 inhibition raises statin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0128-5",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0128-1",
            "REG-SYN-H-0128-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0128-1",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.87,
                "rationale": "reduces interaction burden from diclofenac"
            },
            {
                "regimen_id": "REG-SYN-H-0128-2",
                "replace_drug": "atorvastatin",
                "with_drug": "rosuvastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.28,
                "rationale": "modest risk reduction by replacing atorvastatin"
            },
            {
                "regimen_id": "REG-SYN-H-0128-3",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.66,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0129",
        "age": 95,
        "labs": {
            "egfr": 40.8,
            "creatinine": 2.1,
            "potassium": 5.6,
            "inr": 3.1,
            "alt": 113.6,
            "ast": 112.2
        },
        "diagnoses": [
            "hypothyroidism",
            "heart_failure",
            "gout",
            "chronic_liver_disease",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "amiodarone",
            "apixaban",
            "calcium_carbonate",
            "dabigatran",
            "diltiazem",
            "levothyroxine",
            "losartan",
            "naproxen",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0129-1",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0129-2",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            },
            {
                "interaction_id": "INT-SYN-H-0129-3",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0129-4",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0129-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0129-1",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.27,
                "rationale": "modest risk reduction by replacing spironolactone"
            },
            {
                "regimen_id": "REG-SYN-H-0129-2",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.65,
                "rationale": "reduces interaction burden from naproxen"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0130",
        "age": 85,
        "labs": {
            "egfr": 41.4,
            "creatinine": 2.8,
            "potassium": 5.0,
            "inr": 2.7,
            "alt": 161.8,
            "ast": 164.5
        },
        "diagnoses": [
            "atrial_fibrillation",
            "peripheral_artery_disease",
            "osteoarthritis",
            "depression"
        ],
        "medications": [
            "amiodarone",
            "amlodipine",
            "azithromycin",
            "calcium_carbonate",
            "citalopram",
            "clopidogrel",
            "digoxin",
            "diltiazem",
            "levothyroxine",
            "nitroglycerin",
            "omeprazole",
            "sildenafil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0130-1",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-H-0130-2",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-H-0130-3",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-H-0130-4",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-H-0130-5",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0130-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0130-1",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.88,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0131",
        "age": 86,
        "labs": {
            "egfr": 29.3,
            "creatinine": 2.5,
            "potassium": 5.0,
            "inr": 2.1
        },
        "diagnoses": [
            "dyslipidemia",
            "hypothyroidism",
            "osteoarthritis",
            "depression"
        ],
        "medications": [
            "amiodarone",
            "azithromycin",
            "calcium_carbonate",
            "diclofenac",
            "digoxin",
            "ibuprofen",
            "losartan",
            "metoprolol",
            "prednisone",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0131-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0131-2",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            },
            {
                "interaction_id": "INT-SYN-H-0131-3",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0131-4",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0131-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0131-1",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.64,
                "rationale": "reduces interaction burden from diclofenac"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0132",
        "age": 90,
        "labs": {
            "egfr": 33.1,
            "creatinine": 2.4,
            "potassium": 4.9,
            "inr": 3.0,
            "alt": 112.0,
            "ast": 122.1
        },
        "diagnoses": [
            "depression",
            "nonalcoholic_steatohepatitis",
            "anemia",
            "gout",
            "chronic_pain"
        ],
        "medications": [
            "amiodarone",
            "apixaban",
            "clarithromycin",
            "diltiazem",
            "isosorbide_mononitrate",
            "linezolid",
            "naproxen",
            "omeprazole",
            "rivaroxaban",
            "simvastatin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0132-1",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0132-2",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-H-0132-3",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0132-4",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0132-2",
            "REG-SYN-H-0132-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0132-1",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.25,
                "rationale": "modest risk reduction by replacing simvastatin"
            },
            {
                "regimen_id": "REG-SYN-H-0132-2",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.88,
                "rationale": "reduces interaction burden from clarithromycin"
            },
            {
                "regimen_id": "REG-SYN-H-0132-3",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.72,
                "rationale": "reduces interaction burden from naproxen"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0133",
        "age": 87,
        "labs": {
            "egfr": 42.2,
            "creatinine": 2.1,
            "potassium": 5.2,
            "inr": 2.6,
            "alt": 183.7,
            "ast": 161.1
        },
        "diagnoses": [
            "chronic_liver_disease",
            "osteoarthritis",
            "gout",
            "dyslipidemia"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "atorvastatin",
            "diclofenac",
            "furosemide",
            "glipizide",
            "ibuprofen",
            "metoprolol",
            "omeprazole",
            "simvastatin",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0133-1",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-H-0133-2",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0133-3",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-H-0133-4",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-H-0133-5",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0133-1",
            "REG-SYN-H-0133-2",
            "REG-SYN-H-0133-4"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0133-1",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.78,
                "rationale": "reduces interaction burden from omeprazole"
            },
            {
                "regimen_id": "REG-SYN-H-0133-2",
                "replace_drug": "ibuprofen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.83,
                "rationale": "reduces interaction burden from ibuprofen"
            },
            {
                "regimen_id": "REG-SYN-H-0133-3",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.39,
                "rationale": "modest risk reduction by replacing simvastatin"
            },
            {
                "regimen_id": "REG-SYN-H-0133-4",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.76,
                "rationale": "reduces interaction burden from diclofenac"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0134",
        "age": 88,
        "labs": {
            "egfr": 30.6,
            "creatinine": 2.6,
            "potassium": 5.3,
            "inr": 2.7,
            "alt": 188.6,
            "ast": 147.6
        },
        "diagnoses": [
            "nonalcoholic_steatohepatitis",
            "chronic_liver_disease",
            "heart_failure",
            "dyslipidemia"
        ],
        "medications": [
            "apixaban",
            "azithromycin",
            "calcium_carbonate",
            "citalopram",
            "clarithromycin",
            "diltiazem",
            "furosemide",
            "glipizide",
            "ibuprofen",
            "levothyroxine",
            "metformin",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0134-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0134-2",
                "drug_a": "metformin",
                "drug_b": "furosemide",
                "severity": "moderate",
                "evidence": "reduced renal clearance can increase lactic acidosis risk"
            },
            {
                "interaction_id": "INT-SYN-H-0134-3",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-H-0134-4",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-H-0134-5",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0134-1",
            "REG-SYN-H-0134-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0134-1",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.66,
                "rationale": "reduces interaction burden from clarithromycin"
            },
            {
                "regimen_id": "REG-SYN-H-0134-3",
                "replace_drug": "ibuprofen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.88,
                "rationale": "reduces interaction burden from ibuprofen"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0135",
        "age": 87,
        "labs": {
            "egfr": 29.8,
            "creatinine": 2.6,
            "potassium": 5.4,
            "inr": 2.1,
            "alt": 111.7,
            "ast": 116.6
        },
        "diagnoses": [
            "chronic_liver_disease",
            "gout",
            "peripheral_artery_disease",
            "coronary_artery_disease"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "azithromycin",
            "ciprofloxacin",
            "diltiazem",
            "isosorbide_mononitrate",
            "naproxen",
            "paroxetine",
            "prednisone",
            "sildenafil",
            "simvastatin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0135-1",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-H-0135-2",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0135-3",
                "drug_a": "amlodipine",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive hypotension in frail adults"
            },
            {
                "interaction_id": "INT-SYN-H-0135-4",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0135-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0135-1",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.81,
                "rationale": "reduces interaction burden from naproxen"
            },
            {
                "regimen_id": "REG-SYN-H-0135-2",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.44,
                "rationale": "modest risk reduction by replacing simvastatin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0136",
        "age": 86,
        "labs": {
            "egfr": 36.4,
            "creatinine": 2.5,
            "potassium": 5.4,
            "inr": 2.6,
            "alt": 113.3,
            "ast": 121.0
        },
        "diagnoses": [
            "anemia",
            "heart_failure",
            "osteoarthritis",
            "hypothyroidism"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "ciprofloxacin",
            "clarithromycin",
            "clopidogrel",
            "diclofenac",
            "losartan",
            "omeprazole",
            "simvastatin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0136-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0136-2",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0136-3",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-H-0136-4",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0136-1",
            "REG-SYN-H-0136-2",
            "REG-SYN-H-0136-4"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0136-1",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.9,
                "rationale": "reduces interaction burden from clarithromycin"
            },
            {
                "regimen_id": "REG-SYN-H-0136-2",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.81,
                "rationale": "reduces interaction burden from diclofenac"
            },
            {
                "regimen_id": "REG-SYN-H-0136-3",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.42,
                "rationale": "modest risk reduction by replacing simvastatin"
            },
            {
                "regimen_id": "REG-SYN-H-0136-4",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.68,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0137",
        "age": 94,
        "labs": {
            "egfr": 31.2,
            "creatinine": 2.0,
            "potassium": 5.4,
            "inr": 2.4,
            "alt": 192.8,
            "ast": 154.9
        },
        "diagnoses": [
            "chronic_pain",
            "atrial_fibrillation",
            "type_2_diabetes"
        ],
        "medications": [
            "dabigatran",
            "diclofenac",
            "furosemide",
            "isosorbide_mononitrate",
            "lisinopril",
            "metoprolol",
            "naproxen",
            "rivaroxaban",
            "sildenafil",
            "spironolactone",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0137-1",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-H-0137-2",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0137-3",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0137-4",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-H-0137-5",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0137-1",
            "REG-SYN-H-0137-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0137-1",
                "replace_drug": "trimethoprim_sulfamethoxazole",
                "with_drug": "cephalexin",
                "target_condition": "infection",
                "expected_risk_delta": 0.7,
                "rationale": "reduces interaction burden from trimethoprim_sulfamethoxazole"
            },
            {
                "regimen_id": "REG-SYN-H-0137-2",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.65,
                "rationale": "reduces interaction burden from naproxen"
            },
            {
                "regimen_id": "REG-SYN-H-0137-3",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.49,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0138",
        "age": 87,
        "labs": {
            "egfr": 40.8,
            "creatinine": 2.2,
            "potassium": 5.1,
            "inr": 3.1,
            "alt": 121.5,
            "ast": 117.9
        },
        "diagnoses": [
            "type_2_diabetes",
            "anxiety",
            "chronic_pain",
            "chronic_kidney_disease",
            "hypertension"
        ],
        "medications": [
            "amiodarone",
            "apixaban",
            "clopidogrel",
            "digoxin",
            "ferrous_sulfate",
            "furosemide",
            "linezolid",
            "losartan",
            "metformin",
            "omeprazole",
            "sertraline",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0138-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-H-0138-2",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0138-3",
                "drug_a": "metformin",
                "drug_b": "furosemide",
                "severity": "moderate",
                "evidence": "reduced renal clearance can increase lactic acidosis risk"
            },
            {
                "interaction_id": "INT-SYN-H-0138-4",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-H-0138-5",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0138-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0138-1",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.79,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0139",
        "age": 90,
        "labs": {
            "egfr": 31.7,
            "creatinine": 2.0,
            "potassium": 5.0,
            "inr": 2.1
        },
        "diagnoses": [
            "hypothyroidism",
            "atrial_fibrillation",
            "hypertension",
            "chronic_pain"
        ],
        "medications": [
            "apixaban",
            "azithromycin",
            "clarithromycin",
            "clopidogrel",
            "fluconazole",
            "furosemide",
            "metoprolol",
            "omeprazole",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0139-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0139-2",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0139-3",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-H-0139-4",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0139-1",
            "REG-SYN-H-0139-2",
            "REG-SYN-H-0139-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0139-1",
                "replace_drug": "fluconazole",
                "with_drug": "micafungin",
                "target_condition": "infection",
                "expected_risk_delta": 0.85,
                "rationale": "reduces interaction burden from fluconazole"
            },
            {
                "regimen_id": "REG-SYN-H-0139-2",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.89,
                "rationale": "reduces interaction burden from clarithromycin"
            },
            {
                "regimen_id": "REG-SYN-H-0139-3",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.68,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0140",
        "age": 86,
        "labs": {
            "egfr": 25.6,
            "creatinine": 1.9,
            "potassium": 4.9,
            "inr": 3.1
        },
        "diagnoses": [
            "hypothyroidism",
            "depression",
            "anxiety"
        ],
        "medications": [
            "amlodipine",
            "aspirin",
            "ciprofloxacin",
            "ferrous_sulfate",
            "metoprolol",
            "metronidazole",
            "nitroglycerin",
            "paroxetine",
            "sertraline",
            "spironolactone",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0140-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0140-2",
                "drug_a": "aspirin",
                "drug_b": "sertraline",
                "severity": "minor",
                "evidence": "increased bleeding tendency, amplified in frailty"
            },
            {
                "interaction_id": "INT-SYN-H-0140-3",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            },
            {
                "interaction_id": "INT-SYN-H-0140-4",
                "drug_a": "amlodipine",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive hypotension in frail adults"
            },
            {
                "interaction_id": "INT-SYN-H-0140-5",
                "drug_a": "metoprolol",
                "drug_b": "paroxetine",
                "severity": "moderate",
                "evidence": "CYP2D6 inhibition raises metoprolol exposure"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0140-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0140-1",
                "replace_drug": "metronidazole",
                "with_drug": "doxycycline",
                "target_condition": "infection",
                "expected_risk_delta": 0.84,
                "rationale": "reduces interaction burden from metronidazole"
            },
            {
                "regimen_id": "REG-SYN-H-0140-2",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.49,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0141",
        "age": 94,
        "labs": {
            "egfr": 43.4,
            "creatinine": 1.9,
            "potassium": 5.5,
            "inr": 2.3,
            "alt": 164.4,
            "ast": 171.5
        },
        "diagnoses": [
            "atrial_fibrillation",
            "hypertension",
            "peripheral_artery_disease",
            "dyslipidemia",
            "gout"
        ],
        "medications": [
            "dabigatran",
            "ferrous_sulfate",
            "furosemide",
            "ketoconazole",
            "metoprolol",
            "metronidazole",
            "nitroglycerin",
            "sildenafil",
            "trimethoprim_sulfamethoxazole",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0141-1",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-H-0141-2",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0141-3",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-H-0141-4",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0141-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0141-1",
                "replace_drug": "metronidazole",
                "with_drug": "doxycycline",
                "target_condition": "infection",
                "expected_risk_delta": 0.61,
                "rationale": "reduces interaction burden from metronidazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0142",
        "age": 95,
        "labs": {
            "egfr": 34.7,
            "creatinine": 2.6,
            "potassium": 5.0,
            "inr": 3.0,
            "alt": 129.6,
            "ast": 122.0
        },
        "diagnoses": [
            "dyslipidemia",
            "gout",
            "osteoarthritis"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "aspirin",
            "azithromycin",
            "calcium_carbonate",
            "clarithromycin",
            "digoxin",
            "furosemide",
            "levothyroxine",
            "metformin",
            "metoprolol",
            "trimethoprim_sulfamethoxazole",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0142-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0142-2",
                "drug_a": "digoxin",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "P-gp inhibition can raise digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0142-3",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0142-4",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-H-0142-5",
                "drug_a": "metformin",
                "drug_b": "furosemide",
                "severity": "moderate",
                "evidence": "reduced renal clearance can increase lactic acidosis risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0142-1",
            "REG-SYN-H-0142-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0142-1",
                "replace_drug": "aspirin",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.85,
                "rationale": "reduces interaction burden from aspirin"
            },
            {
                "regimen_id": "REG-SYN-H-0142-2",
                "replace_drug": "digoxin",
                "with_drug": "bisoprolol",
                "target_condition": "rate_control",
                "expected_risk_delta": 0.44,
                "rationale": "modest risk reduction by replacing digoxin"
            },
            {
                "regimen_id": "REG-SYN-H-0142-3",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.66,
                "rationale": "reduces interaction burden from clarithromycin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0143",
        "age": 89,
        "labs": {
            "egfr": 28.9,
            "creatinine": 2.8,
            "potassium": 5.2,
            "inr": 2.5,
            "alt": 175.5,
            "ast": 137.6
        },
        "diagnoses": [
            "heart_failure",
            "nonalcoholic_steatohepatitis",
            "anxiety",
            "anemia"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "aspirin",
            "calcium_carbonate",
            "ciprofloxacin",
            "clarithromycin",
            "fluconazole",
            "isosorbide_mononitrate",
            "naproxen",
            "prednisone",
            "sertraline",
            "sildenafil",
            "simvastatin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0143-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0143-2",
                "drug_a": "aspirin",
                "drug_b": "sertraline",
                "severity": "minor",
                "evidence": "increased bleeding tendency, amplified in frailty"
            },
            {
                "interaction_id": "INT-SYN-H-0143-3",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-H-0143-4",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-H-0143-5",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0143-1",
            "REG-SYN-H-0143-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0143-1",
                "replace_drug": "fluconazole",
                "with_drug": "micafungin",
                "target_condition": "infection",
                "expected_risk_delta": 0.74,
                "rationale": "reduces interaction burden from fluconazole"
            },
            {
                "regimen_id": "REG-SYN-H-0143-2",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.35,
                "rationale": "modest risk reduction by replacing simvastatin"
            },
            {
                "regimen_id": "REG-SYN-H-0143-3",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.81,
                "rationale": "reduces interaction burden from naproxen"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0144",
        "age": 88,
        "labs": {
            "egfr": 32.3,
            "creatinine": 1.9,
            "potassium": 5.3,
            "inr": 2.7
        },
        "diagnoses": [
            "depression",
            "hypertension",
            "heart_failure",
            "gout",
            "atrial_fibrillation"
        ],
        "medications": [
            "amlodipine",
            "calcium_carbonate",
            "ciprofloxacin",
            "clopidogrel",
            "dabigatran",
            "fluconazole",
            "ketoconazole",
            "levothyroxine",
            "metoprolol",
            "naproxen",
            "omeprazole",
            "trimethoprim_sulfamethoxazole",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0144-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-H-0144-2",
                "drug_a": "amlodipine",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive hypotension in frail adults"
            },
            {
                "interaction_id": "INT-SYN-H-0144-3",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0144-4",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            },
            {
                "interaction_id": "INT-SYN-H-0144-5",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0144-1",
            "REG-SYN-H-0144-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0144-1",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.65,
                "rationale": "reduces interaction burden from omeprazole"
            },
            {
                "regimen_id": "REG-SYN-H-0144-2",
                "replace_drug": "fluconazole",
                "with_drug": "micafungin",
                "target_condition": "infection",
                "expected_risk_delta": 0.65,
                "rationale": "reduces interaction burden from fluconazole"
            },
            {
                "regimen_id": "REG-SYN-H-0144-3",
                "replace_drug": "metoprolol",
                "with_drug": "bisoprolol",
                "target_condition": "rate_control",
                "expected_risk_delta": 0.48,
                "rationale": "modest risk reduction by replacing metoprolol"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0145",
        "age": 87,
        "labs": {
            "egfr": 41.1,
            "creatinine": 2.7,
            "potassium": 5.6,
            "inr": 2.9,
            "alt": 115.3,
            "ast": 102.8
        },
        "diagnoses": [
            "anemia",
            "osteoarthritis",
            "hypothyroidism"
        ],
        "medications": [
            "ciprofloxacin",
            "ferrous_sulfate",
            "glipizide",
            "levothyroxine",
            "linezolid",
            "nitroglycerin",
            "omeprazole",
            "sildenafil",
            "simvastatin",
            "ticagrelor",
            "valsartan",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0145-1",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-H-0145-2",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-H-0145-3",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-H-0145-4",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0145-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0145-1",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.68,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0146",
        "age": 90,
        "labs": {
            "egfr": 26.3,
            "creatinine": 2.8,
            "potassium": 5.4,
            "inr": 2.2,
            "alt": 121.6,
            "ast": 122.9
        },
        "diagnoses": [
            "anemia",
            "chronic_liver_disease",
            "nonalcoholic_steatohepatitis",
            "chronic_kidney_disease",
            "gout"
        ],
        "medications": [
            "amiodarone",
            "cetirizine",
            "diclofenac",
            "digoxin",
            "furosemide",
            "lisinopril",
            "losartan",
            "omeprazole",
            "sildenafil",
            "spironolactone",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0146-1",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0146-2",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0146-3",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-H-0146-4",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0146-1",
            "REG-SYN-H-0146-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0146-1",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.6,
                "rationale": "reduces interaction burden from diclofenac"
            },
            {
                "regimen_id": "REG-SYN-H-0146-2",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.66,
                "rationale": "reduces interaction burden from omeprazole"
            },
            {
                "regimen_id": "REG-SYN-H-0146-3",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.49,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0147",
        "age": 85,
        "labs": {
            "egfr": 30.3,
            "creatinine": 2.7,
            "potassium": 5.1,
            "inr": 2.0
        },
        "diagnoses": [
            "dyslipidemia",
            "type_2_diabetes",
            "anxiety",
            "coronary_artery_disease",
            "osteoarthritis"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "ciprofloxacin",
            "clarithromycin",
            "ibuprofen",
            "linezolid",
            "losartan",
            "metformin",
            "rivaroxaban",
            "simvastatin",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0147-1",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0147-2",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            },
            {
                "interaction_id": "INT-SYN-H-0147-3",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0147-4",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0147-1",
            "REG-SYN-H-0147-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0147-1",
                "replace_drug": "ibuprofen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.73,
                "rationale": "reduces interaction burden from ibuprofen"
            },
            {
                "regimen_id": "REG-SYN-H-0147-2",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.34,
                "rationale": "modest risk reduction by replacing spironolactone"
            },
            {
                "regimen_id": "REG-SYN-H-0147-3",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.89,
                "rationale": "reduces interaction burden from clarithromycin"
            },
            {
                "regimen_id": "REG-SYN-H-0147-4",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.37,
                "rationale": "modest risk reduction by replacing simvastatin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0148",
        "age": 91,
        "labs": {
            "egfr": 41.2,
            "creatinine": 2.6,
            "potassium": 5.0,
            "inr": 2.6,
            "alt": 180.9,
            "ast": 156.2
        },
        "diagnoses": [
            "atrial_fibrillation",
            "anemia",
            "peripheral_artery_disease",
            "osteoarthritis",
            "gout"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "ciprofloxacin",
            "clopidogrel",
            "diclofenac",
            "fluconazole",
            "ibuprofen",
            "linezolid",
            "omeprazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0148-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-H-0148-2",
                "drug_a": "amlodipine",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive hypotension in frail adults"
            },
            {
                "interaction_id": "INT-SYN-H-0148-3",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0148-4",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0148-1",
            "REG-SYN-H-0148-2",
            "REG-SYN-H-0148-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0148-1",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.87,
                "rationale": "reduces interaction burden from omeprazole"
            },
            {
                "regimen_id": "REG-SYN-H-0148-2",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.9,
                "rationale": "reduces interaction burden from diclofenac"
            },
            {
                "regimen_id": "REG-SYN-H-0148-3",
                "replace_drug": "ibuprofen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.74,
                "rationale": "reduces interaction burden from ibuprofen"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0149",
        "age": 95,
        "labs": {
            "egfr": 39.7,
            "creatinine": 2.0,
            "potassium": 4.9,
            "inr": 2.7,
            "alt": 195.3,
            "ast": 142.1
        },
        "diagnoses": [
            "hypothyroidism",
            "chronic_liver_disease",
            "coronary_artery_disease",
            "depression"
        ],
        "medications": [
            "amlodipine",
            "furosemide",
            "ketoconazole",
            "linezolid",
            "metformin",
            "metoprolol",
            "sertraline",
            "simvastatin",
            "spironolactone",
            "valsartan"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0149-1",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-H-0149-2",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            },
            {
                "interaction_id": "INT-SYN-H-0149-3",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-H-0149-4",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            }
        ],
        "required_regimens": [],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0149-1",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.33,
                "rationale": "modest risk reduction by replacing spironolactone"
            },
            {
                "regimen_id": "REG-SYN-H-0149-2",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.46,
                "rationale": "modest risk reduction by replacing simvastatin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0150",
        "age": 92,
        "labs": {
            "egfr": 28.1,
            "creatinine": 1.9,
            "potassium": 5.1,
            "inr": 3.0,
            "alt": 165.2,
            "ast": 160.8
        },
        "diagnoses": [
            "atrial_fibrillation",
            "hypertension",
            "chronic_pain"
        ],
        "medications": [
            "apixaban",
            "aspirin",
            "citalopram",
            "clarithromycin",
            "digoxin",
            "ibuprofen",
            "metoprolol",
            "naproxen",
            "nitroglycerin",
            "sildenafil",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0150-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0150-2",
                "drug_a": "digoxin",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "P-gp inhibition can raise digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0150-3",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-H-0150-4",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0150-1",
            "REG-SYN-H-0150-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0150-1",
                "replace_drug": "aspirin",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.68,
                "rationale": "reduces interaction burden from aspirin"
            },
            {
                "regimen_id": "REG-SYN-H-0150-2",
                "replace_drug": "digoxin",
                "with_drug": "bisoprolol",
                "target_condition": "rate_control",
                "expected_risk_delta": 0.34,
                "rationale": "modest risk reduction by replacing digoxin"
            },
            {
                "regimen_id": "REG-SYN-H-0150-3",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.64,
                "rationale": "reduces interaction burden from clarithromycin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0151",
        "age": 94,
        "labs": {
            "egfr": 41.6,
            "creatinine": 2.3,
            "potassium": 5.4,
            "inr": 3.1,
            "alt": 116.8,
            "ast": 107.8
        },
        "diagnoses": [
            "chronic_liver_disease",
            "atrial_fibrillation",
            "type_2_diabetes"
        ],
        "medications": [
            "apixaban",
            "atorvastatin",
            "clopidogrel",
            "dabigatran",
            "diltiazem",
            "ferrous_sulfate",
            "ketoconazole",
            "linezolid",
            "naproxen",
            "omeprazole"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0151-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-H-0151-2",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0151-3",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "CYP3A4 inhibition raises statin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0151-4",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0151-1",
            "REG-SYN-H-0151-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0151-1",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.77,
                "rationale": "reduces interaction burden from omeprazole"
            },
            {
                "regimen_id": "REG-SYN-H-0151-2",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.79,
                "rationale": "reduces interaction burden from naproxen"
            },
            {
                "regimen_id": "REG-SYN-H-0151-3",
                "replace_drug": "atorvastatin",
                "with_drug": "rosuvastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.35,
                "rationale": "modest risk reduction by replacing atorvastatin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0152",
        "age": 88,
        "labs": {
            "egfr": 38.6,
            "creatinine": 2.1,
            "potassium": 4.9,
            "inr": 2.6,
            "alt": 172.2,
            "ast": 154.9
        },
        "diagnoses": [
            "dyslipidemia",
            "depression",
            "hypertension",
            "coronary_artery_disease",
            "hypothyroidism"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "azithromycin",
            "calcium_carbonate",
            "citalopram",
            "dabigatran",
            "ferrous_sulfate",
            "fluconazole",
            "levothyroxine",
            "linezolid",
            "rivaroxaban",
            "sertraline",
            "simvastatin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0152-1",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-H-0152-2",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-H-0152-3",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-H-0152-4",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-H-0152-5",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0152-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0152-1",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.35,
                "rationale": "modest risk reduction by replacing simvastatin"
            },
            {
                "regimen_id": "REG-SYN-H-0152-2",
                "replace_drug": "fluconazole",
                "with_drug": "micafungin",
                "target_condition": "infection",
                "expected_risk_delta": 0.87,
                "rationale": "reduces interaction burden from fluconazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0153",
        "age": 91,
        "labs": {
            "egfr": 31.8,
            "creatinine": 2.2,
            "potassium": 5.3,
            "inr": 3.1,
            "alt": 129.2,
            "ast": 111.7
        },
        "diagnoses": [
            "hypertension",
            "peripheral_artery_disease",
            "chronic_liver_disease",
            "atrial_fibrillation"
        ],
        "medications": [
            "allopurinol",
            "amiodarone",
            "apixaban",
            "azithromycin",
            "clarithromycin",
            "clopidogrel",
            "omeprazole",
            "prednisone",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0153-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0153-2",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            },
            {
                "interaction_id": "INT-SYN-H-0153-3",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0153-4",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0153-1",
            "REG-SYN-H-0153-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0153-1",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.67,
                "rationale": "reduces interaction burden from clarithromycin"
            },
            {
                "regimen_id": "REG-SYN-H-0153-2",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.78,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0154",
        "age": 85,
        "labs": {
            "egfr": 37.1,
            "creatinine": 2.0,
            "potassium": 5.0,
            "inr": 2.6
        },
        "diagnoses": [
            "depression",
            "type_2_diabetes",
            "nonalcoholic_steatohepatitis",
            "hypothyroidism"
        ],
        "medications": [
            "azithromycin",
            "calcium_carbonate",
            "dabigatran",
            "ferrous_sulfate",
            "furosemide",
            "ibuprofen",
            "ketoconazole",
            "levothyroxine",
            "losartan",
            "metformin",
            "metoprolol",
            "nitroglycerin",
            "prednisone",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0154-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0154-2",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-H-0154-3",
                "drug_a": "metformin",
                "drug_b": "furosemide",
                "severity": "moderate",
                "evidence": "reduced renal clearance can increase lactic acidosis risk"
            },
            {
                "interaction_id": "INT-SYN-H-0154-4",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            },
            {
                "interaction_id": "INT-SYN-H-0154-5",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0155",
        "age": 91,
        "labs": {
            "egfr": 41.7,
            "creatinine": 2.5,
            "potassium": 5.0,
            "inr": 2.7,
            "alt": 189.9,
            "ast": 167.5
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "chronic_pain",
            "chronic_liver_disease"
        ],
        "medications": [
            "apixaban",
            "azithromycin",
            "calcium_carbonate",
            "ciprofloxacin",
            "citalopram",
            "diclofenac",
            "digoxin",
            "glipizide",
            "ibuprofen",
            "levothyroxine",
            "linezolid",
            "lisinopril",
            "nitroglycerin",
            "sertraline"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0155-1",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-H-0155-2",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0155-3",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-H-0155-4",
                "drug_a": "glipizide",
                "drug_b": "ciprofloxacin",
                "severity": "moderate",
                "evidence": "dysglycemia risk from fluoroquinolone-sulfonylurea combination"
            },
            {
                "interaction_id": "INT-SYN-H-0155-5",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0155-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0155-1",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.9,
                "rationale": "reduces interaction burden from diclofenac"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0156",
        "age": 86,
        "labs": {
            "egfr": 36.3,
            "creatinine": 2.6,
            "potassium": 5.1,
            "inr": 2.5,
            "alt": 162.5,
            "ast": 143.5
        },
        "diagnoses": [
            "heart_failure",
            "anemia",
            "depression",
            "gout",
            "hypertension"
        ],
        "medications": [
            "amiodarone",
            "amlodipine",
            "digoxin",
            "fluconazole",
            "isosorbide_mononitrate",
            "metoprolol",
            "omeprazole",
            "rivaroxaban",
            "simvastatin",
            "ticagrelor",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0156-1",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-H-0156-2",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0156-3",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0156-4",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-H-0156-5",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0156-1",
            "REG-SYN-H-0156-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0156-1",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.65,
                "rationale": "reduces interaction burden from omeprazole"
            },
            {
                "regimen_id": "REG-SYN-H-0156-2",
                "replace_drug": "fluconazole",
                "with_drug": "micafungin",
                "target_condition": "infection",
                "expected_risk_delta": 0.81,
                "rationale": "reduces interaction burden from fluconazole"
            },
            {
                "regimen_id": "REG-SYN-H-0156-3",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.35,
                "rationale": "modest risk reduction by replacing simvastatin"
            },
            {
                "regimen_id": "REG-SYN-H-0156-4",
                "replace_drug": "metoprolol",
                "with_drug": "bisoprolol",
                "target_condition": "rate_control",
                "expected_risk_delta": 0.48,
                "rationale": "modest risk reduction by replacing metoprolol"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0157",
        "age": 90,
        "labs": {
            "egfr": 36.7,
            "creatinine": 2.3,
            "potassium": 5.2,
            "inr": 2.9,
            "alt": 149.1,
            "ast": 142.2
        },
        "diagnoses": [
            "depression",
            "atrial_fibrillation",
            "osteoarthritis",
            "hypothyroidism",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "amiodarone",
            "amlodipine",
            "azithromycin",
            "ciprofloxacin",
            "clopidogrel",
            "dabigatran",
            "diltiazem",
            "furosemide",
            "isosorbide_mononitrate",
            "metformin",
            "sildenafil",
            "simvastatin",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0157-1",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0157-2",
                "drug_a": "amlodipine",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive hypotension in frail adults"
            },
            {
                "interaction_id": "INT-SYN-H-0157-3",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-H-0157-4",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-H-0157-5",
                "drug_a": "metformin",
                "drug_b": "furosemide",
                "severity": "moderate",
                "evidence": "reduced renal clearance can increase lactic acidosis risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0157-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0157-1",
                "replace_drug": "trimethoprim_sulfamethoxazole",
                "with_drug": "cephalexin",
                "target_condition": "infection",
                "expected_risk_delta": 0.69,
                "rationale": "reduces interaction burden from trimethoprim_sulfamethoxazole"
            },
            {
                "regimen_id": "REG-SYN-H-0157-2",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.35,
                "rationale": "modest risk reduction by replacing simvastatin"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0158",
        "age": 92,
        "labs": {
            "egfr": 41.1,
            "creatinine": 1.9,
            "potassium": 5.0,
            "inr": 3.0,
            "alt": 170.5,
            "ast": 155.2
        },
        "diagnoses": [
            "type_2_diabetes",
            "peripheral_artery_disease",
            "hypertension",
            "osteoarthritis",
            "anemia"
        ],
        "medications": [
            "allopurinol",
            "aspirin",
            "atorvastatin",
            "azithromycin",
            "clopidogrel",
            "diltiazem",
            "isosorbide_mononitrate",
            "losartan",
            "metformin",
            "metoprolol",
            "omeprazole",
            "sildenafil",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0158-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0158-2",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            },
            {
                "interaction_id": "INT-SYN-H-0158-3",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-H-0158-4",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "CYP3A4 inhibition raises statin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-0158-5",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0158-1",
            "REG-SYN-H-0158-4"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0158-1",
                "replace_drug": "aspirin",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.82,
                "rationale": "reduces interaction burden from aspirin"
            },
            {
                "regimen_id": "REG-SYN-H-0158-2",
                "replace_drug": "metoprolol",
                "with_drug": "bisoprolol",
                "target_condition": "rate_control",
                "expected_risk_delta": 0.38,
                "rationale": "modest risk reduction by replacing metoprolol"
            },
            {
                "regimen_id": "REG-SYN-H-0158-3",
                "replace_drug": "atorvastatin",
                "with_drug": "rosuvastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.27,
                "rationale": "modest risk reduction by replacing atorvastatin"
            },
            {
                "regimen_id": "REG-SYN-H-0158-4",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.56,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0159",
        "age": 85,
        "labs": {
            "egfr": 25.5,
            "creatinine": 2.0,
            "potassium": 5.0,
            "inr": 2.4,
            "alt": 121.9,
            "ast": 107.6
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "chronic_liver_disease",
            "type_2_diabetes",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "apixaban",
            "calcium_carbonate",
            "ciprofloxacin",
            "clarithromycin",
            "diclofenac",
            "ferrous_sulfate",
            "glipizide",
            "levothyroxine",
            "linezolid",
            "losartan",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0159-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0159-2",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-H-0159-3",
                "drug_a": "glipizide",
                "drug_b": "ciprofloxacin",
                "severity": "moderate",
                "evidence": "dysglycemia risk from fluoroquinolone-sulfonylurea combination"
            },
            {
                "interaction_id": "INT-SYN-H-0159-4",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0159-5",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0159-1",
            "REG-SYN-H-0159-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0159-1",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.58,
                "rationale": "reduces interaction burden from diclofenac"
            },
            {
                "regimen_id": "REG-SYN-H-0159-3",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.71,
                "rationale": "reduces interaction burden from clarithromycin"
            },
            {
                "regimen_id": "REG-SYN-H-0159-4",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.29,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-0160",
        "age": 92,
        "labs": {
            "egfr": 33.0,
            "creatinine": 1.9,
            "potassium": 5.0,
            "inr": 2.4,
            "alt": 197.6,
            "ast": 160.5
        },
        "diagnoses": [
            "depression",
            "osteoarthritis",
            "peripheral_artery_disease",
            "type_2_diabetes"
        ],
        "medications": [
            "allopurinol",
            "apixaban",
            "ciprofloxacin",
            "dabigatran",
            "diclofenac",
            "furosemide",
            "isosorbide_mononitrate",
            "ketoconazole",
            "metformin",
            "naproxen",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-0160-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-H-0160-2",
                "drug_a": "metformin",
                "drug_b": "furosemide",
                "severity": "moderate",
                "evidence": "reduced renal clearance can increase lactic acidosis risk"
            },
            {
                "interaction_id": "INT-SYN-H-0160-3",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            },
            {
                "interaction_id": "INT-SYN-H-0160-4",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-0160-5",
                "drug_a": "allopurinol",
                "drug_b": "warfarin",
                "severity": "moderate",
                "evidence": "allopurinol may enhance warfarin anticoagulation"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-0160-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-0160-2",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.77,
                "rationale": "reduces interaction burden from diclofenac"
            }
        ],
        "split": "train"
    },
    {
        "case_id": "SYN-H-V0001",
        "age": 92,
        "labs": {
            "egfr": 40.0,
            "creatinine": 2.5,
            "potassium": 5.5,
            "inr": 2.3,
            "alt": 116.5,
            "ast": 110.9
        },
        "diagnoses": [
            "anemia",
            "atrial_fibrillation",
            "osteoarthritis",
            "gout",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "atorvastatin",
            "clarithromycin",
            "diltiazem",
            "glipizide",
            "ibuprofen",
            "isosorbide_mononitrate",
            "lisinopril",
            "metoprolol",
            "sertraline",
            "sildenafil",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-V0001-1",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0001-2",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-H-V0001-3",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            },
            {
                "interaction_id": "INT-SYN-H-V0001-4",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "CYP3A4 inhibition raises statin concentration"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-V0001-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-V0001-1",
                "replace_drug": "ibuprofen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.68,
                "rationale": "reduces interaction burden from ibuprofen"
            },
            {
                "regimen_id": "REG-SYN-H-V0001-2",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.38,
                "rationale": "modest risk reduction by replacing spironolactone"
            },
            {
                "regimen_id": "REG-SYN-H-V0001-3",
                "replace_drug": "atorvastatin",
                "with_drug": "rosuvastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.34,
                "rationale": "modest risk reduction by replacing atorvastatin"
            }
        ],
        "split": "validation",
        "template_family": "synth-val::hard-SYN-H-V0001"
    },
    {
        "case_id": "SYN-H-V0002",
        "age": 87,
        "labs": {
            "egfr": 35.3,
            "creatinine": 2.1,
            "potassium": 5.6,
            "inr": 2.9,
            "alt": 173.0,
            "ast": 179.8
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "nonalcoholic_steatohepatitis",
            "chronic_pain"
        ],
        "medications": [
            "amiodarone",
            "amlodipine",
            "apixaban",
            "atorvastatin",
            "ciprofloxacin",
            "clarithromycin",
            "ferrous_sulfate",
            "fluconazole",
            "glipizide",
            "levothyroxine",
            "linezolid",
            "sertraline"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-V0002-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0002-2",
                "drug_a": "amlodipine",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive hypotension in frail adults"
            },
            {
                "interaction_id": "INT-SYN-H-V0002-3",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0002-4",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-V0002-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-V0002-1",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.87,
                "rationale": "reduces interaction burden from clarithromycin"
            }
        ],
        "split": "validation",
        "template_family": "synth-val::hard-SYN-H-V0002"
    },
    {
        "case_id": "SYN-H-V0003",
        "age": 87,
        "labs": {
            "egfr": 31.0,
            "creatinine": 2.8,
            "potassium": 5.1,
            "inr": 2.8
        },
        "diagnoses": [
            "type_2_diabetes",
            "depression",
            "hypertension",
            "anxiety",
            "gout"
        ],
        "medications": [
            "amiodarone",
            "apixaban",
            "ciprofloxacin",
            "diclofenac",
            "digoxin",
            "glipizide",
            "losartan",
            "metronidazole",
            "prednisone",
            "spironolactone",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-V0003-1",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0003-2",
                "drug_a": "glipizide",
                "drug_b": "ciprofloxacin",
                "severity": "moderate",
                "evidence": "dysglycemia risk from fluoroquinolone-sulfonylurea combination"
            },
            {
                "interaction_id": "INT-SYN-H-V0003-3",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-V0003-4",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            },
            {
                "interaction_id": "INT-SYN-H-V0003-5",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-V0003-1",
            "REG-SYN-H-V0003-4"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-V0003-1",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.61,
                "rationale": "reduces interaction burden from diclofenac"
            },
            {
                "regimen_id": "REG-SYN-H-V0003-3",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.42,
                "rationale": "modest risk reduction by replacing spironolactone"
            },
            {
                "regimen_id": "REG-SYN-H-V0003-4",
                "replace_drug": "metronidazole",
                "with_drug": "doxycycline",
                "target_condition": "infection",
                "expected_risk_delta": 0.72,
                "rationale": "reduces interaction burden from metronidazole"
            }
        ],
        "split": "validation",
        "template_family": "synth-val::hard-SYN-H-V0003"
    },
    {
        "case_id": "SYN-H-V0004",
        "age": 89,
        "labs": {
            "egfr": 32.4,
            "creatinine": 2.4,
            "potassium": 5.0,
            "inr": 2.1
        },
        "diagnoses": [
            "anemia",
            "dyslipidemia",
            "atrial_fibrillation"
        ],
        "medications": [
            "clopidogrel",
            "ferrous_sulfate",
            "fluconazole",
            "furosemide",
            "levothyroxine",
            "metformin",
            "metoprolol",
            "omeprazole",
            "ticagrelor",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-V0004-1",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0004-2",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-H-V0004-3",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-H-V0004-4",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-V0004-1",
            "REG-SYN-H-V0004-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-V0004-1",
                "replace_drug": "trimethoprim_sulfamethoxazole",
                "with_drug": "cephalexin",
                "target_condition": "infection",
                "expected_risk_delta": 0.58,
                "rationale": "reduces interaction burden from trimethoprim_sulfamethoxazole"
            },
            {
                "regimen_id": "REG-SYN-H-V0004-2",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.56,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "validation",
        "template_family": "synth-val::hard-SYN-H-V0004"
    },
    {
        "case_id": "SYN-H-V0005",
        "age": 94,
        "labs": {
            "egfr": 43.2,
            "creatinine": 2.1,
            "potassium": 5.1,
            "inr": 3.2
        },
        "diagnoses": [
            "chronic_liver_disease",
            "depression",
            "hypothyroidism",
            "hypertension"
        ],
        "medications": [
            "ciprofloxacin",
            "citalopram",
            "ferrous_sulfate",
            "levothyroxine",
            "lisinopril",
            "metronidazole",
            "paroxetine",
            "sildenafil",
            "spironolactone",
            "valsartan",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-V0005-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0005-2",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            },
            {
                "interaction_id": "INT-SYN-H-V0005-3",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-H-V0005-4",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-V0005-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-V0005-1",
                "replace_drug": "metronidazole",
                "with_drug": "doxycycline",
                "target_condition": "infection",
                "expected_risk_delta": 0.66,
                "rationale": "reduces interaction burden from metronidazole"
            },
            {
                "regimen_id": "REG-SYN-H-V0005-2",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.4,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "validation",
        "template_family": "synth-val::hard-SYN-H-V0005"
    },
    {
        "case_id": "SYN-H-V0006",
        "age": 85,
        "labs": {
            "egfr": 29.3,
            "creatinine": 1.9,
            "potassium": 5.6,
            "inr": 3.0,
            "alt": 125.4,
            "ast": 122.6
        },
        "diagnoses": [
            "type_2_diabetes",
            "osteoarthritis",
            "heart_failure",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "amiodarone",
            "ciprofloxacin",
            "clopidogrel",
            "digoxin",
            "diltiazem",
            "fluconazole",
            "glipizide",
            "naproxen",
            "omeprazole",
            "rivaroxaban",
            "ticagrelor",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-V0006-1",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-H-V0006-2",
                "drug_a": "digoxin",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "P-gp inhibition can raise digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-V0006-3",
                "drug_a": "glipizide",
                "drug_b": "ciprofloxacin",
                "severity": "moderate",
                "evidence": "dysglycemia risk from fluoroquinolone-sulfonylurea combination"
            },
            {
                "interaction_id": "INT-SYN-H-V0006-4",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0006-5",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-V0006-3",
            "REG-SYN-H-V0006-4"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-V0006-1",
                "replace_drug": "digoxin",
                "with_drug": "bisoprolol",
                "target_condition": "rate_control",
                "expected_risk_delta": 0.4,
                "rationale": "modest risk reduction by replacing digoxin"
            },
            {
                "regimen_id": "REG-SYN-H-V0006-3",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.65,
                "rationale": "reduces interaction burden from naproxen"
            },
            {
                "regimen_id": "REG-SYN-H-V0006-4",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.58,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "validation",
        "template_family": "synth-val::hard-SYN-H-V0006"
    },
    {
        "case_id": "SYN-H-V0007",
        "age": 92,
        "labs": {
            "egfr": 27.2,
            "creatinine": 2.0,
            "potassium": 5.6,
            "inr": 2.7,
            "alt": 196.1,
            "ast": 176.9
        },
        "diagnoses": [
            "osteoarthritis",
            "hypertension",
            "anemia",
            "coronary_artery_disease"
        ],
        "medications": [
            "aspirin",
            "atorvastatin",
            "azithromycin",
            "citalopram",
            "diltiazem",
            "furosemide",
            "linezolid",
            "metformin",
            "rivaroxaban",
            "simvastatin",
            "spironolactone",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-V0007-1",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0007-2",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0007-3",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            },
            {
                "interaction_id": "INT-SYN-H-V0007-4",
                "drug_a": "metformin",
                "drug_b": "furosemide",
                "severity": "moderate",
                "evidence": "reduced renal clearance can increase lactic acidosis risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0007-5",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "CYP3A4 inhibition raises statin concentration"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-V0007-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-V0007-1",
                "replace_drug": "aspirin",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.78,
                "rationale": "reduces interaction burden from aspirin"
            },
            {
                "regimen_id": "REG-SYN-H-V0007-2",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.28,
                "rationale": "modest risk reduction by replacing spironolactone"
            },
            {
                "regimen_id": "REG-SYN-H-V0007-4",
                "replace_drug": "atorvastatin",
                "with_drug": "rosuvastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.41,
                "rationale": "modest risk reduction by replacing atorvastatin"
            }
        ],
        "split": "validation",
        "template_family": "synth-val::hard-SYN-H-V0007"
    },
    {
        "case_id": "SYN-H-V0008",
        "age": 90,
        "labs": {
            "egfr": 39.7,
            "creatinine": 2.0,
            "potassium": 4.8,
            "inr": 2.8,
            "alt": 121.1,
            "ast": 113.8
        },
        "diagnoses": [
            "atrial_fibrillation",
            "chronic_liver_disease",
            "depression"
        ],
        "medications": [
            "clopidogrel",
            "digoxin",
            "diltiazem",
            "furosemide",
            "glipizide",
            "losartan",
            "metformin",
            "metoprolol",
            "omeprazole",
            "prednisone",
            "simvastatin",
            "spironolactone",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-V0008-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-H-V0008-2",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            },
            {
                "interaction_id": "INT-SYN-H-V0008-3",
                "drug_a": "metformin",
                "drug_b": "furosemide",
                "severity": "moderate",
                "evidence": "reduced renal clearance can increase lactic acidosis risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0008-4",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            },
            {
                "interaction_id": "INT-SYN-H-V0008-5",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-V0008-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-V0008-1",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.71,
                "rationale": "reduces interaction burden from omeprazole"
            },
            {
                "regimen_id": "REG-SYN-H-V0008-2",
                "replace_drug": "metoprolol",
                "with_drug": "bisoprolol",
                "target_condition": "rate_control",
                "expected_risk_delta": 0.25,
                "rationale": "modest risk reduction by replacing metoprolol"
            },
            {
                "regimen_id": "REG-SYN-H-V0008-4",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.46,
                "rationale": "modest risk reduction by replacing spironolactone"
            },
            {
                "regimen_id": "REG-SYN-H-V0008-5",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.37,
                "rationale": "modest risk reduction by replacing simvastatin"
            }
        ],
        "split": "validation",
        "template_family": "synth-val::hard-SYN-H-V0008"
    },
    {
        "case_id": "SYN-H-V0009",
        "age": 88,
        "labs": {
            "egfr": 40.4,
            "creatinine": 2.3,
            "potassium": 5.3,
            "inr": 2.9
        },
        "diagnoses": [
            "gout",
            "anxiety",
            "coronary_artery_disease",
            "nonalcoholic_steatohepatitis",
            "peripheral_artery_disease"
        ],
        "medications": [
            "aspirin",
            "citalopram",
            "linezolid",
            "metoprolol",
            "nitroglycerin",
            "prednisone",
            "sertraline",
            "sildenafil",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-V0009-1",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-H-V0009-2",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0009-3",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            },
            {
                "interaction_id": "INT-SYN-H-V0009-4",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-V0009-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-V0009-1",
                "replace_drug": "aspirin",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.69,
                "rationale": "reduces interaction burden from aspirin"
            },
            {
                "regimen_id": "REG-SYN-H-V0009-2",
                "replace_drug": "metoprolol",
                "with_drug": "bisoprolol",
                "target_condition": "rate_control",
                "expected_risk_delta": 0.35,
                "rationale": "modest risk reduction by replacing metoprolol"
            }
        ],
        "split": "validation",
        "template_family": "synth-val::hard-SYN-H-V0009"
    },
    {
        "case_id": "SYN-H-V0010",
        "age": 85,
        "labs": {
            "egfr": 42.7,
            "creatinine": 2.2,
            "potassium": 5.5,
            "inr": 2.0,
            "alt": 177.6,
            "ast": 159.2
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "anemia",
            "osteoarthritis",
            "gout",
            "hypertension"
        ],
        "medications": [
            "azithromycin",
            "ciprofloxacin",
            "diltiazem",
            "ferrous_sulfate",
            "furosemide",
            "isosorbide_mononitrate",
            "losartan",
            "metformin",
            "prednisone",
            "sildenafil",
            "simvastatin",
            "spironolactone",
            "valsartan",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-V0010-1",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-H-V0010-2",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0010-3",
                "drug_a": "metformin",
                "drug_b": "furosemide",
                "severity": "moderate",
                "evidence": "reduced renal clearance can increase lactic acidosis risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0010-4",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            },
            {
                "interaction_id": "INT-SYN-H-V0010-5",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            }
        ],
        "required_regimens": [],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-V0010-1",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.36,
                "rationale": "modest risk reduction by replacing simvastatin"
            },
            {
                "regimen_id": "REG-SYN-H-V0010-3",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.38,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "validation",
        "template_family": "synth-val::hard-SYN-H-V0010"
    },
    {
        "case_id": "SYN-H-V0011",
        "age": 93,
        "labs": {
            "egfr": 43.4,
            "creatinine": 2.1,
            "potassium": 5.5,
            "inr": 2.6,
            "alt": 187.5,
            "ast": 143.2
        },
        "diagnoses": [
            "hypertension",
            "depression",
            "chronic_kidney_disease",
            "osteoarthritis"
        ],
        "medications": [
            "apixaban",
            "aspirin",
            "isosorbide_mononitrate",
            "linezolid",
            "metoprolol",
            "naproxen",
            "sertraline",
            "sildenafil",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-V0011-1",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0011-2",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            },
            {
                "interaction_id": "INT-SYN-H-V0011-3",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0011-4",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-V0011-1",
            "REG-SYN-H-V0011-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-V0011-1",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.75,
                "rationale": "reduces interaction burden from naproxen"
            },
            {
                "regimen_id": "REG-SYN-H-V0011-2",
                "replace_drug": "metoprolol",
                "with_drug": "bisoprolol",
                "target_condition": "rate_control",
                "expected_risk_delta": 0.41,
                "rationale": "modest risk reduction by replacing metoprolol"
            },
            {
                "regimen_id": "REG-SYN-H-V0011-3",
                "replace_drug": "aspirin",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.69,
                "rationale": "reduces interaction burden from aspirin"
            }
        ],
        "split": "validation",
        "template_family": "synth-val::hard-SYN-H-V0011"
    },
    {
        "case_id": "SYN-H-V0012",
        "age": 93,
        "labs": {
            "egfr": 33.6,
            "creatinine": 2.3,
            "potassium": 5.0,
            "inr": 2.4
        },
        "diagnoses": [
            "chronic_liver_disease",
            "heart_failure",
            "anemia"
        ],
        "medications": [
            "apixaban",
            "aspirin",
            "clarithromycin",
            "clopidogrel",
            "lisinopril",
            "losartan",
            "metoprolol",
            "metronidazole",
            "paroxetine",
            "sertraline",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-V0012-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0012-2",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            },
            {
                "interaction_id": "INT-SYN-H-V0012-3",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0012-4",
                "drug_a": "metoprolol",
                "drug_b": "paroxetine",
                "severity": "moderate",
                "evidence": "CYP2D6 inhibition raises metoprolol exposure"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-V0012-1",
            "REG-SYN-H-V0012-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-V0012-1",
                "replace_drug": "aspirin",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.84,
                "rationale": "reduces interaction burden from aspirin"
            },
            {
                "regimen_id": "REG-SYN-H-V0012-2",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.35,
                "rationale": "modest risk reduction by replacing spironolactone"
            },
            {
                "regimen_id": "REG-SYN-H-V0012-3",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.73,
                "rationale": "reduces interaction burden from clarithromycin"
            }
        ],
        "split": "validation",
        "template_family": "synth-val::hard-SYN-H-V0012"
    },
    {
        "case_id": "SYN-H-V0013",
        "age": 87,
        "labs": {
            "egfr": 29.1,
            "creatinine": 1.8,
            "potassium": 5.1,
            "inr": 3.0,
            "alt": 120.9,
            "ast": 124.4
        },
        "diagnoses": [
            "heart_failure",
            "osteoarthritis",
            "gout",
            "dyslipidemia"
        ],
        "medications": [
            "allopurinol",
            "apixaban",
            "aspirin",
            "clarithromycin",
            "digoxin",
            "nitroglycerin",
            "sertraline",
            "sildenafil",
            "spironolactone",
            "trimethoprim_sulfamethoxazole",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-V0013-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0013-2",
                "drug_a": "aspirin",
                "drug_b": "sertraline",
                "severity": "minor",
                "evidence": "increased bleeding tendency, amplified in frailty"
            },
            {
                "interaction_id": "INT-SYN-H-V0013-3",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0013-4",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            },
            {
                "interaction_id": "INT-SYN-H-V0013-5",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-V0013-1",
            "REG-SYN-H-V0013-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-V0013-1",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.72,
                "rationale": "reduces interaction burden from clarithromycin"
            },
            {
                "regimen_id": "REG-SYN-H-V0013-2",
                "replace_drug": "trimethoprim_sulfamethoxazole",
                "with_drug": "cephalexin",
                "target_condition": "infection",
                "expected_risk_delta": 0.84,
                "rationale": "reduces interaction burden from trimethoprim_sulfamethoxazole"
            },
            {
                "regimen_id": "REG-SYN-H-V0013-3",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.34,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "validation",
        "template_family": "synth-val::hard-SYN-H-V0013"
    },
    {
        "case_id": "SYN-H-V0014",
        "age": 92,
        "labs": {
            "egfr": 37.2,
            "creatinine": 2.5,
            "potassium": 4.8,
            "inr": 2.4
        },
        "diagnoses": [
            "atrial_fibrillation",
            "anemia",
            "hypothyroidism"
        ],
        "medications": [
            "allopurinol",
            "azithromycin",
            "calcium_carbonate",
            "citalopram",
            "clopidogrel",
            "fluconazole",
            "levothyroxine",
            "nitroglycerin",
            "sildenafil",
            "ticagrelor",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-V0014-1",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0014-2",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-H-V0014-3",
                "drug_a": "allopurinol",
                "drug_b": "warfarin",
                "severity": "moderate",
                "evidence": "allopurinol may enhance warfarin anticoagulation"
            },
            {
                "interaction_id": "INT-SYN-H-V0014-4",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::hard-SYN-H-V0014"
    },
    {
        "case_id": "SYN-H-V0015",
        "age": 85,
        "labs": {
            "egfr": 41.6,
            "creatinine": 2.3,
            "potassium": 5.0,
            "inr": 2.1,
            "alt": 129.8,
            "ast": 112.0
        },
        "diagnoses": [
            "atrial_fibrillation",
            "coronary_artery_disease",
            "anemia",
            "chronic_kidney_disease",
            "heart_failure"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "atorvastatin",
            "azithromycin",
            "dabigatran",
            "diclofenac",
            "isosorbide_mononitrate",
            "ketoconazole",
            "linezolid",
            "lisinopril",
            "prednisone",
            "sildenafil",
            "simvastatin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-V0015-1",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0015-2",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-H-V0015-3",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-H-V0015-4",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0015-5",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-V0015-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-V0015-1",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.71,
                "rationale": "reduces interaction burden from diclofenac"
            },
            {
                "regimen_id": "REG-SYN-H-V0015-2",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.45,
                "rationale": "modest risk reduction by replacing simvastatin"
            }
        ],
        "split": "validation",
        "template_family": "synth-val::hard-SYN-H-V0015"
    },
    {
        "case_id": "SYN-H-V0016",
        "age": 91,
        "labs": {
            "egfr": 27.3,
            "creatinine": 2.7,
            "potassium": 5.2,
            "inr": 2.7,
            "alt": 192.8,
            "ast": 173.3
        },
        "diagnoses": [
            "hypothyroidism",
            "osteoarthritis",
            "gout",
            "atrial_fibrillation"
        ],
        "medications": [
            "allopurinol",
            "aspirin",
            "azithromycin",
            "citalopram",
            "clopidogrel",
            "diclofenac",
            "glipizide",
            "metronidazole",
            "omeprazole",
            "sertraline",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-V0016-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0016-2",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0016-3",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-H-V0016-4",
                "drug_a": "aspirin",
                "drug_b": "sertraline",
                "severity": "minor",
                "evidence": "increased bleeding tendency, amplified in frailty"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-V0016-1",
            "REG-SYN-H-V0016-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-V0016-1",
                "replace_drug": "metronidazole",
                "with_drug": "doxycycline",
                "target_condition": "infection",
                "expected_risk_delta": 0.89,
                "rationale": "reduces interaction burden from metronidazole"
            },
            {
                "regimen_id": "REG-SYN-H-V0016-2",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.7,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "validation",
        "template_family": "synth-val::hard-SYN-H-V0016"
    },
    {
        "case_id": "SYN-H-V0017",
        "age": 89,
        "labs": {
            "egfr": 42.1,
            "creatinine": 2.3,
            "potassium": 5.3,
            "inr": 2.8
        },
        "diagnoses": [
            "depression",
            "hypothyroidism",
            "coronary_artery_disease"
        ],
        "medications": [
            "azithromycin",
            "clopidogrel",
            "levothyroxine",
            "losartan",
            "metoprolol",
            "nitroglycerin",
            "omeprazole",
            "paroxetine",
            "sildenafil",
            "ticagrelor",
            "valsartan",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-V0017-1",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-H-V0017-2",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-H-V0017-3",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            },
            {
                "interaction_id": "INT-SYN-H-V0017-4",
                "drug_a": "metoprolol",
                "drug_b": "paroxetine",
                "severity": "moderate",
                "evidence": "CYP2D6 inhibition raises metoprolol exposure"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-V0017-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-V0017-1",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.83,
                "rationale": "reduces interaction burden from omeprazole"
            }
        ],
        "split": "validation",
        "template_family": "synth-val::hard-SYN-H-V0017"
    },
    {
        "case_id": "SYN-H-V0018",
        "age": 95,
        "labs": {
            "egfr": 42.2,
            "creatinine": 2.4,
            "potassium": 5.5,
            "inr": 3.1,
            "alt": 179.1,
            "ast": 148.6
        },
        "diagnoses": [
            "hypertension",
            "type_2_diabetes",
            "peripheral_artery_disease",
            "anemia",
            "osteoarthritis"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "calcium_carbonate",
            "cetirizine",
            "ciprofloxacin",
            "fluconazole",
            "glipizide",
            "isosorbide_mononitrate",
            "losartan",
            "metoprolol",
            "nitroglycerin",
            "sildenafil",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-V0018-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0018-2",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-H-V0018-3",
                "drug_a": "glipizide",
                "drug_b": "ciprofloxacin",
                "severity": "moderate",
                "evidence": "dysglycemia risk from fluoroquinolone-sulfonylurea combination"
            },
            {
                "interaction_id": "INT-SYN-H-V0018-4",
                "drug_a": "cetirizine",
                "drug_b": "amlodipine",
                "severity": "minor",
                "evidence": "possible additive sedation in elderly"
            },
            {
                "interaction_id": "INT-SYN-H-V0018-5",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-V0018-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-V0018-1",
                "replace_drug": "fluconazole",
                "with_drug": "micafungin",
                "target_condition": "infection",
                "expected_risk_delta": 0.55,
                "rationale": "reduces interaction burden from fluconazole"
            },
            {
                "regimen_id": "REG-SYN-H-V0018-3",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.43,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "validation",
        "template_family": "synth-val::hard-SYN-H-V0018"
    },
    {
        "case_id": "SYN-H-V0019",
        "age": 87,
        "labs": {
            "egfr": 35.1,
            "creatinine": 2.4,
            "potassium": 5.1,
            "inr": 2.8
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "heart_failure",
            "chronic_kidney_disease",
            "anemia"
        ],
        "medications": [
            "amiodarone",
            "apixaban",
            "ciprofloxacin",
            "citalopram",
            "clarithromycin",
            "digoxin",
            "furosemide",
            "glipizide",
            "losartan",
            "sildenafil",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-V0019-1",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-H-V0019-2",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0019-3",
                "drug_a": "furosemide",
                "drug_b": "warfarin",
                "severity": "minor",
                "evidence": "volume changes may alter INR stability"
            },
            {
                "interaction_id": "INT-SYN-H-V0019-4",
                "drug_a": "glipizide",
                "drug_b": "ciprofloxacin",
                "severity": "moderate",
                "evidence": "dysglycemia risk from fluoroquinolone-sulfonylurea combination"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-V0019-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-V0019-1",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.81,
                "rationale": "reduces interaction burden from clarithromycin"
            }
        ],
        "split": "validation",
        "template_family": "synth-val::hard-SYN-H-V0019"
    },
    {
        "case_id": "SYN-H-V0020",
        "age": 90,
        "labs": {
            "egfr": 30.3,
            "creatinine": 2.0,
            "potassium": 5.0,
            "inr": 2.0,
            "alt": 143.8,
            "ast": 170.9
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "anxiety",
            "chronic_kidney_disease",
            "hypothyroidism",
            "depression"
        ],
        "medications": [
            "ciprofloxacin",
            "dabigatran",
            "diltiazem",
            "ibuprofen",
            "isosorbide_mononitrate",
            "ketoconazole",
            "prednisone",
            "sildenafil",
            "simvastatin",
            "spironolactone",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-V0020-1",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-H-V0020-2",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0020-3",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-H-V0020-4",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-V0020-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-V0020-1",
                "replace_drug": "ibuprofen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.82,
                "rationale": "reduces interaction burden from ibuprofen"
            },
            {
                "regimen_id": "REG-SYN-H-V0020-2",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.49,
                "rationale": "modest risk reduction by replacing simvastatin"
            }
        ],
        "split": "validation",
        "template_family": "synth-val::hard-SYN-H-V0020"
    },
    {
        "case_id": "SYN-H-V0021",
        "age": 86,
        "labs": {
            "egfr": 31.0,
            "creatinine": 2.5,
            "potassium": 5.5,
            "inr": 2.3,
            "alt": 117.6,
            "ast": 105.7
        },
        "diagnoses": [
            "hypothyroidism",
            "anemia",
            "type_2_diabetes"
        ],
        "medications": [
            "amlodipine",
            "aspirin",
            "cetirizine",
            "dabigatran",
            "furosemide",
            "isosorbide_mononitrate",
            "ketoconazole",
            "lisinopril",
            "paroxetine",
            "prednisone",
            "sildenafil",
            "spironolactone",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-V0021-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-H-V0021-2",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0021-3",
                "drug_a": "cetirizine",
                "drug_b": "amlodipine",
                "severity": "minor",
                "evidence": "possible additive sedation in elderly"
            },
            {
                "interaction_id": "INT-SYN-H-V0021-4",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-H-V0021-5",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-V0021-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-V0021-1",
                "replace_drug": "aspirin",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.88,
                "rationale": "reduces interaction burden from aspirin"
            },
            {
                "regimen_id": "REG-SYN-H-V0021-2",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.42,
                "rationale": "modest risk reduction by replacing spironolactone"
            }
        ],
        "split": "validation",
        "template_family": "synth-val::hard-SYN-H-V0021"
    },
    {
        "case_id": "SYN-H-V0022",
        "age": 92,
        "labs": {
            "egfr": 34.9,
            "creatinine": 2.7,
            "potassium": 5.3,
            "inr": 3.2
        },
        "diagnoses": [
            "coronary_artery_disease",
            "nonalcoholic_steatohepatitis",
            "depression"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "calcium_carbonate",
            "cetirizine",
            "fluconazole",
            "isosorbide_mononitrate",
            "levothyroxine",
            "metoprolol",
            "metronidazole",
            "paroxetine",
            "sildenafil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-V0022-1",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-H-V0022-2",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0022-3",
                "drug_a": "metoprolol",
                "drug_b": "paroxetine",
                "severity": "moderate",
                "evidence": "CYP2D6 inhibition raises metoprolol exposure"
            },
            {
                "interaction_id": "INT-SYN-H-V0022-4",
                "drug_a": "cetirizine",
                "drug_b": "amlodipine",
                "severity": "minor",
                "evidence": "possible additive sedation in elderly"
            },
            {
                "interaction_id": "INT-SYN-H-V0022-5",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-V0022-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-V0022-1",
                "replace_drug": "fluconazole",
                "with_drug": "micafungin",
                "target_condition": "infection",
                "expected_risk_delta": 0.64,
                "rationale": "reduces interaction burden from fluconazole"
            }
        ],
        "split": "validation",
        "template_family": "synth-val::hard-SYN-H-V0022"
    },
    {
        "case_id": "SYN-H-V0023",
        "age": 86,
        "labs": {
            "egfr": 39.0,
            "creatinine": 2.3,
            "potassium": 5.4,
            "inr": 2.0,
            "alt": 188.3,
            "ast": 142.6
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "gout",
            "atrial_fibrillation",
            "anxiety"
        ],
        "medications": [
            "atorvastatin",
            "calcium_carbonate",
            "clopidogrel",
            "diltiazem",
            "furosemide",
            "levothyroxine",
            "metformin",
            "metoprolol",
            "omeprazole",
            "ticagrelor"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-V0023-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-H-V0023-2",
                "drug_a": "metformin",
                "drug_b": "furosemide",
                "severity": "moderate",
                "evidence": "reduced renal clearance can increase lactic acidosis risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0023-3",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-H-V0023-4",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "CYP3A4 inhibition raises statin concentration"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-V0023-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-V0023-1",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.84,
                "rationale": "reduces interaction burden from omeprazole"
            },
            {
                "regimen_id": "REG-SYN-H-V0023-3",
                "replace_drug": "atorvastatin",
                "with_drug": "rosuvastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.27,
                "rationale": "modest risk reduction by replacing atorvastatin"
            }
        ],
        "split": "validation",
        "template_family": "synth-val::hard-SYN-H-V0023"
    },
    {
        "case_id": "SYN-H-V0024",
        "age": 95,
        "labs": {
            "egfr": 29.9,
            "creatinine": 2.6,
            "potassium": 5.1,
            "inr": 2.2,
            "alt": 188.6,
            "ast": 171.6
        },
        "diagnoses": [
            "heart_failure",
            "coronary_artery_disease",
            "atrial_fibrillation",
            "chronic_kidney_disease"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "aspirin",
            "ciprofloxacin",
            "clopidogrel",
            "linezolid",
            "lisinopril",
            "omeprazole",
            "sertraline",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-V0024-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-H-V0024-2",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0024-3",
                "drug_a": "amlodipine",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive hypotension in frail adults"
            },
            {
                "interaction_id": "INT-SYN-H-V0024-4",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-V0024-1",
            "REG-SYN-H-V0024-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-V0024-1",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.82,
                "rationale": "reduces interaction burden from omeprazole"
            },
            {
                "regimen_id": "REG-SYN-H-V0024-2",
                "replace_drug": "aspirin",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.74,
                "rationale": "reduces interaction burden from aspirin"
            }
        ],
        "split": "validation",
        "template_family": "synth-val::hard-SYN-H-V0024"
    },
    {
        "case_id": "SYN-H-V0025",
        "age": 92,
        "labs": {
            "egfr": 40.2,
            "creatinine": 2.3,
            "potassium": 5.5,
            "inr": 2.6
        },
        "diagnoses": [
            "hypothyroidism",
            "dyslipidemia",
            "anemia"
        ],
        "medications": [
            "allopurinol",
            "amlodipine",
            "apixaban",
            "ciprofloxacin",
            "clarithromycin",
            "digoxin",
            "diltiazem",
            "metformin",
            "simvastatin",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-V0025-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0025-2",
                "drug_a": "allopurinol",
                "drug_b": "warfarin",
                "severity": "moderate",
                "evidence": "allopurinol may enhance warfarin anticoagulation"
            },
            {
                "interaction_id": "INT-SYN-H-V0025-3",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            },
            {
                "interaction_id": "INT-SYN-H-V0025-4",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-V0025-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-V0025-1",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.87,
                "rationale": "reduces interaction burden from clarithromycin"
            },
            {
                "regimen_id": "REG-SYN-H-V0025-3",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.47,
                "rationale": "modest risk reduction by replacing simvastatin"
            }
        ],
        "split": "validation",
        "template_family": "synth-val::hard-SYN-H-V0025"
    },
    {
        "case_id": "SYN-H-V0026",
        "age": 94,
        "labs": {
            "egfr": 37.2,
            "creatinine": 2.3,
            "potassium": 5.4,
            "inr": 3.1,
            "alt": 124.3,
            "ast": 120.3
        },
        "diagnoses": [
            "coronary_artery_disease",
            "chronic_liver_disease",
            "chronic_kidney_disease",
            "dyslipidemia",
            "gout"
        ],
        "medications": [
            "apixaban",
            "calcium_carbonate",
            "clarithromycin",
            "dabigatran",
            "ibuprofen",
            "isosorbide_mononitrate",
            "lisinopril",
            "omeprazole",
            "sildenafil",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-V0026-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0026-2",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-H-V0026-3",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            },
            {
                "interaction_id": "INT-SYN-H-V0026-4",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-V0026-1",
            "REG-SYN-H-V0026-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-V0026-1",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.8,
                "rationale": "reduces interaction burden from clarithromycin"
            },
            {
                "regimen_id": "REG-SYN-H-V0026-2",
                "replace_drug": "spironolactone",
                "with_drug": "eplerenone",
                "target_condition": "heart_failure",
                "expected_risk_delta": 0.35,
                "rationale": "modest risk reduction by replacing spironolactone"
            },
            {
                "regimen_id": "REG-SYN-H-V0026-3",
                "replace_drug": "ibuprofen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.8,
                "rationale": "reduces interaction burden from ibuprofen"
            }
        ],
        "split": "validation",
        "template_family": "synth-val::hard-SYN-H-V0026"
    },
    {
        "case_id": "SYN-H-V0027",
        "age": 92,
        "labs": {
            "egfr": 33.4,
            "creatinine": 2.4,
            "potassium": 4.9,
            "inr": 2.4,
            "alt": 195.1,
            "ast": 178.3
        },
        "diagnoses": [
            "nonalcoholic_steatohepatitis",
            "hypothyroidism",
            "gout",
            "hypertension",
            "coronary_artery_disease"
        ],
        "medications": [
            "apixaban",
            "diclofenac",
            "ferrous_sulfate",
            "isosorbide_mononitrate",
            "levothyroxine",
            "metoprolol",
            "naproxen",
            "omeprazole",
            "rivaroxaban",
            "ticagrelor",
            "valsartan"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-V0027-1",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-H-V0027-2",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0027-3",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0027-4",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-V0027-1",
            "REG-SYN-H-V0027-2",
            "REG-SYN-H-V0027-3"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-V0027-1",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.75,
                "rationale": "reduces interaction burden from omeprazole"
            },
            {
                "regimen_id": "REG-SYN-H-V0027-2",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.76,
                "rationale": "reduces interaction burden from diclofenac"
            },
            {
                "regimen_id": "REG-SYN-H-V0027-3",
                "replace_drug": "naproxen",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.74,
                "rationale": "reduces interaction burden from naproxen"
            }
        ],
        "split": "validation",
        "template_family": "synth-val::hard-SYN-H-V0027"
    },
    {
        "case_id": "SYN-H-V0028",
        "age": 92,
        "labs": {
            "egfr": 27.0,
            "creatinine": 2.1,
            "potassium": 5.0,
            "inr": 2.7,
            "alt": 123.8,
            "ast": 103.6
        },
        "diagnoses": [
            "gout",
            "depression",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "azithromycin",
            "cetirizine",
            "clarithromycin",
            "dabigatran",
            "diclofenac",
            "isosorbide_mononitrate",
            "ketoconazole",
            "levothyroxine",
            "paroxetine",
            "sertraline",
            "sildenafil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-V0028-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0028-2",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0028-3",
                "drug_a": "cetirizine",
                "drug_b": "amlodipine",
                "severity": "minor",
                "evidence": "possible additive sedation in elderly"
            },
            {
                "interaction_id": "INT-SYN-H-V0028-4",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-H-V0028-5",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-V0028-1",
            "REG-SYN-H-V0028-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-V0028-1",
                "replace_drug": "diclofenac",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.87,
                "rationale": "reduces interaction burden from diclofenac"
            },
            {
                "regimen_id": "REG-SYN-H-V0028-2",
                "replace_drug": "clarithromycin",
                "with_drug": "azithromycin",
                "target_condition": "infection",
                "expected_risk_delta": 0.68,
                "rationale": "reduces interaction burden from clarithromycin"
            }
        ],
        "split": "validation",
        "template_family": "synth-val::hard-SYN-H-V0028"
    },
    {
        "case_id": "SYN-H-V0029",
        "age": 85,
        "labs": {
            "egfr": 37.8,
            "creatinine": 2.6,
            "potassium": 5.3,
            "inr": 2.8
        },
        "diagnoses": [
            "gout",
            "anemia",
            "hypothyroidism",
            "type_2_diabetes"
        ],
        "medications": [
            "amlodipine",
            "atorvastatin",
            "cetirizine",
            "levothyroxine",
            "lisinopril",
            "metoprolol",
            "metronidazole",
            "nitroglycerin",
            "omeprazole",
            "rivaroxaban",
            "sildenafil",
            "ticagrelor",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-V0029-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0029-2",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-H-V0029-3",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-H-V0029-4",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            },
            {
                "interaction_id": "INT-SYN-H-V0029-5",
                "drug_a": "cetirizine",
                "drug_b": "amlodipine",
                "severity": "minor",
                "evidence": "possible additive sedation in elderly"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-V0029-1",
            "REG-SYN-H-V0029-2"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-V0029-1",
                "replace_drug": "metronidazole",
                "with_drug": "doxycycline",
                "target_condition": "infection",
                "expected_risk_delta": 0.66,
                "rationale": "reduces interaction burden from metronidazole"
            },
            {
                "regimen_id": "REG-SYN-H-V0029-2",
                "replace_drug": "omeprazole",
                "with_drug": "pantoprazole",
                "target_condition": "gi_protection",
                "expected_risk_delta": 0.84,
                "rationale": "reduces interaction burden from omeprazole"
            },
            {
                "regimen_id": "REG-SYN-H-V0029-3",
                "replace_drug": "metoprolol",
                "with_drug": "bisoprolol",
                "target_condition": "rate_control",
                "expected_risk_delta": 0.4,
                "rationale": "modest risk reduction by replacing metoprolol"
            }
        ],
        "split": "validation",
        "template_family": "synth-val::hard-SYN-H-V0029"
    },
    {
        "case_id": "SYN-H-V0030",
        "age": 85,
        "labs": {
            "egfr": 42.3,
            "creatinine": 2.4,
            "potassium": 5.3,
            "inr": 2.1
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "coronary_artery_disease",
            "atrial_fibrillation",
            "gout"
        ],
        "medications": [
            "amiodarone",
            "apixaban",
            "aspirin",
            "clarithromycin",
            "digoxin",
            "diltiazem",
            "furosemide",
            "glipizide",
            "metoprolol",
            "rivaroxaban",
            "simvastatin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-H-V0030-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0030-2",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-H-V0030-3",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-H-V0030-4",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            }
        ],
        "required_regimens": [
            "REG-SYN-H-V0030-1"
        ],
        "substitution_options": [
            {
                "regimen_id": "REG-SYN-H-V0030-1",
                "replace_drug": "aspirin",
                "with_drug": "acetaminophen",
                "target_condition": "pain",
                "expected_risk_delta": 0.75,
                "rationale": "reduces interaction burden from aspirin"
            },
            {
                "regimen_id": "REG-SYN-H-V0030-2",
                "replace_drug": "simvastatin",
                "with_drug": "pravastatin",
                "target_condition": "dyslipidemia",
                "expected_risk_delta": 0.44,
                "rationale": "modest risk reduction by replacing simvastatin"
            }
        ],
        "split": "validation",
        "template_family": "synth-val::hard-SYN-H-V0030"
    }
]

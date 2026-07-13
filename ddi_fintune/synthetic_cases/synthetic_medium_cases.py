"""Synthetic DDI cases for the medium task level."""

from typing import Any, Dict, List

Case = Dict[str, Any]

SYNTHETIC_MEDIUM_CASES: List[Case] = [
    {
        "case_id": "SYN-M-0001",
        "age": 81,
        "labs": {
            "egfr": 43.5,
            "creatinine": 1.9,
            "potassium": 5.2,
            "inr": 2.8,
            "alt": 117.3,
            "ast": 112.5
        },
        "diagnoses": [
            "gout",
            "osteoarthritis"
        ],
        "medications": [
            "atorvastatin",
            "digoxin",
            "diltiazem",
            "ibuprofen",
            "ketoconazole",
            "levothyroxine",
            "metoprolol",
            "paroxetine",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0001-1",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0001-2",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "CYP3A4 inhibition raises statin concentration"
            },
            {
                "interaction_id": "INT-SYN-M-0001-3",
                "drug_a": "metoprolol",
                "drug_b": "paroxetine",
                "severity": "moderate",
                "evidence": "CYP2D6 inhibition raises metoprolol exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0001-4",
                "drug_a": "digoxin",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "P-gp inhibition can raise digoxin concentration"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0002",
        "age": 80,
        "labs": {
            "egfr": 72.9,
            "creatinine": 2.1,
            "potassium": 5.0,
            "inr": 1.8
        },
        "diagnoses": [
            "hypertension",
            "gout"
        ],
        "medications": [
            "amiodarone",
            "atorvastatin",
            "ciprofloxacin",
            "clopidogrel",
            "diltiazem",
            "glipizide",
            "naproxen",
            "omeprazole",
            "rivaroxaban",
            "sertraline"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0002-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-M-0002-2",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "CYP3A4 inhibition raises statin concentration"
            },
            {
                "interaction_id": "INT-SYN-M-0002-3",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0002-4",
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
        "case_id": "SYN-M-0003",
        "age": 77,
        "labs": {
            "egfr": 30.3,
            "creatinine": 2.3,
            "potassium": 4.9,
            "inr": 2.6
        },
        "diagnoses": [
            "coronary_artery_disease",
            "depression",
            "dyslipidemia",
            "atrial_fibrillation"
        ],
        "medications": [
            "amiodarone",
            "amlodipine",
            "ciprofloxacin",
            "clopidogrel",
            "dabigatran",
            "ketoconazole",
            "omeprazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0003-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0003-2",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-M-0003-3",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0004",
        "age": 88,
        "labs": {
            "egfr": 33.2,
            "creatinine": 1.1,
            "potassium": 4.9,
            "inr": 2.4,
            "alt": 121.2,
            "ast": 117.2
        },
        "diagnoses": [
            "chronic_pain",
            "anxiety"
        ],
        "medications": [
            "apixaban",
            "dabigatran",
            "diclofenac",
            "ketoconazole",
            "lisinopril",
            "metoprolol",
            "paroxetine"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0004-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0004-2",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0004-3",
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
        "case_id": "SYN-M-0005",
        "age": 77,
        "labs": {
            "egfr": 45.8,
            "creatinine": 1.1,
            "potassium": 4.8,
            "inr": 2.3
        },
        "diagnoses": [
            "type_2_diabetes",
            "hypothyroidism",
            "osteoarthritis",
            "anxiety"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "ciprofloxacin",
            "dabigatran",
            "diclofenac",
            "ferrous_sulfate",
            "ketoconazole",
            "levothyroxine",
            "naproxen"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0005-1",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0005-2",
                "drug_a": "amlodipine",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive hypotension in frail adults"
            },
            {
                "interaction_id": "INT-SYN-M-0005-3",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-M-0005-4",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0006",
        "age": 78,
        "labs": {
            "egfr": 47.1,
            "creatinine": 1.5,
            "potassium": 5.0,
            "inr": 2.3,
            "alt": 114.1,
            "ast": 120.1
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "hypothyroidism",
            "hypertension"
        ],
        "medications": [
            "apixaban",
            "aspirin",
            "azithromycin",
            "citalopram",
            "diclofenac",
            "fluconazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0006-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0006-2",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-M-0006-3",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0007",
        "age": 83,
        "labs": {
            "egfr": 32.8,
            "creatinine": 1.1,
            "potassium": 4.9,
            "inr": 2.9
        },
        "diagnoses": [
            "type_2_diabetes",
            "anxiety",
            "chronic_liver_disease"
        ],
        "medications": [
            "amiodarone",
            "amlodipine",
            "apixaban",
            "ciprofloxacin",
            "dabigatran",
            "digoxin",
            "furosemide",
            "ketoconazole",
            "metronidazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0007-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0007-2",
                "drug_a": "amlodipine",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive hypotension in frail adults"
            },
            {
                "interaction_id": "INT-SYN-M-0007-3",
                "drug_a": "furosemide",
                "drug_b": "warfarin",
                "severity": "minor",
                "evidence": "volume changes may alter INR stability"
            },
            {
                "interaction_id": "INT-SYN-M-0007-4",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0008",
        "age": 90,
        "labs": {
            "egfr": 43.0,
            "creatinine": 2.3,
            "potassium": 5.2,
            "inr": 2.9
        },
        "diagnoses": [
            "hypothyroidism",
            "depression",
            "atrial_fibrillation",
            "coronary_artery_disease"
        ],
        "medications": [
            "amiodarone",
            "calcium_carbonate",
            "ferrous_sulfate",
            "ibuprofen",
            "levothyroxine",
            "omeprazole",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0008-1",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0008-2",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-M-0008-3",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0009",
        "age": 90,
        "labs": {
            "egfr": 89.7,
            "creatinine": 2.2,
            "potassium": 4.8,
            "inr": 2.2,
            "alt": 111.9,
            "ast": 124.0
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "atrial_fibrillation"
        ],
        "medications": [
            "aspirin",
            "lisinopril",
            "metoprolol",
            "metronidazole",
            "naproxen",
            "paroxetine",
            "prednisone",
            "rivaroxaban",
            "sertraline",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0009-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0009-2",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            },
            {
                "interaction_id": "INT-SYN-M-0009-3",
                "drug_a": "metoprolol",
                "drug_b": "paroxetine",
                "severity": "moderate",
                "evidence": "CYP2D6 inhibition raises metoprolol exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0009-4",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0010",
        "age": 80,
        "labs": {
            "egfr": 34.9,
            "creatinine": 2.5,
            "potassium": 5.1,
            "inr": 1.6,
            "alt": 111.9,
            "ast": 118.7
        },
        "diagnoses": [
            "gout",
            "peripheral_artery_disease"
        ],
        "medications": [
            "amlodipine",
            "ciprofloxacin",
            "citalopram",
            "clopidogrel",
            "dabigatran",
            "ibuprofen",
            "ketoconazole",
            "metoprolol",
            "omeprazole",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0010-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0010-2",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0010-3",
                "drug_a": "amlodipine",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive hypotension in frail adults"
            },
            {
                "interaction_id": "INT-SYN-M-0010-4",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0011",
        "age": 80,
        "labs": {
            "egfr": 38.6,
            "creatinine": 2.2,
            "potassium": 5.3,
            "inr": 2.1
        },
        "diagnoses": [
            "chronic_liver_disease",
            "hypothyroidism",
            "atrial_fibrillation",
            "osteoarthritis"
        ],
        "medications": [
            "atorvastatin",
            "dabigatran",
            "diltiazem",
            "ketoconazole",
            "linezolid",
            "sertraline",
            "trimethoprim_sulfamethoxazole"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0011-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0011-2",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-M-0011-3",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "CYP3A4 inhibition raises statin concentration"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0012",
        "age": 86,
        "labs": {
            "egfr": 79.8,
            "creatinine": 1.6,
            "potassium": 5.1,
            "inr": 1.9
        },
        "diagnoses": [
            "heart_failure",
            "hypertension",
            "peripheral_artery_disease"
        ],
        "medications": [
            "aspirin",
            "diclofenac",
            "lisinopril",
            "losartan",
            "naproxen",
            "omeprazole",
            "rivaroxaban",
            "spironolactone",
            "ticagrelor",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0012-1",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-M-0012-2",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            },
            {
                "interaction_id": "INT-SYN-M-0012-3",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0012-4",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0013",
        "age": 89,
        "labs": {
            "egfr": 30.3,
            "creatinine": 1.8,
            "potassium": 5.5,
            "inr": 1.6,
            "alt": 113.2,
            "ast": 117.9
        },
        "diagnoses": [
            "nonalcoholic_steatohepatitis",
            "chronic_pain"
        ],
        "medications": [
            "apixaban",
            "atorvastatin",
            "clarithromycin",
            "dabigatran",
            "diltiazem",
            "isosorbide_mononitrate",
            "ketoconazole",
            "prednisone",
            "sildenafil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0013-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0013-2",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0013-3",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "CYP3A4 inhibition raises statin concentration"
            },
            {
                "interaction_id": "INT-SYN-M-0013-4",
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
        "case_id": "SYN-M-0014",
        "age": 83,
        "labs": {
            "egfr": 33.6,
            "creatinine": 2.5,
            "potassium": 5.2,
            "inr": 2.5
        },
        "diagnoses": [
            "hypothyroidism",
            "dyslipidemia",
            "hypertension"
        ],
        "medications": [
            "apixaban",
            "calcium_carbonate",
            "ciprofloxacin",
            "clopidogrel",
            "diclofenac",
            "digoxin",
            "furosemide",
            "levothyroxine",
            "linezolid",
            "metoprolol",
            "omeprazole"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0014-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-M-0014-2",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0014-3",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-M-0014-4",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0015",
        "age": 75,
        "labs": {
            "egfr": 38.0,
            "creatinine": 1.0,
            "potassium": 5.1,
            "inr": 2.5,
            "alt": 118.1,
            "ast": 103.8
        },
        "diagnoses": [
            "hypertension",
            "hypothyroidism",
            "anemia",
            "osteoarthritis"
        ],
        "medications": [
            "amiodarone",
            "atorvastatin",
            "metformin",
            "nitroglycerin",
            "sildenafil",
            "spironolactone",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0015-1",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-M-0015-2",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0015-3",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0016",
        "age": 77,
        "labs": {
            "egfr": 41.8,
            "creatinine": 1.4,
            "potassium": 4.8,
            "inr": 1.5
        },
        "diagnoses": [
            "hypothyroidism",
            "anemia",
            "nonalcoholic_steatohepatitis",
            "gout"
        ],
        "medications": [
            "ciprofloxacin",
            "dabigatran",
            "ketoconazole",
            "linezolid",
            "lisinopril",
            "sertraline",
            "spironolactone",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0016-1",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-M-0016-2",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0016-3",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0016-4",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0017",
        "age": 88,
        "labs": {
            "egfr": 84.7,
            "creatinine": 1.7,
            "potassium": 4.9,
            "inr": 1.9
        },
        "diagnoses": [
            "gout",
            "chronic_liver_disease",
            "nonalcoholic_steatohepatitis",
            "anxiety"
        ],
        "medications": [
            "apixaban",
            "aspirin",
            "isosorbide_mononitrate",
            "lisinopril",
            "losartan",
            "metformin",
            "naproxen",
            "sildenafil",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0017-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0017-2",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            },
            {
                "interaction_id": "INT-SYN-M-0017-3",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-M-0017-4",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0018",
        "age": 77,
        "labs": {
            "egfr": 45.1,
            "creatinine": 1.3,
            "potassium": 5.3,
            "inr": 2.6,
            "alt": 129.7,
            "ast": 122.3
        },
        "diagnoses": [
            "coronary_artery_disease",
            "type_2_diabetes",
            "osteoarthritis"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "azithromycin",
            "ciprofloxacin",
            "citalopram",
            "dabigatran",
            "diclofenac",
            "furosemide",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0018-1",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0018-2",
                "drug_a": "furosemide",
                "drug_b": "warfarin",
                "severity": "minor",
                "evidence": "volume changes may alter INR stability"
            },
            {
                "interaction_id": "INT-SYN-M-0018-3",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-M-0018-4",
                "drug_a": "amlodipine",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive hypotension in frail adults"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0019",
        "age": 76,
        "labs": {
            "egfr": 85.1,
            "creatinine": 1.6,
            "potassium": 4.8,
            "inr": 2.8
        },
        "diagnoses": [
            "dyslipidemia",
            "chronic_kidney_disease",
            "peripheral_artery_disease"
        ],
        "medications": [
            "azithromycin",
            "calcium_carbonate",
            "citalopram",
            "dabigatran",
            "ferrous_sulfate",
            "furosemide",
            "isosorbide_mononitrate",
            "levothyroxine",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0019-1",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-M-0019-2",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-M-0019-3",
                "drug_a": "furosemide",
                "drug_b": "warfarin",
                "severity": "minor",
                "evidence": "volume changes may alter INR stability"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0020",
        "age": 76,
        "labs": {
            "egfr": 76.6,
            "creatinine": 1.3,
            "potassium": 5.2,
            "inr": 2.6,
            "alt": 112.9,
            "ast": 122.4
        },
        "diagnoses": [
            "gout",
            "anxiety",
            "dyslipidemia",
            "hypothyroidism"
        ],
        "medications": [
            "amiodarone",
            "ciprofloxacin",
            "dabigatran",
            "digoxin",
            "ketoconazole",
            "metronidazole",
            "naproxen",
            "rivaroxaban",
            "spironolactone",
            "valsartan",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0020-1",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0020-2",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            },
            {
                "interaction_id": "INT-SYN-M-0020-3",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            },
            {
                "interaction_id": "INT-SYN-M-0020-4",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0021",
        "age": 82,
        "labs": {
            "egfr": 67.1,
            "creatinine": 1.3,
            "potassium": 4.9,
            "inr": 1.8,
            "alt": 120.7,
            "ast": 123.1
        },
        "diagnoses": [
            "coronary_artery_disease",
            "hypertension",
            "heart_failure",
            "chronic_pain"
        ],
        "medications": [
            "calcium_carbonate",
            "digoxin",
            "isosorbide_mononitrate",
            "levothyroxine",
            "naproxen",
            "nitroglycerin",
            "sildenafil",
            "ticagrelor",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0021-1",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-M-0021-2",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-M-0021-3",
                "drug_a": "digoxin",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "P-gp inhibition can raise digoxin concentration"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0022",
        "age": 78,
        "labs": {
            "egfr": 79.5,
            "creatinine": 1.2,
            "potassium": 5.4,
            "inr": 2.3
        },
        "diagnoses": [
            "atrial_fibrillation",
            "chronic_liver_disease",
            "chronic_kidney_disease"
        ],
        "medications": [
            "apixaban",
            "fluconazole",
            "ibuprofen",
            "linezolid",
            "naproxen",
            "sertraline",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0022-1",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-M-0022-2",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0022-3",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0023",
        "age": 77,
        "labs": {
            "egfr": 43.1,
            "creatinine": 1.6,
            "potassium": 4.6,
            "inr": 1.6,
            "alt": 113.2,
            "ast": 122.0
        },
        "diagnoses": [
            "coronary_artery_disease",
            "hypertension"
        ],
        "medications": [
            "aspirin",
            "atorvastatin",
            "citalopram",
            "linezolid",
            "omeprazole",
            "sertraline",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0023-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0023-2",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-M-0023-3",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0024",
        "age": 86,
        "labs": {
            "egfr": 47.8,
            "creatinine": 2.0,
            "potassium": 5.2,
            "inr": 2.0,
            "alt": 126.3,
            "ast": 107.2
        },
        "diagnoses": [
            "osteoarthritis",
            "atrial_fibrillation",
            "dyslipidemia",
            "chronic_kidney_disease"
        ],
        "medications": [
            "aspirin",
            "calcium_carbonate",
            "dabigatran",
            "ferrous_sulfate",
            "furosemide",
            "isosorbide_mononitrate",
            "ketoconazole",
            "levothyroxine",
            "omeprazole",
            "sertraline",
            "sildenafil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0024-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0024-2",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-M-0024-3",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-M-0024-4",
                "drug_a": "aspirin",
                "drug_b": "sertraline",
                "severity": "minor",
                "evidence": "increased bleeding tendency, amplified in frailty"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0025",
        "age": 79,
        "labs": {
            "egfr": 45.7,
            "creatinine": 2.3,
            "potassium": 4.8,
            "inr": 1.7,
            "alt": 110.8,
            "ast": 114.7
        },
        "diagnoses": [
            "atrial_fibrillation",
            "type_2_diabetes",
            "osteoarthritis",
            "coronary_artery_disease"
        ],
        "medications": [
            "apixaban",
            "dabigatran",
            "ferrous_sulfate",
            "ketoconazole",
            "lisinopril",
            "naproxen",
            "prednisone",
            "spironolactone",
            "trimethoprim_sulfamethoxazole",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0025-1",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0025-2",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0025-3",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0025-4",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0026",
        "age": 79,
        "labs": {
            "egfr": 34.7,
            "creatinine": 1.4,
            "potassium": 5.1,
            "inr": 1.5,
            "alt": 128.5,
            "ast": 114.3
        },
        "diagnoses": [
            "nonalcoholic_steatohepatitis",
            "depression",
            "peripheral_artery_disease"
        ],
        "medications": [
            "amiodarone",
            "ciprofloxacin",
            "citalopram",
            "ferrous_sulfate",
            "levothyroxine",
            "naproxen",
            "omeprazole",
            "rivaroxaban",
            "simvastatin",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0026-1",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0026-2",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            },
            {
                "interaction_id": "INT-SYN-M-0026-3",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-M-0026-4",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0027",
        "age": 82,
        "labs": {
            "egfr": 61.9,
            "creatinine": 1.9,
            "potassium": 4.9,
            "inr": 1.6,
            "alt": 110.2,
            "ast": 114.0
        },
        "diagnoses": [
            "chronic_pain",
            "osteoarthritis",
            "atrial_fibrillation",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "apixaban",
            "diclofenac",
            "digoxin",
            "ibuprofen",
            "nitroglycerin",
            "sildenafil",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0027-1",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0027-2",
                "drug_a": "digoxin",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "P-gp inhibition can raise digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-M-0027-3",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0028",
        "age": 93,
        "labs": {
            "egfr": 27.4,
            "creatinine": 1.1,
            "potassium": 5.0,
            "inr": 1.6
        },
        "diagnoses": [
            "osteoarthritis",
            "hypothyroidism",
            "dyslipidemia",
            "chronic_pain"
        ],
        "medications": [
            "amlodipine",
            "atorvastatin",
            "cetirizine",
            "linezolid",
            "metronidazole",
            "sertraline",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0028-1",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-M-0028-2",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0028-3",
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
        "case_id": "SYN-M-0029",
        "age": 87,
        "labs": {
            "egfr": 69.0,
            "creatinine": 2.1,
            "potassium": 4.6,
            "inr": 2.1,
            "alt": 129.4,
            "ast": 106.3
        },
        "diagnoses": [
            "dyslipidemia",
            "osteoarthritis"
        ],
        "medications": [
            "aspirin",
            "atorvastatin",
            "diltiazem",
            "fluconazole",
            "lisinopril",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0029-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0029-2",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            },
            {
                "interaction_id": "INT-SYN-M-0029-3",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "CYP3A4 inhibition raises statin concentration"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0030",
        "age": 85,
        "labs": {
            "egfr": 25.1,
            "creatinine": 1.4,
            "potassium": 5.0,
            "inr": 2.6,
            "alt": 128.1,
            "ast": 113.4
        },
        "diagnoses": [
            "heart_failure",
            "anxiety"
        ],
        "medications": [
            "clopidogrel",
            "diclofenac",
            "lisinopril",
            "metformin",
            "omeprazole",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0030-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0030-2",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            },
            {
                "interaction_id": "INT-SYN-M-0030-3",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0031",
        "age": 92,
        "labs": {
            "egfr": 33.3,
            "creatinine": 2.4,
            "potassium": 5.0,
            "inr": 1.9
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "heart_failure",
            "osteoarthritis",
            "depression"
        ],
        "medications": [
            "allopurinol",
            "digoxin",
            "linezolid",
            "naproxen",
            "rivaroxaban",
            "sertraline",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0031-1",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-M-0031-2",
                "drug_a": "allopurinol",
                "drug_b": "warfarin",
                "severity": "moderate",
                "evidence": "allopurinol may enhance warfarin anticoagulation"
            },
            {
                "interaction_id": "INT-SYN-M-0031-3",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0032",
        "age": 94,
        "labs": {
            "egfr": 77.0,
            "creatinine": 2.2,
            "potassium": 4.8,
            "inr": 2.9,
            "alt": 118.5,
            "ast": 114.7
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "dabigatran",
            "ferrous_sulfate",
            "furosemide",
            "ketoconazole",
            "levothyroxine",
            "naproxen",
            "rivaroxaban",
            "sertraline"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0032-1",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0032-2",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-M-0032-3",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0033",
        "age": 77,
        "labs": {
            "egfr": 79.5,
            "creatinine": 1.7,
            "potassium": 5.1,
            "inr": 2.8,
            "alt": 122.8,
            "ast": 102.1
        },
        "diagnoses": [
            "atrial_fibrillation",
            "depression",
            "osteoarthritis"
        ],
        "medications": [
            "ciprofloxacin",
            "fluconazole",
            "furosemide",
            "isosorbide_mononitrate",
            "levothyroxine",
            "metformin",
            "nitroglycerin",
            "sildenafil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0033-1",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-M-0033-2",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0033-3",
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
        "case_id": "SYN-M-0034",
        "age": 93,
        "labs": {
            "egfr": 48.0,
            "creatinine": 2.3,
            "potassium": 4.5,
            "inr": 2.2,
            "alt": 123.2,
            "ast": 112.1
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "chronic_pain",
            "dyslipidemia",
            "depression"
        ],
        "medications": [
            "amiodarone",
            "calcium_carbonate",
            "metoprolol",
            "omeprazole",
            "ticagrelor",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0034-1",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-M-0034-2",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0034-3",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0035",
        "age": 94,
        "labs": {
            "egfr": 42.8,
            "creatinine": 1.4,
            "potassium": 5.2,
            "inr": 3.0
        },
        "diagnoses": [
            "atrial_fibrillation",
            "anemia"
        ],
        "medications": [
            "apixaban",
            "ciprofloxacin",
            "citalopram",
            "clarithromycin",
            "clopidogrel",
            "furosemide",
            "glipizide",
            "omeprazole",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0035-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-M-0035-2",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0035-3",
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
        "case_id": "SYN-M-0036",
        "age": 79,
        "labs": {
            "egfr": 81.3,
            "creatinine": 1.1,
            "potassium": 5.3,
            "inr": 2.9,
            "alt": 124.0,
            "ast": 105.7
        },
        "diagnoses": [
            "hypothyroidism",
            "gout"
        ],
        "medications": [
            "allopurinol",
            "amiodarone",
            "azithromycin",
            "citalopram",
            "diltiazem",
            "omeprazole",
            "simvastatin",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0036-1",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-M-0036-2",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-M-0036-3",
                "drug_a": "allopurinol",
                "drug_b": "warfarin",
                "severity": "moderate",
                "evidence": "allopurinol may enhance warfarin anticoagulation"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0037",
        "age": 90,
        "labs": {
            "egfr": 44.7,
            "creatinine": 1.3,
            "potassium": 4.6,
            "inr": 2.4,
            "alt": 116.7,
            "ast": 102.0
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "anxiety",
            "peripheral_artery_disease"
        ],
        "medications": [
            "clopidogrel",
            "ferrous_sulfate",
            "furosemide",
            "levothyroxine",
            "linezolid",
            "metformin",
            "metronidazole",
            "sertraline",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0037-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0037-2",
                "drug_a": "metformin",
                "drug_b": "furosemide",
                "severity": "moderate",
                "evidence": "reduced renal clearance can increase lactic acidosis risk"
            },
            {
                "interaction_id": "INT-SYN-M-0037-3",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-M-0037-4",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0038",
        "age": 75,
        "labs": {
            "egfr": 42.4,
            "creatinine": 2.3,
            "potassium": 4.7,
            "inr": 2.0,
            "alt": 123.3,
            "ast": 120.7
        },
        "diagnoses": [
            "anxiety",
            "nonalcoholic_steatohepatitis",
            "anemia"
        ],
        "medications": [
            "amiodarone",
            "calcium_carbonate",
            "citalopram",
            "digoxin",
            "metronidazole",
            "spironolactone",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0038-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0038-2",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-M-0038-3",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0039",
        "age": 75,
        "labs": {
            "egfr": 42.4,
            "creatinine": 1.7,
            "potassium": 5.0,
            "inr": 1.5,
            "alt": 114.3,
            "ast": 109.5
        },
        "diagnoses": [
            "type_2_diabetes",
            "osteoarthritis"
        ],
        "medications": [
            "amiodarone",
            "apixaban",
            "ciprofloxacin",
            "citalopram",
            "digoxin",
            "glipizide",
            "ibuprofen",
            "metoprolol",
            "naproxen",
            "rivaroxaban",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0039-1",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0039-2",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            },
            {
                "interaction_id": "INT-SYN-M-0039-3",
                "drug_a": "glipizide",
                "drug_b": "ciprofloxacin",
                "severity": "moderate",
                "evidence": "dysglycemia risk from fluoroquinolone-sulfonylurea combination"
            },
            {
                "interaction_id": "INT-SYN-M-0039-4",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0040",
        "age": 92,
        "labs": {
            "egfr": 42.7,
            "creatinine": 1.9,
            "potassium": 5.3,
            "inr": 1.8
        },
        "diagnoses": [
            "chronic_pain",
            "heart_failure"
        ],
        "medications": [
            "aspirin",
            "azithromycin",
            "ciprofloxacin",
            "citalopram",
            "diltiazem",
            "ferrous_sulfate",
            "levothyroxine",
            "omeprazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0040-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0040-2",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-M-0040-3",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0041",
        "age": 89,
        "labs": {
            "egfr": 42.5,
            "creatinine": 1.9,
            "potassium": 5.3,
            "inr": 1.8
        },
        "diagnoses": [
            "nonalcoholic_steatohepatitis",
            "gout",
            "type_2_diabetes",
            "anxiety"
        ],
        "medications": [
            "aspirin",
            "azithromycin",
            "citalopram",
            "dabigatran",
            "ketoconazole",
            "nitroglycerin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0041-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0041-2",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-M-0041-3",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0042",
        "age": 75,
        "labs": {
            "egfr": 34.5,
            "creatinine": 1.8,
            "potassium": 5.3,
            "inr": 2.8,
            "alt": 117.3,
            "ast": 113.9
        },
        "diagnoses": [
            "nonalcoholic_steatohepatitis",
            "osteoarthritis",
            "chronic_kidney_disease",
            "anxiety"
        ],
        "medications": [
            "allopurinol",
            "atorvastatin",
            "azithromycin",
            "citalopram",
            "diltiazem",
            "glipizide",
            "ibuprofen",
            "losartan",
            "spironolactone",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0042-1",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-M-0042-2",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0042-3",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "CYP3A4 inhibition raises statin concentration"
            },
            {
                "interaction_id": "INT-SYN-M-0042-4",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0043",
        "age": 87,
        "labs": {
            "egfr": 41.9,
            "creatinine": 1.4,
            "potassium": 4.9,
            "inr": 2.9,
            "alt": 123.3,
            "ast": 109.1
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "chronic_kidney_disease"
        ],
        "medications": [
            "apixaban",
            "clopidogrel",
            "furosemide",
            "linezolid",
            "metformin",
            "omeprazole",
            "sertraline"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0043-1",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-M-0043-2",
                "drug_a": "metformin",
                "drug_b": "furosemide",
                "severity": "moderate",
                "evidence": "reduced renal clearance can increase lactic acidosis risk"
            },
            {
                "interaction_id": "INT-SYN-M-0043-3",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0044",
        "age": 88,
        "labs": {
            "egfr": 45.5,
            "creatinine": 2.2,
            "potassium": 5.4,
            "inr": 1.6,
            "alt": 115.0,
            "ast": 122.4
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "heart_failure"
        ],
        "medications": [
            "azithromycin",
            "calcium_carbonate",
            "ciprofloxacin",
            "citalopram",
            "clopidogrel",
            "levothyroxine",
            "metronidazole",
            "prednisone",
            "spironolactone",
            "valsartan",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0044-1",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-M-0044-2",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-M-0044-3",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            },
            {
                "interaction_id": "INT-SYN-M-0044-4",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0045",
        "age": 80,
        "labs": {
            "egfr": 25.5,
            "creatinine": 1.1,
            "potassium": 5.5,
            "inr": 1.6
        },
        "diagnoses": [
            "nonalcoholic_steatohepatitis",
            "type_2_diabetes",
            "anxiety"
        ],
        "medications": [
            "apixaban",
            "atorvastatin",
            "azithromycin",
            "fluconazole",
            "naproxen",
            "prednisone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0045-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0045-2",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            },
            {
                "interaction_id": "INT-SYN-M-0045-3",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0046",
        "age": 75,
        "labs": {
            "egfr": 39.5,
            "creatinine": 1.5,
            "potassium": 4.5,
            "inr": 2.5,
            "alt": 126.1,
            "ast": 120.7
        },
        "diagnoses": [
            "chronic_pain",
            "chronic_kidney_disease",
            "hypothyroidism",
            "osteoarthritis"
        ],
        "medications": [
            "apixaban",
            "aspirin",
            "clarithromycin",
            "linezolid",
            "metronidazole",
            "sertraline",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0046-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0046-2",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0046-3",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0047",
        "age": 78,
        "labs": {
            "egfr": 37.6,
            "creatinine": 1.6,
            "potassium": 5.4,
            "inr": 1.8
        },
        "diagnoses": [
            "anemia",
            "coronary_artery_disease",
            "hypertension",
            "type_2_diabetes"
        ],
        "medications": [
            "amiodarone",
            "dabigatran",
            "digoxin",
            "diltiazem",
            "furosemide",
            "metoprolol",
            "metronidazole",
            "naproxen",
            "rivaroxaban",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0047-1",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0047-2",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0047-3",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-M-0047-4",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0048",
        "age": 92,
        "labs": {
            "egfr": 45.9,
            "creatinine": 1.1,
            "potassium": 5.2,
            "inr": 3.0
        },
        "diagnoses": [
            "depression",
            "anemia",
            "chronic_kidney_disease"
        ],
        "medications": [
            "azithromycin",
            "clopidogrel",
            "diclofenac",
            "isosorbide_mononitrate",
            "ketoconazole",
            "linezolid",
            "prednisone",
            "sertraline",
            "sildenafil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0048-1",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-M-0048-2",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            },
            {
                "interaction_id": "INT-SYN-M-0048-3",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-M-0048-4",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0049",
        "age": 92,
        "labs": {
            "egfr": 33.4,
            "creatinine": 2.2,
            "potassium": 5.1,
            "inr": 2.8
        },
        "diagnoses": [
            "anemia",
            "coronary_artery_disease",
            "chronic_pain",
            "hypothyroidism"
        ],
        "medications": [
            "amiodarone",
            "amlodipine",
            "azithromycin",
            "cetirizine",
            "citalopram",
            "metoprolol",
            "paroxetine",
            "simvastatin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0049-1",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0049-2",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-M-0049-3",
                "drug_a": "metoprolol",
                "drug_b": "paroxetine",
                "severity": "moderate",
                "evidence": "CYP2D6 inhibition raises metoprolol exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0049-4",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0050",
        "age": 88,
        "labs": {
            "egfr": 28.0,
            "creatinine": 1.1,
            "potassium": 4.7,
            "inr": 2.8
        },
        "diagnoses": [
            "depression",
            "peripheral_artery_disease"
        ],
        "medications": [
            "apixaban",
            "azithromycin",
            "citalopram",
            "furosemide",
            "linezolid",
            "metoprolol",
            "naproxen",
            "sertraline",
            "valsartan"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0050-1",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0050-2",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-M-0050-3",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-M-0050-4",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0051",
        "age": 76,
        "labs": {
            "egfr": 25.6,
            "creatinine": 1.4,
            "potassium": 5.0,
            "inr": 1.6
        },
        "diagnoses": [
            "depression",
            "coronary_artery_disease"
        ],
        "medications": [
            "calcium_carbonate",
            "diltiazem",
            "fluconazole",
            "furosemide",
            "levothyroxine",
            "metoprolol",
            "paroxetine",
            "simvastatin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0051-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0051-2",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-M-0051-3",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-M-0051-4",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0052",
        "age": 92,
        "labs": {
            "egfr": 44.2,
            "creatinine": 2.2,
            "potassium": 5.1,
            "inr": 2.5,
            "alt": 126.3,
            "ast": 110.9
        },
        "diagnoses": [
            "hypothyroidism",
            "hypertension"
        ],
        "medications": [
            "apixaban",
            "citalopram",
            "diclofenac",
            "digoxin",
            "ibuprofen",
            "omeprazole",
            "ticagrelor",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0052-1",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0052-2",
                "drug_a": "digoxin",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "P-gp inhibition can raise digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-M-0052-3",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0052-4",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0053",
        "age": 84,
        "labs": {
            "egfr": 42.4,
            "creatinine": 1.8,
            "potassium": 5.0,
            "inr": 2.3,
            "alt": 124.5,
            "ast": 103.7
        },
        "diagnoses": [
            "anxiety",
            "atrial_fibrillation",
            "heart_failure"
        ],
        "medications": [
            "azithromycin",
            "ciprofloxacin",
            "citalopram",
            "clopidogrel",
            "ferrous_sulfate",
            "metoprolol",
            "omeprazole",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0053-1",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-M-0053-2",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            },
            {
                "interaction_id": "INT-SYN-M-0053-3",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0054",
        "age": 89,
        "labs": {
            "egfr": 33.8,
            "creatinine": 1.8,
            "potassium": 4.6,
            "inr": 1.8
        },
        "diagnoses": [
            "osteoarthritis",
            "atrial_fibrillation",
            "hypothyroidism",
            "anxiety"
        ],
        "medications": [
            "apixaban",
            "calcium_carbonate",
            "clarithromycin",
            "ferrous_sulfate",
            "levothyroxine",
            "metoprolol",
            "metronidazole",
            "valsartan",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0054-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0054-2",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            },
            {
                "interaction_id": "INT-SYN-M-0054-3",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-M-0054-4",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0055",
        "age": 75,
        "labs": {
            "egfr": 43.6,
            "creatinine": 1.4,
            "potassium": 5.0,
            "inr": 2.3
        },
        "diagnoses": [
            "osteoarthritis",
            "coronary_artery_disease",
            "nonalcoholic_steatohepatitis",
            "hypertension"
        ],
        "medications": [
            "ciprofloxacin",
            "furosemide",
            "isosorbide_mononitrate",
            "levothyroxine",
            "sildenafil",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0055-1",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-M-0055-2",
                "drug_a": "furosemide",
                "drug_b": "warfarin",
                "severity": "minor",
                "evidence": "volume changes may alter INR stability"
            },
            {
                "interaction_id": "INT-SYN-M-0055-3",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0056",
        "age": 86,
        "labs": {
            "egfr": 74.1,
            "creatinine": 1.5,
            "potassium": 4.6,
            "inr": 2.4
        },
        "diagnoses": [
            "chronic_liver_disease",
            "type_2_diabetes",
            "osteoarthritis"
        ],
        "medications": [
            "apixaban",
            "dabigatran",
            "digoxin",
            "isosorbide_mononitrate",
            "ketoconazole",
            "naproxen",
            "prednisone",
            "sildenafil",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0056-1",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0056-2",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0056-3",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-M-0056-4",
                "drug_a": "digoxin",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "P-gp inhibition can raise digoxin concentration"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0057",
        "age": 91,
        "labs": {
            "egfr": 33.6,
            "creatinine": 1.3,
            "potassium": 4.8,
            "inr": 2.2
        },
        "diagnoses": [
            "gout",
            "dyslipidemia",
            "anemia",
            "anxiety"
        ],
        "medications": [
            "apixaban",
            "aspirin",
            "clarithromycin",
            "dabigatran",
            "ketoconazole",
            "metformin",
            "nitroglycerin",
            "sildenafil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0057-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0057-2",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0057-3",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0058",
        "age": 89,
        "labs": {
            "egfr": 47.3,
            "creatinine": 2.2,
            "potassium": 4.5,
            "inr": 2.8,
            "alt": 121.6,
            "ast": 115.2
        },
        "diagnoses": [
            "osteoarthritis",
            "peripheral_artery_disease",
            "gout",
            "hypertension"
        ],
        "medications": [
            "apixaban",
            "aspirin",
            "ciprofloxacin",
            "fluconazole",
            "lisinopril",
            "naproxen",
            "omeprazole",
            "ticagrelor",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0058-1",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0058-2",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            },
            {
                "interaction_id": "INT-SYN-M-0058-3",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0058-4",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0059",
        "age": 95,
        "labs": {
            "egfr": 84.1,
            "creatinine": 2.2,
            "potassium": 4.6,
            "inr": 2.0
        },
        "diagnoses": [
            "nonalcoholic_steatohepatitis",
            "heart_failure"
        ],
        "medications": [
            "apixaban",
            "ciprofloxacin",
            "glipizide",
            "levothyroxine",
            "linezolid",
            "naproxen",
            "sertraline",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0059-1",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-M-0059-2",
                "drug_a": "glipizide",
                "drug_b": "ciprofloxacin",
                "severity": "moderate",
                "evidence": "dysglycemia risk from fluoroquinolone-sulfonylurea combination"
            },
            {
                "interaction_id": "INT-SYN-M-0059-3",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0060",
        "age": 87,
        "labs": {
            "egfr": 64.1,
            "creatinine": 2.5,
            "potassium": 4.8,
            "inr": 2.1,
            "alt": 128.6,
            "ast": 119.2
        },
        "diagnoses": [
            "hypothyroidism",
            "chronic_kidney_disease",
            "coronary_artery_disease",
            "hypertension"
        ],
        "medications": [
            "aspirin",
            "linezolid",
            "losartan",
            "sertraline",
            "spironolactone",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0060-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0060-2",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            },
            {
                "interaction_id": "INT-SYN-M-0060-3",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0061",
        "age": 75,
        "labs": {
            "egfr": 31.4,
            "creatinine": 1.2,
            "potassium": 5.2,
            "inr": 2.1
        },
        "diagnoses": [
            "hypothyroidism",
            "dyslipidemia"
        ],
        "medications": [
            "apixaban",
            "atorvastatin",
            "clopidogrel",
            "diclofenac",
            "ferrous_sulfate",
            "ibuprofen",
            "levothyroxine",
            "omeprazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0061-1",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0061-2",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0061-3",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0062",
        "age": 88,
        "labs": {
            "egfr": 44.9,
            "creatinine": 2.3,
            "potassium": 4.6,
            "inr": 1.7,
            "alt": 126.1,
            "ast": 112.8
        },
        "diagnoses": [
            "gout",
            "chronic_kidney_disease"
        ],
        "medications": [
            "allopurinol",
            "azithromycin",
            "digoxin",
            "metoprolol",
            "nitroglycerin",
            "sildenafil",
            "trimethoprim_sulfamethoxazole",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0062-1",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0062-2",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-M-0062-3",
                "drug_a": "digoxin",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "P-gp inhibition can raise digoxin concentration"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0063",
        "age": 88,
        "labs": {
            "egfr": 78.3,
            "creatinine": 2.4,
            "potassium": 5.0,
            "inr": 2.8,
            "alt": 127.9,
            "ast": 121.1
        },
        "diagnoses": [
            "atrial_fibrillation",
            "depression"
        ],
        "medications": [
            "glipizide",
            "metoprolol",
            "naproxen",
            "nitroglycerin",
            "omeprazole",
            "paroxetine",
            "rivaroxaban",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0063-1",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0063-2",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0063-3",
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
        "case_id": "SYN-M-0064",
        "age": 85,
        "labs": {
            "egfr": 31.6,
            "creatinine": 1.5,
            "potassium": 4.7,
            "inr": 1.8
        },
        "diagnoses": [
            "chronic_liver_disease",
            "nonalcoholic_steatohepatitis",
            "coronary_artery_disease",
            "atrial_fibrillation"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "atorvastatin",
            "clarithromycin",
            "diclofenac",
            "diltiazem",
            "furosemide",
            "lisinopril",
            "simvastatin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0064-1",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0064-2",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-M-0064-3",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "CYP3A4 inhibition raises statin concentration"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0065",
        "age": 77,
        "labs": {
            "egfr": 26.3,
            "creatinine": 2.1,
            "potassium": 5.3,
            "inr": 2.7,
            "alt": 124.1,
            "ast": 110.3
        },
        "diagnoses": [
            "chronic_liver_disease",
            "chronic_kidney_disease",
            "nonalcoholic_steatohepatitis",
            "hypertension"
        ],
        "medications": [
            "amiodarone",
            "apixaban",
            "clopidogrel",
            "diclofenac",
            "omeprazole",
            "simvastatin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0065-1",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0065-2",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-M-0065-3",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0066",
        "age": 89,
        "labs": {
            "egfr": 47.7,
            "creatinine": 2.1,
            "potassium": 5.1,
            "inr": 1.7
        },
        "diagnoses": [
            "anxiety",
            "atrial_fibrillation",
            "chronic_pain"
        ],
        "medications": [
            "apixaban",
            "aspirin",
            "clarithromycin",
            "clopidogrel",
            "linezolid",
            "sertraline",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0066-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0066-2",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0066-3",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0067",
        "age": 83,
        "labs": {
            "egfr": 28.5,
            "creatinine": 2.3,
            "potassium": 5.2,
            "inr": 2.2,
            "alt": 117.5,
            "ast": 124.8
        },
        "diagnoses": [
            "gout",
            "anemia"
        ],
        "medications": [
            "allopurinol",
            "apixaban",
            "diltiazem",
            "isosorbide_mononitrate",
            "levothyroxine",
            "naproxen",
            "nitroglycerin",
            "sildenafil",
            "simvastatin",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0067-1",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0067-2",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-M-0067-3",
                "drug_a": "allopurinol",
                "drug_b": "warfarin",
                "severity": "moderate",
                "evidence": "allopurinol may enhance warfarin anticoagulation"
            },
            {
                "interaction_id": "INT-SYN-M-0067-4",
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
        "case_id": "SYN-M-0068",
        "age": 77,
        "labs": {
            "egfr": 43.9,
            "creatinine": 1.8,
            "potassium": 4.9,
            "inr": 2.6
        },
        "diagnoses": [
            "type_2_diabetes",
            "dyslipidemia",
            "nonalcoholic_steatohepatitis",
            "coronary_artery_disease"
        ],
        "medications": [
            "amlodipine",
            "ciprofloxacin",
            "ferrous_sulfate",
            "levothyroxine",
            "omeprazole",
            "prednisone",
            "simvastatin",
            "trimethoprim_sulfamethoxazole",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0068-1",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0068-2",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-M-0068-3",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-M-0068-4",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0069",
        "age": 84,
        "labs": {
            "egfr": 74.4,
            "creatinine": 1.4,
            "potassium": 4.8,
            "inr": 2.6,
            "alt": 118.6,
            "ast": 122.0
        },
        "diagnoses": [
            "gout",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "aspirin",
            "cetirizine",
            "clarithromycin",
            "clopidogrel",
            "ferrous_sulfate",
            "omeprazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0069-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-M-0069-2",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0069-3",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0069-4",
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
        "case_id": "SYN-M-0070",
        "age": 89,
        "labs": {
            "egfr": 27.1,
            "creatinine": 1.9,
            "potassium": 5.2,
            "inr": 2.8
        },
        "diagnoses": [
            "nonalcoholic_steatohepatitis",
            "osteoarthritis",
            "heart_failure"
        ],
        "medications": [
            "aspirin",
            "azithromycin",
            "citalopram",
            "digoxin",
            "losartan",
            "nitroglycerin",
            "sertraline",
            "sildenafil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0070-1",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-M-0070-2",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-M-0070-3",
                "drug_a": "aspirin",
                "drug_b": "sertraline",
                "severity": "minor",
                "evidence": "increased bleeding tendency, amplified in frailty"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0071",
        "age": 80,
        "labs": {
            "egfr": 26.8,
            "creatinine": 2.1,
            "potassium": 5.2,
            "inr": 1.8
        },
        "diagnoses": [
            "atrial_fibrillation",
            "type_2_diabetes"
        ],
        "medications": [
            "apixaban",
            "glipizide",
            "lisinopril",
            "metoprolol",
            "naproxen",
            "omeprazole",
            "spironolactone",
            "ticagrelor"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0071-1",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-M-0071-2",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            },
            {
                "interaction_id": "INT-SYN-M-0071-3",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0072",
        "age": 75,
        "labs": {
            "egfr": 70.5,
            "creatinine": 1.1,
            "potassium": 4.7,
            "inr": 1.5,
            "alt": 112.5,
            "ast": 116.4
        },
        "diagnoses": [
            "type_2_diabetes",
            "dyslipidemia",
            "chronic_pain"
        ],
        "medications": [
            "apixaban",
            "clarithromycin",
            "dabigatran",
            "diclofenac",
            "ferrous_sulfate",
            "ketoconazole",
            "levothyroxine",
            "nitroglycerin",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0072-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0072-2",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0072-3",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0072-4",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0073",
        "age": 88,
        "labs": {
            "egfr": 45.4,
            "creatinine": 1.3,
            "potassium": 5.4,
            "inr": 1.7,
            "alt": 129.9,
            "ast": 124.3
        },
        "diagnoses": [
            "osteoarthritis",
            "type_2_diabetes",
            "nonalcoholic_steatohepatitis",
            "peripheral_artery_disease"
        ],
        "medications": [
            "apixaban",
            "aspirin",
            "clarithromycin",
            "fluconazole",
            "ibuprofen",
            "metoprolol",
            "naproxen",
            "paroxetine",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0073-1",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0073-2",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0073-3",
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
        "case_id": "SYN-M-0074",
        "age": 89,
        "labs": {
            "egfr": 46.5,
            "creatinine": 1.6,
            "potassium": 5.1,
            "inr": 2.3,
            "alt": 120.6,
            "ast": 100.1
        },
        "diagnoses": [
            "chronic_liver_disease",
            "chronic_kidney_disease"
        ],
        "medications": [
            "allopurinol",
            "atorvastatin",
            "azithromycin",
            "calcium_carbonate",
            "citalopram",
            "levothyroxine",
            "sildenafil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0074-1",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-M-0074-2",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-M-0074-3",
                "drug_a": "allopurinol",
                "drug_b": "warfarin",
                "severity": "moderate",
                "evidence": "allopurinol may enhance warfarin anticoagulation"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0075",
        "age": 87,
        "labs": {
            "egfr": 42.0,
            "creatinine": 2.2,
            "potassium": 4.8,
            "inr": 1.8
        },
        "diagnoses": [
            "hypertension",
            "osteoarthritis",
            "anxiety"
        ],
        "medications": [
            "citalopram",
            "diltiazem",
            "ferrous_sulfate",
            "levothyroxine",
            "linezolid",
            "sertraline",
            "simvastatin",
            "spironolactone",
            "valsartan"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0075-1",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-M-0075-2",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-M-0075-3",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            },
            {
                "interaction_id": "INT-SYN-M-0075-4",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0076",
        "age": 94,
        "labs": {
            "egfr": 76.1,
            "creatinine": 1.6,
            "potassium": 4.7,
            "inr": 2.7
        },
        "diagnoses": [
            "anxiety",
            "dyslipidemia",
            "chronic_kidney_disease",
            "peripheral_artery_disease"
        ],
        "medications": [
            "allopurinol",
            "apixaban",
            "atorvastatin",
            "diltiazem",
            "ibuprofen",
            "levothyroxine",
            "linezolid",
            "naproxen",
            "sertraline",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0076-1",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0076-2",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-M-0076-3",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "CYP3A4 inhibition raises statin concentration"
            },
            {
                "interaction_id": "INT-SYN-M-0076-4",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0077",
        "age": 84,
        "labs": {
            "egfr": 72.7,
            "creatinine": 1.2,
            "potassium": 5.4,
            "inr": 2.1,
            "alt": 119.3,
            "ast": 103.5
        },
        "diagnoses": [
            "heart_failure",
            "peripheral_artery_disease",
            "chronic_pain"
        ],
        "medications": [
            "amlodipine",
            "ciprofloxacin",
            "clopidogrel",
            "fluconazole",
            "linezolid",
            "metformin",
            "omeprazole",
            "sertraline",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0077-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0077-2",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-M-0077-3",
                "drug_a": "amlodipine",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive hypotension in frail adults"
            },
            {
                "interaction_id": "INT-SYN-M-0077-4",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0078",
        "age": 91,
        "labs": {
            "egfr": 42.0,
            "creatinine": 1.4,
            "potassium": 5.3,
            "inr": 2.1
        },
        "diagnoses": [
            "dyslipidemia",
            "peripheral_artery_disease",
            "hypertension"
        ],
        "medications": [
            "amiodarone",
            "apixaban",
            "azithromycin",
            "citalopram",
            "diltiazem",
            "metoprolol",
            "paroxetine",
            "simvastatin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0078-1",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0078-2",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-M-0078-3",
                "drug_a": "metoprolol",
                "drug_b": "paroxetine",
                "severity": "moderate",
                "evidence": "CYP2D6 inhibition raises metoprolol exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0078-4",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0079",
        "age": 90,
        "labs": {
            "egfr": 43.1,
            "creatinine": 2.0,
            "potassium": 4.8,
            "inr": 2.7
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "nonalcoholic_steatohepatitis",
            "gout",
            "dyslipidemia"
        ],
        "medications": [
            "aspirin",
            "losartan",
            "metoprolol",
            "nitroglycerin",
            "paroxetine",
            "sildenafil",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0079-1",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-M-0079-2",
                "drug_a": "metoprolol",
                "drug_b": "paroxetine",
                "severity": "moderate",
                "evidence": "CYP2D6 inhibition raises metoprolol exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0079-3",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0080",
        "age": 86,
        "labs": {
            "egfr": 46.3,
            "creatinine": 2.3,
            "potassium": 4.8,
            "inr": 1.9
        },
        "diagnoses": [
            "depression",
            "coronary_artery_disease"
        ],
        "medications": [
            "aspirin",
            "ciprofloxacin",
            "citalopram",
            "fluconazole",
            "metoprolol",
            "nitroglycerin",
            "sildenafil",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0080-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0080-2",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-M-0080-3",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0081",
        "age": 76,
        "labs": {
            "egfr": 60.2,
            "creatinine": 1.4,
            "potassium": 4.7,
            "inr": 2.6,
            "alt": 120.7,
            "ast": 108.7
        },
        "diagnoses": [
            "osteoarthritis",
            "hypothyroidism",
            "chronic_liver_disease",
            "type_2_diabetes"
        ],
        "medications": [
            "apixaban",
            "azithromycin",
            "clarithromycin",
            "ibuprofen",
            "ketoconazole",
            "metoprolol",
            "naproxen",
            "rivaroxaban",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0081-1",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0081-2",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0081-3",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0082",
        "age": 77,
        "labs": {
            "egfr": 31.7,
            "creatinine": 1.6,
            "potassium": 4.6,
            "inr": 2.4
        },
        "diagnoses": [
            "gout",
            "osteoarthritis"
        ],
        "medications": [
            "amlodipine",
            "cetirizine",
            "clopidogrel",
            "isosorbide_mononitrate",
            "omeprazole",
            "prednisone",
            "sildenafil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0082-1",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-M-0082-2",
                "drug_a": "cetirizine",
                "drug_b": "amlodipine",
                "severity": "minor",
                "evidence": "possible additive sedation in elderly"
            },
            {
                "interaction_id": "INT-SYN-M-0082-3",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0083",
        "age": 76,
        "labs": {
            "egfr": 41.4,
            "creatinine": 2.3,
            "potassium": 4.6,
            "inr": 2.9,
            "alt": 122.8,
            "ast": 108.0
        },
        "diagnoses": [
            "dyslipidemia",
            "heart_failure",
            "type_2_diabetes",
            "anemia"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "aspirin",
            "furosemide",
            "linezolid",
            "metformin",
            "sertraline",
            "simvastatin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0083-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0083-2",
                "drug_a": "metformin",
                "drug_b": "furosemide",
                "severity": "moderate",
                "evidence": "reduced renal clearance can increase lactic acidosis risk"
            },
            {
                "interaction_id": "INT-SYN-M-0083-3",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-M-0083-4",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0084",
        "age": 75,
        "labs": {
            "egfr": 33.0,
            "creatinine": 1.8,
            "potassium": 4.5,
            "inr": 1.6
        },
        "diagnoses": [
            "hypothyroidism",
            "chronic_kidney_disease",
            "osteoarthritis"
        ],
        "medications": [
            "amlodipine",
            "ciprofloxacin",
            "furosemide",
            "lisinopril",
            "metoprolol",
            "metronidazole",
            "sertraline",
            "simvastatin",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0084-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0084-2",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            },
            {
                "interaction_id": "INT-SYN-M-0084-3",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-M-0084-4",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0085",
        "age": 82,
        "labs": {
            "egfr": 69.0,
            "creatinine": 1.7,
            "potassium": 5.5,
            "inr": 2.3
        },
        "diagnoses": [
            "chronic_liver_disease",
            "chronic_kidney_disease",
            "heart_failure",
            "anemia"
        ],
        "medications": [
            "amiodarone",
            "calcium_carbonate",
            "clopidogrel",
            "digoxin",
            "furosemide",
            "ibuprofen",
            "metoprolol",
            "nitroglycerin",
            "sildenafil",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0085-1",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-M-0085-2",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-M-0085-3",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0085-4",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0086",
        "age": 80,
        "labs": {
            "egfr": 44.4,
            "creatinine": 1.3,
            "potassium": 5.3,
            "inr": 2.5,
            "alt": 117.5,
            "ast": 113.6
        },
        "diagnoses": [
            "gout",
            "chronic_liver_disease",
            "dyslipidemia"
        ],
        "medications": [
            "apixaban",
            "atorvastatin",
            "azithromycin",
            "citalopram",
            "ferrous_sulfate",
            "ibuprofen",
            "levothyroxine",
            "metronidazole",
            "naproxen",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0086-1",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0086-2",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-M-0086-3",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0086-4",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0087",
        "age": 76,
        "labs": {
            "egfr": 35.9,
            "creatinine": 1.0,
            "potassium": 4.9,
            "inr": 1.8,
            "alt": 114.1,
            "ast": 117.0
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "chronic_liver_disease",
            "depression"
        ],
        "medications": [
            "apixaban",
            "clarithromycin",
            "losartan",
            "metronidazole",
            "omeprazole",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0087-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0087-2",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-M-0087-3",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0088",
        "age": 88,
        "labs": {
            "egfr": 25.0,
            "creatinine": 1.1,
            "potassium": 4.9,
            "inr": 1.5,
            "alt": 115.2,
            "ast": 115.2
        },
        "diagnoses": [
            "anxiety",
            "osteoarthritis"
        ],
        "medications": [
            "apixaban",
            "calcium_carbonate",
            "clarithromycin",
            "levothyroxine",
            "linezolid",
            "metoprolol",
            "nitroglycerin",
            "paroxetine",
            "sildenafil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0088-1",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-M-0088-2",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0088-3",
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
        "case_id": "SYN-M-0089",
        "age": 94,
        "labs": {
            "egfr": 86.5,
            "creatinine": 1.8,
            "potassium": 4.6,
            "inr": 2.3
        },
        "diagnoses": [
            "chronic_liver_disease",
            "osteoarthritis"
        ],
        "medications": [
            "apixaban",
            "clarithromycin",
            "clopidogrel",
            "dabigatran",
            "furosemide",
            "ketoconazole",
            "lisinopril",
            "metformin",
            "omeprazole",
            "trimethoprim_sulfamethoxazole"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0089-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0089-2",
                "drug_a": "metformin",
                "drug_b": "furosemide",
                "severity": "moderate",
                "evidence": "reduced renal clearance can increase lactic acidosis risk"
            },
            {
                "interaction_id": "INT-SYN-M-0089-3",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0089-4",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0090",
        "age": 80,
        "labs": {
            "egfr": 43.4,
            "creatinine": 1.8,
            "potassium": 4.5,
            "inr": 2.9,
            "alt": 127.5,
            "ast": 120.7
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "depression",
            "heart_failure"
        ],
        "medications": [
            "dabigatran",
            "digoxin",
            "ketoconazole",
            "nitroglycerin",
            "omeprazole",
            "sildenafil",
            "spironolactone",
            "ticagrelor",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0090-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0090-2",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-M-0090-3",
                "drug_a": "digoxin",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "P-gp inhibition can raise digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-M-0090-4",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0091",
        "age": 81,
        "labs": {
            "egfr": 69.8,
            "creatinine": 2.0,
            "potassium": 4.7,
            "inr": 2.9
        },
        "diagnoses": [
            "heart_failure",
            "atrial_fibrillation",
            "hypertension",
            "depression"
        ],
        "medications": [
            "amiodarone",
            "aspirin",
            "clopidogrel",
            "digoxin",
            "linezolid",
            "omeprazole",
            "rivaroxaban",
            "sertraline"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0091-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-M-0091-2",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-M-0091-3",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0092",
        "age": 86,
        "labs": {
            "egfr": 63.0,
            "creatinine": 2.5,
            "potassium": 5.2,
            "inr": 2.8,
            "alt": 120.5,
            "ast": 114.3
        },
        "diagnoses": [
            "anemia",
            "hypertension"
        ],
        "medications": [
            "amiodarone",
            "apixaban",
            "clarithromycin",
            "furosemide",
            "ketoconazole",
            "metoprolol",
            "omeprazole",
            "spironolactone",
            "valsartan",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0092-1",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0092-2",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            },
            {
                "interaction_id": "INT-SYN-M-0092-3",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            },
            {
                "interaction_id": "INT-SYN-M-0092-4",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0093",
        "age": 83,
        "labs": {
            "egfr": 47.8,
            "creatinine": 1.9,
            "potassium": 5.4,
            "inr": 2.6,
            "alt": 113.3,
            "ast": 113.5
        },
        "diagnoses": [
            "chronic_pain",
            "chronic_liver_disease",
            "peripheral_artery_disease"
        ],
        "medications": [
            "amiodarone",
            "apixaban",
            "digoxin",
            "furosemide",
            "metoprolol",
            "naproxen",
            "nitroglycerin",
            "sildenafil",
            "simvastatin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0093-1",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-M-0093-2",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0093-3",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-M-0093-4",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0094",
        "age": 82,
        "labs": {
            "egfr": 66.0,
            "creatinine": 1.9,
            "potassium": 4.9,
            "inr": 2.7,
            "alt": 128.7,
            "ast": 115.1
        },
        "diagnoses": [
            "type_2_diabetes",
            "hypothyroidism",
            "peripheral_artery_disease",
            "chronic_kidney_disease"
        ],
        "medications": [
            "azithromycin",
            "diclofenac",
            "metoprolol",
            "naproxen",
            "nitroglycerin",
            "omeprazole",
            "rivaroxaban",
            "ticagrelor",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0094-1",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-M-0094-2",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0094-3",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0094-4",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0095",
        "age": 86,
        "labs": {
            "egfr": 28.4,
            "creatinine": 2.5,
            "potassium": 4.8,
            "inr": 2.7
        },
        "diagnoses": [
            "chronic_liver_disease",
            "hypertension",
            "type_2_diabetes",
            "gout"
        ],
        "medications": [
            "allopurinol",
            "ferrous_sulfate",
            "furosemide",
            "ketoconazole",
            "lisinopril",
            "metformin",
            "naproxen",
            "rivaroxaban",
            "simvastatin",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0095-1",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0095-2",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            },
            {
                "interaction_id": "INT-SYN-M-0095-3",
                "drug_a": "allopurinol",
                "drug_b": "warfarin",
                "severity": "moderate",
                "evidence": "allopurinol may enhance warfarin anticoagulation"
            },
            {
                "interaction_id": "INT-SYN-M-0095-4",
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
        "case_id": "SYN-M-0096",
        "age": 84,
        "labs": {
            "egfr": 40.4,
            "creatinine": 1.7,
            "potassium": 4.6,
            "inr": 1.7,
            "alt": 129.6,
            "ast": 114.8
        },
        "diagnoses": [
            "hypertension",
            "peripheral_artery_disease",
            "osteoarthritis"
        ],
        "medications": [
            "azithromycin",
            "citalopram",
            "furosemide",
            "ibuprofen",
            "metformin",
            "spironolactone",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0096-1",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-M-0096-2",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0096-3",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0097",
        "age": 83,
        "labs": {
            "egfr": 29.7,
            "creatinine": 1.3,
            "potassium": 5.1,
            "inr": 1.7
        },
        "diagnoses": [
            "nonalcoholic_steatohepatitis",
            "chronic_pain",
            "heart_failure",
            "atrial_fibrillation"
        ],
        "medications": [
            "amiodarone",
            "apixaban",
            "clarithromycin",
            "fluconazole",
            "isosorbide_mononitrate",
            "omeprazole",
            "sildenafil",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0097-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0097-2",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0097-3",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-M-0097-4",
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
        "case_id": "SYN-M-0098",
        "age": 78,
        "labs": {
            "egfr": 44.3,
            "creatinine": 2.4,
            "potassium": 5.2,
            "inr": 1.5,
            "alt": 127.2,
            "ast": 116.3
        },
        "diagnoses": [
            "gout",
            "hypertension",
            "coronary_artery_disease",
            "anxiety"
        ],
        "medications": [
            "aspirin",
            "calcium_carbonate",
            "digoxin",
            "levothyroxine",
            "linezolid",
            "sertraline",
            "spironolactone",
            "trimethoprim_sulfamethoxazole",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0098-1",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0098-2",
                "drug_a": "digoxin",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "P-gp inhibition can raise digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-M-0098-3",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-M-0098-4",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0099",
        "age": 88,
        "labs": {
            "egfr": 44.2,
            "creatinine": 2.1,
            "potassium": 5.5,
            "inr": 1.9
        },
        "diagnoses": [
            "coronary_artery_disease",
            "heart_failure",
            "type_2_diabetes"
        ],
        "medications": [
            "amlodipine",
            "azithromycin",
            "cetirizine",
            "citalopram",
            "clarithromycin",
            "linezolid",
            "lisinopril",
            "nitroglycerin",
            "sertraline",
            "sildenafil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0099-1",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-M-0099-2",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-M-0099-3",
                "drug_a": "cetirizine",
                "drug_b": "amlodipine",
                "severity": "minor",
                "evidence": "possible additive sedation in elderly"
            },
            {
                "interaction_id": "INT-SYN-M-0099-4",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0100",
        "age": 81,
        "labs": {
            "egfr": 42.9,
            "creatinine": 1.6,
            "potassium": 4.9,
            "inr": 1.7
        },
        "diagnoses": [
            "hypertension",
            "heart_failure"
        ],
        "medications": [
            "amlodipine",
            "azithromycin",
            "ciprofloxacin",
            "citalopram",
            "dabigatran",
            "glipizide",
            "ketoconazole"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0100-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0100-2",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-M-0100-3",
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
        "case_id": "SYN-M-0101",
        "age": 77,
        "labs": {
            "egfr": 42.1,
            "creatinine": 2.1,
            "potassium": 4.7,
            "inr": 3.0,
            "alt": 124.6,
            "ast": 117.1
        },
        "diagnoses": [
            "hypothyroidism",
            "hypertension",
            "osteoarthritis",
            "chronic_pain"
        ],
        "medications": [
            "amlodipine",
            "azithromycin",
            "furosemide",
            "ibuprofen",
            "linezolid",
            "metoprolol",
            "sertraline",
            "simvastatin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0101-1",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-M-0101-2",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0101-3",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-M-0101-4",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0102",
        "age": 83,
        "labs": {
            "egfr": 68.1,
            "creatinine": 1.9,
            "potassium": 5.5,
            "inr": 1.7
        },
        "diagnoses": [
            "chronic_liver_disease",
            "anxiety",
            "dyslipidemia"
        ],
        "medications": [
            "apixaban",
            "aspirin",
            "calcium_carbonate",
            "cetirizine",
            "dabigatran",
            "ketoconazole",
            "naproxen",
            "spironolactone",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0102-1",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0102-2",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            },
            {
                "interaction_id": "INT-SYN-M-0102-3",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0102-4",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0103",
        "age": 84,
        "labs": {
            "egfr": 48.0,
            "creatinine": 2.2,
            "potassium": 5.3,
            "inr": 2.1,
            "alt": 123.7,
            "ast": 118.0
        },
        "diagnoses": [
            "hypertension",
            "gout",
            "peripheral_artery_disease"
        ],
        "medications": [
            "amlodipine",
            "ciprofloxacin",
            "lisinopril",
            "simvastatin",
            "spironolactone",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0103-1",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0103-2",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-M-0103-3",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0104",
        "age": 80,
        "labs": {
            "egfr": 80.1,
            "creatinine": 1.2,
            "potassium": 5.0,
            "inr": 1.7,
            "alt": 121.0,
            "ast": 120.2
        },
        "diagnoses": [
            "nonalcoholic_steatohepatitis",
            "hypertension",
            "chronic_liver_disease"
        ],
        "medications": [
            "allopurinol",
            "amiodarone",
            "apixaban",
            "clopidogrel",
            "diclofenac",
            "digoxin",
            "lisinopril",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0104-1",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0104-2",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-M-0104-3",
                "drug_a": "allopurinol",
                "drug_b": "warfarin",
                "severity": "moderate",
                "evidence": "allopurinol may enhance warfarin anticoagulation"
            },
            {
                "interaction_id": "INT-SYN-M-0104-4",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0105",
        "age": 86,
        "labs": {
            "egfr": 45.3,
            "creatinine": 1.8,
            "potassium": 5.4,
            "inr": 1.7
        },
        "diagnoses": [
            "anxiety",
            "gout",
            "chronic_pain",
            "depression"
        ],
        "medications": [
            "azithromycin",
            "citalopram",
            "diclofenac",
            "ibuprofen",
            "isosorbide_mononitrate",
            "metoprolol",
            "naproxen",
            "omeprazole",
            "sildenafil",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0105-1",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-M-0105-2",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-M-0105-3",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0105-4",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0106",
        "age": 90,
        "labs": {
            "egfr": 33.1,
            "creatinine": 2.1,
            "potassium": 5.4,
            "inr": 2.4,
            "alt": 115.8,
            "ast": 110.3
        },
        "diagnoses": [
            "type_2_diabetes",
            "anemia",
            "heart_failure"
        ],
        "medications": [
            "apixaban",
            "ciprofloxacin",
            "diclofenac",
            "diltiazem",
            "ibuprofen",
            "omeprazole",
            "paroxetine",
            "sildenafil",
            "simvastatin",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0106-1",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0106-2",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-M-0106-3",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0106-4",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0107",
        "age": 80,
        "labs": {
            "egfr": 44.0,
            "creatinine": 1.6,
            "potassium": 4.9,
            "inr": 2.6,
            "alt": 129.0,
            "ast": 122.4
        },
        "diagnoses": [
            "chronic_liver_disease",
            "depression",
            "anxiety"
        ],
        "medications": [
            "amiodarone",
            "citalopram",
            "digoxin",
            "ferrous_sulfate",
            "nitroglycerin",
            "omeprazole",
            "sildenafil",
            "ticagrelor",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0107-1",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-M-0107-2",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-M-0107-3",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0108",
        "age": 79,
        "labs": {
            "egfr": 26.4,
            "creatinine": 1.7,
            "potassium": 5.1,
            "inr": 1.8,
            "alt": 113.0,
            "ast": 107.6
        },
        "diagnoses": [
            "type_2_diabetes",
            "peripheral_artery_disease",
            "hypothyroidism"
        ],
        "medications": [
            "amiodarone",
            "amlodipine",
            "cetirizine",
            "diclofenac",
            "digoxin",
            "fluconazole",
            "naproxen",
            "rivaroxaban",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0108-1",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-M-0108-2",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0108-3",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0108-4",
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
        "case_id": "SYN-M-0109",
        "age": 84,
        "labs": {
            "egfr": 46.2,
            "creatinine": 1.6,
            "potassium": 4.6,
            "inr": 1.8
        },
        "diagnoses": [
            "dyslipidemia",
            "coronary_artery_disease",
            "atrial_fibrillation"
        ],
        "medications": [
            "clopidogrel",
            "digoxin",
            "lisinopril",
            "metronidazole",
            "omeprazole",
            "paroxetine",
            "spironolactone",
            "ticagrelor",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0109-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0109-2",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            },
            {
                "interaction_id": "INT-SYN-M-0109-3",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-M-0109-4",
                "drug_a": "digoxin",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "P-gp inhibition can raise digoxin concentration"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0110",
        "age": 77,
        "labs": {
            "egfr": 89.3,
            "creatinine": 1.4,
            "potassium": 5.3,
            "inr": 2.4,
            "alt": 123.8,
            "ast": 108.4
        },
        "diagnoses": [
            "gout",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "ciprofloxacin",
            "digoxin",
            "glipizide",
            "ibuprofen",
            "isosorbide_mononitrate",
            "naproxen",
            "rivaroxaban",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0110-1",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0110-2",
                "drug_a": "glipizide",
                "drug_b": "ciprofloxacin",
                "severity": "moderate",
                "evidence": "dysglycemia risk from fluoroquinolone-sulfonylurea combination"
            },
            {
                "interaction_id": "INT-SYN-M-0110-3",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0111",
        "age": 84,
        "labs": {
            "egfr": 45.5,
            "creatinine": 1.8,
            "potassium": 4.7,
            "inr": 1.9
        },
        "diagnoses": [
            "chronic_liver_disease",
            "coronary_artery_disease",
            "peripheral_artery_disease",
            "hypothyroidism"
        ],
        "medications": [
            "amiodarone",
            "apixaban",
            "aspirin",
            "calcium_carbonate",
            "clarithromycin",
            "dabigatran",
            "ketoconazole",
            "naproxen",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0111-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0111-2",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0111-3",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0112",
        "age": 93,
        "labs": {
            "egfr": 31.2,
            "creatinine": 1.8,
            "potassium": 5.2,
            "inr": 3.0,
            "alt": 125.0,
            "ast": 106.2
        },
        "diagnoses": [
            "nonalcoholic_steatohepatitis",
            "osteoarthritis"
        ],
        "medications": [
            "aspirin",
            "calcium_carbonate",
            "clopidogrel",
            "levothyroxine",
            "losartan",
            "omeprazole",
            "sertraline"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0112-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-M-0112-2",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-M-0112-3",
                "drug_a": "aspirin",
                "drug_b": "sertraline",
                "severity": "minor",
                "evidence": "increased bleeding tendency, amplified in frailty"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0113",
        "age": 78,
        "labs": {
            "egfr": 46.3,
            "creatinine": 1.4,
            "potassium": 4.6,
            "inr": 2.8,
            "alt": 121.3,
            "ast": 102.2
        },
        "diagnoses": [
            "hypertension",
            "depression"
        ],
        "medications": [
            "dabigatran",
            "ketoconazole",
            "linezolid",
            "lisinopril",
            "metformin",
            "metoprolol",
            "omeprazole",
            "paroxetine",
            "rivaroxaban",
            "spironolactone",
            "ticagrelor"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0113-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0113-2",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-M-0113-3",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            },
            {
                "interaction_id": "INT-SYN-M-0113-4",
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
        "case_id": "SYN-M-0114",
        "age": 77,
        "labs": {
            "egfr": 35.5,
            "creatinine": 2.4,
            "potassium": 4.7,
            "inr": 1.6,
            "alt": 127.8,
            "ast": 124.9
        },
        "diagnoses": [
            "depression",
            "type_2_diabetes"
        ],
        "medications": [
            "apixaban",
            "aspirin",
            "clarithromycin",
            "ferrous_sulfate",
            "levothyroxine",
            "linezolid",
            "sertraline"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0114-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0114-2",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-M-0114-3",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0115",
        "age": 95,
        "labs": {
            "egfr": 65.6,
            "creatinine": 2.2,
            "potassium": 5.0,
            "inr": 2.7,
            "alt": 111.3,
            "ast": 113.7
        },
        "diagnoses": [
            "chronic_liver_disease",
            "dyslipidemia",
            "heart_failure",
            "atrial_fibrillation"
        ],
        "medications": [
            "apixaban",
            "diclofenac",
            "ferrous_sulfate",
            "fluconazole",
            "glipizide",
            "metoprolol",
            "paroxetine",
            "spironolactone",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0115-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0115-2",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0115-3",
                "drug_a": "metoprolol",
                "drug_b": "paroxetine",
                "severity": "moderate",
                "evidence": "CYP2D6 inhibition raises metoprolol exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0115-4",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0116",
        "age": 78,
        "labs": {
            "egfr": 44.5,
            "creatinine": 2.3,
            "potassium": 4.6,
            "inr": 1.9
        },
        "diagnoses": [
            "type_2_diabetes",
            "atrial_fibrillation"
        ],
        "medications": [
            "azithromycin",
            "ciprofloxacin",
            "citalopram",
            "clarithromycin",
            "furosemide",
            "metformin",
            "metronidazole",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0116-1",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-M-0116-2",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0116-3",
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
        "case_id": "SYN-M-0117",
        "age": 89,
        "labs": {
            "egfr": 26.5,
            "creatinine": 2.1,
            "potassium": 4.9,
            "inr": 2.8
        },
        "diagnoses": [
            "depression",
            "anxiety"
        ],
        "medications": [
            "apixaban",
            "atorvastatin",
            "ibuprofen",
            "losartan",
            "naproxen",
            "simvastatin",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0117-1",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0117-2",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0117-3",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0118",
        "age": 76,
        "labs": {
            "egfr": 33.4,
            "creatinine": 1.5,
            "potassium": 5.4,
            "inr": 2.8,
            "alt": 111.9,
            "ast": 105.6
        },
        "diagnoses": [
            "hypothyroidism",
            "chronic_pain"
        ],
        "medications": [
            "clarithromycin",
            "dabigatran",
            "diltiazem",
            "ibuprofen",
            "ketoconazole",
            "naproxen",
            "rivaroxaban",
            "simvastatin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0118-1",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0118-2",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0118-3",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0119",
        "age": 88,
        "labs": {
            "egfr": 71.6,
            "creatinine": 1.6,
            "potassium": 5.2,
            "inr": 1.9
        },
        "diagnoses": [
            "dyslipidemia",
            "hypothyroidism"
        ],
        "medications": [
            "amiodarone",
            "digoxin",
            "furosemide",
            "linezolid",
            "losartan",
            "metoprolol",
            "omeprazole",
            "sertraline"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0119-1",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-M-0119-2",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-M-0119-3",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0120",
        "age": 85,
        "labs": {
            "egfr": 47.8,
            "creatinine": 2.0,
            "potassium": 4.6,
            "inr": 2.0,
            "alt": 116.2,
            "ast": 118.2
        },
        "diagnoses": [
            "heart_failure",
            "coronary_artery_disease"
        ],
        "medications": [
            "ciprofloxacin",
            "clopidogrel",
            "glipizide",
            "linezolid",
            "nitroglycerin",
            "omeprazole",
            "sertraline"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0120-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-M-0120-2",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-M-0120-3",
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
        "case_id": "SYN-M-0121",
        "age": 78,
        "labs": {
            "egfr": 46.9,
            "creatinine": 2.4,
            "potassium": 4.9,
            "inr": 2.2
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "nonalcoholic_steatohepatitis",
            "dyslipidemia"
        ],
        "medications": [
            "diclofenac",
            "diltiazem",
            "ferrous_sulfate",
            "furosemide",
            "metformin",
            "nitroglycerin",
            "sildenafil",
            "simvastatin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0121-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0121-2",
                "drug_a": "metformin",
                "drug_b": "furosemide",
                "severity": "moderate",
                "evidence": "reduced renal clearance can increase lactic acidosis risk"
            },
            {
                "interaction_id": "INT-SYN-M-0121-3",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-M-0121-4",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0122",
        "age": 88,
        "labs": {
            "egfr": 30.6,
            "creatinine": 2.0,
            "potassium": 5.4,
            "inr": 2.5,
            "alt": 118.5,
            "ast": 104.1
        },
        "diagnoses": [
            "heart_failure",
            "depression",
            "chronic_kidney_disease",
            "anemia"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "digoxin",
            "ferrous_sulfate",
            "ibuprofen",
            "levothyroxine",
            "lisinopril",
            "spironolactone",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0122-1",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0122-2",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-M-0122-3",
                "drug_a": "digoxin",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "P-gp inhibition can raise digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-M-0122-4",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0123",
        "age": 90,
        "labs": {
            "egfr": 61.9,
            "creatinine": 2.2,
            "potassium": 5.0,
            "inr": 2.5,
            "alt": 128.5,
            "ast": 112.2
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "anemia",
            "dyslipidemia"
        ],
        "medications": [
            "apixaban",
            "calcium_carbonate",
            "clopidogrel",
            "diclofenac",
            "ferrous_sulfate",
            "furosemide",
            "levothyroxine",
            "losartan",
            "metformin",
            "spironolactone"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0123-1",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0123-2",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            },
            {
                "interaction_id": "INT-SYN-M-0123-3",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-M-0123-4",
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
        "case_id": "SYN-M-0124",
        "age": 93,
        "labs": {
            "egfr": 86.3,
            "creatinine": 1.2,
            "potassium": 4.6,
            "inr": 2.8
        },
        "diagnoses": [
            "gout",
            "coronary_artery_disease",
            "hypothyroidism",
            "chronic_kidney_disease"
        ],
        "medications": [
            "apixaban",
            "citalopram",
            "diclofenac",
            "digoxin",
            "furosemide",
            "valsartan",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0124-1",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0124-2",
                "drug_a": "furosemide",
                "drug_b": "warfarin",
                "severity": "minor",
                "evidence": "volume changes may alter INR stability"
            },
            {
                "interaction_id": "INT-SYN-M-0124-3",
                "drug_a": "digoxin",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "P-gp inhibition can raise digoxin concentration"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0125",
        "age": 90,
        "labs": {
            "egfr": 43.4,
            "creatinine": 2.3,
            "potassium": 5.3,
            "inr": 2.5
        },
        "diagnoses": [
            "anemia",
            "heart_failure"
        ],
        "medications": [
            "apixaban",
            "atorvastatin",
            "clopidogrel",
            "diltiazem",
            "furosemide",
            "naproxen",
            "omeprazole",
            "sertraline",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0125-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-M-0125-2",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "CYP3A4 inhibition raises statin concentration"
            },
            {
                "interaction_id": "INT-SYN-M-0125-3",
                "drug_a": "furosemide",
                "drug_b": "warfarin",
                "severity": "minor",
                "evidence": "volume changes may alter INR stability"
            },
            {
                "interaction_id": "INT-SYN-M-0125-4",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0126",
        "age": 78,
        "labs": {
            "egfr": 83.8,
            "creatinine": 1.4,
            "potassium": 5.1,
            "inr": 1.5
        },
        "diagnoses": [
            "type_2_diabetes",
            "osteoarthritis"
        ],
        "medications": [
            "amiodarone",
            "atorvastatin",
            "digoxin",
            "diltiazem",
            "furosemide",
            "linezolid",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0126-1",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-M-0126-2",
                "drug_a": "furosemide",
                "drug_b": "warfarin",
                "severity": "minor",
                "evidence": "volume changes may alter INR stability"
            },
            {
                "interaction_id": "INT-SYN-M-0126-3",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "CYP3A4 inhibition raises statin concentration"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0127",
        "age": 78,
        "labs": {
            "egfr": 37.8,
            "creatinine": 1.1,
            "potassium": 4.5,
            "inr": 2.8,
            "alt": 118.4,
            "ast": 119.1
        },
        "diagnoses": [
            "heart_failure",
            "chronic_pain",
            "atrial_fibrillation"
        ],
        "medications": [
            "amiodarone",
            "amlodipine",
            "clopidogrel",
            "furosemide",
            "losartan",
            "metoprolol",
            "nitroglycerin",
            "omeprazole",
            "simvastatin",
            "spironolactone",
            "valsartan"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0127-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-M-0127-2",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-M-0127-3",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-M-0127-4",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0128",
        "age": 85,
        "labs": {
            "egfr": 76.4,
            "creatinine": 2.2,
            "potassium": 5.4,
            "inr": 3.0
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "chronic_pain"
        ],
        "medications": [
            "amlodipine",
            "cetirizine",
            "clarithromycin",
            "diclofenac",
            "ibuprofen",
            "lisinopril",
            "metoprolol",
            "naproxen",
            "rivaroxaban",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0128-1",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0128-2",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0128-3",
                "drug_a": "cetirizine",
                "drug_b": "amlodipine",
                "severity": "minor",
                "evidence": "possible additive sedation in elderly"
            },
            {
                "interaction_id": "INT-SYN-M-0128-4",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0129",
        "age": 83,
        "labs": {
            "egfr": 42.4,
            "creatinine": 1.7,
            "potassium": 4.9,
            "inr": 3.0,
            "alt": 126.6,
            "ast": 124.9
        },
        "diagnoses": [
            "hypothyroidism",
            "anemia",
            "depression"
        ],
        "medications": [
            "azithromycin",
            "diclofenac",
            "isosorbide_mononitrate",
            "prednisone",
            "sildenafil",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0129-1",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-M-0129-2",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0129-3",
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
        "case_id": "SYN-M-0130",
        "age": 80,
        "labs": {
            "egfr": 35.4,
            "creatinine": 1.0,
            "potassium": 5.5,
            "inr": 2.5,
            "alt": 113.8,
            "ast": 113.9
        },
        "diagnoses": [
            "atrial_fibrillation",
            "nonalcoholic_steatohepatitis",
            "type_2_diabetes",
            "gout"
        ],
        "medications": [
            "amiodarone",
            "aspirin",
            "digoxin",
            "prednisone",
            "sertraline",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0130-1",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0130-2",
                "drug_a": "aspirin",
                "drug_b": "sertraline",
                "severity": "minor",
                "evidence": "increased bleeding tendency, amplified in frailty"
            },
            {
                "interaction_id": "INT-SYN-M-0130-3",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0131",
        "age": 76,
        "labs": {
            "egfr": 47.4,
            "creatinine": 2.3,
            "potassium": 4.9,
            "inr": 2.7,
            "alt": 123.0,
            "ast": 110.6
        },
        "diagnoses": [
            "chronic_pain",
            "depression",
            "type_2_diabetes",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "amlodipine",
            "ciprofloxacin",
            "dabigatran",
            "ketoconazole",
            "linezolid",
            "metoprolol",
            "sertraline",
            "valsartan",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0131-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0131-2",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-M-0131-3",
                "drug_a": "amlodipine",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive hypotension in frail adults"
            },
            {
                "interaction_id": "INT-SYN-M-0131-4",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0132",
        "age": 89,
        "labs": {
            "egfr": 43.5,
            "creatinine": 2.0,
            "potassium": 5.1,
            "inr": 1.9,
            "alt": 129.5,
            "ast": 110.8
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "gout",
            "type_2_diabetes",
            "anemia"
        ],
        "medications": [
            "amiodarone",
            "amlodipine",
            "apixaban",
            "ciprofloxacin",
            "dabigatran",
            "digoxin",
            "furosemide",
            "ketoconazole",
            "naproxen",
            "prednisone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0132-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0132-2",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-M-0132-3",
                "drug_a": "amlodipine",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive hypotension in frail adults"
            },
            {
                "interaction_id": "INT-SYN-M-0132-4",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0133",
        "age": 76,
        "labs": {
            "egfr": 41.8,
            "creatinine": 2.3,
            "potassium": 5.4,
            "inr": 2.4,
            "alt": 126.3,
            "ast": 103.7
        },
        "diagnoses": [
            "chronic_liver_disease",
            "depression",
            "atrial_fibrillation",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "aspirin",
            "dabigatran",
            "isosorbide_mononitrate",
            "ketoconazole",
            "metoprolol",
            "metronidazole",
            "sertraline",
            "sildenafil",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0133-1",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-M-0133-2",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0133-3",
                "drug_a": "aspirin",
                "drug_b": "sertraline",
                "severity": "minor",
                "evidence": "increased bleeding tendency, amplified in frailty"
            },
            {
                "interaction_id": "INT-SYN-M-0133-4",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0134",
        "age": 75,
        "labs": {
            "egfr": 30.9,
            "creatinine": 1.6,
            "potassium": 5.3,
            "inr": 2.0,
            "alt": 110.6,
            "ast": 108.2
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "anxiety",
            "chronic_pain",
            "type_2_diabetes"
        ],
        "medications": [
            "apixaban",
            "aspirin",
            "atorvastatin",
            "losartan",
            "naproxen",
            "sertraline",
            "spironolactone"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0134-1",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0134-2",
                "drug_a": "aspirin",
                "drug_b": "sertraline",
                "severity": "minor",
                "evidence": "increased bleeding tendency, amplified in frailty"
            },
            {
                "interaction_id": "INT-SYN-M-0134-3",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0135",
        "age": 76,
        "labs": {
            "egfr": 34.7,
            "creatinine": 1.8,
            "potassium": 4.6,
            "inr": 1.6
        },
        "diagnoses": [
            "heart_failure",
            "depression",
            "nonalcoholic_steatohepatitis",
            "coronary_artery_disease"
        ],
        "medications": [
            "azithromycin",
            "citalopram",
            "diltiazem",
            "ibuprofen",
            "lisinopril",
            "metronidazole",
            "sildenafil",
            "simvastatin",
            "spironolactone"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0135-1",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-M-0135-2",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-M-0135-3",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0136",
        "age": 78,
        "labs": {
            "egfr": 65.2,
            "creatinine": 2.2,
            "potassium": 4.8,
            "inr": 1.9
        },
        "diagnoses": [
            "type_2_diabetes",
            "osteoarthritis"
        ],
        "medications": [
            "ciprofloxacin",
            "diclofenac",
            "diltiazem",
            "ibuprofen",
            "simvastatin",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0136-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0136-2",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            },
            {
                "interaction_id": "INT-SYN-M-0136-3",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0137",
        "age": 82,
        "labs": {
            "egfr": 36.7,
            "creatinine": 1.4,
            "potassium": 4.5,
            "inr": 1.9,
            "alt": 116.9,
            "ast": 109.7
        },
        "diagnoses": [
            "chronic_liver_disease",
            "coronary_artery_disease",
            "anxiety",
            "anemia"
        ],
        "medications": [
            "aspirin",
            "ferrous_sulfate",
            "fluconazole",
            "metoprolol",
            "naproxen",
            "prednisone",
            "rivaroxaban",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0137-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0137-2",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            },
            {
                "interaction_id": "INT-SYN-M-0137-3",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0138",
        "age": 89,
        "labs": {
            "egfr": 34.7,
            "creatinine": 1.5,
            "potassium": 5.2,
            "inr": 2.3,
            "alt": 119.7,
            "ast": 100.5
        },
        "diagnoses": [
            "chronic_liver_disease",
            "hypothyroidism",
            "coronary_artery_disease"
        ],
        "medications": [
            "amiodarone",
            "apixaban",
            "cetirizine",
            "ciprofloxacin",
            "digoxin",
            "glipizide",
            "naproxen",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0138-1",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0138-2",
                "drug_a": "digoxin",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "P-gp inhibition can raise digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-M-0138-3",
                "drug_a": "glipizide",
                "drug_b": "ciprofloxacin",
                "severity": "moderate",
                "evidence": "dysglycemia risk from fluoroquinolone-sulfonylurea combination"
            },
            {
                "interaction_id": "INT-SYN-M-0138-4",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0139",
        "age": 85,
        "labs": {
            "egfr": 73.0,
            "creatinine": 2.4,
            "potassium": 5.0,
            "inr": 2.7
        },
        "diagnoses": [
            "chronic_liver_disease",
            "depression",
            "hypothyroidism",
            "chronic_pain"
        ],
        "medications": [
            "azithromycin",
            "calcium_carbonate",
            "ciprofloxacin",
            "citalopram",
            "glipizide",
            "levothyroxine",
            "losartan",
            "omeprazole",
            "prednisone",
            "ticagrelor"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0139-1",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-M-0139-2",
                "drug_a": "glipizide",
                "drug_b": "ciprofloxacin",
                "severity": "moderate",
                "evidence": "dysglycemia risk from fluoroquinolone-sulfonylurea combination"
            },
            {
                "interaction_id": "INT-SYN-M-0139-3",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-M-0139-4",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0140",
        "age": 76,
        "labs": {
            "egfr": 36.5,
            "creatinine": 2.0,
            "potassium": 4.6,
            "inr": 2.5,
            "alt": 113.1,
            "ast": 122.8
        },
        "diagnoses": [
            "anxiety",
            "atrial_fibrillation",
            "depression"
        ],
        "medications": [
            "ciprofloxacin",
            "clopidogrel",
            "dabigatran",
            "ketoconazole",
            "losartan",
            "omeprazole",
            "spironolactone",
            "trimethoprim_sulfamethoxazole",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0140-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-M-0140-2",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            },
            {
                "interaction_id": "INT-SYN-M-0140-3",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0140-4",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0141",
        "age": 87,
        "labs": {
            "egfr": 30.8,
            "creatinine": 1.9,
            "potassium": 4.7,
            "inr": 2.4
        },
        "diagnoses": [
            "coronary_artery_disease",
            "hypothyroidism",
            "gout",
            "dyslipidemia"
        ],
        "medications": [
            "amlodipine",
            "cetirizine",
            "dabigatran",
            "furosemide",
            "ibuprofen",
            "ketoconazole",
            "metoprolol",
            "naproxen",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0141-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0141-2",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0141-3",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-M-0141-4",
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
        "case_id": "SYN-M-0142",
        "age": 76,
        "labs": {
            "egfr": 44.9,
            "creatinine": 1.8,
            "potassium": 5.4,
            "inr": 2.3
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "dyslipidemia",
            "nonalcoholic_steatohepatitis",
            "chronic_liver_disease"
        ],
        "medications": [
            "amiodarone",
            "apixaban",
            "azithromycin",
            "diclofenac",
            "digoxin",
            "naproxen",
            "nitroglycerin",
            "sildenafil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0142-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0142-2",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-M-0142-3",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0142-4",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0143",
        "age": 92,
        "labs": {
            "egfr": 41.0,
            "creatinine": 1.3,
            "potassium": 5.5,
            "inr": 2.4,
            "alt": 127.3,
            "ast": 106.2
        },
        "diagnoses": [
            "dyslipidemia",
            "coronary_artery_disease",
            "heart_failure",
            "peripheral_artery_disease"
        ],
        "medications": [
            "apixaban",
            "aspirin",
            "azithromycin",
            "diclofenac",
            "lisinopril",
            "naproxen",
            "rivaroxaban",
            "spironolactone",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0143-1",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0143-2",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0143-3",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            },
            {
                "interaction_id": "INT-SYN-M-0143-4",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0144",
        "age": 85,
        "labs": {
            "egfr": 41.8,
            "creatinine": 1.7,
            "potassium": 5.4,
            "inr": 2.1,
            "alt": 129.8,
            "ast": 107.0
        },
        "diagnoses": [
            "gout",
            "nonalcoholic_steatohepatitis",
            "anemia"
        ],
        "medications": [
            "amiodarone",
            "diclofenac",
            "digoxin",
            "diltiazem",
            "ferrous_sulfate",
            "metronidazole",
            "simvastatin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0144-1",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-M-0144-2",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0144-3",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0145",
        "age": 83,
        "labs": {
            "egfr": 46.5,
            "creatinine": 1.1,
            "potassium": 5.1,
            "inr": 2.0
        },
        "diagnoses": [
            "chronic_liver_disease",
            "anxiety",
            "dyslipidemia"
        ],
        "medications": [
            "azithromycin",
            "diclofenac",
            "diltiazem",
            "nitroglycerin",
            "omeprazole",
            "prednisone",
            "simvastatin",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0145-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0145-2",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            },
            {
                "interaction_id": "INT-SYN-M-0145-3",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-M-0145-4",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0146",
        "age": 85,
        "labs": {
            "egfr": 46.5,
            "creatinine": 1.4,
            "potassium": 5.0,
            "inr": 2.4
        },
        "diagnoses": [
            "chronic_liver_disease",
            "anemia",
            "hypothyroidism",
            "atrial_fibrillation"
        ],
        "medications": [
            "allopurinol",
            "amlodipine",
            "aspirin",
            "citalopram",
            "clarithromycin",
            "metronidazole",
            "sertraline",
            "simvastatin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0146-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0146-2",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-M-0146-3",
                "drug_a": "aspirin",
                "drug_b": "sertraline",
                "severity": "minor",
                "evidence": "increased bleeding tendency, amplified in frailty"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0147",
        "age": 88,
        "labs": {
            "egfr": 86.6,
            "creatinine": 1.8,
            "potassium": 5.2,
            "inr": 2.5,
            "alt": 124.2,
            "ast": 100.4
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "type_2_diabetes"
        ],
        "medications": [
            "apixaban",
            "clarithromycin",
            "diclofenac",
            "ferrous_sulfate",
            "fluconazole",
            "levothyroxine",
            "linezolid",
            "losartan",
            "sertraline",
            "simvastatin",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0147-1",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-M-0147-2",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            },
            {
                "interaction_id": "INT-SYN-M-0147-3",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0147-4",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0148",
        "age": 87,
        "labs": {
            "egfr": 34.1,
            "creatinine": 1.3,
            "potassium": 5.0,
            "inr": 1.7,
            "alt": 111.9,
            "ast": 102.3
        },
        "diagnoses": [
            "hypertension",
            "chronic_kidney_disease"
        ],
        "medications": [
            "atorvastatin",
            "clopidogrel",
            "diclofenac",
            "diltiazem",
            "fluconazole",
            "metoprolol",
            "paroxetine",
            "simvastatin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0148-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0148-2",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-M-0148-3",
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
        "case_id": "SYN-M-0149",
        "age": 75,
        "labs": {
            "egfr": 30.6,
            "creatinine": 2.0,
            "potassium": 4.9,
            "inr": 2.4
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "nonalcoholic_steatohepatitis",
            "type_2_diabetes"
        ],
        "medications": [
            "amiodarone",
            "cetirizine",
            "dabigatran",
            "ketoconazole",
            "linezolid",
            "sertraline",
            "spironolactone",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0149-1",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0149-2",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-M-0149-3",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0150",
        "age": 88,
        "labs": {
            "egfr": 43.2,
            "creatinine": 1.2,
            "potassium": 5.0,
            "inr": 2.2
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "chronic_liver_disease",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "amlodipine",
            "cetirizine",
            "clopidogrel",
            "digoxin",
            "isosorbide_mononitrate",
            "omeprazole",
            "simvastatin",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0150-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-M-0150-2",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-M-0150-3",
                "drug_a": "digoxin",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "P-gp inhibition can raise digoxin concentration"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0151",
        "age": 91,
        "labs": {
            "egfr": 70.4,
            "creatinine": 2.0,
            "potassium": 5.2,
            "inr": 2.5,
            "alt": 123.9,
            "ast": 122.8
        },
        "diagnoses": [
            "heart_failure",
            "dyslipidemia",
            "anemia",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "ibuprofen",
            "isosorbide_mononitrate",
            "lisinopril",
            "metformin",
            "prednisone",
            "rivaroxaban",
            "sildenafil",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0151-1",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-M-0151-2",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0151-3",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0152",
        "age": 79,
        "labs": {
            "egfr": 87.0,
            "creatinine": 1.9,
            "potassium": 4.9,
            "inr": 2.4
        },
        "diagnoses": [
            "chronic_liver_disease",
            "chronic_pain",
            "anxiety",
            "hypertension"
        ],
        "medications": [
            "allopurinol",
            "amiodarone",
            "dabigatran",
            "ketoconazole",
            "nitroglycerin",
            "sertraline",
            "sildenafil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0152-1",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0152-2",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0152-3",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0153",
        "age": 75,
        "labs": {
            "egfr": 77.0,
            "creatinine": 1.2,
            "potassium": 5.0,
            "inr": 3.0
        },
        "diagnoses": [
            "type_2_diabetes",
            "chronic_kidney_disease",
            "chronic_pain",
            "peripheral_artery_disease"
        ],
        "medications": [
            "glipizide",
            "losartan",
            "metoprolol",
            "nitroglycerin",
            "spironolactone",
            "ticagrelor",
            "trimethoprim_sulfamethoxazole",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0153-1",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0153-2",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            },
            {
                "interaction_id": "INT-SYN-M-0153-3",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0154",
        "age": 88,
        "labs": {
            "egfr": 31.9,
            "creatinine": 1.5,
            "potassium": 4.8,
            "inr": 2.4
        },
        "diagnoses": [
            "anemia",
            "atrial_fibrillation"
        ],
        "medications": [
            "allopurinol",
            "amiodarone",
            "ciprofloxacin",
            "digoxin",
            "fluconazole",
            "nitroglycerin",
            "omeprazole",
            "sildenafil",
            "ticagrelor",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0154-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0154-2",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            },
            {
                "interaction_id": "INT-SYN-M-0154-3",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-M-0154-4",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0155",
        "age": 95,
        "labs": {
            "egfr": 85.1,
            "creatinine": 1.5,
            "potassium": 5.0,
            "inr": 2.9
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "anemia",
            "gout",
            "chronic_pain"
        ],
        "medications": [
            "allopurinol",
            "amiodarone",
            "apixaban",
            "ciprofloxacin",
            "clarithromycin",
            "diclofenac",
            "losartan",
            "metronidazole",
            "spironolactone",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0155-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0155-2",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0155-3",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            },
            {
                "interaction_id": "INT-SYN-M-0155-4",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0156",
        "age": 78,
        "labs": {
            "egfr": 61.3,
            "creatinine": 2.2,
            "potassium": 5.4,
            "inr": 2.1,
            "alt": 125.7,
            "ast": 122.7
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "depression",
            "hypothyroidism",
            "osteoarthritis"
        ],
        "medications": [
            "atorvastatin",
            "clopidogrel",
            "diltiazem",
            "fluconazole",
            "furosemide",
            "linezolid",
            "omeprazole",
            "sertraline",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0156-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-M-0156-2",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-M-0156-3",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0156-4",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "CYP3A4 inhibition raises statin concentration"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0157",
        "age": 85,
        "labs": {
            "egfr": 89.9,
            "creatinine": 1.9,
            "potassium": 4.7,
            "inr": 2.8
        },
        "diagnoses": [
            "type_2_diabetes",
            "osteoarthritis"
        ],
        "medications": [
            "amiodarone",
            "linezolid",
            "metoprolol",
            "naproxen",
            "rivaroxaban",
            "sertraline",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0157-1",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-M-0157-2",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0157-3",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0158",
        "age": 89,
        "labs": {
            "egfr": 44.9,
            "creatinine": 2.0,
            "potassium": 5.0,
            "inr": 1.7
        },
        "diagnoses": [
            "hypertension",
            "atrial_fibrillation",
            "coronary_artery_disease"
        ],
        "medications": [
            "apixaban",
            "clarithromycin",
            "dabigatran",
            "metoprolol",
            "naproxen",
            "paroxetine",
            "rivaroxaban",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0158-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0158-2",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-0158-3",
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
        "case_id": "SYN-M-0159",
        "age": 91,
        "labs": {
            "egfr": 42.9,
            "creatinine": 2.2,
            "potassium": 4.8,
            "inr": 1.8,
            "alt": 122.1,
            "ast": 100.1
        },
        "diagnoses": [
            "nonalcoholic_steatohepatitis",
            "heart_failure"
        ],
        "medications": [
            "amlodipine",
            "atorvastatin",
            "azithromycin",
            "cetirizine",
            "diclofenac",
            "ferrous_sulfate",
            "glipizide",
            "isosorbide_mononitrate",
            "levothyroxine",
            "sildenafil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0159-1",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-M-0159-2",
                "drug_a": "cetirizine",
                "drug_b": "amlodipine",
                "severity": "minor",
                "evidence": "possible additive sedation in elderly"
            },
            {
                "interaction_id": "INT-SYN-M-0159-3",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-M-0159-4",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-0160",
        "age": 75,
        "labs": {
            "egfr": 44.5,
            "creatinine": 1.4,
            "potassium": 4.9,
            "inr": 1.9
        },
        "diagnoses": [
            "depression",
            "hypothyroidism",
            "chronic_kidney_disease"
        ],
        "medications": [
            "azithromycin",
            "clopidogrel",
            "dabigatran",
            "digoxin",
            "ketoconazole",
            "losartan",
            "nitroglycerin",
            "prednisone",
            "sildenafil",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-0160-1",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-M-0160-2",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            },
            {
                "interaction_id": "INT-SYN-M-0160-3",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            },
            {
                "interaction_id": "INT-SYN-M-0160-4",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-M-V0001",
        "age": 92,
        "labs": {
            "egfr": 33.8,
            "creatinine": 1.9,
            "potassium": 4.8,
            "inr": 2.5,
            "alt": 123.3,
            "ast": 121.4
        },
        "diagnoses": [
            "atrial_fibrillation",
            "coronary_artery_disease",
            "chronic_pain",
            "gout"
        ],
        "medications": [
            "allopurinol",
            "apixaban",
            "aspirin",
            "diclofenac",
            "fluconazole",
            "sertraline",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-V0001-1",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0001-2",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0001-3",
                "drug_a": "aspirin",
                "drug_b": "sertraline",
                "severity": "minor",
                "evidence": "increased bleeding tendency, amplified in frailty"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::medium-SYN-M-V0001"
    },
    {
        "case_id": "SYN-M-V0002",
        "age": 85,
        "labs": {
            "egfr": 41.0,
            "creatinine": 1.9,
            "potassium": 4.6,
            "inr": 2.3,
            "alt": 117.6,
            "ast": 114.8
        },
        "diagnoses": [
            "nonalcoholic_steatohepatitis",
            "hypothyroidism",
            "gout",
            "type_2_diabetes"
        ],
        "medications": [
            "aspirin",
            "azithromycin",
            "clopidogrel",
            "losartan",
            "omeprazole",
            "prednisone",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-V0002-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-M-V0002-2",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            },
            {
                "interaction_id": "INT-SYN-M-V0002-3",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::medium-SYN-M-V0002"
    },
    {
        "case_id": "SYN-M-V0003",
        "age": 75,
        "labs": {
            "egfr": 39.9,
            "creatinine": 1.6,
            "potassium": 4.7,
            "inr": 2.6
        },
        "diagnoses": [
            "nonalcoholic_steatohepatitis",
            "chronic_pain",
            "heart_failure",
            "hypertension"
        ],
        "medications": [
            "allopurinol",
            "amlodipine",
            "diclofenac",
            "furosemide",
            "metoprolol",
            "naproxen",
            "nitroglycerin",
            "sildenafil",
            "simvastatin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-V0003-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0003-2",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-M-V0003-3",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-M-V0003-4",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::medium-SYN-M-V0003"
    },
    {
        "case_id": "SYN-M-V0004",
        "age": 92,
        "labs": {
            "egfr": 60.1,
            "creatinine": 1.7,
            "potassium": 4.6,
            "inr": 1.6
        },
        "diagnoses": [
            "hypothyroidism",
            "chronic_kidney_disease",
            "chronic_pain",
            "gout"
        ],
        "medications": [
            "cetirizine",
            "ciprofloxacin",
            "dabigatran",
            "diltiazem",
            "linezolid",
            "naproxen",
            "rivaroxaban",
            "sertraline",
            "simvastatin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-V0004-1",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0004-2",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0004-3",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::medium-SYN-M-V0004"
    },
    {
        "case_id": "SYN-M-V0005",
        "age": 78,
        "labs": {
            "egfr": 78.3,
            "creatinine": 2.3,
            "potassium": 5.1,
            "inr": 2.2,
            "alt": 126.9,
            "ast": 112.1
        },
        "diagnoses": [
            "chronic_pain",
            "coronary_artery_disease",
            "hypothyroidism",
            "dyslipidemia"
        ],
        "medications": [
            "allopurinol",
            "amlodipine",
            "aspirin",
            "losartan",
            "simvastatin",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-V0005-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0005-2",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            },
            {
                "interaction_id": "INT-SYN-M-V0005-3",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::medium-SYN-M-V0005"
    },
    {
        "case_id": "SYN-M-V0006",
        "age": 85,
        "labs": {
            "egfr": 44.9,
            "creatinine": 2.2,
            "potassium": 4.7,
            "inr": 2.4,
            "alt": 116.8,
            "ast": 110.2
        },
        "diagnoses": [
            "gout",
            "osteoarthritis",
            "depression"
        ],
        "medications": [
            "amiodarone",
            "amlodipine",
            "digoxin",
            "losartan",
            "simvastatin",
            "spironolactone",
            "valsartan",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-V0006-1",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-M-V0006-2",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0006-3",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            },
            {
                "interaction_id": "INT-SYN-M-V0006-4",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::medium-SYN-M-V0006"
    },
    {
        "case_id": "SYN-M-V0007",
        "age": 94,
        "labs": {
            "egfr": 44.5,
            "creatinine": 1.3,
            "potassium": 5.3,
            "inr": 2.7,
            "alt": 118.3,
            "ast": 117.3
        },
        "diagnoses": [
            "anemia",
            "depression",
            "dyslipidemia",
            "gout"
        ],
        "medications": [
            "diltiazem",
            "furosemide",
            "isosorbide_mononitrate",
            "losartan",
            "metoprolol",
            "rivaroxaban",
            "sildenafil",
            "simvastatin",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-V0007-1",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-M-V0007-2",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0007-3",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-M-V0007-4",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::medium-SYN-M-V0007"
    },
    {
        "case_id": "SYN-M-V0008",
        "age": 75,
        "labs": {
            "egfr": 47.6,
            "creatinine": 1.7,
            "potassium": 5.3,
            "inr": 2.0
        },
        "diagnoses": [
            "anemia",
            "chronic_kidney_disease",
            "dyslipidemia",
            "peripheral_artery_disease"
        ],
        "medications": [
            "azithromycin",
            "calcium_carbonate",
            "citalopram",
            "furosemide",
            "isosorbide_mononitrate",
            "sildenafil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-V0008-1",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0008-2",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-M-V0008-3",
                "drug_a": "furosemide",
                "drug_b": "warfarin",
                "severity": "minor",
                "evidence": "volume changes may alter INR stability"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::medium-SYN-M-V0008"
    },
    {
        "case_id": "SYN-M-V0009",
        "age": 76,
        "labs": {
            "egfr": 28.3,
            "creatinine": 2.0,
            "potassium": 5.4,
            "inr": 2.9,
            "alt": 120.3,
            "ast": 116.2
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "type_2_diabetes",
            "osteoarthritis",
            "chronic_liver_disease"
        ],
        "medications": [
            "amlodipine",
            "aspirin",
            "clarithromycin",
            "dabigatran",
            "ketoconazole",
            "nitroglycerin",
            "sertraline",
            "sildenafil",
            "simvastatin",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-V0009-1",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-M-V0009-2",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0009-3",
                "drug_a": "aspirin",
                "drug_b": "sertraline",
                "severity": "minor",
                "evidence": "increased bleeding tendency, amplified in frailty"
            },
            {
                "interaction_id": "INT-SYN-M-V0009-4",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::medium-SYN-M-V0009"
    },
    {
        "case_id": "SYN-M-V0010",
        "age": 79,
        "labs": {
            "egfr": 32.3,
            "creatinine": 2.4,
            "potassium": 5.2,
            "inr": 1.8
        },
        "diagnoses": [
            "type_2_diabetes",
            "hypertension"
        ],
        "medications": [
            "apixaban",
            "aspirin",
            "cetirizine",
            "diclofenac",
            "losartan",
            "metronidazole",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-V0010-1",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0010-2",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            },
            {
                "interaction_id": "INT-SYN-M-V0010-3",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::medium-SYN-M-V0010"
    },
    {
        "case_id": "SYN-M-V0011",
        "age": 76,
        "labs": {
            "egfr": 44.1,
            "creatinine": 2.5,
            "potassium": 5.1,
            "inr": 2.5
        },
        "diagnoses": [
            "osteoarthritis",
            "chronic_kidney_disease",
            "depression"
        ],
        "medications": [
            "aspirin",
            "atorvastatin",
            "digoxin",
            "diltiazem",
            "metronidazole",
            "nitroglycerin",
            "sertraline",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-V0011-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0011-2",
                "drug_a": "digoxin",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "P-gp inhibition can raise digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-M-V0011-3",
                "drug_a": "aspirin",
                "drug_b": "sertraline",
                "severity": "minor",
                "evidence": "increased bleeding tendency, amplified in frailty"
            },
            {
                "interaction_id": "INT-SYN-M-V0011-4",
                "drug_a": "atorvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "CYP3A4 inhibition raises statin concentration"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::medium-SYN-M-V0011"
    },
    {
        "case_id": "SYN-M-V0012",
        "age": 86,
        "labs": {
            "egfr": 27.9,
            "creatinine": 2.3,
            "potassium": 4.7,
            "inr": 1.6,
            "alt": 122.4,
            "ast": 117.3
        },
        "diagnoses": [
            "heart_failure",
            "osteoarthritis",
            "anemia",
            "anxiety"
        ],
        "medications": [
            "citalopram",
            "ibuprofen",
            "levothyroxine",
            "lisinopril",
            "losartan",
            "nitroglycerin",
            "sildenafil",
            "spironolactone",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-V0012-1",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0012-2",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-M-V0012-3",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            },
            {
                "interaction_id": "INT-SYN-M-V0012-4",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::medium-SYN-M-V0012"
    },
    {
        "case_id": "SYN-M-V0013",
        "age": 81,
        "labs": {
            "egfr": 43.8,
            "creatinine": 1.3,
            "potassium": 4.8,
            "inr": 2.7,
            "alt": 110.8,
            "ast": 123.6
        },
        "diagnoses": [
            "type_2_diabetes",
            "atrial_fibrillation"
        ],
        "medications": [
            "amiodarone",
            "apixaban",
            "azithromycin",
            "citalopram",
            "diltiazem",
            "naproxen",
            "nitroglycerin",
            "omeprazole",
            "sildenafil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-V0013-1",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-M-V0013-2",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0013-3",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::medium-SYN-M-V0013"
    },
    {
        "case_id": "SYN-M-V0014",
        "age": 87,
        "labs": {
            "egfr": 27.4,
            "creatinine": 1.4,
            "potassium": 4.6,
            "inr": 1.5,
            "alt": 125.3,
            "ast": 111.4
        },
        "diagnoses": [
            "gout",
            "osteoarthritis",
            "anemia"
        ],
        "medications": [
            "calcium_carbonate",
            "ciprofloxacin",
            "citalopram",
            "clopidogrel",
            "furosemide",
            "levothyroxine",
            "metoprolol",
            "nitroglycerin",
            "omeprazole",
            "paroxetine",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-V0014-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-M-V0014-2",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-M-V0014-3",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            },
            {
                "interaction_id": "INT-SYN-M-V0014-4",
                "drug_a": "metoprolol",
                "drug_b": "paroxetine",
                "severity": "moderate",
                "evidence": "CYP2D6 inhibition raises metoprolol exposure"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::medium-SYN-M-V0014"
    },
    {
        "case_id": "SYN-M-V0015",
        "age": 86,
        "labs": {
            "egfr": 42.2,
            "creatinine": 2.1,
            "potassium": 4.7,
            "inr": 2.9,
            "alt": 111.1,
            "ast": 122.3
        },
        "diagnoses": [
            "heart_failure",
            "osteoarthritis",
            "anemia",
            "depression"
        ],
        "medications": [
            "amiodarone",
            "atorvastatin",
            "azithromycin",
            "citalopram",
            "clopidogrel",
            "digoxin",
            "lisinopril",
            "omeprazole",
            "paroxetine",
            "spironolactone"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-V0015-1",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0015-2",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            },
            {
                "interaction_id": "INT-SYN-M-V0015-3",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-M-V0015-4",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::medium-SYN-M-V0015"
    },
    {
        "case_id": "SYN-M-V0016",
        "age": 93,
        "labs": {
            "egfr": 71.3,
            "creatinine": 2.0,
            "potassium": 5.3,
            "inr": 2.7,
            "alt": 116.6,
            "ast": 116.5
        },
        "diagnoses": [
            "atrial_fibrillation",
            "hypertension"
        ],
        "medications": [
            "diclofenac",
            "isosorbide_mononitrate",
            "metoprolol",
            "metronidazole",
            "paroxetine",
            "sildenafil",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-V0016-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0016-2",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-M-V0016-3",
                "drug_a": "metoprolol",
                "drug_b": "paroxetine",
                "severity": "moderate",
                "evidence": "CYP2D6 inhibition raises metoprolol exposure"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::medium-SYN-M-V0016"
    },
    {
        "case_id": "SYN-M-V0017",
        "age": 75,
        "labs": {
            "egfr": 84.5,
            "creatinine": 1.9,
            "potassium": 4.6,
            "inr": 2.8
        },
        "diagnoses": [
            "coronary_artery_disease",
            "hypothyroidism",
            "anxiety",
            "anemia"
        ],
        "medications": [
            "amiodarone",
            "calcium_carbonate",
            "ciprofloxacin",
            "levothyroxine",
            "lisinopril",
            "simvastatin",
            "spironolactone",
            "trimethoprim_sulfamethoxazole",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-V0017-1",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0017-2",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            },
            {
                "interaction_id": "INT-SYN-M-V0017-3",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            },
            {
                "interaction_id": "INT-SYN-M-V0017-4",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::medium-SYN-M-V0017"
    },
    {
        "case_id": "SYN-M-V0018",
        "age": 83,
        "labs": {
            "egfr": 27.8,
            "creatinine": 2.3,
            "potassium": 5.5,
            "inr": 2.1
        },
        "diagnoses": [
            "chronic_liver_disease",
            "dyslipidemia"
        ],
        "medications": [
            "amiodarone",
            "atorvastatin",
            "calcium_carbonate",
            "digoxin",
            "fluconazole",
            "levothyroxine",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-V0018-1",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-M-V0018-2",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0018-3",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::medium-SYN-M-V0018"
    },
    {
        "case_id": "SYN-M-V0019",
        "age": 76,
        "labs": {
            "egfr": 43.9,
            "creatinine": 1.0,
            "potassium": 4.6,
            "inr": 1.6
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "heart_failure",
            "type_2_diabetes"
        ],
        "medications": [
            "clopidogrel",
            "diltiazem",
            "fluconazole",
            "metoprolol",
            "omeprazole",
            "paroxetine",
            "prednisone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-V0019-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0019-2",
                "drug_a": "metoprolol",
                "drug_b": "paroxetine",
                "severity": "moderate",
                "evidence": "CYP2D6 inhibition raises metoprolol exposure"
            },
            {
                "interaction_id": "INT-SYN-M-V0019-3",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::medium-SYN-M-V0019"
    },
    {
        "case_id": "SYN-M-V0020",
        "age": 82,
        "labs": {
            "egfr": 45.3,
            "creatinine": 1.4,
            "potassium": 4.8,
            "inr": 1.9,
            "alt": 115.1,
            "ast": 116.8
        },
        "diagnoses": [
            "coronary_artery_disease",
            "atrial_fibrillation"
        ],
        "medications": [
            "amiodarone",
            "amlodipine",
            "apixaban",
            "aspirin",
            "cetirizine",
            "diclofenac",
            "digoxin",
            "ketoconazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-V0020-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0020-2",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0020-3",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-M-V0020-4",
                "drug_a": "cetirizine",
                "drug_b": "amlodipine",
                "severity": "minor",
                "evidence": "possible additive sedation in elderly"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::medium-SYN-M-V0020"
    },
    {
        "case_id": "SYN-M-V0021",
        "age": 78,
        "labs": {
            "egfr": 32.4,
            "creatinine": 1.3,
            "potassium": 4.9,
            "inr": 2.3
        },
        "diagnoses": [
            "gout",
            "chronic_liver_disease",
            "anemia"
        ],
        "medications": [
            "amlodipine",
            "cetirizine",
            "clopidogrel",
            "fluconazole",
            "metformin",
            "metoprolol",
            "omeprazole",
            "paroxetine",
            "sertraline",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-V0021-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-M-V0021-2",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0021-3",
                "drug_a": "metoprolol",
                "drug_b": "paroxetine",
                "severity": "moderate",
                "evidence": "CYP2D6 inhibition raises metoprolol exposure"
            },
            {
                "interaction_id": "INT-SYN-M-V0021-4",
                "drug_a": "cetirizine",
                "drug_b": "amlodipine",
                "severity": "minor",
                "evidence": "possible additive sedation in elderly"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::medium-SYN-M-V0021"
    },
    {
        "case_id": "SYN-M-V0022",
        "age": 85,
        "labs": {
            "egfr": 43.3,
            "creatinine": 1.4,
            "potassium": 4.9,
            "inr": 2.6,
            "alt": 129.7,
            "ast": 106.9
        },
        "diagnoses": [
            "gout",
            "coronary_artery_disease"
        ],
        "medications": [
            "ciprofloxacin",
            "furosemide",
            "ibuprofen",
            "metformin",
            "metoprolol",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-V0022-1",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0022-2",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-M-V0022-3",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::medium-SYN-M-V0022"
    },
    {
        "case_id": "SYN-M-V0023",
        "age": 75,
        "labs": {
            "egfr": 80.6,
            "creatinine": 1.9,
            "potassium": 5.3,
            "inr": 2.9
        },
        "diagnoses": [
            "hypothyroidism",
            "hypertension",
            "depression",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "amiodarone",
            "clopidogrel",
            "lisinopril",
            "losartan",
            "metoprolol",
            "omeprazole",
            "sertraline",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-V0023-1",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-M-V0023-2",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            },
            {
                "interaction_id": "INT-SYN-M-V0023-3",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::medium-SYN-M-V0023"
    },
    {
        "case_id": "SYN-M-V0024",
        "age": 87,
        "labs": {
            "egfr": 75.2,
            "creatinine": 1.7,
            "potassium": 4.8,
            "inr": 2.7,
            "alt": 114.5,
            "ast": 116.8
        },
        "diagnoses": [
            "osteoarthritis",
            "anemia"
        ],
        "medications": [
            "apixaban",
            "clarithromycin",
            "fluconazole",
            "furosemide",
            "linezolid",
            "metformin",
            "prednisone",
            "sertraline",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-V0024-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0024-2",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0024-3",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0024-4",
                "drug_a": "metformin",
                "drug_b": "furosemide",
                "severity": "moderate",
                "evidence": "reduced renal clearance can increase lactic acidosis risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::medium-SYN-M-V0024"
    },
    {
        "case_id": "SYN-M-V0025",
        "age": 85,
        "labs": {
            "egfr": 43.9,
            "creatinine": 1.3,
            "potassium": 5.2,
            "inr": 1.9
        },
        "diagnoses": [
            "chronic_liver_disease",
            "hypertension",
            "atrial_fibrillation",
            "osteoarthritis"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "fluconazole",
            "losartan",
            "naproxen",
            "ticagrelor",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-V0025-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0025-2",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0025-3",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::medium-SYN-M-V0025"
    },
    {
        "case_id": "SYN-M-V0026",
        "age": 91,
        "labs": {
            "egfr": 41.9,
            "creatinine": 2.0,
            "potassium": 5.0,
            "inr": 2.5
        },
        "diagnoses": [
            "coronary_artery_disease",
            "heart_failure",
            "type_2_diabetes"
        ],
        "medications": [
            "furosemide",
            "ketoconazole",
            "linezolid",
            "metoprolol",
            "paroxetine",
            "sertraline",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-V0026-1",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0026-2",
                "drug_a": "metoprolol",
                "drug_b": "paroxetine",
                "severity": "moderate",
                "evidence": "CYP2D6 inhibition raises metoprolol exposure"
            },
            {
                "interaction_id": "INT-SYN-M-V0026-3",
                "drug_a": "furosemide",
                "drug_b": "warfarin",
                "severity": "minor",
                "evidence": "volume changes may alter INR stability"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::medium-SYN-M-V0026"
    },
    {
        "case_id": "SYN-M-V0027",
        "age": 87,
        "labs": {
            "egfr": 44.5,
            "creatinine": 1.0,
            "potassium": 4.9,
            "inr": 2.6
        },
        "diagnoses": [
            "gout",
            "chronic_liver_disease"
        ],
        "medications": [
            "apixaban",
            "azithromycin",
            "clarithromycin",
            "digoxin",
            "diltiazem",
            "furosemide",
            "metoprolol",
            "metronidazole",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-V0027-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0027-2",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-M-V0027-3",
                "drug_a": "digoxin",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "P-gp inhibition can raise digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-M-V0027-4",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::medium-SYN-M-V0027"
    },
    {
        "case_id": "SYN-M-V0028",
        "age": 88,
        "labs": {
            "egfr": 62.2,
            "creatinine": 1.7,
            "potassium": 5.2,
            "inr": 1.5
        },
        "diagnoses": [
            "anemia",
            "hypertension",
            "chronic_liver_disease",
            "gout"
        ],
        "medications": [
            "amiodarone",
            "apixaban",
            "citalopram",
            "diclofenac",
            "digoxin",
            "losartan",
            "metoprolol",
            "paroxetine",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-V0028-1",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0028-2",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-M-V0028-3",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            },
            {
                "interaction_id": "INT-SYN-M-V0028-4",
                "drug_a": "metoprolol",
                "drug_b": "paroxetine",
                "severity": "moderate",
                "evidence": "CYP2D6 inhibition raises metoprolol exposure"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::medium-SYN-M-V0028"
    },
    {
        "case_id": "SYN-M-V0029",
        "age": 75,
        "labs": {
            "egfr": 42.9,
            "creatinine": 1.9,
            "potassium": 4.5,
            "inr": 1.6,
            "alt": 123.3,
            "ast": 114.1
        },
        "diagnoses": [
            "nonalcoholic_steatohepatitis",
            "type_2_diabetes",
            "heart_failure",
            "anxiety"
        ],
        "medications": [
            "amiodarone",
            "clarithromycin",
            "digoxin",
            "fluconazole",
            "ibuprofen",
            "ketoconazole",
            "losartan",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-V0029-1",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0029-2",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            },
            {
                "interaction_id": "INT-SYN-M-V0029-3",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::medium-SYN-M-V0029"
    },
    {
        "case_id": "SYN-M-V0030",
        "age": 82,
        "labs": {
            "egfr": 68.5,
            "creatinine": 1.6,
            "potassium": 4.8,
            "inr": 2.4,
            "alt": 110.9,
            "ast": 108.9
        },
        "diagnoses": [
            "osteoarthritis",
            "gout",
            "depression",
            "heart_failure"
        ],
        "medications": [
            "amiodarone",
            "azithromycin",
            "citalopram",
            "clopidogrel",
            "digoxin",
            "diltiazem",
            "linezolid",
            "sertraline",
            "simvastatin",
            "ticagrelor"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-M-V0030-1",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0030-2",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-M-V0030-3",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-M-V0030-4",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::medium-SYN-M-V0030"
    }
]

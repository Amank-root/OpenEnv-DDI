"""Synthetic DDI cases for the easy task level."""

from typing import Any, Dict, List

Case = Dict[str, Any]

SYNTHETIC_EASY_CASES: List[Case] = [
    {
        "case_id": "SYN-E-0001",
        "age": 58,
        "labs": {
            "egfr": 60.8,
            "creatinine": 1.0,
            "potassium": 3.9,
            "inr": 2.6
        },
        "diagnoses": [
            "hypertension",
            "hypothyroidism"
        ],
        "medications": [
            "allopurinol",
            "digoxin",
            "fluconazole",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0001-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0001-2",
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
        "case_id": "SYN-E-0002",
        "age": 65,
        "labs": {
            "egfr": 66.4,
            "creatinine": 1.3,
            "potassium": 4.3,
            "inr": 1.8
        },
        "diagnoses": [
            "chronic_pain",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "apixaban",
            "clarithromycin",
            "diltiazem",
            "furosemide",
            "naproxen",
            "rivaroxaban",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0002-1",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0002-2",
                "drug_a": "furosemide",
                "drug_b": "warfarin",
                "severity": "minor",
                "evidence": "volume changes may alter INR stability"
            },
            {
                "interaction_id": "INT-SYN-E-0002-3",
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
        "case_id": "SYN-E-0003",
        "age": 69,
        "labs": {
            "egfr": 63.6,
            "creatinine": 1.3,
            "potassium": 4.3,
            "inr": 2.0
        },
        "diagnoses": [
            "chronic_pain",
            "coronary_artery_disease"
        ],
        "medications": [
            "aspirin",
            "metoprolol",
            "paroxetine",
            "simvastatin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0003-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0003-2",
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
        "case_id": "SYN-E-0004",
        "age": 65,
        "labs": {
            "egfr": 61.7,
            "creatinine": 1.2,
            "potassium": 4.2,
            "inr": 1.8
        },
        "diagnoses": [
            "osteoarthritis",
            "dyslipidemia"
        ],
        "medications": [
            "amiodarone",
            "apixaban",
            "clarithromycin",
            "clopidogrel",
            "digoxin",
            "omeprazole"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0004-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0004-2",
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
        "case_id": "SYN-E-0005",
        "age": 58,
        "labs": {
            "egfr": 62.3,
            "creatinine": 0.8,
            "potassium": 4.3,
            "inr": 1.6
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "chronic_liver_disease"
        ],
        "medications": [
            "dabigatran",
            "diltiazem",
            "ketoconazole",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0005-1",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0005-2",
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
        "case_id": "SYN-E-0006",
        "age": 75,
        "labs": {
            "egfr": 81.6,
            "creatinine": 0.9,
            "potassium": 4.3,
            "inr": 2.4
        },
        "diagnoses": [
            "anxiety",
            "osteoarthritis",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "amiodarone",
            "digoxin",
            "linezolid",
            "metformin",
            "nitroglycerin",
            "sertraline",
            "sildenafil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0006-1",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-E-0006-2",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-E-0006-3",
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
        "case_id": "SYN-E-0007",
        "age": 70,
        "labs": {
            "egfr": 78.8,
            "creatinine": 1.3,
            "potassium": 3.8,
            "inr": 1.1
        },
        "diagnoses": [
            "depression",
            "type_2_diabetes",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "amlodipine",
            "cetirizine",
            "dabigatran",
            "metoprolol",
            "omeprazole",
            "ticagrelor",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0007-1",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-E-0007-2",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            },
            {
                "interaction_id": "INT-SYN-E-0007-3",
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
        "case_id": "SYN-E-0008",
        "age": 61,
        "labs": {
            "egfr": 85.2,
            "creatinine": 1.0,
            "potassium": 4.4,
            "inr": 2.2
        },
        "diagnoses": [
            "depression",
            "chronic_liver_disease"
        ],
        "medications": [
            "amiodarone",
            "amlodipine",
            "apixaban",
            "clarithromycin",
            "digoxin",
            "furosemide",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0008-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0008-2",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-E-0008-3",
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
        "case_id": "SYN-E-0009",
        "age": 70,
        "labs": {
            "egfr": 73.4,
            "creatinine": 1.1,
            "potassium": 4.1,
            "inr": 2.0
        },
        "diagnoses": [
            "anxiety",
            "chronic_pain",
            "chronic_liver_disease"
        ],
        "medications": [
            "apixaban",
            "cetirizine",
            "clarithromycin",
            "furosemide",
            "linezolid",
            "spironolactone",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0009-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0009-2",
                "drug_a": "furosemide",
                "drug_b": "warfarin",
                "severity": "minor",
                "evidence": "volume changes may alter INR stability"
            },
            {
                "interaction_id": "INT-SYN-E-0009-3",
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
        "case_id": "SYN-E-0010",
        "age": 74,
        "labs": {
            "egfr": 88.8,
            "creatinine": 1.1,
            "potassium": 4.1,
            "inr": 2.4
        },
        "diagnoses": [
            "chronic_liver_disease",
            "anemia",
            "heart_failure"
        ],
        "medications": [
            "apixaban",
            "clarithromycin",
            "furosemide",
            "metoprolol",
            "spironolactone"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0010-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0010-2",
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
        "case_id": "SYN-E-0011",
        "age": 69,
        "labs": {
            "egfr": 62.6,
            "creatinine": 1.0,
            "potassium": 4.5,
            "inr": 1.7
        },
        "diagnoses": [
            "hypertension",
            "hypothyroidism",
            "peripheral_artery_disease"
        ],
        "medications": [
            "apixaban",
            "diclofenac",
            "fluconazole",
            "furosemide",
            "metoprolol",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0011-1",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0011-2",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-E-0011-3",
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
        "case_id": "SYN-E-0012",
        "age": 59,
        "labs": {
            "egfr": 74.9,
            "creatinine": 1.0,
            "potassium": 4.6,
            "inr": 2.5
        },
        "diagnoses": [
            "osteoarthritis",
            "anxiety",
            "chronic_liver_disease"
        ],
        "medications": [
            "apixaban",
            "clarithromycin",
            "ibuprofen",
            "losartan",
            "simvastatin",
            "spironolactone",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0012-1",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0012-2",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            },
            {
                "interaction_id": "INT-SYN-E-0012-3",
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
        "case_id": "SYN-E-0013",
        "age": 62,
        "labs": {
            "egfr": 71.4,
            "creatinine": 1.1,
            "potassium": 3.9,
            "inr": 1.1
        },
        "diagnoses": [
            "anxiety",
            "chronic_pain"
        ],
        "medications": [
            "dabigatran",
            "ferrous_sulfate",
            "fluconazole",
            "levothyroxine",
            "linezolid",
            "sertraline",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0013-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0013-2",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-E-0013-3",
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
        "case_id": "SYN-E-0014",
        "age": 64,
        "labs": {
            "egfr": 89.9,
            "creatinine": 1.3,
            "potassium": 4.5,
            "inr": 1.8
        },
        "diagnoses": [
            "anxiety",
            "atrial_fibrillation",
            "anemia"
        ],
        "medications": [
            "amlodipine",
            "ciprofloxacin",
            "fluconazole",
            "omeprazole",
            "ticagrelor"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0014-1",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-E-0014-2",
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
        "case_id": "SYN-E-0015",
        "age": 70,
        "labs": {
            "egfr": 81.4,
            "creatinine": 1.2,
            "potassium": 4.0,
            "inr": 1.6
        },
        "diagnoses": [
            "dyslipidemia",
            "osteoarthritis"
        ],
        "medications": [
            "ciprofloxacin",
            "dabigatran",
            "diltiazem",
            "fluconazole",
            "furosemide",
            "metoprolol",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0015-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0015-2",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            },
            {
                "interaction_id": "INT-SYN-E-0015-3",
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
        "case_id": "SYN-E-0016",
        "age": 60,
        "labs": {
            "egfr": 86.1,
            "creatinine": 0.8,
            "potassium": 4.1,
            "inr": 2.4
        },
        "diagnoses": [
            "chronic_pain",
            "chronic_kidney_disease",
            "coronary_artery_disease"
        ],
        "medications": [
            "amiodarone",
            "diclofenac",
            "digoxin",
            "furosemide",
            "glipizide",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0016-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0016-2",
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
        "case_id": "SYN-E-0017",
        "age": 69,
        "labs": {
            "egfr": 85.0,
            "creatinine": 1.3,
            "potassium": 4.2,
            "inr": 2.1
        },
        "diagnoses": [
            "depression",
            "anxiety"
        ],
        "medications": [
            "apixaban",
            "clarithromycin",
            "ferrous_sulfate",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0017-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0017-2",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-E-0018",
        "age": 77,
        "labs": {
            "egfr": 87.5,
            "creatinine": 1.0,
            "potassium": 4.2,
            "inr": 2.7
        },
        "diagnoses": [
            "anxiety",
            "chronic_pain",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "allopurinol",
            "ketoconazole",
            "metronidazole",
            "nitroglycerin",
            "sildenafil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0018-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0018-2",
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
        "case_id": "SYN-E-0019",
        "age": 74,
        "labs": {
            "egfr": 64.2,
            "creatinine": 0.8,
            "potassium": 4.1,
            "inr": 1.7
        },
        "diagnoses": [
            "nonalcoholic_steatohepatitis",
            "anemia"
        ],
        "medications": [
            "azithromycin",
            "ciprofloxacin",
            "isosorbide_mononitrate",
            "omeprazole",
            "prednisone",
            "sildenafil",
            "ticagrelor"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0019-1",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-E-0019-2",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            },
            {
                "interaction_id": "INT-SYN-E-0019-3",
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
        "case_id": "SYN-E-0020",
        "age": 55,
        "labs": {
            "egfr": 70.7,
            "creatinine": 1.2,
            "potassium": 4.3,
            "inr": 1.8
        },
        "diagnoses": [
            "atrial_fibrillation",
            "heart_failure"
        ],
        "medications": [
            "amiodarone",
            "apixaban",
            "diclofenac",
            "naproxen",
            "rivaroxaban",
            "trimethoprim_sulfamethoxazole"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0020-1",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0020-2",
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
        "case_id": "SYN-E-0021",
        "age": 57,
        "labs": {
            "egfr": 67.1,
            "creatinine": 1.2,
            "potassium": 4.4,
            "inr": 2.2
        },
        "diagnoses": [
            "gout",
            "peripheral_artery_disease",
            "type_2_diabetes"
        ],
        "medications": [
            "atorvastatin",
            "fluconazole",
            "linezolid",
            "spironolactone",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0021-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0021-2",
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
        "case_id": "SYN-E-0022",
        "age": 59,
        "labs": {
            "egfr": 73.0,
            "creatinine": 1.3,
            "potassium": 4.2,
            "inr": 2.6
        },
        "diagnoses": [
            "coronary_artery_disease",
            "dyslipidemia",
            "depression"
        ],
        "medications": [
            "atorvastatin",
            "fluconazole",
            "furosemide",
            "metoprolol",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0022-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0022-2",
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
        "case_id": "SYN-E-0023",
        "age": 75,
        "labs": {
            "egfr": 62.7,
            "creatinine": 1.2,
            "potassium": 4.4,
            "inr": 2.2
        },
        "diagnoses": [
            "chronic_liver_disease",
            "chronic_pain"
        ],
        "medications": [
            "apixaban",
            "calcium_carbonate",
            "clarithromycin",
            "diltiazem",
            "omeprazole",
            "simvastatin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0023-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0023-2",
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
        "case_id": "SYN-E-0024",
        "age": 74,
        "labs": {
            "egfr": 74.2,
            "creatinine": 0.8,
            "potassium": 4.5,
            "inr": 1.4
        },
        "diagnoses": [
            "depression",
            "gout"
        ],
        "medications": [
            "amiodarone",
            "digoxin",
            "furosemide",
            "metformin",
            "spironolactone"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0024-1",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-E-0024-2",
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
        "case_id": "SYN-E-0025",
        "age": 56,
        "labs": {
            "egfr": 63.0,
            "creatinine": 1.0,
            "potassium": 4.1,
            "inr": 1.9
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "anxiety"
        ],
        "medications": [
            "amiodarone",
            "diclofenac",
            "digoxin",
            "sildenafil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0025-1",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-E-0025-2",
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
        "case_id": "SYN-E-0026",
        "age": 64,
        "labs": {
            "egfr": 80.7,
            "creatinine": 0.8,
            "potassium": 4.6,
            "inr": 2.6
        },
        "diagnoses": [
            "anxiety",
            "nonalcoholic_steatohepatitis",
            "coronary_artery_disease"
        ],
        "medications": [
            "aspirin",
            "ciprofloxacin",
            "ferrous_sulfate",
            "glipizide",
            "naproxen",
            "rivaroxaban",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0026-1",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0026-2",
                "drug_a": "glipizide",
                "drug_b": "ciprofloxacin",
                "severity": "moderate",
                "evidence": "dysglycemia risk from fluoroquinolone-sulfonylurea combination"
            },
            {
                "interaction_id": "INT-SYN-E-0026-3",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-E-0027",
        "age": 66,
        "labs": {
            "egfr": 63.6,
            "creatinine": 0.9,
            "potassium": 4.0,
            "inr": 2.2
        },
        "diagnoses": [
            "gout",
            "heart_failure",
            "coronary_artery_disease"
        ],
        "medications": [
            "allopurinol",
            "calcium_carbonate",
            "levothyroxine",
            "metronidazole",
            "sertraline",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0027-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0027-2",
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
        "case_id": "SYN-E-0028",
        "age": 77,
        "labs": {
            "egfr": 62.8,
            "creatinine": 1.2,
            "potassium": 3.9,
            "inr": 2.5
        },
        "diagnoses": [
            "gout",
            "hypertension"
        ],
        "medications": [
            "allopurinol",
            "amiodarone",
            "digoxin",
            "metronidazole",
            "naproxen",
            "rivaroxaban",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0028-1",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-E-0028-2",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0028-3",
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
        "case_id": "SYN-E-0029",
        "age": 55,
        "labs": {
            "egfr": 72.4,
            "creatinine": 1.1,
            "potassium": 4.3,
            "inr": 2.5
        },
        "diagnoses": [
            "chronic_pain",
            "dyslipidemia"
        ],
        "medications": [
            "clarithromycin",
            "ketoconazole",
            "omeprazole",
            "ticagrelor",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0029-1",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0029-2",
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
        "case_id": "SYN-E-0030",
        "age": 72,
        "labs": {
            "egfr": 70.0,
            "creatinine": 1.0,
            "potassium": 4.1,
            "inr": 1.9
        },
        "diagnoses": [
            "heart_failure",
            "type_2_diabetes",
            "anemia"
        ],
        "medications": [
            "allopurinol",
            "cetirizine",
            "clopidogrel",
            "omeprazole",
            "paroxetine",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0030-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-E-0030-2",
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
        "case_id": "SYN-E-0031",
        "age": 66,
        "labs": {
            "egfr": 67.6,
            "creatinine": 0.8,
            "potassium": 4.0,
            "inr": 2.3
        },
        "diagnoses": [
            "chronic_liver_disease",
            "chronic_kidney_disease",
            "atrial_fibrillation"
        ],
        "medications": [
            "amiodarone",
            "aspirin",
            "naproxen",
            "rivaroxaban",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0031-1",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-E-0031-2",
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
        "case_id": "SYN-E-0032",
        "age": 73,
        "labs": {
            "egfr": 80.6,
            "creatinine": 1.1,
            "potassium": 4.4,
            "inr": 2.7
        },
        "diagnoses": [
            "anxiety",
            "dyslipidemia",
            "chronic_liver_disease"
        ],
        "medications": [
            "azithromycin",
            "citalopram",
            "digoxin",
            "fluconazole",
            "linezolid",
            "omeprazole",
            "ticagrelor",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0032-1",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-E-0032-2",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-E-0032-3",
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
        "case_id": "SYN-E-0033",
        "age": 57,
        "labs": {
            "egfr": 80.2,
            "creatinine": 1.2,
            "potassium": 4.3,
            "inr": 1.6
        },
        "diagnoses": [
            "depression",
            "coronary_artery_disease"
        ],
        "medications": [
            "amiodarone",
            "atorvastatin",
            "ciprofloxacin",
            "digoxin",
            "valsartan",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0033-1",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-E-0033-2",
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
        "case_id": "SYN-E-0034",
        "age": 74,
        "labs": {
            "egfr": 79.0,
            "creatinine": 1.2,
            "potassium": 4.5,
            "inr": 1.2
        },
        "diagnoses": [
            "chronic_pain",
            "dyslipidemia"
        ],
        "medications": [
            "amlodipine",
            "diclofenac",
            "digoxin",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0034-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0034-2",
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
        "case_id": "SYN-E-0035",
        "age": 77,
        "labs": {
            "egfr": 62.5,
            "creatinine": 1.3,
            "potassium": 4.5,
            "inr": 1.2
        },
        "diagnoses": [
            "gout",
            "atrial_fibrillation"
        ],
        "medications": [
            "ferrous_sulfate",
            "isosorbide_mononitrate",
            "levothyroxine",
            "metronidazole",
            "sertraline",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0035-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0035-2",
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
        "case_id": "SYN-E-0036",
        "age": 68,
        "labs": {
            "egfr": 71.0,
            "creatinine": 1.2,
            "potassium": 4.3,
            "inr": 1.2
        },
        "diagnoses": [
            "osteoarthritis",
            "chronic_kidney_disease"
        ],
        "medications": [
            "amiodarone",
            "calcium_carbonate",
            "digoxin",
            "furosemide",
            "metoprolol",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0036-1",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-E-0036-2",
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
        "case_id": "SYN-E-0037",
        "age": 71,
        "labs": {
            "egfr": 60.1,
            "creatinine": 1.1,
            "potassium": 3.8,
            "inr": 2.2
        },
        "diagnoses": [
            "nonalcoholic_steatohepatitis",
            "type_2_diabetes"
        ],
        "medications": [
            "atorvastatin",
            "ciprofloxacin",
            "glipizide",
            "metronidazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0037-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0037-2",
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
        "case_id": "SYN-E-0038",
        "age": 62,
        "labs": {
            "egfr": 68.8,
            "creatinine": 1.0,
            "potassium": 4.1,
            "inr": 2.6
        },
        "diagnoses": [
            "atrial_fibrillation",
            "nonalcoholic_steatohepatitis",
            "hypothyroidism"
        ],
        "medications": [
            "ferrous_sulfate",
            "ibuprofen",
            "ketoconazole",
            "losartan",
            "omeprazole",
            "spironolactone",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0038-1",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-E-0038-2",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            },
            {
                "interaction_id": "INT-SYN-E-0038-3",
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
        "case_id": "SYN-E-0039",
        "age": 77,
        "labs": {
            "egfr": 73.4,
            "creatinine": 1.3,
            "potassium": 4.5,
            "inr": 1.6
        },
        "diagnoses": [
            "hypothyroidism",
            "dyslipidemia"
        ],
        "medications": [
            "calcium_carbonate",
            "dabigatran",
            "diclofenac",
            "ketoconazole",
            "levothyroxine"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0039-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-E-0039-2",
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
        "case_id": "SYN-E-0040",
        "age": 59,
        "labs": {
            "egfr": 77.6,
            "creatinine": 1.0,
            "potassium": 4.6,
            "inr": 1.1
        },
        "diagnoses": [
            "chronic_pain",
            "atrial_fibrillation"
        ],
        "medications": [
            "dabigatran",
            "ketoconazole",
            "lisinopril",
            "nitroglycerin",
            "omeprazole",
            "sildenafil",
            "ticagrelor"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0040-1",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-E-0040-2",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-E-0040-3",
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
        "case_id": "SYN-E-0041",
        "age": 67,
        "labs": {
            "egfr": 64.8,
            "creatinine": 0.9,
            "potassium": 4.1,
            "inr": 2.5
        },
        "diagnoses": [
            "anemia",
            "depression",
            "gout"
        ],
        "medications": [
            "digoxin",
            "ketoconazole",
            "linezolid",
            "naproxen",
            "rivaroxaban",
            "sertraline"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0041-1",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-E-0041-2",
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
        "case_id": "SYN-E-0042",
        "age": 71,
        "labs": {
            "egfr": 77.1,
            "creatinine": 1.1,
            "potassium": 4.0,
            "inr": 1.4
        },
        "diagnoses": [
            "osteoarthritis",
            "chronic_liver_disease",
            "chronic_pain"
        ],
        "medications": [
            "apixaban",
            "furosemide",
            "naproxen",
            "prednisone",
            "rivaroxaban",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0042-1",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0042-2",
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
        "case_id": "SYN-E-0043",
        "age": 78,
        "labs": {
            "egfr": 82.8,
            "creatinine": 0.9,
            "potassium": 3.9,
            "inr": 2.8
        },
        "diagnoses": [
            "chronic_pain",
            "gout",
            "hypothyroidism"
        ],
        "medications": [
            "furosemide",
            "metoprolol",
            "naproxen",
            "paroxetine",
            "rivaroxaban"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0043-1",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0043-2",
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
        "case_id": "SYN-E-0044",
        "age": 65,
        "labs": {
            "egfr": 85.8,
            "creatinine": 0.9,
            "potassium": 4.4,
            "inr": 1.3
        },
        "diagnoses": [
            "hypertension",
            "atrial_fibrillation",
            "depression"
        ],
        "medications": [
            "aspirin",
            "clarithromycin",
            "linezolid",
            "losartan",
            "sertraline",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0044-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0044-2",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            },
            {
                "interaction_id": "INT-SYN-E-0044-3",
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
        "case_id": "SYN-E-0045",
        "age": 70,
        "labs": {
            "egfr": 83.6,
            "creatinine": 1.1,
            "potassium": 4.3,
            "inr": 1.5
        },
        "diagnoses": [
            "chronic_pain",
            "chronic_liver_disease"
        ],
        "medications": [
            "clopidogrel",
            "dabigatran",
            "ferrous_sulfate",
            "ketoconazole",
            "levothyroxine",
            "nitroglycerin",
            "omeprazole"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0045-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-E-0045-2",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-E-0045-3",
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
        "case_id": "SYN-E-0046",
        "age": 59,
        "labs": {
            "egfr": 72.6,
            "creatinine": 0.9,
            "potassium": 4.5,
            "inr": 1.9
        },
        "diagnoses": [
            "hypertension",
            "dyslipidemia"
        ],
        "medications": [
            "apixaban",
            "clarithromycin",
            "ibuprofen",
            "linezolid",
            "sertraline"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0046-1",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-E-0046-2",
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
        "case_id": "SYN-E-0047",
        "age": 69,
        "labs": {
            "egfr": 65.4,
            "creatinine": 1.1,
            "potassium": 4.4,
            "inr": 1.2
        },
        "diagnoses": [
            "hypothyroidism",
            "anemia",
            "peripheral_artery_disease"
        ],
        "medications": [
            "diltiazem",
            "furosemide",
            "metoprolol",
            "metronidazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0047-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0047-2",
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
        "case_id": "SYN-E-0048",
        "age": 62,
        "labs": {
            "egfr": 60.1,
            "creatinine": 0.9,
            "potassium": 4.1,
            "inr": 1.1
        },
        "diagnoses": [
            "chronic_liver_disease",
            "atrial_fibrillation",
            "osteoarthritis"
        ],
        "medications": [
            "amiodarone",
            "apixaban",
            "clarithromycin",
            "dabigatran",
            "ketoconazole",
            "losartan",
            "simvastatin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0048-1",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-E-0048-2",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-E-0048-3",
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
        "case_id": "SYN-E-0049",
        "age": 61,
        "labs": {
            "egfr": 68.0,
            "creatinine": 0.9,
            "potassium": 4.0,
            "inr": 1.6
        },
        "diagnoses": [
            "nonalcoholic_steatohepatitis",
            "type_2_diabetes",
            "dyslipidemia"
        ],
        "medications": [
            "amiodarone",
            "amlodipine",
            "atorvastatin",
            "ciprofloxacin",
            "digoxin",
            "ibuprofen",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0049-1",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0049-2",
                "drug_a": "amlodipine",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive hypotension in frail adults"
            },
            {
                "interaction_id": "INT-SYN-E-0049-3",
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
        "case_id": "SYN-E-0050",
        "age": 77,
        "labs": {
            "egfr": 66.6,
            "creatinine": 1.2,
            "potassium": 3.8,
            "inr": 1.3
        },
        "diagnoses": [
            "anxiety",
            "nonalcoholic_steatohepatitis",
            "coronary_artery_disease"
        ],
        "medications": [
            "amiodarone",
            "digoxin",
            "isosorbide_mononitrate",
            "prednisone",
            "sildenafil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0050-1",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-E-0050-2",
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
        "case_id": "SYN-E-0051",
        "age": 59,
        "labs": {
            "egfr": 82.4,
            "creatinine": 1.1,
            "potassium": 3.9,
            "inr": 1.5
        },
        "diagnoses": [
            "anemia",
            "chronic_kidney_disease",
            "type_2_diabetes"
        ],
        "medications": [
            "atorvastatin",
            "diltiazem",
            "linezolid",
            "metformin",
            "omeprazole",
            "sertraline",
            "sildenafil",
            "ticagrelor"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0051-1",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-E-0051-2",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-E-0051-3",
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
        "case_id": "SYN-E-0052",
        "age": 72,
        "labs": {
            "egfr": 65.9,
            "creatinine": 0.9,
            "potassium": 3.9,
            "inr": 2.2
        },
        "diagnoses": [
            "atrial_fibrillation",
            "heart_failure",
            "depression"
        ],
        "medications": [
            "allopurinol",
            "amiodarone",
            "digoxin",
            "ibuprofen",
            "rivaroxaban",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0052-1",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0052-2",
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
        "case_id": "SYN-E-0053",
        "age": 59,
        "labs": {
            "egfr": 65.6,
            "creatinine": 0.9,
            "potassium": 4.4,
            "inr": 2.4
        },
        "diagnoses": [
            "gout",
            "chronic_liver_disease"
        ],
        "medications": [
            "ciprofloxacin",
            "fluconazole",
            "furosemide",
            "ticagrelor",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0053-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0053-2",
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
        "case_id": "SYN-E-0054",
        "age": 77,
        "labs": {
            "egfr": 77.7,
            "creatinine": 1.0,
            "potassium": 4.3,
            "inr": 2.3
        },
        "diagnoses": [
            "osteoarthritis",
            "depression"
        ],
        "medications": [
            "atorvastatin",
            "diltiazem",
            "fluconazole",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0054-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0054-2",
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
        "case_id": "SYN-E-0055",
        "age": 79,
        "labs": {
            "egfr": 79.7,
            "creatinine": 1.2,
            "potassium": 4.0,
            "inr": 1.2
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "atrial_fibrillation",
            "gout"
        ],
        "medications": [
            "amiodarone",
            "apixaban",
            "azithromycin",
            "calcium_carbonate",
            "naproxen",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0055-1",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-E-0055-2",
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
        "case_id": "SYN-E-0056",
        "age": 65,
        "labs": {
            "egfr": 62.3,
            "creatinine": 1.0,
            "potassium": 4.1,
            "inr": 1.8
        },
        "diagnoses": [
            "chronic_liver_disease",
            "peripheral_artery_disease"
        ],
        "medications": [
            "amiodarone",
            "amlodipine",
            "ciprofloxacin",
            "diclofenac",
            "ketoconazole",
            "losartan",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0056-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0056-2",
                "drug_a": "amlodipine",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive hypotension in frail adults"
            },
            {
                "interaction_id": "INT-SYN-E-0056-3",
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
        "case_id": "SYN-E-0057",
        "age": 59,
        "labs": {
            "egfr": 89.4,
            "creatinine": 1.1,
            "potassium": 4.6,
            "inr": 1.7
        },
        "diagnoses": [
            "anxiety",
            "peripheral_artery_disease",
            "anemia"
        ],
        "medications": [
            "allopurinol",
            "digoxin",
            "linezolid",
            "naproxen",
            "rivaroxaban",
            "sertraline",
            "sildenafil",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0057-1",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-E-0057-2",
                "drug_a": "digoxin",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "P-gp inhibition can raise digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-E-0057-3",
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
        "case_id": "SYN-E-0058",
        "age": 55,
        "labs": {
            "egfr": 63.8,
            "creatinine": 1.2,
            "potassium": 4.0,
            "inr": 1.1
        },
        "diagnoses": [
            "dyslipidemia",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "apixaban",
            "aspirin",
            "clopidogrel",
            "naproxen",
            "sertraline",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0058-1",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0058-2",
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
        "case_id": "SYN-E-0059",
        "age": 62,
        "labs": {
            "egfr": 75.5,
            "creatinine": 1.0,
            "potassium": 3.8,
            "inr": 2.2
        },
        "diagnoses": [
            "anemia",
            "chronic_pain",
            "chronic_kidney_disease"
        ],
        "medications": [
            "amiodarone",
            "azithromycin",
            "losartan",
            "prednisone",
            "sertraline",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0059-1",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-E-0059-2",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            },
            {
                "interaction_id": "INT-SYN-E-0059-3",
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
        "case_id": "SYN-E-0060",
        "age": 62,
        "labs": {
            "egfr": 79.0,
            "creatinine": 1.2,
            "potassium": 3.9,
            "inr": 1.5
        },
        "diagnoses": [
            "gout",
            "anemia"
        ],
        "medications": [
            "calcium_carbonate",
            "ciprofloxacin",
            "fluconazole",
            "ketoconazole",
            "linezolid",
            "sertraline",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0060-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0060-2",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-E-0060-3",
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
        "case_id": "SYN-E-0061",
        "age": 77,
        "labs": {
            "egfr": 63.3,
            "creatinine": 1.2,
            "potassium": 4.6,
            "inr": 2.1
        },
        "diagnoses": [
            "anxiety",
            "nonalcoholic_steatohepatitis",
            "atrial_fibrillation"
        ],
        "medications": [
            "allopurinol",
            "amlodipine",
            "metoprolol",
            "omeprazole",
            "paroxetine",
            "ticagrelor"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0061-1",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-E-0061-2",
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
        "case_id": "SYN-E-0062",
        "age": 59,
        "labs": {
            "egfr": 89.8,
            "creatinine": 1.1,
            "potassium": 4.2,
            "inr": 2.2
        },
        "diagnoses": [
            "heart_failure",
            "gout",
            "depression"
        ],
        "medications": [
            "cetirizine",
            "ciprofloxacin",
            "isosorbide_mononitrate",
            "naproxen",
            "rivaroxaban",
            "sildenafil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0062-1",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-E-0062-2",
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
        "case_id": "SYN-E-0063",
        "age": 72,
        "labs": {
            "egfr": 78.5,
            "creatinine": 1.3,
            "potassium": 3.9,
            "inr": 1.6
        },
        "diagnoses": [
            "depression",
            "nonalcoholic_steatohepatitis",
            "osteoarthritis"
        ],
        "medications": [
            "allopurinol",
            "fluconazole",
            "ibuprofen",
            "isosorbide_mononitrate",
            "sildenafil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0063-1",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-E-0063-2",
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
        "case_id": "SYN-E-0064",
        "age": 72,
        "labs": {
            "egfr": 62.6,
            "creatinine": 1.0,
            "potassium": 4.4,
            "inr": 1.9
        },
        "diagnoses": [
            "depression",
            "atrial_fibrillation"
        ],
        "medications": [
            "dabigatran",
            "diclofenac",
            "ferrous_sulfate",
            "ketoconazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0064-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0064-2",
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
        "case_id": "SYN-E-0065",
        "age": 74,
        "labs": {
            "egfr": 74.1,
            "creatinine": 0.9,
            "potassium": 4.4,
            "inr": 2.6
        },
        "diagnoses": [
            "anxiety",
            "type_2_diabetes"
        ],
        "medications": [
            "ferrous_sulfate",
            "fluconazole",
            "ibuprofen",
            "lisinopril",
            "nitroglycerin",
            "sildenafil",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0065-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0065-2",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-E-0065-3",
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
        "case_id": "SYN-E-0066",
        "age": 58,
        "labs": {
            "egfr": 62.7,
            "creatinine": 0.8,
            "potassium": 4.1,
            "inr": 2.0
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "nonalcoholic_steatohepatitis",
            "chronic_liver_disease"
        ],
        "medications": [
            "amiodarone",
            "digoxin",
            "diltiazem",
            "linezolid",
            "paroxetine",
            "sertraline"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0066-1",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-E-0066-2",
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
        "case_id": "SYN-E-0067",
        "age": 78,
        "labs": {
            "egfr": 64.0,
            "creatinine": 1.1,
            "potassium": 4.1,
            "inr": 2.6
        },
        "diagnoses": [
            "hypothyroidism",
            "atrial_fibrillation",
            "chronic_kidney_disease"
        ],
        "medications": [
            "cetirizine",
            "ciprofloxacin",
            "diltiazem",
            "glipizide",
            "omeprazole",
            "simvastatin",
            "ticagrelor"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0067-1",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-E-0067-2",
                "drug_a": "glipizide",
                "drug_b": "ciprofloxacin",
                "severity": "moderate",
                "evidence": "dysglycemia risk from fluoroquinolone-sulfonylurea combination"
            },
            {
                "interaction_id": "INT-SYN-E-0067-3",
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
        "case_id": "SYN-E-0068",
        "age": 75,
        "labs": {
            "egfr": 89.1,
            "creatinine": 0.9,
            "potassium": 4.6,
            "inr": 2.4
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "hypothyroidism"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "cetirizine",
            "diclofenac",
            "digoxin",
            "isosorbide_mononitrate",
            "sildenafil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0068-1",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0068-2",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-E-0068-3",
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
        "case_id": "SYN-E-0069",
        "age": 62,
        "labs": {
            "egfr": 65.1,
            "creatinine": 0.9,
            "potassium": 4.4,
            "inr": 1.8
        },
        "diagnoses": [
            "nonalcoholic_steatohepatitis",
            "type_2_diabetes",
            "dyslipidemia"
        ],
        "medications": [
            "amiodarone",
            "apixaban",
            "digoxin",
            "isosorbide_mononitrate",
            "lisinopril",
            "naproxen",
            "sildenafil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0069-1",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-E-0069-2",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-E-0069-3",
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
        "case_id": "SYN-E-0070",
        "age": 79,
        "labs": {
            "egfr": 83.6,
            "creatinine": 0.8,
            "potassium": 3.8,
            "inr": 2.3
        },
        "diagnoses": [
            "heart_failure",
            "atrial_fibrillation"
        ],
        "medications": [
            "aspirin",
            "ibuprofen",
            "isosorbide_mononitrate",
            "sertraline",
            "sildenafil",
            "ticagrelor"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0070-1",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-E-0070-2",
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
        "case_id": "SYN-E-0071",
        "age": 78,
        "labs": {
            "egfr": 89.2,
            "creatinine": 1.2,
            "potassium": 4.0,
            "inr": 1.2
        },
        "diagnoses": [
            "gout",
            "type_2_diabetes"
        ],
        "medications": [
            "aspirin",
            "metoprolol",
            "nitroglycerin",
            "prednisone",
            "sildenafil",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0071-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0071-2",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-E-0071-3",
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
        "case_id": "SYN-E-0072",
        "age": 77,
        "labs": {
            "egfr": 85.7,
            "creatinine": 0.9,
            "potassium": 4.0,
            "inr": 1.3
        },
        "diagnoses": [
            "anxiety",
            "peripheral_artery_disease"
        ],
        "medications": [
            "amiodarone",
            "azithromycin",
            "citalopram",
            "digoxin",
            "metronidazole"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0072-1",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-E-0072-2",
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
        "case_id": "SYN-E-0073",
        "age": 74,
        "labs": {
            "egfr": 62.8,
            "creatinine": 1.1,
            "potassium": 4.1,
            "inr": 2.1
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "hypothyroidism"
        ],
        "medications": [
            "azithromycin",
            "citalopram",
            "furosemide",
            "rivaroxaban",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0073-1",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-E-0073-2",
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
        "case_id": "SYN-E-0074",
        "age": 57,
        "labs": {
            "egfr": 71.0,
            "creatinine": 1.1,
            "potassium": 3.9,
            "inr": 2.5
        },
        "diagnoses": [
            "hypothyroidism",
            "chronic_kidney_disease",
            "gout"
        ],
        "medications": [
            "ciprofloxacin",
            "dabigatran",
            "furosemide",
            "glipizide",
            "naproxen",
            "nitroglycerin",
            "rivaroxaban",
            "sildenafil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0074-1",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0074-2",
                "drug_a": "glipizide",
                "drug_b": "ciprofloxacin",
                "severity": "moderate",
                "evidence": "dysglycemia risk from fluoroquinolone-sulfonylurea combination"
            },
            {
                "interaction_id": "INT-SYN-E-0074-3",
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
        "case_id": "SYN-E-0075",
        "age": 56,
        "labs": {
            "egfr": 77.8,
            "creatinine": 0.8,
            "potassium": 4.2,
            "inr": 1.3
        },
        "diagnoses": [
            "hypertension",
            "chronic_kidney_disease",
            "peripheral_artery_disease"
        ],
        "medications": [
            "furosemide",
            "metronidazole",
            "nitroglycerin",
            "rivaroxaban",
            "sildenafil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0075-1",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-E-0075-2",
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
        "case_id": "SYN-E-0076",
        "age": 70,
        "labs": {
            "egfr": 75.4,
            "creatinine": 1.2,
            "potassium": 4.2,
            "inr": 1.8
        },
        "diagnoses": [
            "hypertension",
            "anemia"
        ],
        "medications": [
            "clarithromycin",
            "diclofenac",
            "isosorbide_mononitrate",
            "omeprazole",
            "sertraline",
            "sildenafil",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0076-1",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-E-0076-2",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-E-0076-3",
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
        "case_id": "SYN-E-0077",
        "age": 78,
        "labs": {
            "egfr": 84.3,
            "creatinine": 1.1,
            "potassium": 4.5,
            "inr": 1.8
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "anxiety",
            "depression"
        ],
        "medications": [
            "apixaban",
            "diclofenac",
            "ferrous_sulfate",
            "losartan",
            "nitroglycerin",
            "sildenafil",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0077-1",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0077-2",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-E-0077-3",
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
        "case_id": "SYN-E-0078",
        "age": 72,
        "labs": {
            "egfr": 87.0,
            "creatinine": 1.1,
            "potassium": 4.6,
            "inr": 1.3
        },
        "diagnoses": [
            "coronary_artery_disease",
            "hypertension"
        ],
        "medications": [
            "lisinopril",
            "naproxen",
            "nitroglycerin",
            "rivaroxaban",
            "sildenafil",
            "spironolactone"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0078-1",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-E-0078-2",
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
        "case_id": "SYN-E-0079",
        "age": 79,
        "labs": {
            "egfr": 89.3,
            "creatinine": 1.3,
            "potassium": 4.2,
            "inr": 1.6
        },
        "diagnoses": [
            "chronic_pain",
            "anemia"
        ],
        "medications": [
            "apixaban",
            "ferrous_sulfate",
            "fluconazole",
            "naproxen",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0079-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0079-2",
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
        "case_id": "SYN-E-0080",
        "age": 67,
        "labs": {
            "egfr": 62.7,
            "creatinine": 1.1,
            "potassium": 4.1,
            "inr": 2.0
        },
        "diagnoses": [
            "chronic_pain",
            "osteoarthritis",
            "hypothyroidism"
        ],
        "medications": [
            "apixaban",
            "dabigatran",
            "diclofenac",
            "ketoconazole",
            "linezolid",
            "losartan",
            "sertraline",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0080-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-E-0080-2",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            },
            {
                "interaction_id": "INT-SYN-E-0080-3",
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
        "case_id": "SYN-E-0081",
        "age": 76,
        "labs": {
            "egfr": 60.4,
            "creatinine": 1.1,
            "potassium": 4.4,
            "inr": 2.7
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "atrial_fibrillation"
        ],
        "medications": [
            "azithromycin",
            "diclofenac",
            "losartan",
            "metronidazole",
            "prednisone",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0081-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0081-2",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            },
            {
                "interaction_id": "INT-SYN-E-0081-3",
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
        "case_id": "SYN-E-0082",
        "age": 72,
        "labs": {
            "egfr": 60.1,
            "creatinine": 1.0,
            "potassium": 4.0,
            "inr": 2.7
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "gout",
            "heart_failure"
        ],
        "medications": [
            "dabigatran",
            "diclofenac",
            "furosemide",
            "ketoconazole",
            "metoprolol",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0082-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0082-2",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-E-0082-3",
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
        "case_id": "SYN-E-0083",
        "age": 58,
        "labs": {
            "egfr": 82.1,
            "creatinine": 1.1,
            "potassium": 4.3,
            "inr": 2.6
        },
        "diagnoses": [
            "depression",
            "gout"
        ],
        "medications": [
            "azithromycin",
            "ibuprofen",
            "prednisone",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0083-1",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0083-2",
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
        "case_id": "SYN-E-0084",
        "age": 64,
        "labs": {
            "egfr": 63.4,
            "creatinine": 0.9,
            "potassium": 3.9,
            "inr": 2.2
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "anxiety"
        ],
        "medications": [
            "apixaban",
            "isosorbide_mononitrate",
            "naproxen",
            "nitroglycerin",
            "sildenafil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0084-1",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-E-0084-2",
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
        "case_id": "SYN-E-0085",
        "age": 78,
        "labs": {
            "egfr": 72.3,
            "creatinine": 1.0,
            "potassium": 4.4,
            "inr": 2.5
        },
        "diagnoses": [
            "osteoarthritis",
            "heart_failure"
        ],
        "medications": [
            "amiodarone",
            "isosorbide_mononitrate",
            "metoprolol",
            "naproxen",
            "paroxetine",
            "rivaroxaban"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0085-1",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0085-2",
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
        "case_id": "SYN-E-0086",
        "age": 74,
        "labs": {
            "egfr": 61.0,
            "creatinine": 1.3,
            "potassium": 4.3,
            "inr": 2.1
        },
        "diagnoses": [
            "atrial_fibrillation",
            "gout"
        ],
        "medications": [
            "fluconazole",
            "isosorbide_mononitrate",
            "ketoconazole",
            "sildenafil",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0086-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0086-2",
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
        "case_id": "SYN-E-0087",
        "age": 69,
        "labs": {
            "egfr": 65.9,
            "creatinine": 0.9,
            "potassium": 4.2,
            "inr": 2.7
        },
        "diagnoses": [
            "hypertension",
            "dyslipidemia"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "ciprofloxacin",
            "clarithromycin",
            "diclofenac",
            "metronidazole",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0087-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0087-2",
                "drug_a": "amlodipine",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive hypotension in frail adults"
            },
            {
                "interaction_id": "INT-SYN-E-0087-3",
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
        "case_id": "SYN-E-0088",
        "age": 76,
        "labs": {
            "egfr": 62.7,
            "creatinine": 1.0,
            "potassium": 4.4,
            "inr": 1.9
        },
        "diagnoses": [
            "atrial_fibrillation",
            "type_2_diabetes"
        ],
        "medications": [
            "aspirin",
            "ciprofloxacin",
            "clopidogrel",
            "diltiazem",
            "fluconazole",
            "omeprazole",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0088-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0088-2",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-E-0088-3",
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
        "case_id": "SYN-E-0089",
        "age": 63,
        "labs": {
            "egfr": 77.8,
            "creatinine": 1.1,
            "potassium": 4.1,
            "inr": 1.8
        },
        "diagnoses": [
            "gout",
            "chronic_kidney_disease"
        ],
        "medications": [
            "amiodarone",
            "apixaban",
            "citalopram",
            "diclofenac",
            "digoxin",
            "omeprazole",
            "ticagrelor"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0089-1",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0089-2",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-E-0089-3",
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
        "case_id": "SYN-E-0090",
        "age": 73,
        "labs": {
            "egfr": 84.4,
            "creatinine": 0.9,
            "potassium": 4.5,
            "inr": 1.8
        },
        "diagnoses": [
            "hypothyroidism",
            "atrial_fibrillation"
        ],
        "medications": [
            "clopidogrel",
            "diclofenac",
            "omeprazole",
            "rivaroxaban",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0090-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0090-2",
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
        "case_id": "SYN-E-0091",
        "age": 78,
        "labs": {
            "egfr": 82.1,
            "creatinine": 0.8,
            "potassium": 4.5,
            "inr": 1.5
        },
        "diagnoses": [
            "hypothyroidism",
            "peripheral_artery_disease",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "amiodarone",
            "azithromycin",
            "calcium_carbonate",
            "citalopram",
            "glipizide",
            "levothyroxine",
            "linezolid",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0091-1",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-E-0091-2",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-E-0091-3",
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
        "case_id": "SYN-E-0092",
        "age": 71,
        "labs": {
            "egfr": 78.1,
            "creatinine": 1.0,
            "potassium": 4.5,
            "inr": 2.6
        },
        "diagnoses": [
            "chronic_pain",
            "hypothyroidism",
            "anxiety"
        ],
        "medications": [
            "apixaban",
            "aspirin",
            "dabigatran",
            "digoxin",
            "ketoconazole",
            "levothyroxine",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0092-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0092-2",
                "drug_a": "digoxin",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "P-gp inhibition can raise digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-E-0092-3",
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
        "case_id": "SYN-E-0093",
        "age": 59,
        "labs": {
            "egfr": 81.0,
            "creatinine": 1.1,
            "potassium": 4.3,
            "inr": 1.9
        },
        "diagnoses": [
            "type_2_diabetes",
            "peripheral_artery_disease",
            "hypothyroidism"
        ],
        "medications": [
            "losartan",
            "metronidazole",
            "nitroglycerin",
            "sildenafil",
            "simvastatin",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0093-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0093-2",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            },
            {
                "interaction_id": "INT-SYN-E-0093-3",
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
        "case_id": "SYN-E-0094",
        "age": 77,
        "labs": {
            "egfr": 77.5,
            "creatinine": 0.8,
            "potassium": 4.3,
            "inr": 2.4
        },
        "diagnoses": [
            "type_2_diabetes",
            "dyslipidemia",
            "peripheral_artery_disease"
        ],
        "medications": [
            "apixaban",
            "diclofenac",
            "diltiazem",
            "losartan",
            "metoprolol",
            "sildenafil",
            "simvastatin",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0094-1",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0094-2",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            },
            {
                "interaction_id": "INT-SYN-E-0094-3",
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
        "case_id": "SYN-E-0095",
        "age": 79,
        "labs": {
            "egfr": 79.4,
            "creatinine": 0.9,
            "potassium": 4.5,
            "inr": 1.5
        },
        "diagnoses": [
            "atrial_fibrillation",
            "chronic_liver_disease",
            "hypothyroidism"
        ],
        "medications": [
            "ketoconazole",
            "metoprolol",
            "omeprazole",
            "paroxetine",
            "ticagrelor"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0095-1",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-E-0095-2",
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
        "case_id": "SYN-E-0096",
        "age": 58,
        "labs": {
            "egfr": 67.4,
            "creatinine": 1.0,
            "potassium": 4.3,
            "inr": 1.7
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "peripheral_artery_disease",
            "chronic_liver_disease"
        ],
        "medications": [
            "amiodarone",
            "fluconazole",
            "lisinopril",
            "naproxen",
            "rivaroxaban",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0096-1",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0096-2",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0096-3",
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
        "case_id": "SYN-E-0097",
        "age": 55,
        "labs": {
            "egfr": 63.7,
            "creatinine": 0.8,
            "potassium": 4.3,
            "inr": 1.1
        },
        "diagnoses": [
            "hypothyroidism",
            "chronic_pain"
        ],
        "medications": [
            "apixaban",
            "azithromycin",
            "citalopram",
            "dabigatran",
            "naproxen"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0097-1",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-E-0097-2",
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
        "case_id": "SYN-E-0098",
        "age": 75,
        "labs": {
            "egfr": 77.8,
            "creatinine": 1.0,
            "potassium": 4.3,
            "inr": 1.5
        },
        "diagnoses": [
            "chronic_pain",
            "heart_failure",
            "type_2_diabetes"
        ],
        "medications": [
            "apixaban",
            "clopidogrel",
            "diclofenac",
            "fluconazole",
            "losartan",
            "naproxen",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0098-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0098-2",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            },
            {
                "interaction_id": "INT-SYN-E-0098-3",
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
        "case_id": "SYN-E-0099",
        "age": 71,
        "labs": {
            "egfr": 77.6,
            "creatinine": 1.1,
            "potassium": 4.6,
            "inr": 2.8
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "gout"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "ciprofloxacin",
            "clarithromycin",
            "linezolid",
            "ticagrelor"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0099-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0099-2",
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
        "case_id": "SYN-E-0100",
        "age": 68,
        "labs": {
            "egfr": 86.4,
            "creatinine": 1.0,
            "potassium": 4.0,
            "inr": 1.0
        },
        "diagnoses": [
            "chronic_liver_disease",
            "peripheral_artery_disease",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "levothyroxine",
            "naproxen",
            "rivaroxaban",
            "trimethoprim_sulfamethoxazole",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0100-1",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0100-2",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-E-0101",
        "age": 76,
        "labs": {
            "egfr": 68.0,
            "creatinine": 1.1,
            "potassium": 4.4,
            "inr": 2.6
        },
        "diagnoses": [
            "heart_failure",
            "hypothyroidism"
        ],
        "medications": [
            "dabigatran",
            "fluconazole",
            "ketoconazole",
            "lisinopril",
            "metronidazole",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0101-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-E-0101-2",
                "drug_a": "spironolactone",
                "drug_b": "lisinopril",
                "severity": "moderate",
                "evidence": "hyperkalemia risk in CKD"
            },
            {
                "interaction_id": "INT-SYN-E-0101-3",
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
        "case_id": "SYN-E-0102",
        "age": 67,
        "labs": {
            "egfr": 89.4,
            "creatinine": 1.2,
            "potassium": 4.4,
            "inr": 1.7
        },
        "diagnoses": [
            "anxiety",
            "peripheral_artery_disease",
            "anemia"
        ],
        "medications": [
            "clopidogrel",
            "dabigatran",
            "ketoconazole",
            "linezolid",
            "nitroglycerin",
            "sertraline",
            "sildenafil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0102-1",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-E-0102-2",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-E-0102-3",
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
        "case_id": "SYN-E-0103",
        "age": 68,
        "labs": {
            "egfr": 67.5,
            "creatinine": 1.1,
            "potassium": 4.5,
            "inr": 2.5
        },
        "diagnoses": [
            "coronary_artery_disease",
            "anxiety"
        ],
        "medications": [
            "amlodipine",
            "clarithromycin",
            "diclofenac",
            "naproxen",
            "rivaroxaban",
            "simvastatin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0103-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0103-2",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-E-0103-3",
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
        "case_id": "SYN-E-0104",
        "age": 58,
        "labs": {
            "egfr": 71.7,
            "creatinine": 1.1,
            "potassium": 4.6,
            "inr": 1.4
        },
        "diagnoses": [
            "nonalcoholic_steatohepatitis",
            "depression",
            "osteoarthritis"
        ],
        "medications": [
            "calcium_carbonate",
            "fluconazole",
            "levothyroxine",
            "prednisone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0104-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0104-2",
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
        "case_id": "SYN-E-0105",
        "age": 58,
        "labs": {
            "egfr": 69.3,
            "creatinine": 1.1,
            "potassium": 4.1,
            "inr": 1.3
        },
        "diagnoses": [
            "anxiety",
            "chronic_liver_disease",
            "osteoarthritis"
        ],
        "medications": [
            "digoxin",
            "rivaroxaban",
            "trimethoprim_sulfamethoxazole",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0105-1",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0105-2",
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
        "case_id": "SYN-E-0106",
        "age": 75,
        "labs": {
            "egfr": 82.9,
            "creatinine": 1.1,
            "potassium": 4.2,
            "inr": 2.0
        },
        "diagnoses": [
            "dyslipidemia",
            "chronic_liver_disease",
            "heart_failure"
        ],
        "medications": [
            "digoxin",
            "fluconazole",
            "losartan",
            "nitroglycerin",
            "sildenafil",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0106-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0106-2",
                "drug_a": "digoxin",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "P-gp inhibition can raise digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-E-0106-3",
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
        "case_id": "SYN-E-0107",
        "age": 79,
        "labs": {
            "egfr": 69.2,
            "creatinine": 1.0,
            "potassium": 4.3,
            "inr": 2.8
        },
        "diagnoses": [
            "depression",
            "peripheral_artery_disease",
            "hypothyroidism"
        ],
        "medications": [
            "clarithromycin",
            "furosemide",
            "ibuprofen",
            "losartan",
            "metoprolol",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0107-1",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0107-2",
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
        "case_id": "SYN-E-0108",
        "age": 75,
        "labs": {
            "egfr": 60.1,
            "creatinine": 0.9,
            "potassium": 4.0,
            "inr": 1.5
        },
        "diagnoses": [
            "nonalcoholic_steatohepatitis",
            "chronic_liver_disease",
            "gout"
        ],
        "medications": [
            "calcium_carbonate",
            "diclofenac",
            "levothyroxine",
            "lisinopril",
            "metformin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0108-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0108-2",
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
        "case_id": "SYN-E-0109",
        "age": 57,
        "labs": {
            "egfr": 70.2,
            "creatinine": 1.1,
            "potassium": 4.3,
            "inr": 1.8
        },
        "diagnoses": [
            "chronic_pain",
            "anxiety"
        ],
        "medications": [
            "ibuprofen",
            "losartan",
            "metoprolol",
            "paroxetine",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0109-1",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0109-2",
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
        "case_id": "SYN-E-0110",
        "age": 77,
        "labs": {
            "egfr": 86.9,
            "creatinine": 0.8,
            "potassium": 4.2,
            "inr": 1.6
        },
        "diagnoses": [
            "dyslipidemia",
            "gout"
        ],
        "medications": [
            "aspirin",
            "furosemide",
            "metoprolol",
            "rivaroxaban",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0110-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0110-2",
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
        "case_id": "SYN-E-0111",
        "age": 59,
        "labs": {
            "egfr": 77.3,
            "creatinine": 1.0,
            "potassium": 4.0,
            "inr": 2.6
        },
        "diagnoses": [
            "type_2_diabetes",
            "peripheral_artery_disease",
            "anxiety"
        ],
        "medications": [
            "calcium_carbonate",
            "diclofenac",
            "isosorbide_mononitrate",
            "metoprolol",
            "sildenafil",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0111-1",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-E-0111-2",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            },
            {
                "interaction_id": "INT-SYN-E-0111-3",
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
        "case_id": "SYN-E-0112",
        "age": 63,
        "labs": {
            "egfr": 60.3,
            "creatinine": 1.2,
            "potassium": 3.8,
            "inr": 1.8
        },
        "diagnoses": [
            "atrial_fibrillation",
            "coronary_artery_disease",
            "anxiety"
        ],
        "medications": [
            "amiodarone",
            "azithromycin",
            "calcium_carbonate",
            "digoxin",
            "metoprolol",
            "paroxetine",
            "prednisone"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0112-1",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-E-0112-2",
                "drug_a": "metoprolol",
                "drug_b": "paroxetine",
                "severity": "moderate",
                "evidence": "CYP2D6 inhibition raises metoprolol exposure"
            },
            {
                "interaction_id": "INT-SYN-E-0112-3",
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
        "case_id": "SYN-E-0113",
        "age": 66,
        "labs": {
            "egfr": 67.3,
            "creatinine": 1.2,
            "potassium": 3.8,
            "inr": 2.6
        },
        "diagnoses": [
            "heart_failure",
            "peripheral_artery_disease"
        ],
        "medications": [
            "amiodarone",
            "ciprofloxacin",
            "diltiazem",
            "sildenafil",
            "simvastatin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0113-1",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-E-0113-2",
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
        "case_id": "SYN-E-0114",
        "age": 61,
        "labs": {
            "egfr": 63.3,
            "creatinine": 1.0,
            "potassium": 3.8,
            "inr": 1.8
        },
        "diagnoses": [
            "depression",
            "gout",
            "dyslipidemia"
        ],
        "medications": [
            "aspirin",
            "azithromycin",
            "glipizide",
            "losartan",
            "naproxen",
            "prednisone",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0114-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0114-2",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            },
            {
                "interaction_id": "INT-SYN-E-0114-3",
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
        "case_id": "SYN-E-0115",
        "age": 64,
        "labs": {
            "egfr": 63.3,
            "creatinine": 1.3,
            "potassium": 4.0,
            "inr": 2.5
        },
        "diagnoses": [
            "hypertension",
            "gout",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "atorvastatin",
            "azithromycin",
            "citalopram",
            "linezolid",
            "metronidazole",
            "sertraline",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0115-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0115-2",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-E-0115-3",
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
        "case_id": "SYN-E-0116",
        "age": 79,
        "labs": {
            "egfr": 86.1,
            "creatinine": 1.0,
            "potassium": 4.2,
            "inr": 1.8
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "heart_failure",
            "anxiety"
        ],
        "medications": [
            "amiodarone",
            "amlodipine",
            "digoxin",
            "furosemide",
            "linezolid",
            "metoprolol",
            "simvastatin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0116-1",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-E-0116-2",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-E-0116-3",
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
        "case_id": "SYN-E-0117",
        "age": 61,
        "labs": {
            "egfr": 77.1,
            "creatinine": 1.3,
            "potassium": 4.0,
            "inr": 2.7
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "anemia",
            "type_2_diabetes"
        ],
        "medications": [
            "amiodarone",
            "digoxin",
            "furosemide",
            "metformin",
            "omeprazole",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0117-1",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-E-0117-2",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-E-0117-3",
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
        "case_id": "SYN-E-0118",
        "age": 77,
        "labs": {
            "egfr": 62.3,
            "creatinine": 0.9,
            "potassium": 4.0,
            "inr": 2.3
        },
        "diagnoses": [
            "heart_failure",
            "chronic_liver_disease",
            "chronic_kidney_disease"
        ],
        "medications": [
            "aspirin",
            "clarithromycin",
            "metronidazole",
            "omeprazole",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0118-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0118-2",
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
        "case_id": "SYN-E-0119",
        "age": 59,
        "labs": {
            "egfr": 71.3,
            "creatinine": 0.8,
            "potassium": 4.0,
            "inr": 2.0
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "hypothyroidism"
        ],
        "medications": [
            "azithromycin",
            "clarithromycin",
            "diclofenac",
            "furosemide",
            "metoprolol",
            "prednisone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0119-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0119-2",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-E-0119-3",
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
        "case_id": "SYN-E-0120",
        "age": 61,
        "labs": {
            "egfr": 77.9,
            "creatinine": 0.8,
            "potassium": 4.4,
            "inr": 1.8
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "gout",
            "hypertension"
        ],
        "medications": [
            "amlodipine",
            "cetirizine",
            "nitroglycerin",
            "paroxetine",
            "sildenafil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0120-1",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-E-0120-2",
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
        "case_id": "SYN-E-0121",
        "age": 77,
        "labs": {
            "egfr": 82.9,
            "creatinine": 0.9,
            "potassium": 3.9,
            "inr": 1.3
        },
        "diagnoses": [
            "chronic_liver_disease",
            "osteoarthritis"
        ],
        "medications": [
            "apixaban",
            "diclofenac",
            "glipizide",
            "omeprazole",
            "ticagrelor"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0121-1",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-E-0121-2",
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
        "case_id": "SYN-E-0122",
        "age": 78,
        "labs": {
            "egfr": 62.5,
            "creatinine": 1.0,
            "potassium": 4.2,
            "inr": 1.3
        },
        "diagnoses": [
            "anxiety",
            "chronic_liver_disease"
        ],
        "medications": [
            "diclofenac",
            "furosemide",
            "ibuprofen",
            "metoprolol",
            "omeprazole",
            "ticagrelor",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0122-1",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-E-0122-2",
                "drug_a": "furosemide",
                "drug_b": "metoprolol",
                "severity": "minor",
                "evidence": "electrolyte shifts may mask metoprolol bradycardia signal"
            },
            {
                "interaction_id": "INT-SYN-E-0122-3",
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
        "case_id": "SYN-E-0123",
        "age": 78,
        "labs": {
            "egfr": 68.6,
            "creatinine": 1.1,
            "potassium": 4.4,
            "inr": 2.5
        },
        "diagnoses": [
            "gout",
            "chronic_kidney_disease"
        ],
        "medications": [
            "azithromycin",
            "ciprofloxacin",
            "citalopram",
            "glipizide",
            "lisinopril",
            "omeprazole",
            "ticagrelor"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0123-1",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-E-0123-2",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-E-0123-3",
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
        "case_id": "SYN-E-0124",
        "age": 63,
        "labs": {
            "egfr": 85.1,
            "creatinine": 1.1,
            "potassium": 4.4,
            "inr": 1.4
        },
        "diagnoses": [
            "atrial_fibrillation",
            "gout"
        ],
        "medications": [
            "azithromycin",
            "citalopram",
            "diclofenac",
            "nitroglycerin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0124-1",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-E-0124-2",
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
        "case_id": "SYN-E-0125",
        "age": 75,
        "labs": {
            "egfr": 87.0,
            "creatinine": 1.2,
            "potassium": 4.6,
            "inr": 2.5
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "osteoarthritis"
        ],
        "medications": [
            "cetirizine",
            "diclofenac",
            "naproxen",
            "rivaroxaban",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0125-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0125-2",
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
        "case_id": "SYN-E-0126",
        "age": 57,
        "labs": {
            "egfr": 77.2,
            "creatinine": 1.3,
            "potassium": 3.9,
            "inr": 1.6
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "hypertension"
        ],
        "medications": [
            "cetirizine",
            "isosorbide_mononitrate",
            "linezolid",
            "metformin",
            "sertraline",
            "sildenafil",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0126-1",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0126-2",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-E-0126-3",
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
        "case_id": "SYN-E-0127",
        "age": 67,
        "labs": {
            "egfr": 68.1,
            "creatinine": 1.3,
            "potassium": 3.9,
            "inr": 1.8
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "osteoarthritis",
            "hypertension"
        ],
        "medications": [
            "amlodipine",
            "isosorbide_mononitrate",
            "ketoconazole",
            "linezolid",
            "lisinopril",
            "sertraline",
            "sildenafil",
            "simvastatin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0127-1",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-E-0127-2",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-E-0127-3",
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
        "case_id": "SYN-E-0128",
        "age": 67,
        "labs": {
            "egfr": 75.1,
            "creatinine": 0.9,
            "potassium": 3.9,
            "inr": 2.5
        },
        "diagnoses": [
            "atrial_fibrillation",
            "anemia",
            "chronic_liver_disease"
        ],
        "medications": [
            "aspirin",
            "azithromycin",
            "ferrous_sulfate",
            "fluconazole",
            "levothyroxine",
            "metoprolol",
            "prednisone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0128-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0128-2",
                "drug_a": "ferrous_sulfate",
                "drug_b": "levothyroxine",
                "severity": "minor",
                "evidence": "iron chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-E-0128-3",
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
        "case_id": "SYN-E-0129",
        "age": 64,
        "labs": {
            "egfr": 85.1,
            "creatinine": 0.9,
            "potassium": 4.5,
            "inr": 1.2
        },
        "diagnoses": [
            "atrial_fibrillation",
            "anxiety",
            "gout"
        ],
        "medications": [
            "apixaban",
            "aspirin",
            "linezolid",
            "naproxen",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0129-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0129-2",
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
        "case_id": "SYN-E-0130",
        "age": 77,
        "labs": {
            "egfr": 60.2,
            "creatinine": 0.8,
            "potassium": 4.4,
            "inr": 2.6
        },
        "diagnoses": [
            "heart_failure",
            "nonalcoholic_steatohepatitis",
            "hypothyroidism"
        ],
        "medications": [
            "azithromycin",
            "citalopram",
            "nitroglycerin",
            "omeprazole",
            "ticagrelor"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0130-1",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-E-0130-2",
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
        "case_id": "SYN-E-0131",
        "age": 75,
        "labs": {
            "egfr": 62.5,
            "creatinine": 0.9,
            "potassium": 3.9,
            "inr": 1.7
        },
        "diagnoses": [
            "chronic_liver_disease",
            "heart_failure",
            "atrial_fibrillation"
        ],
        "medications": [
            "ciprofloxacin",
            "diclofenac",
            "furosemide",
            "metformin",
            "sertraline",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0131-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0131-2",
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
        "case_id": "SYN-E-0132",
        "age": 64,
        "labs": {
            "egfr": 61.0,
            "creatinine": 0.9,
            "potassium": 4.0,
            "inr": 1.3
        },
        "diagnoses": [
            "anemia",
            "anxiety",
            "hypothyroidism"
        ],
        "medications": [
            "amiodarone",
            "digoxin",
            "fluconazole",
            "isosorbide_mononitrate",
            "losartan",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0132-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0132-2",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-E-0132-3",
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
        "case_id": "SYN-E-0133",
        "age": 61,
        "labs": {
            "egfr": 62.6,
            "creatinine": 1.2,
            "potassium": 4.3,
            "inr": 2.1
        },
        "diagnoses": [
            "anemia",
            "type_2_diabetes"
        ],
        "medications": [
            "amlodipine",
            "cetirizine",
            "ibuprofen",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0133-1",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0133-2",
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
        "case_id": "SYN-E-0134",
        "age": 66,
        "labs": {
            "egfr": 89.4,
            "creatinine": 1.1,
            "potassium": 4.2,
            "inr": 1.1
        },
        "diagnoses": [
            "depression",
            "osteoarthritis",
            "dyslipidemia"
        ],
        "medications": [
            "aspirin",
            "ciprofloxacin",
            "clopidogrel",
            "omeprazole",
            "prednisone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0134-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-E-0134-2",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-E-0135",
        "age": 79,
        "labs": {
            "egfr": 74.6,
            "creatinine": 0.9,
            "potassium": 4.0,
            "inr": 2.2
        },
        "diagnoses": [
            "hypertension",
            "osteoarthritis",
            "dyslipidemia"
        ],
        "medications": [
            "aspirin",
            "isosorbide_mononitrate",
            "metformin",
            "sildenafil",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0135-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0135-2",
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
        "case_id": "SYN-E-0136",
        "age": 55,
        "labs": {
            "egfr": 63.7,
            "creatinine": 1.1,
            "potassium": 4.2,
            "inr": 2.8
        },
        "diagnoses": [
            "hypothyroidism",
            "chronic_liver_disease",
            "anxiety"
        ],
        "medications": [
            "amiodarone",
            "atorvastatin",
            "azithromycin",
            "digoxin",
            "diltiazem",
            "ferrous_sulfate",
            "isosorbide_mononitrate",
            "sildenafil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0136-1",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-E-0136-2",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-E-0136-3",
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
        "case_id": "SYN-E-0137",
        "age": 55,
        "labs": {
            "egfr": 64.8,
            "creatinine": 1.0,
            "potassium": 4.4,
            "inr": 2.3
        },
        "diagnoses": [
            "atrial_fibrillation",
            "dyslipidemia",
            "hypertension"
        ],
        "medications": [
            "linezolid",
            "metoprolol",
            "nitroglycerin",
            "paroxetine",
            "sertraline"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0137-1",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-E-0137-2",
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
        "case_id": "SYN-E-0138",
        "age": 75,
        "labs": {
            "egfr": 63.8,
            "creatinine": 1.3,
            "potassium": 4.4,
            "inr": 2.7
        },
        "diagnoses": [
            "chronic_pain",
            "osteoarthritis"
        ],
        "medications": [
            "aspirin",
            "dabigatran",
            "ketoconazole",
            "sertraline",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0138-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-E-0138-2",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "train"
    },
    {
        "case_id": "SYN-E-0139",
        "age": 63,
        "labs": {
            "egfr": 64.2,
            "creatinine": 1.0,
            "potassium": 4.0,
            "inr": 1.7
        },
        "diagnoses": [
            "coronary_artery_disease",
            "dyslipidemia",
            "atrial_fibrillation"
        ],
        "medications": [
            "amlodipine",
            "diltiazem",
            "isosorbide_mononitrate",
            "sildenafil",
            "simvastatin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0139-1",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-E-0139-2",
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
        "case_id": "SYN-E-0140",
        "age": 62,
        "labs": {
            "egfr": 79.1,
            "creatinine": 1.3,
            "potassium": 4.5,
            "inr": 1.7
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "coronary_artery_disease"
        ],
        "medications": [
            "amiodarone",
            "clopidogrel",
            "diclofenac",
            "digoxin",
            "omeprazole"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0140-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-E-0140-2",
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
        "case_id": "SYN-E-0141",
        "age": 62,
        "labs": {
            "egfr": 68.7,
            "creatinine": 1.0,
            "potassium": 3.9,
            "inr": 1.6
        },
        "diagnoses": [
            "depression",
            "anxiety",
            "dyslipidemia"
        ],
        "medications": [
            "aspirin",
            "azithromycin",
            "calcium_carbonate",
            "citalopram",
            "dabigatran",
            "ketoconazole",
            "levothyroxine"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0141-1",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-E-0141-2",
                "drug_a": "levothyroxine",
                "drug_b": "calcium_carbonate",
                "severity": "minor",
                "evidence": "calcium chelation reduces levothyroxine absorption"
            },
            {
                "interaction_id": "INT-SYN-E-0141-3",
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
        "case_id": "SYN-E-0142",
        "age": 57,
        "labs": {
            "egfr": 62.9,
            "creatinine": 1.0,
            "potassium": 4.4,
            "inr": 2.8
        },
        "diagnoses": [
            "anxiety",
            "coronary_artery_disease",
            "gout"
        ],
        "medications": [
            "apixaban",
            "fluconazole",
            "glipizide",
            "lisinopril",
            "naproxen",
            "spironolactone",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0142-1",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0142-2",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0142-3",
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
        "case_id": "SYN-E-0143",
        "age": 60,
        "labs": {
            "egfr": 75.7,
            "creatinine": 1.2,
            "potassium": 4.0,
            "inr": 1.7
        },
        "diagnoses": [
            "hypothyroidism",
            "chronic_pain",
            "osteoarthritis"
        ],
        "medications": [
            "apixaban",
            "aspirin",
            "atorvastatin",
            "dabigatran",
            "furosemide",
            "ketoconazole",
            "naproxen",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0143-1",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0143-2",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-E-0143-3",
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
        "case_id": "SYN-E-0144",
        "age": 78,
        "labs": {
            "egfr": 70.6,
            "creatinine": 1.1,
            "potassium": 4.4,
            "inr": 1.6
        },
        "diagnoses": [
            "osteoarthritis",
            "coronary_artery_disease"
        ],
        "medications": [
            "amiodarone",
            "atorvastatin",
            "calcium_carbonate",
            "ciprofloxacin",
            "levothyroxine",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0144-1",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-E-0144-2",
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
        "case_id": "SYN-E-0145",
        "age": 65,
        "labs": {
            "egfr": 86.9,
            "creatinine": 1.1,
            "potassium": 4.5,
            "inr": 1.1
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "anxiety",
            "chronic_liver_disease"
        ],
        "medications": [
            "amiodarone",
            "amlodipine",
            "ciprofloxacin",
            "digoxin",
            "fluconazole",
            "nitroglycerin",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0145-1",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0145-2",
                "drug_a": "amlodipine",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive hypotension in frail adults"
            },
            {
                "interaction_id": "INT-SYN-E-0145-3",
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
        "case_id": "SYN-E-0146",
        "age": 67,
        "labs": {
            "egfr": 64.7,
            "creatinine": 1.1,
            "potassium": 4.4,
            "inr": 1.1
        },
        "diagnoses": [
            "heart_failure",
            "gout"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "azithromycin",
            "clarithromycin",
            "ketoconazole",
            "metoprolol",
            "paroxetine",
            "prednisone"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0146-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0146-2",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            },
            {
                "interaction_id": "INT-SYN-E-0146-3",
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
        "case_id": "SYN-E-0147",
        "age": 64,
        "labs": {
            "egfr": 83.8,
            "creatinine": 1.3,
            "potassium": 4.1,
            "inr": 1.3
        },
        "diagnoses": [
            "anemia",
            "hypertension",
            "heart_failure"
        ],
        "medications": [
            "azithromycin",
            "ciprofloxacin",
            "citalopram",
            "diclofenac",
            "metoprolol",
            "prednisone",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0147-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0147-2",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            },
            {
                "interaction_id": "INT-SYN-E-0147-3",
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
        "case_id": "SYN-E-0148",
        "age": 71,
        "labs": {
            "egfr": 85.0,
            "creatinine": 1.1,
            "potassium": 4.1,
            "inr": 1.5
        },
        "diagnoses": [
            "heart_failure",
            "gout"
        ],
        "medications": [
            "linezolid",
            "metoprolol",
            "trimethoprim_sulfamethoxazole",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0148-1",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0148-2",
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
        "case_id": "SYN-E-0149",
        "age": 79,
        "labs": {
            "egfr": 67.3,
            "creatinine": 0.9,
            "potassium": 4.4,
            "inr": 2.2
        },
        "diagnoses": [
            "anxiety",
            "anemia"
        ],
        "medications": [
            "apixaban",
            "dabigatran",
            "diclofenac",
            "ketoconazole",
            "linezolid",
            "losartan",
            "naproxen",
            "sertraline"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0149-1",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0149-2",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-E-0149-3",
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
        "case_id": "SYN-E-0150",
        "age": 78,
        "labs": {
            "egfr": 61.0,
            "creatinine": 0.9,
            "potassium": 4.3,
            "inr": 1.9
        },
        "diagnoses": [
            "coronary_artery_disease",
            "atrial_fibrillation",
            "chronic_pain"
        ],
        "medications": [
            "apixaban",
            "clarithromycin",
            "dabigatran",
            "nitroglycerin",
            "prednisone",
            "sildenafil",
            "spironolactone",
            "valsartan"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0150-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0150-2",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            },
            {
                "interaction_id": "INT-SYN-E-0150-3",
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
        "case_id": "SYN-E-0151",
        "age": 74,
        "labs": {
            "egfr": 77.1,
            "creatinine": 1.1,
            "potassium": 4.2,
            "inr": 2.3
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "hypothyroidism",
            "anemia"
        ],
        "medications": [
            "amlodipine",
            "ciprofloxacin",
            "metoprolol",
            "naproxen",
            "rivaroxaban"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0151-1",
                "drug_a": "rivaroxaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "additive anticoagulant-related bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0151-2",
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
        "case_id": "SYN-E-0152",
        "age": 63,
        "labs": {
            "egfr": 70.3,
            "creatinine": 1.3,
            "potassium": 4.5,
            "inr": 2.5
        },
        "diagnoses": [
            "anemia",
            "anxiety",
            "chronic_pain"
        ],
        "medications": [
            "amiodarone",
            "azithromycin",
            "ciprofloxacin",
            "nitroglycerin",
            "prednisone",
            "sildenafil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0152-1",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-E-0152-2",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            },
            {
                "interaction_id": "INT-SYN-E-0152-3",
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
        "case_id": "SYN-E-0153",
        "age": 62,
        "labs": {
            "egfr": 82.2,
            "creatinine": 1.1,
            "potassium": 4.2,
            "inr": 2.1
        },
        "diagnoses": [
            "hypothyroidism",
            "osteoarthritis"
        ],
        "medications": [
            "amiodarone",
            "amlodipine",
            "dabigatran",
            "ketoconazole",
            "losartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0153-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-E-0153-2",
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
        "case_id": "SYN-E-0154",
        "age": 60,
        "labs": {
            "egfr": 74.6,
            "creatinine": 0.9,
            "potassium": 4.1,
            "inr": 1.9
        },
        "diagnoses": [
            "osteoarthritis",
            "chronic_kidney_disease",
            "hypertension"
        ],
        "medications": [
            "calcium_carbonate",
            "dabigatran",
            "ketoconazole",
            "metoprolol",
            "trimethoprim_sulfamethoxazole",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0154-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-E-0154-2",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0154-3",
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
        "case_id": "SYN-E-0155",
        "age": 73,
        "labs": {
            "egfr": 74.1,
            "creatinine": 1.1,
            "potassium": 4.4,
            "inr": 2.5
        },
        "diagnoses": [
            "type_2_diabetes",
            "chronic_kidney_disease"
        ],
        "medications": [
            "calcium_carbonate",
            "ciprofloxacin",
            "diltiazem",
            "glipizide",
            "isosorbide_mononitrate",
            "sildenafil",
            "simvastatin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0155-1",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-E-0155-2",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-E-0155-3",
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
        "case_id": "SYN-E-0156",
        "age": 73,
        "labs": {
            "egfr": 87.7,
            "creatinine": 1.1,
            "potassium": 4.3,
            "inr": 1.9
        },
        "diagnoses": [
            "type_2_diabetes",
            "dyslipidemia"
        ],
        "medications": [
            "ciprofloxacin",
            "dabigatran",
            "fluconazole",
            "sertraline",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0156-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-0156-2",
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
        "case_id": "SYN-E-0157",
        "age": 61,
        "labs": {
            "egfr": 63.6,
            "creatinine": 0.8,
            "potassium": 4.2,
            "inr": 2.3
        },
        "diagnoses": [
            "atrial_fibrillation",
            "gout",
            "dyslipidemia"
        ],
        "medications": [
            "amiodarone",
            "azithromycin",
            "ciprofloxacin",
            "citalopram",
            "metformin",
            "nitroglycerin",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0157-1",
                "drug_a": "warfarin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "CYP inhibition elevates warfarin exposure"
            },
            {
                "interaction_id": "INT-SYN-E-0157-2",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-E-0157-3",
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
        "case_id": "SYN-E-0158",
        "age": 68,
        "labs": {
            "egfr": 61.4,
            "creatinine": 1.1,
            "potassium": 4.2,
            "inr": 1.2
        },
        "diagnoses": [
            "anxiety",
            "coronary_artery_disease",
            "depression"
        ],
        "medications": [
            "dabigatran",
            "ketoconazole",
            "nitroglycerin",
            "rivaroxaban",
            "sildenafil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0158-1",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-E-0158-2",
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
        "case_id": "SYN-E-0159",
        "age": 79,
        "labs": {
            "egfr": 87.7,
            "creatinine": 1.2,
            "potassium": 3.9,
            "inr": 1.9
        },
        "diagnoses": [
            "type_2_diabetes",
            "hypertension"
        ],
        "medications": [
            "dabigatran",
            "furosemide",
            "isosorbide_mononitrate",
            "ketoconazole",
            "omeprazole",
            "prednisone",
            "sildenafil",
            "ticagrelor"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0159-1",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-E-0159-2",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-E-0159-3",
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
        "case_id": "SYN-E-0160",
        "age": 62,
        "labs": {
            "egfr": 71.7,
            "creatinine": 1.2,
            "potassium": 4.2,
            "inr": 2.1
        },
        "diagnoses": [
            "osteoarthritis",
            "chronic_kidney_disease",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "dabigatran",
            "ibuprofen",
            "ketoconazole",
            "nitroglycerin",
            "sildenafil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-0160-1",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-E-0160-2",
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
        "case_id": "SYN-E-V0001",
        "age": 67,
        "labs": {
            "egfr": 78.2,
            "creatinine": 0.8,
            "potassium": 4.0,
            "inr": 1.6
        },
        "diagnoses": [
            "dyslipidemia",
            "hypothyroidism"
        ],
        "medications": [
            "allopurinol",
            "aspirin",
            "dabigatran",
            "digoxin",
            "ketoconazole",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-V0001-1",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-E-V0001-2",
                "drug_a": "digoxin",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "P-gp inhibition can raise digoxin concentration"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::easy-SYN-E-V0001"
    },
    {
        "case_id": "SYN-E-V0002",
        "age": 72,
        "labs": {
            "egfr": 68.9,
            "creatinine": 1.1,
            "potassium": 3.8,
            "inr": 2.1
        },
        "diagnoses": [
            "anxiety",
            "osteoarthritis"
        ],
        "medications": [
            "losartan",
            "metformin",
            "metronidazole",
            "naproxen",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-V0002-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-V0002-2",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::easy-SYN-E-V0002"
    },
    {
        "case_id": "SYN-E-V0003",
        "age": 79,
        "labs": {
            "egfr": 73.1,
            "creatinine": 1.3,
            "potassium": 4.3,
            "inr": 1.6
        },
        "diagnoses": [
            "coronary_artery_disease",
            "depression",
            "dyslipidemia"
        ],
        "medications": [
            "ciprofloxacin",
            "dabigatran",
            "ketoconazole",
            "losartan",
            "metronidazole",
            "nitroglycerin",
            "sildenafil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-V0003-1",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-E-V0003-2",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            },
            {
                "interaction_id": "INT-SYN-E-V0003-3",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::easy-SYN-E-V0003"
    },
    {
        "case_id": "SYN-E-V0004",
        "age": 71,
        "labs": {
            "egfr": 67.7,
            "creatinine": 0.9,
            "potassium": 4.4,
            "inr": 1.5
        },
        "diagnoses": [
            "coronary_artery_disease",
            "chronic_pain",
            "dyslipidemia"
        ],
        "medications": [
            "amiodarone",
            "diclofenac",
            "metformin",
            "nitroglycerin",
            "sildenafil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-V0004-1",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-E-V0004-2",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::easy-SYN-E-V0004"
    },
    {
        "case_id": "SYN-E-V0005",
        "age": 68,
        "labs": {
            "egfr": 72.1,
            "creatinine": 1.3,
            "potassium": 4.5,
            "inr": 1.9
        },
        "diagnoses": [
            "nonalcoholic_steatohepatitis",
            "osteoarthritis",
            "chronic_liver_disease"
        ],
        "medications": [
            "apixaban",
            "ciprofloxacin",
            "isosorbide_mononitrate",
            "linezolid",
            "metformin",
            "naproxen",
            "sertraline",
            "sildenafil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-V0005-1",
                "drug_a": "isosorbide_mononitrate",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "severe hypotension risk with combined nitrate-PDE5 inhibition"
            },
            {
                "interaction_id": "INT-SYN-E-V0005-2",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-V0005-3",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::easy-SYN-E-V0005"
    },
    {
        "case_id": "SYN-E-V0006",
        "age": 55,
        "labs": {
            "egfr": 78.8,
            "creatinine": 1.2,
            "potassium": 4.3,
            "inr": 1.5
        },
        "diagnoses": [
            "atrial_fibrillation",
            "anxiety",
            "hypertension"
        ],
        "medications": [
            "amiodarone",
            "aspirin",
            "ciprofloxacin",
            "digoxin",
            "diltiazem",
            "metronidazole",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-V0006-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-V0006-2",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-E-V0006-3",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::easy-SYN-E-V0006"
    },
    {
        "case_id": "SYN-E-V0007",
        "age": 59,
        "labs": {
            "egfr": 76.4,
            "creatinine": 1.2,
            "potassium": 4.0,
            "inr": 1.4
        },
        "diagnoses": [
            "hypothyroidism",
            "nonalcoholic_steatohepatitis",
            "type_2_diabetes"
        ],
        "medications": [
            "amiodarone",
            "apixaban",
            "diclofenac",
            "digoxin",
            "ketoconazole",
            "metformin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-V0007-1",
                "drug_a": "apixaban",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-V0007-2",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::easy-SYN-E-V0007"
    },
    {
        "case_id": "SYN-E-V0008",
        "age": 73,
        "labs": {
            "egfr": 65.8,
            "creatinine": 0.9,
            "potassium": 4.2,
            "inr": 2.6
        },
        "diagnoses": [
            "dyslipidemia",
            "chronic_pain",
            "heart_failure"
        ],
        "medications": [
            "apixaban",
            "clopidogrel",
            "digoxin",
            "linezolid",
            "losartan",
            "naproxen",
            "sertraline",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-V0008-1",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-V0008-2",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-E-V0008-3",
                "drug_a": "verapamil",
                "drug_b": "losartan",
                "severity": "minor",
                "evidence": "possible additive hypotensive effect"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::easy-SYN-E-V0008"
    },
    {
        "case_id": "SYN-E-V0009",
        "age": 60,
        "labs": {
            "egfr": 72.5,
            "creatinine": 1.0,
            "potassium": 4.4,
            "inr": 1.5
        },
        "diagnoses": [
            "coronary_artery_disease",
            "anemia",
            "gout"
        ],
        "medications": [
            "apixaban",
            "digoxin",
            "metoprolol",
            "metronidazole",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-V0009-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-V0009-2",
                "drug_a": "digoxin",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "P-gp inhibition can raise digoxin concentration"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::easy-SYN-E-V0009"
    },
    {
        "case_id": "SYN-E-V0010",
        "age": 77,
        "labs": {
            "egfr": 71.0,
            "creatinine": 1.2,
            "potassium": 3.9,
            "inr": 1.3
        },
        "diagnoses": [
            "coronary_artery_disease",
            "chronic_kidney_disease"
        ],
        "medications": [
            "amlodipine",
            "glipizide",
            "losartan",
            "metoprolol",
            "nitroglycerin",
            "sildenafil",
            "simvastatin",
            "spironolactone"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-V0010-1",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            },
            {
                "interaction_id": "INT-SYN-E-V0010-2",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-E-V0010-3",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::easy-SYN-E-V0010"
    },
    {
        "case_id": "SYN-E-V0011",
        "age": 76,
        "labs": {
            "egfr": 64.9,
            "creatinine": 1.0,
            "potassium": 4.0,
            "inr": 1.4
        },
        "diagnoses": [
            "atrial_fibrillation",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "azithromycin",
            "citalopram",
            "clarithromycin",
            "fluconazole",
            "nitroglycerin",
            "sildenafil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-V0011-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-V0011-2",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-E-V0011-3",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::easy-SYN-E-V0011"
    },
    {
        "case_id": "SYN-E-V0012",
        "age": 78,
        "labs": {
            "egfr": 64.7,
            "creatinine": 1.0,
            "potassium": 4.4,
            "inr": 2.4
        },
        "diagnoses": [
            "anxiety",
            "osteoarthritis",
            "hypertension"
        ],
        "medications": [
            "azithromycin",
            "citalopram",
            "diltiazem",
            "furosemide",
            "metformin",
            "metronidazole",
            "simvastatin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-V0012-1",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            },
            {
                "interaction_id": "INT-SYN-E-V0012-2",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-E-V0012-3",
                "drug_a": "metformin",
                "drug_b": "furosemide",
                "severity": "moderate",
                "evidence": "reduced renal clearance can increase lactic acidosis risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::easy-SYN-E-V0012"
    },
    {
        "case_id": "SYN-E-V0013",
        "age": 76,
        "labs": {
            "egfr": 70.9,
            "creatinine": 1.2,
            "potassium": 3.9,
            "inr": 1.1
        },
        "diagnoses": [
            "hypertension",
            "gout",
            "peripheral_artery_disease"
        ],
        "medications": [
            "apixaban",
            "aspirin",
            "ciprofloxacin",
            "clarithromycin",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-V0013-1",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-V0013-2",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::easy-SYN-E-V0013"
    },
    {
        "case_id": "SYN-E-V0014",
        "age": 59,
        "labs": {
            "egfr": 64.5,
            "creatinine": 1.2,
            "potassium": 4.4,
            "inr": 1.5
        },
        "diagnoses": [
            "gout",
            "nonalcoholic_steatohepatitis",
            "type_2_diabetes"
        ],
        "medications": [
            "apixaban",
            "azithromycin",
            "clarithromycin",
            "diclofenac",
            "prednisone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-V0014-1",
                "drug_a": "warfarin",
                "drug_b": "diclofenac",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-V0014-2",
                "drug_a": "prednisone",
                "drug_b": "azithromycin",
                "severity": "minor",
                "evidence": "minor QT prolongation risk in elderly"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::easy-SYN-E-V0014"
    },
    {
        "case_id": "SYN-E-V0015",
        "age": 65,
        "labs": {
            "egfr": 86.9,
            "creatinine": 1.3,
            "potassium": 4.5,
            "inr": 2.4
        },
        "diagnoses": [
            "osteoarthritis",
            "anxiety"
        ],
        "medications": [
            "azithromycin",
            "citalopram",
            "diltiazem",
            "ibuprofen",
            "lisinopril",
            "rivaroxaban",
            "simvastatin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-V0015-1",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-V0015-2",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            },
            {
                "interaction_id": "INT-SYN-E-V0015-3",
                "drug_a": "citalopram",
                "drug_b": "azithromycin",
                "severity": "major",
                "evidence": "QT prolongation risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::easy-SYN-E-V0015"
    },
    {
        "case_id": "SYN-E-V0016",
        "age": 58,
        "labs": {
            "egfr": 87.6,
            "creatinine": 1.0,
            "potassium": 4.2,
            "inr": 2.4
        },
        "diagnoses": [
            "heart_failure",
            "hypothyroidism",
            "anxiety"
        ],
        "medications": [
            "apixaban",
            "aspirin",
            "naproxen",
            "sertraline",
            "valsartan"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-V0016-1",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-V0016-2",
                "drug_a": "aspirin",
                "drug_b": "sertraline",
                "severity": "minor",
                "evidence": "increased bleeding tendency, amplified in frailty"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::easy-SYN-E-V0016"
    },
    {
        "case_id": "SYN-E-V0017",
        "age": 60,
        "labs": {
            "egfr": 86.7,
            "creatinine": 1.0,
            "potassium": 4.3,
            "inr": 1.9
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "coronary_artery_disease",
            "heart_failure"
        ],
        "medications": [
            "amiodarone",
            "ciprofloxacin",
            "digoxin",
            "losartan",
            "spironolactone",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-V0017-1",
                "drug_a": "digoxin",
                "drug_b": "amiodarone",
                "severity": "major",
                "evidence": "P-gp inhibition raises digoxin concentration"
            },
            {
                "interaction_id": "INT-SYN-E-V0017-2",
                "drug_a": "spironolactone",
                "drug_b": "losartan",
                "severity": "moderate",
                "evidence": "combined potassium retention"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::easy-SYN-E-V0017"
    },
    {
        "case_id": "SYN-E-V0018",
        "age": 73,
        "labs": {
            "egfr": 61.3,
            "creatinine": 0.9,
            "potassium": 4.5,
            "inr": 2.1
        },
        "diagnoses": [
            "chronic_pain",
            "dyslipidemia"
        ],
        "medications": [
            "amlodipine",
            "ciprofloxacin",
            "diclofenac",
            "digoxin",
            "diltiazem",
            "metronidazole",
            "simvastatin",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-V0018-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-V0018-2",
                "drug_a": "amlodipine",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive hypotension in frail adults"
            },
            {
                "interaction_id": "INT-SYN-E-V0018-3",
                "drug_a": "simvastatin",
                "drug_b": "diltiazem",
                "severity": "moderate",
                "evidence": "increased statin exposure and myopathy risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::easy-SYN-E-V0018"
    },
    {
        "case_id": "SYN-E-V0019",
        "age": 76,
        "labs": {
            "egfr": 81.4,
            "creatinine": 1.1,
            "potassium": 4.3,
            "inr": 2.5
        },
        "diagnoses": [
            "dyslipidemia",
            "nonalcoholic_steatohepatitis"
        ],
        "medications": [
            "clopidogrel",
            "fluconazole",
            "losartan",
            "omeprazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-V0019-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-V0019-2",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::easy-SYN-E-V0019"
    },
    {
        "case_id": "SYN-E-V0020",
        "age": 59,
        "labs": {
            "egfr": 80.0,
            "creatinine": 1.3,
            "potassium": 4.0,
            "inr": 1.6
        },
        "diagnoses": [
            "depression",
            "coronary_artery_disease",
            "dyslipidemia"
        ],
        "medications": [
            "allopurinol",
            "dabigatran",
            "ketoconazole",
            "nitroglycerin",
            "omeprazole",
            "ticagrelor"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-V0020-1",
                "drug_a": "ticagrelor",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "potential reduction in antiplatelet effectiveness"
            },
            {
                "interaction_id": "INT-SYN-E-V0020-2",
                "drug_a": "dabigatran",
                "drug_b": "ketoconazole",
                "severity": "major",
                "evidence": "P-gp inhibition raises dabigatran exposure"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::easy-SYN-E-V0020"
    },
    {
        "case_id": "SYN-E-V0021",
        "age": 68,
        "labs": {
            "egfr": 68.4,
            "creatinine": 0.9,
            "potassium": 4.0,
            "inr": 1.4
        },
        "diagnoses": [
            "hypothyroidism",
            "osteoarthritis"
        ],
        "medications": [
            "calcium_carbonate",
            "metronidazole",
            "spironolactone",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-V0021-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-V0021-2",
                "drug_a": "spironolactone",
                "drug_b": "valsartan",
                "severity": "moderate",
                "evidence": "severe hyperkalemia risk in advanced CKD"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::easy-SYN-E-V0021"
    },
    {
        "case_id": "SYN-E-V0022",
        "age": 73,
        "labs": {
            "egfr": 82.6,
            "creatinine": 1.2,
            "potassium": 4.6,
            "inr": 2.2
        },
        "diagnoses": [
            "depression",
            "nonalcoholic_steatohepatitis",
            "chronic_pain"
        ],
        "medications": [
            "digoxin",
            "ibuprofen",
            "levothyroxine",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-V0022-1",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-V0022-2",
                "drug_a": "digoxin",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "P-gp inhibition can raise digoxin concentration"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::easy-SYN-E-V0022"
    },
    {
        "case_id": "SYN-E-V0023",
        "age": 62,
        "labs": {
            "egfr": 79.4,
            "creatinine": 1.2,
            "potassium": 4.1,
            "inr": 1.3
        },
        "diagnoses": [
            "dyslipidemia",
            "depression"
        ],
        "medications": [
            "amlodipine",
            "apixaban",
            "losartan",
            "naproxen",
            "simvastatin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-V0023-1",
                "drug_a": "apixaban",
                "drug_b": "naproxen",
                "severity": "major",
                "evidence": "substantial additive bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-V0023-2",
                "drug_a": "simvastatin",
                "drug_b": "amlodipine",
                "severity": "moderate",
                "evidence": "higher statin exposure and myopathy risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::easy-SYN-E-V0023"
    },
    {
        "case_id": "SYN-E-V0024",
        "age": 79,
        "labs": {
            "egfr": 84.4,
            "creatinine": 1.0,
            "potassium": 4.5,
            "inr": 1.8
        },
        "diagnoses": [
            "nonalcoholic_steatohepatitis",
            "anxiety",
            "peripheral_artery_disease"
        ],
        "medications": [
            "digoxin",
            "fluconazole",
            "ketoconazole",
            "linezolid",
            "sertraline",
            "sildenafil",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-V0024-1",
                "drug_a": "warfarin",
                "drug_b": "fluconazole",
                "severity": "contraindicated",
                "evidence": "major CYP-mediated INR increase and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-V0024-2",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-E-V0024-3",
                "drug_a": "digoxin",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "P-gp inhibition can raise digoxin concentration"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::easy-SYN-E-V0024"
    },
    {
        "case_id": "SYN-E-V0025",
        "age": 75,
        "labs": {
            "egfr": 67.4,
            "creatinine": 1.0,
            "potassium": 4.5,
            "inr": 1.3
        },
        "diagnoses": [
            "chronic_liver_disease",
            "coronary_artery_disease"
        ],
        "medications": [
            "apixaban",
            "clarithromycin",
            "ibuprofen",
            "omeprazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-V0025-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-V0025-2",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::easy-SYN-E-V0025"
    },
    {
        "case_id": "SYN-E-V0026",
        "age": 73,
        "labs": {
            "egfr": 67.7,
            "creatinine": 0.9,
            "potassium": 4.5,
            "inr": 1.9
        },
        "diagnoses": [
            "peripheral_artery_disease",
            "chronic_kidney_disease",
            "heart_failure"
        ],
        "medications": [
            "aspirin",
            "linezolid",
            "sertraline",
            "trimethoprim_sulfamethoxazole",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-V0026-1",
                "drug_a": "linezolid",
                "drug_b": "sertraline",
                "severity": "major",
                "evidence": "serotonin syndrome risk"
            },
            {
                "interaction_id": "INT-SYN-E-V0026-2",
                "drug_a": "warfarin",
                "drug_b": "aspirin",
                "severity": "major",
                "evidence": "additive anticoagulation and bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::easy-SYN-E-V0026"
    },
    {
        "case_id": "SYN-E-V0027",
        "age": 79,
        "labs": {
            "egfr": 66.4,
            "creatinine": 0.9,
            "potassium": 3.9,
            "inr": 1.1
        },
        "diagnoses": [
            "depression",
            "anxiety"
        ],
        "medications": [
            "ciprofloxacin",
            "ibuprofen",
            "linezolid",
            "sertraline",
            "verapamil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-V0027-1",
                "drug_a": "warfarin",
                "drug_b": "ibuprofen",
                "severity": "major",
                "evidence": "substantial GI and systemic bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-V0027-2",
                "drug_a": "verapamil",
                "drug_b": "ciprofloxacin",
                "severity": "minor",
                "evidence": "possible additive conduction slowing"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::easy-SYN-E-V0027"
    },
    {
        "case_id": "SYN-E-V0028",
        "age": 58,
        "labs": {
            "egfr": 64.4,
            "creatinine": 1.0,
            "potassium": 4.1,
            "inr": 2.1
        },
        "diagnoses": [
            "anxiety",
            "hypertension",
            "heart_failure"
        ],
        "medications": [
            "clopidogrel",
            "omeprazole",
            "sertraline",
            "trimethoprim_sulfamethoxazole",
            "valsartan",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-V0028-1",
                "drug_a": "clopidogrel",
                "drug_b": "omeprazole",
                "severity": "major",
                "evidence": "reduced clopidogrel activation and antiplatelet efficacy"
            },
            {
                "interaction_id": "INT-SYN-E-V0028-2",
                "drug_a": "warfarin",
                "drug_b": "trimethoprim_sulfamethoxazole",
                "severity": "contraindicated",
                "evidence": "marked INR elevation and severe bleeding risk"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::easy-SYN-E-V0028"
    },
    {
        "case_id": "SYN-E-V0029",
        "age": 70,
        "labs": {
            "egfr": 84.9,
            "creatinine": 1.0,
            "potassium": 4.2,
            "inr": 2.5
        },
        "diagnoses": [
            "chronic_kidney_disease",
            "anxiety"
        ],
        "medications": [
            "amlodipine",
            "diclofenac",
            "metronidazole",
            "nitroglycerin",
            "sildenafil",
            "warfarin"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-V0029-1",
                "drug_a": "warfarin",
                "drug_b": "metronidazole",
                "severity": "contraindicated",
                "evidence": "substantial INR increase and severe bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-V0029-2",
                "drug_a": "nitroglycerin",
                "drug_b": "sildenafil",
                "severity": "contraindicated",
                "evidence": "profound hypotension risk from combined vasodilation"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::easy-SYN-E-V0029"
    },
    {
        "case_id": "SYN-E-V0030",
        "age": 69,
        "labs": {
            "egfr": 75.3,
            "creatinine": 1.1,
            "potassium": 4.5,
            "inr": 2.8
        },
        "diagnoses": [
            "chronic_pain",
            "heart_failure"
        ],
        "medications": [
            "apixaban",
            "clarithromycin",
            "losartan",
            "metoprolol",
            "verapamil"
        ],
        "interactions": [
            {
                "interaction_id": "INT-SYN-E-V0030-1",
                "drug_a": "apixaban",
                "drug_b": "clarithromycin",
                "severity": "major",
                "evidence": "increased anticoagulant exposure and bleeding risk"
            },
            {
                "interaction_id": "INT-SYN-E-V0030-2",
                "drug_a": "metoprolol",
                "drug_b": "verapamil",
                "severity": "moderate",
                "evidence": "additive AV nodal blockade and bradycardia"
            }
        ],
        "required_regimens": [],
        "substitution_options": [],
        "split": "validation",
        "template_family": "synth-val::easy-SYN-E-V0030"
    }
]

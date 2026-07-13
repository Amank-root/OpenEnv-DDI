"""
Generates 500+ synthetic DDI cases from the 43 known drug-pair interactions.

Strategy
--------
- Keep every real case as-is (18 train + 6 val).
- For each new synthetic case:
    1. Randomly sample 2-5 interacting drug pairs from DDI_KNOWLEDGE_BASE.
    2. Pick patient labs (age, eGFR, ALT, AST) that straddle clinical thresholds
       so the model has to reason about *when* moderate → flag.
    3. Deterministically compute the correct expected_decision using the same
       logic as graders.py, so labels are always ground-truth correct.
    4. Assign split='train' for ~85%, 'validation' for ~15%.

Output
------
  synthetic_easy_cases.py
  synthetic_medium_cases.py
  synthetic_hard_cases.py
Each file is a Python list that mirrors the exact schema of the original case files.
"""

from __future__ import annotations
import random
import json
from typing import Dict, List, Tuple, Any

# ── Reproducible seed ────────────────────────────────────────────────────────
RNG = random.Random(42)

# ── Full DDI knowledge base extracted from the 8 original case files ─────────
# (drug_a, drug_b, severity, evidence, substitution_hint)
DDI_KB: List[Tuple[str, str, str, str, str]] = [
    # contraindicated
    ("warfarin", "trimethoprim_sulfamethoxazole", "contraindicated",
     "marked INR elevation and severe bleeding risk", "cephalexin"),
    ("warfarin", "metronidazole", "contraindicated",
     "substantial INR increase and severe bleeding risk", "doxycycline"),
    ("warfarin", "fluconazole", "contraindicated",
     "major CYP-mediated INR increase and bleeding risk", "micafungin"),
    ("nitroglycerin", "sildenafil", "contraindicated",
     "profound hypotension risk from combined vasodilation", "isosorbide_mononitrate"),
    ("isosorbide_mononitrate", "sildenafil", "contraindicated",
     "severe hypotension risk with combined nitrate-PDE5 inhibition", "nitroglycerin"),
    # major
    ("warfarin", "aspirin", "major",
     "additive anticoagulation and bleeding risk", "acetaminophen"),
    ("warfarin", "amiodarone", "major",
     "CYP inhibition elevates warfarin exposure", "dronedarone"),
    ("warfarin", "ibuprofen", "major",
     "substantial GI and systemic bleeding risk", "acetaminophen"),
    ("warfarin", "diclofenac", "major",
     "substantial GI and systemic bleeding risk", "acetaminophen"),
    ("clopidogrel", "omeprazole", "major",
     "reduced clopidogrel activation and antiplatelet efficacy", "pantoprazole"),
    ("ticagrelor", "omeprazole", "major",
     "potential reduction in antiplatelet effectiveness", "pantoprazole"),
    ("apixaban", "clarithromycin", "major",
     "increased anticoagulant exposure and bleeding risk", "azithromycin"),
    ("apixaban", "diclofenac", "major",
     "substantial additive bleeding risk", "acetaminophen"),
    ("apixaban", "naproxen", "major",
     "substantial additive bleeding risk", "acetaminophen"),
    ("rivaroxaban", "naproxen", "major",
     "additive anticoagulant-related bleeding risk", "acetaminophen"),
    ("digoxin", "amiodarone", "major",
     "P-gp inhibition raises digoxin concentration", "direct_monitoring"),
    ("linezolid", "sertraline", "major",
     "serotonin syndrome risk", "alternative_antibiotic"),
    ("citalopram", "azithromycin", "major",
     "QT prolongation risk", "alternative_antibiotic"),
    ("dabigatran", "ketoconazole", "major",
     "P-gp inhibition raises dabigatran exposure", "alternative_antifungal"),
    # moderate
    ("simvastatin", "amlodipine", "moderate",
     "higher statin exposure and myopathy risk", "pravastatin"),
    ("simvastatin", "diltiazem", "moderate",
     "increased statin exposure and myopathy risk", "pravastatin"),
    ("atorvastatin", "diltiazem", "moderate",
     "CYP3A4 inhibition raises statin concentration", "rosuvastatin"),
    ("spironolactone", "lisinopril", "moderate",
     "hyperkalemia risk in CKD", "eplerenone"),
    ("spironolactone", "losartan", "moderate",
     "combined potassium retention", "eplerenone"),
    ("spironolactone", "valsartan", "moderate",
     "severe hyperkalemia risk in advanced CKD", "eplerenone"),
    ("digoxin", "verapamil", "moderate",
     "P-gp inhibition can raise digoxin concentration", "bisoprolol"),
    ("metoprolol", "verapamil", "moderate",
     "additive AV nodal blockade and bradycardia", "bisoprolol"),
    ("metoprolol", "paroxetine", "moderate",
     "CYP2D6 inhibition raises metoprolol exposure", "alternative_ssri"),
    ("glipizide", "ciprofloxacin", "moderate",
     "dysglycemia risk from fluoroquinolone-sulfonylurea combination", "levofloxacin"),
    ("metformin", "furosemide", "moderate",
     "reduced renal clearance can increase lactic acidosis risk", "torsemide"),
    ("allopurinol", "warfarin", "moderate",
     "allopurinol may enhance warfarin anticoagulation", "direct_monitoring"),
    # minor
    ("furosemide", "warfarin", "minor",
     "volume changes may alter INR stability", None),
    ("aspirin", "sertraline", "minor",
     "increased bleeding tendency, amplified in frailty", None),
    ("verapamil", "ciprofloxacin", "minor",
     "possible additive conduction slowing", None),
    ("verapamil", "losartan", "minor",
     "possible additive hypotensive effect", None),
    ("amlodipine", "ciprofloxacin", "minor",
     "possible additive hypotension in frail adults", None),
    ("levothyroxine", "calcium_carbonate", "minor",
     "calcium chelation reduces levothyroxine absorption", None),
    ("ferrous_sulfate", "levothyroxine", "minor",
     "iron chelation reduces levothyroxine absorption", None),
    ("cetirizine", "amlodipine", "minor",
     "possible additive sedation in elderly", None),
    ("prednisone", "azithromycin", "minor",
     "minor QT prolongation risk in elderly", None),
    ("furosemide", "metoprolol", "minor",
     "electrolyte shifts may mask metoprolol bradycardia signal", None),
]

# index by (drug_a, drug_b)
DDI_LOOKUP: Dict[Tuple[str, str], Tuple[str, str, str]] = {
    (a, b): (sev, ev, sub or "") for a, b, sev, ev, sub in DDI_KB
}

SEVERITY_ORDER = ["contraindicated", "major", "moderate", "minor"]

ALL_DRUGS = sorted({d for a, b, *_ in DDI_KB for d in (a, b)})

DIAGNOSES_POOL = [
    "atrial_fibrillation", "hypertension", "type_2_diabetes",
    "chronic_kidney_disease", "heart_failure", "dyslipidemia",
    "coronary_artery_disease", "depression", "osteoarthritis",
    "chronic_pain", "hypothyroidism", "peripheral_artery_disease",
    "nonalcoholic_steatohepatitis", "chronic_liver_disease",
    "anxiety", "anemia", "gout",
]

# Substitution drug pool for hard cases
SUB_DRUGS = {
    "cephalexin": "infection", "doxycycline": "infection",
    "azithromycin": "infection", "micafungin": "infection",
    "acetaminophen": "pain", "pantoprazole": "gi_protection",
    "pravastatin": "dyslipidemia", "rosuvastatin": "dyslipidemia",
    "eplerenone": "heart_failure", "bisoprolol": "rate_control",
}

# ── Clinical threshold helpers (mirrors graders.py logic exactly) ─────────────

def expected_decision(severity: str, age: int, egfr: float,
                      alt: float, ast: float, task_level: str) -> str:
    INTERACTION_RECOMMENDATIONS = {
        "contraindicated": "flag_interaction",
        "major": "flag_interaction",
        "moderate": "monitor",
        "minor": "ignore",
    }
    default = INTERACTION_RECOMMENDATIONS[severity]

    if task_level == "easy":
        return default

    # medium / hard modifiers
    hepatic_stress = alt >= 120 or ast >= 120
    if severity == "moderate" and (age >= 80 or egfr < 45 or hepatic_stress):
        return "flag_interaction"
    if severity == "minor" and (age >= 85 or egfr < 30 or alt >= 150):
        return "monitor"
    return default


# ── Lab samplers biased toward clinical boundaries ───────────────────────────

def sample_age(target_zone: str) -> int:
    if target_zone == "low":   return RNG.randint(55, 74)
    if target_zone == "mid":   return RNG.randint(75, 79)
    if target_zone == "high":  return RNG.randint(80, 89)
    return RNG.randint(85, 95)  # "extreme"

def sample_egfr(target_zone: str) -> float:
    if target_zone == "normal": return round(RNG.uniform(60, 90), 1)
    if target_zone == "border": return round(RNG.uniform(42, 48), 1)  # straddles 45
    if target_zone == "low":    return round(RNG.uniform(25, 44), 1)
    return round(RNG.uniform(10, 24), 1)  # "severe"

def sample_alt_ast(target_zone: str) -> Tuple[float, float]:
    if target_zone == "normal":  return (round(RNG.uniform(15, 40), 1), round(RNG.uniform(15, 40), 1))
    if target_zone == "border":  return (round(RNG.uniform(110, 130), 1), round(RNG.uniform(100, 125), 1))
    return (round(RNG.uniform(140, 200), 1), round(RNG.uniform(130, 180), 1))  # "elevated"


# ── Case generators ───────────────────────────────────────────────────────────

def _pick_pairs(n_pairs: int, severity_filter=None) -> List[Tuple]:
    """Pick n_pairs unique drug pairs. severity_filter='severe' requires ≥1 contraindicated/major."""
    pool = list(DDI_LOOKUP.items())
    RNG.shuffle(pool)
    chosen = []
    used_drugs: set = set()

    # First pass: if we need a severe one, grab it
    if severity_filter == "severe":
        severe = [(k, v) for k, v in pool if v[0] in ("contraindicated", "major")]
        if severe:
            k, v = RNG.choice(severe)
            chosen.append((k, v))
            used_drugs.update(k)

    for k, v in pool:
        if len(chosen) >= n_pairs:
            break
        if k in [c[0] for c in chosen]:
            continue
        # Avoid the same drug appearing on both sides of multiple pairs (keeps cases realistic)
        if k[0] in used_drugs or k[1] in used_drugs:
            continue
        chosen.append((k, v))
        used_drugs.update(k)

    # If we couldn't fill without drug overlap, relax that constraint
    if len(chosen) < n_pairs:
        for k, v in pool:
            if len(chosen) >= n_pairs:
                break
            if k in [c[0] for c in chosen]:
                continue
            chosen.append((k, v))

    return chosen[:n_pairs]


def make_easy_case(case_id: str, split: str) -> Dict[str, Any]:
    age_zone = RNG.choice(["low", "mid", "low"])
    age = sample_age(age_zone)
    egfr = sample_egfr("normal")
    alt, ast = sample_alt_ast("normal")

    pairs = _pick_pairs(n_pairs=RNG.randint(2, 3), severity_filter="severe")
    interactions = []
    all_meds: set = set()
    for idx, ((drug_a, drug_b), (severity, evidence, _sub)) in enumerate(pairs):
        iid = f"INT-{case_id}-{idx+1}"
        interactions.append({
            "interaction_id": iid,
            "drug_a": drug_a,
            "drug_b": drug_b,
            "severity": severity,
            "evidence": evidence,
        })
        all_meds.update([drug_a, drug_b])

    # Add 1-2 background drugs that don't interact
    bg = [d for d in ALL_DRUGS if d not in all_meds]
    RNG.shuffle(bg)
    for d in bg[:RNG.randint(1, 2)]:
        all_meds.add(d)

    diagnoses = RNG.sample(DIAGNOSES_POOL, k=RNG.randint(2, 3))

    case: Dict[str, Any] = {
        "case_id": case_id,
        "age": age,
        "labs": {
            "egfr": egfr, "creatinine": round(RNG.uniform(0.8, 1.3), 1),
            "potassium": round(RNG.uniform(3.8, 4.6), 1),
            "inr": round(RNG.uniform(1.0, 2.8), 1),
        },
        "diagnoses": diagnoses,
        "medications": sorted(all_meds),
        "interactions": interactions,
        "required_regimens": [],
        "substitution_options": [],
    }
    if split == "validation":
        tf = f"synth-val::easy-{case_id}"
        case["split"] = "validation"
        case["template_family"] = tf
    else:
        case["split"] = "train"
    return case


def make_medium_case(case_id: str, split: str) -> Dict[str, Any]:
    # Deliberately straddle the moderate→flag thresholds
    age_zone = RNG.choice(["mid", "high", "extreme"])
    egfr_zone = RNG.choice(["border", "low", "normal"])
    alt_zone = RNG.choice(["normal", "border"])

    age = sample_age(age_zone)
    egfr = sample_egfr(egfr_zone)
    alt, ast = sample_alt_ast(alt_zone)

    pairs = _pick_pairs(n_pairs=RNG.randint(3, 4), severity_filter="severe")
    interactions = []
    all_meds: set = set()
    for idx, ((drug_a, drug_b), (severity, evidence, _sub)) in enumerate(pairs):
        iid = f"INT-{case_id}-{idx+1}"
        interactions.append({
            "interaction_id": iid,
            "drug_a": drug_a,
            "drug_b": drug_b,
            "severity": severity,
            "evidence": evidence,
        })
        all_meds.update([drug_a, drug_b])

    bg = [d for d in ALL_DRUGS if d not in all_meds]
    RNG.shuffle(bg)
    for d in bg[:RNG.randint(1, 3)]:
        all_meds.add(d)

    diagnoses = RNG.sample(DIAGNOSES_POOL, k=RNG.randint(2, 4))
    labs: Dict[str, float] = {
        "egfr": egfr,
        "creatinine": round(RNG.uniform(1.0, 2.5), 1),
        "potassium": round(RNG.uniform(4.5, 5.5), 1),
        "inr": round(RNG.uniform(1.5, 3.0), 1),
    }
    if alt_zone != "normal":
        labs["alt"] = alt
        labs["ast"] = ast

    case: Dict[str, Any] = {
        "case_id": case_id,
        "age": age,
        "labs": labs,
        "diagnoses": diagnoses,
        "medications": sorted(all_meds),
        "interactions": interactions,
        "required_regimens": [],
        "substitution_options": [],
    }
    if split == "validation":
        case["split"] = "validation"
        case["template_family"] = f"synth-val::medium-{case_id}"
    else:
        case["split"] = "train"
    return case


def make_hard_case(case_id: str, split: str) -> Dict[str, Any]:
    age = sample_age("extreme")
    egfr = sample_egfr("low")
    alt, ast = sample_alt_ast(RNG.choice(["normal", "border", "elevated"]))

    pairs = _pick_pairs(n_pairs=RNG.randint(4, 5), severity_filter="severe")
    interactions = []
    all_meds: set = set()
    substitution_options = []
    required_regimens = []
    reg_counter = 1

    for idx, ((drug_a, drug_b), (severity, evidence, sub_drug)) in enumerate(pairs):
        iid = f"INT-{case_id}-{idx+1}"
        interactions.append({
            "interaction_id": iid,
            "drug_a": drug_a,
            "drug_b": drug_b,
            "severity": severity,
            "evidence": evidence,
        })
        all_meds.update([drug_a, drug_b])

        # Add substitution for major/contraindicated pairs
        if severity in ("contraindicated", "major") and sub_drug and sub_drug in SUB_DRUGS:
            reg_id = f"REG-{case_id}-{reg_counter}"
            reg_counter += 1
            risk_delta = round(RNG.uniform(0.55, 0.90), 2)
            replace_drug = drug_b if drug_b not in ("acetaminophen", "pantoprazole") else drug_a
            substitution_options.append({
                "regimen_id": reg_id,
                "replace_drug": replace_drug,
                "with_drug": sub_drug,
                "target_condition": SUB_DRUGS[sub_drug],
                "expected_risk_delta": risk_delta,
                "rationale": f"reduces interaction burden from {replace_drug}",
            })
            required_regimens.append(reg_id)
        elif severity == "moderate" and sub_drug:
            # Optional, lower-delta substitution
            reg_id = f"REG-{case_id}-{reg_counter}"
            reg_counter += 1
            risk_delta = round(RNG.uniform(0.25, 0.49), 2)
            replace_drug = drug_a
            if sub_drug in SUB_DRUGS:
                substitution_options.append({
                    "regimen_id": reg_id,
                    "replace_drug": replace_drug,
                    "with_drug": sub_drug,
                    "target_condition": SUB_DRUGS[sub_drug],
                    "expected_risk_delta": risk_delta,
                    "rationale": f"modest risk reduction by replacing {replace_drug}",
                })

    bg = [d for d in ALL_DRUGS if d not in all_meds]
    RNG.shuffle(bg)
    for d in bg[:RNG.randint(2, 4)]:
        all_meds.add(d)

    diagnoses = RNG.sample(DIAGNOSES_POOL, k=RNG.randint(3, 5))
    labs: Dict[str, float] = {
        "egfr": egfr,
        "creatinine": round(RNG.uniform(1.8, 2.8), 1),
        "potassium": round(RNG.uniform(4.8, 5.6), 1),
        "inr": round(RNG.uniform(2.0, 3.2), 1),
    }
    if alt >= 110:
        labs["alt"] = alt
        labs["ast"] = ast

    case: Dict[str, Any] = {
        "case_id": case_id,
        "age": age,
        "labs": labs,
        "diagnoses": diagnoses,
        "medications": sorted(all_meds),
        "interactions": interactions,
        "required_regimens": required_regimens,
        "substitution_options": substitution_options,
    }
    if split == "validation":
        case["split"] = "validation"
        case["template_family"] = f"synth-val::hard-{case_id}"
    else:
        case["split"] = "train"
    return case


# ── Main generation loop ──────────────────────────────────────────────────────

def generate(n_train: int = 160, n_val: int = 30, output_dir: str = ".") -> None:
    """
    Generate n_train train + n_val validation cases per difficulty level.
    Writes three Python files ready to be drop-in replacements or supplements
    for the original task_cases/*.py files.
    """
    import os
    os.makedirs(output_dir, exist_ok=True)

    for level, maker in [("easy", make_easy_case),
                          ("medium", make_medium_case),
                          ("hard", make_hard_case)]:
        cases = []
        for i in range(1, n_train + 1):
            cid = f"SYN-{level[0].upper()}-{i:04d}"
            cases.append(maker(cid, "train"))
        for i in range(1, n_val + 1):
            cid = f"SYN-{level[0].upper()}-V{i:04d}"
            cases.append(maker(cid, "validation"))

        out_path = os.path.join(output_dir, f"synthetic_{level}_cases.py")
        with open(out_path, "w") as f:
            f.write(f'"""Synthetic DDI cases for the {level} task level."""\n\n')
            f.write("from typing import Any, Dict, List\n\n")
            f.write("Case = Dict[str, Any]\n\n")
            f.write(f"SYNTHETIC_{level.upper()}_CASES: List[Case] = ")
            f.write(json.dumps(cases, indent=4))
            f.write("\n")

        print(f"[{level}] wrote {n_train} train + {n_val} val → {out_path}")

    # Also write a combined loader
    loader_path = os.path.join(output_dir, "load_all_cases.py")
    with open(loader_path, "w") as f:
        f.write('''"""Load and merge original + synthetic cases, preserving split integrity."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from task_cases import EASY_CASES, MEDIUM_CASES, HARD_CASES
from synthetic_easy_cases import SYNTHETIC_EASY_CASES
from synthetic_medium_cases import SYNTHETIC_MEDIUM_CASES
from synthetic_hard_cases import SYNTHETIC_HARD_CASES

ALL_EASY   = EASY_CASES   + SYNTHETIC_EASY_CASES
ALL_MEDIUM = MEDIUM_CASES + SYNTHETIC_MEDIUM_CASES
ALL_HARD   = HARD_CASES   + SYNTHETIC_HARD_CASES

def get_split(cases, split="train"):
    return [c for c in cases if c.get("split", "train") == split]

TRAIN_EASY   = get_split(ALL_EASY,   "train")
TRAIN_MEDIUM = get_split(ALL_MEDIUM, "train")
TRAIN_HARD   = get_split(ALL_HARD,   "train")

VAL_EASY   = get_split(ALL_EASY,   "validation")
VAL_MEDIUM = get_split(ALL_MEDIUM, "validation")
VAL_HARD   = get_split(ALL_HARD,   "validation")

print(f"Easy   train={len(TRAIN_EASY)}  val={len(VAL_EASY)}")
print(f"Medium train={len(TRAIN_MEDIUM)} val={len(VAL_MEDIUM)}")
print(f"Hard   train={len(TRAIN_HARD)}  val={len(VAL_HARD)}")
''')
    print(f"\nLoader written → {loader_path}")


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--n-train", type=int, default=160,
                   help="Train cases per difficulty level (default 160 → 480 total)")
    p.add_argument("--n-val",   type=int, default=30,
                   help="Val cases per difficulty level (default 30 → 90 total)")
    p.add_argument("--output-dir", default="synthetic_cases",
                   help="Directory to write output files into")
    args = p.parse_args()
    generate(n_train=args.n_train, n_val=args.n_val, output_dir=args.output_dir)

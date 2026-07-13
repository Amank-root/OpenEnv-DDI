"""Load and merge original + synthetic cases, preserving split integrity."""
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

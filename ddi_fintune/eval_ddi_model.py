"""
Evaluates a fine-tuned DDI model in two modes:

Mode 1: offline  (--mode offline)
  Runs the model against every row in ddi_val.jsonl and measures
  per-step accuracy (does the model predict the correct action_type and
  the correct interaction_id / regimen_id?).
  Fast, no environment needed.

Mode 2: online   (--mode online)
  Runs full episodes against the local DdiEnvironment (no Docker needed)
  and reports final_score per episode, same as the competition evaluator.
  Mirrors what inference.py does but uses the fine-tuned model.

Usage
-----
# Offline eval (fast — just needs the JSONL val file)
python eval_ddi_model.py \\
    --model-dir ddi_lora_adapter \\
    --base-model Qwen/Qwen2.5-7B-Instruct \\
    --val-file   dataset/ddi_val.jsonl \\
    --mode offline

# Online eval (full episodes, needs openenv-ddi installed)
python eval_ddi_model.py \\
    --model-dir ddi_lora_adapter \\
    --base-model Qwen/Qwen2.5-7B-Instruct \\
    --openenv-dir /path/to/OpenEnv-DDI \\
    --mode online \\
    --episodes 20
"""

from __future__ import annotations
import argparse
import json
import os
import sys
import re
from collections import defaultdict
from typing import Dict, List, Optional

import torch

# ── ROCm hint ─────────────────────────────────────────────────────────────────
os.environ.setdefault("HSA_OVERRIDE_GFX_VERSION", "9.4.0")


# ─────────────────────────────────────────────────────────────────────────────
# Args
# ─────────────────────────────────────────────────────────────────────────────

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--model-dir",    required=True,
                   help="Path to saved LoRA adapter (or merged model dir)")
    p.add_argument("--base-model",   default="Qwen/Qwen2.5-7B-Instruct",
                   help="Base HF model ID (only needed if model-dir is a LoRA adapter)")
    p.add_argument("--val-file",     default="dataset/ddi_val.jsonl")
    p.add_argument("--openenv-dir",  default=os.path.abspath(os.path.join(os.path.dirname(__file__), "..")),
                   help="Path to OpenEnv-DDI repo (for online evaluation)")
    p.add_argument("--mode",         choices=["offline", "online"], default="offline")
    p.add_argument("--episodes",     type=int, default=30,
                   help="Number of online episodes to run (online mode only)")
    p.add_argument("--max-seq-len",  type=int, default=2048)
    p.add_argument("--load-in-4bit", dest="load_in_4bit", action="store_true", default=True)
    p.add_argument("--no-load-in-4bit", dest="load_in_4bit", action="store_false")
    p.add_argument("--temperature",  type=float, default=0.0)
    p.add_argument("--max-tokens",   type=int, default=256)
    return p.parse_args()


# ─────────────────────────────────────────────────────────────────────────────
# Model loading
# ─────────────────────────────────────────────────────────────────────────────

def load_model(args):
    """Load LoRA adapter on top of base model, or a merged model directly."""
    from unsloth import FastLanguageModel
    from unsloth.chat_templates import get_chat_template

    print(f"Loading model from: {args.model_dir}")
    # Check if it's a merged model (has config.json with full weights) or adapter
    is_adapter = os.path.exists(os.path.join(args.model_dir, "adapter_config.json"))

    if is_adapter:
        print(f"  Detected LoRA adapter — loading base: {args.base_model}")
        model, tokenizer = FastLanguageModel.from_pretrained(
            model_name   = args.base_model,
            max_seq_length = args.max_seq_len,
            dtype        = None,
            load_in_4bit = args.load_in_4bit,
        )
        from peft import PeftModel
        model = PeftModel.from_pretrained(model, args.model_dir)
    else:
        print("  Detected merged model — loading directly")
        model, tokenizer = FastLanguageModel.from_pretrained(
            model_name   = args.model_dir,
            max_seq_length = args.max_seq_len,
            dtype        = None,
            load_in_4bit = args.load_in_4bit,
        )

    tokenizer = get_chat_template(tokenizer, chat_template="qwen-2.5")
    FastLanguageModel.for_inference(model)  # switch to inference mode
    return model, tokenizer


# ─────────────────────────────────────────────────────────────────────────────
# Inference helper
# ─────────────────────────────────────────────────────────────────────────────

JSON_BLOCK = re.compile(r"\{.*?\}", re.DOTALL)


def generate_action(model, tokenizer, messages: List[Dict],
                    temperature: float = 0.0, max_tokens: int = 256) -> str:
    """Run one forward pass and return the raw text response."""
    text = tokenizer.apply_chat_template(
        messages,
        tokenize              = False,
        add_generation_prompt = True,
    )
    inputs = tokenizer(text, return_tensors="pt").to(model.device)

    with torch.no_grad():
        gen_kwargs = dict(
            max_new_tokens = max_tokens,
            # Explicitly unset max_length so it doesn't conflict with max_new_tokens
            # (Unsloth sets max_length=32768 internally; this silences the FutureWarning)
        )
        if temperature == 0.0:
            out = model.generate(**inputs, **gen_kwargs, do_sample=False)
        else:
            out = model.generate(**inputs, **gen_kwargs, do_sample=True,
                                 temperature=temperature, top_p=0.9)

    # Decode only the newly generated tokens
    prompt_len = inputs["input_ids"].shape[1]
    return tokenizer.decode(out[0][prompt_len:], skip_special_tokens=True).strip()


def parse_json_action(text: str) -> Optional[Dict]:
    """Extract the first valid JSON object from model output."""
    try:
        return json.loads(text.strip())
    except json.JSONDecodeError:
        m = JSON_BLOCK.search(text)
        if m:
            try:
                return json.loads(m.group(0))
            except json.JSONDecodeError:
                pass
    return None


# ─────────────────────────────────────────────────────────────────────────────
# Offline evaluation
# ─────────────────────────────────────────────────────────────────────────────

def eval_offline(model, tokenizer, args) -> None:
    """
    Per-step accuracy on the validation JSONL.
    Metrics:
      - action_type accuracy  (did model pick the right action class?)
      - target accuracy       (did model pick the right interaction_id or regimen_id?)
      - both correct (full step accuracy)
    Broken down by step_type and task_level.
    """
    rows = []
    with open(args.val_file) as f:
        for line in f:
            rows.append(json.loads(line))

    SYSTEM_PROMPT = rows[0]["messages"][0]["content"]  # reuse from data

    stats = defaultdict(lambda: {"n": 0, "action_ok": 0, "target_ok": 0, "both_ok": 0})

    for idx, row in enumerate(rows):
        step_type  = row["step_type"]
        task_level = row["task_level"]

        # Build prompt: system + user only (no assistant turn)
        messages = [
            row["messages"][0],  # system
            row["messages"][1],  # user observation
        ]

        # Ground truth
        gt = json.loads(row["messages"][2]["content"])
        gt_action = gt["action_type"]
        gt_iid    = gt.get("interaction_id")
        gt_rid    = gt.get("suggested_regimen_id")

        raw = generate_action(model, tokenizer, messages,
                              args.temperature, args.max_tokens)
        pred = parse_json_action(raw)

        if pred is None:
            # Model produced unparseable output
            key = f"{task_level}/{step_type}"
            stats[key]["n"] += 1
            continue

        pred_action = pred.get("action_type", "")
        pred_iid    = pred.get("interaction_id")
        pred_rid    = pred.get("suggested_regimen_id")

        action_ok = (pred_action == gt_action)
        target_ok = (
            (gt_iid is None and pred_iid is None and gt_rid is None and pred_rid is None)
            or (gt_iid is not None  and pred_iid  == gt_iid)
            or (gt_rid is not None  and pred_rid  == gt_rid)
        )

        key = f"{task_level}/{step_type}"
        stats[key]["n"]         += 1
        stats[key]["action_ok"] += int(action_ok)
        stats[key]["target_ok"] += int(target_ok)
        stats[key]["both_ok"]   += int(action_ok and target_ok)

        if (idx + 1) % 50 == 0:
            print(f"  [{idx+1}/{len(rows)}] running…")

    # ── Print results ──────────────────────────────────────────────────────────
    print("\n" + "="*65)
    print(f"  OFFLINE EVAL — {args.val_file}")
    print("="*65)
    print(f"{'Category':<30} {'N':>5} {'Action%':>8} {'Target%':>8} {'Both%':>8}")
    print("-"*65)

    totals = {"n": 0, "action_ok": 0, "target_ok": 0, "both_ok": 0}
    for key in sorted(stats):
        s = stats[key]
        n = s["n"] or 1
        print(f"  {key:<28} {s['n']:>5} "
              f"{s['action_ok']/n*100:>7.1f}% "
              f"{s['target_ok']/n*100:>7.1f}% "
              f"{s['both_ok']/n*100:>7.1f}%")
        for k in totals:
            totals[k] += s[k]

    n = totals["n"] or 1
    print("-"*65)
    print(f"  {'TOTAL':<28} {totals['n']:>5} "
          f"{totals['action_ok']/n*100:>7.1f}% "
          f"{totals['target_ok']/n*100:>7.1f}% "
          f"{totals['both_ok']/n*100:>7.1f}%")
    print("="*65)


# ─────────────────────────────────────────────────────────────────────────────
# Online evaluation (full episodes)
# ─────────────────────────────────────────────────────────────────────────────

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


def observation_to_prompt(obs) -> str:
    """Same as inference.py — build user-turn JSON from DdiObservation."""
    candidates = [
        {
            "interaction_id": i.interaction_id,
            "drug_a": i.drug_a,
            "drug_b": i.drug_b,
            "severity": i.severity,
            "evidence": i.evidence,
        }
        for i in obs.ddi_candidates
    ]
    options = [
        {
            "regimen_id": o.regimen_id,
            "replace_drug": o.replace_drug,
            "with_drug": o.with_drug,
            "expected_risk_delta": o.expected_risk_delta,
        }
        for o in obs.substitution_options
    ]
    payload = {
        "task_level": obs.task_level,
        "objective":  obs.objective,
        "patient_id": obs.patient_id,
        "age":        obs.age,
        "labs":       obs.labs,
        "diagnoses":  obs.diagnoses,
        "medications":obs.medications,
        "remaining_critical_ddis": obs.remaining_critical_ddis,
        "current_risk_score":      obs.current_risk_score,
        "steps_used":  obs.steps_used,
        "step_budget": obs.step_budget,
        "ddi_candidates":      candidates,
        "substitution_options": options,
        "decision_log_tail":   obs.decision_log[-4:],
        "history_tail":        [],
    }
    return json.dumps(payload, indent=2)


def heuristic_fallback(obs) -> Dict:
    """Mirror inference.py heuristic_action for guardrail fallback."""
    decisions = obs.metadata.get("decisions", {}) if obs.metadata else {}
    decided   = set(decisions.keys())
    suggested = set(obs.metadata.get("suggested_regimens", [])) if obs.metadata else set()

    for cand in obs.ddi_candidates:
        if cand.interaction_id in decided:
            continue
        if cand.severity in {"contraindicated", "major"}:
            return {"action_type": "flag_interaction",
                    "interaction_id": cand.interaction_id,
                    "suggested_regimen_id": None, "rationale": "severe"}
        if (obs.task_level in {"medium", "hard"}
                and cand.severity == "moderate"
                and (obs.age >= 80 or obs.labs.get("egfr", 90.0) < 45)):
            return {"action_type": "flag_interaction",
                    "interaction_id": cand.interaction_id,
                    "suggested_regimen_id": None, "rationale": "risk-amplified moderate"}
        if cand.severity == "moderate":
            return {"action_type": "monitor",
                    "interaction_id": cand.interaction_id,
                    "suggested_regimen_id": None, "rationale": "monitor moderate"}
        return {"action_type": "ignore",
                "interaction_id": cand.interaction_id,
                "suggested_regimen_id": None, "rationale": "low risk"}

    if obs.task_level == "hard":
        for opt in sorted(obs.substitution_options,
                          key=lambda o: o.expected_risk_delta, reverse=True):
            if opt.regimen_id not in suggested and opt.expected_risk_delta >= 0.5:
                return {"action_type": "suggest_alternative",
                        "interaction_id": None,
                        "suggested_regimen_id": opt.regimen_id, "rationale": "high impact"}

    return {"action_type": "finish",
            "interaction_id": None, "suggested_regimen_id": None, "rationale": "done"}


def eval_online(model, tokenizer, args) -> None:
    """Run full episodes in DdiEnvironment and report final scores."""
    sys.path.insert(0, args.openenv_dir)
    from server.ddi_environment import DdiEnvironment
    from models import DdiAction

    env = DdiEnvironment(case_split="validation", task_sampling="curriculum")

    scores_by_level: Dict[str, List[float]] = defaultdict(list)
    all_scores: List[float] = []

    for ep in range(args.episodes):
        obs   = env.reset()
        level = obs.task_level
        done  = False
        steps = 0
        ep_score = 0.0

        while not done and steps < obs.step_budget:
            messages = [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user",   "content": observation_to_prompt(obs)},
            ]
            raw  = generate_action(model, tokenizer, messages,
                                   args.temperature, args.max_tokens)
            pred = parse_json_action(raw)

            if pred is None:
                payload = heuristic_fallback(obs)
            else:
                payload = pred

            # Basic validation
            try:
                action = DdiAction(**payload)
            except Exception:
                payload = heuristic_fallback(obs)
                action  = DdiAction(**payload)

            result = env.step(action)
            obs    = result
            done   = bool(obs.done)
            steps += 1

            if done and obs.final_score is not None:
                ep_score = float(obs.final_score)

        if not done:
            result = env.step(DdiAction(action_type="finish", rationale="budget"))
            if result.final_score is not None:
                ep_score = float(result.final_score)

        scores_by_level[level].append(ep_score)
        all_scores.append(ep_score)
        print(f"  ep {ep+1:>3}/{args.episodes}  level={level:<6}  "
              f"steps={steps:>2}  final_score={ep_score:.3f}")

    # ── Print results ──────────────────────────────────────────────────────────
    print("\n" + "="*50)
    print("  ONLINE EVAL RESULTS")
    print("="*50)
    for level in ["easy", "medium", "hard"]:
        s = scores_by_level.get(level, [])
        if s:
            avg = sum(s) / len(s)
            print(f"  {level:<8}  n={len(s):>3}  avg_score={avg:.3f}  "
                  f"min={min(s):.3f}  max={max(s):.3f}")
    overall = sum(all_scores) / max(len(all_scores), 1)
    print(f"  {'OVERALL':<8}  n={len(all_scores):>3}  avg_score={overall:.3f}")
    print("="*50)


# ─────────────────────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────────────────────

def main():
    args = parse_args()
    model, tokenizer = load_model(args)

    if args.mode == "offline":
        eval_offline(model, tokenizer, args)
    else:
        eval_online(model, tokenizer, args)


if __name__ == "__main__":
    main()

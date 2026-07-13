"""
T4-optimised DDI fine-tune. Trains in ~20-35 min instead of 5+ hours.

Usage (Colab cell)
------------------
  !python train_ddi_sft.py
  # or with HF upload:
  !python train_ddi_sft.py --push-hub amank-root/ddi-1.5b-lora
"""

from __future__ import annotations
import argparse
import json
import math
import os

import torch
from datasets import Dataset


# ─────────────────────────────────────────────────────────────────────────────
# Args
# ─────────────────────────────────────────────────────────────────────────────

def parse_args():
    p = argparse.ArgumentParser(description="DDI SFT — T4 optimised")

    # Model
    p.add_argument("--model", default="Qwen/Qwen2.5-1.5B-Instruct",
                   help="CHANGE 1: 1.5B fits T4 comfortably; 8x faster than 7B")

    # Data
    p.add_argument("--train-file", default="dataset/ddi_train.jsonl")
    p.add_argument("--val-file",   default="dataset/ddi_val.jsonl")
    p.add_argument("--output-dir", default="ddi_lora_adapter")
    p.add_argument("--merged-dir", default="ddi_merged_model")

    # LoRA  (CHANGE 5: r=8 instead of 16)
    p.add_argument("--lora-r",       type=int,   default=8)
    p.add_argument("--lora-alpha",   type=int,   default=16)   # keep alpha = 2*r
    p.add_argument("--lora-dropout", type=float, default=0.05)

    # Training  (CHANGES 4, 6, 7)
    p.add_argument("--epochs",      type=int,   default=2)     # CHANGE 6
    p.add_argument("--batch-size",  type=int,   default=2)     # CHANGE 7
    p.add_argument("--grad-accum",  type=int,   default=8)     # CHANGE 7 → eff=16
    p.add_argument("--lr",          type=float, default=2e-4)
    p.add_argument("--max-seq-len", type=int,   default=896)   # CHANGE 3
    p.add_argument("--weight-decay",type=float, default=0.01)
    p.add_argument("--warmup-ratio",type=float, default=0.05)

    # Misc
    p.add_argument("--seed",         type=int,  default=42)
    p.add_argument("--max-rows",     type=int,  default=None)
    p.add_argument("--merge",        action="store_true",
                   help="Merge LoRA into base weights after training")
    p.add_argument("--push-hub",     type=str,  default=None,
                   help="HF Hub repo ID to push to, e.g. amank-root/ddi-1.5b-lora")
    p.add_argument("--load-in-4bit", dest="load_in_4bit", action="store_true", default=True)
    p.add_argument("--no-load-in-4bit", dest="load_in_4bit", action="store_false")

    return p.parse_args()


# ─────────────────────────────────────────────────────────────────────────────
# Dataset helpers
# ─────────────────────────────────────────────────────────────────────────────

def load_jsonl(path: str, max_rows: int | None = None) -> list[dict]:
    rows = []
    with open(path) as f:
        for i, line in enumerate(f):
            if max_rows and i >= max_rows:
                break
            rows.append(json.loads(line))
    return rows


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

def main():
    args = parse_args()

    # ── 1. Load model + tokenizer ─────────────────────────────────────────────
    from unsloth import FastLanguageModel

    print(f"\n[1/6] Loading {args.model}")
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name    = args.model,
        max_seq_length= args.max_seq_len,
        dtype         = None,          # Unsloth picks fp16 on T4 automatically
        load_in_4bit  = args.load_in_4bit,
    )

    # ── 2. LoRA ──────────────────────────────────────────────────────────────
    # CHANGE 5: r=8 (was 16). Sufficient for structured JSON output.
    print(f"\n[2/6] LoRA r={args.lora_r}, alpha={args.lora_alpha}")
    model = FastLanguageModel.get_peft_model(
        model,
        r                          = args.lora_r,
        lora_alpha                 = args.lora_alpha,
        lora_dropout               = args.lora_dropout,
        target_modules             = [
            "q_proj", "k_proj", "v_proj", "o_proj",
            "gate_proj", "up_proj", "down_proj",
        ],
        bias                       = "none",
        use_gradient_checkpointing = "unsloth",
        random_state               = args.seed,
    )

    # ── 3. Chat template ──────────────────────────────────────────────────────
    print("\n[3/6] Chat template")
    from unsloth.chat_templates import get_chat_template
    tokenizer = get_chat_template(tokenizer, chat_template="qwen-2.5")

    # ── 4. Load + format dataset ──────────────────────────────────────────────
    print("\n[4/6] Loading dataset")
    train_rows = load_jsonl(args.train_file, args.max_rows)
    val_rows   = load_jsonl(args.val_file)
    print(f"  train: {len(train_rows)} rows  |  val: {len(val_rows)} rows")

    def format_sample(sample):
        """
        CHANGE 2: compact observation JSON + drop always-empty fields.

        Before: pretty-printed JSON with 2-space indent = avg ~620 tokens/sample
        After:  compact JSON, no empty fields          = avg ~587 tokens/sample

        Fields dropped (always [] in SFT — they carry zero signal):
          - history_tail
          - decision_log_tail
          - objective  (already stated in system prompt)
        """
        messages = sample["messages"]

        # Re-serialize the user observation compactly
        user_content = messages[1]["content"]
        try:
            obs = json.loads(user_content)
            # Drop always-empty / redundant fields
            obs.pop("history_tail",      None)
            obs.pop("decision_log_tail", None)
            obs.pop("objective",         None)
            compact_obs = json.dumps(obs, separators=(",", ":"))
        except (json.JSONDecodeError, AttributeError):
            compact_obs = user_content  # fallback: keep as-is

        trimmed_messages = [
            messages[0],                                           # system (unchanged)
            {"role": "user",      "content": compact_obs},        # compacted
            messages[2],                                           # assistant (unchanged)
        ]

        text = tokenizer.apply_chat_template(
            trimmed_messages,
            tokenize              = False,
            add_generation_prompt = False,
        )
        return {"text": text}

    train_ds = Dataset.from_list(train_rows).map(
        format_sample, batched=False, remove_columns=Dataset.from_list(train_rows).column_names
    )
    val_ds = Dataset.from_list(val_rows).map(
        format_sample, batched=False, remove_columns=Dataset.from_list(val_rows).column_names
    )

    # ── 5. Training plan ──────────────────────────────────────────────────────
    eff_batch       = args.batch_size * args.grad_accum   # 2 × 8 = 16
    steps_per_epoch = math.ceil(len(train_ds) / eff_batch)
    total_steps     = steps_per_epoch * args.epochs
    warmup_steps    = max(5, int(total_steps * args.warmup_ratio))

    print(f"\n[5/6] Training plan")
    print(f"  model:         {args.model}")
    print(f"  rows:          {len(train_ds)}")
    print(f"  effective batch: {args.batch_size} × {args.grad_accum} = {eff_batch}")
    print(f"  max_seq_len:   {args.max_seq_len}  (was 1024)")
    print(f"  steps/epoch:   {steps_per_epoch}")
    print(f"  total steps:   {total_steps}  ({args.epochs} epochs, was 3)")
    print(f"  warmup_steps:  {warmup_steps}")
    print(f"  lora_r:        {args.lora_r}  (was 16)")
    print(f"  packing:       True  (was False)")

    # ── 6. Train ──────────────────────────────────────────────────────────────
    from trl import SFTTrainer, SFTConfig

    training_args = SFTConfig(
        output_dir              = args.output_dir,
        logging_steps           = 10,
        report_to               = "none",

        # Schedule
        num_train_epochs        = args.epochs,
        warmup_steps            = warmup_steps,
        learning_rate           = args.lr,
        lr_scheduler_type       = "cosine",
        weight_decay            = args.weight_decay,

        # Batch
        per_device_train_batch_size = args.batch_size,
        per_device_eval_batch_size  = args.batch_size,
        gradient_accumulation_steps = args.grad_accum,

        # Precision — T4 uses fp16 (no bf16 support)
        fp16                    = True,
        bf16                    = False,

        # Eval & checkpoint
        eval_strategy           = "steps",
        eval_steps              = steps_per_epoch,
        save_strategy           = "steps",
        save_steps              = steps_per_epoch,
        save_total_limit        = 2,
        load_best_model_at_end  = True,
        metric_for_best_model   = "eval_loss",
        greater_is_better       = False,

        # Misc
        seed                    = args.seed,
        dataloader_num_workers  = 2,
        optim                   = "adamw_8bit",

        # SFT-specific
        dataset_text_field      = "text",
        max_seq_length          = args.max_seq_len,
        dataset_num_proc        = 2,
        # CHANGE 4: packing=True — safe for single-turn samples, ~1.5x throughput
        packing                 = True,
    )

    trainer = SFTTrainer(
        model        = model,
        tokenizer    = tokenizer,
        train_dataset= train_ds,
        eval_dataset = val_ds,
        args         = training_args,
    )

    print(f"\n[6/6] Training — expect ~20-35 min on T4\n")
    trainer_stats = trainer.train()

    # ── 7. Save ──────────────────────────────────────────────────────────────
    print(f"\nSaving LoRA adapter → {args.output_dir}")
    model.save_pretrained(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)

    runtime_min = trainer_stats.metrics.get("train_runtime", 0) / 60
    print("\n── Training complete ────────────────────────────────────────────")
    print(f"  Runtime:    {runtime_min:.1f} min")
    print(f"  Train loss: {trainer_stats.metrics.get('train_loss', 0):.4f}")
    print("─────────────────────────────────────────────────────────────────")

    # ── 8. Merge + upload ─────────────────────────────────────────────────────
    if args.merge or args.push_hub:
        print(f"\nMerging LoRA weights into base model...")
        model = model.merge_and_unload()

        if args.merge:
            model.save_pretrained(args.merged_dir)
            tokenizer.save_pretrained(args.merged_dir)
            print(f"  Merged model saved → {args.merged_dir}")

        if args.push_hub:
            # Uploads the LoRA adapter only (small, ~50MB)
            # For the full merged model pass --merge too
            print(f"\nUploading to HuggingFace Hub: {args.push_hub}")
            print("  (make sure you ran: huggingface-cli login)")
            model.push_to_hub(args.push_hub, private=False)
            tokenizer.push_to_hub(args.push_hub, private=False)
            print(f"  Done → https://huggingface.co/{args.push_hub}")

    return trainer_stats


if __name__ == "__main__":
    main()

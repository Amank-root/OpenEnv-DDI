"""
TWO OPTIONS — pick one:

  Option A (recommended): push LoRA adapter only — small (~50 MB), fast,
    loads on any machine with peft installed.

  Option B: merge + push full 16-bit model — larger (~3 GB for 1.5B),
    loads without peft, better for inference endpoints.

Usage
-----
  # Login first (one-time):
  huggingface-cli login

  # Option A — adapter only (fast, ~50 MB):
  python upload_to_hub.py --mode adapter --repo amank-root/ddi-1.5b-lora

  # Option B — merged 16-bit model (~3 GB):
  python upload_to_hub.py --mode merged --repo amank-root/ddi-1.5b-merged
"""

from __future__ import annotations
import argparse
import os

import torch


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--mode",        choices=["adapter", "merged"], default="adapter",
                   help="adapter: push LoRA weights only (~50MB). merged: full 16-bit model (~3GB)")
    p.add_argument("--repo",        required=True,
                   help="HF repo ID, e.g. amank-root/ddi-1.5b-lora")
    p.add_argument("--adapter-dir", default="ddi_lora_adapter",
                   help="Path to saved LoRA adapter (output of training)")
    p.add_argument("--base-model",  default="Qwen/Qwen2.5-1.5B-Instruct",
                   help="Base model used during training")
    p.add_argument("--merged-dir",  default="ddi_merged_model",
                   help="Local dir to save merged weights before upload (Option B)")
    p.add_argument("--private",     action="store_true", default=False)
    p.add_argument("--token",       default=None,
                   help="HF token (or set HF_TOKEN env var / use huggingface-cli login)")
    return p.parse_args()


def push_adapter_only(args):
    """
    Option A: push just the adapter files.
    The repo will contain: adapter_config.json, adapter_model.safetensors, tokenizer files.
    Users load it with:
        model = PeftModel.from_pretrained(base_model, "amank-root/ddi-1.5b-lora")
    """
    from peft import PeftModel
    from transformers import AutoModelForCausalLM, AutoTokenizer

    print(f"\n[Option A] Pushing LoRA adapter to: {args.repo}")
    print(f"  adapter_dir: {args.adapter_dir}")
    print(f"  base_model:  {args.base_model}")

    # Load tokenizer from adapter dir (it was saved there during training)
    print("\nLoading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(args.adapter_dir)

    # Load the PEFT adapter (no need to load full base model for adapter-only push)
    # We just need the adapter_config + weights to exist — push them directly
    from huggingface_hub import HfApi
    api = HfApi(token=args.token)

    # Create the repo if it doesn't exist
    try:
        api.create_repo(repo_id=args.repo, private=args.private, exist_ok=True)
        print(f"  Repo ready: https://huggingface.co/{args.repo}")
    except Exception as e:
        print(f"  Warning creating repo: {e}")

    # Upload the entire adapter directory
    print(f"\nUploading {args.adapter_dir}/ ...")
    api.upload_folder(
        folder_path = args.adapter_dir,
        repo_id     = args.repo,
        repo_type   = "model",
        commit_message = "Upload DDI LoRA adapter (Qwen2.5-1.5B fine-tuned)",
        token       = args.token,
    )

    # Write a minimal README / model card
    readme = f"""---
base_model: {args.base_model}
library_name: peft
tags:
  - lora
  - qwen2
  - drug-drug-interaction
  - medical
  - fine-tuned
---

# DDI Triage LoRA — {args.repo}

LoRA adapter fine-tuned on the [OpenEnv-DDI](https://huggingface.co/spaces/amank-root/ddi)
drug-drug interaction triage task.

**Base model:** `{args.base_model}`  
**Task:** Given a patient's medication list and labs, flag/monitor/ignore DDIs and suggest safer alternatives.  
**Training:** 2 500 SFT rows (18 real + 480 synthetic cases), 2 epochs, r=8 LoRA.

## Load

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

base = AutoModelForCausalLM.from_pretrained("{args.base_model}", torch_dtype="auto", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("{args.repo}")
model = PeftModel.from_pretrained(base, "{args.repo}")
model = model.merge_and_unload()  # optional: merge for faster inference
```
"""
    api.upload_file(
        path_or_fileobj = readme.encode(),
        path_in_repo    = "README.md",
        repo_id         = args.repo,
        repo_type       = "model",
        token           = args.token,
        commit_message  = "Add model card",
    )

    print(f"\n✅ Done → https://huggingface.co/{args.repo}")


def push_merged_model(args):
    """
    Option B: merge LoRA into base weights and push the full 16-bit model.
    Uses Unsloth's save_pretrained_merged() which correctly dequantizes 4-bit
    weights before saving — bypassing the NotImplementedError from vanilla
    model.save_pretrained() on Unsloth's quantized models.
    """
    from unsloth import FastLanguageModel
    from unsloth.chat_templates import get_chat_template

    print(f"\n[Option B] Merging LoRA → full 16-bit model → {args.repo}")
    print(f"  adapter_dir: {args.adapter_dir}")
    print(f"  base_model:  {args.base_model}")

    # Reload the trained model exactly as it was during training
    print("\nLoading base model + LoRA adapter...")
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name   = args.adapter_dir,   # Unsloth reads adapter_config.json here
        max_seq_length = 896,
        dtype        = None,
        load_in_4bit = True,
    )
    tokenizer = get_chat_template(tokenizer, chat_template="qwen-2.5")

    # Use Unsloth's merge path — this is the critical fix.
    # save_pretrained_merged() handles dequantization internally and avoids the
    # reverse_transform NotImplementedError that hits vanilla save_pretrained().
    print(f"\nMerging and saving to {args.merged_dir} (this takes ~2-3 min)...")
    model.save_pretrained_merged(
        args.merged_dir,
        tokenizer,
        save_method = "merged_16bit",   # dequantize 4bit → fp16 before save
    )
    print(f"  Saved locally → {args.merged_dir}/")

    # Now push to hub
    print(f"\nPushing to HuggingFace Hub: {args.repo}")
    model.push_to_hub_merged(
        args.repo,
        tokenizer,
        save_method = "merged_16bit",
        token       = args.token,
        private     = args.private,
    )

    print(f"\n✅ Done → https://huggingface.co/{args.repo}")
    print(f"   Load with:")
    print(f"   model = AutoModelForCausalLM.from_pretrained('{args.repo}', torch_dtype='auto')")


def main():
    args = parse_args()

    # Verify adapter dir exists
    if not os.path.isdir(args.adapter_dir):
        raise FileNotFoundError(
            f"Adapter dir not found: {args.adapter_dir}\n"
            "Make sure training completed and the adapter was saved."
        )
    required = ["adapter_config.json", "tokenizer_config.json"]
    missing  = [f for f in required if not os.path.exists(os.path.join(args.adapter_dir, f))]
    if missing:
        raise FileNotFoundError(f"Adapter dir is incomplete. Missing: {missing}")

    print(f"✓ Adapter dir OK: {args.adapter_dir}")
    print(f"  Files: {os.listdir(args.adapter_dir)}")

    if args.mode == "adapter":
        push_adapter_only(args)
    else:
        push_merged_model(args)


if __name__ == "__main__":
    main()

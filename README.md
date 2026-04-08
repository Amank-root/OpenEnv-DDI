---
title: DDI Polypharmacy Triage Environment
emoji: 🩺
colorFrom: yellow
colorTo: red
sdk: docker
pinned: false
app_port: 8000
base_path: /web
tags:
  - openenv
  - healthcare
  - safety
---

# DDI Polypharmacy Triage Environment

This OpenEnv environment simulates a real clinical safety workflow: triaging drug-drug interactions (DDIs) for older adults with polypharmacy.

Agents review medication lists, labs, and diagnosis context, then decide whether to:

- `flag_interaction`
- `monitor`
- `suggest_alternative`
- `ignore`
- `finish`

The environment is deterministic and built for reproducible benchmarking.

## Why This Task

Polypharmacy in elderly populations is associated with preventable adverse events and avoidable hospitalizations. This benchmark focuses on medication safety triage that clinicians and pharmacists perform in real care settings.

## Task Suite

By default, the environment cycles task levels on each `reset()` in order: `easy -> medium -> hard`.
To reduce overfitting to fixed task order during training, you can switch to mixed sampling while
keeping the initial curriculum warmup cycle.

1. Easy: severe DDI detection in a 5-drug list.
2. Medium: risk-aware triage using severity plus patient factors (age, renal function).
3. Hard: triage plus constrained alternative regimen suggestions to reduce risk while preserving treatment intent.

Each episode corresponds to one patient case.

### Expected Difficulty Profile

- **Easy**: mostly severe DDI identification with short medication lists and minimal planning burden.
- **Medium**: context-sensitive decision boundary (e.g., moderate interactions can escalate with renal/hepatic/age risk).
- **Hard**: multi-objective control (correct triage + substitution planning + finish timing) with longer horizons.

## Dataset Splits

Cases are organized into strict template-family splits to prevent train/validation leakage.
Each case can declare:

- `template_family`: stable family key used for leakage checks
- `split`: `train` or `validation`

Runtime split selection is controlled by `DDI_CASE_SPLIT`:

- `all` (default): union of train + validation
- `train`: train-only cases
- `validation`: validation-only cases

Task ordering is controlled by `DDI_TASK_SAMPLING`:

- `curriculum` (default): fixed `easy -> medium -> hard`
- `mixed`: one curriculum warmup, then deterministic mixed-difficulty pattern
- `mixed_seeded` / `mixed_shuffled`: one curriculum warmup, then seeded shuffled windows for reproducible randomness

Optional seeded-shuffle controls:

- `DDI_TASK_SHUFFLE_SEED` (default `17`)
- `DDI_TASK_SHUFFLE_WINDOW` (default `6`)

## Observation Space

`DdiObservation` includes:

- `task_level`, `task_title`, `objective`
- `patient_id`, `age`, `medications`, `diagnoses`, `labs`
- `ddi_candidates`: list of structured interaction candidates
- `substitution_options`: fixed alternatives catalog (hard task)
- `decision_log`, `remaining_critical_ddis`, `current_risk_score`
- `step_budget`, `steps_used`, `final_score`

## Action Space

`DdiAction` fields:

- `action_type`: one of `flag_interaction | monitor | suggest_alternative | ignore | finish`
- `interaction_id`: required for triage actions (`flag_interaction`, `monitor`, `ignore`)
- `suggested_regimen_id`: required for `suggest_alternative`
- `rationale`: optional short text

## Reward Function

Shaped reward is provided over the full trajectory:

- Positive reward for correct triage decisions.
- `+1` for correctly catching critical DDIs.
- Penalties for false positives and missed critical interactions.
- Penalties for invalid or duplicate actions.
- Hard-task reward for correct alternative regimen suggestions.
- Terminal adjustment based on grader score.

This provides dense feedback, not just sparse terminal success/failure.

## Graders

Programmatic deterministic graders are implemented for all three tasks and always return scores in `0.0..1.0`:

- `grade_easy`
- `grade_medium`
- `grade_hard`

Hard task combines interaction triage score and regimen suggestion score.

## Project Structure

```
.
├── __init__.py
├── client.py
├── ddi_data.py
├── graders.py
├── inference.py
├── models.py
├── openenv.yaml
├── pyproject.toml
├── task_cases/
│   ├── easy_cases.py
│   ├── medium_cases.py
│   └── hard_cases.py
├── task_registry.py
├── tests/
│   ├── test_accuracy.py
│   ├── test_environment.py
│   └── test_graders.py
└── server/
    ├── app.py
    ├── ddi_environment.py
    └── Dockerfile
```

  `ddi_data.py` now contains shared constants and composes `TASK_CASES` from level-specific modules in `task_cases/`. This keeps large deterministic datasets separate from environment logic and grading logic.

## Local Setup

Install dependencies:

```bash
uv sync
```

Run server:

```bash
uvicorn server.app:app --reload --host 0.0.0.0 --port 8000
```

Validate OpenEnv spec:

```bash
openenv validate
```

Run tests:

```bash
pytest -q
```

## Baseline Inference

The required baseline script is `inference.py` at repository root and uses the OpenAI client.

Set environment variables:

```bash
export API_BASE_URL=https://router.huggingface.co/v1
export MODEL_NAME=<your-model>
export HF_TOKEN=<your-token>
# Optional fallback for API credentials
export API_KEY=<your-token>

# Optional runtime controls
export TASK_EPISODES=3
export MAX_STEPS=16
export DDI_CASE_SPLIT=all          # all | train | validation
export DDI_TASK_SAMPLING=curriculum # curriculum | mixed
```

Run baseline:

```bash
python inference.py
```

Optional environment connection variables:

- `ENV_BASE_URL`: connect to existing server URL.
- `LOCAL_IMAGE_NAME`: preferred Docker image variable when running with `from_docker_image`.
- `IMAGE_NAME`: fallback Docker image variable.
- `ENV_IMAGE`: legacy fallback Docker image variable.

## Baseline Scores

Representative baseline results from `inference.py` (curriculum order, `TASK_EPISODES=3`, one easy/medium/hard cycle):

| Task | Score |
|---|---:|
| easy | 0.999 |
| medium | 0.999 |
| hard | 0.979 |
| mean | 0.992 |

Notes:

- Scores are deterministic for fixed case order and policy behavior.
- Validation checks parse the structured `[START]`, `[STEP]`, and `[END]` lines emitted by `inference.py`.

## Docker

Build image:

```bash
docker build -t ddi-env:latest -f server/Dockerfile .
```

Run image:

```bash
docker run -p 8000:8000 ddi-env:latest
```

## Hugging Face Space Deployment

From repository root:

```bash
openenv push
```

The deployed API exposes:

- `POST /reset`
- `POST /step`
- `GET /state`
- `GET /schema`
- `GET /web`

## Submission Validation

Use the provided validator script:

```bash
./validate-submission.sh https://amank-root-ddi-env.hf.space
```

This checks Space availability, Docker build success, and `openenv validate` compliance.

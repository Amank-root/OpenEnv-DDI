# ✅ Pre-Submission Checklist

All items below **must pass**, or your submission will be **disqualified**.

---

## 🚀 Core Requirements

- [ ] **HF Space deploys successfully**
- [ ] **Automated ping to Space URL**
  - Must return **HTTP 200**
  - Must respond correctly to `reset()`

---

## ⚙️ OpenEnv Compliance

- [ ] `openenv.yaml` is valid and present
- [ ] Typed models are properly defined
- [ ] Required endpoints are implemented and functional:
  - [ ] `step()`
  - [ ] `reset()`
  - [ ] `state()`

---

## 🐳 Docker

- [ ] `Dockerfile` exists in the root directory
- [ ] Docker image builds successfully
- [ ] Automated docker build passes on the submitted repository

---

## 📊 Baseline Execution

- [ ] `inference.py` runs without errors
- [ ] Script completes execution successfully
- [ ] Outputs valid scores/results

---

## 🧪 Tasks & Graders

- [ ] At least **3 tasks** are implemented
- [ ] Each task includes a corresponding grader
- [ ] All graders execute successfully
- [ ] All scores fall within the valid range: **0.0 – 1.0**

---

# Mandatory Additional Info

- [ ] The inference script must be named `inference.py` and placed in the root directory of the project
- [ ] Participants must use OpenAI Client for all LLM calls using the variables documented below
- [ ] Participants must emit structured stdout logs strictly following the [START], [STEP], and [END] format defined in the sample inference.py provided below. Any deviation in field names, ordering, or formatting will result in incorrect evaluation scoring.

---

## 🔐 Environment Variables

Set the baseline variables using this credential precedence:

1. `HF_TOKEN`
2. `API_KEY`

Required:

```bash
API_BASE_URL=<your_api_endpoint>
MODEL_NAME=<your_model_name>
HF_TOKEN=<your_huggingface_token>
```

Optional (recommended):

```bash
API_KEY=<fallback_api_key>
ENV_BASE_URL=<running_env_server_url>
LOCAL_ENV_BASE_URL=http://localhost:8000
LOCAL_IMAGE_NAME=ddi-env:latest
IMAGE_NAME=ddi-env:latest
ENV_IMAGE=ddi-env:latest
DOCKER_READY_TIMEOUT=90
TASK_EPISODES=3
MAX_STEPS=16
```
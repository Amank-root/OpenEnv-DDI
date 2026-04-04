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

[] The inference script must be named `inference.py` and placed in the root directory of the project
[] Participants must use OpenAI Client for all LLM calls using above variables
[] Participants must emit structured stdout logs strictly following the [START], [STEP], and [END] format defined in the sample inference.py provided below. Any deviation in field names, ordering, or formatting will result in incorrect evaluation scoring. Refer to the Sample Inference Script for the complete format specification and examples.

---

## 🔐 Environment Variables

Ensure the following environment variables are defined:

```bash
API_BASE_URL=<your_api_endpoint>
MODEL_NAME=<your_model_name>
HF_TOKEN=<your_huggingface_token>
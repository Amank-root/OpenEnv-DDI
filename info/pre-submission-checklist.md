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

## 🔐 Environment Variables

Ensure the following environment variables are defined:

```bash
API_BASE_URL=<your_api_endpoint>
MODEL_NAME=<your_model_name>
HF_TOKEN=<your_huggingface_token>
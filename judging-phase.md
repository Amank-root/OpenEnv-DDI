# 🧪 Evaluation Process & Disqualification Criteria

---

## 🥇 Phase 1: Automated Validation (Pass/Fail)

Submissions must pass all automated checks to proceed.

### Requirements:
- [ ] **HF Space deploys successfully**
- [ ] **OpenEnv specification compliance**
- [ ] **Dockerfile builds successfully**
- [ ] **Baseline reproduces correctly**
- [ ] **At least 3 tasks with graders implemented**

> ❗ This is a strict **pass/fail gate**. Failure in any check results in rejection.

---

## 🤖 Phase 2: Agentic Evaluation (Scored)

Submissions that pass Phase 1 are evaluated using automated agents.

### Evaluation Steps:
- 🔁 **Baseline agent re-run**
- 🤖 **Standard Open LLM agent execution**
  - Example: *Nemotron 3 Super*
- 📊 **Score variance check**
  - Ensures consistency and robustness across runs

---

## 👨‍🔬 Phase 3: Human Review

Top-performing submissions are manually reviewed by experts.

### Review Conducted By:
- Meta engineers
- Hugging Face engineers

### Evaluation Criteria:
- 💡 Real-world utility
- 🎨 Creativity and originality
- 🔍 Exploit and edge-case handling

---

## ❌ Disqualification Criteria

Submissions will be disqualified if any of the following apply:

- [ ] Environment **does not deploy or respond**
- [ ] **Plagiarized** or trivially modified existing environments
- [ ] Graders that **always return the same score**
- [ ] Missing **baseline inference script (`inference.py`)**

---

## 📌 Important Notes

- Ensure all components are **fully functional and tested**
- Submissions should be **original, robust, and reproducible**
- Follow all specifications strictly to avoid disqualification
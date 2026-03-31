# 📊 Evaluation Criteria & Scoring Breakdown

Submissions are evaluated across five key dimensions. Each dimension contributes a weighted percentage to the final score.

---

## 🧮 Parameter Weights

| Parameter                     | Weight | Description |
|-----------------------------|--------|-------------|
| **Real-world utility**       | 30%    | Does the environment model a genuine task? Would it be useful for training or evaluating agents? |
| **Task & grader quality**   | 25%    | Are tasks clearly defined? Do graders fairly and accurately measure success? Is there meaningful difficulty progression? |
| **Environment design**      | 20%    | Quality of state management, action/observation spaces, reward shaping, and episode boundaries |
| **Code quality & compliance** | 15%  | Adherence to OpenEnv spec, clean structure, typed models, documentation, and Docker functionality |
| **Creativity & novelty**    | 10%    | Originality, unique problem domain, and innovative mechanics or reward design |

---

## 🧾 Detailed Scoring Breakdown

### 🌍 Real-World Utility (30%)

- **0–5**: Toy or artificial problem with no practical use  
- **6–15**: Valid domain, but shallow or simplistic modeling  
- **16–25**: Good modeling; useful for evaluating agents  
- **26–30**: Excellent — fills a real gap and provides strong value to the RL/agent community  

---

### 🧪 Task & Grader Quality (25%)

Evaluation considerations:

- [ ] At least **3 tasks** with a range of difficulty  
- [ ] Graders return scores within **0.0 – 1.0**  
- [ ] Graders are **deterministic and reproducible**  
- [ ] Hard tasks meaningfully challenge **frontier models**

---

### 🧠 Environment Design (20%)

Evaluation considerations:

- [ ] `reset()` produces a clean and valid initial state  
- [ ] Action and observation spaces are **well-designed and documented**  
- [ ] Reward function provides **meaningful, varying signals** (not purely sparse)  
- [ ] Episode boundaries are **logical and well-defined**

---

### 🧑‍💻 Code Quality & Spec Compliance (15%)

Evaluation considerations:

- [ ] `openenv validate` passes successfully  
- [ ] `docker build` and `docker run` work without issues  
- [ ] HF Space deploys and responds correctly  
- [ ] Baseline script runs and reproduces expected scores  
- [ ] Codebase is clean, modular, typed, and documented  

---

### 🎨 Creativity & Novelty (10%)

Evaluation considerations:

- [ ] Problem domain is **unique or uncommon** within OpenEnv  
- [ ] Reward design includes **interesting or non-trivial mechanics**  
- [ ] Environment introduces **clever or engaging interactions**

---

## 📌 Summary

To achieve a high score:
- Focus on **real-world relevance and usability**
- Ensure **robust, fair, and reproducible evaluation**
- Build a **clean, well-structured environment**
- Add **originality and thoughtful design choices**

> High-quality submissions balance **technical correctness**, **practical value**, and **creative design**.
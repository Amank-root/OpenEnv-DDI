# Functional Requirements

## Real-world Task Simulation
- The environment must simulate a task humans actually do.  
- **Not games or toys.**  
- Examples: email triage, code review, data cleaning, scheduling, customer support, content moderation.

## OpenEnv Spec Compliance
- Implement the full OpenEnv interface: typed **Observation**, **Action**, and **Reward** Pydantic models.  
- Required methods:  
  - `step(action)` → returns `(observation, reward, done, info)`  
  - `reset()` → returns initial observation  
  - `state()` → returns current state  
- Include `openenv.yaml` with metadata.  
- Must pass validation with `openenv validate`.

## Minimum 3 Tasks with Agent Graders
- Each task defines a concrete objective an agent must accomplish.  
- Each task includes a **programmatic grader** that scores performance (0.0–1.0).  
- Tasks should range from **easy → medium → hard**.  
- Graders must have **clear, deterministic success/failure criteria**.

## Meaningful Reward Function
- Provides signal over the **full trajectory**, not just binary end-of-episode.  
- Rewards **partial progress** toward task completion.  
- Penalizes clearly undesirable behavior (e.g., infinite loops, destructive actions).

## Baseline Inference Script
- Uses the **OpenAI API client** to run a model against the environment.  
- Reads API credentials from environment variables (`OPENAI_API_KEY`).  
- Produces a reproducible **baseline score** on all 3 tasks.

# Detailed Requirements

## Non-Functional Requirements

### Deploys to a Hugging Face Space
- Environment must run as a **containerized HF Space** tagged with `openenv`.

### Containerized Execution
- Must include a working **Dockerfile**.  
- Environment should start cleanly with:  
  ```bash
  docker build .
  docker run <image>
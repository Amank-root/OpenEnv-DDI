"""Baseline inference script for DDI triage OpenEnv environment."""

from __future__ import annotations

import asyncio
import inspect
import json
from dotenv import load_dotenv
import os
import re
from urllib import error as urlerror
from urllib import request as urlrequest
from typing import Dict, List, Optional

from openai import OpenAI

try:
    from client import DdiEnv
    from models import DdiAction, DdiObservation
except ImportError:
    from ddi.client import DdiEnv
    from ddi.models import DdiAction, DdiObservation

load_dotenv()  # Load environment variables from .env file if present


def normalize_base_url(base_url: str) -> str:
    cleaned = base_url.rstrip("/")
    for suffix in ("/chat/completions", "/responses"):
        if cleaned.endswith(suffix):
            cleaned = cleaned[: -len(suffix)]
    return cleaned


API_BASE_URL = normalize_base_url(
    os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
)
API_KEY = os.getenv("HF_TOKEN") or os.getenv("API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")
ENV_BASE_URL = os.getenv("ENV_BASE_URL")
ENV_IMAGE = os.getenv("ENV_IMAGE", "ddi-env:latest")
DEFAULT_LOCAL_ENV_BASE_URL = os.getenv("LOCAL_ENV_BASE_URL", "http://localhost:8000")
DOCKER_READY_TIMEOUT = float(os.getenv("DOCKER_READY_TIMEOUT", "90"))
HARD_REGIMEN_DELTA_THRESHOLD = float(os.getenv("HARD_REGIMEN_DELTA_THRESHOLD", "0.5"))
BENCHMARK = os.getenv("DDI_BENCHMARK", "openenv-ddi")
TASK_NAME = os.getenv("DDI_TASK_NAME", "ddi-triage")
MAX_STEPS = int(os.getenv("MAX_STEPS", "16"))
SUCCESS_SCORE_THRESHOLD = float(os.getenv("SUCCESS_SCORE_THRESHOLD", "0.7"))
TEMPERATURE = 0.0
MAX_TOKENS = 250
JSON_BLOCK = re.compile(r"\{.*\}", re.DOTALL)


SYSTEM_PROMPT = (
    "You are a clinical medication safety triage assistant. "
    "Return exactly one JSON object with keys: "
    "action_type, interaction_id, suggested_regimen_id, rationale. "
    "Valid action_type values are flag_interaction, monitor, suggest_alternative, ignore, finish. "
    "If action_type does not require a field, set it to null."
)


def log_start(task: str, env: str, model: str) -> None:
    print(f"[START] task={task} env={env} model={model}", flush=True)


def log_step(step: int, action: str, reward: float, done: bool, error: Optional[str]) -> None:
    # Keep STEP output single-line even if upstream error text contains newlines.
    error_val = "null" if not error else " ".join(str(error).splitlines())
    action_val = " ".join(str(action).splitlines())
    done_val = str(done).lower()
    print(
        f"[STEP] step={step} action={action_val} reward={reward:.2f} done={done_val} error={error_val}",
        flush=True,
    )


def log_end(success: bool, steps: int, rewards: List[float]) -> None:
    rewards_str = ",".join(f"{reward:.2f}" for reward in rewards)
    print(
        f"[END] success={str(success).lower()} steps={steps} rewards={rewards_str}",
        flush=True,
    )


def action_to_str(action: DdiAction) -> str:
    if action.action_type in {"flag_interaction", "monitor", "ignore"}:
        return f"{action.action_type}('{action.interaction_id}')"
    if action.action_type == "suggest_alternative":
        return f"suggest_alternative('{action.suggested_regimen_id}')"
    return "finish()"


def last_action_error(observation: DdiObservation) -> Optional[str]:
    direct_error = getattr(observation, "last_action_error", None)
    if direct_error:
        return str(direct_error)

    metadata = observation.metadata or {}
    for key in ("last_action_error", "error"):
        value = metadata.get(key)
        if value:
            return str(value)

    return None


def observation_to_prompt(observation: DdiObservation, history: List[str]) -> str:
    candidates = [
        {
            "interaction_id": item.interaction_id,
            "drug_a": item.drug_a,
            "drug_b": item.drug_b,
            "severity": item.severity,
            "evidence": item.evidence,
        }
        for item in observation.ddi_candidates
    ]
    options = [
        {
            "regimen_id": item.regimen_id,
            "replace_drug": item.replace_drug,
            "with_drug": item.with_drug,
            "expected_risk_delta": item.expected_risk_delta,
        }
        for item in observation.substitution_options
    ]

    payload = {
        "task_level": observation.task_level,
        "objective": observation.objective,
        "patient_id": observation.patient_id,
        "age": observation.age,
        "labs": observation.labs,
        "diagnoses": observation.diagnoses,
        "medications": observation.medications,
        "remaining_critical_ddis": observation.remaining_critical_ddis,
        "current_risk_score": observation.current_risk_score,
        "steps_used": observation.steps_used,
        "step_budget": observation.step_budget,
        "ddi_candidates": candidates,
        "substitution_options": options,
        "decision_log_tail": observation.decision_log[-4:],
        "history_tail": history[-4:],
    }
    return json.dumps(payload, indent=2)


def heuristic_action(observation: DdiObservation) -> Dict:
    decisions = observation.metadata.get("decisions", {}) if observation.metadata else {}
    suggested = set(observation.metadata.get("suggested_regimens", [])) if observation.metadata else set()

    for candidate in observation.ddi_candidates:
        if candidate.interaction_id in decisions:
            continue

        if candidate.severity in {"contraindicated", "major"}:
            return {
                "action_type": "flag_interaction",
                "interaction_id": candidate.interaction_id,
                "suggested_regimen_id": None,
                "rationale": "severe interaction",
            }

        if (
            observation.task_level in {"medium", "hard"}
            and candidate.severity == "moderate"
            and (observation.age >= 80 or observation.labs.get("egfr", 90.0) < 45)
        ):
            return {
                "action_type": "flag_interaction",
                "interaction_id": candidate.interaction_id,
                "suggested_regimen_id": None,
                "rationale": "moderate interaction amplified by patient risk",
            }

        if candidate.severity == "moderate":
            return {
                "action_type": "monitor",
                "interaction_id": candidate.interaction_id,
                "suggested_regimen_id": None,
                "rationale": "moderate monitor",
            }

        return {
            "action_type": "ignore",
            "interaction_id": candidate.interaction_id,
            "suggested_regimen_id": None,
            "rationale": "low risk",
        }

    if observation.task_level == "hard":
        for option in sorted(
            observation.substitution_options,
            key=lambda item: item.expected_risk_delta,
            reverse=True,
        ):
            if option.regimen_id not in suggested and option.expected_risk_delta >= 0.5:
                return {
                    "action_type": "suggest_alternative",
                    "interaction_id": None,
                    "suggested_regimen_id": option.regimen_id,
                    "rationale": "high risk reduction",
                }

    return {
        "action_type": "finish",
        "interaction_id": None,
        "suggested_regimen_id": None,
        "rationale": "triage complete",
    }


def expected_treatment_action(observation: DdiObservation, interaction_id: str) -> str | None:
    for candidate in observation.ddi_candidates:
        if candidate.interaction_id != interaction_id:
            continue

        if candidate.severity in {"contraindicated", "major"}:
            return "flag_interaction"

        if (
            observation.task_level in {"medium", "hard"}
            and candidate.severity == "moderate"
            and (observation.age >= 80 or observation.labs.get("egfr", 90.0) < 45)
        ):
            return "flag_interaction"

        if candidate.severity == "moderate":
            return "monitor"

        return "ignore"

    return None


def unresolved_interaction_ids(observation: DdiObservation) -> set[str]:
    decisions = observation.metadata.get("decisions", {}) if observation.metadata else {}
    decided = set(decisions.keys())
    return {
        item.interaction_id
        for item in observation.ddi_candidates
        if item.interaction_id not in decided
    }


def pending_high_value_regimens(observation: DdiObservation) -> list[str]:
    if observation.task_level != "hard":
        return []

    suggested = set(observation.metadata.get("suggested_regimens", [])) if observation.metadata else set()
    options = sorted(
        observation.substitution_options,
        key=lambda item: item.expected_risk_delta,
        reverse=True,
    )
    return [
        item.regimen_id
        for item in options
        if item.regimen_id not in suggested and item.expected_risk_delta >= HARD_REGIMEN_DELTA_THRESHOLD
    ]


def apply_action_guardrails(payload: Dict, observation: DdiObservation) -> Dict:
    action_type = payload.get("action_type")
    interaction_id = payload.get("interaction_id")
    suggested_regimen_id = payload.get("suggested_regimen_id")

    unresolved = unresolved_interaction_ids(observation)
    pending_regimens = pending_high_value_regimens(observation)

    if action_type in {"flag_interaction", "monitor", "ignore"}:
        if interaction_id not in unresolved:
            return heuristic_action(observation)

        expected = expected_treatment_action(observation, interaction_id)
        if expected is None:
            return heuristic_action(observation)

        if action_type != expected:
            return {
                "action_type": expected,
                "interaction_id": interaction_id,
                "suggested_regimen_id": None,
                "rationale": "guardrail corrected triage",
            }

        return {
            "action_type": action_type,
            "interaction_id": interaction_id,
            "suggested_regimen_id": None,
            "rationale": payload.get("rationale", ""),
        }

    if action_type == "suggest_alternative":
        if observation.task_level != "hard" or not suggested_regimen_id:
            return heuristic_action(observation)

        valid_option_ids = {item.regimen_id for item in observation.substitution_options}
        if suggested_regimen_id not in valid_option_ids:
            return heuristic_action(observation)

        if pending_regimens and suggested_regimen_id not in pending_regimens:
            return heuristic_action(observation)

        return {
            "action_type": "suggest_alternative",
            "interaction_id": None,
            "suggested_regimen_id": suggested_regimen_id,
            "rationale": payload.get("rationale", ""),
        }

    if action_type == "finish":
        if unresolved:
            return heuristic_action(observation)
        if observation.task_level == "hard" and pending_regimens:
            return heuristic_action(observation)
        return {
            "action_type": "finish",
            "interaction_id": None,
            "suggested_regimen_id": None,
            "rationale": payload.get("rationale", ""),
        }

    return heuristic_action(observation)


def parse_action(content: str, observation: DdiObservation) -> Dict:
    if not content:
        return heuristic_action(observation)

    stripped = content.strip()
    try:
        parsed = json.loads(stripped)
    except json.JSONDecodeError:
        match = JSON_BLOCK.search(stripped)
        if not match:
            return heuristic_action(observation)
        try:
            parsed = json.loads(match.group(0))
        except json.JSONDecodeError:
            return heuristic_action(observation)

    candidate = {
        "action_type": parsed.get("action_type"),
        "interaction_id": parsed.get("interaction_id"),
        "suggested_regimen_id": parsed.get("suggested_regimen_id"),
        "rationale": parsed.get("rationale", ""),
    }
    try:
        DdiAction(**candidate)
        return candidate
    except Exception:
        return heuristic_action(observation)


def call_model(client: OpenAI, observation: DdiObservation, history: List[str]) -> Dict:
    user_prompt = observation_to_prompt(observation, history)
    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
    )
    response_text = completion.choices[0].message.content or ""
    return parse_action(response_text, observation)


async def maybe_await(value):
    return await value if inspect.isawaitable(value) else value


def is_server_ready(base_url: str) -> bool:
    health_url = f"{base_url.rstrip('/')}/health"
    try:
        with urlrequest.urlopen(health_url, timeout=2.0) as response:
            status = getattr(response, "status", 200)
            return 200 <= status < 300
    except (urlerror.URLError, TimeoutError, ValueError):
        return False


async def create_env() -> DdiEnv:
    if ENV_BASE_URL:
        return DdiEnv(base_url=ENV_BASE_URL)

    if is_server_ready(DEFAULT_LOCAL_ENV_BASE_URL):
        return DdiEnv(base_url=DEFAULT_LOCAL_ENV_BASE_URL)

    from openenv.core.containers.runtime import LocalDockerProvider

    provider = LocalDockerProvider()
    base_url = provider.start_container(ENV_IMAGE)

    try:
        provider.wait_for_ready(base_url, timeout_s=DOCKER_READY_TIMEOUT)
    except TimeoutError as exc:
        provider.stop_container()
        raise RuntimeError(
            f"Container for image '{ENV_IMAGE}' did not become ready within {DOCKER_READY_TIMEOUT}s. "
            "Set ENV_BASE_URL to a running server (e.g. http://localhost:8000), "
            "or rebuild and test the image locally."
        ) from exc

    env = DdiEnv(base_url=base_url, provider=provider)
    await env.connect()
    return env


async def run_baseline() -> None:
    rewards: List[float] = []
    history: List[str] = []
    steps_taken = 0
    success = False
    env = None

    log_start(task=TASK_NAME, env=BENCHMARK, model=MODEL_NAME or "unknown")

    try:
        if not API_KEY or not MODEL_NAME:
            return

        client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)
        env = await create_env()

        reset_result = await maybe_await(env.reset())
        observation = reset_result.observation
        done = bool(reset_result.done)
        step_limit = min(observation.step_budget or MAX_STEPS, MAX_STEPS)

        for step in range(1, step_limit + 1):
            if done:
                break

            try:
                payload = await asyncio.to_thread(call_model, client, observation, history)
                payload = apply_action_guardrails(payload, observation)
            except Exception:
                payload = heuristic_action(observation)

            action = DdiAction(**payload)
            result = await maybe_await(env.step(action))
            observation = result.observation

            reward = float(result.reward or 0.0)
            done = bool(result.done)
            error = last_action_error(observation)

            rewards.append(reward)
            steps_taken = step

            log_step(
                step=step,
                action=action_to_str(action),
                reward=reward,
                done=done,
                error=error,
            )

            history.append(
                f"step={step} action={action.action_type} interaction={action.interaction_id} "
                f"regimen={action.suggested_regimen_id} reward={reward:.2f}"
            )

            if done:
                final_score = observation.final_score if observation.final_score is not None else 0.0
                success = final_score >= SUCCESS_SCORE_THRESHOLD
                break
    except Exception:
        success = False
    finally:
        if env is not None:
            try:
                await maybe_await(env.close())
            except Exception:
                pass

        log_end(success=success, steps=steps_taken, rewards=rewards)


if __name__ == "__main__":
    asyncio.run(run_baseline())

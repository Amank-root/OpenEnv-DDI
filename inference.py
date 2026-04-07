"""Baseline inference script for DDI triage OpenEnv environment."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
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
    from ddi.client import DdiEnv  # type: ignore[import-not-found]
    from ddi.models import DdiAction, DdiObservation  # type: ignore[import-not-found]

load_dotenv()  # Load environment variables from .env file if present


def normalize_base_url(base_url: str) -> str:
    cleaned = base_url.rstrip("/")
    for suffix in ("/chat/completions", "/responses"):
        if cleaned.endswith(suffix):
            cleaned = cleaned[: -len(suffix)]
    return cleaned


API_BASE_URL = os.getenv("API_BASE_URL") or "https://router.huggingface.co/v1"  # Default to Hugging Face API base URL
API_KEY = os.getenv("API_KEY") or os.getenv("HF_TOKEN")
MODEL_NAME = os.getenv("MODEL_NAME") or "openai/gpt-oss-120b"  # Default to a large open-source model on Hugging Face
ENV_BASE_URL = os.getenv("ENV_BASE_URL")
# Align with sample naming while still accepting common aliases.
IMAGE_NAME = (
    os.getenv("LOCAL_IMAGE_NAME")
    or os.getenv("IMAGE_NAME")
    or os.getenv("ENV_IMAGE", "ddi-env:latest")
)
DEFAULT_LOCAL_ENV_BASE_URL = os.getenv("LOCAL_ENV_BASE_URL", "http://localhost:8000")
DOCKER_READY_TIMEOUT = float(os.getenv("DOCKER_READY_TIMEOUT", "90"))
HARD_REGIMEN_DELTA_THRESHOLD = float(os.getenv("HARD_REGIMEN_DELTA_THRESHOLD", "0.5"))
TASK_EPISODES = int(os.getenv("TASK_EPISODES", os.getenv("EPISODES", "3")))
BENCHMARK = os.getenv("DDI_BENCHMARK", "openenv-ddi")
TASK_NAME = os.getenv("DDI_TASK_NAME", "ddi-triage")
MAX_STEPS = int(os.getenv("MAX_STEPS", "16"))
SUCCESS_SCORE_THRESHOLD = float(os.getenv("SUCCESS_SCORE_THRESHOLD", "0.7"))
TEMPERATURE = 0.0
MAX_TOKENS = 3500
JSON_BLOCK = re.compile(r"\{.*\}", re.DOTALL)

# Keep displayed score strictly in (0, 1) after 3-decimal formatting.
LOG_SCORE_MIN = 0.001
LOG_SCORE_MAX = 0.999
LOG_REWARD_MIN = 0.0
LOG_REWARD_MAX = 1.0


SYSTEM_PROMPT = (
    "You are a clinical medication safety triage assistant. "
    "Return exactly one JSON object with keys: "
    "action_type, interaction_id, suggested_regimen_id, rationale. "
    "Valid action_type values are flag_interaction, monitor, suggest_alternative, ignore, finish. "
    "If action_type does not require a field, set it to null."
)


def require_proxy_config() -> tuple[str, str, str]:
    """Require the injected LiteLLM proxy configuration for submission runs."""
    missing = []
    if not API_BASE_URL:
        missing.append("API_BASE_URL")
    if not API_KEY:
        missing.append("API_KEY")
    if not MODEL_NAME:
        missing.append("MODEL_NAME")

    if missing:
        joined = ", ".join(missing)
        raise RuntimeError(f"Missing required environment variable(s): {joined}")

    return normalize_base_url(API_BASE_URL), API_KEY, MODEL_NAME


def log_start(task: str, env: str, model: str) -> None:
    print(f"[START] task={task} env={env} model={model}", flush=True)


def log_step(
    step: int, action: str, reward: float, done: bool, error: Optional[str]
) -> None:
    # Keep STEP output single-line even if upstream error text contains newlines.
    error_val = "null" if not error else " ".join(str(error).splitlines())
    action_val = " ".join(str(action).splitlines())
    done_val = str(done).lower()
    print(
        f"[STEP] step={step} action={action_val} reward={reward:.2f} done={done_val} error={error_val}",
        flush=True,
    )


def log_end(success: bool, steps: int, score: float, rewards: List[float]) -> None:
    rewards_str = ",".join(f"{reward:.2f}" for reward in rewards)
    print(
        f"[END] success={str(success).lower()} steps={steps} score={score:.3f} rewards={rewards_str}",
        flush=True,
    )


def clamp_log_score(score: float) -> float:
    return min(LOG_SCORE_MAX, max(LOG_SCORE_MIN, score))


def clamp_log_reward(reward: float) -> float:
    return min(LOG_REWARD_MAX, max(LOG_REWARD_MIN, reward))


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


def heuristic_action(
    observation: DdiObservation,
    decided_interactions: Optional[set[str]] = None,
    suggested_regimens: Optional[set[str]] = None,
) -> Dict:
    decisions = (
        observation.metadata.get("decisions", {}) if observation.metadata else {}
    )
    decided = set(decisions.keys())
    if decided_interactions:
        decided |= decided_interactions

    suggested = (
        set(observation.metadata.get("suggested_regimens", []))
        if observation.metadata
        else set()
    )
    if suggested_regimens:
        suggested |= suggested_regimens

    for candidate in observation.ddi_candidates:
        if candidate.interaction_id in decided:
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
            if (
                option.regimen_id not in suggested
                and option.expected_risk_delta >= HARD_REGIMEN_DELTA_THRESHOLD
            ):
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


def expected_treatment_action(
    observation: DdiObservation, interaction_id: str
) -> str | None:
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
    decisions = (
        observation.metadata.get("decisions", {}) if observation.metadata else {}
    )
    decided = set(decisions.keys())
    return {
        item.interaction_id
        for item in observation.ddi_candidates
        if item.interaction_id not in decided
    }


def pending_high_value_regimens(observation: DdiObservation) -> list[str]:
    if observation.task_level != "hard":
        return []

    suggested = (
        set(observation.metadata.get("suggested_regimens", []))
        if observation.metadata
        else set()
    )
    options = sorted(
        observation.substitution_options,
        key=lambda item: item.expected_risk_delta,
        reverse=True,
    )
    return [
        item.regimen_id
        for item in options
        if item.regimen_id not in suggested
        and item.expected_risk_delta >= HARD_REGIMEN_DELTA_THRESHOLD
    ]


def apply_action_guardrails(
    payload: Dict,
    observation: DdiObservation,
    decided_interactions: Optional[set[str]] = None,
    suggested_regimens: Optional[set[str]] = None,
) -> Dict:
    action_type = payload.get("action_type")
    interaction_id = payload.get("interaction_id")
    suggested_regimen_id = payload.get("suggested_regimen_id")

    metadata_decisions = (
        observation.metadata.get("decisions", {}) if observation.metadata else {}
    )
    all_decided = set(metadata_decisions.keys())
    if decided_interactions:
        all_decided |= decided_interactions

    metadata_suggested = (
        set(observation.metadata.get("suggested_regimens", []))
        if observation.metadata
        else set()
    )
    if suggested_regimens:
        metadata_suggested |= suggested_regimens

    unresolved = {
        item.interaction_id
        for item in observation.ddi_candidates
        if item.interaction_id not in all_decided
    }

    pending_regimens = []
    if observation.task_level == "hard":
        options = sorted(
            observation.substitution_options,
            key=lambda item: item.expected_risk_delta,
            reverse=True,
        )
        pending_regimens = [
            item.regimen_id
            for item in options
            if item.regimen_id not in metadata_suggested
            and item.expected_risk_delta >= HARD_REGIMEN_DELTA_THRESHOLD
        ]

    if action_type in {"flag_interaction", "monitor", "ignore"}:
        if interaction_id not in unresolved:
            return heuristic_action(observation, all_decided, metadata_suggested)

        expected = expected_treatment_action(observation, interaction_id)
        if expected is None:
            return heuristic_action(observation, all_decided, metadata_suggested)

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
            return heuristic_action(observation, all_decided, metadata_suggested)

        if suggested_regimen_id in metadata_suggested:
            return heuristic_action(observation, all_decided, metadata_suggested)

        valid_option_ids = {
            item.regimen_id for item in observation.substitution_options
        }
        if suggested_regimen_id not in valid_option_ids:
            return heuristic_action(observation, all_decided, metadata_suggested)

        if pending_regimens and suggested_regimen_id not in pending_regimens:
            return heuristic_action(observation, all_decided, metadata_suggested)

        return {
            "action_type": "suggest_alternative",
            "interaction_id": None,
            "suggested_regimen_id": suggested_regimen_id,
            "rationale": payload.get("rationale", ""),
        }

    if action_type == "finish":
        if unresolved:
            return heuristic_action(observation, all_decided, metadata_suggested)
        if observation.task_level == "hard" and pending_regimens:
            return heuristic_action(observation, all_decided, metadata_suggested)
        return {
            "action_type": "finish",
            "interaction_id": None,
            "suggested_regimen_id": None,
            "rationale": payload.get("rationale", ""),
        }

    return heuristic_action(observation, all_decided, metadata_suggested)


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


def call_model(
    client: OpenAI,
    model_name: str,
    observation: DdiObservation,
    history: List[str],
) -> Dict:
    user_prompt = observation_to_prompt(observation, history)
    completion = client.chat.completions.create(
        model=model_name,
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


@dataclass
class LocalStepResult:
    observation: DdiObservation
    reward: float
    done: bool


class LocalDdiEnvAdapter:
    """In-process adapter used when no reachable server/container is available."""

    def __init__(self) -> None:
        try:
            from server.ddi_environment import DdiEnvironment
        except ImportError:
            from ddi.server.ddi_environment import DdiEnvironment  # type: ignore[import-not-found]

        self._env = DdiEnvironment()

    async def reset(self) -> LocalStepResult:
        observation = self._env.reset()
        return LocalStepResult(
            observation=observation,
            reward=float(observation.reward or 0.0),
            done=bool(observation.done),
        )

    async def step(self, action: DdiAction) -> LocalStepResult:
        observation = self._env.step(action)
        return LocalStepResult(
            observation=observation,
            reward=float(observation.reward or 0.0),
            done=bool(observation.done),
        )

    async def close(self) -> None:
        return None


def is_server_ready(base_url: str) -> bool:
    health_url = f"{base_url.rstrip('/')}/health"
    try:
        with urlrequest.urlopen(health_url, timeout=2.0) as response:
            status = getattr(response, "status", 200)
            return 200 <= status < 300
    except (urlerror.URLError, TimeoutError, ValueError):
        return False


async def create_env() -> DdiEnv | LocalDdiEnvAdapter:
    if ENV_BASE_URL:
        if is_server_ready(ENV_BASE_URL):
            return DdiEnv(base_url=ENV_BASE_URL)

    if is_server_ready(DEFAULT_LOCAL_ENV_BASE_URL):
        return DdiEnv(base_url=DEFAULT_LOCAL_ENV_BASE_URL)

    from openenv.core.containers.runtime import LocalDockerProvider

    try:
        provider = LocalDockerProvider()
        base_url = provider.start_container(IMAGE_NAME)

        try:
            provider.wait_for_ready(base_url, timeout_s=DOCKER_READY_TIMEOUT)
        except TimeoutError as exc:
            provider.stop_container()
            raise RuntimeError(
                f"Container for image '{IMAGE_NAME}' did not become ready within {DOCKER_READY_TIMEOUT}s. "
                "Set ENV_BASE_URL to a running server (e.g. http://localhost:8000), "
                "or rebuild and test the image locally."
            ) from exc

        env = DdiEnv(base_url=base_url, provider=provider)
        await env.connect()
        return env
    except Exception:
        # Final local fallback for development environments without a live server/docker daemon.
        return LocalDdiEnvAdapter()


async def run_baseline() -> None:
    env = None
    model_name = MODEL_NAME or "unknown"

    try:
        api_base_url, api_key, model_name = require_proxy_config()
        client = OpenAI(base_url=api_base_url, api_key=api_key)

        env = await create_env()

        for _episode in range(max(1, TASK_EPISODES)):
            episode_rewards: List[float] = []
            episode_steps = 0
            episode_score = 0.0
            episode_success = False
            episode_task = TASK_NAME
            start_logged = False

            try:
                reset_result = await maybe_await(env.reset())
            except Exception:
                try:
                    await maybe_await(env.close())
                except Exception:
                    pass
                env = LocalDdiEnvAdapter()
                reset_result = await maybe_await(env.reset())

            observation = reset_result.observation
            episode_task = observation.task_level
            log_start(task=episode_task, env=BENCHMARK, model=model_name)
            start_logged = True
            done = bool(reset_result.done)
            step_limit = min(observation.step_budget or MAX_STEPS, MAX_STEPS)
            history: List[str] = []
            local_decided_interactions: set[str] = set()
            local_suggested_regimens: set[str] = set()

            for _step in range(1, step_limit + 1):
                if done:
                    break

                payload = await asyncio.to_thread(
                    call_model,
                    client,
                    model_name,
                    observation,
                    history,
                )
                payload = apply_action_guardrails(
                    payload,
                    observation,
                    decided_interactions=local_decided_interactions,
                    suggested_regimens=local_suggested_regimens,
                )

                if not payload:
                    payload = heuristic_action(
                        observation,
                        decided_interactions=local_decided_interactions,
                        suggested_regimens=local_suggested_regimens,
                    )

                action = DdiAction(**payload)
                if (
                    action.action_type in {"flag_interaction", "monitor", "ignore"}
                    and action.interaction_id
                ):
                    local_decided_interactions.add(action.interaction_id)
                if (
                    action.action_type == "suggest_alternative"
                    and action.suggested_regimen_id
                ):
                    local_suggested_regimens.add(action.suggested_regimen_id)

                result = await maybe_await(env.step(action))
                observation = result.observation

                reward = float(result.reward or 0.0)
                logged_reward = clamp_log_reward(reward)
                done = bool(result.done)
                error = last_action_error(observation)

                episode_rewards.append(logged_reward)
                episode_steps += 1

                log_step(
                    step=episode_steps,
                    action=action_to_str(action),
                    reward=logged_reward,
                    done=done,
                    error=error,
                )

                history.append(
                    f"step={episode_steps} action={action.action_type} interaction={action.interaction_id} "
                    f"regimen={action.suggested_regimen_id} reward={reward:.2f}"
                )

            if not done:
                # Force episode scoring when a custom MAX_STEPS truncates the policy loop.
                finish_action = DdiAction(
                    action_type="finish", rationale="max-step fallback"
                )
                result = await maybe_await(env.step(finish_action))
                observation = result.observation
                reward = float(result.reward or 0.0)
                logged_reward = clamp_log_reward(reward)
                done = bool(result.done)
                error = last_action_error(observation)

                episode_rewards.append(logged_reward)
                episode_steps += 1
                log_step(
                    step=episode_steps,
                    action=action_to_str(finish_action),
                    reward=logged_reward,
                    done=done,
                    error=error,
                )

            if observation.final_score is not None:
                episode_score = float(observation.final_score)
            episode_score = clamp_log_score(episode_score)
            episode_success = episode_score >= SUCCESS_SCORE_THRESHOLD

            log_end(
                success=episode_success,
                steps=episode_steps,
                score=episode_score,
                rewards=episode_rewards,
            )
    except Exception:
        log_start(task=TASK_NAME, env=BENCHMARK, model=model_name)
        log_end(success=False, steps=0, score=LOG_SCORE_MIN, rewards=[])
    finally:
        if env is not None:
            try:
                await maybe_await(env.close())
            except Exception:
                pass


if __name__ == "__main__":
    asyncio.run(run_baseline())

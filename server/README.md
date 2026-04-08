# Server Package

This folder contains the runtime server implementation for the DDI OpenEnv environment.

## What This Server Does

- Hosts the environment over HTTP and WebSocket using OpenEnv's FastAPI server wrapper.
- Exposes reset/step/state/schema endpoints used by the baseline agent and validators.
- Creates isolated environment instances per session when the backend is configured for concurrent sessions.

## Key Files

- `app.py`: FastAPI entrypoint. Wires the environment, action model, and observation model into `create_app(...)`.
- `ddi_environment.py`: Core environment logic (reset, step, reward shaping, episode termination, task selection).
- `Dockerfile`: Container runtime for deployment.
- `requirements.txt`: Python dependencies used by this server image.

## API Surface

When running, the server exposes OpenEnv-compatible endpoints:

- `POST /reset`
- `POST /step`
- `GET /state`
- `GET /schema`
- `GET /health`
- `WS /ws`

## Task and Case Routing

The environment supports multiple task levels in one server instance:

- easy
- medium
- hard

Task scheduling behavior is controlled with environment variables:

- `DDI_TASK_SAMPLING=curriculum|mixed|mixed_seeded|mixed_shuffled`
- `DDI_TASK_SHUFFLE_SEED` (used by seeded/shuffled task modes)
- `DDI_TASK_SHUFFLE_WINDOW` (shuffle block size)

Case split selection is controlled by:

- `DDI_CASE_SPLIT=all|train|validation`

## Run Locally

From repository root:

```bash
uvicorn server.app:app --host 0.0.0.0 --port 8000 --reload
```

Or via module entrypoint:

```bash
python -m server.app --port 8000
```

## Docker

Build from repository root:

```bash
docker build -t ddi-env:latest -f server/Dockerfile .
```

Run:

```bash
docker run -p 8000:8000 ddi-env:latest
```

## Notes for Contributors

- Keep environment transition logic deterministic unless randomness is intentionally introduced with an explicit seed.
- If you change reward shaping, run tests in `tests/` and verify submission log format from `inference.py` still matches the required START/STEP/END schema.
- Avoid changing endpoint behavior in ways that break OpenEnv validator expectations.

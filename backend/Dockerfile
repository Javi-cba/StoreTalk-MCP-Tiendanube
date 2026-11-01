# StoreTalk backend (FastAPI REST + FastMCP) — one image, one process.
# Build:  docker build -t storetalk-backend .
# Run:    docker run --env-file .env -p 8000:8000 storetalk-backend

# --- Stage 1: install dependencies with uv ---
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=0

WORKDIR /app

# Lockfile first so the dependency layer is cached between code changes
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

# --- Stage 2: slim runtime (no uv, no build tools) ---
FROM python:3.12-slim-bookworm

ENV PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH" \
    AWS_LWA_PORT=8000 \
    AWS_LWA_READINESS_CHECK_PATH=/health

# Lambda Web Adapter: lets AWS Lambda run this same uvicorn server. Inert on ECS/local.
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:1.1.0 /lambda-adapter /opt/extensions/lambda-adapter

RUN useradd --create-home --uid 1000 app
WORKDIR /app

COPY --from=builder /app/.venv /app/.venv
COPY alembic.ini ./
COPY alembic ./alembic
COPY scripts ./scripts
COPY src ./src

USER app
EXPOSE 8000

# --proxy-headers: behind the ALB, keep https:// in generated URLs (OAuth issuer, redirects)
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers", "--forwarded-allow-ips", "*"]

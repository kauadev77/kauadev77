# FastAPI Production Template

A clean backend template showing how I structure a small **production-ready FastAPI service**.

It includes application configuration, API versioning, health checks, PostgreSQL-ready settings, Docker, tests and GitHub Actions.

## Features

- FastAPI application factory
- Versioned API routes
- Environment-based settings
- Health and readiness endpoints
- Structured service layer
- Docker support
- Automated tests with pytest
- GitHub Actions CI
- PostgreSQL connection string support

## Structure

```text
app/
├── api/
│   └── v1/
├── core/
├── services/
├── main.py
└── schemas.py
tests/
Dockerfile
docker-compose.yml
.github/workflows/ci.yml
```

## Local development

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Tests

```bash
pytest
```

## Docker

```bash
docker compose up --build
```

API docs: `http://localhost:8000/docs`

## Why this project exists

This repository demonstrates engineering practices I use when working with APIs and production systems, without exposing any proprietary code or internal architecture from my professional work.

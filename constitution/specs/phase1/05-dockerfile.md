# Spec: Dockerfile

## What

Container image that runs the FastMCP skill server anywhere Docker is available.

## Why

Removes "works on my machine" friction. Any operator can pull the repo, build the image, and have a running server without installing Python or uv locally.

## Behavior

- Base image: `python:3.12-slim`
- `uv` installed inside the image; used for dependency install and running the server
- Dependencies installed from `pyproject.toml` + lockfile at build time (no network at runtime)
- `SKILLS_DIR` defaults to `/app/skills` inside the container
- Skills directory mountable as a volume: `-v ./skills:/app/skills`
- `API_KEY` and `PORT` passed as env vars at `docker run` time — not baked into image
- Exposed port: `8000` (matches `PORT` default)
- CMD: `uv run python src/server.py`

**Minimal run example:**
```bash
docker build -t fastmcp-skill-server .
docker run -e API_KEY=secret -p 8000:8000 fastmcp-skill-server
```

## Acceptance Criteria

- [ ] `docker build` succeeds from a clean checkout
- [ ] `docker run` with `API_KEY` env var starts server and accepts connections
- [ ] Skills directory can be overridden via volume mount
- [ ] Image contains no secrets or credentials

## Out of Scope

- Multi-stage build optimization
- Docker Compose file
- Published image on Docker Hub / GHCR

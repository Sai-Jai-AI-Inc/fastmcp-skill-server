# Spec: Server Setup

## What

Bootstrap a FastMCP server as an installable Python project managed by `uv`.

## Why

Establishes the runnable foundation everything else in Phase 1 builds on. Must exist before any tool, auth, or Docker work can be validated.

## Behavior

- Project root has `pyproject.toml` declaring `fastmcp` as a dependency
- Server entry point: `src/server.py`
- `uv run python src/server.py` starts the server
- Transport: streamable-HTTP on `0.0.0.0:8000` (port configurable via `PORT` env var)
- `SKILLS_DIR` env var controls skill file location; defaults to `./skills`
- Server name exposed to MCP clients: `fastmcp-skill-server`

## Acceptance Criteria

- [x] `uv run python src/server.py` starts without error
- [x] MCP client can connect and receive server info
- [x] `SKILLS_DIR` and `PORT` read from environment at startup

## Out of Scope

- Hot reload of `SKILLS_DIR` at runtime
- Any tool implementation (covered in separate specs)

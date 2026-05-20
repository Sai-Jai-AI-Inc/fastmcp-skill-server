# Spec: API Key Auth

## What

Protect all tool calls with a static API key validated as a Bearer token.

## Why

Skills may be proprietary. Unauthenticated access would expose them to anyone who can reach the server. API key is the simplest auth shape that still teaches the "secured MCP server" pattern.

## Behavior

- Client passes key in the `Authorization` header: `Authorization: Bearer <key>`
- Server reads expected key from `API_KEY` env var at startup
- FastMCP's bearer auth mechanism validates the token on every tool call
- Any request with a missing or incorrect key receives an auth error and no tool is invoked
- `API_KEY` is required — server fails to start if env var is unset or empty

## Acceptance Criteria

- [ ] Valid key → tool call succeeds
- [ ] Missing `Authorization` header → auth error
- [ ] Wrong key → auth error
- [ ] Server refuses to start if `API_KEY` is unset

## Out of Scope

- Key rotation
- Per-key permissions or scopes
- OAuth flows (future phase)

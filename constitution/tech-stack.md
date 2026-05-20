# Tech Stack

## Runtime

| Layer | Choice | Reason |
|---|---|---|
| Language | Python 3.12+ | FastMCP is Python-native |
| Framework | FastMCP | Batteries-included MCP server: tool registration, OAuth, transports. Open source, vendor-neutral. |
| Package manager | uv | Fast, lockfile-based, reproducible |
| Container | Docker | Deploy anywhere a Docker runtime exists |

## Server

**FastMCP** handles:
- MCP protocol compliance
- Tool registration (`list_skills`, `get_skill`)
- OAuth 2.0 server-side flow
- HTTP transport (SSE or streamable HTTP)

No raw MCP SDK, no LangChain, no vendor lock-in.

## Skill Storage

Skills live in a Git repository (one repo per server instance). The server reads `.md` files directly from the filesystem at startup or on-demand. No database. The Git repo is the source of truth.

Skill file format follows the Claude Code skills convention: YAML frontmatter + prompt body.

## Auth

OAuth 2.0. FastMCP provides the OAuth server primitives. Clients (Claude Code) authenticate before calling any tool.

## Eval Pipeline

Skill PRs are validated before merge using an end-to-end eval pipeline modeled after [agoda-com/agent-catalog-eval](https://github.com/agoda-com/agent-catalog-eval). A skill that does not pass eval does not ship.

## Consumer

Claude Code only (current scope). The MCP server is configured as an MCP server entry in the Claude Code config, connected over HTTP with OAuth credentials.

## Deployment

A `Dockerfile` ships with the repo. Build once, run anywhere Docker is available: local, VPS, cloud run, Fly.io, etc.

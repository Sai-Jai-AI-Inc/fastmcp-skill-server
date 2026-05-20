# fastmcp-skill-server

Reference implementation of an MCP server (built on [FastMCP](https://github.com/jlowin/fastmcp)) as a distribution layer for Claude Code skills.

A companion to a technical post. Read it, fork it, adapt it.

## What it does

Exposes two MCP tools:

| Tool | Description |
|---|---|
| `list_skills` | Returns filenames of all available skills |
| `get_skill` | Returns raw `.md` content of a skill by filename |

Claude Code connects to the server, discovers skills, and loads them on demand. Skills live as `.md` files in a `skills/` directory — the server just serves them.

## Stack

- **Python 3.12+** managed by `uv`
- **FastMCP** — MCP protocol, tool registration, bearer auth
- **Docker** — single-container deployment, no dependencies at runtime
- **API key** — Bearer token auth via `API_KEY` env var

## Quickstart

```bash
# Build
docker build -t fastmcp-skill-server .

# Run
docker run -e API_KEY=your-secret -p 8000:8000 fastmcp-skill-server
```

To use a custom skills directory:

```bash
docker run -e API_KEY=your-secret -p 8000:8000 \
  -v ./my-skills:/app/skills \
  fastmcp-skill-server
```

Add to Claude Code's MCP config:

```json
{
  "mcpServers": {
    "skill-server": {
      "url": "http://localhost:8000",
      "headers": { "Authorization": "Bearer your-secret" }
    }
  }
}
```

## Environment variables

| Variable | Default | Required |
|---|---|---|
| `API_KEY` | — | Yes |
| `SKILLS_DIR` | `./skills` | No |
| `PORT` | `8000` | No |

## Project structure

```
skills/          # Skill .md files served by the server
src/
  server.py      # FastMCP app entry point
constitution/    # Mission, tech stack, roadmap, feature specs
Dockerfile
pyproject.toml
```

## Contributing skills

Skills are authored as pull requests. See the contribution guide (Phase 2).

## Roadmap

See [`constitution/roadmap.md`](constitution/roadmap.md).

## License

MIT

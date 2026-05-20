# Spec: `list_skills` Tool

## What

MCP tool that returns all available skills on the server.

## Why

Claude Code needs to know what skills exist before it can fetch one. Discovery is the entry point to the distribution pattern.

## Behavior

- Tool name: `list_skills`
- Input: none
- Scans `SKILLS_DIR` for files matching `*.md`
- Returns a JSON array of filenames (basename only, with `.md` extension)
- If `SKILLS_DIR` is empty or contains no `.md` files, returns empty array `[]`
- Subdirectories are ignored — flat scan only

**Example response:**
```json
["hello-world.md", "echo.md", "greet.md"]
```

## Acceptance Criteria

- [ ] Tool appears in MCP tool list
- [ ] Returns correct filenames for all `.md` files in `SKILLS_DIR`
- [ ] Returns `[]` when `SKILLS_DIR` is empty
- [ ] Does not include non-`.md` files in results
- [ ] Does not recurse into subdirectories

## Out of Scope

- Skill metadata (name, description, tags) — filenames only in this phase
- Filtering or search

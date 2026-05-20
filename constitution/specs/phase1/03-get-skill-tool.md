# Spec: `get_skill` Tool

## What

MCP tool that fetches the raw content of a skill file by filename.

## Why

The agent needs the full skill `.md` content to load it into Claude Code. Filename-based lookup keeps the API simple and matches how Claude Code identifies skills.

## Behavior

- Tool name: `get_skill`
- Input: `filename` (string) — the `.md` filename as returned by `list_skills`
- Reads `{SKILLS_DIR}/{filename}` and returns its full text content as a string
- **Error — not found:** if filename does not exist in `SKILLS_DIR`, return MCP error with message `"Skill '{filename}' not found"`
- **Security:** `filename` must be a bare filename with no path separators. Any input containing `/` or `\` or `..` is rejected with MCP error `"Invalid filename"`; this prevents path traversal outside `SKILLS_DIR`

**Example input:**
```json
{ "filename": "hello-world.md" }
```

**Example response:** raw string content of the file.

## Acceptance Criteria

- [ ] Returns full raw content of an existing skill file
- [ ] Returns MCP error for a filename that does not exist
- [ ] Rejects filenames containing `/`, `\`, or `..`
- [ ] Content returned is byte-for-byte identical to the file on disk

## Out of Scope

- Parsing or transforming skill content
- Partial reads or line ranges

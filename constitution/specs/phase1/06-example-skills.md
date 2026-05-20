# Spec: Example Skills

## What

A minimal set of toy skill files bundled in `skills/` to prove the end-to-end pattern works.

## Why

Without real skills in the repo, the server cannot be validated. These are not meant to be useful skills — they exist to exercise `list_skills` and `get_skill` and confirm Claude Code can load a skill fetched from the server.

## Behavior

Three files in `skills/`:

| Filename | What it does |
|---|---|
| `hello-world.md` | Responds "Hello, World!" when invoked |
| `echo.md` | Repeats back whatever the user says |
| `greet.md` | Greets the user by name |

Each file is a valid Claude Code skill: YAML frontmatter (`name`, `description`) followed by a prompt body. Content is minimal — enough to be loadable and runnable in Claude Code, no more.

**Minimal valid structure:**
```markdown
---
name: hello-world
description: Responds with Hello World
---

When the user invokes this skill, respond with exactly: "Hello, World!"
```

## Acceptance Criteria

- [ ] All three `.md` files present in `skills/`
- [ ] Each file has valid YAML frontmatter with `name` and `description`
- [ ] `list_skills` returns all three filenames
- [ ] `get_skill` returns correct content for each
- [ ] At least one skill executes correctly when loaded into Claude Code from the server

## Out of Scope

- Useful or production-quality skill content
- Skills with parameters or complex logic

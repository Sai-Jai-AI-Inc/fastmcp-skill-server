# Roadmap

This is a living document. Each phase maps to a discrete set of features. Each feature follows a repeatable process:

> **Plan → Implement → Validate**

A feature is not done until it is validated. Validation means the behavior is confirmed to work end-to-end, not just that tests pass.

---

## Phase 1 — Deployable Skill Server

**Goal:** A running MCP server that Claude Code can connect to, authenticate with, and use to discover and fetch skills.

**Scope:**
- [ ] FastMCP server with two tools: `list_skills` and `get_skill`
- [ ] Skills identified and fetched by filename
- [ ] Skills loaded from a local directory of `.md` files
- [ ] OAuth 2.0 auth via FastMCP
- [ ] `Dockerfile` for container deployment
- [ ] Minimal skill library (2–3 example skills) to prove the pattern

**Done when:**
- [ ] Claude Code connects to a Docker-hosted instance over HTTP with OAuth
- [ ] `list_skills` returns available skills
- [ ] `get_skill` returns raw `.md` content by filename
- [ ] A skill retrieved from the server executes correctly inside Claude Code

**Feature specs:** TBD (drafted before implementation begins)

---

## Phase 2 — Skill Authorship Pipeline

**Goal:** A PR-based workflow for contributing, reviewing, and validating new skills.

**Scope:**
- [ ] Contribution guide for skill authors
- [ ] Eval harness (based on agoda-com/agent-catalog-eval pattern)
- [ ] CI check that runs evals on skill PRs before merge
- [ ] Skill metadata schema (name, description, version, tags)

**Done when:**
- [ ] A contributor can open a PR with a new skill
- [ ] CI runs evals and blocks merge on failure
- [ ] Merged skill is immediately available via the server

---

## Principles

- No phase begins implementation until its feature spec is written and agreed upon
- Phases are sequential; scope does not bleed across phase boundaries
- The reference implementation stays readable — complexity added only when it earns its place

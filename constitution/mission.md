# Mission

## Problem

Claude Code skills are powerful but trapped in individual developer configs and private repos. There is no standard way to discover, distribute, or consume a shared skill library across teams or agents. Skills today are copy-pasted, silently forked, and never updated.

## Solution

A FastMCP server that acts as a distribution layer for Claude Code skills. Agents call the server to discover and fetch skill files dynamically. The server is the single source of truth for a curated skill library. Skills are authored as pull requests, reviewed by maintainers, and validated through end-to-end evals before merge.

This project is a **reference implementation** — a companion to a technical post demonstrating the pattern. It is designed to be read, forked, and adapted, not consumed as a managed service.

## Goals

- Demonstrate MCP as a skill distribution protocol for Claude Code
- Provide a production-shaped reference: OAuth, Docker, eval pipeline, PR-based authorship
- Keep the implementation minimal enough to be understood in a single sitting

## Non-Goals

- Multi-tenant SaaS hosting
- Supporting agent runtimes other than Claude Code (in this phase)
- Skill execution — the server serves skill content only, it does not run skills

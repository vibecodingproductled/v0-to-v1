# Connecting the harness to your real tools (MCP)

A harness that can only read files is a notebook. A harness wired to your actual tools, your docs, your chat, your analytics, is where the work happens. Model Context Protocol (MCP) servers are how Claude Code reaches those external systems. This guide is about the *architecture* of that integration, not the setup mechanics (those live in the Claude Code docs).

## The principle: your tools are systems of record

The single-source-of-truth rule extends to external tools. Each tool owns a class of fact, and your harness points at it rather than copying from it:

| Fact class | Owner (system of record) | In the harness |
|-----------|--------------------------|----------------|
| Published, canonical docs | Wiki / docs tool | Pointer by page ID or URL; read on demand |
| Team decisions and shared context | Team wiki / shared memory | Read at session start; never duplicated locally |
| Usage and metrics | Analytics tool | Queried live; results summarized into the relevant context |
| Tasks and tickets | Tracker | Referenced by ID |

A knowledge context should link to the canonical doc, not paste it. A pasted copy is a duplicated fact that will drift the moment the source is edited. Pointer-by-ID keeps the tool as the truth and the harness as the index.

## The read-at-session-start pattern

If your team keeps shared context in an external system (a team wiki page, a shared memory), have a SessionStart step pull it so every session begins grounded in the same team truth. Keep it small and cache-friendly: read a single canonical page, not the whole space. This is how a harness stays aligned with a team without copying the team's knowledge into local files that then go stale.

## Which tools are worth wiring first

Start with the tools you already live in. For most PMs that is:
1. **Your tracker** (tickets, sprints), so specs turn into tickets without copy-paste.
2. **Your docs/wiki tool**, so Claude can read the canonical strategy and writeups and publish back to them.
3. **Your customer-intelligence or analytics source**, so evidence questions get live answers instead of your memory.

Add integrations when a real, recurring task needs them, not speculatively. An unused MCP server is the God Hook of the tool layer: setup cost and surface area for no return.

## The ceiling: 3-5 servers, and why it is a real limit

Every connected MCP server injects all of its tool definitions into context at session start, before your first message. This is paid every session whether you use the tools or not, and measured setups have lost most of their context window to tool definitions alone before any conversation happened. Practitioner consensus converges on 3-5 servers and roughly 10-15 active tools as the working ceiling.

Two tests before adding a server:
- **The 2x test.** Would this integration make a recurring workflow twice as good, or just slightly more convenient? Convenience does not pay its context rent.
- **The staleness test.** Does this data change faster than you could reasonably export it by hand? Stable data (templates, past docs, reference material) belongs in files; MCP is for what moves.

Watch your context meter and prune the server you use least whenever output quality drifts. Context bloat degrades results before it announces itself.

## Start read-only

Grant write access only after the integration has produced a month of output you would have shipped anyway. Until then, let the skill produce structured output you paste into the tool yourself: the pasting is cheap, and it is your review gate. Note that many tools cannot scope a token per project, so a write token is often a write token to everything your account touches. That asymmetry is why read-only is the default and write is the earned exception.

## Safety: least privilege, and do not exfiltrate

This is the part people skip, and it matters most in a public or shared harness.

- **Least privilege.** Give each MCP server the narrowest scope that does the job. Read-only where you only read. Do not grant write access to systems you only query.
- **Do not send private context to external services.** Your personal config and private knowledge contexts contain things that should not leave your machine. Be deliberate about what a skill sends to an external tool. "Summarize this and post it to the public channel" should never include a paste of your private notes.
- **Sending is publishing.** Anything written to an external system may be cached, indexed, or seen by others even if you delete it later. Treat an external write like a publish, and confirm before doing the irreversible ones.
- **Authentication is per-environment.** An integration that works in your interactive session may be absent in a headless or automated run. Do not build a skill that silently fails when a server is not authenticated; have it detect the missing tool and say so.

## Keep the boundary clean

The harness orchestrates; the tools own the data. When you find yourself copying data out of a tool and into a local file "so Claude always has it," stop. That is a duplicated fact. Point at the tool, read on demand, and let the tool stay the source of truth.

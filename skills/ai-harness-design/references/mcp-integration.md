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
1. **Your docs/wiki tool**, so Claude can read the canonical strategy and writeups and publish back to them.
2. **Your chat tool**, so it can draft and read messages in your voice.
3. **Your analytics tool**, so it can answer usage questions with live data instead of your memory.

Add integrations when a real, recurring task needs them, not speculatively. An unused MCP server is the God Hook of the tool layer: setup cost and surface area for no return.

## Safety: least privilege, and do not exfiltrate

This is the part people skip, and it matters most in a public or shared harness.

- **Least privilege.** Give each MCP server the narrowest scope that does the job. Read-only where you only read. Do not grant write access to systems you only query.
- **Do not send private context to external services.** Your personal config and private knowledge contexts contain things that should not leave your machine. Be deliberate about what a skill sends to an external tool. "Summarize this and post it to the public channel" should never include a paste of your private notes.
- **Sending is publishing.** Anything written to an external system may be cached, indexed, or seen by others even if you delete it later. Treat an external write like a publish, and confirm before doing the irreversible ones.
- **Authentication is per-environment.** An integration that works in your interactive session may be absent in a headless or automated run. Do not build a skill that silently fails when a server is not authenticated; have it detect the missing tool and say so.

## Keep the boundary clean

The harness orchestrates; the tools own the data. When you find yourself copying data out of a tool and into a local file "so Claude always has it," stop. That is a duplicated fact. Point at the tool, read on demand, and let the tool stay the source of truth.

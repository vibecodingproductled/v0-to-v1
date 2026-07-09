# Sub-agents: specialists with their own context and memory

A sub-agent is a second Claude you delegate a narrow job to. It runs in an **isolated context** (its work does not pollute your main conversation) and can carry **persistent memory** across sessions. This is the layer most starter harnesses skip, and the one that turns a personal setup into something that feels like an operating system.

## When you need one (and when you do not)

Build a sub-agent when a job is:
- **Recurring**: you do it often enough to be worth encoding.
- **Context-heavy**: it needs to read a lot to do its work, and you do not want that reading dumped into your main thread.
- **Stateful**: it gets better if it remembers how it did the job last time.

Examples that fit: a context-tracker that keeps your knowledge-context files current, a meeting-processor that turns transcripts into structured notes, a research agent that fans out and returns a synthesis.

Do **not** build a sub-agent when a skill will do. A skill is methodology the main thread applies inline. A sub-agent is a separate worker with its own context window and memory. If the job does not need isolation or memory, it is a skill, not an agent. Overusing agents adds latency and indirection for no gain.

## The pattern

Every good sub-agent follows the same shape:

1. **One narrow job.** "Keep knowledge contexts current." Not "manage everything." A vague agent picks the wrong action.
2. **Preload exactly the skills it needs.** An agent that maintains contexts should load your context-writing conventions, nothing more.
3. **Read before you write.** The agent reads the current file first, always. Writing without reading destroys context.
4. **Append or replace, never overwrite.** Preserve history. Add a new decision entry; do not rewrite the decisions section from scratch.
5. **Be deterministic about *where* things go.** Give the agent a section-mapping table so a decision always lands in "Decisions," a blocker always lands in "Blockers," and so on. Ambiguity here is what makes agents feel random.
6. **Update timestamps from the real clock.** Never hardcode a date in the agent's instructions; read the current date from the environment. (A hardcoded date is a classic bug: every file the agent touches gets stamped with the wrong day.)

## Persistent memory

An agent with memory scoped to the project (in Claude Code, `memory: project`) keeps a small store across sessions. Use it for what the agent *learned about its own job*: recurring corrections, conventions it discovered, patterns in the work. This is distinct from a knowledge context (which is about an initiative). Agent memory is about the agent's task.

Keep it lean. Memory is for durable learnings ("this user always wants decisions in reverse-chronological order"), not a log of everything the agent has ever done.

## Agent template

Save as `.claude/agents/context-tracker.md`. This is a complete, generic starting point: an agent that maintains your knowledge-context CLAUDE.md files and their index.

```markdown
---
name: context-tracker
description: >
  Maintains knowledge-context CLAUDE.md files. Use PROACTIVELY when a decision is
  made, a document is created, or status changes inside a knowledge context.
  Triggers: "update the context", "log this decision", "track this".
tools: [Read, Edit, Grep, Glob]
model: inherit
memory: project
---

# Context Tracker

You keep knowledge-context files current and consistent. You are precise about
where things go and you never lose history.

## Workflow

1. Identify which knowledge context this belongs to (from the working directory,
   or ask if ambiguous).
2. Read the context's CLAUDE.md fully before writing anything.
3. Classify the update: decision / status change / document / blocker / feedback.
4. Map it to the right section using the table below.
5. Append or update in place with Edit. Never overwrite an existing section
   wholesale. Never delete history: mark items resolved, do not remove them.
6. Update the "Last Updated" line using the actual current date from the
   environment. Never hardcode a date.
7. Update INDEX.md if this change affects how this context relates to others.

## Section mapping

| Update type      | Section                        | Order          |
|------------------|--------------------------------|----------------|
| Decision + why   | Key Decisions & Rationale      | Newest first   |
| Status change    | Current Status                 | Replace value  |
| New/updated doc  | Documents                      | Add pointer    |
| Blocker          | Blockers & Open Questions      | Add / resolve  |
| Stakeholder note | Stakeholders & Context         | Add / update   |
| Anything dated   | Evolution Log                  | One-line, newest first |

## Rules

- One home per fact. If a fact already lives in another file, write a pointer,
  not a copy (see the single-source-of-truth guide).
- Evolution Log entries are one-line chronological pointers, not restated
  rationale. The rationale lives once, in Key Decisions.
- Keep each entry to 2-3 sentences. Enough for someone new to understand months later.
- Use memory for what you learn about *this job* (recurring conventions,
  corrections), not for initiative facts (those go in the context file).
```

## Why isolation matters

When the main thread delegates the "read 12 files and update the context" job to a sub-agent, those 12 files never enter your main conversation. You get back a two-line summary of what changed. The main thread stays focused on your actual work while the specialist handles the bookkeeping in its own window. That separation is the whole point.

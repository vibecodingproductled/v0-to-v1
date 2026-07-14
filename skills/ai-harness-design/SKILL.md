---
name: ai-harness-design
description: Set up a production-grade Claude Code harness from scratch. Use when starting a new project, auditing an existing setup, helping someone new to Claude Code, or when Claude's output feels inconsistent. Covers the full architecture: CLAUDE.md, rules, skills, hooks, knowledge contexts, memory, sub-agents, personas, tool (MCP) integration, and the single-source-of-truth principle that keeps it from rotting.
---

# AI Harness Design

Your prompts are inputs to a system. The system's architecture determines the floor quality of every interaction. A well-structured harness means Claude is consistent, remembers what matters, applies the right frameworks, and fails predictably rather than randomly.

This skill teaches the architecture. Not tips. Not prompt tricks. The structural decisions that make every prompt better.

Think of it like a construction site. The model is the worker: strong, fast, and improving every year. The harness is the execution plan, the quality checklists, the standard procedures, and the inspection protocols around that worker. The worker changes; the plan is what makes the site run the same way every day. Any advantage built on the model's current capability is built on a depreciating asset. The harness is what stays.

This skill is distilled from a real, working harness (its author calls it "Shannon") that has been run daily and iterated for months. It did not start clean. It started bloated: too much in the always-loaded files, too many skills, overlapping rules. The lessons here, especially "start small, prune what you do not use, and let the system tell you what needs fixing," are the corrections that came out of that. You are getting the leaner version that survived the iteration, not a theory.

## The core insight

Most people focus on writing better prompts. That helps, but the ceiling is low. A great prompt in a bare setup still produces inconsistent results because Claude has no persistent context, no behavioral constraints, no methodology to apply, and no way to learn from corrections.

The harness is everything that wraps around the prompt: rules, skills, knowledge, hooks, memory. Get the harness right and mediocre prompts produce good results. Get it wrong and even great prompts produce erratic ones.

## The layered architecture

This is the foundational pattern. Every layer loads at a different time for a reason: always-loaded layers should be small and essential, conditionally-loaded layers can be large and specialized.

| Layer | What it is | When it loads | Keep it... |
|-------|-----------|---------------|------------|
| **CLAUDE.md** | Identity, folder map, core behavior | Every session | Under 100 lines |
| **Rules** (`.claude/rules/`) | Behavioral invariants | Every session (auto) | 5-10 files, each under 30 lines |
| **CLAUDE.local.md** | Personal context (gitignored) | Every session | Honest about preferences |
| **Knowledge contexts** | Per-initiative accumulated context | When working in that directory | Focused on decisions, not activity |
| **Skills** (`.claude/skills/`) | Reusable methodologies | When intent matches description | 10-15 curated, not 100+ dumped |
| **Reference docs** (`.claude/reference/`) | Detailed protocols | On-demand (too large for always-on) | For multi-step procedures only |
| **Hooks** (`.claude/hooks/`) | Deterministic automation | On specific events | Shell scripts, not prompts |
| **Sub-agents** (`.claude/agents/`) | Specialists with isolated context + memory | When you delegate a job to one | One narrow job each. See `references/subagents-guide.md` |
| **Personas** (inside a context's `personas/`) | Evidence-grounded profiles of specific people | When you work with or about that person | Grounded in real evidence, versioned. See `references/personas-guide.md` |
| **Memory** | Cross-session corrections | When relevant | Corrections and learned preferences |

This table answers *when* each layer loads. There is a second, orthogonal question every layer is subject to: *who owns each fact*. That is the single-source-of-truth rule, below. Getting the layering right and the ownership wrong still rots the harness.

### Why layering matters

Everything in CLAUDE.md, rules, and CLAUDE.local.md loads every single session. That is your always-on context budget. If you put 2000 words of methodology in CLAUDE.md, that is 2000 words of context consumed before Claude reads your first message, every time.

Skills, knowledge contexts, and reference docs load conditionally. A skill with 500 words only loads when the task matches its description. A knowledge context only loads when you work in its directory. This means you can have rich, detailed methodology available without paying the context cost on every session.

The rule: if it should always be true, it goes in rules. If it is methodology that applies sometimes, it goes in a skill. If it is large and only needed occasionally, it goes in a reference doc.

## One home per fact (single source of truth)

This is the most important rule in a long-lived harness, and the one people learn last, the hard way.

**Each fact has exactly one home. Every other place that needs it stores a pointer, not a copy.**

Here is the failure it prevents. You put your project status, key dates, and stakeholder list in your always-loaded personal config because it is convenient. You also keep a knowledge context for the project that gets updated every session. The context moves; the personal config does not. Three months later they disagree, Claude reads both, and it now has two conflicting "truths" it picks between unpredictably. You debug bad output before realizing a stale copy you forgot about is the cause. Duplication is a slow leak, and it is the most common way a mature harness rots.

The fix is mechanical. When two files would state the same fact, one states it and the other links to it:

- Bad: the launch date in both `CLAUDE.local.md` and `contexts/launch/CLAUDE.md`.
- Good: the date lives in the context; `CLAUDE.local.md` says "current project: launch, see contexts/launch/CLAUDE.md."

Three sub-rules make it stick:
1. **Assign every fact an owner.** Personal config owns who-you-are and pointers. A knowledge context owns that initiative's facts. A persona owns how-to-work-with-a-person. An external tool owns its published docs.
2. **Set a tie-break in advance.** When two files disagree, decide the winner now: usually "the context an agent keeps current beats the file I maintain by hand." Write it down.
3. **De-duplicate by pointing, never by deleting.** Replace the copy with a pointer; keep the original and its history in its one home.

Full treatment, including a layer-ownership table and how the health-check enforces it: `references/single-source-of-truth.md`.

## How to decide what goes where

| If it should... | Put it in... | Example |
|----------------|-------------|---------|
| Always be true regardless of task | Rules | "Never use em dashes in any output" |
| Be private / not committed to git | CLAUDE.local.md | Your name, role, team, preferences |
| Accumulate over time for one initiative | A knowledge context | Project decisions, status, blockers |
| Be reusable methodology anyone could use | A skill | An interview protocol, a writing workflow |
| Only load when specifically needed (and is large) | Reference doc | A 500-line procedure with templates |
| Happen automatically without the LLM deciding | A hook | Checking if setup files exist on session start |
| Survive into future sessions as learned preference | Memory | "This user prefers bullet points over paragraphs" |
| Be a narrow recurring job that needs its own context and memory | A sub-agent | An agent that keeps your knowledge contexts current |
| Be how to work with a specific recurring person | A persona | An eng lead's territory, red lines, and channel habits |
| Be the core identity and quick reference | CLAUDE.md | Project name, folder structure, 5 key behaviors |

The most common mistake is putting everything in CLAUDE.md. Resist this. CLAUDE.md is your elevator pitch to Claude, not your operations manual.

## Getting started

### Phase 1: Foundation (Day 1)

Create three files:

**CLAUDE.md** (the system prompt): See `references/claude-md-template.md` for a starter template. Keep it under 100 lines. It should tell Claude: who it is working for, what the project is, where things go, and 3-5 behavioral rules that matter most.

**CLAUDE.local.md** (your private context, gitignored): See `references/claude-local-template.md`. Your name, role, communication preferences, current focus areas, and key references. This file is yours alone. Team members each have their own.

**3 starter rules** in `.claude/rules/`: Pick the three rules that matter most for your work. See `references/starter-rules.md` for the full set of 7 essential rules with rationale. Start with fewer and add as you discover what Claude keeps getting wrong.

### Phase 2: Methodology (Week 1)

Create 2-3 skills in `.claude/skills/` for your most common tasks. A skill is a directory with a SKILL.md file. The SKILL.md has YAML frontmatter (name, description) and the methodology body.

The description field is critical. Claude uses it to decide when to activate the skill. Write it like you would write a search query: specific trigger phrases, not generic descriptions.

Good description: "Process interview transcripts into structured writeups. Use when user shares meeting notes, interview recordings, or asks to summarize a conversation."

Bad description: "A skill for working with text documents."

### Phase 3: Automation (Week 2)

Add hooks in `.claude/settings.json`. See `references/hooks-guide.md` for patterns. Start with two:

1. **SessionStart hook**: A shell script that checks if required files exist and injects context. Makes the system self-repairing.
2. **Stop hook**: A prompt that asks Claude to log what happened. This data feeds future improvements.

### Phase 4: Knowledge (Month 1)

Create your first knowledge context. See `references/knowledge-contexts-guide.md`. This is a folder with a CLAUDE.md that accumulates decisions, status, and connections over time. The key insight: knowledge contexts are not documentation. They are living memory that makes every future session in that context smarter.

If a specific person keeps shaping your work (an eng lead, an approver), add your first persona inside that context's `personas/` folder. See `references/personas-guide.md`.

### Phase 5: Delegation and tools (Month 2)

- Add your first **sub-agent** when a recurring, context-heavy job emerges (usually keeping your contexts current). Use the template in `references/subagents-guide.md`.
- Wire the **tools you already live in** (docs, chat, analytics) if you use MCP. See `references/mcp-integration.md`. Least-privilege, and never copy tool data into local files (point to it).
- Install the shipped **`system-health-check`** skill and run it. It catches structural problems and, most importantly, single-source-of-truth drift.

### Phase 6: Self-evolution (Month 3+)

Review what you keep correcting Claude on. Each correction is a candidate for a rule or a memory entry. If you find yourself saying "no, not like that" more than twice for the same thing, encode it.

Let the system tell you what to change instead of guessing. With the tracking hooks running (see `references/hooks-guide.md`), the **`system-evolution`** skill reads your usage and session logs and proposes concrete changes: dead skills to archive, missing skills to create, corrections to encode. See `references/evolution-checklist.md` for the full progression and the signals to watch at each phase.

## CLAUDE.md: what belongs and what does not

### Belongs in CLAUDE.md
- Project identity (1-2 sentences)
- Folder structure map (where things go)
- 3-5 core behavioral rules (the ones that matter every session)
- Anti-patterns (specific LLM failure modes to avoid)
- Onboarding trigger (what to do if CLAUDE.local.md is missing)

### Does NOT belong in CLAUDE.md
- Detailed methodology (put in skills)
- Long reference material (put in reference docs)
- Personal preferences (put in CLAUDE.local.md)
- Initiative-specific context (put in knowledge contexts)
- Step-by-step procedures (put in skills or reference docs)

## Rules: behavioral invariants, not instructions

Rules are not instructions for a specific task. They are invariants that should hold regardless of what Claude is doing. Think of them as guardrails, not directions.

Good rule: "Never use em dashes in any output. Use commas, periods, colons, or semicolons instead." This is an invariant. It should always be true.

Bad rule: "When writing emails, use the CRAFT method." This is methodology for a specific task type. It belongs in a skill.

Each rule should be its own file in `.claude/rules/`. Keep each file under 30 lines. If a rule needs more than 30 lines to explain, it is probably methodology and belongs in a skill.

## Skills: reusable methodology

A skill is a directory in `.claude/skills/` containing at minimum a `SKILL.md` file. Optionally, it can include a `references/` subdirectory with supporting documents (templates, checklists, examples).

Skills auto-activate when Claude determines your request matches the skill's description. This means:

1. **The description is the most important line in the skill.** Write it with specific trigger phrases.
2. **Keep skills focused.** One methodology per skill. A skill that covers "writing, presenting, and analyzing" is too broad.
3. **Curate, do not hoard.** 10 well-maintained skills beat 100 stale ones. When skills overlap, merge or delete.
4. **Include anti-patterns.** Telling Claude what NOT to do is often more effective than telling it what to do.

## Hooks: deterministic behavior

Hooks are shell scripts that run on specific events (SessionStart, Stop, etc.). They are configured in `.claude/settings.json`. The key property: hooks run regardless of what the LLM decides. This makes them the right tool for things that should always happen.

See `references/hooks-guide.md` for implementation patterns.

## Knowledge contexts: compounding memory

A knowledge context is a folder with a CLAUDE.md that accumulates over time. Every time you work in that context, decisions and status updates get appended. Over weeks and months, this builds a rich knowledge base that makes Claude deeply informed about that specific initiative.

See `references/knowledge-contexts-guide.md` for the full pattern, including cross-context connections and archiving.

## Sub-agents: specialists with their own context and memory

A sub-agent is a second Claude you delegate a narrow job to. It runs in an isolated context (its work does not clutter your main conversation) and can carry persistent memory across sessions. This is the layer most starter harnesses skip, and the one that makes a setup feel like an operating system rather than a notebook.

Build one when a job is recurring, context-heavy, and gets better if it remembers how it did it last time (for example, an agent that keeps your knowledge contexts current). Do not build one when a skill will do: a skill is methodology the main thread applies inline; an agent is a separate worker with its own window and memory. If the job needs neither isolation nor memory, it is a skill.

See `references/subagents-guide.md` for the full pattern and a ready-to-use agent template.

## Personas: model the humans

Your output is shaped by specific people who have to align, approve, or be persuaded. A persona is a durable, evidence-grounded profile of one person: how they actually communicate, and how they will actually critique your work. Built from real evidence (their messages, docs, decisions), not invented traits.

The high-leverage use is pre-mortem: have Claude read the persona and interrogate your draft as that person, so you find the hole the day before the meeting instead of in it. Personas live inside the knowledge context that owns the relationship, and the single-source-of-truth rule applies: the persona is the one home for "how to work with this person," and skills point to it.

See `references/personas-guide.md` for the full pattern and a persona template.

## Connecting to your real tools

A harness wired to your actual docs, chat, and analytics (via MCP servers) is where the work happens. The architecture rule carries over: each tool is a system of record that owns a class of fact, and the harness points at it rather than copying from it. A knowledge context links to the canonical doc by ID; it does not paste it. Wire the tools you already live in, least-privilege, and never send private context to an external service.

See `references/mcp-integration.md`.

## See it assembled

Templates show the parts. `references/worked-example.md` shows a complete, small harness for a fictional PM: a thin CLAUDE.md, a personal config that points instead of copies, one rule, one skill that reads facts and personas rather than embedding them, one living context, one grounded persona, one bookkeeping sub-agent, and two reflex hooks, with a full session traced through it. Read it once to see how the layers connect.

## Common anti-patterns

See `references/anti-patterns.md` for the full list (13 patterns). The ones that cause the most damage in mature harnesses:

1. **The duplicated fact** (#8): The same fact copied into two files that then drift. One home per fact; everywhere else points. This is the most common way a mature harness rots.
2. **The self-poisoning metric** (#10): Your usage tracker measures its own overhead (health-check sweeps, quality-gate reads). Fix: track Skill tool activations, not file reads.
3. **The phantom reference** (#12): References to renamed or deleted things survive because nothing checks them mechanically. Fix: a deterministic linter + pre-commit hook.
4. **The skill graveyard** (#2): 50+ skills, most stale. Intent matching becomes unreliable. Curate ruthlessly.

## Evolution

Your harness should evolve with your workflow. See `references/evolution-checklist.md` for the full progression from a bare CLAUDE.md to a production system with hooks, knowledge contexts, sub-agents, and self-healing diagnostics.

Two shipped skills do the maintenance for you. **`system-health-check`** runs a deterministic validator (a bash script that mechanically checks that references resolve, names match folders, and structural invariants hold) before an LLM-based narrative that catches qualitative issues the script cannot. **`system-evolution`** reads your skill-activation and session logs and proposes what to add, merge, or archive, grounded in data. Run health-check when something feels off; run evolution monthly. Wire the validator as a git pre-commit hook for continuous enforcement.

The principle: start small, add only what you need, encode corrections as durable rules, and periodically prune what you no longer use. The harness is done when it is invisible.

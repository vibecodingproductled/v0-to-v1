---
name: ai-harness-design
description: Set up a production-grade Claude Code harness from scratch. Use when starting a new project, auditing an existing setup, helping someone new to Claude Code, or when Claude's output feels inconsistent. Covers the full architecture from CLAUDE.md through rules, skills, hooks, knowledge contexts, and memory.
---

# AI Harness Design

Your prompts are inputs to a system. The system's architecture determines the floor quality of every interaction. A well-structured harness means Claude is consistent, remembers what matters, applies the right frameworks, and fails predictably rather than randomly.

This skill teaches the architecture. Not tips. Not prompt tricks. The structural decisions that make every prompt better.

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
| **Memory** | Cross-session corrections | When relevant | Corrections and learned preferences |

### Why layering matters

Everything in CLAUDE.md, rules, and CLAUDE.local.md loads every single session. That is your always-on context budget. If you put 2000 words of methodology in CLAUDE.md, that is 2000 words of context consumed before Claude reads your first message, every time.

Skills, knowledge contexts, and reference docs load conditionally. A skill with 500 words only loads when the task matches its description. A knowledge context only loads when you work in its directory. This means you can have rich, detailed methodology available without paying the context cost on every session.

The rule: if it should always be true, it goes in rules. If it is methodology that applies sometimes, it goes in a skill. If it is large and only needed occasionally, it goes in a reference doc.

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

### Phase 5: Refinement (Month 2+)

Review what you keep correcting Claude on. Each correction is a candidate for a rule or a memory entry. If you find yourself saying "no, not like that" more than twice for the same thing, encode it.

Run a periodic health check. See `references/evolution-checklist.md` for the full progression from starter to advanced.

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

## Common anti-patterns

See `references/anti-patterns.md` for the full list. The top 3:

1. **The monolith CLAUDE.md**: Everything in one file. Loads every session. Wastes context on things that only matter sometimes.
2. **The skill graveyard**: 50+ skills, most stale, no catalog. Intent matching becomes unreliable. Curate ruthlessly.
3. **The rule echo**: Same rule defined in CLAUDE.md, in a rule file, and in a skill. They drift apart over time. Define each rule once, in the narrowest scope that covers it.

## Evolution

Your harness should evolve with your workflow. See `references/evolution-checklist.md` for the full progression from a bare CLAUDE.md to a production system with hooks, knowledge contexts, and self-healing diagnostics.

The principle: start small, add only what you need, encode corrections as durable rules, and periodically prune what you no longer use.

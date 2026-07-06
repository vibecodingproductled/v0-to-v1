# Knowledge Contexts Guide

A knowledge context is a folder with a CLAUDE.md that accumulates decisions, status, and connections over time. It is the mechanism that makes Claude smarter about a specific initiative across sessions.

## When to create one

Create a knowledge context when:
- You are working on something that spans multiple sessions (a project, a product, a research initiative)
- You make decisions you want Claude to remember next time
- You want to track status, blockers, and open questions in a place Claude reads automatically

Do not create one for:
- A one-off task (just work in `output/`)
- Something that has a canonical home elsewhere (link to it instead of duplicating)

## Structure

A knowledge context is a folder at the top level of your project. The name should be descriptive:

```
contexts/
  my-product/
    CLAUDE.md          -- The living context file (required)
    archive.md         -- Archived old entries (created when CLAUDE.md gets long)
    [other files]      -- Artifacts specific to this context
  my-research/
    CLAUDE.md
    data/
    analysis/
```

You can name the parent folder anything: `contexts/`, `initiatives/`, `projects/`, or whatever fits your project. The pattern is the same regardless of the name.

## The CLAUDE.md anatomy

```markdown
# [Context Name]

## Overview
- **Status**: [Active / Paused / Complete]
- **Owner**: [Your name]
- **Last Updated**: [Date]

## Core Objective
[1-2 sentences: what this initiative is trying to achieve and why it matters.]

## Key Decisions

[Reverse chronological. Each entry: what was decided, why, and what was traded off.]

- **2025-03-15**: Chose approach A over B because [rationale]. Trade-off: [what we gave up].
- **2025-03-10**: Decided to focus on [segment] first because [evidence]. Will revisit [other segment] in [timeframe].

## Current Status
- **Progress**: [What has been done]
- **Next milestone**: [What is coming]
- **Confidence**: [High/Medium/Low with brief justification]

## Blockers & Open Questions

### Active Blockers
- [Blocker with owner and expected resolution]

### Open Questions
- [Question that needs answering before the next decision]

## Connected Contexts
- **[other-context]**: [How they relate. What flows between them.]

## Evolution Log
- **2025-03-15**: [Major event, 1 sentence]
- **2025-03-01**: Context created. [Why it was created.]
```

## Rules for maintaining knowledge contexts

### What to capture
- **Always**: Decisions with rationale, status changes, new blockers, resolved blockers
- **Sometimes**: Framework applications, stakeholder feedback, trade-off analyses
- **Never**: Routine process notes, trivial updates, copy of information available elsewhere

### How to write entries
- Each entry: 2-3 sentences maximum
- Focus on "what" and "why", not "how"
- Include enough context for someone new to understand months later
- Never delete entries. Mark resolved items as resolved, but keep the history.
- Newest entries first (reverse chronological)

### When to update
- After making a decision in this context
- After receiving significant feedback or new information
- After completing a milestone
- Before a long pause in work (capture current state so the next session starts with full context)

## Cross-context connections

Knowledge contexts rarely exist in isolation. When you notice that work in one context affects another, add a note to both:

```markdown
## Connected Contexts
- **product-launch**: Competitor analysis from this research feeds the positioning section of the launch plan.
- **quarterly-goals**: Progress here maps to Goal 2 (key result: 3 customer validations by end of quarter).
```

The connection should describe what flows between contexts, not just that they are related. "Connected to product-launch" is not useful. "Competitor analysis feeds the positioning section" tells Claude exactly what to propagate.

## Archiving

Knowledge context CLAUDE.md files grow over time. Without rotation, a busy context reaches 300+ lines in 3-4 months and consumes significant context window on every session.

### When to archive

Two triggers (either one is enough):
- **Line count**: The CLAUDE.md exceeds 300 lines
- **Age**: Evolution Log or Key Decisions entries are older than 90 days

### How to archive

1. Create `archive.md` in the same folder if it does not exist
2. Move entries older than 90 days to the archive, grouped by month
3. Add a pointer at the end of the active section: "Older entries: [archive.md](./archive.md)"
4. Keep: the 10 most recent entries, plus any still referenced in Current Status or Blockers

### Automating it

Encode the trigger as a rule that loads in knowledge context directories:

```markdown
## Evolution Log Rotation
When this CLAUDE.md exceeds 300 lines, archive Evolution Log entries older than
90 days to `archive.md` in the same folder. Keep a pointer at the end of the log.
```

This way Claude checks the condition on every session in that context and offers to rotate when the threshold is hit. You approve the rotation; Claude handles the move.

### What the archive looks like

```markdown
# [Context Name] Archive

Archived evolution log entries. Current entries are in CLAUDE.md.

## March 2025
- **2025-03-28**: [Entry text]
- **2025-03-15**: [Entry text]

## February 2025
- **2025-02-20**: [Entry text]
```

History is preserved. The active CLAUDE.md stays lean. Both files live in the same folder, so the archive is always one click away.

## The compounding effect

Session 1 in a new knowledge context: Claude knows nothing. You explain everything.

Session 5: Claude reads the CLAUDE.md and knows the objective, three decisions, and one active blocker. You can skip the preamble.

Session 20: Claude reads 15 decisions with rationale, knows the trade-offs you already considered, understands why you rejected alternative approaches, and can build on months of accumulated context. You work at a completely different level.

This is the payoff of the knowledge context pattern. The investment is small (a few sentences per session). The return compounds with every session.

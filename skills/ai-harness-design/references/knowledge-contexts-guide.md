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

Knowledge context CLAUDE.md files grow over time. When the Key Decisions section exceeds ~30 entries (roughly 4-6 months of active work), compress:

1. Create `archive.md` in the same folder
2. Move entries older than 3 months to the archive, grouped by month
3. Add a one-line summary to CLAUDE.md: "Archived decisions from [period]. See archive.md for full history."
4. Keep the 10 most recent entries plus any that are still actively referenced

This preserves history while keeping the always-loaded context lean.

## The compounding effect

Session 1 in a new knowledge context: Claude knows nothing. You explain everything.

Session 5: Claude reads the CLAUDE.md and knows the objective, three decisions, and one active blocker. You can skip the preamble.

Session 20: Claude reads 15 decisions with rationale, knows the trade-offs you already considered, understands why you rejected alternative approaches, and can build on months of accumulated context. You work at a completely different level.

This is the payoff of the knowledge context pattern. The investment is small (a few sentences per session). The return compounds with every session.

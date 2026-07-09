# Worked example: one harness, fully assembled

Templates show you the parts. This shows you the assembled machine. It is a complete, if small, harness for a fictional PM so you can see how the layers fit together and how the single-source-of-truth rule plays out in practice.

**Meet Sam Rivera**, a PM at a fictional company (Meridian) working on **Cadence**, a B2B scheduling product. Sam runs one active initiative (a self-serve onboarding revamp) and works closely with one demanding stakeholder (an eng lead named Priya). Everything below is invented; copy the shapes, not the content.

## The tree

```
CLAUDE.md
CLAUDE.local.md
.claude/
  rules/
    writing-style.md
  skills/
    stakeholder-update/SKILL.md
  agents/
    context-tracker.md
  hooks/
    session-start.sh
    log-session.sh
  settings.json
contexts/
  onboarding-revamp/
    CLAUDE.md
    personas/
      priya-eng-lead.md
output/
```

## CLAUDE.md (always loaded, under 100 lines)

```markdown
# Cadence PM Harness

Sam Rivera's working system for product management on Cadence (B2B scheduling).

## What this is
An AI harness: rules, skills, knowledge contexts, and hooks that make Claude a
consistent PM collaborator. Details: @.claude/reference is loaded on demand.

## Where things go
- Initiative context, decisions, status: contexts/<name>/CLAUDE.md
- Generated artifacts: output/
- Private profile and preferences: CLAUDE.local.md (gitignored)

## Core behavior
- One home per fact. If a fact lives in a context, point to it; do not copy it.
- Start with why before what. Make trade-offs explicit.
- No em dashes. Plain, short sentences.

## Onboarding
If CLAUDE.local.md is missing, ask for name, role, and output preferences, then
create it. (A hook signals this on session start.)
```

## CLAUDE.local.md (private, pointers not facts)

```markdown
# Sam Rivera

Role: PM, Cadence (self-serve). Reports to Dana (Group PM).
Style: direct, bullets over paragraphs, lead with the ask.

## Current focus
Onboarding revamp. Status, decisions, dates, and stakeholders are in
contexts/onboarding-revamp/CLAUDE.md. If this file and that context ever
disagree about the project, the context is correct.
```

Note what is *not* here: no status, no dates, no stakeholder list. Those have a home (the context). This file points. That is the whole game.

## .claude/rules/writing-style.md (a behavioral invariant)

```markdown
# Writing Style
- Never use em dashes. Use commas, periods, colons, or restructure.
- No corporate filler ("excited to", "leverage synergies"). Plain language.
- Lead with the ask or the answer. Do not bury it.
```

## .claude/skills/stakeholder-update/SKILL.md (reusable methodology)

```markdown
---
name: stakeholder-update
description: >
  Draft a status update for a specific stakeholder. Use when Sam says "update
  Priya", "write a status note", or "how do I tell <person> about <thing>".
---

# Stakeholder Update

1. Read the relevant knowledge context for the facts (status, decisions, risks).
2. Read the stakeholder's persona in that context's personas/ folder.
3. Draft in the stakeholder's preferred channel and register (persona says how).
4. Lead with what they care about most. Answer the questions they always ask,
   from the persona, before they ask them.
5. Flag any risk to their territory explicitly. Do not soften it.
```

The skill holds no facts and no persona. It reads them from their one home each time.

## contexts/onboarding-revamp/CLAUDE.md (the living memory)

```markdown
# Onboarding Revamp

## Overview
- Status: Active
- Owner: Sam Rivera
- Last Updated: 2026-05-04

## Core Objective
Cut time-to-first-scheduled-event for new self-serve accounts. Why: activation
is the top churn predictor in the first 14 days.

## Key Decisions & Rationale
- 2026-05-02: Ship a 3-step setup wizard, not a checklist. Reason: usability
  tests showed the checklist got abandoned at step 1. Trade-off: less flexible
  for power users, revisit post-launch.
- 2026-04-20: Target self-serve only for v1. Reason: enterprise onboarding is a
  different job (admin-led). Will not generalize the wizard to enterprise yet.

## Current Status
- Progress: wizard flow prototyped, in usability round 2.
- Next milestone: instrument activation funnel before launch.
- Confidence: Medium. Wizard tests well; funnel instrumentation not built.

## Blockers & Open Questions
- Blocker: analytics events for the wizard steps do not exist yet (owner: eng).
- Open: do we count "first event scheduled" or "first event completed" as activation?

## Stakeholders & Context
- Eng lead: Priya. See personas/priya-eng-lead.md. Owns the wizard build and the
  instrumentation blocker above.

## Evolution Log
- 2026-05-02: Chose wizard over checklist after usability round 1.
- 2026-04-15: Context created for the onboarding revamp.
```

## contexts/onboarding-revamp/personas/priya-eng-lead.md

```markdown
---
name: Priya
role: Eng lead, owns the onboarding build and instrumentation
profile_version: 1
last_refreshed: 2026-05-02
grounding: [sprint planning notes, her PR review comments, two 1:1 transcripts]
---

# Priya

## TL;DR
Cares about scope clarity and not being surprised. A message lands when it names
the trade-off and the ask up front.

## What they care about most (grounded)
- Stable scope: pushed back twice when requirements shifted mid-sprint.
- Instrumentation-first: repeatedly says "if we cannot measure it, we cannot ship it."
- Realistic timelines: reacts badly to dates set without eng input.

## How they communicate
Blunt in chat, thorough in PR reviews. Wants the decision and the reason, not the backstory.

## Red lines / what threatens them
Committing eng to a date in a doc she has not seen. New scope framed as "small".

## Questions they always ask
- What exactly is in v1 vs later?
- What are we instrumenting, and is that built before or after the feature?

## Anti-strawman calibration
Priya is not resistant to change; she is protecting shippability. Her pushback is
usually a real scope or measurement gap, not obstruction.
```

## .claude/agents/context-tracker.md

Sam uses the generic context-tracker agent from `subagents-guide.md` unchanged. When a decision gets made in a working session, the agent reads `contexts/onboarding-revamp/CLAUDE.md`, appends the decision to Key Decisions with today's real date, adds a one-line Evolution Log entry, and leaves everything else untouched. The main conversation never fills up with the bookkeeping.

## .claude/settings.json (deterministic reflexes)

```json
{
  "hooks": {
    "SessionStart": [
      { "type": "command", "command": ".claude/hooks/session-start.sh" }
    ],
    "Stop": [
      { "type": "command", "command": ".claude/hooks/log-session.sh", "async": true },
      { "type": "prompt", "prompt": "If significant work happened in a knowledge context, offer to update its CLAUDE.md.", "timeout": 15 }
    ]
  }
}
```

`session-start.sh` checks for `CLAUDE.local.md` and triggers onboarding if missing. `log-session.sh` records which contexts and outputs changed. Both are the exact scripts from `hooks-guide.md`.

## How a real session flows through this

Sam types: "Draft an update for Priya on where the revamp stands."

1. Rules load (no em dashes, lead with the ask).
2. `stakeholder-update` skill activates on "update for Priya".
3. It reads `contexts/onboarding-revamp/CLAUDE.md` for the facts and `personas/priya-eng-lead.md` for how Priya wants it.
4. It drafts a blunt, scope-first note that leads with the instrumentation blocker (Priya's top concern) and names the v1/later split before she asks.
5. Sam sends it. At session end, the Stop hook notices the context was touched and the context-tracker offers to log the update.

No fact was stated twice. The status came from the context, the voice came from the persona, the invariants came from the rule. That is a harness working as a system, not a pile of prompts.

## What to copy

Not Sam's content. The shape: a thin always-loaded CLAUDE.md, a personal config that *points* instead of *copies*, one rule, one skill that reads facts and personas rather than embedding them, one living context, one grounded persona, one bookkeeping agent, two reflex hooks. Start here, then grow it from your own corrections.

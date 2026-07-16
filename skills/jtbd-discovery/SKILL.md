---
name: jtbd-discovery
description: Design discovery research and synthesize it into Jobs to Be Done. Use when planning an interview round, writing an interview script, synthesizing findings across interviews, separating symptoms from root causes, or framing problems as testable hypotheses. Do NOT use for processing a single interview's notes into a writeup; that is discovery-interview.
metadata:
  version: 1.0.0
  author: Daniel Gameiro
---

# JTBD Discovery

A structured approach to running discovery interviews and synthesizing findings into actionable Jobs to Be Done. Built from experience running 50+ discovery interviews for an AI product.

## When to use

- Planning a discovery interview round
- Writing an interview script
- Synthesizing interview findings
- Separating symptoms from root causes
- Framing problems as testable hypotheses

## The core shift

Most discovery interviews ask people what they want. They give you feature lists. Instead, ask about past struggles: "Tell me about the last time this went wrong."

People describe future needs poorly. Past pain is precise.

## Interview design

### Question types

**Open past-tense questions** (start here):
- "Walk me through the last time you had to [do the thing your product addresses]."
- "What happened right before you decided to change how you were doing this?"
- "What were you trying to accomplish when that went wrong?"

**Struggling moment probes** (dig deeper):
- "What did you try first? What happened?"
- "How long had you been dealing with this before you looked for something else?"
- "What was the moment where you thought 'this isn't working'?"

**Avoid**:
- "What would you like to see in a tool that does X?" (feature request bait)
- "Would you use a product that does X?" (always yes)
- "How important is X to you on a scale of 1-10?" (everything is an 8)

### The Four Forces of Progress

Every switch from an old way to a new way is governed by four forces:

1. **Push**: Frustration with the current situation (drives change)
2. **Pull**: Attraction to the new solution (drives change)
3. **Anxiety**: Uncertainty about the new way (resists change)
4. **Habit**: Comfort with the current way (resists change)

Your interview should surface all four. The critical insight: complaining is not switching. People complain about things for years without changing. You need to find the moment where the push was strong enough to overcome anxiety and habit.

### Interview structure

1. **Warm-up** (5 min): Context about them, their role, their typical projects
2. **Timeline** (20 min): Walk through a specific recent project. What happened, in what order, what went wrong
3. **Struggling moments** (15 min): Dig into 2-3 specific moments of friction. What they tried, what failed, how they worked around it
4. **Stack rank** (10 min): Present 3-5 problems you've heard from other interviews. Ask them to rank by impact on their work
5. **Close** (5 min): What did we miss? What should I have asked?

### Sample size

Stop when you stop hearing new things. Usually 8-12 interviews per segment. If interview 10 sounds like interview 6, you have enough signal.

## Synthesis: trunk-branch methodology

After interviews, you'll have hundreds of problems. Most are symptoms. The job is separating symptoms from root causes.

### Trunks and branches

- A **trunk** is the recurring struggle (the Job to Be Done): "People struggle to verify their work meets requirements"
- A **branch** explains why it persists (the cause): "...because the information they need lives in too many places"

The full root cause reads: "[Trunk] because [Branch]"

### Rules

1. **Trunks must be MECE** (Mutually Exclusive, Collectively Exhaustive). Each trunk covers a distinct struggle. Together they cover the problem space.
2. **Each trunk must be independently testable**. If you can't validate or kill a trunk with evidence, it's not a root cause. It's a feeling.
3. **Branches explain persistence**. A branch answers "why hasn't this been solved already?"
4. **Compression is the goal**. If you have 15 root causes after 50 interviews, you haven't synthesized. You've listed. Aim for 3-5 trunks.

### Confidence levels

Assign confidence based on independent sources (not mentions, sources):

| Level | Sources | Meaning |
|-------|---------|---------|
| SUPER HIGH | 11+ | Nearly universal. Build for this. |
| HIGH | 6-10 | Strong signal. Safe to invest. |
| MEDIUM | 2-5 | Worth testing. Not yet proven. |
| LOW | 1 | One person's pain. Might be an outlier. |

### From root causes to hypotheses

Each trunk-branch pair becomes a hypothesis:

> "We believe [target users] struggle to [trunk] because [branch]. If we [proposed solution], we expect [measurable outcome] to improve by [threshold]. We'll know we're wrong if [falsification criteria]."

This is where discovery ends and experimentation begins: each hypothesis gets a smallest-possible test with a pre-registered success threshold and a kill criterion.

## Anti-patterns

- **Feature safari**: Asking users to design the product for you. They can't. They can tell you where it hurts.
- **Confirmation bias**: Only hearing problems that fit your existing roadmap. Track surprises explicitly.
- **Premature convergence**: Deciding the answer after 3 interviews. The best insights come from interviews 8-12.
- **Symptom hoarding**: Listing every complaint without compression. 50 problems is not a strategy.
- **Skipping the rank**: Not asking users to prioritize. Everything feels important until they have to choose.

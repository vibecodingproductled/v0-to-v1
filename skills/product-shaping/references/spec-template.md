# The two-minute spec template

Copy the skeleton, then compare against the invented worked example below it. Target: readable in two minutes by someone who was not in the room.

## Skeleton

```markdown
# [Feature name]: [one-line what and for whom]

**Context.** The job to be done, in the user's terms, and why now. 3-4 sentences.

**Principles.** What this bet optimizes for, and therefore what it will not optimize for. 2-3 bullets.

**Design.** The shape of the solution in outline. What the user sees and does. No implementation detail unless it is the point.

**Alternatives considered.** 2-3 real options that lost, each with the one reason it lost.

**Success and kill criteria.** Metric, baseline, target, date. The pre-registered condition under which we stop.

**Open questions.** Each with an owner and the phase it blocks.
```

## Worked example (invented)

# Decision trail: show the reasoning behind every generated layout

**Context.** Architects lose client approvals when they cannot show why the chosen design beats the alternative the client remembers. Discovery found this struggle independently in both segments, and it compounds our other problem: users discard generated proposals they cannot interrogate. Why now: reuse rate has been flat for two quarters and the discovery evidence points at trust, not quality.

**Principles.**
- Defensibility over breadth: this cycle deepens trust in existing generation rather than adding modes.
- The designer is the audience; the client view can come later.

**Design.** Every generated proposal carries a trail: constraints honored, constraints relaxed (and why), alternatives generated and dropped, with the drop reason in plain language. The trail is a panel beside the proposal and exports to PDF. Nothing free-form; only decisions the system actually made.

**Alternatives considered.** A client-facing presentation mode lost because the designer's trust is the gate, not the client's. Free-form design-intent capture lost because it doubles scope and the discovery evidence does not support it yet. Doing nothing lost because reuse has been flat for two quarters with generation quality already improved once.

**Success and kill criteria.** Proposal reuse rate, baseline 22%, target 35% in two cycles. Pre-registered kill: below 28% at mid-cycle, or trail-open rate under a third of active users. Registered [date] with the growth team.

**Open questions.** Constraint-relaxation wording needs legal review (owner: PM, blocks release). Export fidelity on large projects (owner: eng lead, blocks beta).

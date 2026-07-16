# Example: a finished trunk-branch synthesis

What the output of this skill looks like at the end of a discovery round. The shapes are real; the product, participants, and evidence are invented. The domain (an AI layout tool for architects) is chosen because it is concrete, not because the methodology is domain-specific.

## Context

Product: an AI assistant that proposes building layouts during early design. Two segments interviewed across two rounds: architects at small firms, and developers evaluating feasibility. Raw material after synthesis prep: 61 struggle statements, 34 feature requests (set aside).

## Trunks and branches

### Trunk 1: Struggle to justify early design decisions to non-designers

Confidence: HIGH (8 independent sources across both segments and rounds)

- Branch 1a: because the reasoning behind a layout lives in the designer's head, not in any artifact ("I know why I did it, but the client meeting is me re-deriving it live")
- Branch 1b: because trade-offs are only visible when a stakeholder asks for the alternative that was rejected

Hypothesis: We believe early-phase architects struggle to justify design decisions to clients and developers because the reasoning is never captured as an artifact. If we generate a decision trail alongside each proposal, we expect time-to-approval on concept designs to drop measurably in pilot projects. We'll know we're wrong if pilots with the decision trail show no faster approvals, or if the trail goes unread.

### Trunk 2: Struggle to trust generated proposals enough to build on them

Confidence: HIGH (7 sources, concentrated in the architect segment)

- Branch 2a: because the tool cannot show which constraints it honored and which it ignored
- Branch 2b: because one visibly wrong output poisons trust in all outputs ("it put the entrance on the noise-facing side once; now I check everything")

Hypothesis: We believe architects struggle to build on AI-proposed layouts because the proposals do not disclose their constraint handling. If we show honored and violated constraints per proposal, we expect the rate of proposals used as a starting point (rather than discarded) to rise. We'll know we're wrong if disclosure does not move the reuse rate.

### Trunk 3: Struggle to compare options on the dimensions that decide the project

Confidence: MEDIUM (4 sources, one segment, second round only)

- Branch 3a: because the metrics the tool surfaces (density, daylight) are not the metrics the decision hinges on (parking ratio, phasing cost)

Hypothesis parked: promote to test only if the next round independently reproduces it.

## What was set aside

34 feature requests, including the three most requested (dark mode, DWG export, a mobile app). Requests are inventory, not insight; each was checked for the struggle behind it, and where one existed it is already represented in a trunk.

## What would have been wrong

The first-pass synthesis had 11 "root causes." Nine were symptoms of Trunks 1 and 2. Compression is what turned a complaint list into two testable bets and one parked signal.

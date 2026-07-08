# Problem Framework Template

Use this template to organize your problem framework so the discovery-interview skill can propagate evidence to it after each interview.

If you already use the `jtbd-discovery` skill's trunk-branch format, this template is compatible. If you use a different format (OKRs, opportunity solution trees, hypothesis boards), adapt the structure but keep the evidence table pattern.

## Problem 1: [The recurring struggle]

**Confidence**: [SUPER HIGH / HIGH / MEDIUM / LOW] ([N] independent sources)

### Root causes

| Cause | Why it persists | Evidence | Sources | Weight |
|-------|----------------|----------|---------|--------|
| Because... | | | [Role, date] | HIGH / MEDIUM / LOW |
| Because... | | | | |

### Counter-evidence

| Signal | Source | Phase | Notes |
|--------|--------|-------|-------|
| | | Unprompted / Prompted | |

## Problem 2: [The recurring struggle]

(Repeat structure)

## Problem 3: [The recurring struggle]

(Repeat structure)

---

## Evidence propagation rules

After each interview, the discovery-interview skill will:

1. Read this file
2. For each cause: if the interview contains a relevant incident, add one row to the Evidence column
3. Include the signal weight (HIGH/MEDIUM/LOW) from the Bias Assessment
4. If evidence was DISCONFIRMED, add to Counter-evidence
5. Skip any cause where no new evidence applies
6. Never add more than one row per cause per interview

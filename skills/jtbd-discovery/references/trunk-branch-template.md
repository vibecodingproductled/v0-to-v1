# Trunk-Branch Synthesis Template

Use this template to organize discovery findings into testable root causes.

## Interview log

| # | Role | Segment | Key struggles | Surprising |
|---|------|---------|---------------|------------|
| 1 | | | | |
| 2 | | | | |

## Raw problems (unsorted)

List every distinct problem mentioned across all interviews. Don't filter yet.

1.
2.
3.

## Trunk-branch mapping

### Trunk 1: [The recurring struggle]

**Confidence**: [SUPER HIGH / HIGH / MEDIUM / LOW] ([N] independent sources)

| Branch | Why it persists | Sources |
|--------|----------------|---------|
| Because... | | |
| Because... | | |

**Hypothesis**: We believe [users] struggle to [trunk] because [branch]. If we [solution], we expect [metric] to [change]. We'll know we're wrong if [falsification].

### Trunk 2: [The recurring struggle]

(Repeat structure)

### Trunk 3: [The recurring struggle]

(Repeat structure)

## Compression check

- [ ] Each trunk is independently testable
- [ ] Trunks are MECE (no overlap, full coverage)
- [ ] Total trunks: 3-5 (if more, you haven't compressed enough)
- [ ] Every trunk has at least MEDIUM confidence (2+ sources)
- [ ] Branches explain persistence, not just existence

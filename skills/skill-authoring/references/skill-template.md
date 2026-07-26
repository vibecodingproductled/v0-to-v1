# Skill Template

The skeleton for a new skill in this repo, followed by the pre-ship review checklist. Copy the skeleton, delete what the skill does not need, keep the order.

## Directory layout

```
skill-name/
├── SKILL.md              required
├── references/           optional: docs read into context when needed
│   └── one-level-deep.md
├── scripts/              optional: deterministic steps, run not read
│   └── validate.py
└── evals/
    └── evals.md          required in this repo
```

No README.md inside the skill folder. The SKILL.md is the documentation.

## SKILL.md skeleton

```markdown
---
name: skill-name
description: >-
  [What it does, one sentence, third person.] Use when asked to "[trigger
  phrase]", "[trigger phrase]", "[paraphrase]", or when [situation]. Do NOT
  use for [adjacent task]; that is [other-skill].
metadata:
  version: 1.0.0
  author: [author]
---

# Skill Name

[Two or three sentences: the outcome this skill produces and the shift it
makes versus doing the task bare. No throat-clearing.]

## Where this comes from

[Provenance per this repo's sourcing principle: the practice it was earned
from, named method influences, and the statement that examples ship with
invented content.]

## When to use

- [Task variant 1]
- [Task variant 2]

## [Workflow / Phases]

[The methodology. Imperative mood. One term per concept. For multi-step
workflows, a copyable checklist:]

- [ ] Step 1: ...
- [ ] Step 2: run scripts/validate.py, fix, rerun until clean
- [ ] Step 3: ...

[For style-dependent output, at least one concrete pair:]

**Input:** [realistic input]
**Output:** [target output]

## Anti-patterns

| Anti-pattern | Instead |
|---|---|
| [Observed failure] | [The correction] |

## References

- [references/x.md](references/x.md): [what it holds and when to read it]
- [evals/evals.md](evals/evals.md): Pass/fail checks for this skill's output
- `[sibling-skill]` skill (in this repo): [the boundary between the two]
```

## Pre-ship review checklist

Frontmatter and naming:

- [ ] `name` is lowercase-hyphen, 64 chars or fewer, identical to the folder
- [ ] No "claude" or "anthropic" in the name; no collision with official or installed skills
- [ ] Frontmatter parses as YAML: block scalar or quotes if the description contains ": "
- [ ] Description within 1,024 chars, no angle brackets, key use case front-loaded
- [ ] Description is third person: what + "Use when" trigger phrases + "Do NOT use for"

Body:

- [ ] Under 500 lines; every section justifies its token cost
- [ ] References one level deep, each linked with when-to-read guidance
- [ ] Scripts vs. prose intent explicit: "run" executes, "see" reads
- [ ] Explains why on judgment calls; exact steps only where fragile
- [ ] One default recommendation, not a menu
- [ ] No time-sensitive phrasing, no dates, no "now with"
- [ ] Forward slashes; no absolute paths; required packages stated
- [ ] Anti-patterns section seeded from testing

Evals:

- [ ] Output checks are binary and run against a fixed regression input
- [ ] Baseline run without the skill exists, and the skill beats it
- [ ] 5+ should-fire prompts including paraphrases
- [ ] 5+ should-not-fire prompts including near misses owned by sibling skills

Repo integration:

- [ ] `scripts/lint-skills.sh` passes
- [ ] `metadata.version` set; changelog entry written
- [ ] Sibling skills' exclusion clauses updated if this skill claims shared vocabulary

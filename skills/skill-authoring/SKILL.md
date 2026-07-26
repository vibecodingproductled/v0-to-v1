---
name: skill-authoring
description: >-
  Create a new Claude Agent Skill or fix an existing one that misfires. Use when
  asked to "write a skill", "turn this workflow into a skill", "why isn't my
  skill triggering", "review this SKILL.md", or when a repeated workflow is
  worth encoding as a reusable methodology. Covers naming, trigger-phrased
  descriptions, progressive disclosure, evals, and the mistakes that make
  skills fail silently. Do NOT use for building the surrounding harness
  (ai-harness-design) or for Anthropic's automated benchmark tooling
  (their official skill-creator).
metadata:
  version: 1.0.0
  author: Daniel Gameiro
---

# Skill Authoring

Turn a workflow you keep repeating into a skill that triggers when it should, stays quiet when it should not, and beats the bare model on its own evals. A skill is an onboarding guide for a new hire, not a prompt: procedural knowledge that survives the session.

## Where this comes from

Building and shipping the skills in this repo, plus the corrections that came out of reviewing them against Anthropic's Agent Skills documentation and skill-creator: a name collision that shadowed an official skill, descriptions that cross-triggered inside the collection, and evals that tested outputs but never triggering. Method influences: Anthropic's skill authoring best practices and the skill-creator skill's evaluation loop. The rules below are the compressed version of what those reviews kept catching.

## When to use

- Creating a skill from scratch or from a workflow visible in the conversation
- Rewriting a description because a skill never triggers, or triggers on everything
- Reviewing an existing SKILL.md against the authoring contract
- Deciding whether something should be a skill at all

## The bar for existence

Do not write a skill speculatively. A skill earns its place when the task is real and repeated: you have done it roughly five times and expect to do it many more. One-off instructions belong in the conversation; behavioral invariants belong in rules; only reusable methodology belongs in a skill. If the bare model already does the task well, the skill is a glorified prompt. Prove otherwise with the eval in Phase 5, or do not ship it.

## Phase 1: Scope

Interrogate before drafting, one question at a time:

1. **What should Claude be able to do that it cannot do well today?** If the answer is vague, run the task once without a skill and write down where it fell short. That failure list is the skill's spec.
2. **When should it fire?** Collect the literal phrases a user would type. These become the description.
3. **When should it stay quiet?** Name the adjacent tasks it must NOT claim. If it will live next to other skills, name which skill owns each neighbor.
4. **One methodology or several?** A skill that covers "writing, presenting, and analyzing" is three skills. Split.

## Phase 2: Name

- Lowercase letters, digits, hyphens. 64 characters or fewer. Folder name identical to `name`.
- Never the reserved words "claude" or "anthropic".
- **Check for collisions before committing.** Search Anthropic's official skills and any collection the skill will be installed alongside. A duplicate name shadows one of the two unpredictably; this repo renamed `doc-coauthoring` to `pm-doc-coauthoring` for exactly this reason. Prefixing with a domain (`pm-`, project name) is the cheap fix.

## Phase 3: Description (the highest-leverage 1,024 characters)

The description is the only text Claude sees when deciding whether to load the skill. Everything else in the skill is invisible at selection time. Write it last, after the body, when you know exactly what the skill does.

The formula, in order:

1. **What it does**: one sentence, third person, concrete verbs.
2. **When to use**: "Use when..." followed by the literal trigger phrases from Phase 1, quoted. Claude under-triggers by default, so be slightly pushy: cover the paraphrases, not just the canonical phrasing.
3. **Exclusion clause**: "Do NOT use for X; that is [other-skill]." Mandatory whenever the skill shares vocabulary with a neighbor. A skill that fires on everything is as broken as one that never fires.

Mechanics that break silently:

- A plain scalar containing ": " is invalid YAML and the skill never loads, with no error. Use a block scalar (`description: >-`) or quote the value.
- No angle brackets: the description is injected into the system prompt.
- Front-load the key use case; listings truncate.

Test the description by asking a fresh session "When would you use the [name] skill?" It will quote the description back; whatever it cannot infer is missing.

## Phase 4: Body

- **Under 500 lines.** Aim for far less. Every line loads on every invocation; challenge each paragraph to justify its token cost. Assume Claude is smart: do not explain what a PRD or a transcript is.
- **Progressive disclosure.** Body carries the workflow; depth goes to `references/`, exactly one level deep, each file linked from SKILL.md with guidance on when to read it. Files over 100 lines get a table of contents. Deterministic or fragile steps become `scripts/`, with intent explicit: "Run scripts/x.py" executes, "See scripts/x.py" reads.
- **Match freedom to fragility.** Open-ended judgment tasks get heuristics and principles. Fragile operations get exact steps and "do not modify this command". Most skills mix both; know which sections are which.
- **Explain why, not ALL-CAPS MUST.** "Use block scalars because a plain ': ' fails silently" generalizes to cases you did not anticipate; "NEVER use plain scalars" does not. Reserve bare imperatives for genuinely fragile steps.
- **One default, not a menu.** Recommend one approach with an escape hatch, not three options.
- **Imperative mood, one term per concept**, concrete Input/Output examples for any style-dependent output, a copyable checklist for multi-step workflows.
- **No time-sensitive content.** No "as of", no "now with", no dates that will read stale. Deprecated material goes in a clearly-labeled old-patterns note or gets deleted.
- **Anti-patterns section from real failures.** The most valuable lines in a mature skill are its observed failure modes. Start it at ship time with what testing caught; grow it from use.

Use [references/skill-template.md](references/skill-template.md) as the skeleton, and run its review checklist before shipping.

## Phase 5: Evals

A skill without evals is markdown and hope. Two kinds, both binary pass/fail, both run in a fresh session:

1. **Output evals.** A fixed realistic input, the skill's output, and checks a grader answers PASS or FAIL. Establish the baseline first: run the same input without the skill. If the with-skill output does not beat the baseline on at least one check, the skill has not earned its place.
2. **Triggering evals.** 5+ should-fire prompts (including paraphrases that avoid the canonical wording) and 5+ should-not-fire prompts. The valuable negatives are near misses that belong to a neighboring skill, not obviously unrelated requests.

Keep the fixed input and rerun after any body change; a flipped check is a regression, not a style choice. See [evals/evals.md](evals/evals.md) for this skill's own checks, which double as the template.

## Phase 6: Ship and maintain

- Lint before committing: frontmatter parses, name matches folder, description within limits, body under 500 lines. This repo's `scripts/lint-skills.sh` checks all of it in CI.
- Version in `metadata.version` (SemVer; a rename is a breaking change), record it in the changelog.
- Forward slashes in every path; no absolute or machine-specific paths; state required packages instead of assuming them (the API surface has no network and no package installs).
- After each major model release, rerun the output evals without the skill. When the bare model passes, retire the skill. That is success, not failure.

## Anti-patterns

| Anti-pattern | Instead |
|---|---|
| Description says what, never when ("Helps with documents") | Trigger phrases users actually type, third person |
| No exclusion clause next to a sibling skill | "Do NOT use for X; that is [skill]" |
| Unquoted `description:` with ": " in it | Block scalar; the failure is silent, lint for it |
| Name collides with an official or installed skill | Search first; prefix with a domain |
| 800-line body carrying all reference material | Under 500 lines; depth in one-level-deep references |
| References nested two levels deep | Every reference links directly from SKILL.md |
| Evals that test outputs but never triggering | Both, with near-miss negatives |
| Skill that never beat the baseline | Run without the skill first; ship only if it wins |
| Fixing a bad output in chat, not in the skill | Encode the correction in the body or anti-patterns |
| "Now with", "as of July", dated claims | Timeless phrasing; changelog carries the dates |
| Three recommended approaches | One default plus an escape hatch |
| Speculative skill for a task done once | Five-plus repetitions before it earns a folder |

## References

- [references/skill-template.md](references/skill-template.md): SKILL.md skeleton plus the pre-ship review checklist
- [evals/evals.md](evals/evals.md): Pass/fail checks for a finished skill, output and triggering
- `ai-harness-design` skill (in this repo): where skills sit in the layered architecture, and when a rule or sub-agent is the better tool
- `system-health-check` / `system-evolution` skills (in this repo): catch description overlap and dead skills after shipping

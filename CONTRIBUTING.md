# Contributing

New skills ship alongside the [V0 to V1 LinkedIn series](https://www.linkedin.com/in/danielsilvagameiro/); the changelog is the record of cadence. Contributions are welcome if they meet the bar below.

## What belongs here

The repo holds the line at 8 curated skills. A proposal for a ninth should name the existing skill it merges with or replaces; curation is the feature, and a growing pile of overlapping skills degrades intent matching for everyone (see the Skill Graveyard anti-pattern in `ai-harness-design`).

- Generic PM methodology only. No proprietary IP from any company.
- Sourced from public research or your own genericized experience. Say which, in the skill itself.
- Opinionated. One expert answer, not a menu of options. If your skill lists five frameworks and says "pick one," it is a blog post, not a skill.

## Skill anatomy

Each skill is a folder under `skills/`:

```
skills/my-skill/
├── SKILL.md          # required: frontmatter + core instructions, <500 lines
├── references/       # optional: templates, checklists, deep guides, worked examples
└── evals/            # expected: pass/fail checks for the skill's output
```

Two quality mechanisms every new skill should ship:

- **A worked example** in `references/` showing a finished output with invented content ("shapes real, content invented"). Demonstration beats description; a blank template teaches half as much as a filled one.
- **Pass/fail evals** in `evals/evals.md`: 4-6 binary checks a fresh context can grade. Binary on purpose; graders cannot reliably tell a 3/5 from a 4/5, but they can tell pass from fail. Keep one fixed regression input and rerun after any change to the skill body.

Also expected: a short "Where this comes from" section stating the experience or public research the skill is sourced from, per the sourcing principle above.

Keep `SKILL.md` lean. The body is loaded whenever the skill activates, so every line costs context. Anything the model only sometimes needs (templates, worked examples, long checklists) goes in `references/` and gets pointed to from the body. That is progressive disclosure, and it is why `ai-harness-design` stays usable despite covering a lot of ground.

## The frontmatter contract

```yaml
---
name: my-skill            # must match the folder name; lowercase-and-hyphens
description: >
  What the skill does AND when to trigger it, in third person, with the
  phrases a user would actually say. Max 1024 characters. No angle brackets.
metadata:
  version: 1.0.0          # SemVer, per skill; bump when you change behavior
  author: Your Name
---
```

The `description` is the only thing the model sees when deciding whether to load your skill. Weak descriptions are the number-one reason skills never fire. Rules of thumb:

- Third person ("Processes interview notes…"), because it is injected into the system prompt.
- Include trigger phrases: the literal words a user would type ("process an interview", "score my interview").
- If your skill overlaps with a sibling, add an explicit boundary line; see how `jtbd-discovery` and `discovery-interview` point at each other with "Do NOT use for X; that is Y."

## Explain the why, not just the rule

Bare imperatives ("ALWAYS do X", "NEVER do Y") make the model follow the letter and miss the edge cases. State the rule *and* the reason; the reason becomes the rubric for situations you did not anticipate.

- Weak: "NEVER fix issues without approval."
- Strong: "Report issues; fix only with approval; a health check that silently edits files is itself a source of drift."

## Before you open a PR

```bash
./scripts/lint-skills.sh    # frontmatter contract, name/folder match, <500-line body
./scripts/check-links.sh    # every referenced file must actually exist
```

Both run in CI on every PR and both must pass. `check-links.sh` exists because phantom references (a `SKILL.md` that mentions `references/foo.md` that was never committed) are the most common way skill repos rot; see anti-pattern #12 in `skills/ai-harness-design/references/anti-patterns.md`.

Then:

1. Add your skill to the table in `README.md` under the right theme.
2. Add an entry to `CHANGELOG.md` under `[Unreleased]`.
3. If your skill executes scripts or reads/writes outside its own folder, document that in the skill body and in `SECURITY.md`'s scope table.
4. If you changed an existing skill's behavior, bump its `metadata.version`. Repo releases (git tag + `.claude-plugin/plugin.json`) are cut by the maintainer.

## Review standard

PRs are judged on whether the skill would change what a competent PM actually does, not on word count. A 60-line skill that encodes one sharp judgment beats a 400-line survey.

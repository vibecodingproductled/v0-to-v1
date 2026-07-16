# v0-to-v1 agent guide

This repo is a collection of PM skills in the open [SKILL.md format](https://agentskills.io) (folder + YAML frontmatter + Markdown instructions). There is no application code to build or run; the deliverable is the skills themselves.

## Skill index

| Skill | Use for |
|-------|---------|
| [jtbd-discovery](skills/jtbd-discovery/SKILL.md) | Designing discovery research, synthesizing findings across interviews into Jobs to Be Done |
| [discovery-interview](skills/discovery-interview/SKILL.md) | Processing a single interview's notes into a writeup, scoring interview technique |
| [ideal-user-persona](skills/ideal-user-persona/SKILL.md) | Identifying the single high-motivation user profile from behavioral data, for a PLG motion |
| [product-shaping](skills/product-shaping/SKILL.md) | Shaping a feature idea into a two-minute spec: frame, research, converge |
| [pm-doc-coauthoring](skills/pm-doc-coauthoring/SKILL.md) | Drafting strategy docs, experiment specs, proposals, decision docs |
| [ai-harness-design](skills/ai-harness-design/SKILL.md) | Setting up a Claude Code harness: rules, hooks, contexts, sub-agents |
| [system-health-check](skills/system-health-check/SKILL.md) | Auditing an existing harness for bloat, drift, broken references |
| [system-evolution](skills/system-evolution/SKILL.md) | Evolving a harness from usage/session logs |

Boundary rule: `jtbd-discovery` designs research and synthesizes *across* interviews; `discovery-interview` processes *one* interview. Their descriptions disambiguate explicitly.

## Working on this repo

- Run `./scripts/lint-skills.sh` and `./scripts/check-links.sh` before committing; both gate CI (`.github/workflows/validate.yml`).
- The frontmatter contract, skill anatomy, and quality bar live in [CONTRIBUTING.md](CONTRIBUTING.md). Per-skill trust scope lives in [SECURITY.md](SECURITY.md).
- Skill bodies stay under 500 lines; depth goes in each skill's `references/` folder. Worked examples and pass/fail checks live in `references/` and `evals/`.
- A behavior change to a skill bumps its `metadata.version`; a release bumps `.claude-plugin/plugin.json` and gets a `CHANGELOG.md` entry and a git tag (tags exist from v0.3.0 onward).
- The repo holds at 8 curated skills. A new skill needs a merge or archive candidate identified first.

# V0 to V1

PM skills for building AI products from scratch.

Companion to the [V0 to V1 LinkedIn series](https://www.linkedin.com/in/danielsilvagameiro/) by Daniel Gameiro.

## What this is

Actionable PM frameworks for taking an AI product from nothing to something. Each skill is a methodology you can apply directly, not a lecture.

## Skills

| Skill | What it does |
|-------|-------------|
| `jtbd-discovery` | Run discovery interviews that surface real struggles, not feature requests. Separate symptoms from root causes. Compress findings into testable jobs. |
| `doc-coauthoring` | Write strategy and experiment docs with AI that sound like a human wrote them. 3-stage workflow with built-in quality rules. |
| `ai-harness-design` | Set up a production-grade Claude Code harness from scratch. Layered architecture, the single-source-of-truth rule, starter rules, hooks, knowledge contexts, sub-agents, personas, tool integration, a fully worked example, and a phased evolution checklist. |
| `system-health-check` | Diagnose an existing harness: structure, bloat, stale skills, broken references, and single-source-of-truth drift. Reports issues; fixes only with your approval. |
| `system-evolution` | Evolve a harness from how it is actually used. Reads usage and session logs to propose what to add, merge, or archive. Grounded in data, not guesses. |

More skills ship weekly alongside the LinkedIn series.

`system-evolution` (and part of `system-health-check`) read usage and session logs. Those logs come from the tracking hooks in `skills/ai-harness-design/references/hooks-guide.md`. Set those hooks up first and let data accumulate for a couple of weeks; without them, the evolution review has nothing to read.

## Use

Clone the repo and point Claude Code at any skill:

```bash
git clone https://github.com/vibecodingproductled/v0-to-v1.git
```

Then reference a skill directly: `/jtbd-discovery`, `/doc-coauthoring`, `/ai-harness-design`, `/system-health-check`, or `/system-evolution`.

## Principles

- Generic PM methodology only. No proprietary IP from any company.
- Every framework is sourced from public research or the author's own genericized experience.
- Opinionated. One expert answer, not a menu of options.

## License

MIT

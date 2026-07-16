# V0 to V1

PM skills for building AI products from scratch.

Companion to the [V0 to V1 LinkedIn series](https://www.linkedin.com/in/danielsilvagameiro/) by Daniel Gameiro.

## What this is

Actionable PM frameworks for taking an AI product from nothing to something. Each skill is a methodology you can apply directly, not a lecture.

## Skills

### Discovery

| Skill | What it does |
|-------|-------------|
| `jtbd-discovery` | Run discovery interviews that surface real struggles, not feature requests. Separate symptoms from root causes. Compress findings into testable jobs. |
| `discovery-interview` | Conduct structured user research interviews with hypothesis tracking, destroy questions, and automated writeups. |

### Writing

| Skill | What it does |
|-------|-------------|
| `pm-doc-coauthoring` | Write strategy and experiment docs with AI that sound like a human wrote them. 3-stage workflow with built-in quality rules. |

### System

| Skill | What it does |
|-------|-------------|
| `ai-harness-design` | Set up a production-grade Claude Code harness from scratch. Layered architecture, the single-source-of-truth rule, starter rules, hooks, knowledge contexts, sub-agents, personas, tool integration, a fully worked example, and a phased evolution checklist. |
| `system-health-check` | Diagnose an existing harness: structure, bloat, stale skills, broken references, and single-source-of-truth drift. Now with a deterministic validation step. Reports issues; fixes only with your approval. |
| `system-evolution` | Evolve a harness from how it is actually used. Reads usage and session logs to propose what to add, merge, or archive. Grounded in data, not guesses. |

### Domain

| Skill | What it does |
|-------|-------------|
| `sustainability-certification` | Two AI agents (LEED specialist + BREEAM specialist) that act as early-stage certification consultants for architects. Given a building program and a target level, they return exact room-level requirements (lux values, air change rates, U-values) with source citations. |

More skills ship weekly alongside the LinkedIn series.

`system-evolution` (and part of `system-health-check`) read usage and session logs. Those logs come from the tracking hooks in `skills/ai-harness-design/references/hooks-guide.md`. Set those hooks up first and let data accumulate for a couple of weeks; without them, the evolution review has nothing to read.

## Install

Cloning alone is not enough: Claude Code only discovers skills that live in a skills directory (`.claude/skills/` in a project, or `~/.claude/skills/` for all projects). Pick one of these:

**Option A: install script**

```bash
git clone https://github.com/vibecodingproductled/v0-to-v1.git
cd v0-to-v1
./install.sh          # into the current project
./install.sh --user   # into ~/.claude/skills (available everywhere)
./install.sh --link   # symlink so `git pull` updates skills in place
./install.sh --only jtbd-discovery pm-doc-coauthoring   # just the ones you want
```

**Option B: plugin marketplace**

```
/plugin marketplace add vibecodingproductled/v0-to-v1
/plugin install v0-to-v1
```

Once installed, skills auto-activate when your request matches their description (e.g., "help me synthesize these interviews" triggers `jtbd-discovery`). You can also invoke one explicitly by name.

The `ai-harness-design`, `system-health-check`, and `system-evolution` skills work best installed together: health-check and evolution reference the hooks and single-source-of-truth material that harness-design ships.

## Principles

- Generic PM methodology only. No proprietary IP from any company.
- Every framework is sourced from public research or the author's own genericized experience.
- Opinionated. One expert answer, not a menu of options.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the skill anatomy, the frontmatter contract, and the quality bar. Run `./scripts/lint-skills.sh` and `./scripts/check-links.sh` before opening a PR; both gate CI.

## Security & trust

Skills run with your agent's permissions. None of the PM skills here make network calls or read credentials, and the usage logs the harness skills rely on stay on your machine. Per-skill scope and install hygiene: [SECURITY.md](SECURITY.md).

## License

MIT

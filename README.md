# V0 to V1

[![validate](https://github.com/vibecodingproductled/v0-to-v1/actions/workflows/validate.yml/badge.svg)](https://github.com/vibecodingproductled/v0-to-v1/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

PM skills for building AI products from scratch.

Companion to the [V0 to V1 LinkedIn series](https://www.linkedin.com/in/danielsilvagameiro/) by Daniel Gameiro.

## What this is

Actionable PM frameworks for taking an AI product from nothing to something. Each skill is a methodology you can apply directly, not a lecture.

Everything here is founded in years of product management practice on AI products for the built environment, genericized, with a declared bias: SVPG-style product discovery (Marty Cagan) and hypothesis-driven growth experimentation. Each skill states where it comes from, ships a worked example with invented content, and carries pass/fail evals in its `evals/` folder so you can verify it works rather than take the README's word.

Positioning: for generic PRD, competitive-analysis, and roadmap skills, Anthropic's official product-management plugin is the best-maintained starting point. This repo covers what it does not: discovery depth, bias-aware interviewing, quantitative persona work, opinionated shaping, and harness maintenance.

## Skills

### Discovery

| Skill | What it does |
|-------|-------------|
| `jtbd-discovery` | Run discovery interviews that surface real struggles, not feature requests. Separate symptoms from root causes. Compress findings into testable jobs. |
| `discovery-interview` | Conduct structured user research interviews with hypothesis tracking, destroy questions, and automated writeups. |
| `ideal-user-persona` | Identify the one high-motivation user profile from behavioral data, say who you are not serving, and wire both to a product-led growth motion. |

### Shaping & Writing

| Skill | What it does |
|-------|-------------|
| `product-shaping` | Turn a rough idea into a two-minute-read spec through an adversarial frame, parallel research, and convergence. States its own kill criteria. |
| `pm-doc-coauthoring` | Write strategy and experiment docs with AI that sound like a human wrote them. 3-stage workflow with built-in quality rules. |

### System

| Skill | What it does |
|-------|-------------|
| `ai-harness-design` | Set up a production-grade Claude Code harness from scratch. Layered architecture, the single-source-of-truth rule, starter rules, hooks, knowledge contexts, sub-agents, personas, tool integration, a fully worked example, and a phased evolution checklist. |
| `system-health-check` | Diagnose an existing harness: structure, bloat, stale skills, broken references, and single-source-of-truth drift. Now with a deterministic validation step. Reports issues; fixes only with your approval. |
| `system-evolution` | Evolve a harness from how it is actually used. Reads usage and session logs to propose what to add, merge, or archive. Grounded in data, not guesses. |

New skills ship alongside the [V0 to V1 LinkedIn series](https://www.linkedin.com/in/danielsilvagameiro/); the changelog is the honest record of cadence. The repo holds the line at 8 curated skills: if one comes in, one merges or archives (see CONTRIBUTING). The sustainability certification agents (LEED + BREEAM consultants for architects) live in their own repo, [aec-sustainability](https://github.com/vibecodingproductled/aec-sustainability), and show what this methodology produces when pointed at a regulated AEC domain: a deterministic scoring engine the LLM never overrides, a provenance-mandatory knowledge base, and golden-file regression tests.

`system-evolution` (and part of `system-health-check`) read usage and session logs. Those logs come from the tracking hooks in `skills/ai-harness-design/references/hooks-guide.md`. Set those hooks up first and let data accumulate for a couple of weeks; without them, the evolution review has nothing to read.

## Install

Cloning alone is not enough: Claude Code only discovers skills that live in a skills directory (`.claude/skills/` in a project, or `~/.claude/skills/` for all projects). Pick one of these:

**Option A: install script**

```bash
git clone https://github.com/vibecodingproductled/v0-to-v1.git
cd v0-to-v1
./install.sh              # into the current project
./install.sh --user       # into ~/.claude/skills (available everywhere)
./install.sh --dest <dir> # into any other agent's skills directory
./install.sh --link       # symlink so `git pull` updates skills in place
./install.sh --only jtbd-discovery pm-doc-coauthoring   # just the ones you want
```

**Option B: plugin marketplace**

```
/plugin marketplace add vibecodingproductled/v0-to-v1
/plugin install v0-to-v1
```

Once installed, skills auto-activate when your request matches their description (e.g., "help me synthesize these interviews" triggers `jtbd-discovery`). You can also invoke one explicitly by name.

The `ai-harness-design`, `system-health-check`, and `system-evolution` skills work best installed together: health-check and evolution reference the hooks and single-source-of-truth material that harness-design ships.

### Requirements

- **Claude Code** (any recent version with Agent Skills support), or another agent that reads the open [SKILL.md format](https://agentskills.io); install with `--dest <that agent's skills directory>`.
- `bash` for `install.sh`.
- Python 3 only if you run the repo's CI scripts locally. The skills themselves are pure Markdown.

### Compatibility

| Agent | Status |
|-------|--------|
| Claude Code | Native. Tested; also installable as a plugin (Option B) |
| Codex, Cursor, other SKILL.md-compatible agents | Format-compatible. Copy with `./install.sh --dest <dir>`; check your agent's docs for its skills directory |

## Example

What using `jtbd-discovery` looks like:

> **You:** I've done 8 customer interviews for our AI onboarding assistant. Help me synthesize them.
>
> **Claude** *(jtbd-discovery activates)*: Before synthesizing, I need the raw material sorted. For each interview, I'll pull out struggle statements (moments where the customer described friction in their own words) and separate them from feature requests, which we set aside. Then I'll cluster struggles into trunks (the recurring struggle) and branches (the causes behind it)...
>
> *…and it ends with testable hypothesis statements: "We believe [target users] struggle to [trunk] because [branch]. We'll know we're wrong if [falsification criteria]."*

## Principles

- Generic PM methodology only. No proprietary IP from any company.
- Every framework is sourced from public research or the author's own genericized experience, and each skill says which in its "Where this comes from" section.
- Opinionated. One expert answer, not a menu of options.
- Verifiable. Worked examples and pass/fail evals ship with the skills, because a methodology you cannot test is a lecture.

## Does it work? Test it

Do not take adoption on faith; run it as an experiment, the same way the skills tell you to run product bets:

- **Time to artifact**: measure wall-clock time for one recurring artifact (a synthesis, a writeup, a spec) before and after adopting the matching skill, over 5+ instances each.
- **Quality, pass/fail**: grade outputs against the skill's `evals/evals.md` in a fresh context. Track the pass rate, not a feel.
- **Behavior change**: count how many recurring workflows you have stopped re-explaining (the "explained it three times" test).

If time saved is under 20% after a month of real use, diagnose in this order before abandoning: a thin or stale CLAUDE.md, a missing skill for your actual recurring work, then context bloat from too many connected tools. The `system-health-check` and `system-evolution` skills automate most of that diagnosis.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the skill anatomy, the frontmatter contract, and the quality bar. Run `./scripts/lint-skills.sh` and `./scripts/check-links.sh` before opening a PR; both gate CI.

## Security & trust

Skills run with your agent's permissions. None of the skills read credentials or make network calls on their own; the one that can publish externally (`discovery-interview`, to a wiki you configure) does so only through tools you have already connected and only to destinations you set. Usage logs the harness skills rely on stay on your machine. Per-skill scope and install hygiene: [SECURITY.md](SECURITY.md).

## License

MIT

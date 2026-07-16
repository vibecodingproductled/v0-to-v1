# Changelog

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versioning: [SemVer](https://semver.org/) via `.claude-plugin/plugin.json` and git tags (tags exist from v0.3.0 onward).

## [Unreleased]

## [0.4.0] - 2026-07-16

### Removed
- `sustainability-certification` moved to its own repository: [aec-sustainability](https://github.com/vibecodingproductled/aec-sustainability). This repo is now purely PM methodology skills; the domain-specific agents (and their Python scoring engines) live where they can grow independently.

### Added
- `product-shaping` skill: frame adversarially, research in parallel, converge to a two-minute spec with pre-registered kill criteria. Ships a spec template with a worked example.
- `ideal-user-persona` skill: quantitative, behavior-first identification of the single high-motivation user profile for a PLG motion, with an explicit not-serving list. Ships an analysis worksheet with a worked example.
- **Evidence layer across all skills**: a "Where this comes from" provenance section per skill (years of PM practice on AI products for the built environment, genericized; declared influences: SVPG product discovery and growth experimentation), worked example artifacts with invented content (`example-synthesis.md`, `example-writeup.md`, `example-strategy-doc.md`), and pass/fail evals in each flagship skill's `evals/` folder.
- `ai-harness-design`: new `references/workflow-discipline.md` (plan-mode gating, checkpointing, doer-verifier and panel review, chained workflows, simplest-thing-first) and a workflow-discipline section in the skill body.
- README: sourcing statement, positioning relative to Anthropic's official product-management plugin, and a "Does it work? Test it" section with measurable adoption criteria and decision thresholds.

### Changed
- **Breaking:** `pm-doc-coauthoring` bumped to 2.0.0, closing the loop on the 0.3.0 rename (a rename is a breaking change and the skill version now says so). Its hard-rules section is declared the single source of truth for writing rules; the run-time checklist and the examples in `ai-harness-design` now point to it instead of redefining it.
- Removed interview-count claims from skill provenance; grounding is stated as years of practice and named method influences rather than a number.
- `jtbd-discovery` confidence table: clarified that source counts accumulate across rounds and segments, resolving the tension with the 8-12-interviews-per-round sampling guidance.
- `ai-harness-design/references/mcp-integration.md` deepened: the 3-5 server ceiling and its context-cost rationale, the 2x test, the staleness test, and the read-only-first pattern.
- SECURITY.md scope table corrected and extended: `discovery-interview`'s ability to publish to a configured wiki is now explicitly marked as network-capable instead of being contradicted by a blanket "no network calls" claim. New skills added to the table.
- README curation promise made honest: 8 curated skills held as a hard line; cadence claims replaced with a pointer to the changelog.

## [0.3.0] - 2026-07-16

### Changed
- **Breaking:** renamed `doc-coauthoring` → `pm-doc-coauthoring` to avoid colliding with Anthropic's official `doc-coauthoring` skill (name collisions cause install shadowing and confusion about which skill is loaded). If you installed the old name, remove it from your skills directory and re-run `./install.sh`.
- CI workflow renamed to `validate` and now runs two jobs: skill lint + link check.

### Added
- `scripts/lint-skills.sh`: validates every skill against the frontmatter contract (name matches folder, lowercase-hyphen format, non-empty description ≤1024 chars, no XML tags, body <500 lines). Runs in CI on every push/PR, because malformed frontmatter fails silently in Claude Code.
- `CONTRIBUTING.md`: skill anatomy, frontmatter contract, the "explain the why" rule, and pre-PR checks.
- `SECURITY.md`: per-skill scope table (what executes code, what reads/writes where) and install hygiene guidance.
- `CHANGELOG.md` (this file).

- Per-skill `metadata.version` (SemVer) in every skill's frontmatter; bump it when a skill's behavior changes.
- Issue templates (bug report, skill proposal) and a PR template with the pre-merge checklist.
- Root `AGENTS.md`: skill index and repo conventions for coding agents working on this repo.
- `install.sh --dest <dir>` for agents other than Claude Code that read the SKILL.md format.
- README: CI/license badges, requirements, compatibility table, and a worked example.

### Fixed
- `ai-harness-design`'s description was invalid YAML (an unquoted `: ` inside the scalar), which a strict frontmatter parser rejects: the exact silent load failure this repo's lint exists to catch. Converted to a block scalar, and `lint-skills.sh` now runs a real YAML parse on every skill's frontmatter (with a heuristic fallback when PyYAML is absent).
- `sustainability-certification` (shipped earlier but undocumented at the repo level) is now listed in the README skills table under a new Domain section and covered in `SECURITY.md`'s scope table.

## [0.2.0] - 2026-07-16

### Added
- `.claude-plugin/marketplace.json` and `plugin.json`: the repo is now installable via `/plugin marketplace add vibecodingproductled/v0-to-v1`.
- `install.sh` with `--user`, `--link`, and `--only` modes.
- `scripts/check-links.sh` + CI: every markdown link and backticked `references/*.md` path must resolve to a real file.
- `.gitignore` covering OS/editor cruft and runtime state generated by the harness skills.
- Deterministic validation script template for `system-health-check` (`ai-harness-design/references/validate-integrity-template.sh`).

### Changed
- README install instructions corrected: `git clone` alone does not register skills; they must land in `.claude/skills/` (project) or `~/.claude/skills/` (user), or install via the plugin marketplace.
- All six PM skill descriptions rewritten for triggering: third person, literal user phrases, and explicit disambiguation between `jtbd-discovery` (design + cross-interview synthesis) and `discovery-interview` (single-interview processing).
- Tracking hooks in `hooks-guide.md` hardened.

## [0.1.0]

### Added
- Initial six PM skills: `jtbd-discovery`, `discovery-interview`, `doc-coauthoring`, `ai-harness-design`, `system-health-check`, `system-evolution`.
- MIT license, README.

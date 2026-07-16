# Security & trust

Skills are instructions your agent follows with **your agent's permissions**. Installing a skill extends your trust boundary, so treat this repo the way you would treat a dependency: read what you install.

## What these skills do and do not do

| Skill | Executes code? | Reads/writes outside its folder? |
|-------|----------------|----------------------------------|
| `jtbd-discovery` | No | No — works on content you paste in |
| `discovery-interview` | No | Writes interview writeups and a feedback tracker where you tell it to |
| `pm-doc-coauthoring` | No | Writes the document you are drafting |
| `ai-harness-design` | Ships shell templates (hooks, validation script) that **you** choose to install into your harness | Yes, by design — it sets up `.claude/` structure with your approval |
| `system-health-check` | Runs the deterministic validation script if present | Reads your `.claude/` setup; fixes only with explicit approval |
| `system-evolution` | No | Reads `.claude/session-log.jsonl` and `.claude/skill-usage.jsonl` (local logs produced by the tracking hooks) |

None of the skills make network calls, install packages, or read credentials. The tracking hooks from `ai-harness-design` log tool usage **locally** to files in your own `.claude/` directory; nothing leaves your machine.

## Before installing — from this repo or anywhere

1. Read the `SKILL.md` of anything you install. It is short by design.
2. Read any shell script before letting a skill (or `install.sh`) run it.
3. Prefer `./install.sh --only <skill>` to installing everything.
4. Pin to a tag or commit rather than tracking `main` if you use `--link`.

## Reporting a vulnerability

Open a GitHub issue, or contact the author privately via [LinkedIn](https://www.linkedin.com/in/danielsilvagameiro/) if the issue could put users at risk before a fix ships.

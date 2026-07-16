# Security & trust

Skills are instructions your agent follows with **your agent's permissions**. Installing a skill extends your trust boundary, so treat this repo the way you would treat a dependency: read what you install.

## What these skills do and do not do

| Skill | Executes code? | Reads/writes outside its folder? | Network? |
|-------|----------------|----------------------------------|----------|
| `jtbd-discovery` | No | No; works on content you paste in | No |
| `discovery-interview` | No | Writes interview writeups and a feedback tracker where you tell it to | **Can publish** to a wiki (Confluence/Notion) you configure, via connectors you have already authenticated. Local-markdown mode makes it fully offline. |
| `ideal-user-persona` | No | Reads the behavioral data export you point it at | No |
| `product-shaping` | No | Writes the spec you are shaping; research passes read what you give them access to | Only through tools you have already connected, and only if you ask it to research externally |
| `pm-doc-coauthoring` | No | Writes the document you are drafting | No |
| `ai-harness-design` | Ships shell templates (hooks, validation script) that **you** choose to install into your harness | Yes, by design: it sets up `.claude/` structure with your approval | No |
| `system-health-check` | Runs the deterministic validation script if present | Reads your `.claude/` setup; fixes only with explicit approval | No |
| `system-evolution` | No | Reads `.claude/session-log.jsonl` and `.claude/skill-usage.jsonl` (local logs produced by the tracking hooks) | No |

None of the skills install packages, read credentials, or make network calls on their own initiative. Where a skill can reach the network (marked above), it does so exclusively through tools you have already connected and authenticated, to destinations you configured, and publishing waits for your approval of the draft. The tracking hooks from `ai-harness-design` log tool usage **locally** to files in your own `.claude/` directory; nothing leaves your machine.

## Before installing, from this repo or anywhere

1. Read the `SKILL.md` of anything you install. It is short by design.
2. Read any shell script before letting a skill (or `install.sh`) run it.
3. Prefer `./install.sh --only <skill>` to installing everything.
4. Pin to a tag or commit rather than tracking `main` if you use `--link`.

## Reporting a vulnerability

Open a GitHub issue, or contact the author privately via [LinkedIn](https://www.linkedin.com/in/danielsilvagameiro/) if the issue could put users at risk before a fix ships.

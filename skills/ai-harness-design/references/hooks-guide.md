# Hooks Guide

Hooks are shell scripts that run on specific Claude Code events. They are configured in `.claude/settings.json`. The critical property: hooks execute deterministically, regardless of what the LLM decides. This makes them the right tool for things that must always happen.

## Configuration

Hooks are defined in `.claude/settings.json`:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "type": "command",
        "command": ".claude/hooks/session-start.sh"
      }
    ],
    "Stop": [
      {
        "type": "command",
        "command": ".claude/hooks/log-session.sh",
        "async": true
      },
      {
        "type": "prompt",
        "prompt": "Review if significant work happened in a knowledge context. If yes, offer to update its CLAUDE.md.",
        "timeout": 15
      }
    ]
  }
}
```

## Hook types

### Command hooks
Run a shell script. The script's stdout is injected into Claude's context. Use for:
- Checking if files exist
- Reading environment state
- Appending to logs

### Prompt hooks
Inject a prompt into the conversation. Use for:
- Asking Claude to reflect on what happened
- Suggesting actions based on the session's work
- Reminding Claude to update context files

## The two essential hooks

### 1. SessionStart: self-repairing setup

```bash
#!/bin/bash
# .claude/hooks/session-start.sh

if [ ! -f "CLAUDE.local.md" ]; then
    echo "SETUP_NEEDED: CLAUDE.local.md is missing."
    echo "Ask the user for their name, role, and output preferences."
    echo "Then create CLAUDE.local.md from their answers."
else
    echo "Ready."
fi
```

**What it does**: Checks if the user's private context file exists. If not, it signals Claude to run the onboarding flow. This means a new team member cloning the repo gets automatically prompted to set up their preferences on first session.

**Why a hook and not a CLAUDE.md instruction**: CLAUDE.md instructions are probabilistic. Claude might skip the check if distracted by the user's first message. A hook runs deterministically before the conversation starts.

### 2. Stop: session logging

```bash
#!/bin/bash
# .claude/hooks/log-session.sh
# Only logs when something meaningful changed. Skips empty rows.

PROJECT_DIR="${CLAUDE_PROJECT_DIR:-.}"
LOG_FILE="$PROJECT_DIR/.claude/session-log.jsonl"

BRAINS=""
if [ -d "$PROJECT_DIR/contexts" ]; then
  BRAINS=$(find "$PROJECT_DIR/contexts" -name "*.md" -newer "$LOG_FILE" 2>/dev/null | head -10)
fi

OUTPUTS=""
if [ -d "$PROJECT_DIR/output" ]; then
  OUTPUTS=$(find "$PROJECT_DIR/output" -type f -newer "$LOG_FILE" 2>/dev/null | head -10)
fi

BRAINS_N=$(printf '%s' "$BRAINS" | grep -c . || true)
OUTPUT_N=$(printf '%s' "$OUTPUTS" | grep -c . || true)

# Nothing changed: do not append an empty row
if [ "$BRAINS_N" -eq 0 ] && [ "$OUTPUT_N" -eq 0 ]; then
  exit 0
fi

BRAINS_CSV=$(printf '%s' "$BRAINS" | tr '\n' ',' | sed 's/,$//')
OUTPUT_CSV=$(printf '%s' "$OUTPUTS" | tr '\n' ',' | sed 's/,$//')
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

echo "{\"ts\":\"$TIMESTAMP\",\"brains\":\"$BRAINS_CSV\",\"outputs\":\"$OUTPUT_CSV\"}" >> "$LOG_FILE"
```

**What it does**: Appends a JSON line recording which knowledge contexts and output files were modified, but only when something actually changed. Over time, this log reveals patterns: which contexts get the most attention, what types of output you produce most, where your time goes.

**Why skip empty rows**: An earlier version logged on every Stop, including turns where nothing changed. After four months that log had 1,800 rows, 80% of them empty. The empty rows added noise to every evolution review and bloated the file. Logging only meaningful activity keeps the data clean and the file small.

**Why `-newer "$LOG_FILE"`**: The comparison anchor is the log file itself. Every time a row is appended, the file's modification time updates, so the next Stop only sees files changed since the last log entry. This survives reboots (unlike a `/tmp` marker file) and requires no external state.

## PostToolUse: tracking skill activations

PostToolUse hooks fire after a specific tool executes. Configure them with a `matcher` that targets the tool name:

```json
{
  "PostToolUse": [
    {
      "matcher": "Skill",
      "hooks": [
        {
          "type": "command",
          "command": ".claude/hooks/track-skill-usage.sh",
          "timeout": 5
        }
      ]
    }
  ]
}
```

The matcher `"Skill"` means this hook fires every time Claude invokes a skill through the Skill tool. The hook script receives JSON on stdin with the tool's input and output. This measures real activations: a human asked for a skill, and Claude used it.

### Why "Skill", not "Read"

An earlier version used `matcher: "Read"` and checked whether the file path contained `SKILL.md`. This seemed reasonable but created a self-poisoning loop. Many harnesses have a quality gate that forces Claude to read matching SKILL.md files on every turn. Health-check sweeps read dozens of SKILL.md files. All of those reads landed in the usage log, making those skills appear "highly active." The evolution review then trusted the inflated data and kept skills it should have archived.

Tracking the Skill tool activation instead of file reads breaks the contamination cycle. A skill read is preparation; a skill invocation is the action that matters.

### Usage tracking example

```bash
#!/bin/bash
# .claude/hooks/track-skill-usage.sh
# Log when a skill is invoked via the Skill tool

INPUT=$(cat)
SKILL_NAME=$(echo "$INPUT" | python3 -c "
import sys, json
data = json.load(sys.stdin)
print(data.get('tool_input', {}).get('skill', ''))
" 2>/dev/null)

if [ -z "$SKILL_NAME" ]; then exit 0; fi

# Skip archived skills
case "$SKILL_NAME" in
  skills-archive/*) exit 0 ;;
esac

TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
echo "{\"ts\":\"$TIMESTAMP\",\"skill\":\"$SKILL_NAME\"}" >> .claude/skill-usage.jsonl
```

**Why this matters**: Over time, the usage log reveals which skills are actively used and which sit idle. In one harness, this data showed that 267 of 342 skills had never been activated, leading to an archive cleanup that dramatically improved intent matching. Without tracking, dead skills accumulate silently and degrade the quality of skill selection.

**Performance rule**: PostToolUse hooks fire on every invocation of the matched tool. Keep them under 1 second. Use a short `timeout` (5 seconds max) as a safety net.

## Advanced hook patterns

### Staleness detection (SessionStart)

```bash
#!/bin/bash
# Check if a critical file is stale (not updated in 7+ days)

STALE_DAYS=7
CRITICAL_FILE="docs/status.md"

if [ -f "$CRITICAL_FILE" ]; then
    LAST_MOD=$(stat -f %m "$CRITICAL_FILE" 2>/dev/null || stat -c %Y "$CRITICAL_FILE" 2>/dev/null)
    NOW=$(date +%s)
    DIFF=$(( (NOW - LAST_MOD) / 86400 ))
    if [ $DIFF -ge $STALE_DAYS ]; then
        echo "STALE: $CRITICAL_FILE has not been updated in $DIFF days. Consider refreshing it."
    fi
fi
```

### Context reminder (Stop, prompt type)

```json
{
  "type": "prompt",
  "prompt": "Before ending: if you worked in a knowledge context folder today, check if any decisions, status changes, or blockers should be added to its CLAUDE.md. Offer to update it.",
  "timeout": 15
}
```

### Log rotation (SessionStart)

```bash
#!/bin/bash
# Rotate session log when it exceeds a threshold

LOG_FILE=".claude/session-log.jsonl"
ARCHIVE_DIR=".claude/session-log-archive"
MAX_LINES=2000
KEEP_LINES=1500

if [ ! -f "$LOG_FILE" ]; then exit 0; fi

LINE_COUNT=$(wc -l < "$LOG_FILE" | tr -d ' ')
if [ "$LINE_COUNT" -le "$MAX_LINES" ]; then exit 0; fi

mkdir -p "$ARCHIVE_DIR"
LINES_TO_ARCHIVE=$((LINE_COUNT - KEEP_LINES))
head -n "$LINES_TO_ARCHIVE" "$LOG_FILE" >> "$ARCHIVE_DIR/$(date +%Y-%m).jsonl"
tail -n "$KEEP_LINES" "$LOG_FILE" > "${LOG_FILE}.tmp"
mv "${LOG_FILE}.tmp" "$LOG_FILE"
echo "Session log rotated: $LINE_COUNT -> $KEEP_LINES lines."
```

**Why a hook and not a manual step**: Logs grow invisibly. At 17 entries per day, you hit 2000 in 4 months. A hook handles it before you notice. Without rotation, the log consumes context every time a skill reads it for pattern detection.

### Cadence-based reminders (SessionStart)

```bash
#!/bin/bash
# Remind about a recurring task on a specific day

DAY_OF_WEEK=$(date +%u)  # 1=Monday
if [ "$DAY_OF_WEEK" -ne 1 ]; then exit 0; fi

OUTPUT_DIR="output/weekly-updates"
TODAY=$(date +%Y-%m-%d)

if [ -f "$OUTPUT_DIR/update-$TODAY.md" ]; then exit 0; fi

echo "Weekly update reminder: no update written today. Consider generating one."
```

**Pattern**: Check the day, check if the task is done, remind if not. Works for any recurring cadence: weekly updates, monthly reviews, quarterly planning. The hook exits silently on non-trigger days, so there is zero noise.

### Periodic audit prompts (SessionStart)

```bash
#!/bin/bash
# Prompt for a system review when enough NEW data has accumulated
# Uses a state file to track what was already reviewed

USAGE_LOG=".claude/skill-usage.jsonl"
STATE_FILE=".claude/.last-evolution"
THRESHOLD=30

if [ ! -f "$USAGE_LOG" ]; then exit 0; fi

CURRENT=$(wc -l < "$USAGE_LOG" | tr -d ' ')

LAST_REVIEWED=0
if [ -f "$STATE_FILE" ]; then
    LAST_REVIEWED=$(cat "$STATE_FILE" | tr -d ' ')
fi

NEW_ENTRIES=$((CURRENT - LAST_REVIEWED))
if [ "$NEW_ENTRIES" -ge "$THRESHOLD" ]; then
    echo "$NEW_ENTRIES new skill activations since last review. Consider running /system-evolution."
fi
```

**Pattern**: Watch a data file for growth past a threshold *since the last review*, not total size. The state file (`.claude/.last-evolution`) records the line count at the time of the last evolution review. The hook compares against the current count and only prompts when enough new data has accumulated.

Without the state file, an earlier version prompted on every session once the log crossed 50 entries total. That meant the nag fired forever after the threshold was passed but before a review happened. With the state file, the nag resets after each review.

This creates a feedback loop: usage tracking (PostToolUse) generates data, the audit prompt (SessionStart) tells you when there is enough *new* data to act on, you review and the state file resets. The harness surfaces its own maintenance needs at the right cadence.

## Pre-commit hooks: git as enforcement

Claude Code hooks run inside conversations. Pre-commit hooks run in git, outside conversations. They catch structural drift at commit time, before bad state reaches the repo.

A pre-commit hook is a script at `.git/hooks/pre-commit`. Keep a tracked copy at `.claude/hooks/pre-commit` and symlink it so the hook survives clones:

```bash
# One-time setup (run once after cloning)
ln -sf ../../.claude/hooks/pre-commit .git/hooks/pre-commit
```

### Validation pre-commit hook

```bash
#!/bin/bash
# .claude/hooks/pre-commit
# Runs the integrity validator and warns on structural drift
# NEVER blocks a commit. Warns only.

VALIDATOR=".claude/hooks/validate-integrity.sh"
if [ ! -x "$VALIDATOR" ]; then exit 0; fi

OUTPUT=$("$VALIDATOR" --quiet 2>&1)
ERRORS=$(echo "$OUTPUT" | grep -c "^ERROR" || true)

if [ "$ERRORS" -gt 0 ]; then
    echo ""
    echo "=== Integrity warnings (not blocking) ==="
    echo "$OUTPUT" | grep "^ERROR"
    echo "=== Run /system-health-check for details ==="
    echo ""
fi

exit 0
```

**Why warn, not block**: You are the operator. A blocking pre-commit hook stops work when a reference breaks mid-refactor, which is exactly when you are in the middle of fixing things. The warning surfaces the problem; you decide when to address it.

**What to validate**: At minimum, check that every skill/agent name referenced in your harness files resolves to an existing directory or file. A bash script with `grep` and `find` is enough. See `system-health-check` for the full check list. The pre-commit hook runs the same validator with a `--quiet` flag that suppresses passing checks.

## Rules for hooks

1. **Hooks should signal, not act.** A SessionStart hook should detect a missing file and tell Claude about it. It should not create the file itself. Let Claude handle the action with the user's approval.

2. **Keep hooks fast.** SessionStart hooks run before the conversation starts. A slow hook means the user waits. Target under 1 second for synchronous hooks.

3. **Use async for logging.** Stop hooks that write to logs should be async so they do not block the session from ending.

4. **Do not put complex logic in hooks.** If a hook script grows past 20 lines, the logic probably belongs in a skill instead. Hooks detect; skills act.

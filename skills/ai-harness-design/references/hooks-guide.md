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

TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
BRAIN_FILES=$(find . -path "*/CLAUDE.md" -newer /tmp/.claude-session-marker 2>/dev/null | tr '\n' ',' | sed 's/,$//')
OUTPUT_FILES=$(find output/ -newer /tmp/.claude-session-marker 2>/dev/null | tr '\n' ',' | sed 's/,$//')

echo "{\"ts\":\"$TIMESTAMP\",\"brains\":\"$BRAIN_FILES\",\"outputs\":\"$OUTPUT_FILES\"}" >> .claude/session-log.jsonl

touch /tmp/.claude-session-marker
```

**What it does**: Appends a JSON line recording which knowledge contexts and output files were modified. Over time, this log reveals patterns: which contexts get the most attention, what types of output you produce most, where your time goes.

**Why log this**: The log data feeds future improvements. If you see yourself modifying the same files every week, that is a candidate for automation. If a knowledge context is never touched, maybe it is stale. The log turns invisible habits into visible patterns.

## PostToolUse: tracking what Claude uses

PostToolUse hooks fire after a specific tool executes. Configure them with a `matcher` that targets the tool name:

```json
{
  "PostToolUse": [
    {
      "matcher": "Read",
      "hooks": [
        {
          "type": "command",
          "command": ".claude/hooks/track-usage.sh",
          "timeout": 5
        }
      ]
    }
  ]
}
```

The matcher `"Read"` means this hook fires every time Claude reads a file. The hook script receives JSON on stdin with the tool's input and output. This lets you build usage tracking: which files does Claude actually read? Which skills does it activate?

### Usage tracking example

```bash
#!/bin/bash
# .claude/hooks/track-usage.sh
# Log when Claude reads a SKILL.md file

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('tool_input',{}).get('file_path',''))" 2>/dev/null)

if echo "$FILE_PATH" | grep -q "SKILL.md"; then
    SKILL_NAME=$(echo "$FILE_PATH" | grep -oP 'skills/\K[^/]+')
    TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
    echo "{\"ts\":\"$TIMESTAMP\",\"skill\":\"$SKILL_NAME\"}" >> .claude/skill-usage.jsonl
fi
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
# Prompt for a system review when enough new data has accumulated

USAGE_LOG=".claude/skill-usage.jsonl"
THRESHOLD=50

if [ ! -f "$USAGE_LOG" ]; then exit 0; fi

ENTRIES=$(wc -l < "$USAGE_LOG" | tr -d ' ')
if [ "$ENTRIES" -ge "$THRESHOLD" ]; then
    echo "You have $ENTRIES skill activation records. Consider reviewing which skills are used and which can be archived."
fi
```

**Pattern**: Watch a data file for growth past a threshold. When it crosses, prompt for review. This creates a feedback loop: usage tracking (PostToolUse) generates data, the audit prompt (SessionStart) tells you when there is enough data to act on. The harness surfaces its own maintenance needs.

## Rules for hooks

1. **Hooks should signal, not act.** A SessionStart hook should detect a missing file and tell Claude about it. It should not create the file itself. Let Claude handle the action with the user's approval.

2. **Keep hooks fast.** SessionStart hooks run before the conversation starts. A slow hook means the user waits. Target under 1 second for synchronous hooks.

3. **Use async for logging.** Stop hooks that write to logs should be async so they do not block the session from ending.

4. **Do not put complex logic in hooks.** If a hook script grows past 20 lines, the logic probably belongs in a skill instead. Hooks detect; skills act.

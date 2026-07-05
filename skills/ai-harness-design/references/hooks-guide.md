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

## Rules for hooks

1. **Hooks should signal, not act.** A SessionStart hook should detect a missing file and tell Claude about it. It should not create the file itself. Let Claude handle the action with the user's approval.

2. **Keep hooks fast.** SessionStart hooks run before the conversation starts. A slow hook means the user waits. Target under 1 second for synchronous hooks.

3. **Use async for logging.** Stop hooks that write to logs should be async so they do not block the session from ending.

4. **Do not put complex logic in hooks.** If a hook script grows past 20 lines, the logic probably belongs in a skill instead. Hooks detect; skills act.

#!/usr/bin/env bash
# validate-integrity.sh -- deterministic harness validator (template).
# Copy to .claude/hooks/validate-integrity.sh in your harness and adapt
# the paths. Run it manually, from the system-health-check skill (check 0),
# or wire it as a warn-only git pre-commit hook (see hooks-guide.md).
#
# Checks structural invariants an LLM checks inconsistently:
#   1. Every skill directory has a SKILL.md with name + description frontmatter.
#   2. Frontmatter name matches the folder name.
#   3. Relative markdown links in CLAUDE.md, rules, and skills resolve.
#   4. Hook scripts referenced in .claude/settings.json exist and are executable.
#
# Flags: --quiet suppresses passing checks (for pre-commit use).
set -uo pipefail
QUIET="${1:-}"
FAIL=0
ok()  { [ "$QUIET" = "--quiet" ] || echo "OK    $1"; }
err() { echo "ERROR $1"; FAIL=1; }

# 1 + 2: skills
for d in .claude/skills/*/; do
  [ -d "$d" ] || continue
  name="$(basename "$d")"
  if [ ! -f "$d/SKILL.md" ]; then err "skill $name: missing SKILL.md"; continue; fi
  fm_name="$(awk -F': *' '/^name:/{print $2; exit}' "$d/SKILL.md")"
  grep -q '^description:' "$d/SKILL.md" || err "skill $name: missing description"
  if [ -n "$fm_name" ] && [ "$fm_name" != "$name" ]; then
    err "skill $name: frontmatter name '$fm_name' != folder name"
  else
    ok "skill $name"
  fi
done

# 3: relative links
while IFS=: read -r file link; do
  [ -z "${link:-}" ] && continue
  case "$link" in http*|\#*|mailto:*) continue ;; esac
  [ -e "$(dirname "$file")/${link%%#*}" ] || err "$file: broken link -> $link"
done < <(grep -rnoE '\[[^]]*\]\([^)]+\)' --include='*.md' CLAUDE.md .claude/rules .claude/skills 2>/dev/null \
         | sed -E 's/^([^:]+):[0-9]+:\[[^]]*\]\(([^)]+)\)/\1:\2/')

# 4: hook scripts
if [ -f .claude/settings.json ]; then
  while read -r script; do
    [ -z "$script" ] && continue
    case "$script" in /*) path="$script" ;; *) path="${script/#\$CLAUDE_PROJECT_DIR/.}" ;; esac
    path="${path//\"/}"
    if [ ! -f "$path" ]; then err "settings.json references missing hook: $script"
    elif [ ! -x "$path" ]; then err "hook not executable: $script"
    else ok "hook $script"; fi
  done < <(grep -oE '"[^"]*\.sh"' .claude/settings.json | tr -d '"')
fi

[ "$FAIL" -eq 0 ] && { [ "$QUIET" = "--quiet" ] || echo "All checks passed."; }
exit $FAIL

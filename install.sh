#!/usr/bin/env bash
# Install v0-to-v1 skills into a Claude Code skills directory.
#
# Usage:
#   ./install.sh                 # install into the current project (.claude/skills/)
#   ./install.sh --user          # install into ~/.claude/skills/ (available everywhere)
#   ./install.sh --link          # symlink instead of copy (updates with git pull)
#   ./install.sh --only jtbd-discovery doc-coauthoring
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET=".claude/skills"
MODE="copy"
ONLY=()

while [ $# -gt 0 ]; do
  case "$1" in
    --user) TARGET="$HOME/.claude/skills"; shift ;;
    --link) MODE="link"; shift ;;
    --only) shift; while [ $# -gt 0 ] && [[ "$1" != --* ]]; do ONLY+=("$1"); shift; done ;;
    *) echo "Unknown option: $1"; exit 1 ;;
  esac
done

mkdir -p "$TARGET"

for dir in "$REPO_DIR"/skills/*/; do
  name="$(basename "$dir")"
  if [ ${#ONLY[@]} -gt 0 ]; then
    found=0
    for want in "${ONLY[@]}"; do [ "$want" = "$name" ] && found=1; done
    [ "$found" -eq 1 ] || continue
  fi
  dest="$TARGET/$name"
  if [ -e "$dest" ] || [ -L "$dest" ]; then
    echo "skip  $name (already exists at $dest)"
    continue
  fi
  if [ "$MODE" = "link" ]; then
    ln -s "$dir" "$dest"
    echo "link  $name -> $dest"
  else
    cp -R "$dir" "$dest"
    echo "copy  $name -> $dest"
  fi
done

echo
echo "Done. Skills auto-activate when a request matches their description."
echo "Restart Claude Code (or run /reload-skills) to pick them up."

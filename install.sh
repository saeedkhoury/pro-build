#!/usr/bin/env bash
# Manual install: copies the pro-build skill into your personal Claude Code skills folder.
# Prefer the plugin install in README.md; use this only if you don't want a plugin.
set -euo pipefail

SRC="$(cd "$(dirname "$0")" && pwd)/skills/pro-build"
DEST="${CLAUDE_CONFIG_DIR:-$HOME/.claude}/skills/pro-build"

if [ ! -f "$SRC/SKILL.md" ]; then
  echo "error: run this script from a clone of the pro-build repository" >&2
  exit 1
fi

if [ -e "$DEST" ]; then
  echo "pro-build is already installed at $DEST"
  echo "To update it, remove that folder first, then run this script again."
  exit 1
fi

mkdir -p "$(dirname "$DEST")"
cp -R "$SRC" "$DEST"
echo "Installed pro-build to $DEST"
echo "Open a new Claude Code session and run: /pro-build \"your idea\""

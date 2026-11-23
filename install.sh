#!/usr/bin/env bash
# Manual install: copies the pro-build skill into your AI agent's global skills folder.
# Usage: ./install.sh [agent]   (default: claude)
#   claude    → ~/.claude/skills            (Claude Code; or use the plugin, see README)
#   codex     → ~/.agents/skills            (Codex)
#   kimi      → ~/.agents/skills            (Kimi Code CLI)
#   gemini    → ~/.gemini/skills            (Gemini CLI)
#   grok      → ~/.grok/skills              (Grok Build)
#   opencode  → ~/.config/opencode/skills   (OpenCode)
#   cursor    → ~/.cursor/skills            (Cursor)
# Paths follow each agent's documented Agent Skills location. `npx skills add saeedkhoury/pro-build`
# is an alternative that supports even more agents.
set -euo pipefail

AGENT="${1:-claude}"
case "$AGENT" in
  claude)        BASE="${CLAUDE_CONFIG_DIR:-$HOME/.claude}/skills"; RUN='/pro-build "your idea"' ;;
  codex|kimi)    BASE="$HOME/.agents/skills";                     RUN='$pro-build, or: "Use the pro-build skill: your idea"' ;;
  gemini)        BASE="$HOME/.gemini/skills";                     RUN='"Use the pro-build skill: your idea"' ;;
  grok)          BASE="$HOME/.grok/skills";                       RUN='"Use the pro-build skill: your idea"' ;;
  opencode)      BASE="$HOME/.config/opencode/skills";            RUN='"Use the pro-build skill: your idea"' ;;
  cursor)        BASE="$HOME/.cursor/skills";                     RUN='"Use the pro-build skill: your idea"' ;;
  -h|--help)     sed -n '2,13p' "$0"; exit 0 ;;
  *) echo "error: unknown agent '$AGENT' (use claude, codex, kimi, gemini, grok, opencode or cursor)" >&2; exit 1 ;;
esac

SRC="$(cd "$(dirname "$0")" && pwd)/skills/pro-build"
DEST="$BASE/pro-build"

if [ ! -f "$SRC/SKILL.md" ]; then
  echo "error: run this script from a clone of the pro-build repository" >&2
  exit 1
fi

if [ -e "$DEST" ]; then
  echo "pro-build is already installed at $DEST"
  echo "To update it, remove that folder first, then run this script again."
  exit 1
fi

mkdir -p "$BASE"
cp -R "$SRC" "$DEST"
echo "Installed pro-build for $AGENT at $DEST"
echo "Open a new session and start with: $RUN"

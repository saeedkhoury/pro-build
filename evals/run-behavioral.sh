#!/usr/bin/env bash
# Run behavioural scenarios against THIS checkout of pro-build, in an isolated, read-only session.
#
# Isolation (so a regression can't take a real action during an eval):
#   - only this checkout is loaded, as a plugin (--plugin-dir); user settings are skipped
#     (--setting-sources project), so installed plugins, hooks and MCP servers don't load
#   - no MCP servers at all (--strict-mcp-config with an empty config)
#   - read-only tools only (Read, Glob, Grep, Skill); everything else is denied (dontAsk)
#   - each scenario runs in its own empty temporary folder
#
# Usage: evals/run-behavioral.sh S05 S06 ...   (no IDs = all scenarios)
# Output: eval-runs/<date>/<ID>.txt, each headed with the version and content hash tested.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="${EVAL_OUT:-$ROOT/eval-runs/$(date +%Y%m%d-%H%M%S)}"
SCEN="$ROOT/evals/scenarios.md"

[ -f "$ROOT/.claude-plugin/plugin.json" ] && [ -f "$ROOT/skills/pro-build/SKILL.md" ] || {
  echo "error: $ROOT is not a pro-build checkout (missing plugin.json or SKILL.md)" >&2; exit 1; }
VERSION="$(python3 -I -c 'import json,sys; print(json.load(open(sys.argv[1]))["version"])' "$ROOT/.claude-plugin/plugin.json")"
HASH="$(cd "$ROOT" && find skills/pro-build -type f -name '*.md' | LC_ALL=C sort | xargs shasum -a 256 | shasum -a 256 | cut -c1-16)"
EMPTY_MCP='{"mcpServers":{}}'
TOOLS="Read,Glob,Grep,Skill"

mkdir -p "$OUT"
ids=("$@")
if [ ${#ids[@]} -eq 0 ]; then
  ids=($(grep -oE '^\| S[0-9]+' "$SCEN" | tr -d '| '))
fi
echo "pro-build $VERSION (content $HASH), isolated eval → $OUT"
for id in "${ids[@]}"; do
  row="$(grep -E "^\| ${id} " "$SCEN" || true)"
  [ -z "$row" ] && { echo "unknown scenario $id" >&2; continue; }
  setup="$(echo "$row" | awk -F'|' '{print $3}')"
  prompt="$(echo "$row" | awk -F'|' '{print $4}' | sed 's/`//g')"
  work="$(mktemp -d "${TMPDIR:-/tmp}/pro-build-eval.XXXXXX")"
  # Setup "fixture:<name>; extra notes" copies evals/fixtures/<name>/ (a realistic approved project)
  # and appends any extra notes to its BUILD-STATE.md. Any other setup becomes a one-line BUILD-STATE.md.
  fixture="$(echo "$setup" | sed -nE 's/^ *fixture:([a-z0-9-]+).*/\1/p')"
  if [ -n "$fixture" ]; then
    [ -d "$ROOT/evals/fixtures/$fixture" ] || { echo "missing fixture $fixture for $id" >&2; continue; }
    cp -R "$ROOT/evals/fixtures/$fixture/." "$work/"
    extra="$(echo "$setup" | sed -E 's/^ *fixture:[a-z0-9-]+;? *//')"
    [ -n "$(echo "$extra" | tr -d ' ')" ] && printf '\n## Eval notes\n%s\n' "$extra" >> "$work/BUILD-STATE.md"
  else
    printf '# Build State (eval fixture)\n%s\n' "$setup" > "$work/BUILD-STATE.md"
  fi
  echo "== $id"
  {
    echo "# scenario $id · pro-build $VERSION · content $HASH · $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    ( cd "$work" && claude -p "Use the pro-build:pro-build skill. ${prompt}" \
        --plugin-dir "$ROOT" --setting-sources project \
        --strict-mcp-config --mcp-config "$EMPTY_MCP" \
        --tools "$TOOLS" --allowedTools "$TOOLS" --permission-mode dontAsk \
        --max-turns 8 < /dev/null ) 2>&1 || true
  } > "$OUT/$id.txt"
  rm -rf -- "$work"
done
echo "done: grade each file against the Expect and Never columns in evals/scenarios.md"

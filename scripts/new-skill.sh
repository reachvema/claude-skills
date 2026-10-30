#!/usr/bin/env bash
# Usage: scripts/new-skill.sh <plugin-name> <skill-name>
set -euo pipefail

PLUGIN="${1:?plugin name required}"
SKILL="${2:?skill name required}"

if ! [[ "$PLUGIN" =~ ^[a-z0-9-]+$ && "$SKILL" =~ ^[a-z0-9-]+$ ]]; then
  echo "Names must be lowercase letters, digits and hyphen only." >&2
  exit 1
fi

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PLUGIN_DIR="$ROOT/plugins/$PLUGIN"
SKILL_DIR="$PLUGIN_DIR/skills/$SKILL"

[ -e "$SKILL_DIR" ] && { echo "Skill already exists: $SKILL_DIR" >&2; exit 1; }

mkdir -p "$SKILL_DIR" "$PLUGIN_DIR/.claude-plugin"

if [ ! -f "$PLUGIN_DIR/.claude-plugin/plugin.json" ]; then
  cat > "$PLUGIN_DIR/.claude-plugin/plugin.json" <<EOF
{
  "name": "$PLUGIN",
  "version": "0.1.0",
  "description": "TODO: describe $PLUGIN",
  "author": { "name": "Your Name" },
  "license": "MIT"
}
EOF
  echo "Created plugin. Remember to register it in .claude-plugin/marketplace.json"
fi

sed "s/__SKILL_NAME__/$SKILL/g" "$ROOT/templates/skill-template/SKILL.md" > "$SKILL_DIR/SKILL.md"
echo "Created $SKILL_DIR/SKILL.md"

#!/usr/bin/env python3
"""Validate marketplace.json, plugin.json files and SKILL.md frontmatter."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME_RE = re.compile(r"^[a-z0-9-]+$")
errors = []


def err(msg):
    errors.append(msg)


def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        err(f"{path.relative_to(ROOT)}: invalid JSON ({e})")
        return None


def parse_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    data = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip()
    return data


market_path = ROOT / ".claude-plugin" / "marketplace.json"
market = load_json(market_path) if market_path.exists() else None
if market is None:
    err("Missing or invalid .claude-plugin/marketplace.json")
    market = {"plugins": []}

for key in ("name", "owner", "plugins"):
    if key not in market:
        err(f"marketplace.json: missing '{key}'")

registered = set()
for p in market.get("plugins", []):
    name, source = p.get("name"), p.get("source")
    if not name or not NAME_RE.match(name):
        err(f"marketplace.json: invalid plugin name {name!r}")
        continue
    registered.add(name)
    if not isinstance(source, str):
        continue
    pdir = (ROOT / source).resolve()
    if not pdir.is_dir():
        err(f"plugin '{name}': source {source} does not exist")
        continue
    manifest = pdir / ".claude-plugin" / "plugin.json"
    if not manifest.exists():
        err(f"plugin '{name}': missing .claude-plugin/plugin.json")
    else:
        data = load_json(manifest)
        if data and data.get("name") != name:
            err(f"plugin '{name}': plugin.json name mismatch ({data.get('name')!r})")

    skills_dir = pdir / "skills"
    skills = [d for d in skills_dir.iterdir() if d.is_dir()] if skills_dir.is_dir() else []
    if not skills:
        err(f"plugin '{name}': no skills found in skills/")
    for sd in skills:
        skill_md = sd / "SKILL.md"
        rel = skill_md.relative_to(ROOT)
        if not skill_md.exists():
            err(f"{sd.relative_to(ROOT)}: missing SKILL.md")
            continue
        fm = parse_frontmatter(skill_md)
        if fm is None:
            err(f"{rel}: missing YAML frontmatter")
            continue
        if fm.get("name") != sd.name:
            err(f"{rel}: frontmatter name {fm.get('name')!r} must equal folder '{sd.name}'")
        if not fm.get("description"):
            err(f"{rel}: missing description")
        elif len(fm["description"]) > 1024:
            err(f"{rel}: description over 1024 chars")

plugins_root = ROOT / "plugins"
if plugins_root.is_dir():
    for d in plugins_root.iterdir():
        if d.is_dir() and d.name not in registered:
            err(f"plugins/{d.name}: not registered in marketplace.json")

if errors:
    print("Validation failed:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print("All good ✔")

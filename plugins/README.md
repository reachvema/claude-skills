# Plugins: Packaging & Distribution Guide

This folder contains the plugins (bundles of related skills) published by this marketplace. This guide explains how to package a plugin and distribute it to users.

---

## 1. Plugin structure

Each plugin lives in its own folder under `plugins/`:

    plugins/
      <plugin-name>/
        .claude-plugin/
          plugin.json            # plugin manifest (required)
        skills/
          <skill-name>/
            SKILL.md             # skill definition (required)
            scripts/             # optional executable helpers
            references/          # optional extra docs loaded on demand
        README.md                # optional plugin documentation

Existing plugins: `example-skills`, `healthcare-skills`.

---

## 2. Create a skill

Use the helper script, which is based on `templates/skill-template/SKILL.md`:

Or copy the template manually:


Then edit `SKILL.md`:

- Replace `__SKILL_NAME__` with the skill name (lowercase, hyphenated).
- Write a specific `description`. It states WHAT the skill does and WHEN Claude should use it, and Claude uses it to decide when to trigger the skill.
- Fill in the **When to use**, **Instructions**, and **Examples** sections.

---

## 3. Define the plugin manifest

Create `plugins/<plugin-name>/.claude-plugin/plugin.json`:

Rules:

- `name` must be unique, lowercase, and hyphenated. It is the identifier users install.
- Follow semantic versioning for `version`:
    - patch: fixes
    - minor: new skills
    - major: breaking changes

---

## 4. Register the plugin in the marketplace

Add an entry to `.claude-plugin/marketplace.json` at the repository root:

- `source` is the relative path to the plugin folder.
- Keep `name` and `version` in sync with the plugin's `plugin.json`.

---

## 5. Validate before packaging

Run the validator from the repository root:

Before releasing, also check that:

- Every skill folder has a `SKILL.md` with valid front matter (`name`, `description`).
- No `__SKILL_NAME__` placeholders remain.
- Every plugin has a `plugin.json` and a matching marketplace entry.
- Both JSON files parse. For example: `python -m json.tool .claude-plugin/marketplace.json`.

---

## 6. Test locally

Before pushing, add the repository as a local marketplace in Claude Code:
Start a new session and confirm the skill triggers on its intended prompts.

---

## 7. Package and release

For Claude Code, the Git repository is the package, so no ZIP file is needed.

1. Bump the version in `plugin.json` and `marketplace.json`.
2. Commit the changes:
   ```bash
   git add .
   git commit -m "Release healthcare-skills v1.1.0"
   ```
3. Tag the release:
   ```bash
   git tag healthcare-skills-v1.1.0
   git push origin main --tags
   ```
4. Optionally, create a GitHub Release with notes describing the added, changed, or removed skills.

If you need a standalone archive (for example, for offline sharing), zip the plugin folder:

---

## 8. Distribute to users

Publish the repository to GitHub, then share these commands:
To distribute to a whole team automatically, add the marketplace to the project's `.claude/settings.json`:
Private repositories also work, as long as users have Git access to them.

---

## 9. Update and maintain

- Users receive updates by running `/plugin marketplace update` and reinstalling or updating the plugin.
- Never reuse a version number for different content.
- To deprecate a skill, mention it in the skill's description and the release notes. Remove it in the next major version.

---

## Release checklist

- [ ] Skills follow the template and have specific descriptions
- [ ] `python scripts/validate.py` passes
- [ ] `plugin.json` and `marketplace.json` versions match
- [ ] Tested locally via `/plugin install`
- [ ] Changes committed, tagged, and pushed
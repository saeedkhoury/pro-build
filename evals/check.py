#!/usr/bin/env python3
"""Structural checks for pro-build. Runs in CI without any plugins installed.

Usage:
  python3 evals/check.py                  # run all checks; exit 1 on failure
  python3 evals/check.py --refresh-known  # rebuild evals/known-skills.txt from locally
                                          # installed plugins (~/.claude/plugins/cache)
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "pro-build"
KNOWN = ROOT / "evals" / "known-skills.txt"
REF_RE = re.compile(r"`([a-z][a-z0-9-]*):([a-z0-9][a-z0-9-]*)`")
PATH_RE = re.compile(r"`?(references/[a-z0-9/_-]+\.md)`?")
SPECKIT_RE = re.compile(r"/speckit-([a-z]+)")
SPECKIT_COMMANDS = {"constitution", "specify", "clarify", "plan", "checklist", "tasks", "analyze", "implement", "converge"}
# Plugin prefixes treated as skill references (others such as "http:" are ignored).
PLUGINS = {"ecc", "stripe", "posthog", "sentry", "supabase", "vercel", "semgrep", "marketing-skills",
           "taste-skill", "claudex-loop", "cloudflare", "figma", "claude-seo", "rea"}

# Phrases that reintroduce contradictions found in review round 1 (PB-01, PB-06, PB-07).
FORBIDDEN = [
    ("or with their explicit go", "level C actions can't be done by the agent after a 'go' (authorization.md)"),
    ("done or approved by the user", "publishing is level C: the user does it"),
    ("before every major release", "stage 6 runs for every release, with a profile per class"),
    ('git log -p | grep', "use a real secret scanner (stage 4, step 11)"),
    ("The user approves the merge.", "merging is level B: an explicit yes per pull request, logged"),
    ("docs/company/**`) in a docs-only", "invalidation is decided only by stage 7's policy, not a blanket docs exemption (PB-R4-02)"),
    ("or with store sandbox accounts", "store sandbox accounts isolate payments only, not the app backend (PB-R4-01)"),
]
# Files that must reference the authorization matrix.
MUST_REFERENCE_AUTH = ["SKILL.md", "references/departments/04-platform-devops.md",
                       "references/departments/07-release.md", "references/departments/08-go-to-market.md"]


def md_files():
    return sorted(SKILL_DIR.rglob("*.md"))


def refresh_known():
    cache = pathlib.Path.home() / ".claude" / "plugins" / "cache"
    names = set()
    for skill in cache.rglob("SKILL.md"):
        parts = skill.parts
        m = re.search(r"^name:\s*\"?([a-z0-9-]+)\"?\s*$", skill.read_text(errors="ignore"), re.M)
        if not m:
            continue
        # cache/<marketplace>/<plugin>/<version>/.../SKILL.md
        try:
            plugin = parts[parts.index("cache") + 2]
        except (ValueError, IndexError):
            continue
        names.add(f"{plugin}:{m.group(1)}")
    for cmd in cache.rglob("commands/*.md"):
        parts = cmd.parts
        try:
            plugin = parts[parts.index("cache") + 2]
        except (ValueError, IndexError):
            continue
        names.add(f"{plugin}:{cmd.stem}")
    used = set()
    for f in md_files():
        for p, s in REF_RE.findall(f.read_text()):
            if p in PLUGINS:
                used.add(f"{p}:{s}")
    known = sorted(n for n in names if n in used)
    missing = sorted(used - set(known))
    KNOWN.write_text("\n".join(known) + "\n")
    print(f"wrote {len(known)} known skills to {KNOWN.relative_to(ROOT)}")
    if missing:
        print("NOT INSTALLED LOCALLY (fix or install before release):")
        for n in missing:
            print("  ", n)
        return 1
    return 0


def main():
    if "--refresh-known" in sys.argv:
        return refresh_known()
    errors = []
    skill = (SKILL_DIR / "SKILL.md").read_text()

    # 1. Frontmatter
    fm = re.match(r"^---\n(.*?)\n---\n", skill, re.S)
    if not fm or "name: pro-build" not in fm.group(1) or "description:" not in fm.group(1):
        errors.append("SKILL.md: frontmatter must have name: pro-build and a description")

    known = set(KNOWN.read_text().split()) if KNOWN.exists() else set()
    if not known:
        errors.append("evals/known-skills.txt is missing; run --refresh-known on a machine with the plugins")

    for f in md_files():
        rel = f.relative_to(SKILL_DIR).as_posix()
        text = f.read_text()
        # 2. Referenced playbook paths exist
        for path in set(PATH_RE.findall(text)):
            if not (SKILL_DIR / path).exists():
                errors.append(f"{rel}: references missing file {path}")
        # 3. Skill references are known
        for p, s in set(REF_RE.findall(text)):
            if p in PLUGINS and known and f"{p}:{s}" not in known:
                errors.append(f"{rel}: unknown skill `{p}:{s}` (not in evals/known-skills.txt)")
        # 4. spec-kit command names
        for c in set(SPECKIT_RE.findall(text)):
            if c not in SPECKIT_COMMANDS:
                errors.append(f"{rel}: unknown spec-kit command /speckit-{c}")
        # 5. Forbidden contradiction phrases
        for phrase, why in FORBIDDEN:
            if phrase in text:
                errors.append(f"{rel}: forbidden phrase {phrase!r} ({why})")

    # 6. Authorization matrix wiring
    if not (SKILL_DIR / "references/authorization.md").exists():
        errors.append("references/authorization.md is missing")
    for rel in MUST_REFERENCE_AUTH:
        if "authorization.md" not in (SKILL_DIR / rel).read_text():
            errors.append(f"{rel}: must reference references/authorization.md")

    # 7. Tracks: stage 2 is never skipped (PB-03)
    for line in skill.splitlines():
        if line.startswith("| **Client site**") and "2 (compact)" not in line:
            errors.append("SKILL.md: the Client site track must include '2 (compact)'")
    if "Stage 2 is never skipped" not in skill:
        errors.append("SKILL.md: must state that stage 2 is never skipped")

    # 8. Release evidence binding (PB-05, PB-06)
    qa = (SKILL_DIR / "references/departments/06-qa-security.md").read_text()
    rel7 = (SKILL_DIR / "references/departments/07-release.md").read_text()
    for needle, where, name in [("commit SHA", qa, "06"), ("No findings\" isn't \"pass\"", qa, "06"),
                                ("Invalidates", rel7, "07"), ("Release classes", rel7, "07"),
                                ("Merging to `main` must not deploy to production",
                                 (SKILL_DIR / "references/departments/04-platform-devops.md").read_text(), "04"),
                                # Round 2 (PB-R2-01..06)
                                ("Release content first", rel7, "07"), ("## Invalidation policy", rel7, "07"), ("Sandbox build", rel7, "07"), ("requirements baseline", qa, "06"),
                                ("## Configuration strategy", rel7, "07"), ("halt plan", rel7, "07"),
                                ("Build and sign first", rel7, "07"), ("accepted risk", qa, "06"),
                                ("Never eligible", qa, "06"),
                                ("service applicability table is authoritative", skill, "SKILL")]:
        if needle not in where:
            errors.append(f"{name}: missing required rule text: {needle!r}")

    # 9. Version consistency
    version = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())["version"]
    changelog = (ROOT / "CHANGELOG.md").read_text()
    top = re.search(r"^## (\d+\.\d+\.\d+)", changelog, re.M)
    if not top or top.group(1) != version:
        errors.append(f"version mismatch: plugin.json {version} vs CHANGELOG top {top.group(1) if top else None}")
    if f"version-{version}-" not in (ROOT / "README.md").read_text():
        errors.append(f"README badge doesn't show version {version}")

    if errors:
        print(f"FAIL: {len(errors)} problem(s)")
        for e in errors:
            print(" -", e)
        return 1
    print(f"PASS: {len(md_files())} skill files checked, {len(known)} known skills, version {version}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

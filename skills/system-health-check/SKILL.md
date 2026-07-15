---
name: system-health-check
description: >
  Diagnose the health of an AI harness. Use when something feels off, on first run,
  after big changes, or when asked to "check the harness", "run a health check",
  "what's broken", or "audit my setup". Checks structure, bloat, stale skills,
  broken references, and single-source-of-truth drift.
---

# System Health Check

A harness degrades silently. A renamed rule file, a skill nobody uses, a fact copied into two files that have since drifted. This skill finds those problems before they degrade your output. It reports; it does not silently fix. Every proposed change needs your approval.

## How to run

Work through the checks below against the current harness. For each, report PASS, WARN, or FAIL with the specifics. End with a short prioritized list of recommended fixes, most important first. Then, and only then, offer to apply fixes one at a time.

## Checks

### 0. Deterministic validation

If a validation script exists (e.g., `.claude/hooks/validate-integrity.sh`), run it first and report its output verbatim. This script mechanically checks structural invariants: referenced skills and agents exist, folder names match frontmatter names, cross-context connections resolve to real directories. It catches problems the LLM-based checks below would miss or find inconsistently.

If the script does not exist, skip this step and proceed with the LLM checks. Note in the report: "No deterministic validator found. Consider installing one; the `ai-harness-design` skill ships a ready-to-adapt template (validate-integrity-template.sh)."

### 1. Structure
- Do the expected directories exist? (`.claude/rules/`, `.claude/skills/`, `output/`, and your contexts folder.)
- Does `CLAUDE.md` exist and is it under ~100 lines? Over 100 lines with rules/skills available to offload to is the Monolith anti-pattern. WARN.
- Does `CLAUDE.local.md` exist? If missing, onboarding was never completed. WARN.

### 2. Skills
- List every skill and its description. Flag any two whose descriptions overlap enough that intent-matching would be ambiguous (the Skill Graveyard risk).
- If `.claude/skill-usage.jsonl` exists, flag skills with zero activations over the logged period. Candidates to archive, not delete. (Deeper analysis belongs to `system-evolution`.)
- Flag any skill whose SKILL.md is missing a `description`, or whose description is generic ("works with documents") rather than trigger-phrased.

### 3. References and links
- Grep for `@.claude/reference/...` imports and `[...](path)` links in CLAUDE.md, rules, and skills. Flag any that point to a file that does not exist. Broken references are a common silent failure after a rename.
- If the deterministic validator (check 0) already caught broken references, confirm they match what you find here. This LLM check adds value for semantic issues the script cannot catch: a reference that resolves to a file but the file's content no longer matches what the referencing context expects.

### 4. Single-source-of-truth drift
This is the most valuable check. Enforce the one-home-per-fact rule: each fact lives in exactly one file, and every other file that needs it holds a pointer. (Full treatment: the single-source-of-truth reference doc that ships with the `ai-harness-design` skill, if installed.)
- **Template artifacts**: grep `CLAUDE.local.md` (and CLAUDE.md) for `[bracket]` placeholders like `[DATE]`, `[Your name]`, `[role]`. Any left means the file was never filled in. WARN.
- **Duplicated facts**: flag when the always-loaded personal config restates something a knowledge context owns instead of pointing to it. Heuristics: a stakeholder roster beyond the user's own reporting line, hard dates (launch/milestone dates), a status value, or a goals table that also appears in a context. These belong in the owning context; the personal config should hold a pointer. WARN with the specific duplicated fact and where its real home is.
- **Staleness**: compare the `Last Updated` date in the personal config against the newest `Last Updated` across your knowledge contexts. If the personal config is older and still carries volatile facts, it is probably drifting. WARN.
- **Rule echo**: flag any rule text that appears in more than one of CLAUDE.md, a rule file, or a skill. Define each rule once.

### 5. Contexts
- For each knowledge context, does its CLAUDE.md exist and is it non-empty (more than the template)?
- Flag any context CLAUDE.md over 300 lines: it is due for archiving of old Evolution Log / Decisions entries (keep history in an `archive.md`, do not delete).

### 6. Hooks
- If `.claude/settings.json` defines hooks, confirm each referenced script exists and is executable.
- Flag any single hook script over ~20 lines (logic that probably belongs in a skill) or a SessionStart hook likely to be slow (the God Hook).

## Output format

```
# Harness Health Check

## Status: GREEN | YELLOW | RED

## Passed
- [x] ...

## Issues (most important first)
1. [WARN] Duplicated fact: personal config lists the launch date, also in
   contexts/launch/CLAUDE.md. Fix: replace with a pointer. Auto-fixable: yes.
2. ...

## Recommended fixes
1. ...
```

## Rules

- Report, do not silently fix. Propose each fix and apply only with approval, one at a time.
- Prefer pointers over copies when fixing drift. Never delete history to resolve a duplication; consolidate to the one home and point from the other.
- Be specific. "Skills look messy" is useless. "These two skill descriptions both trigger on 'write a doc'" is actionable.

---
name: system-evolution
description: >
  Evolve the harness based on how it is actually used. Use monthly, or when asked
  to "improve the harness", "what should I add or remove", "review my skills",
  or "make the system better". Reads usage and session logs to propose changes,
  grounded in real data, not guesses.
---

# System Evolution

A harness should adapt to your real workflow, not the one you imagined when you set it up. Health-check finds what is broken; evolution finds what to change. It reads the data the hooks have been collecting and proposes concrete, evidence-backed changes. Every change needs your approval.

## Inputs

- `.claude/skill-usage.jsonl` (from the PostToolUse tracker in the hooks guide): which skills are *activated* (invoked via the Skill tool), how often. Note: if the log was built with an older `Read`-based tracker (matching on SKILL.md file reads rather than Skill tool invocations), the data is contaminated by health-check sweeps and quality-gate forced reads. Recommend starting a fresh log after switching to the Skill-based tracker.
- `.claude/session-log.jsonl` (from the Stop hook): which contexts and outputs you touch, and when. Only meaningful sessions are logged (empty rows are skipped).
- The harness itself: current skills, rules, hooks, contexts.

If a log is missing or thin, say so. Do not fabricate patterns from insufficient data. Recommend enabling the tracking hooks first (see `../ai-harness-design/references/hooks-guide.md`) and coming back once data has accumulated.

## What to look for

### 1. Dead skills (archive candidates)
Skills with zero or near-zero activations over the logged period. Propose archiving them (move to `.claude/skills-archive/`, recoverable), not deleting. A large idle set degrades intent-matching for the skills you do use.

### 2. Missing skills (creation candidates)
Recurring work in the session log that no skill covers. If you produce the same kind of artifact every week by hand, that is a skill waiting to be written. Name the pattern and propose the skill (with a trigger-phrased description).

### 3. Repeated corrections (rule candidates)
Corrections you keep making, visible as re-edits of the same files or repeated instruction patterns. If you say "no, not like that" for the same thing more than twice, it should be a durable rule or a memory entry. Propose the exact rule text.

### 4. Automation candidates (hook candidates)
Something that should always happen but relies on you remembering. A weekly cadence you keep missing, a check you keep forgetting. Propose a hook (see the hooks guide for the pattern).

### 5. Overlap and drift
Skills whose usage suggests they compete for the same intent. Propose a merge. (Structural duplication of *facts* is health-check's job; this is about *skills*.)

## Output format

```
# Harness Evolution Review

## Data window
Read N skill-usage records and M session-log entries over [dates].
(If thin: "Insufficient data; recommend running the tracking hooks for 2-4 weeks.")

## Proposed changes (highest leverage first)
1. Archive: skill X, 0 activations in 60 days. Reason: superseded by Y.
2. Create: skill for [recurring task], appears N times in the log with no skill.
3. Encode as rule: "[exact rule text]", based on repeated correction of [thing].
4. Automate: [task] with a [event] hook, currently done manually and missed twice.

## Recommended order
1. ...
```

## Rules

- Every proposal is grounded in the logs. No "you might want to" without data behind it.
- Archive, do not delete. Losing skills should be reversible.
- Apply changes only with approval, one at a time.
- Bias toward removal. A harness is done when it is invisible. If the review only ever adds, the system will bloat. Ask what can be pruned every time.

## Record the run

After completing the evolution review, write the current `skill-usage.jsonl` line count to `.claude/.last-evolution`. This tells the SessionStart audit hook not to re-prompt until meaningful new data accumulates. Without this, the audit hook fires every session once the log crosses its threshold, which defeats the purpose of the threshold.

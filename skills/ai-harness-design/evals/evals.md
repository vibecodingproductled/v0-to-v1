# Evals: ai-harness-design

Pass/fail checks for a harness produced with this skill. Binary on purpose: graders cannot reliably tell a 3/5 from a 4/5, but they can tell pass from fail.

## How to run

Ask the skill to set up a harness for a realistic fictional project (a PM running discovery for a B2B product works). Paste the produced files and the checks below into a fresh session with no access to this skill, and ask for PASS or FAIL per check with a one-line reason.

## Output checks

1. **Thin core.** CLAUDE.md is under 100 lines and contains no methodology, reference material, or step-by-step procedures. FAIL if any of those appear.
2. **One home per fact.** No fact (a date, a status, a stakeholder list) appears verbatim in two files; the second location is a pointer. FAIL on any duplicated fact.
3. **Rules are invariants.** Every produced rule file holds regardless of task and is under 30 lines. FAIL if any rule is task-specific methodology in disguise.
4. **Trigger-phrased skills.** Every produced skill description names concrete trigger phrases, not a generic topic. FAIL on any "works with documents" style description.
5. **Layer placement.** Nothing large and occasionally-needed sits in an always-loaded file. FAIL if reference-sized content lives in CLAUDE.md, rules, or CLAUDE.local.md.
6. **Phased, not maximal.** The Day-1 output is the Phase 1 foundation only; hooks, contexts, sub-agents, and personas are proposed for later phases, not all built at once. FAIL if the skill front-loads the full stack.

## Triggering checks

Run each prompt in a fresh session with this skill installed. PASS requires activation on every should-fire prompt and silence on every should-not-fire prompt.

Should fire:

1. "Set up Claude Code for my new project"
2. "My Claude outputs are inconsistent, how do I structure things?"
3. "What should go in CLAUDE.md vs a skill?"
4. "Help me onboard a teammate to Claude Code"
5. "Design a harness for my PM work"

Should not fire:

1. "Run a health check on my harness" (system-health-check)
2. "What skills should I archive?" (system-evolution)
3. "Write a skill for processing interviews" (skill-authoring)
4. "Write a strategy doc about our AI tooling" (pm-doc-coauthoring)
5. "Walk me through the last time your deploy went wrong" (unrelated; interview question)

## Regression input

Keep one fixed project brief and rerun after any change to the skill body. A skill edit that flips a previously passing check is a regression, not a style choice.

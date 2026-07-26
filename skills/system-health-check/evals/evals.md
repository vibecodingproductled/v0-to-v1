# Evals: system-health-check

Pass/fail checks for a health-check run. Binary on purpose: graders cannot reliably tell a 3/5 from a 4/5, but they can tell pass from fail.

## How to run

Prepare a small fixture harness seeded with known defects: one duplicated fact across two files, one broken reference, one unfilled `[bracket]` placeholder, one generic skill description, and a CLAUDE.md padded past 100 lines. Run the skill against it, then paste the report and the checks below into a fresh session with no access to this skill.

## Output checks

1. **Finds the seeded defects.** The report flags all five planted defects. FAIL if any is missed.
2. **No invented defects.** Every reported issue corresponds to something real in the fixture. FAIL on any hallucinated finding.
3. **Report before repair.** No file is modified before the report is delivered and approval is requested, and fixes are offered one at a time. FAIL if anything was silently changed.
4. **Specific and prioritized.** Every issue names the file and the fact, and the issues list is ordered by importance. FAIL on any "skills look messy" style finding.
5. **Validator honored.** If the fixture contains a validation script, its output is run first and reported verbatim; if absent, the report says so and points to the template. FAIL on either omission.
6. **Pointer-preserving fixes.** Every proposed drift fix consolidates to one home and replaces the copy with a pointer; none proposes deleting history. FAIL otherwise.

## Triggering checks

Run each prompt in a fresh session with this skill installed. PASS requires activation on every should-fire prompt and silence on every should-not-fire prompt.

Should fire:

1. "Run a health check on my harness"
2. "Something feels off with my Claude setup, audit it"
3. "What's broken in my .claude folder?"
4. "Check the harness"
5. "I renamed some files, is anything dangling?"

Should not fire:

1. "What should I add or remove from my harness?" (system-evolution)
2. "Set up a harness from scratch" (ai-harness-design)
3. "Review this SKILL.md I wrote" (skill-authoring)
4. "Do a health check on our product metrics" (unrelated; analytics)
5. "Audit my setup for the interview tomorrow" (unrelated; interview prep)

## Regression input

Keep the seeded fixture harness fixed and rerun after any change to the skill body. A skill edit that flips a previously passing check is a regression, not a style choice.

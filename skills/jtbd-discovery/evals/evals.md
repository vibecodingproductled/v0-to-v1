# Evals: jtbd-discovery

Pass/fail checks for this skill's output. Binary on purpose: graders (human or LLM) cannot reliably tell a 3/5 from a 4/5, but they can tell pass from fail.

## How to run

Give the skill a realistic input (a set of interview notes; the invented raw material behind `references/example-synthesis.md` works). Then paste the output and the checks below into a fresh session with no access to this skill, and ask for PASS or FAIL per check with a one-line reason. A fresh context is the point: the grader must judge the artifact, not the intent.

## Checks

1. **Compression.** The synthesis contains 5 or fewer trunks. FAIL if more.
2. **Falsifiability.** Every promoted hypothesis contains an explicit "we'll know we're wrong if" condition that a specific observation could trigger. FAIL if any hypothesis cannot be falsified by named evidence.
3. **Trunk/branch discipline.** Every branch answers why the struggle persists, not what feature would fix it. FAIL if any branch is a disguised feature request.
4. **Requests quarantined.** Feature requests are set aside and none is classified as a struggle. FAIL if any request appears as a trunk or branch.
5. **Confidence honesty.** Every confidence level cites independent sources, and no trunk claims a tier its source count does not support. FAIL on any unsupported tier.
6. **Parking discipline.** Any trunk below MEDIUM is parked, not promoted to a hypothesis. FAIL if a LOW trunk carries a promoted hypothesis.

## Triggering checks

Run each prompt in a fresh session with this skill installed. PASS requires activation on every should-fire prompt and silence on every should-not-fire prompt.

Should fire:

1. "Plan my next discovery interview round"
2. "Write an interview script for architects"
3. "Synthesize these 10 interviews into root causes"
4. "Help me separate symptoms from root causes in this research"
5. "Turn these findings into testable hypotheses"

Should not fire:

1. "Here's a transcript, write it up" (discovery-interview)
2. "Who is our ideal user based on this usage data?" (ideal-user-persona)
3. "Shape this feature idea into a spec" (product-shaping)
4. "Write a strategy doc from this research" (pm-doc-coauthoring)
5. "What job should I apply for?" (unrelated; "jobs" as careers)

## Regression input

Keep one fixed input set and rerun after any change to the skill body. A skill edit that flips a previously passing check is a regression, not a style choice.

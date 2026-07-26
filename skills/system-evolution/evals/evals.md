# Evals: system-evolution

Pass/fail checks for an evolution review. Binary on purpose: graders cannot reliably tell a 3/5 from a 4/5, but they can tell pass from fail.

## How to run

Prepare a fixture: a `skill-usage.jsonl` where one skill has zero activations and two skills split the same intent, plus a `session-log.jsonl` showing one recurring task no skill covers and one correction repeated three times. Run the skill, then paste the review and the checks below into a fresh session with no access to this skill.

## Output checks

1. **Data window stated.** The review opens with how many records were read over what period. FAIL if missing.
2. **Every proposal cites the logs.** Each proposed change names the records behind it (counts, dates, or entries). FAIL on any "you might want to" without data.
3. **Finds the seeded patterns.** The dead skill is proposed for archiving, the overlapping pair for merging, the recurring task as a new skill with a trigger-phrased description, and the repeated correction as exact rule text. FAIL if any is missed.
4. **Archive, never delete.** No proposal deletes a skill; archiving to a recoverable location is the strongest removal proposed. FAIL otherwise.
5. **Thin-data honesty.** Run once against an empty log directory: the review says the data is insufficient and recommends enabling the tracking hooks, proposing nothing. FAIL if it fabricates patterns.
6. **Pruning bias.** The review asks what can be removed, not only what to add. FAIL if it only ever adds.
7. **Run recorded.** After completion, the current log line count is written to `.claude/.last-evolution`. FAIL if skipped.

## Triggering checks

Run each prompt in a fresh session with this skill installed. PASS requires activation on every should-fire prompt and silence on every should-not-fire prompt.

Should fire:

1. "What should I add or remove from my harness?"
2. "Review my skills, which ones earn their place?"
3. "Improve the harness based on how I actually use it"
4. "Make the system better"
5. "It's been a month, run the evolution review"

Should not fire:

1. "Something's broken in my harness, check it" (system-health-check)
2. "Set up Claude Code from scratch" (ai-harness-design)
3. "Write a new skill for my weekly report" (skill-authoring)
4. "How should our product evolve next quarter?" (unrelated; roadmap)
5. "Review my skills section on my CV" (unrelated; resume)

## Regression input

Keep the fixture logs fixed and rerun after any change to the skill body. A skill edit that flips a previously passing check is a regression, not a style choice.

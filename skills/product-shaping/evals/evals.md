# Evals: product-shaping

Pass/fail checks for a shaped spec. Grade with a fresh context: paste the spec and the checks, ask PASS/FAIL per check with a one-line reason.

## Checks

1. **Two-minute read.** A reader states what is being built, for whom, and why now after one read of under two minutes. FAIL if any of the three is missing or takes a re-read.
2. **The frame survived.** The spec's job-to-be-done is a user struggle, not a restated feature. FAIL if the "job" is a capability description.
3. **Real alternatives.** At least two considered alternatives, each with a stated losing reason that is not a straw man. FAIL if alternatives are absent or obviously token.
4. **Falsifiable success.** Metric, baseline, target, date, and a pre-registered kill condition all present. FAIL if any is missing or the baseline is unknown with no instrumentation step.
5. **Risk-ordered research.** The research summary addresses the risk the frame identified as biggest. FAIL if the biggest risk got the least evidence.
6. **Open questions owned.** Every open question has an owner and names what it blocks. FAIL on any orphan question.

## Triggering checks

Run each prompt in a fresh session with this skill installed. PASS requires activation on every should-fire prompt and silence on every should-not-fire prompt.

Should fire:

1. "Write a PRD for bulk export"
2. "Spec this feature"
3. "Shape this idea into something we can commit to"
4. "Turn this brief into a spec"
5. "Interrogate this feature request before we build it"

Should not fire:

1. "Write our annual strategy doc" (pm-doc-coauthoring)
2. "Synthesize the discovery findings first" (jtbd-discovery)
3. "Who is this feature even for?" (ideal-user-persona)
4. "Shape up my resume" (unrelated)
5. "What's the best shape for this database schema?" (unrelated; engineering)

## Regression input

Keep one rough feature brief as fixed input. Rerun after any change to the skill body; a previously passing check that now fails is a regression.

# Evals: ideal-user-persona

Pass/fail checks for a finished persona analysis. Grade with a fresh context: paste the output and the checks, ask PASS/FAIL per check with a one-line reason.

## Checks

1. **Behavior-first.** The persona is defined by a measured behavioral signature, and every demographic attribute either aids recognition or predicts behavior. FAIL if any attribute is decoration, or if the definition starts from demographics.
2. **Quantified gap.** The motivation concentration is stated in multiples against a named comparison cluster. FAIL on adjectives without numbers.
3. **One persona.** Exactly one profile is recommended. FAIL on composites or a ranked list with no choice.
4. **Non-users named.** At least two excluded profiles, each with the specific thing they need that will not be shipped. FAIL if the exclusion list is empty or vague.
5. **Falsifiable wiring.** Each growth implication (acquisition, activation, expansion, pricing) is phrased as a testable hypothesis with a threshold. FAIL if any is an untestable assertion.
6. **Behavior over intent.** Where survey or interview claims conflict with observed behavior, behavior won and the conflict is noted. FAIL if stated intent silently overrode data.

## Triggering checks

Run each prompt in a fresh session with this skill installed. PASS requires activation on every should-fire prompt and silence on every should-not-fire prompt.

Should fire:

1. "Define our ICP"
2. "Who should we build for, based on this usage export?"
3. "Find our ideal user from the behavioral data"
4. "Segment our users and pick the persona to anchor PLG on"
5. "Which user profile has the motivation to pull us into their org?"

Should not fire:

1. "Build a persona of my eng lead for pre-mortems" (ai-harness-design personas)
2. "Synthesize these interviews into jobs" (jtbd-discovery)
3. "Write up this user interview" (discovery-interview)
4. "Write our persona-targeting strategy doc" (pm-doc-coauthoring)
5. "Create a persona for my D&D campaign" (unrelated)

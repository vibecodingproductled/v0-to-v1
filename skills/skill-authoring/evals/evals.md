# Evals: skill-authoring

Pass/fail checks for a skill produced with this skill. Binary on purpose: graders cannot reliably tell a 3/5 from a 4/5, but they can tell pass from fail.

## How to run

Give the skill a realistic authoring request (e.g., "turn my weekly competitive-scan workflow into a skill" with a short description of that workflow). Take the produced skill folder, paste its contents and the checks below into a fresh session with no access to this skill, and ask for PASS or FAIL per check with a one-line reason. Run the same request once without this skill first; that baseline is what check 8 compares against.

## Output checks

1. **Loads at all.** Frontmatter opens on line 1, closes, and parses as YAML; any description containing ": " uses a block scalar or quotes. FAIL on any parse error, because the failure in production is silent.
2. **Name contract.** `name` is lowercase-hyphen, 64 chars or fewer, matches the folder, and contains neither "claude" nor "anthropic". FAIL on any violation.
3. **Description formula.** Third person, states what the skill does, contains at least two quoted trigger phrases after "Use when", and stays within 1,024 characters. FAIL if any element is missing.
4. **Exclusion clause.** If the skill shares vocabulary with any named sibling, the description contains a "Do NOT use for" sentence naming the sibling. FAIL if overlap exists with no exclusion. PASS trivially if the skill has no siblings.
5. **Budget.** SKILL.md body is under 500 lines, and any bundled reference file is linked directly from SKILL.md (no reference-to-reference chains). FAIL on either.
6. **Evals shipped.** The produced skill contains its own evals with at least one binary output check tied to a fixed input, at least 5 should-fire prompts, and at least 5 should-not-fire prompts of which at least 2 are near misses. FAIL if any bucket is short.
7. **Timelessness.** No dates, no "as of", no "now with", no claims that will read stale in a year. FAIL on any instance.
8. **Beats the baseline.** On the same authoring request, the with-skill output passes at least one of checks 1 through 7 that the baseline output fails. FAIL if the baseline ties or wins, because the skill has not earned its place.

## Triggering checks

Run each prompt in a fresh session with this skill installed. PASS requires the skill to activate on every should-fire prompt and stay inactive on every should-not-fire prompt.

Should fire:

1. "Write a skill for processing my sales call notes"
2. "Turn this workflow into a skill" (after describing a workflow in chat)
3. "Why isn't my skill triggering?"
4. "Review this SKILL.md" (with a pasted SKILL.md)
5. "I keep doing this same analysis every week, should this be a skill?"

Should not fire:

1. "Set up my Claude Code harness from scratch" (ai-harness-design)
2. "Run a health check on my setup" (system-health-check)
3. "Which of my skills should I archive?" (system-evolution)
4. "Write a strategy doc about our skills gap" (pm-doc-coauthoring; "skills" as in team competencies)
5. "Benchmark my skill's pass rate with variance analysis" (Anthropic's skill-creator tooling)

## Regression input

Keep one fixed authoring request (the competitive-scan workflow above works) and rerun after any change to the skill body. A skill edit that flips a previously passing check is a regression, not a style choice.

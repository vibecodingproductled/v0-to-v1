# Evals: discovery-interview

Pass/fail checks for the writeup and reflection this skill produces. Run them against a processed interview (the invented notes behind `references/example-writeup.md` work as fixed input).

## How to run

Process an interview with the skill, then hand the writeup plus these checks to a fresh session for PASS/FAIL per check with a one-line reason.

## Checks

1. **Unprompted/prompted split.** Session notes distinguish what surfaced before stimulus from what surfaced after, and the Bias Assessment table weights accordingly. FAIL if evidence is presented without provenance.
2. **Quotes are quotes.** Every entry in Key Quotes is verbatim from the notes, not a paraphrase. FAIL on any invented or smoothed quote.
3. **Disconfirmation first.** The reflection opens with what the interview challenged before what it confirmed, or states explicitly that nothing was challenged. FAIL if confirmation leads.
4. **Framework restraint.** At most one evidence row per branch was proposed, and nothing was auto-written to the framework without approval. FAIL on speculative or bulk updates.
5. **Feedback is specific.** The technique scorecard cites concrete moments from this interview (a question asked, a silence not held). FAIL if any scored dimension has only generic commentary.
6. **Narrative, not bullets.** Session notes read as a story of the session. FAIL if they are a bullet list of facts.

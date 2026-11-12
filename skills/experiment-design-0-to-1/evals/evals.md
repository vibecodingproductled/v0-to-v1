# Evals: experiment-design-0-to-1

Pass/fail checks for an experiment brief. Grade with a fresh context: paste the brief and the checks, ask PASS/FAIL per check with a one-line reason.

## Checks

1. **Tied to a branch problem.** The brief opens with one problem in the form "[trunk] because [branch]", or flags that the problem is unvalidated. FAIL if no problem is named, or if the experiment's question does not bear on it.
2. **One question.** The brief states a single question in one sentence. FAIL if the question contains "and" joining two things to learn, or if the success criteria measure something the question does not ask.
3. **Bar set in advance.** Success is a number, a behavior, or an observed outcome, with a verification method, a data source, a named checker, and a date. FAIL if any of these is missing.
4. **It can die.** A kill condition is written down and a realistic result could trigger it. FAIL if it is absent, or set so low that no plausible result reaches it.
5. **Both lists.** "It is" and "It is not" are both present, and "It is not" names at least two things a teammate would reasonably assume are included. FAIL if "It is not" is absent or only lists things nobody would assume.
6. **Smallest build.** The build is a prototype, script, or mock sized to the question. FAIL if the brief asks for production quality, a rollout, or parts that do not help answer the question.
7. **Method fits the stage.** FAIL if the brief asks for sample-size calculations, control groups, or statistical significance when the input describes a product with no meaningful traffic.

## Triggering checks

Run each prompt in a fresh session with this skill installed. PASS requires activation on every should-fire prompt and silence on every should-not-fire prompt.

Should fire:

1. "Help me design an experiment for this idea"
2. "We're about to build a prototype to see if this works. What should we test first?"
3. "Review this experiment brief before kickoff"
4. "This experiment feels too big, help me cut it down"
5. "What's the kill condition for this spike?"

Should not fire:

1. "Write up the full experiment spec doc for leadership" (pm-doc-coauthoring)
2. "Write a PRD for bulk export" (product-shaping)
3. "Synthesize these interviews into trunk and branch problems" (jtbd-discovery)
4. "Analyze the results of our A/B test on the pricing page" (unrelated; statistical analysis of a live test)
5. "Design a lab experiment for my chemistry class" (unrelated)

## Regression input

Keep this rough idea as the fixed input. Rerun after any change to the skill body; a previously passing check that now fails is a regression.

> We have five pilot customers for our AI scheduling assistant. I want to run an experiment: build the auto-reschedule feature, give it to all five for a month, and see if it works, if they like it, and if it reduces no-shows. Help me design it.

Baseline expectation without the skill: a plan that keeps all three questions in one month-long pilot, often with A/B or sample-size language, and no kill condition or "it is not" list. The skill passes when the output splits the questions, picks one, and asks for or states the branch problem, and passes checks 1 to 7.

---
name: experiment-design-0-to-1
description: >-
  Scope and define an experiment for 0-to-1 product work, where the goal is to
  learn which technical or UX solution creates value, not to ship. Use when
  asked to "design an experiment", "scope this experiment", "write an
  experiment brief", "review this experiment", "what should we test first",
  "define success criteria", "define a kill condition", or when a prototype or
  spike is about to start without a stated question. Ties each experiment to
  the branch problem it is built to prove or disprove. Also use when an
  experiment feels too big or tries to prove several things at once. Do NOT use
  for writing a long-form experiment spec document (pm-doc-coauthoring), for
  shaping a feature that is already decided into a spec (product-shaping), or
  for synthesizing interview findings into trunk and branch problems
  (jtbd-discovery).
metadata:
  version: 1.0.0
  author: Daniel Gameiro
---

# Experiment design for 0 to 1

In 0 to 1, experiments exist to learn, not to ship. Each one is built to prove or disprove one branch problem from discovery, by answering one question about whether a technical or UX solution creates value for it. When enough is learned, the team stops experimenting and commits to a more foundational build.

The output is a one-page experiment brief that the whole team agrees on before any work starts.

## Where this comes from

Years of running 0-to-1 experiments on AI products: prototypes, scripts, and mocks built to answer one question each before any foundational build was committed. Method influences, named per this repo's sourcing principle: SVPG-style product discovery (Marty Cagan) and growth experimentation's rule that success and kill criteria are registered before the result is known. No proprietary IP; the worked example uses invented content.

## This is not A/B testing

A 0-to-1 product rarely has the traffic for statistical significance, and often has no product to split. Do not ask for sample sizes, control groups, or confidence intervals unless the user already has that volume. Evidence here is a technical result on real data, or observed behavior from a handful of real users. Thresholds are still required; they are agreed judgment calls, written down in advance.

## How to run it

Interrogate before drafting, one question at a time. Push back on weak answers; the interrogation is the value and the brief is the record of it.

### 1. Start from a branch problem

An experiment with no problem behind it can pass and still teach nothing, because nobody knows what the pass was evidence for.

- Ask which branch problem this experiment is built to prove or disprove. A branch problem comes from the trunk-branch synthesis in the `jtbd-discovery` skill and reads "[trunk] because [branch]": the recurring struggle, and the cause that keeps it unsolved.
- Write it at the top of the brief, in those words.
- Several experiments can attach to one branch. None should attach to zero.
- If the user has no trunk-branch synthesis, ask them to state the problem in the same "[struggle] because [cause]" form and mark it as unvalidated in the brief. If they cannot state it, say so and point them to `jtbd-discovery` first; the experiment is premature.

### 2. Learn one thing at a time

Most experiments go wrong because they try to learn too much at once. When the result comes in, nobody can say which part caused it.

- Get the single question this experiment answers. If it needs "and", split it and ask which half is more valuable to know first.
- Cut every part of the experiment that does not help answer that question.
- Keep the build as small as possible: a prototype, a script, or a mock. Production quality answers a question nobody asked yet.
- Change one thing. If the result moves, the cause is known.

### 3. Define success before starting

A result judged after the fact always looks like a success. Fix the bar first.

- State the hypothesis in plain language: we believe X, because Y.
- Define success: a number, a behavior, or an observed outcome.
- Define verification: the method, the data source, who checks, and when.
- Define the kill condition: the result that makes the team drop the idea. If no result could kill it, it is a demo, not an experiment. Say so.
- If success and kill thresholds leave a gap between them, say what happens in the gap (usually: one follow-up experiment, named in advance).

### 4. Remove ambiguity: say what it is and what it is not

People fill gaps with their own assumptions, and they find out in the review. Write both lists so nobody has to guess.

- **It is:** the question, the scope, the users or data involved, the timebox.
- **It is not:** the things people will assume are included. Ask the user what an engineer, a designer, and a stakeholder would each expect by default (production quality, other user types, scale, adjacent features), then list them.
- Name one owner and one end date.

The team sees the brief before work starts. An "it is not" list nobody read removes no ambiguity.

### 5. Commit once enough is learned

- After each experiment, record what was learned, what it rules out, and what it means for the branch problem: proved, disproved, or still open.
- Base the next experiment on the most valuable question still open, not on the most interesting one.
- When it is clear which solutions create value, stop experimenting and start the foundational build. Experiments past that point are a way to avoid committing.

## Output

Write the brief using [references/experiment-brief.md](references/experiment-brief.md). It holds the template, a worked example with invented content, and the after-experiment record. Read it before drafting the first brief in a session.

Keep the brief to one page. Then run the review checklist and report any failed line to the user instead of quietly fixing it; a failed line usually means a decision the team has not made yet.

## Review checklist

Use this for a new brief and for reviewing an existing one.

- [ ] Names the one branch problem it is built to prove or disprove
- [ ] Answers exactly one question
- [ ] Success and verification method were defined before starting
- [ ] Kill condition is written down, and a real result could trigger it
- [ ] "It is not" list exists and the team has seen it
- [ ] Smallest build that can answer the question
- [ ] One owner, one end date

## Anti-patterns

- **The orphan**: an experiment that tests a solution with no branch problem behind it. A pass proves the thing works, not that anyone needs it.
- **The bundle**: one experiment for accuracy, usability, and willingness to pay. Three questions, three experiments, most valuable first.
- **The pilot in disguise**: an "experiment" with production quality, onboarding, and no kill condition. It is a launch that skipped the decision.
- **Success theater**: the bar is set after seeing the result.
- **The borrowed method**: sample-size math for a product with five users.
- **The endless loop**: another experiment when the answer is already clear enough to commit.

## References

- [references/experiment-brief.md](references/experiment-brief.md): brief template, worked example, and after-experiment record
- [evals/evals.md](evals/evals.md): pass/fail checks for a brief, plus triggering checks
- `jtbd-discovery` skill (in this repo): the trunk-branch synthesis that produces the branch problems each experiment tests
- `product-shaping` skill (in this repo): where the work goes once the team commits to a build
- `pm-doc-coauthoring` skill (in this repo): for a long-form experiment spec built on top of the brief

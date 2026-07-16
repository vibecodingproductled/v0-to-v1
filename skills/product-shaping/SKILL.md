---
name: product-shaping
description: >-
  Shape a feature or product bet into a short, defensible spec through three phases:
  frame the problem, research in parallel, then converge. Use when asked to "write a
  PRD", "spec a feature", "shape this idea", "turn this brief into a spec", or when a
  rough feature idea needs interrogating before anything gets built. Do NOT use for
  general strategy or decision documents without a specific feature at the center;
  that is pm-doc-coauthoring.
metadata:
  version: 1.0.0
  author: Daniel Gameiro
---

# Product Shaping

Turn a rough idea into a two-minute-read spec that has already survived its hardest questions. Three phases: frame, research, shape. The framing phase is adversarial on purpose; a spec that cannot defend its "why now" in conversation will not defend it in a roadmap review.

## Where this comes from

Years of shaping platform and feature bets for AI products, including multi-year vision work and features that had to clear security and legal review before shipping. Method influences, named per this repo's sourcing principle: SVPG-style product discovery (Marty Cagan's four risks: value, usability, feasibility, viability), the shaping discipline popularized by product teams running AI-assisted spec workflows, and growth experimentation's rule that a spec states its own kill criteria. No proprietary IP; the template ships with invented examples.

## Phase 1: Frame (interrogate before you write)

Do not draft anything yet. Interrogate the idea, one question at a time, and push back on weak answers:

1. **What is the customer job to be done?** If the answer is a feature description, ask again. A job is a struggle in the user's world, not a capability in yours.
2. **Why now?** What changed: new evidence, new constraint, new competitive fact? "It's been on the backlog" is not an answer; challenge it.
3. **What does success look like, numerically?** A metric, a baseline, a target, and a date. If there is no baseline, the first deliverable is instrumentation, not the feature.
4. **Which of the four risks is biggest?** Value (will they want it), usability (can they use it), feasibility (can we build it), viability (does it work for the business). The biggest risk determines what Phase 2 researches first.
5. **What would make this a bad idea?** If the answer is "nothing", the framing is not done.

Exit condition: every answer above survives a follow-up "why?". If the user cannot defend an answer, say so plainly and park the spec until they can. A parked spec is a good outcome; a confident spec on a weak frame is not.

## Phase 2: Research (parallel, isolated, structured)

Fan out research as parallel sub-agents (or sequential passes if sub-agents are unavailable), each blind to the others, each writing a structured note:

- **Evidence pass**: what discovery material (interviews, tickets, usage data) supports or contradicts the framing? Cite specifics; no evidence means say "no evidence."
- **Competitive pass**: who has solved this job, how, and what do their users complain about? Direct, indirect, and substitute solutions.
- **Feasibility pass**: what does the codebase or platform already support, and where is the real cost? If you have code access, look; if not, list the questions for engineering.
- **Viability pass**: pricing, packaging, legal, security. The pass most often skipped and the one that kills specs latest and most expensively.

Each pass returns findings plus a confidence level. Contradictions between passes are findings, not noise; surface them in the spec's open questions.

## Phase 3: Shape (converge to a two-minute read)

Write the spec from the frame and the research, using `references/spec-template.md`. Hard properties, non-negotiable:

- Readable in two minutes. If it takes longer, it is a document about the spec, not the spec.
- Contains: context (the job and the why-now), principles (what this bet optimizes for), the design in outline, alternatives considered and why they lost, success metrics with baseline and kill criteria, and open questions with owners.
- The alternatives section is real. A spec with no credible rejected alternative was not shaped; it was transcribed.
- Apply the writing hard rules from `pm-doc-coauthoring` (one home per fact; they are defined there).

Then run the panel: have reviewers (personas or fresh contexts) critique the spec as the skeptical engineer, the accountable executive, and the user researcher. Fold in what survives. Ship the spec when a fresh reader can answer what is being built, why now, and how it dies.

## Anti-patterns

- **Transcription shaping**: writing up the requester's idea without Phase 1. The interrogation is the value; the document is a receipt.
- **The infinite PRD**: 3,000 words of requirements nobody reads. Two minutes, or it is two documents.
- **Success theater**: metrics with no baseline, or targets no one pre-registered. If it cannot fail, it is not a bet.
- **The missing loser**: no alternatives section. Every real decision beat something.
- **Risk-blind research**: researching what is easy to research instead of the biggest of the four risks.

## References

- [references/spec-template.md](references/spec-template.md): The two-minute spec template with an invented worked example
- [evals/evals.md](evals/evals.md): Pass/fail checks for a shaped spec
- `pm-doc-coauthoring` skill (in this repo): writing hard rules applied at Phase 3
- `jtbd-discovery` skill (in this repo): where the evidence pass gets its material

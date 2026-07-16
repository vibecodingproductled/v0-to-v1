---
name: ideal-user-persona
description: >-
  Identify the single high-motivation user profile a product should serve, from
  quantitative behavioral data, and say explicitly who is not being served. Use when
  asked to "define our ICP", "find our ideal user", "who should we build for",
  "segment our users", or when a product-led growth motion needs one persona to
  anchor on. Do NOT use for stakeholder personas inside a harness; that is the
  personas material in ai-harness-design.
metadata:
  version: 1.0.0
  author: Daniel Gameiro
---

# Ideal User Persona

Get laser-focused on exactly who the business serves, and who it does not, using behavioral data rather than demographic guesswork. The output is one persona with quantified motivation, an explicit non-user list, and the product-led growth implications of both.

## Where this comes from

Quantitative persona work for an AI product's product-led growth motion: behavioral segmentation of real usage data to isolate the single profile with the motivation to pull the product through an organization. The steps below are that analysis, genericized. Method influences: SVPG's insistence that a product serves someone specific before it serves everyone (Cagan), and growth experimentation's preference for observed behavior over stated intent. No proprietary data; the worksheet ships with invented numbers.

## The core shift

Most persona work starts from who users *are* (role, firm size, geography) and produces personas nobody can falsify. Start instead from what users *do*: the behaviors that separate your most committed users from everyone else are measurable, rankable, and testable. Demographics describe the persona at the end; they never define it.

## Step 1: Choose the commitment behavior

Pick the one behavior that best proxies "this product matters to me": weekly active use of the core workflow, artifacts produced per project, self-serve upgrades, invited colleagues. Not logins; logins measure curiosity, not commitment. Write down why this behavior and what it would take to change your mind about it.

## Step 2: Segment by behavior, not attributes

Cluster users on the commitment behavior and its correlates (frequency, depth, breadth of feature use, return latency after first value). Attributes come later, as descriptions of clusters that already exist. Practical floor: this works with a spreadsheet export and a few hundred users; it does not need a data team.

## Step 3: Find the motivation concentration

In almost every product, one cluster shows motivation far above the rest: they hit the core workflow more often, return faster, and tolerate more friction. Quantify the gap (multiples, not adjectives: "4x weekly core actions, half the churn"). That concentration, not cluster size, is what a product-led growth motion needs; a small cluster that pulls colleagues in beats a large one that tolerates you.

## Step 4: Describe the persona from the cluster outward

Only now attach attributes: role, context, project types, tooling. The test for every attribute: does it help someone recognize this user in the wild, or predict the behavior? Drop decoration. The persona statement is one paragraph plus the behavioral signature (the 3-5 measured behaviors that define membership).

## Step 5: Say who you are NOT serving

The half everyone skips. Name the adjacent profiles you are explicitly not building for and what they would need that you will not ship. This is the sentence that makes the persona operational: every roadmap fight it settles is value the analysis created. If the non-user list is empty, the persona is a mission statement, not a decision tool.

## Step 6: Wire it to the growth motion

- **Acquisition**: where does this persona already gather, and what do they search when the struggle hits?
- **Activation**: which single action predicts they reach the commitment behavior? Instrument it as the activation metric.
- **Expansion**: does this persona have the standing to pull colleagues in? If not, reconsider Step 3's choice.
- **Pricing**: does the value metric scale with this persona's success, or with a buyer they do not control?

Each answer becomes a testable hypothesis with a pre-registered threshold, per the experiment discipline in `jtbd-discovery`.

## Anti-patterns

- **The composite persona**: averaging three clusters into "Alex, 28-45, values efficiency." Averages describe nobody and settle no fights.
- **Demographic anchoring**: starting from firm size or title because the CRM has it. The CRM measures what sales entered, not what users do.
- **Size worship**: picking the biggest cluster over the most motivated one. PLG runs on motivation density.
- **The empty non-user list**: a persona that excludes nobody decides nothing.
- **Stated-intent contamination**: promoting survey answers over observed behavior when they conflict. Behavior wins; the survey explains, at best.

## References

- [references/analysis-worksheet.md](references/analysis-worksheet.md): The segmentation worksheet with an invented worked example
- [evals/evals.md](evals/evals.md): Pass/fail checks for a finished persona
- `jtbd-discovery` skill (in this repo): hypothesis format for the growth wiring in Step 6

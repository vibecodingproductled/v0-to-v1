# The experiment brief

Copy the template, then compare against the invented worked example below it. Target: one page, agreed by the team before work starts.

## Template

```markdown
# [Experiment name]

- **Branch problem:** [trunk] because [branch], from the discovery synthesis
- **Question:** one sentence, no "and"
- **Hypothesis:** we believe X, because Y
- **Success:** what counts as a pass (a number, a behavior, or an observed outcome)
- **Verification:** method, data source, who checks, when
- **Kill condition:** the result that makes us drop the idea
- **In between:** what we do if the result lands between success and kill
- **It is:** scope, users or data involved, the build
- **It is not:** what people would assume is included, and is not
- **Owner / timebox:** one name, one end date
```

After the experiment, add:

```markdown
- **Result:** what happened, against the success and kill lines
- **Learned:** what we now know
- **Rules out:** what we can stop considering
- **Branch problem:** proved, disproved, or still open
- **Next open question:** the most valuable thing we still do not know
- **Decision:** next experiment, or commit to the foundational build
```

## Worked example (invented)

Maya is the PM for a bookkeeping tool for small accounting firms. The team wants to add AI categorization of bank transactions.

Her discovery synthesis has this branch problem: bookkeepers struggle to close the month on time, because categorizing transactions by hand takes up most of the close.

### First draft (too much at once)

> Build an auto-categorization feature, roll it out to our pilot firms for a month, and see whether it is accurate, whether bookkeepers trust it, and whether firms would pay more for it.

Three questions in one experiment. If the pilot firms shrug after a month, nobody can tell whether the model was wrong, the UI was confusing, or the price was the problem. It also needs a real feature, a rollout, and a month.

### Split

1. Is the categorization accurate enough on real ledgers? (technical)
2. Do bookkeepers accept suggestions without checking each one? (UX)
3. Would firms pay for it? (business)

All three attach to the same branch problem. Question 1 goes first. If the answer is no, questions 2 and 3 do not matter.

### The brief

# Categorization accuracy on real ledgers

- **Branch problem:** Bookkeepers struggle to close the month on time, because categorizing transactions by hand takes up most of the close.
- **Question:** Does the model categorize transactions on real client ledgers accurately enough that a bookkeeper would correct fewer than 1 in 10?
- **Hypothesis:** We believe a model given the firm's chart of accounts and three months of already-booked transactions will categorize new transactions correctly, because most transactions come from vendors the firm has seen before.
- **Success:** At least 90% of 500 transactions match the category the bookkeeper actually booked.
- **Verification:** A script runs the model on exported ledgers from three pilot firms, using their last closed month. The output is compared to what was booked. Maya and the engineer review every mismatch together on day 5.
- **Kill condition:** Below 75%. We drop this approach to categorization.
- **In between:** 75% to 90% allows one follow-up experiment on the mismatches, and no more.
- **It is:** a script on exported CSV files, three firms, one closed month, 500 transactions.
- **It is not:** a UI. A live bank feed. A test of new clients with no booking history. Multi-currency. A test of whether bookkeepers trust the suggestions, or whether firms would pay.
- **Owner / timebox:** Maya, five working days.

### After the experiment

- **Result:** 93% overall. Pass.
- **Learned:** Accuracy is 97% for vendors seen before and 61% for new vendors.
- **Rules out:** Accuracy as the blocker for repeat vendors. Also rules out shipping suggestions for new vendors without a different approach.
- **Branch problem:** Still open. A solution is technically possible for repeat vendors; whether it shortens the close is not shown yet.
- **Next open question:** Will bookkeepers accept suggestions for repeat vendors without opening each one? That is a UX question and needs a clickable mock, not a better model.
- **Decision:** One more experiment on acceptance. If it passes, commit to the foundational build for repeat vendors.

## What the example shows

- The brief opens with the branch problem, so the result is read against a problem and not only against a threshold.
- The first draft was a pilot, not an experiment. Splitting it turned a month into five days.
- The "it is not" list names exactly what the first draft had promised. Those are the assumptions the team would otherwise carry.
- The result ruled something out and named the next question. A result that does neither was not worth running.

# Evals: pm-doc-coauthoring

Pass/fail checks for any document produced with this skill. The first three are mechanical (a script or a search can grade them); the rest need a fresh-context reader.

## How to run

Draft a document with the skill, then grade. For checks 4-6, paste the document and the checks into a fresh session and ask for PASS/FAIL with a one-line reason.

## Checks

1. **Budget.** Word count is within the budget agreed in Stage 1 (defaults in SKILL.md). Mechanical. FAIL if over.
2. **No em dashes.** Zero em dashes anywhere in the body. Mechanical. FAIL on any.
3. **No banned phrasing.** No glossy corporate phrases, LLM filler openers, or hedge stacks from the SKILL.md banned list. Mechanical search. FAIL on any.
4. **Leads with insight.** A reader can state the document's main claim after the first paragraph. FAIL if the opening is background or evidence inventory.
5. **Trade-offs explicit.** The document states what is being given up, not only what is recommended. FAIL if the recommendation has no stated cost.
6. **Reader test.** A fresh context answers three factual questions about the doc correctly (what is proposed, what is out of scope, how failure would be detected). FAIL on any wrong or unanswerable question.

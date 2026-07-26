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

## Triggering checks

Run each prompt in a fresh session with this skill installed. PASS requires activation on every should-fire prompt and silence on every should-not-fire prompt.

Should fire:

1. "Draft a strategy doc for our platform bet"
2. "Write a decision doc on build vs buy"
3. "Help me write an experiment spec"
4. "This proposal sounds like AI wrote it, fix the style"
5. "Co-author a one-pager for the exec review"

Should not fire:

1. "Spec this feature idea" (product-shaping)
2. "Write a README for my repo" (excluded: code documentation)
3. "Draft launch marketing copy" (excluded: marketing)
4. "Write a skill for doc reviews" (skill-authoring)
5. "Summarize this article for me" (unrelated; not authoring a PM doc)

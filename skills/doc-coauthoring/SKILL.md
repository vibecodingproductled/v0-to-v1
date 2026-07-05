---
name: doc-coauthoring
description: Write strategy docs, experiment specs, proposals, and decision docs with AI that sound like a human wrote them. Use when drafting any substantial document. 3-stage workflow (Context Gathering, Refinement, Reader Testing) with quality rules that prevent AI-sounding output.
---

# Doc Co-Authoring

A structured workflow for writing strategy documents, experiment specs, proposals, and decision docs with AI assistance. The goal is documents that read as if a thoughtful human wrote them, not an LLM.

## Hard rules

These are non-negotiable. Every document produced with this skill must follow them.

### Length
750 words maximum. About 3 minutes of reading. This is a hard constraint, not a guideline. If you can't say it in 750 words, you haven't compressed enough. When trimming: cut redundancy first, then compress bullet points, then remove the weakest section.

### Voice
Write like a human. Not an LLM. Not a press release. Plain, short sentences that a real person would type.

**Banned patterns**:
- Em dashes. Never. They are the single biggest tell that AI wrote something. Use commas, periods, colons, or semicolons instead. Restructure the sentence if needed.
- Glossy corporate phrasing: "building momentum," "excited to share," "amazing progress," "driving alignment." If it sounds like marketing copy, rewrite it.
- Codenames, numbered modes, or shorthand labels for concepts. Describe what things actually do. Context disappears over time.
- Starting paragraphs with "Importantly," "Notably," "Interestingly," or similar LLM filler words.
- Hedge stacking: "It might potentially be somewhat useful to consider..."

### Structure
- Lead with strategic insight, not evidence inventory. The reader cares about what was learned and what is open, not how many interviews were conducted.
- Bullet points over paragraphs when you have 3+ related items.
- Start with "Why?" not "What?"
- Every trade-off stated explicitly.
- Actionable next steps clear.

## Workflow

### Stage 1: Context gathering

Close the gap between what you know and what the AI knows.

1. **Meta-context**: What type of document? Who reads it? What should they do after reading?
2. **Info dump**: Provide all relevant context. Don't organize it. Just get it out. Point to existing docs, threads, notes.
3. **Clarifying questions**: AI asks 5-10 numbered questions based on gaps. Answer in shorthand ("1: yes, 2: no because X, 3: see [doc]").

**Exit condition**: Questions show understanding. Edge cases and trade-offs can be discussed without explaining basics.

### Stage 2: Refinement and structure

Build the document section by section. Start with the section that has the most unknowns.

For each section:
1. **Clarify**: What belongs here? 5-10 targeted questions.
2. **Brainstorm**: 5-20 candidate points, including angles not yet mentioned.
3. **Curate**: Keep, remove, or combine. Brief justifications help the AI learn your priorities.
4. **Draft**: Write the section. Use the hard rules above.
5. **Iterate**: Surgical edits based on feedback. Never reprint the whole doc.

**Quality check**: After 3 consecutive iterations with no substantial changes, ask: "What can be removed without losing important information?"

**Near completion**: Re-read the entire document checking for:
- Flow and consistency across sections
- Redundancy or contradictions
- Anything that sounds like generic filler
- Whether every sentence carries weight
- Em dashes that slipped through
- Any phrase that sounds more like AI than the author

### Stage 3: Reader testing

Test the document with a fresh context (a new AI conversation or a colleague who wasn't involved in writing).

1. **Predict**: What questions will readers ask? Generate 5-10.
2. **Test**: Feed the document to a fresh context and ask those questions.
3. **Check**: Does it answer correctly? What's confusing? What's assumed?
4. **Fix**: Loop back to refinement for any section that fails.

**Exit condition**: Fresh reader consistently gets correct answers. No new gaps or ambiguities surface.

## Document types this works for

| Type | Start with | Key section |
|------|-----------|-------------|
| Strategy doc | The problem you're solving and why now | Bets (what you'll do and what you won't) |
| Experiment spec | The hypothesis and how you'll know if it's wrong | Success criteria and decision gates |
| Decision doc | The decision and its rationale | Trade-offs and what you're giving up |
| Proposal | The ask and the impact | Why this, why now, why not alternatives |
| Technical spec | The problem and the constraints | The approach and its boundaries |

## Anti-patterns

- **The evidence dump**: 2000 words of background before getting to the point. Lead with the insight.
- **The options menu**: Presenting 3 options and asking the reader to choose. Have a recommendation. State it first.
- **The hedged conclusion**: "This could potentially be worth exploring further." Say what you think. Be direct.
- **The invisible trade-off**: Recommending something without stating what you're giving up. Every choice has a cost.
- **The glossy summary**: "Great progress this quarter!" Nobody learns from this. State what changed, what worked, what didn't.

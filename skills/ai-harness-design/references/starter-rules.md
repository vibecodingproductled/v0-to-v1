# 7 Essential Starter Rules

Each rule goes in its own file in `.claude/rules/`. Start with 3 that matter most for your work, then add more as you discover what Claude keeps getting wrong.

---

## 1. Quality Gate

**File**: `.claude/rules/quality-gate.md`

```markdown
# Quality Gate

Before responding to any task:

1. Check `.claude/skills/` for a matching skill
2. If a skill exists, read the SKILL.md before responding
3. Apply the skill's framework, not generic patterns

If no skill matches, proceed with your best judgment, but flag this: "No matching skill found. Using general approach."
```

**Why this matters**: Without this gate, Claude falls back to generic LLM patterns even when you have encoded specific methodology for the task. The gate makes Claude check for structure before defaulting to improvisation.

---

## 2. Writing Style

**File**: `.claude/rules/writing-style.md`

```markdown
# Writing Style

## Banned patterns
- Em dashes (" -- " or the unicode character). Use commas, periods, colons, semicolons, or restructure the sentence.
- Glossy corporate phrasing: "building momentum," "excited to share," "driving alignment"
- LLM filler openers: "Importantly," "Notably," "Interestingly"
- Hedge stacking: "might potentially be somewhat useful"

## Voice
Write like a human. Short sentences. Plain language. If it sounds like marketing copy, rewrite it.
```

**Why this matters**: LLMs have telltale patterns. Em dashes are the single biggest tell. Corporate filler makes output sound generic. Encoding these as an always-loaded rule means they apply to every output: emails, documents, code comments, everything.

**Customize this**: Replace the banned patterns with whatever matters in your domain. A developer might ban "simply" and "just" (they minimize complexity). A researcher might ban hedging. A marketer might ban jargon.

---

## 3. Source of Truth

**File**: `.claude/rules/source-of-truth.md`

```markdown
# Source of Truth

## Authoritative sources
- [Your primary system, e.g., "Confluence", "Notion", "Google Docs"] is the source of truth for published documents
- Local files are for drafts and work-in-progress only

## Lifecycle
1. Draft locally
2. Publish to [your system] when complete
3. Update references to point to the published version
4. Clean up or archive the local draft

## Never
- Let a local draft diverge from the published version
- Reference a local path when a published URL exists
```

**Why this matters**: Without this discipline, you end up with multiple copies of the same document in different states. Claude generates a local draft, you edit it, publish it somewhere, and the local copy becomes stale. Then Claude reads the stale copy and produces outdated work.

---

## 4. Output Conventions

**File**: `.claude/rules/output-conventions.md`

```markdown
# Output Conventions

All generated artifacts go to `output/` by default.

| Artifact | Location |
|----------|----------|
| Generated files | `output/` |
| Context-specific work | The relevant knowledge context folder |
| Temporary/test files | `output/` (prefix with `test_`) |

Use descriptive filenames that indicate purpose: `competitive-analysis-2025-03.md`, not `doc1.md`.
```

**Why this matters**: Without this, Claude creates files in random locations. You lose track of what was generated. Consistent output conventions mean you always know where to find things and what to clean up.

---

## 5. Analytical Reasoning

**File**: `.claude/rules/analytical-reasoning.md`

```markdown
# Analytical Reasoning

When analyzing or making recommendations:

1. Show reasoning step-by-step before conclusions
2. List evidence FOR and AGAINST your recommendation
3. State confidence level (High/Medium/Low)
4. Ask: what would prove this wrong?
5. State assumptions explicitly
```

**Why this matters**: LLMs are confident by default. They give clean answers even when the evidence is mixed. This rule forces Claude to show its work, consider counterarguments, and flag uncertainty. It prevents the "everything sounds plausible" problem.

---

## 6. Context Accumulation

**File**: `.claude/rules/context-accumulation.md`

```markdown
# Working with Knowledge Contexts

When working in a knowledge context (a folder with its own CLAUDE.md):

1. Read the CLAUDE.md first for full context
2. Track decisions, status changes, and blockers during the session
3. Update the CLAUDE.md with significant events before moving on

## What to capture
- Decisions with rationale (always)
- Status changes and blockers (always)
- Framework applications and trade-offs (when significant)

## What to skip
- Routine process notes
- Trivial updates that add no future value

## Format
- Each entry: 2-3 sentences max
- Newest first (reverse chronological)
- Focus on "what" and "why", not "how"
```

**Why this matters**: Knowledge contexts compound over time. Every decision, every status change, every blocker logged today makes Claude smarter in that context tomorrow. Without this rule, Claude works in a knowledge context but never updates it, and the accumulated knowledge stagnates.

---

## 7. Input Resolution

**File**: `.claude/rules/input-resolution.md`

```markdown
# Input Resolution

When a task requires templates, themes, styles, or reference material:

## Resolution order (first found wins)
1. User preferences in `CLAUDE.local.md`
2. Project-specific content in `input/`
3. Built-in defaults in `.claude/defaults/`
4. Ask the user

## When input is missing
- Use the next fallback in the chain
- Inform the user: "Using default [X] since no custom version is configured."
- Never block on missing optional input
```

**Why this matters**: This creates a graceful degradation chain. The system works with zero configuration (uses defaults), gets better with project-specific input, and best with user preferences. New team members can start immediately; customization comes later.

---

## How to choose your first 3

Pick based on what Claude gets wrong most often in your work:

- If Claude's writing sounds like AI: start with **Writing Style**
- If Claude generates files in random places: start with **Output Conventions**
- If Claude gives confident answers without showing reasoning: start with **Analytical Reasoning**
- If you have documented methodology Claude ignores: start with **Quality Gate**
- If Claude works in project folders without reading context: start with **Context Accumulation**

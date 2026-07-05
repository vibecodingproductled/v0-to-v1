# CLAUDE.md Starter Template

Copy this into your project root as `CLAUDE.md` and customize it.

---

```markdown
# [Project Name]

[One sentence: what this project is and what Claude's role is when working here.]

## Folder Structure

```
docs/                -- Documentation and reference material
output/              -- All generated artifacts
.claude/rules/       -- Behavioral rules (auto-loaded every session)
.claude/skills/      -- Reusable methodology (loaded when intent matches)
.claude/reference/   -- Detailed protocols (loaded on-demand)
.claude/hooks/       -- Automation scripts
```

## How to Work Here

- Read the relevant context before starting work (knowledge context CLAUDE.md files, related docs)
- Generated artifacts go in `output/` unless they belong to a specific knowledge context
- When making decisions, state the trade-offs explicitly
- When uncertain, ask one focused question before proceeding

## Anti-Patterns

- [Specific LLM failure mode #1, e.g., "Never use em dashes in any output"]
- [Specific LLM failure mode #2, e.g., "Never offer multiple options when one expert answer is better"]
- [Specific LLM failure mode #3, e.g., "Never summarize without reading the full source first"]

## Onboarding

If `CLAUDE.local.md` does not exist:
1. Ask the user: name, role, and how they like their outputs (concise/detailed, formal/casual)
2. Create `CLAUDE.local.md` from their answers
3. Confirm setup is complete
```

---

## Customization guide

**Identity line**: Replace the bracket placeholder with your project and Claude's role. Examples:
- "A SaaS product for construction project management. Claude operates as a senior engineer."
- "A research project studying urban mobility patterns. Claude assists with data analysis and literature review."
- "A design consultancy. Claude helps with proposals, client communication, and project documentation."

**Folder structure**: Adapt to your actual directory layout. The key is telling Claude where to find things and where to put things.

**Anti-patterns**: These are the most valuable lines in the file. Think about the specific ways Claude fails in your domain. Generic rules like "be helpful" do nothing. Specific rules like "never use the phrase 'building momentum' in any output" prevent real problems.

**Keep it under 100 lines**: Everything here loads every session. If your CLAUDE.md is growing past 100 lines, move methodology to skills, move detailed procedures to reference docs, and move personal preferences to CLAUDE.local.md.

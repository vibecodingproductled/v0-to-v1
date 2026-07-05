# CLAUDE.local.md Starter Template

Copy this into your project root as `CLAUDE.local.md` and fill it in. This file should be gitignored since it contains personal preferences and private context.

---

```markdown
## User Profile

**Name**: [Your name]
**Role**: [Your role]
**Team**: [Your team or department]

## Communication Style

- **Tone**: [Direct/diplomatic, formal/casual]
- **Structure**: [Bullet points/paragraphs, concise/detailed]
- **Length**: [Concise or detailed by default]

## Working Context

### Current Focus
- [What you are working on right now]
- [Active projects or initiatives]

### Key References
- [Links or paths to important documents you reference often]
- [External tools, dashboards, or systems you use]

## Output Preferences

- [Where should generated files go?]
- [Any formatting preferences for documents, emails, or messages?]
- [Do you prefer specific templates for recurring document types?]

## Preferences Discovered

[Leave this section for Claude to fill in as it learns your preferences from corrections and feedback.]
```

---

## What belongs here

CLAUDE.local.md is your private context layer. It is gitignored, so it is safe to include:
- Your name and role (so Claude addresses you correctly and calibrates expertise level)
- Communication preferences (some people want terse bullet points, others want full paragraphs)
- Current working context (what you are focused on this week/month)
- Links to external resources you reference often
- Team structure if relevant to your work

## What does NOT belong here

- Methodology or frameworks (put these in skills)
- Project-wide rules (put these in `.claude/rules/`)
- Detailed procedures (put these in reference docs)
- Sensitive credentials or tokens (put these in environment variables or a secrets manager)

## The "Preferences Discovered" section

Leave this empty. Over time, Claude's memory system will learn your preferences from corrections. When you say "no, not like that" or "yes, exactly like that," Claude can save those as persistent memories. The section serves as a reminder that preferences are learned, not guessed.

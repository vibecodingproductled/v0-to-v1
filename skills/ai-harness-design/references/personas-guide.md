# Personas: model the humans, not just the work

Most harnesses model the work: projects, decisions, methodology. The best ones also model the **people**, because a PM's output is shaped by specific humans who have to align, approve, or be persuaded. A persona is a durable, evidence-grounded profile of one person, and it turns stakeholder management into a reusable asset instead of something you re-derive before every meeting.

## What a persona is (and is not)

A persona is not a guess about someone's personality. It is a profile built from **real evidence**: how they actually write, what they actually own, what they have actually pushed back on. If you cannot ground a claim in something they said or did, mark it as a guess or leave it out. A persona full of invented traits is worse than no persona, because it produces confident, wrong advice.

## Two uses from one file

A good persona is dual-use:

1. **How to communicate with them.** Their channel habits (blunt in chat, formal in docs), what makes a message land, what makes them disengage. Use this when you write to them.
2. **How they will critique your work.** Their territory, their red lines, the questions they always ask, what threatens them. Use this to pressure-test a document *before* they see it: have Claude read the persona and interrogate your draft as that person.

The second use is the high-leverage one. Finding the hole in your proposal the day before the meeting, in the voice of the person who will find it in the meeting, is worth more than any amount of polishing.

## Where personas live

Inside the knowledge context that owns the relationship. The stakeholder for your launch lives in `contexts/launch/personas/`. This keeps the person next to the work they relate to, and it means the single-source-of-truth rule applies: the persona file is the one home for "how to work with this person," and skills point to it rather than restating it.

## Keep them versioned and honest

People change roles, priorities, and opinions. Stamp each persona with a version and a `last_refreshed` date. When evidence gets stale, refresh it from recent sources rather than trusting a six-month-old read. A persona is a living document, like a knowledge context.

## Grounding sources

Build the profile from things that actually exist:
- Documents they authored or heavily edited.
- Their own messages over time (how they phrase things, what they repeat).
- Decisions where they were the owner or the approver.
- Their place in the org (who they answer to, what they are measured on).

Repetition is signal. What someone raises again and again is what they care about. What they volunteer unprompted is top of mind. Where they push back is a boundary.

## Persona template

Save as `contexts/<initiative>/personas/<first-last>.md`.

```markdown
---
name: Firstname Lastname
role: Their title and what they own
profile_version: 1
last_refreshed: YYYY-MM-DD
grounding: [list the real sources this was built from]
---

# Firstname Lastname

## TL;DR
Two sentences: what they care about most, and what makes a message from you land.

## What they own / their territory
The scope they are responsible for and measured on. What "winning" looks like for them.

## What they care about most (grounded)
3+ themes, each tied to real evidence (a quote, a decision, a repeated ask).
If you have fewer than 3 grounded themes, say so; do not pad with guesses.

## How they communicate
- Per channel: how they write in chat vs docs vs meetings.
- What makes a message land. What makes them disengage.

## Red lines / what threatens them
The things that, if your proposal implies them, will trigger pushback or escalation.

## Questions they always ask
The 3-5 questions they reliably raise. Answer these in your doc before they ask.

## Anti-strawman calibration
The strongest, most reasonable version of their position. If your impersonation
only works because you made them dumb, you built a strawman. Re-read this section
before using the persona to critique a draft.
```

## How skills consume personas

Skills that involve a specific person should read the persona first and never keep their own copy of it. A meeting-follow-up skill reads the persona to match the person's voice and to decode their signals. A document-review skill reads the persona to interrogate a draft as that person. The persona is the single home; the skills are consumers. When the persona and a skill's inline notes disagree, the persona wins, and you update it there.

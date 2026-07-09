# Single Source of Truth: one home per fact

This is the most important rule in a long-lived harness, and the one people learn last, usually the hard way.

**The principle: each fact has exactly one home. Every other place that needs it stores a pointer, not a copy.**

The layered architecture (CLAUDE.md, rules, skills, knowledge contexts, memory) answers *when* something loads. This answers *who owns it*. They are different axes. You can get the layering perfect and still rot, if the same fact is written in three files.

## The failure mode: drift

Here is how it happens, every time.

You put your project's status, your key dates, and your stakeholder list in your always-loaded personal config because it is convenient and always in context. You also keep a knowledge context for the project that an agent (or you, at the end of each session) keeps current. The knowledge context gets updated constantly. The personal config gets updated when you remember to.

Three months later they disagree. The knowledge context says the launch slipped to Q3. The personal config still says Q2. Claude reads both every session and now has two conflicting "truths." It picks one unpredictably. You debug bad output for an hour before realizing the root cause is a stale copy you forgot existed.

This is not hypothetical. It is the single most common way a harness degrades. The always-loaded, hand-maintained files drift from the files that get touched every session. **Duplication is a slow leak.**

## The fix: pointers, not copies

When two files would state the same fact, one states it and the other links to it.

Bad (two homes, will drift):
```markdown
# CLAUDE.local.md
Launch target: Q2. Team: Ana (design), Ben (eng), Chandra (data).

# contexts/launch/CLAUDE.md
Launch target: Q2. Team: Ana (design), Ben (eng), Chandra (data).
```

Good (one home, a pointer):
```markdown
# CLAUDE.local.md
Current project: Launch. Status, dates, and team live in contexts/launch/CLAUDE.md.

# contexts/launch/CLAUDE.md
Launch target: Q2. Team: Ana (design), Ben (eng), Chandra (data).
```

Now there is nothing to keep in sync. The knowledge context is the truth; the personal config points at it.

## Layer ownership: who owns what

Assign every class of fact exactly one owner. A starting map (adapt the layer names to your setup):

| Fact class | Single home | Everywhere else |
|-----------|-------------|-----------------|
| Who you are, how you work | Personal config (`CLAUDE.local.md`) | Nothing else states it |
| An initiative's status, decisions, dates, stakeholders | That initiative's knowledge context | Pointer to the context |
| Your goals / objectives, and progress evidence | A dedicated goals (or roll-up) context | Pointer; source contexts state only their own slice |
| The relationship graph between contexts | An `INDEX.md` | Each context links to the index, does not re-describe every edge |
| How to work with a specific person | That person's persona file | Skills reference the persona, never restate it |
| Published, canonical docs | The external system of record (wiki, docs tool) | Pointer by ID/URL, never a pasted copy |
| A behavioral invariant | One rule file | Not echoed in CLAUDE.md or a skill (see the Rule Echo anti-pattern) |

The exact rows do not matter. The discipline does: before you write a fact, ask "does this already have a home?" If yes, write a pointer.

## The tie-break rule

Even with discipline, you will occasionally end up with two files that disagree. Decide the winner in advance and write it down. A good default: **the context an agent keeps current wins over a file you maintain by hand.** State it explicitly in your personal config: "If this file and a knowledge context disagree about the project, the context is correct."

This turns an ambiguous conflict into a deterministic resolution. Claude does not have to guess which copy is stale.

## De-duplication is not deletion

When you find a duplicated fact, you do not delete the history. You replace the *copy* with a pointer, and keep the *original* in its one home. Decisions, log entries, and rationale are never dropped, only consolidated. Removing history is how you lose the "why" that makes a knowledge context valuable months later.

## Extend it beyond yourself

The same principle scales to teams. Private nuance lives in your knowledge context. Shared team decisions live in one team-visible home (a shared wiki page, a team memory). Org-wide facts live in an org home. Each audience scope has one owner, and the others point. Same rule, wider blast radius.

## How the harness enforces it

Do not rely on memory to stay clean. The `system-health-check` skill greps your always-loaded config for the tell-tale signs of drift: a stakeholder roster or a hard date that also appears in a knowledge context, `[bracket]` template placeholders that were never filled, and a personal-config `Last Updated` older than your newest knowledge context. It reports these as warnings so you can replace the copy with a pointer before it rots. The principle is a rule; the health check is the enforcement.

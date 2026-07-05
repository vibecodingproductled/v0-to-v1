# Anti-Patterns

These are the mistakes that erode the value of an AI harness over time. Each one looks reasonable in the moment but creates problems at scale.

## 1. The Monolith CLAUDE.md

**What it looks like**: A 500-line CLAUDE.md with methodology, procedures, templates, personal preferences, and project-specific context all in one file.

**Why it is tempting**: It is the easiest place to put things. It loads every session. "If I put it here, Claude will always know it."

**Why it fails**: Everything in CLAUDE.md consumes context window every session, even when it is irrelevant to the current task. A 500-line system prompt leaves less room for your actual conversation. Claude also struggles to prioritize when everything is presented as equally important.

**Fix**: CLAUDE.md under 100 lines. Methodology goes in skills. Procedures go in reference docs. Preferences go in CLAUDE.local.md. Context goes in knowledge contexts.

## 2. The Skill Graveyard

**What it looks like**: 50+ skill directories, most created months ago, many overlapping, no one remembers what half of them do.

**Why it is tempting**: Skills are easy to create. Every new methodology gets its own skill. "More is better."

**Why it fails**: Claude uses the skill description to decide when to activate it. With 50+ skills, descriptions overlap, and Claude either picks the wrong one or ignores all of them. Stale skills with outdated methodology actively mislead Claude.

**Fix**: Curate ruthlessly. 10-15 well-maintained skills beat 100 stale ones. Periodically review: if a skill has not been activated in a month and you do not miss it, delete it. When two skills overlap, merge them.

## 3. The Rule Echo

**What it looks like**: The same rule defined in CLAUDE.md ("write concisely"), in a rule file ("keep outputs under 500 words"), and in a skill ("3-minute read maximum, about 750 words"). Three definitions, three different thresholds.

**Why it is tempting**: You want to make sure Claude follows the rule, so you reinforce it in multiple places.

**Why it fails**: The definitions drift apart as you update one and forget the others. Claude sees conflicting instructions and picks unpredictably. Worse, you debug inconsistent behavior without realizing the root cause is three competing rules.

**Fix**: Define each rule once, in the narrowest scope that covers every case where it applies. A rule that should always hold goes in `.claude/rules/`. A rule that only applies to a specific task type goes in a skill. Never in both.

## 4. The Unbounded Context

**What it looks like**: A knowledge context CLAUDE.md with 200+ entries spanning 8 months. Every detail ever recorded, nothing archived.

**Why it is tempting**: "What if I need that decision from February?" So nothing gets removed.

**Why it fails**: The file becomes so long that it consumes significant context on load. Claude has to process months of history to find the 5 entries that matter today. Old entries reference decisions that have been superseded, creating confusion.

**Fix**: Archive entries older than 3 months to a separate `archive.md`. Keep the 10 most recent plus any that are still actively referenced. Add a one-line summary pointing to the archive.

## 5. The God Hook

**What it looks like**: A SessionStart hook that reads 10 files, checks 5 conditions, formats a detailed briefing, and takes 8 seconds to run.

**Why it is tempting**: "If I front-load all the context, Claude starts every session fully informed."

**Why it fails**: The hook runs before every session, including quick ones where you just want to ask a question. 8 seconds of startup latency kills the experience. The detailed briefing consumes context window on every session whether or not it is relevant.

**Fix**: Hooks should be fast (under 1 second) and focused. A SessionStart hook should check one or two conditions and output a short signal. Let Claude load detailed context on demand, not by default.

## 6. The Instruction Novel

**What it looks like**: Rules that are 100+ lines long, explaining every nuance, edge case, and exception.

**Why it is tempting**: You want Claude to handle every scenario correctly, so you document them all.

**Why it fails**: Long rules dilute the signal. Claude weighs the first and last lines more heavily; the middle gets lost. A 100-line rule about writing style is less effective than a 10-line rule that encodes the 3 patterns that matter most.

**Fix**: Each rule file under 30 lines. If a rule needs more explanation, the detailed version goes in a reference doc or a skill. The rule file contains the invariants; the supporting material lives elsewhere.

## 7. The Silent Failure

**What it looks like**: No health check, no session logging, no way to detect when the system is broken.

**Why it is tempting**: "The system works. Why add overhead?"

**Why it fails**: Everything is fine until it is not. A renamed rule file, a deleted skill, a broken hook. Without diagnostics, you only notice when Claude's output quality degrades, and by then you do not know what broke or when.

**Fix**: Add a session log (Stop hook) so you have a record of what Claude touches. Periodically run a structural check: do the expected directories exist? Do they contain files? Are there skills that have not been activated in 30 days?

## 8. The Copy-Paste Setup

**What it looks like**: Someone else's CLAUDE.md copied verbatim, with their role, their rules, their anti-patterns.

**Why it is tempting**: "They have a great setup. I'll use theirs."

**Why it fails**: A harness is personal. Their anti-patterns might not be yours. Their rules reflect their domain and their failure modes. Copying creates a setup that looks sophisticated but does not actually serve your work.

**Fix**: Start with a minimal template (this skill provides one). Add rules only when you discover what Claude gets wrong in your specific workflow. Let your harness grow from your corrections, not someone else's.

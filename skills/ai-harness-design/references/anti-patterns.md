# Anti-Patterns

These are the mistakes that erode the value of an AI harness over time. Each one looks reasonable in the moment but creates problems at scale.

## 1. The Monolith CLAUDE.md

**What it looks like**: A 500-line CLAUDE.md with methodology, procedures, templates, personal preferences, and project-specific context all in one file.

**Why it is tempting**: It is the easiest place to put things. It loads every session. "If I put it here, Claude will always know it."

**Why it fails**: Everything in CLAUDE.md consumes context window every session, even when it is irrelevant to the current task. A 500-line system prompt leaves less room for your actual conversation. Claude also struggles to prioritize when everything is presented as equally important.

**Fix**: CLAUDE.md under 100 lines. Methodology goes in skills. Procedures go in reference docs. Preferences go in CLAUDE.local.md. Context goes in knowledge contexts.

**The reference extraction technique**: When your CLAUDE.md is growing past the limit, look for blocks that are stable (rarely change) and informational (not needed every session). Folder structure maps, onboarding protocols, architectural overviews. Move each block to `.claude/reference/filename.md` and replace it with a one-line pointer: "Architecture and onboarding: @.claude/reference/architecture.md". Claude loads the reference on demand when the topic comes up, not on every session. One harness went from 95 lines to 50 by extracting three stable blocks, saving roughly 800 tokens per session.

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

## 8. The Duplicated Fact

**What it looks like**: The launch date, the team roster, or the project status written in your always-loaded personal config *and* in the initiative's knowledge context. Two copies of the same fact.

**Why it is tempting**: The personal config is always in context, so putting the fact there feels like it guarantees Claude always knows it. Keeping it in the context too feels thorough.

**Why it fails**: The two copies drift. The context gets updated every session; the personal config gets updated when you remember. Weeks later they disagree, Claude sees two conflicting truths, and picks unpredictably. You debug bad output without realizing a stale copy is the cause. This is the single most common way a mature harness rots.

**Fix**: One home per fact. The fact lives in exactly one place (usually the knowledge context); everywhere else stores a pointer, not a copy. Set a tie-break rule in advance ("if this file and a context disagree, the context wins"). De-duplicate by replacing the copy with a pointer, never by deleting history. See `single-source-of-truth.md`, and let `system-health-check` catch drift for you.

## 9. The Copy-Paste Setup

**What it looks like**: Someone else's CLAUDE.md copied verbatim, with their role, their rules, their anti-patterns.

**Why it is tempting**: "They have a great setup. I'll use theirs."

**Why it fails**: A harness is personal. Their anti-patterns might not be yours. Their rules reflect their domain and their failure modes. Copying creates a setup that looks sophisticated but does not actually serve your work.

**Fix**: Start with a minimal template (this skill provides one). Add rules only when you discover what Claude gets wrong in your specific workflow. Let your harness grow from your corrections, not someone else's.

## 10. The Self-Poisoning Metric

**What it looks like**: Your PostToolUse usage tracker fires on every file `Read` and checks if the path contains `SKILL.md`. The log says `system-health-check` is your most-used skill. It is not. Health-check reads every SKILL.md file during its sweep, and each read lands in the usage log.

**Why it is tempting**: Tracking file reads feels comprehensive. "If Claude reads a SKILL.md, it is using that skill."

**Why it fails**: The measurement instrument measures its own overhead. A quality gate that forces SKILL.md reads on every turn inflates every skill's count. A health-check sweep that reads 30 SKILL.md files produces 30 "activations" in the log. The evolution review trusts this data and keeps skills it should archive. Worse, the more you maintain your harness, the more contaminated the data becomes.

**Fix**: Track the *action*, not the preparation. Match on the `Skill` tool (the moment a human invokes a skill), not on `Read` (the moment Claude looks at a file). If you already have a contaminated log, start a fresh one after switching trackers. See the hooks guide for the corrected pattern.

## 11. The Protocol Triplication

**What it looks like**: Three files describe how to update a knowledge context. One is the "official protocol." Another is an agent that re-implements it with a slightly different section-mapping table. A third is a rule that summarizes it with subtly different wording. Claude reads all three and picks from whichever it saw last.

**Why it is tempting**: The protocol is important, so you put it in the reference doc (thorough), in the agent (so it knows what to do), and in the rule (so the main thread knows too). "Redundancy is safety."

**Why it fails**: The three copies drift as you update one and forget the others. In one harness, this created 937 lines across 3 files describing one behavior with 6 section-mapping differences. Claude's output varied depending on which file it weighted most in a given session. Debugging felt random until someone diffed all three.

**Fix**: One file owns the protocol. The agent references it instead of re-implementing it. The rule delegates to it instead of summarizing. When you need to change the protocol, you change one file. The pointer files stay stable because they contain no protocol logic to drift.

## 12. The Phantom Reference

**What it looks like**: An agent file references a skill that was renamed three months ago. A skill references an agent that was deleted. A CLAUDE.md links to a reference doc that was moved. Nobody notices because the references are in prose, not imports, and nothing checks them.

**Why it is tempting**: References accumulate naturally as you build the harness. Renaming or deleting something updates the thing itself but not the 4-9 files that reference it.

**Why it fails**: Claude follows the reference, finds nothing, and either silently ignores it (missing context) or hallucinates content for the missing file (wrong context). One harness had 9 references to a deleted agent across 4 files. The agent never existed in the active directory, but Claude kept trying to delegate to it.

**Fix**: A deterministic linter (bash + grep + find) that extracts every referenced skill, agent, and context name from your harness files, then checks whether the target path exists. Run it inside your health-check skill and as a pre-commit hook. The script is simple (under 100 lines of bash), but it catches drift that the LLM cannot because the LLM does not systematically resolve every reference on every check.

## 13. The Fire-Once Prompt

**What it looks like**: A Stop hook prompts Claude to propagate updates from one knowledge context to another. Claude offers to propagate, the user declines because they are in a hurry, and the intent is lost. Next session, neither Claude nor the user remembers.

**Why it is tempting**: A prompt hook is the simplest way to trigger cross-context communication. "Just ask Claude to do it at the end."

**Why it fails**: The prompt fires once, in one moment, and depends on the user saying "yes" right then. If they decline, close the session, or the conversation crashes, the propagation never happens. Over time, the roll-up context (the one that should accumulate updates from its sources) drifts behind because propagation is lossy.

**Fix**: Append the propagation intent to a durable queue file (JSONL, append-only). Surface pending items at the next session start. The user can act on them whenever they are ready. The intent persists until it is explicitly completed or dismissed. The Stop prompt still fires, but it writes to the queue before offering, so even a "no" does not lose the intent.

# Evolution Checklist

Growing a harness from scratch to production. Each phase builds on the previous one. Do not skip ahead; you need to discover your own failure modes before encoding solutions for them.

## Phase 1: Foundation (Day 1)

**Goal**: Claude knows who you are, what the project is, and where to put things.

- [ ] Create `CLAUDE.md` from the template (under 100 lines)
- [ ] Create `CLAUDE.local.md` with your profile and preferences (gitignored)
- [ ] Create `.claude/rules/` with your 3 most important rules
- [ ] Create `output/` directory for generated artifacts
- [ ] Verify: start a new session, ask Claude about the project. Does it know your name? Does it know where to save files?

**What you should notice**: Claude's responses are already more consistent. It addresses you correctly. Generated files go in `output/`.

**What to defer**: Skills, hooks, knowledge contexts. You do not know what you need yet.

## Phase 2: Methodology (Week 1)

**Goal**: Your most common tasks are backed by encoded methodology.

- [ ] Identify 2-3 tasks you do most often with Claude
- [ ] Create a skill for each in `.claude/skills/[name]/SKILL.md`
- [ ] Write descriptions that include specific trigger phrases
- [ ] Test: ask Claude to do each task. Does it find and apply the skill?
- [ ] Iterate on descriptions until activation is reliable

**What you should notice**: Tasks you do frequently are now more consistent. Claude applies your methodology instead of improvising.

**Diagnostic**: If a skill does not activate, the description is probably too generic. Make it more specific. Include the exact phrases you would use when requesting the task.

## Phase 3: Automation (Week 2)

**Goal**: Things that should always happen now happen automatically.

- [ ] Create `.claude/hooks/` directory
- [ ] Add a SessionStart hook that checks for CLAUDE.local.md
- [ ] Add a Stop hook that logs which files were modified (async)
- [ ] Configure both in `.claude/settings.json`
- [ ] Test: start a new session and verify the hook runs. End a session and check the log.

**What you should notice**: New team members get prompted to set up their preferences automatically. You have a record of what Claude touches in each session.

**What to defer**: Advanced hooks (staleness detection, context reminders). Get the basics working first.

## Phase 4: Knowledge Accumulation (Month 1)

**Goal**: Your main initiative has a living memory that compounds across sessions.

- [ ] Create a knowledge context folder for your primary initiative
- [ ] Add a CLAUDE.md following the template in the knowledge contexts guide
- [ ] Work in that context for a week, updating CLAUDE.md after each session
- [ ] After a week: start a fresh session in the context. Does Claude understand the history?

**What you should notice**: Sessions start faster because Claude reads the accumulated context. You stop repeating yourself. Decisions from last week inform this week's work automatically.

**Diagnostic**: If the knowledge context is not helping, check: are you actually updating it? An empty CLAUDE.md provides no value. Even one decision entry per session adds up quickly.

## Phase 5: Refinement (Month 2)

**Goal**: The system learns from your corrections and prunes what it does not use.

- [ ] Review Claude's auto-memory: what preferences has it learned? Are they accurate?
- [ ] Review your rules: are there corrections you keep making that should be encoded?
- [ ] Review your skills: are any unused? Do any overlap? Merge or delete.
- [ ] Add 1-2 new rules based on repeated corrections
- [ ] Archive old entries in knowledge contexts that exceed 30 entries

**What you should notice**: Claude rarely makes the same mistake twice. The system is adapting to you rather than you adapting to it.

## Phase 6: Maturity (Month 3+)

**Goal**: The system maintains itself and evolves intentionally.

- [ ] Run a monthly "health check": directories exist, files are not empty, skills are not stale
- [ ] Review the session log for patterns: where does your time go? What should be automated?
- [ ] Consider adding a Stop prompt hook for knowledge context update reminders
- [ ] Consider adding cross-context connections as your initiative portfolio grows
- [ ] If session log exceeds 500 entries, rotate: keep last 90 days, archive the rest

**What you should notice**: You spend less time on setup and more time on substance. New team members onboard faster. The harness feels invisible because it just works.

## Phase 7: Self-Healing (Month 6+)

**Goal**: The system detects its own maintenance needs and prompts you to act.

- [ ] Add a PostToolUse hook that logs skill activations to a usage file (see hooks guide)
- [ ] Add a SessionStart hook that rotates the session log when it exceeds threshold
- [ ] Add a SessionStart hook that prompts for a system audit when enough usage data accumulates
- [ ] Review the usage data: which skills are never activated? Archive or merge them
- [ ] Review the session log: what patterns emerge? Which tasks should be automated with a new skill or hook?
- [ ] Archive knowledge context entries older than 90 days (or automate this with a rule)

**What you should notice**: The system tells you what needs attention before you discover it by accident. Skill usage tracking reveals dead skills. Log rotation keeps data files lean. Audit prompts close the feedback loop: data accumulates, you review, you adapt.

**Diagnostic**: If you keep discovering stale skills, broken references, or bloated context files through accident rather than a prompt, your self-healing layer is incomplete.

**The feedback loop**: PostToolUse tracking generates data. SessionStart audit hooks tell you when there is enough data to act on. You review and adapt. The harness evolves intentionally, not by drift.

## Phase 8: Deterministic Enforcement (Month 9+)

**Goal**: Structural invariants are checked by a script, not by the LLM.

The self-healing layer (Phase 7) runs through the LLM: it reads logs and narrates what is wrong. That works for qualitative problems (a skill description is vague, a context is stale). It fails for structural invariants: does every referenced skill exist? Does every folder match its frontmatter name? Does every cross-context connection target a real directory? The LLM checks these sometimes, inconsistently. A script checks them always, the same way.

- [ ] Build a validation script (bash + grep + find, no LLM, under 100 lines) that checks:
  - Every skill/agent name referenced in harness files resolves to an existing path
  - Folder names match frontmatter `name:` fields
  - Cross-context connection targets exist
  - No skill appears in two locations with divergent content
- [ ] Wire it into `system-health-check` as the mandatory first step: run the script, report its output, then proceed with LLM-based checks
- [ ] Wire it as a git pre-commit hook (warns, never blocks; see the hooks guide for the pattern)
- [ ] Add a durable queue for cross-context propagation intent: a JSONL file where the Stop hook appends propagation needs, and the SessionStart hook surfaces pending items
- [ ] Review the durable queue after a month of use: are items being acted on, or accumulating indefinitely?

**What you should notice**: Broken references, phantom names, and naming drift are caught by the script before you discover them by accident. The health-check goes from "Claude narrates what looks wrong" to "the script reports what is wrong, then Claude interprets the results." Pre-commit warnings catch drift at the moment you introduce it.

**Diagnostic**: If you discover a broken reference manually that the validator did not catch, the script has a gap. Add the check and re-run.

## Signals that you are on track

At each phase, look for these signals:

| Phase | Signal | Red flag |
|-------|--------|----------|
| 1 | Claude addresses you by name and saves files to `output/` | Claude puts files in random places |
| 2 | Common tasks produce consistent, methodology-backed results | Claude improvises differently each time |
| 3 | Hooks run without you noticing. New teammates get prompted to set up | Hooks are slow, break, or produce errors |
| 4 | You stop re-explaining context in ongoing initiatives | You still repeat the same background every session |
| 5 | Claude rarely makes the same mistake twice | The same corrections keep appearing |
| 6 | The system feels effortless. You think about your work, not the system | You spend time debugging the harness instead of using it |
| 7 | The system surfaces its own maintenance needs before you notice | You discover stale skills or bloated files by accident |
| 8 | Broken references and naming drift are caught by a script, not by accident | You discover a phantom reference manually that the validator should have caught |

## When to stop adding

The harness is done when it is invisible. If you are spending more time maintaining the harness than it saves you, you have over-engineered it. The goal is a system that fades into the background, not one that demands attention.

Common signs of over-engineering:
- More than 15 skills (unless your domain genuinely has 15 distinct methodologies)
- Rules longer than 30 lines each
- Hooks that take more than 3 seconds total to run, or more than 3 hooks doing redundant checks on the same event
- Knowledge contexts for one-off projects that will never have a second session
- A CLAUDE.md that exceeds 100 lines despite having rules, skills, and knowledge contexts to offload to

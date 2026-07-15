---
name: discovery-interview
description: |
  Bias-aware discovery interview processing. Turn raw interview notes or transcripts into
  structured writeups, propagate evidence to a problem framework, and score interview
  technique with persistent tracking. Use when the user shares interview notes or a
  transcript, or asks to "process an interview", "write up an interview", "score my
  interview", or wants "interview feedback". Do NOT use for designing interview scripts or
  synthesizing findings across many interviews; that is jtbd-discovery.
---

# Discovery Interview

A bias-aware system for running and processing discovery interviews. Built from experience running 60+ interviews for an AI product in a high-stakes domain.

This skill is the operational counterpart to recognizing your own bias. Knowing you are biased is step one. This skill is step two: a systematic protocol that counteracts bias before, during, and after every interview, with persistent tracking so you can measure whether you are actually improving.

## When to use

- Processing raw interview notes into a structured writeup
- Propagating new evidence to your problem framework
- Scoring your interview technique and tracking improvement
- Preparing for an interview with assumption mapping
- Reflecting on how new evidence challenges or confirms your hypotheses

## Complements

- **jtbd-discovery**: Use that skill for structuring problems (trunk-branch methodology, evidence thresholds, synthesis). Use THIS skill for conducting and processing the interviews that generate that evidence.

## Phase 0: SETUP (first run only)

Configuration and tracker state live in the user's project at `.claude/discovery-interview/`, never inside this skill's directory. Skill directories may be read-only (plugin installs, shared repos), and user state committed into a skill pollutes it for everyone else.

On first invocation, check whether `.claude/discovery-interview/config.md` exists in the project. If not, walk the user through setup:

1. **Notes location**: "Where do your interview notes live?"
   - A directory path (e.g., `research/interviews/`)
   - "I'll paste them in chat each time"

2. **Publishing destination**: "Where do you publish writeups?"
   - Confluence (ask for cloud URL, space key, parent page ID)
   - Notion (ask for database URL)
   - Local markdown (ask for output directory)
   - Other (ask for details)

3. **Problem framework**: "Do you have an existing problem framework?"
   - Yes, trunk-branch structure (ask for file path or wiki page)
   - Yes, another format (OKRs, hypothesis board, opportunity solution tree)
   - No, I'll create one (point them to `jtbd-discovery` skill)

4. **Interview structure**: "How are your interviews structured?"
   - Number of phases/acts and their names
   - Which phases are "unprompted" (no stimulus shown) vs. "prompted" (stimulus material shown)
   - This determines how evidence is weighted in later phases

Save answers to `.claude/discovery-interview/config.md` in the project (create the directory if needed). The user can edit this file directly to update their setup.

On subsequent invocations, read that file and skip to Phase 1.

## Phase 1: LOCATE

Find the interview notes:
1. Scan the configured notes directory for recent files (sort by modification date).
2. Present the most recent unprocessed file. Ask user to confirm or specify a different one.
3. **Fallback**: If no file found, ask user to paste notes or transcript directly in chat.
4. Read the full input.

## Phase 2: TEMPLATE

Load the writeup template:
1. If the user has a custom template configured, use that.
2. Otherwise, use the bundled [references/writeup-template.md](references/writeup-template.md).
3. If the user publishes to a wiki with existing writeups, optionally fetch the most recent one to match evolving format.

## Phase 3: GENERATE

Transform raw notes into a structured writeup following the template. Standard sections:

- **Session Metadata**: participant (role, not full name in published version), date, duration, format, interviewer
- **Participant Profile**: role, organization type, specialization, team size, location
- **Tools & Workflow**: tools mentioned, current workflow for the problem space
- **Session Notes**: narrative organized by interview phase/act (see structure note below)
- **Key Quotes**: table with 8-10 strongest direct quotes, timestamps, and topic tags
- **Bias Assessment**: the signal contamination table (see below)
- **Hypothesis Validation**: what confirms vs. what challenges existing hypotheses

Save locally. Show the user for review before publishing. Wait for approval.

### Session Notes structure

Organize notes by the interview phases defined in `config.md`:

- **Unprompted phases**: What surfaced before any framework, stimulus, or prototype was shown. Flag these as highest-signal sections.
- **Prompted phases**: What surfaced after showing material. Note which elements the participant self-selected first, which they confirmed vs. dismissed.
- **Close**: Final reflections, anything they added unprompted after the structured portion.

### Bias Assessment table

After Key Quotes, add a table tracking signal contamination:

| Signal | Surfaced unprompted? | Prompted response? | Weight |
|--------|---------------------|-------------------|--------|
| _e.g., "data is scattered"_ | Yes, described specific incident | Confirmed when shown | HIGH (unprompted + confirmed) |
| _e.g., "can't compare versions"_ | No | "Yeah that's annoying" | LOW (only surfaced when prompted) |

Weight rules:
- **HIGH**: Surfaced unprompted AND confirmed when prompted
- **MEDIUM**: Surfaced unprompted OR strongly confirmed when prompted (not both)
- **LOW**: Only surfaced when prompted; may be acquiescence bias
- **DISCONFIRMED**: Participant actively pushed back or said "that's not how I work"

### Quality rules

- Session Notes must be narrative, not bullet lists. Capture the story, not just facts.
- Key Quotes must be direct quotes, not paraphrases.
- Hypothesis Validation must separately assess what was confirmed unprompted vs. what was only confirmed when prompted. Unprompted confirmation is stronger evidence.

## Phase 4: PUBLISH

Push to the configured destination:

**If Confluence**: Create child page under the configured parent. Use the writeup content. Update any registry table on the parent page with one row for the new participant.

**If Notion**: Create new entry in the configured database with the writeup content.

**If local markdown**: Save to the configured output directory with a descriptive filename (e.g., `writeup-role-date.md`).

Report the location to the user.

## Phase 5: UPDATE FRAMEWORK

Add new evidence to the user's problem framework:

1. Read the current framework (file path or wiki page from `config.md`).
2. For each branch/hypothesis in the framework: if the interview contains a relevant incident, add one evidence row with the signal weight from the Bias Assessment.
3. Skip any branch where no new evidence applies.
4. If evidence was DISCONFIRMED, add it as counter-evidence. This is as valuable as confirming evidence.

**Signal weighting**: Evidence from unprompted phases carries more weight than evidence from prompted phases. Note the source phase in the evidence description.

**Minimal update principle**: One row per branch per interview. If in doubt, skip. The user can always add manually.

## Phase 6: REFLECT

Present in-chat reflection on framework evolution. Do NOT auto-update any files or wiki pages. This is advisory only.

**Disconfirmation-first rule**: Start every reflection section with what this interview challenged or contradicted in the existing framework, BEFORE discussing what it confirmed. If nothing was challenged, say so explicitly.

### 6a. New problems

Does any evidence suggest a new struggle not covered by existing framework entries?
- Apply independence test: can this struggle exist if all other entries were solved?
- Apply cross-cutting test: does it appear across 3+ existing entries?
- Evidence standard: 2+ independent sources with specific incidents. Below that, flag as "emerging signal."

### 6b. New root causes

Does any evidence suggest a new causal factor under an existing struggle?
- Apply MECE test: distinct from existing causes?
- Same evidence standard.

### 6c. Experiment seeds

For each framework entry that received new evidence, assess whether a new experiment is worth testing:
- **Root cause**: one sentence
- **New evidence from this interview**: specific quotes or incidents
- **Draft hypothesis**: belief statement (no if/should/could)
- **Why now**: what changed that makes this worth testing?

## Phase 7: FEEDBACK

Score interview technique and save to the persistent tracker.

### 7a. Scorecard

Rate each dimension 1-10. Compare against prior interviews in the feedback tracker.

| Dimension | What "10" looks like |
|-----------|---------------------|
| **Opening** | States purpose, sets expectations, grounds in a specific real project |
| **Question quality** | Open-ended, single-barreled, invites narrative ("Walk me through...") |
| **Follow-up depth** | Every workaround or pain point gets a "why" probe |
| **Listening ratio** | Interviewer talks ≤20% of the time |
| **Leading question avoidance** | No yes/no frames, no assumptions embedded, no mid-flow rephrasing that narrows the participant's next answer |
| **Tangent management** | Redirects within ~90 seconds using bridge phrases |
| **Hypothesis testing** | Pre-session assumptions map to specific questions; post-interview assessment of which survived |
| **Pain quantification** | Gets specific numbers for time, cost, or frequency of the problem |
| **Closing technique** | Mirror-back at end of each phase, catch-all "what did I miss?", follow-up commitment |
| **Real-world grounding** | Every answer anchored to a specific project or incident, no hypotheticals accepted |
| **Confirmation bias avoidance** | Unprompted phases contain zero framework references; disconfirming signals are probed, not dismissed |

### 7b. Trend analysis

Compare this interview to:
- **Your best session** (highest average score in the tracker)
- **Your rolling average** (last 5 interviews)
- **Your worst dimension** (the one that needs the most work)

Flag whether you are improving, plateauing, or regressing, and on which specific dimension.

### 7c. Anti-patterns to flag

| Anti-pattern | Fix |
|---|---|
| Accepting surface answers ("sometimes yes, sometimes no") | "What determines when there is one vs. when there isn't?" |
| Compound questions ("your role and how does a typical week look?") | Ask one question. Wait. Ask the next. |
| Filling silence with rephrasing | Ask once. Count to 7 silently. |
| Moving on after pain without probing root cause | "Why has it stayed that way?" |
| Rushed close under time pressure | Front-load critical questions. Close is for validation, not new topics. |
| Leading via embedded assumption ("how much time were you wasting?") | "How does this process affect your time?" |
| Mid-flow rephrasing that narrows ("Am I reading this correctly that...") | Ask "What didn't work about it?" mid-flow. Save synthesis for the phase close. |
| Accepting unqualified enthusiasm | Push: "What would make you NOT use something like this?" |
| Dismissing disconfirmation (participant pushes back, you move on) | Probe deeper: "How does it work for you?" Their correction IS the data. |

### 7d. One concrete suggestion

End with the single highest-leverage improvement for the next interview:
- **The habit**: What to do differently (one sentence)
- **When it triggers**: The moment in the interview that should cue it
- **Why it matters**: What insight it unlocks

### 7e. Save to tracker

Append this interview's scores to the persistent feedback tracker at `.claude/discovery-interview/feedback-tracker.md` in the project. On first use, create it from [references/feedback-tracker-template.md](references/feedback-tracker-template.md). Never append rows to the template inside the skill directory.

The tracker accumulates across all interviews so you can see your progression over 5, 10, 20+ sessions.

## Bias Mitigation Protocol

This protocol is the core of the skill. It runs before, during, and after every interview.

### Before the interview

1. **Pre-register predictions**: Write down what you expect to hear. Include kill signals (conditions that would invalidate your hypothesis). Seal these; review only after the interview.

2. **Assumption mapping**: 3 assumptions about this specific participant. For each:
   - The assumption itself
   - A "destroy question" designed to kill it
   - A "dead if they say..." condition

3. **Mindset reset**: "You know nothing about how this specific person works. Your prior interviews are a hypothesis, not a fact."

### During the interview

| Rule | Why |
|---|---|
| Talk ≤20% of the time (hard ceiling: 25%) | You will want to explain and share. Do not. |
| Zero framework language | Never use your own terminology. These are your words, not theirs. |
| Never reference prior interviews | Social proof biases their response toward agreement. |
| Do not explain the prototype | "Tell me what you see" not "this does X." Confusion is data. |
| Count to 7 after every question | Longer than feels natural. The second thought is often the real answer. |
| Count to 10 when they say "I think that's it" | The answer after "that's it" is frequently the most honest one. |
| Ask the counter-question at every phase | "What would make you NOT [do this]?" |

### After the interview

1. Score assumption mapping (survived / killed / inconclusive) BEFORE writing the narrative. Writing the narrative first rationalizes assumptions into the story.
2. Complete the Bias Assessment table.
3. Run Phase 7 (Feedback) to score your own technique.

## Anti-patterns

| Anti-Pattern | Instead |
|---|---|
| Generating a generic writeup without checking the template | Always load the template first |
| Auto-updating the problem framework with speculative entries | Present as in-chat reflection only; let the user decide |
| Bloating evidence tables with multiple rows from one interview | One row per branch per interview, maximum |
| Skipping hypothesis validation in the writeup | Always include what confirms AND what challenges |
| Generic interview feedback ("good job") | Specific, cite concrete moments from the notes |
| Treating all evidence equally regardless of when it surfaced | Distinguish unprompted vs. prompted evidence; weight accordingly |
| Reflecting only on what confirmed the framework | Start every reflection with what was challenged BEFORE what was confirmed |
| Skipping the feedback tracker save | Always append scores; the longitudinal view is where the value compounds |

## References

- [references/writeup-template.md](references/writeup-template.md): Structured writeup template
- [references/framework-update-template.md](references/framework-update-template.md): Problem framework template for evidence propagation
- [references/feedback-tracker-template.md](references/feedback-tracker-template.md): Persistent interviewer scorecard tracker
- `jtbd-discovery` skill (in this repo): Trunk-branch problem framing and synthesis methodology

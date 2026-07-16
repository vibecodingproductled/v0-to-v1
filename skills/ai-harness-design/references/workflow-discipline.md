# Workflow discipline: how to drive the harness

Structure (the layers) determines what the harness *can* do. Discipline (this guide) determines what it *actually* does, session after session. These patterns are the practitioner consensus, ordered by how much each one matters.

## The loop: research, plan, execute, review, ship

Every non-trivial task runs the same loop. Let the agent research first (read-only exploration of the files, data, or code involved). Have it propose a plan and gate on your approval before anything is produced or changed. Execute against the approved plan. Review the output against a verification mechanism, not against vibes. Then ship. The specific tooling changes constantly; the loop is the part to bet on.

## Plan mode as the default gate

For anything beyond a quick question, start in plan mode (or its equivalent: an explicit "propose before you touch anything" instruction). The agent explores and proposes; nothing is created or edited until you approve. Two reasons this earns its friction:

- The plan is where misunderstandings surface cheaply. A wrong plan costs one read; a wrong execution costs the cleanup.
- For PMs exploring a codebase ("can we build this?"), plan mode is the safe way to let the agent read everything and change nothing.

Treat plan approval as a convenience gate, not a security boundary. It structures the workflow; it does not enforce permissions.

## Checkpoint relentlessly

Commit (or snapshot) at every stable point, and clear the conversation between unrelated tasks. Frequent checkpoints make any wrong turn cheap to revert, and a cleared context keeps the kitchen-sink session (three unrelated tasks sharing one degrading context) from becoming your default working mode. The rule of thumb: if you would describe the next task with a different noun, it gets a fresh session.

## Verification: give every artifact a way to fail

An agent with a validation mechanism it can run against its own work is reliably better than one without. For code that means tests. For PM artifacts the equivalents are:

- **Pass/fail evals** per skill (this repo ships them in each skill's `evals/` folder). Binary on purpose: graders cannot reliably tell a 3 from a 4, but they can tell pass from fail.
- **Rubrics and checklists** applied by a fresh context, not by the context that wrote the draft.
- **The reader test**: a fresh session answers factual questions about the document; wrong answers locate the unclear sections.

The discipline that makes all of this work: never ship an artifact you cannot explain and defend yourself. The harness drafts; you own.

## Doer-verifier and the panel

For high-stakes artifacts, separate the producing context from the reviewing context:

- **Doer-verifier**: one agent produces, a second agent with fresh context and a skeptical prompt tries to find what is wrong. The verifier must not see the doer's reasoning, only the artifact.
- **The panel**: three reviewers with different mandates (the skeptical engineer, the accountable executive, the user researcher) critique in parallel, blind to each other. Persona files (see `personas-guide.md`) make panel reviewers specific instead of generic. The panel catches what any single reviewer misses, and disagreement between reviewers is itself information.

Use these for the artifacts where being wrong is expensive: strategy docs, shaped specs, anything pre-registered. They are overkill for routine output, and running them on everything dulls their signal.

## Chained workflows: encode the ritual

When the same multi-skill sequence recurs weekly (synthesize, then update the framework, then draft the stakeholder update), encode the chain once as a workflow command instead of re-prompting it from memory. The trigger for encoding is the same as for skills: explained it three times means it belongs in a file.

## Escalate complexity only when the simple version fails

The strongest cross-source warning: find the simplest thing that works, and only add machinery when it demonstrably fails. A single well-contexted session beats a subagent fleet for most PM work. Subagents earn their place for research isolation, parallel processing of many similar items, and blind review; heavier orchestration is a specialist tool, not a default. If the simple loop above is not producing quality, the fix is almost always context (a thin CLAUDE.md, a stale skill, tool bloat), not more agents.

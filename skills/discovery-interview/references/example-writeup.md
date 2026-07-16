# Example: a finished interview writeup

What Phase 3 output looks like. Shapes real, content invented. Note what makes this a *bias-aware* writeup rather than a summary: the unprompted/prompted split, the signal table, and the disconfirmation given equal billing.

## Session Metadata

Participant: Senior architect, mid-size residential firm (name withheld in published version). Date: [date]. Duration: 52 min. Format: remote, recorded. Interviewer: [PM].

## Participant Profile

12 years in practice, leads concept design on 3-5 residential projects a year, team of four. Describes herself as "the person who says no to the software the juniors want."

## Tools & Workflow

Concept work in a mix of CAD and hand sketches; feasibility checks in spreadsheets maintained by a colleague. Has trialed two AI layout tools; neither survived past one project.

## Session Notes

### Act 1 (unprompted): the last project that hurt

She walked through a 40-unit infill project where the client rejected the concept twice. The story she told without prompting was not about design quality but about defensibility: "Both times I lost the room because I couldn't show why the alternative they liked was worse. I knew. I just couldn't show it." She had rebuilt her own rejected option that evening to produce a comparison, by hand, at 11pm.

### Act 2 (prompted): reaction to the prototype

Shown the layout assistant, she self-selected the constraint panel first, ignored the generation button for four minutes, and asked "what does it do when it can't satisfy this?" When the facilitator explained instead of letting her find out, she visibly disengaged (interviewer error, logged in Phase 7).

### Close

Unprompted addition after the formal end: "If it kept a record of what we decided and why, I'd use it for that alone."

## Key Quotes

| Quote | Timestamp | Topic |
|---|---|---|
| "I lost the room because I couldn't show why the alternative was worse." | 00:14 | Decision justification |
| "I check everything now. Once burned." | 00:31 | Trust in generated output |
| "What does it do when it can't satisfy this?" | 00:38 | Constraint transparency |
| "I'd use it for the record of what we decided alone." | 00:50 | Decision trail |

## Bias Assessment

| Signal | Surfaced unprompted? | Prompted response? | Weight |
|---|---|---|---|
| Can't defend decisions to clients | Yes, with a specific 11pm incident | Confirmed on prototype | HIGH |
| Distrust of generated layouts | Yes ("once burned") | Confirmed | HIGH |
| Wants constraint transparency | No | Strong, self-selected first | MEDIUM |
| Wants faster generation | No | Mild agreement only | LOW |

## Hypothesis Validation

Confirmed unprompted: the defensibility struggle (hypothesis 1) with a concrete incident. Challenged: the assumption that generation speed is a top-three concern for this segment; she never raised it and shrugged when prompted. This is counter-evidence and goes to the framework as such.

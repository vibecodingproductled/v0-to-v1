# Example: a strategy doc that follows the hard rules

An invented but complete strategy doc, 428 words, so you can see the rules applied rather than described: leads with the insight, states trade-offs, no glossy phrasing, no em dashes, every section earns its place. Product and data are fictional.

---

## Concept-stage decision records: our next bet

**Why this, why now.** Discovery across two interview rounds found the same struggle in both of our segments: architects lose client approval not because their designs are worse but because the reasoning behind the design is not an artifact they can show. Meanwhile our generation features fight for trust one output at a time. A decision record that captures what was tried, what was rejected, and why turns our biggest trust liability into the thing users show their clients.

**The bet.** We will attach a decision trail to every generated proposal: constraints honored, alternatives considered, and the stated reason a direction was dropped. We believe this lifts proposal reuse (proposals used as a starting point rather than discarded) from its current 22% to 35% within two release cycles.

**What we are explicitly not doing.** Not building client-facing presentation views this cycle; the record is for the designer first. Not capturing free-form design intent; only decisions the system already sees. Both cut scope roughly in half and both are reversible later.

**Trade-offs.** We are trading generation breadth for defensibility depth: the two engineers who would have built the next generation mode build this instead. If reuse is gated by output quality rather than trust, this bet underperforms and the generation-mode path was the better use of the cycle. The discovery evidence says trust is the gate, and the falsification below tells us quickly if that is wrong.

**How we will know we are wrong.** If proposal reuse does not reach 28% by the mid-cycle check, or if fewer than a third of active users open the decision trail at all, we stop and re-scope. Pre-registered on [date] with the growth team.

**Next steps.** Design spike on the record format (1 week). Instrument reuse and trail-open events before the feature ships, so the baseline is real. Pilot with five design partners from the discovery panel.

---

## Why this example passes

Word budget: 428 of 750. Leads with the learned insight, not the interview inventory. The recommendation is stated, not offered as a menu. The non-goals and trade-offs are explicit, including the condition under which the bet was the wrong call. Falsification criteria are pre-registered and numeric. And it reads like a person: no momentum being built, nothing anyone is excited to share.

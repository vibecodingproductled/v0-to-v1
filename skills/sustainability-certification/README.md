# Sustainability Certification Agents

Two AI agents that act as early-stage LEED and BREEAM certification consultants for architects. They translate certification goals into exact, room-level design requirements.

## The problem

An architect targeting LEED Gold or BREEAM Excellent needs to know: what daylight factor do my classrooms need? What ventilation rate for meeting rooms? What U-value for the envelope? These numbers live in dense certification manuals, cross-reference multiple standards (ASHRAE, BS EN, IES), and vary by room type, building type, and certification level.

A general-purpose LLM will give you vague advice ("aim for good daylight") or confidently hallucinate thresholds. Wrong certification advice costs real money and failed certifications.

## The solution

Each agent is grounded in a structured, version-locked knowledge base where every credit is encoded as JSON with exact thresholds, units, and source citations. A deterministic scoring engine handles all the math. The LLM reasons, explains, and knows when to say "I don't have this threshold, check with your assessor."

### Architecture

```
Architect provides:              Agent returns:
  building type + location         room-level requirements
  room schedule                    exact metrics + thresholds
  target certification level       referenced standards
  constraints                      credit strategy + trade-offs
         |                                  |
         v                                  v
  [Project Intake]  -->  [Knowledge Base]  -->  [Scoring Engine]
                              (JSON)              (Python)
                                |
                                v
                         [LLM Reasoning]
                    translates, explains, flags gaps
```

**The LLM never does the math.** It reads the knowledge base, calls the scoring engine, and translates results into actionable guidance for the architect. Every number cites its source.

## Quick start

1. Clone this repo
2. Open your project folder in Claude Code
3. Ask: "Using the agent at `skills/sustainability-certification/agents/leed-specialist.md`, assess my office building in Oslo for LEED Gold"

## Agents

| Agent | File | Covers |
|-------|------|--------|
| LEED Specialist | `agents/leed-specialist.md` | LEED BD+C v4.1 New Construction |
| BREEAM Specialist | `agents/breeam-specialist.md` | BREEAM New Construction 2023 |

## Example output

```
CLASSROOMS (12 rooms, ~65 sqm each)

  Daylight (Hea 01):
    - Average daylight factor >= 3.0% on working plane at 850mm [BS EN 17037]
    - Uniformity ratio >= 0.3 [BS EN 17037]
    - View of sky from desk height through vision glazing
    - Artificial lighting UGR <= 19 [BS EN 12464-1]
    Minimum standard: 2 credits required for Excellent
    Confidence: High | Source: Hea 01, BREEAM NC 2023

  Ventilation (Hea 02):
    - Fresh air rate >= 8 L/s per person [BS EN 16798-1, Category II]
    - CO2 < 1000 ppm above outdoor level
    Confidence: High | Source: Hea 02, BREEAM NC 2023
```

## Knowledge base

Credits are stored as structured JSON, not prose. Each credit record includes:
- Exact metric and threshold per room type
- Unit of measurement
- Referenced standard (ASHRAE, BS EN, IES, etc.)
- Credit/issue ID and manual version
- Minimum standards for higher ratings (BREEAM)
- Prerequisite dependencies (LEED)

## Scoring

- **LEED**: additive points. 110 possible. Certified (40), Silver (50), Gold (60), Platinum (80). All prerequisites mandatory.
- **BREEAM**: weighted percentage. Category scores weighted and summed. Pass (30%), Good (45%), Very Good (55%), Excellent (70%), Outstanding (85%). Minimum standards per rating level.

## Limitations

- Covers credits with quantitative requirements. Qualitative credits noted but not detailed.
- Built from publicly available summaries, not full copyrighted manuals.
- LEED v4.1 and BREEAM NC 2023 only.
- Decision-support for early design. Not a replacement for licensed LEED APs, BREEAM Assessors, or formal certification review.

## Contributing

To improve thresholds or add credits: edit the JSON files in `knowledge/` following the schema in `knowledge/schemas/credit.json`. If you are a licensed LEED AP or BREEAM Assessor and spot an error, please open an issue.

## License

MIT

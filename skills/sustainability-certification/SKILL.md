---
name: sustainability-certification
description: Two AI agents (LEED specialist + BREEAM specialist) that act as early-stage certification consultants for architects. Given a building program and a target certification level, they return exact room-level requirements (lux values, air change rates, U-values, water flow rates) with source citations. Clone and run in Claude Code. No platform dependency.
metadata:
  version: 1.0.0
  author: Daniel Gameiro
---

# Sustainability Certification Agents

Two specialist agents that translate certification goals into concrete, measurable design requirements for architects at early design stage.

## What these agents do

An architect says "I want BREEAM Excellent for this school" and the agent tells them exactly what daylight factor each classroom needs, what ventilation rates the HVAC must deliver, what acoustic performance to target. Every number cites the exact credit, manual version, and referenced standard.

## What these agents don't do

They are not certification management systems, scoring dashboards, or submission tools. They do not replace licensed LEED APs or BREEAM Assessors. They give architects the numbers they need to start designing right.

## Available agents

- **LEED Specialist** (`agents/leed-specialist.md`): LEED BD+C v4.1 New Construction
- **BREEAM Specialist** (`agents/breeam-specialist.md`): BREEAM New Construction 2023

## How to use

1. Open your project in Claude Code
2. Reference the agent: "Use the LEED specialist agent at `agents/leed-specialist.md`"
3. Provide your building program: building type, location, room schedule, target level
4. Get room-level requirements with exact metrics, thresholds, and citations

### Example prompts

- "I'm designing a 22,000 sqm office in Oslo. We want LEED Gold. What requirements do my spaces need to hit?"
- "What daylight requirements do my classrooms need for BREEAM Excellent?"
- "What ventilation rates does LEED require for open plan offices?"
- "Compare the daylight requirements between LEED Gold and BREEAM Excellent for my office building."

## Architecture

The agents follow a neuro-symbolic pattern:
- **LLM** (the agent): reasons about the project, translates requirements into plain language, identifies conflicts, asks follow-up questions, knows when to abstain
- **Deterministic engine** (`engine/`): does all the math (scoring, prerequisite checking, credit applicability). The LLM never calculates points or scores.
- **Structured knowledge base** (`knowledge/`): every credit encoded as JSON with exact thresholds, units, and source references. The LLM reads this, never invents requirements.

### Why not just ask Claude about LEED/BREEAM?

A general LLM will:
- Mix LEED v4 with v4.1 thresholds
- Conflate BREEAM UK with International requirements
- Hallucinate credit numbers or invent thresholds
- Give vague advice ("aim for good daylight") instead of exact metrics

These agents ground every answer in a structured, version-locked knowledge base. Every threshold is citable. When the agent doesn't know, it says so instead of guessing.

## File structure

```
agents/           Claude Code agent definitions
knowledge/        Structured credit data (JSON)
  schemas/        JSON Schema for project and credit records
  leed/           LEED BD+C v4.1 credits and scoring
  breeam/         BREEAM NC 2023 issues and weighting
engine/           Deterministic scoring logic (Python)
eval/             Test cases and evaluation harness
examples/         Worked examples
```

## Extending

To add credits: edit the JSON files in `knowledge/`. Follow the schema in `knowledge/schemas/credit.json`.

To add a new certification system: create a new folder in `knowledge/`, add a scoring module in `engine/`, and create an agent definition in `agents/`.

## Limitations

- Covers the credits with quantitative, room-level requirements. Qualitative credits (Innovation, some Site credits) are noted but not detailed.
- Knowledge base built from publicly available summaries and referenced standards. Not the full copyrighted manuals.
- LEED v4.1 and BREEAM NC 2023 only. Other versions and schemes are not covered.
- Decision-support for architects, not a replacement for licensed professionals or formal review processes.

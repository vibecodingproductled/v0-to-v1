"""
Shared scoring interface for certification assessment.

The LLM never does the math. This module does.
It loads the credit knowledge base, matches credits to room types,
computes achievable points, and checks prerequisites.

Usage:
    from engine.scoring import assess_project
    from engine.leed_scoring import LEEDScorer
    from engine.breeam_scoring import BREEAMScorer

    result = assess_project(project_data, LEEDScorer())
"""

import json
import os
from pathlib import Path
from abc import ABC, abstractmethod


KNOWLEDGE_DIR = Path(__file__).parent.parent / "knowledge"


def load_json(path: str) -> dict | list:
    with open(path, "r") as f:
        return json.load(f)


class CertificationScorer(ABC):
    """Base class for certification scoring. LEED and BREEAM implement this."""

    @abstractmethod
    def load_credits(self) -> list[dict]:
        """Load all credits/issues from the knowledge base."""
        pass

    @abstractmethod
    def load_scoring(self) -> dict:
        """Load scoring thresholds and certification levels."""
        pass

    @abstractmethod
    def compute_score(self, achieved_credits: list[dict]) -> dict:
        """Compute total score and certification level from achieved credits."""
        pass

    @abstractmethod
    def check_prerequisites(self, project: dict) -> list[dict]:
        """Return list of prerequisites with pass/fail status."""
        pass

    def get_applicable_credits(self, project: dict) -> list[dict]:
        """Return credits applicable to this project's room types."""
        credits = self.load_credits()
        rooms = project.get("rooms", [])
        room_types = {r["type"] for r in rooms}
        room_types.add("all_occupied")
        room_types.add("regularly_occupied")

        applicable = []
        for credit in credits:
            reqs = credit.get("requirements", []) or credit.get("room_level_requirements", [])
            matched_reqs = []
            for req in reqs:
                space_types = req.get("space_types", [])
                if not space_types:
                    matched_reqs.append(req)
                    continue
                if "all" in space_types or "all_spaces" in space_types:
                    matched_reqs.append(req)
                    continue
                if any(st in room_types for st in space_types):
                    matched_reqs.append(req)
                    continue
                if "regularly_occupied" in space_types and any(
                    r.get("is_regularly_occupied", True) for r in rooms
                ):
                    matched_reqs.append(req)

            if matched_reqs:
                credit_copy = dict(credit)
                credit_copy["matched_requirements"] = matched_reqs
                applicable.append(credit_copy)

        return applicable

    def get_requirements_by_room(self, project: dict) -> dict:
        """Return requirements organized by room type."""
        applicable = self.get_applicable_credits(project)
        by_room = {}

        for credit in applicable:
            for req in credit.get("matched_requirements", []):
                space_types = req.get("space_types", ["all_spaces"])
                for st in space_types:
                    if st not in by_room:
                        by_room[st] = []
                    by_room[st].append({
                        "credit_id": credit["id"],
                        "credit_title": credit.get("title") or credit.get("issue", ""),
                        "category": credit["category"],
                        "type": credit.get("type", "credit"),
                        "metric": req["metric"],
                        "threshold": req["threshold"],
                        "unit": req.get("unit", ""),
                        "standard": req.get("standard", ""),
                        "notes": req.get("notes", ""),
                        "source_clause": credit["source_clause"],
                    })

        return by_room

    def get_certification_gap(self, current_points: int | float, target_level: str) -> dict:
        """Calculate how many more points/score needed for target level."""
        scoring = self.load_scoring()
        levels = scoring.get("certification_levels", {})
        target = levels.get(target_level.lower())
        if not target:
            return {"error": f"Unknown level: {target_level}"}

        min_needed = target["min_score"] if "min_score" in target else target["min_points"]
        gap = max(0, min_needed - current_points)
        return {
            "current": current_points,
            "target_level": target_level,
            "minimum_needed": min_needed,
            "gap": gap,
            "on_track": gap == 0,
        }


def assess_project(project: dict, scorer: CertificationScorer) -> dict:
    """
    Full project assessment.

    Returns:
        {
            "prerequisites": [...],
            "applicable_credits": [...],
            "requirements_by_room": {...},
            "scoring": {...},
            "certification_gap": {...}
        }
    """
    prerequisites = scorer.check_prerequisites(project)
    applicable = scorer.get_applicable_credits(project)
    by_room = scorer.get_requirements_by_room(project)
    scoring_info = scorer.load_scoring()

    target = project.get("certification_target", {})
    target_level = target.get("level", "")

    all_prereqs_met = all(p.get("met", False) for p in prerequisites)

    return {
        "system": target.get("system", ""),
        "version": target.get("version", ""),
        "target_level": target_level,
        "prerequisites": prerequisites,
        "all_prerequisites_met": all_prereqs_met,
        "applicable_credits": [
            {
                "id": c["id"],
                "title": c.get("title") or c.get("issue", ""),
                "category": c["category"],
                "type": c.get("type", "credit"),
                "points_available": c.get("points_available") or c.get("credits_available", 0),
                "requirement_count": len(c.get("matched_requirements", [])),
            }
            for c in applicable
        ],
        "requirements_by_room": by_room,
        "scoring": scoring_info,
        "certification_levels": scoring_info.get("certification_levels", {}),
    }

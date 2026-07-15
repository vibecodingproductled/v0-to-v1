"""
LEED BD+C v4.1 scoring module.

LEED uses additive point scoring:
- Prerequisites are mandatory (pass/fail, no points)
- Credits earn points
- Total points determine certification level
- 110 points possible
"""

from engine.scoring import CertificationScorer, load_json, KNOWLEDGE_DIR


LEED_DIR = KNOWLEDGE_DIR / "leed" / "v4.1-bdc"


class LEEDScorer(CertificationScorer):

    def load_credits(self) -> list[dict]:
        return load_json(LEED_DIR / "credits.json")

    def load_scoring(self) -> dict:
        return load_json(LEED_DIR / "scoring.json")

    def compute_score(self, achieved_credits: list[dict]) -> dict:
        """
        Compute LEED score from achieved credits.

        achieved_credits: list of {"credit_id": str, "points_earned": int}
        """
        scoring = self.load_scoring()
        total = sum(c.get("points_earned", 0) for c in achieved_credits)

        level = "not_certified"
        for lvl_name, lvl_data in sorted(
            scoring["certification_levels"].items(),
            key=lambda x: x[1]["min_points"],
            reverse=True,
        ):
            if total >= lvl_data["min_points"]:
                level = lvl_name
                break

        return {
            "total_points": total,
            "max_possible": scoring["total_possible_points"],
            "certification_level": level,
            "credits_achieved": len(achieved_credits),
        }

    def check_prerequisites(self, project: dict) -> list[dict]:
        """
        Check all LEED prerequisites.

        Returns a list of prerequisites with their status.
        At early design stage, most prerequisites cannot be verified yet,
        so we flag them as requirements the architect must be aware of.
        """
        credits = self.load_credits()
        prerequisites = [c for c in credits if c.get("type") == "prerequisite"]

        results = []
        for prereq in prerequisites:
            results.append({
                "id": prereq["id"],
                "title": prereq["title"],
                "category": prereq["category"],
                "met": None,
                "status": "requires_verification",
                "requirements": [
                    {
                        "metric": r["metric"],
                        "threshold": r["threshold"],
                        "unit": r.get("unit", ""),
                        "standard": r.get("standard", ""),
                    }
                    for r in prereq.get("requirements", [])
                ],
                "note": "Prerequisites are mandatory. Failing any prerequisite disqualifies the project from certification.",
            })

        return results

    def get_points_for_threshold(self, credit_id: str, achieved_value: float) -> int:
        """
        For credits with tiered points (like EAc2), determine points earned
        based on the achieved value.
        """
        credits = self.load_credits()
        credit = next((c for c in credits if c["id"] == credit_id), None)
        if not credit:
            return 0

        best_points = 0
        for req in credit.get("requirements", []):
            if isinstance(req.get("threshold"), list):
                for tier in req["threshold"]:
                    if achieved_value >= tier.get("value", 0):
                        best_points = max(best_points, tier.get("points", 0))
            elif isinstance(req.get("threshold"), (int, float)):
                if achieved_value >= req["threshold"]:
                    best_points = max(best_points, credit.get("points_available", 0))

        return best_points

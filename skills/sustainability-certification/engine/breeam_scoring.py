"""
BREEAM New Construction 2023 scoring module.

BREEAM uses weighted category scoring:
- Each category has a percentage weight
- Credits earned within a category determine the category percentage achieved
- Final score = sum of (category_percentage * category_weight)
- Minimum standards must be met for higher ratings
- Innovation can add up to 10% directly
"""

from engine.scoring import CertificationScorer, load_json, KNOWLEDGE_DIR


BREEAM_DIR = KNOWLEDGE_DIR / "breeam" / "nc-2023"


class BREEAMScorer(CertificationScorer):

    def load_credits(self) -> list[dict]:
        return load_json(BREEAM_DIR / "issues.json")

    def load_scoring(self) -> dict:
        return load_json(BREEAM_DIR / "weighting.json")

    def compute_score(self, achieved_credits: list[dict]) -> dict:
        """
        Compute BREEAM score from achieved credits.

        achieved_credits: list of {"issue_id": str, "credits_earned": int}

        BREEAM scoring:
        1. For each category, compute % of available credits achieved
        2. Multiply by category weight
        3. Sum all categories for final score
        4. Check minimum standards for target level
        """
        scoring = self.load_scoring()
        issues = self.load_credits()
        weightings = scoring["category_weightings"]

        category_totals = {}
        for issue in issues:
            cat = issue["category"]
            if cat not in category_totals:
                category_totals[cat] = {"available": 0, "achieved": 0}
            category_totals[cat]["available"] += issue.get("credits_available", 0)

        for ac in achieved_credits:
            issue = next((i for i in issues if i["id"] == ac["issue_id"]), None)
            if issue:
                cat = issue["category"]
                category_totals[cat]["achieved"] += ac.get("credits_earned", 0)

        final_score = 0.0
        category_scores = {}
        for cat, totals in category_totals.items():
            if totals["available"] > 0:
                pct = (totals["achieved"] / totals["available"]) * 100
            else:
                pct = 0
            weight = weightings.get(cat, 0)
            weighted = (pct / 100) * weight
            category_scores[cat] = {
                "achieved": totals["achieved"],
                "available": totals["available"],
                "percentage": round(pct, 1),
                "weight": weight,
                "weighted_score": round(weighted, 2),
            }
            final_score += weighted

        level = "unclassified"
        for lvl_name, lvl_data in sorted(
            scoring["certification_levels"].items(),
            key=lambda x: x[1]["min_score"],
            reverse=True,
        ):
            if final_score >= lvl_data["min_score"]:
                level = lvl_name
                break

        return {
            "final_score": round(final_score, 1),
            "certification_level": level,
            "category_scores": category_scores,
        }

    def check_prerequisites(self, project: dict) -> list[dict]:
        """
        Check BREEAM minimum standards.

        BREEAM doesn't have "prerequisites" in the LEED sense, but has
        minimum standards: certain issues must achieve a minimum number
        of credits for higher ratings (Excellent, Outstanding).
        """
        issues = self.load_credits()
        target_level = project.get("certification_target", {}).get("level", "").lower()

        results = []
        for issue in issues:
            min_stds = issue.get("minimum_standards", {})
            if not min_stds:
                continue

            required = min_stds.get(target_level)
            if required:
                results.append({
                    "id": issue["id"],
                    "issue": issue.get("issue", ""),
                    "category": issue["category"],
                    "met": None,
                    "status": "requires_verification",
                    "minimum_for_level": required,
                    "target_level": target_level,
                    "note": f"Minimum standard for {target_level}: {required}",
                })

        return results

    def check_minimum_standards(self, achieved: list[dict], target_level: str) -> list[dict]:
        """
        Verify that all minimum standards are met for the target level.

        Returns list of minimum standards with pass/fail.
        """
        issues = self.load_credits()
        achieved_map = {a["issue_id"]: a.get("credits_earned", 0) for a in achieved}

        failures = []
        for issue in issues:
            min_stds = issue.get("minimum_standards", {})
            required = min_stds.get(target_level.lower())
            if required is None:
                continue

            if isinstance(required, str) and required.endswith("credits"):
                min_credits = int(required.split()[0])
            elif isinstance(required, (int, float)):
                min_credits = int(required)
            else:
                continue

            earned = achieved_map.get(issue["id"], 0)
            if earned < min_credits:
                failures.append({
                    "id": issue["id"],
                    "issue": issue.get("issue", ""),
                    "required": min_credits,
                    "achieved": earned,
                    "met": False,
                })

        return failures

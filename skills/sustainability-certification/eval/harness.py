"""
Evaluation harness for sustainability certification agents.

Runs the scoring engine against synthetic test cases and verifies:
- Correct credit applicability per room type
- Correct thresholds
- Prerequisite detection
- Proper handling of missing data

Usage:
    cd sustainability-certification
    python eval/harness.py
"""

import json
import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from engine.scoring import assess_project
from engine.leed_scoring import LEEDScorer
from engine.breeam_scoring import BREEAMScorer


CASES_DIR = Path(__file__).parent / "cases"


def load_test_cases(system: str) -> list[dict]:
    case_dir = CASES_DIR / system.lower()
    cases = []
    if not case_dir.exists():
        return cases
    for f in sorted(case_dir.glob("*.json")):
        with open(f) as fh:
            cases.append(json.load(fh))
    return cases


def run_leed_tests() -> tuple[int, int, list[str]]:
    scorer = LEEDScorer()
    cases = load_test_cases("leed")
    passed = 0
    failed = 0
    errors = []

    for case in cases:
        project = case["project"]
        expected = case["expected"]
        case_name = case.get("name", "unnamed")

        try:
            result = assess_project(project, scorer)

            if "prerequisite_count" in expected:
                actual_count = len(result["prerequisites"])
                if actual_count != expected["prerequisite_count"]:
                    errors.append(
                        f"[{case_name}] Prerequisites: expected {expected['prerequisite_count']}, got {actual_count}"
                    )
                    failed += 1
                    continue

            if "applicable_credit_ids" in expected:
                actual_ids = {c["id"] for c in result["applicable_credits"]}
                expected_ids = set(expected["applicable_credit_ids"])
                missing = expected_ids - actual_ids
                extra = actual_ids - expected_ids
                if missing or extra:
                    msg = f"[{case_name}] Credits:"
                    if missing:
                        msg += f" missing {missing}"
                    if extra:
                        msg += f" unexpected {extra}"
                    errors.append(msg)
                    failed += 1
                    continue

            if "room_types_with_requirements" in expected:
                actual_rooms = set(result["requirements_by_room"].keys())
                expected_rooms = set(expected["room_types_with_requirements"])
                if not expected_rooms.issubset(actual_rooms):
                    missing = expected_rooms - actual_rooms
                    errors.append(
                        f"[{case_name}] Missing room types: {missing}"
                    )
                    failed += 1
                    continue

            if "certification_levels" in expected:
                actual_levels = result["certification_levels"]
                for level, data in expected["certification_levels"].items():
                    if level not in actual_levels:
                        errors.append(f"[{case_name}] Missing level: {level}")
                        failed += 1
                        continue
                    actual_min = actual_levels[level].get("min_points")
                    if actual_min != data.get("min_points"):
                        errors.append(
                            f"[{case_name}] {level} min_points: expected {data['min_points']}, got {actual_min}"
                        )
                        failed += 1
                        continue

            passed += 1

        except Exception as e:
            errors.append(f"[{case_name}] Exception: {e}")
            failed += 1

    return passed, failed, errors


def run_breeam_tests() -> tuple[int, int, list[str]]:
    scorer = BREEAMScorer()
    cases = load_test_cases("breeam")
    passed = 0
    failed = 0
    errors = []

    for case in cases:
        project = case["project"]
        expected = case["expected"]
        case_name = case.get("name", "unnamed")

        try:
            result = assess_project(project, scorer)

            if "minimum_standard_count" in expected:
                actual_count = len(result["prerequisites"])
                if actual_count < expected["minimum_standard_count"]:
                    errors.append(
                        f"[{case_name}] Minimum standards: expected >= {expected['minimum_standard_count']}, got {actual_count}"
                    )
                    failed += 1
                    continue

            if "applicable_issue_ids" in expected:
                actual_ids = {c["id"] for c in result["applicable_credits"]}
                expected_ids = set(expected["applicable_issue_ids"])
                missing = expected_ids - actual_ids
                if missing:
                    errors.append(
                        f"[{case_name}] Missing issues: {missing}"
                    )
                    failed += 1
                    continue

            if "room_types_with_requirements" in expected:
                actual_rooms = set(result["requirements_by_room"].keys())
                expected_rooms = set(expected["room_types_with_requirements"])
                if not expected_rooms.issubset(actual_rooms):
                    missing = expected_rooms - actual_rooms
                    errors.append(
                        f"[{case_name}] Missing room types: {missing}"
                    )
                    failed += 1
                    continue

            if "certification_levels" in expected:
                actual_levels = result["certification_levels"]
                for level, data in expected["certification_levels"].items():
                    if level not in actual_levels:
                        errors.append(f"[{case_name}] Missing level: {level}")
                        failed += 1
                        continue
                    actual_min = actual_levels[level].get("min_score")
                    if actual_min != data.get("min_score"):
                        errors.append(
                            f"[{case_name}] {level} min_score: expected {data['min_score']}, got {actual_min}"
                        )
                        failed += 1
                        continue

            passed += 1

        except Exception as e:
            errors.append(f"[{case_name}] Exception: {e}")
            failed += 1

    return passed, failed, errors


def main():
    print("=" * 60)
    print("Sustainability Certification Agent - Evaluation Harness")
    print("=" * 60)

    total_passed = 0
    total_failed = 0
    all_errors = []

    print("\n--- LEED BD+C v4.1 ---")
    p, f, e = run_leed_tests()
    total_passed += p
    total_failed += f
    all_errors.extend(e)
    print(f"  Passed: {p}, Failed: {f}")

    print("\n--- BREEAM NC 2023 ---")
    p, f, e = run_breeam_tests()
    total_passed += p
    total_failed += f
    all_errors.extend(e)
    print(f"  Passed: {p}, Failed: {f}")

    print("\n" + "=" * 60)
    print(f"TOTAL: {total_passed} passed, {total_failed} failed")

    if all_errors:
        print("\nErrors:")
        for err in all_errors:
            print(f"  {err}")

    print("=" * 60)
    return 0 if total_failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

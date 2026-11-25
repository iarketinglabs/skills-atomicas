#!/usr/bin/env python3
"""Summarize paired baseline/candidate results without making statistical claims."""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any


def is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def load(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ValueError(f"Cannot read {path}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}") from exc
    if not isinstance(value, dict):
        raise ValueError("Input must be a JSON object")
    return value


def index_results(rows: Any, label: str) -> dict[str, dict[str, Any]]:
    if not isinstance(rows, list) or not rows:
        raise ValueError(f"{label} must be a non-empty array")
    indexed: dict[str, dict[str, Any]] = {}
    for position, row in enumerate(rows):
        if not isinstance(row, dict):
            raise ValueError(f"{label}[{position}] must be an object")
        case_id = row.get("case_id")
        if not isinstance(case_id, str) or not case_id.strip():
            raise ValueError(f"{label}[{position}].case_id must be a non-empty string")
        case_id = case_id.strip()
        if case_id in indexed:
            raise ValueError(f"Duplicate case_id {case_id!r} in {label}")
        score = row.get("score")
        if not is_number(score):
            raise ValueError(f"{label}[{position}].score must be a finite number")
        critical = row.get("critical_failure", False)
        if not isinstance(critical, bool):
            raise ValueError(f"{label}[{position}].critical_failure must be true or false")
        indexed[case_id] = {"score": float(score), "critical_failure": critical}
    return indexed


def compare(data: dict[str, Any]) -> dict[str, Any]:
    metric = data.get("metric")
    direction = data.get("direction")
    if not isinstance(metric, str) or not metric.strip():
        raise ValueError("metric must be a non-empty string")
    if direction not in {"higher_is_better", "lower_is_better"}:
        raise ValueError("direction must be 'higher_is_better' or 'lower_is_better'")

    baseline = index_results(data.get("baseline"), "baseline")
    candidate = index_results(data.get("candidate"), "candidate")
    if set(baseline) != set(candidate):
        missing = sorted(set(baseline) - set(candidate))
        extra = sorted(set(candidate) - set(baseline))
        raise ValueError(f"case IDs must match exactly; missing from candidate={missing}, extra in candidate={extra}")

    rows: list[dict[str, Any]] = []
    wins = ties = losses = 0
    baseline_failures = candidate_failures = 0
    for case_id in sorted(baseline):
        before = baseline[case_id]
        after = candidate[case_id]
        raw_delta = after["score"] - before["score"]
        oriented_delta = raw_delta if direction == "higher_is_better" else -raw_delta
        if oriented_delta > 1e-12:
            wins += 1
        elif oriented_delta < -1e-12:
            losses += 1
        else:
            ties += 1
        baseline_failures += int(before["critical_failure"])
        candidate_failures += int(after["critical_failure"])
        rows.append({
            "case_id": case_id,
            "baseline_score": before["score"],
            "candidate_score": after["score"],
            "direction_adjusted_delta": oriented_delta,
            "baseline_critical_failure": before["critical_failure"],
            "candidate_critical_failure": after["critical_failure"],
        })

    count = len(rows)
    mean_baseline = sum(row["baseline_score"] for row in rows) / count
    mean_candidate = sum(row["candidate_score"] for row in rows) / count
    mean_improvement = sum(row["direction_adjusted_delta"] for row in rows) / count
    return {
        "metric": metric.strip(),
        "direction": direction,
        "sample_size": count,
        "mean_baseline": mean_baseline,
        "mean_candidate": mean_candidate,
        "mean_direction_adjusted_improvement": mean_improvement,
        "paired_wins": wins,
        "paired_ties": ties,
        "paired_losses": losses,
        "baseline_critical_failures": baseline_failures,
        "candidate_critical_failures": candidate_failures,
        "cases": rows,
        "notice": "Descriptive paired summary only. It does not estimate uncertainty, establish statistical significance, prove generalization, or authorize promotion.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("results", type=Path, help="JSON file containing paired baseline and candidate results")
    args = parser.parse_args()
    try:
        result = compare(load(args.results))
    except ValueError as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False, indent=2))
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

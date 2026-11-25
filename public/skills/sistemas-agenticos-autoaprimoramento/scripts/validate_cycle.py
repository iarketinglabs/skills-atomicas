#!/usr/bin/env python3
"""Validate a self-improvement cycle record and report declared promotion gates."""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any


SURFACES = {"output", "prompt", "memory", "skill", "workflow", "tool", "code", "evaluator", "weights"}
RISKS = {"low", "medium", "high", "critical"}
DIRECTIONS = {"higher_is_better", "lower_is_better"}
DECISIONS = {"promote", "hold", "reject"}
ROLLOUTS = {"none", "shadow", "canary", "limited", "general"}


def is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ValueError(f"Cannot read {path}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}") from exc


def add_check(checks: list[dict[str, Any]], name: str, passed: bool, detail: str) -> None:
    checks.append({"name": name, "passed": bool(passed), "detail": detail})


def validate(record: Any) -> tuple[list[str], list[dict[str, Any]], bool, dict[str, Any]]:
    errors: list[str] = []
    checks: list[dict[str, Any]] = []

    def mapping(value: Any, label: str) -> dict[str, Any]:
        if not isinstance(value, dict):
            errors.append(f"{label} must be an object")
            return {}
        return value

    def text(value: Any, label: str, *, required: bool = True) -> str | None:
        if value is None and not required:
            return None
        if not isinstance(value, str) or not value.strip():
            if required:
                errors.append(f"{label} must be a non-empty string")
            return None
        return value.strip()

    def boolean(value: Any, label: str) -> bool | None:
        if not isinstance(value, bool):
            errors.append(f"{label} must be true or false")
            return None
        return value

    def number(value: Any, label: str, *, minimum: float | None = None) -> float | None:
        if not is_number(value):
            errors.append(f"{label} must be a finite number")
            return None
        result = float(value)
        if minimum is not None and result < minimum:
            errors.append(f"{label} must be at least {minimum}")
        return result

    def integer(value: Any, label: str, *, minimum: int = 0) -> int | None:
        if isinstance(value, bool) or not isinstance(value, int):
            errors.append(f"{label} must be an integer")
            return None
        if value < minimum:
            errors.append(f"{label} must be at least {minimum}")
        return value

    root = mapping(record, "record")
    text(root.get("schema_version"), "schema_version")
    text(root.get("cycle_id"), "cycle_id")

    system = mapping(root.get("system"), "system")
    text(system.get("id"), "system.id")
    text(system.get("version_before"), "system.version_before")

    change = mapping(root.get("change"), "change")
    text(change.get("id"), "change.id")
    surface = text(change.get("surface"), "change.surface")
    if surface and surface not in SURFACES:
        errors.append(f"change.surface must be one of: {', '.join(sorted(SURFACES))}")
    text(change.get("summary"), "change.summary")
    risk = text(change.get("risk"), "change.risk")
    if risk and risk not in RISKS:
        errors.append(f"change.risk must be one of: {', '.join(sorted(RISKS))}")
    for key in ("baseline_ref", "candidate_ref", "rollback_ref"):
        text(change.get(key), f"change.{key}")

    objective = mapping(root.get("objective"), "objective")
    metric = text(objective.get("metric"), "objective.metric")
    direction = text(objective.get("direction"), "objective.direction")
    if direction and direction not in DIRECTIONS:
        errors.append(f"objective.direction must be one of: {', '.join(sorted(DIRECTIONS))}")

    budget = mapping(root.get("budget"), "budget")
    max_iterations = integer(budget.get("max_iterations"), "budget.max_iterations", minimum=1)
    iterations_used = integer(budget.get("iterations_used"), "budget.iterations_used")
    if max_iterations is not None and iterations_used is not None and iterations_used > max_iterations:
        errors.append("budget.iterations_used cannot exceed budget.max_iterations")

    resource_caps = (
        ("max_runtime_seconds", "runtime_used_seconds"),
        ("max_tokens", "tokens_used"),
        ("max_cost", "cost_used"),
    )
    declared_resource_caps = 0
    budgets_within_limits = max_iterations is not None and iterations_used is not None and iterations_used <= max_iterations
    for cap_key, used_key in resource_caps:
        cap_value = budget.get(cap_key)
        used_value = budget.get(used_key)
        if cap_value is None and used_value is None:
            continue
        if cap_value is None:
            errors.append(f"budget.{cap_key} is required when {used_key} is provided")
            budgets_within_limits = False
            continue
        cap = number(cap_value, f"budget.{cap_key}", minimum=0.000001)
        declared_resource_caps += 1
        used = 0.0 if used_value is None else number(used_value, f"budget.{used_key}", minimum=0)
        if cap is not None and used is not None and used > cap:
            errors.append(f"budget.{used_key} cannot exceed budget.{cap_key}")
            budgets_within_limits = False
    if declared_resource_caps == 0:
        errors.append("budget must include at least one limit besides max_iterations: time, tokens, or cost")
        budgets_within_limits = False
    if budget.get("max_cost") is not None:
        text(budget.get("currency"), "budget.currency")
    elif budget.get("currency") is not None:
        text(budget.get("currency"), "budget.currency")
    add_check(checks, "resource_budget_respected", budgets_within_limits, "Observed iterations and declared resource use are within the recorded caps.")

    evaluation = mapping(root.get("evaluation"), "evaluation")
    dataset = mapping(evaluation.get("dataset"), "evaluation.dataset")
    text(dataset.get("id"), "evaluation.dataset.id")
    text(dataset.get("version"), "evaluation.dataset.version")
    held_out = boolean(dataset.get("held_out"), "evaluation.dataset.held_out")
    case_ids = dataset.get("case_ids")
    if not isinstance(case_ids, list) or not case_ids or any(not isinstance(item, str) or not item.strip() for item in case_ids):
        errors.append("evaluation.dataset.case_ids must be a non-empty array of non-empty strings")
        case_ids = []
    elif len(set(case_ids)) != len(case_ids):
        errors.append("evaluation.dataset.case_ids must not contain duplicates")
    add_check(checks, "protected_evaluation_set", held_out is True and bool(case_ids), "Dataset is declared held out and has at least one identified case.")

    method = text(evaluation.get("method"), "evaluation.method")
    if method and method not in {"paired", "unpaired"}:
        errors.append("evaluation.method must be 'paired' or 'unpaired'")
    rationale = text(evaluation.get("comparison_rationale"), "evaluation.comparison_rationale")
    if method == "unpaired" and not rationale:
        errors.append("Unpaired comparison requires evaluation.comparison_rationale")

    evaluator = mapping(evaluation.get("evaluator"), "evaluation.evaluator")
    text(evaluator.get("id"), "evaluation.evaluator.id")
    text(evaluator.get("version"), "evaluation.evaluator.version")
    independent = boolean(evaluator.get("independent"), "evaluation.evaluator.independent")
    candidate_can_modify = boolean(evaluator.get("candidate_can_modify"), "evaluation.evaluator.candidate_can_modify")
    evaluator_gate = independent is True and candidate_can_modify is False
    add_check(checks, "independent_immutable_evaluator", evaluator_gate, "The evaluator is declared independent and not candidate-modifiable.")

    results = mapping(evaluation.get("results"), "evaluation.results")
    baseline = mapping(results.get("baseline"), "evaluation.results.baseline")
    candidate = mapping(results.get("candidate"), "evaluation.results.candidate")
    baseline_primary = number(baseline.get("primary_metric"), "evaluation.results.baseline.primary_metric")
    candidate_primary = number(candidate.get("primary_metric"), "evaluation.results.candidate.primary_metric")
    improvement: float | None = None
    if baseline_primary is not None and candidate_primary is not None and direction in DIRECTIONS:
        improvement = candidate_primary - baseline_primary if direction == "higher_is_better" else baseline_primary - candidate_primary

    acceptance = mapping(root.get("acceptance"), "acceptance")
    minimum_effect = number(acceptance.get("minimum_effect"), "acceptance.minimum_effect", minimum=0)
    max_critical = integer(acceptance.get("max_critical_failures"), "acceptance.max_critical_failures")
    decision = text(acceptance.get("decision"), "acceptance.decision")
    if decision and decision not in DECISIONS:
        errors.append(f"acceptance.decision must be one of: {', '.join(sorted(DECISIONS))}")
    approval_required = boolean(acceptance.get("human_approval_required"), "acceptance.human_approval_required")
    approved_by = text(acceptance.get("approved_by"), "acceptance.approved_by", required=False)
    surface_needs_approval = surface in {"code", "evaluator", "weights"} or risk in {"high", "critical"}
    approval_declaration_ok = not surface_needs_approval or approval_required is True
    if not approval_declaration_ok:
        errors.append("High-risk, code, evaluator, and weight changes must declare human_approval_required=true")
    approval_gate = approval_required is False or bool(approved_by)
    add_check(checks, "required_human_approval_recorded", approval_declaration_ok and approval_gate, "Approval is recorded when required by the declared risk and change surface.")

    critical_failures = integer(evaluation.get("critical_failures"), "evaluation.critical_failures")
    if max_critical is not None and critical_failures is not None:
        add_check(checks, "critical_failure_limit", critical_failures <= max_critical, f"Observed {critical_failures}; allowed {max_critical}.")
    else:
        add_check(checks, "critical_failure_limit", False, "Critical-failure counts are incomplete.")

    if improvement is not None and minimum_effect is not None:
        add_check(checks, "minimum_effect", improvement >= minimum_effect, f"Direction-adjusted change is {improvement:g}; required minimum is {minimum_effect:g}.")
    else:
        add_check(checks, "minimum_effect", False, "Primary metric direction or results are incomplete.")

    guardrails = evaluation.get("guardrails")
    baseline_guardrails = baseline.get("guardrails")
    candidate_guardrails = candidate.get("guardrails")
    guardrail_passed = True
    if not isinstance(guardrails, list):
        errors.append("evaluation.guardrails must be an array")
        guardrails = []
        guardrail_passed = False
    elif not guardrails:
        errors.append("evaluation.guardrails must declare at least one protected metric")
        guardrail_passed = False
    if not isinstance(baseline_guardrails, dict) or not isinstance(candidate_guardrails, dict):
        errors.append("baseline and candidate guardrails must be objects")
        baseline_guardrails = {}
        candidate_guardrails = {}
        guardrail_passed = False
    for index, guardrail in enumerate(guardrails):
        if not isinstance(guardrail, dict):
            errors.append(f"evaluation.guardrails[{index}] must be an object")
            guardrail_passed = False
            continue
        g_metric = text(guardrail.get("metric"), f"evaluation.guardrails[{index}].metric")
        g_direction = text(guardrail.get("direction"), f"evaluation.guardrails[{index}].direction")
        max_regression = number(guardrail.get("max_regression"), f"evaluation.guardrails[{index}].max_regression", minimum=0)
        if g_direction and g_direction not in DIRECTIONS:
            errors.append(f"evaluation.guardrails[{index}].direction must be a valid metric direction")
            guardrail_passed = False
        if not g_metric or max_regression is None or g_direction not in DIRECTIONS:
            guardrail_passed = False
            continue
        b_value = number(baseline_guardrails.get(g_metric), f"baseline guardrail {g_metric}")
        c_value = number(candidate_guardrails.get(g_metric), f"candidate guardrail {g_metric}")
        if b_value is None or c_value is None:
            guardrail_passed = False
            continue
        regression = b_value - c_value if g_direction == "higher_is_better" else c_value - b_value
        if regression > max_regression:
            guardrail_passed = False
    add_check(checks, "guardrails_within_tolerance", guardrail_passed, "Every declared guardrail is within its maximum regression.")

    rollout = mapping(root.get("rollout"), "rollout")
    rollout_mode = text(rollout.get("mode"), "rollout.mode")
    if rollout_mode and rollout_mode not in ROLLOUTS:
        errors.append(f"rollout.mode must be one of: {', '.join(sorted(ROLLOUTS))}")
    rollback_plan = text(rollout.get("rollback_plan"), "rollout.rollback_plan")
    stop_conditions = rollout.get("stop_conditions")
    if not isinstance(stop_conditions, list) or not stop_conditions or any(not isinstance(item, str) or not item.strip() for item in stop_conditions):
        errors.append("rollout.stop_conditions must be a non-empty array of non-empty strings")
        stop_conditions = []
    rollback_gate = bool(text(change.get("rollback_ref"), "change.rollback_ref")) and bool(rollback_plan) and bool(stop_conditions)
    add_check(checks, "rollback_and_stops_defined", rollback_gate, "Rollback reference, plan, and stop conditions are present.")

    record_valid = not errors
    promotion_gates_passed = record_valid and all(check["passed"] for check in checks)
    if decision == "promote" and not promotion_gates_passed:
        recommendation = "promotion_blocked"
    elif decision == "promote":
        recommendation = "declared_gates_passed_human_or_policy_review_still_applies"
    elif decision in {"hold", "reject"}:
        recommendation = f"recorded_decision_{decision}; validator_does_not_override"
    else:
        recommendation = "hold_invalid_or_incomplete_record"

    summary = {
        "cycle_id": root.get("cycle_id"),
        "record_valid": record_valid,
        "declared_decision": decision,
        "promotion_gates_passed": promotion_gates_passed,
        "direction_adjusted_effect": improvement,
        "recommendation": recommendation,
        "checks": checks,
        "errors": errors,
        "notice": "This script checks the supplied record and declared gates only. It cannot prove evidence independence, legal authorization, safety, statistical validity, or deployment readiness.",
    }
    return errors, checks, promotion_gates_passed, summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path, help="Path to a cycle-record JSON file")
    parser.add_argument("--require-promotion", action="store_true", help="Return exit code 2 unless decision is promote and all declared gates pass")
    args = parser.parse_args()

    try:
        record = read_json(args.record)
        errors, checks, gates_passed, summary = validate(record)
    except ValueError as exc:
        print(json.dumps({"record_valid": False, "errors": [str(exc)]}, ensure_ascii=False, indent=2))
        return 1

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if errors:
        return 1
    if args.require_promotion and (summary.get("declared_decision") != "promote" or not gates_passed):
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())

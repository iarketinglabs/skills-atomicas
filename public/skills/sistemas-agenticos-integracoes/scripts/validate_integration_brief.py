#!/usr/bin/env python3
"""Check basic completeness of a JSON integration brief; no external packages."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def is_blank(value: Any) -> bool:
    return value is None or value == "" or value == [] or value == {}


def validate(document: Any) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not isinstance(document, dict):
        return ["A raiz do ficheiro deve ser um objeto JSON."], warnings

    for field in ("objective", "flows"):
        if field not in document or is_blank(document[field]):
            errors.append(f"Campo obrigatório ausente ou vazio: {field}.")

    flows = document.get("flows")
    if flows is not None and not isinstance(flows, list):
        errors.append("O campo flows deve ser uma lista.")
        flows = []

    for index, flow in enumerate(flows or []):
        label = f"flows[{index}]"
        if not isinstance(flow, dict):
            errors.append(f"{label} deve ser um objeto.")
            continue
        for field in ("source", "destination", "pattern"):
            if field not in flow or is_blank(flow[field]):
                errors.append(f"Campo obrigatório ausente ou vazio: {label}.{field}.")
        for field in (
            "trigger",
            "data_and_semantics",
            "freshness",
            "ordering",
            "deduplication",
            "idempotency",
            "failure_handling",
            "reconciliation",
        ):
            if field not in flow or is_blank(flow[field]):
                warnings.append(f"Reveja se é aplicável: {label}.{field}.")

    for section, fields in {
        "security": ("data_classification", "identity_and_authentication", "authorization"),
        "operations": ("support_owner", "signals_and_alerts", "recovery_and_replay"),
        "rollout": ("acceptance_criteria", "rollback_or_recovery"),
    }.items():
        values = document.get(section)
        if not isinstance(values, dict):
            warnings.append(f"Reveja a secção {section}: ausente ou não é um objeto.")
            continue
        for field in fields:
            if field not in values or is_blank(values[field]):
                warnings.append(f"Reveja se é aplicável: {section}.{field}.")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verifica campos básicos e lacunas a rever num brief de integração JSON."
    )
    parser.add_argument("brief", type=Path, help="Caminho para o ficheiro JSON")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Devolve código de saída 1 também quando existirem avisos de completude",
    )
    args = parser.parse_args()

    try:
        with args.brief.open("r", encoding="utf-8") as stream:
            document = json.load(stream)
    except OSError as exc:
        print(f"Erro ao ler {args.brief}: {exc}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as exc:
        print(f"JSON inválido em {args.brief}, linha {exc.lineno}, coluna {exc.colno}: {exc.msg}", file=sys.stderr)
        return 2

    errors, warnings = validate(document)
    for message in errors:
        print(f"ERRO: {message}")
    for message in warnings:
        print(f"REVER: {message}")

    if errors:
        print("Brief incompleto: corrija os erros antes de avançar.")
        return 2
    if warnings:
        print(f"Brief estruturalmente legível; há {len(warnings)} ponto(s) a rever.")
        return 1 if args.strict else 0

    print("Brief estruturalmente legível; esta verificação não prova a qualidade do desenho.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

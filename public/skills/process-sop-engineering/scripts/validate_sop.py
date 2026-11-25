#!/usr/bin/env python3
"""Check the structural completeness of a Markdown procedure.

Usage:
    python validate_sop.py path/to/procedure.md
    python validate_sop.py path/to/agent-procedure.md --profile agent-ready

Uses only the Python standard library. A passing result checks headings and
numbered steps only; it does not validate process correctness, evidence,
compliance, safety, permissions, or behavior in a target runtime.
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path


GENERIC_SECTIONS = {
    "objective": r"\b(objective|objetivo)\b",
    "scope": r"\b(scope|escopo)\b",
    "inputs and preconditions": r"\b(input|inputs|entrada|entradas)\b.*\b(precondition|preconditions|precondicao|precondicoes|prerequisite|prerequisites|gatilho|trigger)\b|\b(precondition|preconditions|precondicao|precondicoes|prerequisite|prerequisites)\b.*\b(input|inputs|entrada|entradas)\b",
    "roles and responsibilities": r"\b(role|roles|papel|papeis|responsibility|responsibilities|responsabilidade|responsabilidades)\b",
    "procedure steps": r"\b(procedure|procedimento|steps|passos)\b",
    "success criteria or controls": r"\b(success|completion|criteria|criterion|criterios|criterio|control|controls|controle|controles)\b",
    "exceptions, stop, or escalation": r"\b(exception|exceptions|excecao|excecoes|stop|parada|escalation|escalonamento|fallback|failure|falha|falhas)\b",
    "governance or review": r"\b(governance|governanca|review|revision|revisao|version|versao|approval|aprovacao)\b",
}

AGENT_SECTIONS = {
    "autonomy and prohibited actions": r"\b(autonomy|autonomia|prohibited|proibidas?|denied actions|acoes negadas)\b",
    "human oversight": r"\b(human oversight|human supervision|supervisao humana|human-in-the-loop|hitl)\b",
    "failure fallback or recovery": r"\b(fallback|recovery|recuperacao|failure|falha|falhas)\b",
    "records audit or monitoring": r"\b(records|registros|audit|auditoria|monitoring|monitoramento|logs?)\b",
    "evaluation or release criteria": r"\b(evaluation|evaluations|avaliacao|avaliacoes|release|liberacao|criteria|criterios)\b",
}


def normalize(value: str) -> str:
    """Lowercase and remove diacritics to make Portuguese heading checks robust."""
    decomposed = unicodedata.normalize("NFKD", value.casefold())
    return "".join(char for char in decomposed if not unicodedata.combining(char))


def markdown_headings(content: str) -> str:
    found = []
    for line in content.splitlines():
        match = re.match(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", line)
        if match:
            found.append(normalize(match.group(1)))
    return "\n".join(found)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path, help="Markdown procedure to inspect")
    parser.add_argument(
        "--profile",
        choices=("generic", "agent-ready"),
        default="generic",
        help="additional structure required for an agent-ready procedure",
    )
    args = parser.parse_args()

    try:
        content = args.file.read_text(encoding="utf-8-sig")
    except OSError as exc:
        print(f"[ERROR] Cannot read {args.file}: {exc}", file=sys.stderr)
        return 2
    except UnicodeError as exc:
        print(f"[ERROR] File must be UTF-8 Markdown: {exc}", file=sys.stderr)
        return 2

    headings = markdown_headings(content)
    requirements = dict(GENERIC_SECTIONS)
    if args.profile == "agent-ready":
        requirements.update(AGENT_SECTIONS)

    missing = [
        label
        for label, pattern in requirements.items()
        if not re.search(pattern, headings)
    ]
    has_numbered_step = any(
        re.match(r"^\s*\d+[.)]\s+\S", line)
        for line in content.splitlines()
    )
    if not has_numbered_step:
        missing.append("at least one numbered procedure step")

    if not re.match(r"^---\s*\n", content):
        print("[WARN] No YAML metadata block found; add owner/version/status fields if your document-control process needs them.")
    else:
        print("[INFO] YAML metadata block detected; its syntax and values were not parsed.")

    if missing:
        print("[FAIL] Missing structural elements:")
        for item in missing:
            print(f"  - {item}")
        return 1

    print(f"[OK] Required {args.profile} procedure headings and numbered steps are present.")
    print("[LIMIT] This check does not verify accuracy, policy, compliance, safety, approval, or runtime behavior.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

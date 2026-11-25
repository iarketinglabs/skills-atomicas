#!/usr/bin/env python3
"""Check the structure of exported Markdown without modifying it."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

TITLE = re.compile(r"^ {0,3}#[ \t]+\S")
SECOND_TITLE = re.compile(r"^ {0,3}#(?:[ \t]|$)")
FENCE = re.compile(r"^ {0,3}(~{3,}|`{3,})(.*)$")
WRAPPER_HEADING = re.compile(r"^ {0,3}##[ \t]+(consulta|resposta)[ \t#]*$", re.IGNORECASE)
TRANSPORT_FIELDS = {"answer", "conversation_id", "sources_used", "citations", "status"}


def has_transport_envelope(body: str) -> bool:
    if not body.startswith("{"):
        return False
    try:
        parsed = json.loads(body)
    except json.JSONDecodeError:
        return False
    return isinstance(parsed, dict) and bool(parsed.keys() & TRANSPORT_FIELDS)


def structure_errors(text: str) -> list[str]:
    if not text.strip():
        return ["arquivo vazio"]

    lines = text.splitlines()
    errors = []
    if not TITLE.match(lines[0]):
        errors.append("H1 ausente na primeira linha")

    body = "\n".join(lines[1:]) if TITLE.match(lines[0]) else text
    if not body.strip():
        errors.append("corpo vazio")
    if has_transport_envelope(body.strip()):
        errors.append("objeto JSON de transporte")

    headings = set()
    duplicate_title = False
    fence = ""
    for line in lines[1:]:
        fence_match = FENCE.match(line)
        if fence_match:
            marker, rest = fence_match.groups()
            if fence:
                if marker[0] == fence[0] and len(marker) >= len(fence) and not rest.strip():
                    fence = ""
                continue
            if marker[0] != chr(96) or chr(96) not in rest:
                fence = marker
                continue
        if fence:
            continue
        if SECOND_TITLE.match(line):
            duplicate_title = True
        wrapper = WRAPPER_HEADING.match(line)
        if wrapper:
            headings.add(wrapper.group(1).casefold())

    if duplicate_title:
        errors.append("mais de um H1")
    if headings == {"consulta", "resposta"}:
        errors.append("seções do invólucro Consulta/Resposta")
    if fence:
        errors.append("cerca de código sem fechamento")
    return errors


def validate(path: Path) -> tuple[bool, list[str]]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return False, ["UTF-8 inválido"]
    except OSError:
        return False, ["arquivo ilegível"]
    return bool(text.strip()), structure_errors(text)


def collect_files(path: Path) -> list[Path]:
    if path.is_file() and path.suffix.lower() == ".md":
        return [path]
    if path.is_dir():
        return sorted(file for file in path.rglob("*") if file.is_file() and file.suffix.lower() == ".md")
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="arquivo Markdown ou pasta de respostas")
    parser.add_argument("--expected-count", type=int, help="quantidade esperada de documentos")
    args = parser.parse_args()
    if args.expected_count is not None and args.expected_count < 1:
        parser.error("--expected-count precisa ser um inteiro positivo")

    files = collect_files(args.path)
    nonempty = invalid = 0
    for file in files:
        has_text, errors = validate(file)
        nonempty += int(has_text)
        invalid += int(bool(errors))
        relative = file.relative_to(args.path) if args.path.is_dir() else file.name
        if errors:
            print(f"INVALID {relative}: {', '.join(errors)}")
        else:
            print(f"OK {relative}")

    print(f"COUNT={len(files)}\nNONEMPTY={nonempty}\nVALID={len(files) - invalid}\nINVALID={invalid}")
    if args.expected_count is not None:
        print(f"EXPECTED={args.expected_count}")
    if not files:
        print("Nenhum arquivo Markdown encontrado.")
    count_mismatch = args.expected_count is not None and len(files) != args.expected_count
    return int(not files or invalid > 0 or count_mismatch)


if __name__ == "__main__":
    raise SystemExit(main())

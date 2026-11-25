#!/usr/bin/env python3
"""Check the structure of exported Markdown without modifying it."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

HEADING = re.compile(r"^ {0,3}(#{1,6})(?:[ \t]+(.*))?$")
CLOSING_HASHES = re.compile(r"(?:^|[ \t]+)#+[ \t]*$")
SETEXT_MARKER = re.compile(r"^ {0,3}=+[ \t]*$")
FENCE = re.compile(r"^ {0,3}(~{3,}|`{3,})(.*)$")
TRANSPORT_METADATA = {"conversation_id", "sources_used", "citations"}


def heading_title(heading: re.Match[str]) -> str:
    return CLOSING_HASHES.sub("", heading[2] or "").strip()


def has_transport_envelope(body: str) -> bool:
    if not body.startswith("{"):
        return False
    try:
        parsed = json.loads(body)
    except json.JSONDecodeError:
        return False
    if not isinstance(parsed, dict):
        return False
    metadata = parsed.keys() & TRANSPORT_METADATA
    return len(metadata) >= 2 or (bool(metadata) and "answer" in parsed)


def inspect_structure(text: str) -> tuple[list[str], list[str]]:
    if not text.strip():
        return ["arquivo vazio"], []

    lines = text.splitlines()
    errors = []
    review = []
    first_heading = HEADING.fullmatch(lines[0])
    has_initial_h1 = first_heading is not None and first_heading[1] == "#"
    if not has_initial_h1 or not heading_title(first_heading):
        errors.append("H1 ATX com título na primeira linha é obrigatório")

    body_lines = lines[1:] if has_initial_h1 else lines
    if has_transport_envelope("\n".join(body_lines).strip()):
        errors.append("objeto JSON de transporte")

    sections = set()
    has_body = False
    duplicate_title = False
    has_setext_marker = False
    fence = ""
    for line in body_lines:
        fence_match = FENCE.fullmatch(line)
        if fence:
            if fence_match and fence_match[1].startswith(fence) and not fence_match[2].strip():
                fence = ""
            elif line.strip():
                has_body = True
            continue
        if fence_match and (fence_match[1][0] == "~" or chr(96) not in fence_match[2]):
            fence = fence_match[1]
            continue

        heading = HEADING.fullmatch(line)
        if heading:
            if heading[1] == "#":
                duplicate_title = True
            if heading[1] == "##":
                sections.add(heading_title(heading).casefold())
        elif SETEXT_MARKER.fullmatch(line):
            has_setext_marker = True
        elif line.strip():
            has_body = True

    if not has_body:
        errors.append("corpo vazio")
    if duplicate_title:
        errors.append("mais de um H1 ATX")
    if has_setext_marker:
        errors.append("marcador Setext fora de código; use títulos ATX")
    if {"consulta", "resposta"} <= sections:
        review.append("Confira se Consulta e Resposta são seções técnicas ou um invólucro de extração.")
    if fence:
        errors.append("cerca de código sem fechamento")
    return errors, review


def validate(path: Path) -> tuple[bool, list[str], list[str]]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return False, ["UTF-8 inválido"], []
    except OSError:
        return False, ["arquivo ilegível"], []
    errors, review = inspect_structure(text)
    return bool(text.strip()), errors, review


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
        has_text, errors, review = validate(file)
        nonempty += int(has_text)
        invalid += int(bool(errors))
        relative = file.relative_to(args.path) if args.path.is_dir() else file.name
        if errors:
            print(f"INVALID {relative}: {', '.join(errors)}")
        else:
            print(f"OK {relative}")
        for note in review:
            print(f"REVIEW {relative}: {note}")

    print(f"COUNT={len(files)}\nNONEMPTY={nonempty}\nVALID={len(files) - invalid}\nINVALID={invalid}")
    if args.expected_count is not None:
        print(f"EXPECTED={args.expected_count}")
    if not files:
        print("Nenhum arquivo Markdown encontrado.")
    count_mismatch = args.expected_count is not None and len(files) != args.expected_count
    return int(not files or invalid > 0 or count_mismatch)


if __name__ == "__main__":
    raise SystemExit(main())

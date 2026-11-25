#!/usr/bin/env python3
"""Sanitize LinkedIn profile data supplied by a guest or authorized user.

This helper performs no network requests and does not retrieve LinkedIn pages.
Use only local data supplied for editorial preparation with documented
permission. The output removes contact details, URLs, and non-editorial fields.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


SENSITIVE_KEY = re.compile(
    r"(e[-_ ]?mail|phone|telephone|mobile|contact|connection|token|"
    r"cookie|password|secret|auth|address|publicidentifier|profileid|user[-_ ]?id)",
    re.IGNORECASE,
)
EDITORIAL_KEYS = {
    "name", "fullName", "firstName", "lastName", "headline", "about",
    "summary", "occupation", "title", "jobTitle", "company", "companyName",
    "currentCompany", "experiences", "experience", "positions", "education",
    "location", "city", "country", "industry", "skills",
}
EMAIL_VALUE = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+", re.IGNORECASE)
PHONE_VALUE = re.compile(r"(?<!\w)(?:\+?\d[\d\s().-]{7,}\d)(?!\w)")
URL_VALUE = re.compile(r"""https?://[^\s<>"']+""", re.IGNORECASE)


def sanitize(value: Any, *, top_level: bool = False) -> Any:
    if isinstance(value, str):
        value = EMAIL_VALUE.sub("[e-mail removido]", value)
        value = PHONE_VALUE.sub("[telefone removido]", value)
        return URL_VALUE.sub("[link removido]", value)
    if isinstance(value, list):
        return [sanitize(item) for item in value]
    if not isinstance(value, dict):
        return value

    clean: dict[str, Any] = {}
    for key, item in value.items():
        normalized_key = re.sub(r"[^a-z0-9]", "", str(key).lower())
        if SENSITIVE_KEY.search(str(key)) or normalized_key in {"url", "profileurl"}:
            continue
        if top_level and key not in EDITORIAL_KEYS:
            continue
        clean[key] = sanitize(item)
    return clean


def load_profile(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError("Não foi possível ler o JSON local fornecido.") from exc
    if not isinstance(value, dict):
        raise ValueError("O JSON precisa conter um objeto de perfil.")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Sanitiza dados locais de perfil fornecidos com permissão."
    )
    parser.add_argument("--input", required=True, help="Arquivo JSON local fornecido pelo convidado.")
    parser.add_argument(
        "--permission-confirmed",
        action="store_true",
        help="Confirma que a pessoa autorizou o uso editorial dos dados fornecidos.",
    )
    args = parser.parse_args()
    if not args.permission_confirmed:
        print("Confirme a autorização documentada com --permission-confirmed.", file=sys.stderr)
        return 2

    try:
        profile = load_profile(Path(args.input))
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    clean_profile = sanitize(profile, top_level=True)
    if not clean_profile:
        print("O JSON não contém campos editoriais utilizáveis.", file=sys.stderr)
        return 4
    print(json.dumps(clean_profile, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

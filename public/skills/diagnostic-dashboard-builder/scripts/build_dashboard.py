#!/usr/bin/env python3
"""Render an explicitly selected, public or synthetic diagnostic snapshot."""

import argparse
import json
import re
from datetime import date
from html import escape
from pathlib import Path


CLASSIFICATIONS = {
    "sintetico": "Demonstração sintética",
    "liberado-publico": "Material liberado para divulgação",
}
STATES = {
    "pendente": "Pendente",
    "em-curso": "Em curso",
    "bloqueado": "Bloqueado",
    "concluido": "Concluído",
}
DOC_ID = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
TEMPLATE = Path(__file__).resolve().parents[1] / "assets" / "leitor.html.template"


def require_fields(obj, fields, label):
    if not isinstance(obj, dict) or set(obj) != set(fields.split()):
        raise ValueError(f"{label}: campos esperados são {fields}.")


def require_text(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label}: informe texto não vazio.")


def require_links(links, ids, label):
    if not isinstance(links, list) or any(
        not isinstance(item, str) or item not in ids for item in links
    ):
        raise ValueError(f"{label}: lista contém uma referência sem destino.")
    if len(links) != len(set(links)):
        raise ValueError(f"{label}: IDs de referência repetidos.")


def validate(data):
    require_fields(data, "titulo resumo atualizado_em classificacao marcos documentos", "Manifesto")
    for key in ("titulo", "resumo", "atualizado_em", "classificacao"):
        require_text(data[key], key)
    if data["classificacao"] not in CLASSIFICATIONS:
        raise ValueError("Use somente classificação sintetico ou liberado-publico.")
    if date.fromisoformat(data["atualizado_em"]).isoformat() != data["atualizado_em"]:
        raise ValueError("Use AAAA-MM-DD para atualizado_em.")
    if not isinstance(data["documentos"], list) or not isinstance(data["marcos"], list):
        raise ValueError("Documentos e marcos devem ser listas.")
    ids = set()
    for index, doc in enumerate(data["documentos"], 1):
        label = f"Documento {index}"
        require_fields(doc, "id titulo area versao estado texto relacionados", label)
        for key in ("id", "titulo", "area", "versao", "estado", "texto"):
            require_text(doc[key], f"{label}: {key}")
        if not DOC_ID.fullmatch(doc["id"]) or doc["id"] in ids:
            raise ValueError(f"{label}: ID inválido ou repetido.")
        ids.add(doc["id"])
    for index, doc in enumerate(data["documentos"], 1):
        require_links(doc["relacionados"], ids - {doc["id"]}, f"Documento {index}")
    for index, stage in enumerate(data["marcos"], 1):
        label = f"Marco {index}"
        require_fields(stage, "titulo estado responsavel proximo documentos", label)
        for key in ("titulo", "estado", "responsavel", "proximo"):
            require_text(stage[key], f"{label}: {key}")
        if stage["estado"] not in STATES:
            raise ValueError(f"{label}: estado desconhecido.")
        require_links(stage["documentos"], ids, label)


def render(data):
    docs = {doc["id"]: doc for doc in data["documentos"]}

    def links(ids):
        if not ids:
            return ""
        items = "".join(f'<li><a href="#doc-{i}">{escape(docs[i]["titulo"])}</a></li>' for i in ids)
        return f'<nav aria-label="Documentos relacionados"><ul>{items}</ul></nav>'

    stages = []
    for stage in data["marcos"]:
        stages.append(
            f'<li><h3>{escape(stage["titulo"])}</h3>'
            f'<p class="meta">{STATES[stage["estado"]]} · {escape(stage["responsavel"])}</p>'
            f'<p>{escape(stage["proximo"])}</p>{links(stage["documentos"])}</li>'
        )
    entries = []
    for doc in docs.values():
        title, area = escape(doc["titulo"]), escape(doc["area"])
        lookup = escape(doc["titulo"] + " " + doc["area"])
        entries.append(
            f'<article class="doc" id="doc-{doc["id"]}" data-lookup="{lookup}"><details>'
            f'<summary>{title} · {area}</summary>'
            f'<p class="meta">{escape(doc["versao"])} · {escape(doc["estado"])}</p>'
            f'<pre>{escape(doc["texto"])}</pre>{links(doc["relacionados"])}</details></article>'
        )
    replacements = {
        "titulo": escape(data["titulo"]),
        "resumo": escape(data["resumo"]),
        "classificacao": CLASSIFICATIONS[data["classificacao"]],
        "atualizado_em": escape(data["atualizado_em"]),
        "marcos": '<ul class="cards">' + "".join(stages) + "</ul>" if stages else "<p>Sem marcos neste recorte.</p>",
        "documentos": "".join(entries) if entries else "<p>Sem documentos neste recorte.</p>",
    }
    template = TEMPLATE.read_text(encoding="utf-8")
    return re.sub(r"\{\{([a-z_]+)\}\}", lambda match: replacements[match[1]], template)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifesto", type=Path)
    parser.add_argument("saida", type=Path, help="novo arquivo HTML, em pasta já existente")
    args = parser.parse_args()
    try:
        data = json.loads(args.manifesto.read_text(encoding="utf-8-sig"))
        validate(data)
        html = render(data)
        if args.saida.suffix.lower() != ".html":
            raise ValueError("A saída deve terminar em .html.")
        with args.saida.open("x", encoding="utf-8", newline="\n") as output:
            output.write(html)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Falha ao gerar o painel: {error}\n")
    print("Painel gerado. Revise o conteúdo e a visibilidade antes de distribuir.")


if __name__ == "__main__":
    main()

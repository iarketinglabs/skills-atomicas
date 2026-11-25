#!/usr/bin/env python3
"""
Bootstrap Doc Skeleton - Cria o esqueleto inicial de directives/documentacao/
==============================================================================
Gera a estrutura padrão de documentação viva (skill `system-documentation-keeper`):
um README.md de índice na raiz de directives/documentacao/ e uma subpasta por
tópico padrão, cada uma com um README.md placeholder.

100% agnóstico a cliente/stack: não lê nem escreve nada fora de directives/documentacao/,
não depende de nenhum MCP ou credencial.

Idempotente: nunca sobrescreve um arquivo já existente, só cria o que falta. Pode
ser rodado de novo com segurança se o esqueleto já existir parcialmente.

Uso:
    python bootstrap_doc_skeleton.py
    python bootstrap_doc_skeleton.py --root /caminho/do/projeto
    python bootstrap_doc_skeleton.py --project-name "Nome do Projeto"
    python bootstrap_doc_skeleton.py --directives-dir directives

Requer: Python 3.8+ (sem dependências externas)
"""

import argparse
from pathlib import Path

# Mesma lista de tópicos documentada em references/topic-skeleton.md e no SKILL.md —
# mudar aqui exige atualizar os dois em conjunto.
TOPICS = [
    {
        "id": "00-visao-geral",
        "title": "Visão Geral",
        "description": (
            "O que é o sistema, para quem serve e o glossário de termos do domínio. "
            "Ponto de entrada recomendado para PMs e para qualquer dev novo no projeto."
        ),
    },
    {
        "id": "01-arquitetura",
        "title": "Arquitetura",
        "description": (
            "Componentes do sistema, diagrama de arquitetura, stack tecnológica e "
            "decisões de design de alto nível."
        ),
    },
    {
        "id": "02-integracoes",
        "title": "Integrações",
        "description": (
            "Um arquivo por integração externa — contrato, autenticação, limites conhecidos "
            "e particularidades de cada uma."
        ),
    },
    {
        "id": "03-modelo-de-dados",
        "title": "Modelo de Dados",
        "description": (
            "Schemas de todo dado persistido pelo sistema (databases, tabelas, filas), "
            "com o significado de cada campo."
        ),
    },
    {
        "id": "04-fluxos",
        "title": "Fluxos",
        "description": "Um arquivo por fluxo de ponta a ponta do sistema.",
    },
    {
        "id": "05-operacao",
        "title": "Operação",
        "description": (
            "Deploy, variáveis de ambiente, runbook de incidentes comuns e como consultar "
            "observabilidade — o guia de quem mantém o sistema rodando no dia a dia."
        ),
    },
    {
        "id": "06-decisoes",
        "title": "Decisões",
        "description": (
            "Registro curto (estilo ADR — contexto, decisão, trade-offs) de decisões "
            "técnicas relevantes tomadas ao longo do projeto."
        ),
    },
]

SKILL_DIR = Path(__file__).resolve().parent.parent


def write_if_missing(path: Path, content: str) -> bool:
    """Cria o arquivo só se ele ainda não existir. Retorna True se criou."""
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def render(template_path: Path, replacements: dict) -> str:
    text = template_path.read_text(encoding="utf-8")
    for key, value in replacements.items():
        text = text.replace(f"{{{{{key}}}}}", value)
    return text


def bootstrap(root: Path, directives_dir: str, project_name: str) -> None:
    docs_root = root / directives_dir / "documentacao"
    assets_dir = SKILL_DIR / "assets"

    created, skipped = [], []

    root_template = assets_dir / "root-readme.template.md"
    root_readme_content = render(root_template, {"PROJECT_NAME": project_name})
    root_readme_path = docs_root / "README.md"
    if write_if_missing(root_readme_path, root_readme_content):
        created.append(root_readme_path)
    else:
        skipped.append(root_readme_path)

    topic_template = assets_dir / "topic-readme.template.md"
    for topic in TOPICS:
        topic_readme_content = render(
            topic_template,
            {"TOPIC_TITLE": topic["title"], "TOPIC_DESCRIPTION": topic["description"]},
        )
        topic_readme_path = docs_root / topic["id"] / "README.md"
        if write_if_missing(topic_readme_path, topic_readme_content):
            created.append(topic_readme_path)
        else:
            skipped.append(topic_readme_path)

    print(f"Esqueleto de documentação em: {docs_root}")
    print(f"Criados: {len(created)}")
    for p in created:
        print(f"  + {p.relative_to(root)}")
    if skipped:
        print(f"Já existiam (não sobrescritos): {len(skipped)}")
        for p in skipped:
            print(f"  = {p.relative_to(root)}")


def main():
    parser = argparse.ArgumentParser(
        description="Cria o esqueleto inicial de directives/documentacao/"
    )
    parser.add_argument(
        "--root", default=".", help="Raiz do projeto (padrão: diretório atual)"
    )
    parser.add_argument(
        "--directives-dir",
        default="directives",
        help="Nome da pasta de diretrizes na raiz do projeto (padrão: directives)",
    )
    parser.add_argument(
        "--project-name",
        default="TODO: nome do projeto",
        help="Nome do projeto/cliente, usado no título do README raiz",
    )
    args = parser.parse_args()

    bootstrap(Path(args.root).resolve(), args.directives_dir, args.project_name)


if __name__ == "__main__":
    main()

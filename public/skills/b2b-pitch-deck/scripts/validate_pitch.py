#!/usr/bin/env python3
"""
Validador rápido de pitch deck B2B complexo.
Lê um arquivo markdown ou texto com roteiro de slides e verifica
presença de elementos críticos da arquitetura de pitch B2B.

Uso:
    python validate_pitch.py <caminho_do_arquivo>
"""

import sys
import re

REQUIRED_ELEMENTS = [
    ("recomendacao", [
        r"recomendamos",
        r"nossa (leitura|tese|recomendação)",
        r"propomos",
        r"sugerimos",
    ]),
    ("impacto_economico", [
        r"custo",
        r"impacto financeiro",
        r"roi",
        r"retorno",
        r"economia",
        r"r\$",
        r"usd",
        r"milh",
        r"mil",
    ]),
    ("prova", [
        r"case",
        r"benchmark",
        r"exemplo",
        r"já vimos",
        r"cliente",
        r"resultado",
    ]),
    ("proximos_passos", [
        r"próximo(s)? passo",
        r"next step",
        r"próxima etapa",
        r"agend",
        r"data",
        r"até \d{1,2}/\d{1,2}",
    ]),
    ("metodologia_fases", [
        r"fase",
        r"etapa",
        r"módulo",
        r"sprint",
        r"semana",
        r"diagnóstico",
        r"implanta",
        r"reforço",
    ]),
]

FORBIDDEN_PATTERNS = [
    ("abertura_vendor_centric", [
        r"^slide\s*1.*quem somos",
        r"^slide\s*1.*nossa empresa",
        r"^slide\s*1.*história",
        r"^slide\s*1.*fundada em",
    ]),
]


def check_elements(text: str) -> dict:
    text_lower = text.lower()
    lines = text_lower.splitlines()
    results = {}

    for label, patterns in REQUIRED_ELEMENTS:
        found = any(re.search(p, text_lower) for p in patterns)
        results[label] = found

    # Verificar se a recomendação aparece cedo (primeiros 30% do texto ou primeiros 20 slides)
    early_text = "\n".join(lines[: max(20, len(lines) // 3)])
    recommendation_early = any(
        re.search(p, early_text) for p in REQUIRED_ELEMENTS[0][1]
    )
    results["recomendacao_cedo"] = recommendation_early

    return results


def check_forbidden(text: str) -> list:
    text_lower = text.lower()
    issues = []
    for label, patterns in FORBIDDEN_PATTERNS:
        for p in patterns:
            if re.search(p, text_lower, re.MULTILINE):
                issues.append(label)
                break
    return issues


def main():
    if len(sys.argv) < 2:
        print("Uso: python validate_pitch.py <caminho_do_arquivo>")
        sys.exit(1)

    path = sys.argv[1]
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        sys.exit(1)

    results = check_elements(text)
    forbidden = check_forbidden(text)

    print("=" * 50)
    print("VALIDAÇÃO DE PITCH B2B COMPLEXO")
    print("=" * 50)

    score = 0
    total = len(results)
    for label, found in results.items():
        status = "✅ OK" if found else "❌ AUSENTE"
        print(f"  {label:25s} {status}")
        if found:
            score += 1

    if forbidden:
        print("\n⚠️  Padrões problemáticos detectados:")
        for issue in forbidden:
            print(f"    - {issue}")

    print("\n" + "-" * 50)
    print(f"Score: {score}/{total}")
    if score == total and not forbidden:
        print("Resultado: Pitch validado com sucesso.")
    elif score >= total - 1 and not forbidden:
        print("Resultado: Pitch aceitável, mas há gaps a endereçar.")
    else:
        print("Resultado: Pitch precisa de revisão significativa antes da apresentação.")


if __name__ == "__main__":
    main()

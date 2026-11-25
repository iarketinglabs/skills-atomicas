# Template — Mapa de Processo AS-IS

Copie esta estrutura para documentar um processo mapeado. Preencha apenas os campos com dado real; marque explicitamente o que está pendente em vez de inferir ou deixar implícito.

```markdown
# Processo: <nome do processo>

**Categoria**: [Primário / Suporte / Gestão]
**Status do mapeamento**: [Preliminar / Consolidado]
**Fontes**: <entrevista com fulano, data> | <documento X> | <log de sistema Y>
**Última atualização**: <data>

## Gatilho e entrada
- Evento/solicitação que inicia o processo:
- Frequência:

## Fluxo observado
1. <etapa> — responsável: <papel> — sistema: <ferramenta>
2. ...

Decisões/bifurcações:
- <ponto de decisão> → critério: <regra de negócio>

## Atores
| Papel | Responsabilidade no processo | Sistema/ferramenta usado |
|---|---|---|

## Handoffs
| De | Para | O que é transferido | Mecanismo (notificação/fila/e-mail) | Risco observado |
|---|---|---|---|---|

## Regras de negócio
- <regra> — fonte:

## Saída e critério de encerramento
- Output final:
- Critério de "concluído com sucesso":

## Exceções
- <caso excepcional> — como é tratado hoje:

## Métricas disponíveis
| Métrica | Valor | Unidade | Período | Fonte |
|---|---|---|---|---|

## Métricas ausentes (lacunas)
- <métrica desejada e por que não existe hoje>

## Momentos da verdade (se aplicável)
- <ponto de contato com cliente externo> — expectativa vs. realidade:

## Gargalos e riscos identificados
- <gargalo> — evidência:

## Classificação de confiança dos achados
- Factual:
- Hipótese:
- Pendente:
- Contradição:
- Caso observado (não generalizar):
```

Ao consolidar este template, cruze-o com `guia-elicitacao-as-is.md` (classificação de confiabilidade) e, se o objetivo final for identificar oportunidades de IA, com `diagnostico-ia-e-redesenho.md` antes de propor qualquer automação.

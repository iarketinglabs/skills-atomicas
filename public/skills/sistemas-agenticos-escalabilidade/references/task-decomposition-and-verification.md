# Decomposição em Sub-problemas Verificáveis

Parte de **Escalabilidade e Multi-Agentes** (ver Framework Mental no `SKILL.md` e o ciclo completo em `hierarchical-planner-worker.md`). A pergunta que decide se uma tarefa é candidata a uma arquitetura multi-agente não é "a IA consegue fazer isso", mas **"esse fluxo pode ser decomposto em sub-problemas logicamente verificáveis"**.

## O princípio da verificabilidade

Uma tarefa é viável de ser delegada a uma infraestrutura multi-agente de forma robusta se, e somente se, o resultado final puder ser classificado deterministicamente como correto ou incorreto por um teste automatizado ou um critério objetivo — uma porta de qualidade, não um julgamento subjetivo.

**Domínios altamente verificáveis:** geração de código (linter e testes unitários provam a integridade), problemas matemáticos, conformidade baseada em regras explícitas de um playbook, triagem automatizada de incidentes contra critérios definidos.

**Domínios pouco verificáveis:** julgamento estético, redação criativa aberta, decisões de negócio sem métrica objetiva — nesses casos, paralelizar não converte poder computacional em confiabilidade, só multiplica o custo sem garantia de melhora.

## Convertendo computação em confiabilidade

Quando o domínio é verificável, a arquitetura multi-agente converte de fato poder computacional (mais tokens gerados em paralelo) em confiabilidade real: o sistema testa e valida dezenas de alternativas autonomamente até uma passar na barreira de sucesso, em vez de aceitar a primeira resposta de um único agente.

## Implementer-Reviewer-Resolver

```
IMPLEMENTER (Ator)  ──► código/rascunho ──►  REVIEWER (Juiz, contexto limpo)
     ▲                                              │
     └──────────── lista de falhas ─────────────────┘
     │ (se aprovado)
     ▼
OUTPUT CONSOLIDADO
```

Uma variação nomeada do padrão Juiz (ver a versão completa com os quatro vereditos em `hierarchical-planner-worker.md`), com um terceiro papel explícito:

1. **Implementer:** gera o rascunho bruto na própria sandbox isolada.
2. **Reviewer/Juiz:** contexto limpo, avalia adversariamente contra a porta de qualidade.
3. **Resolver:** se falhas forem identificadas, um terceiro agente isolado recebe as diretrizes do revisor e faz os ajustes cirúrgicos até o crivo conceder aprovação.

Separar explicitamente quem corrige de quem julga (em vez de o Juiz corrigir diretamente) mantém cada papel focado em uma única responsabilidade cognitiva.

## Exemplo de decomposição paralela com verificação

```python
def run_pipeline(dataset):
    # Decompõe o problema em chunks independentes e executa em paralelo
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(worker_audit, chunk) for chunk in dataset]
        reports = [f.result() for f in as_completed(futures)]

    # O Juiz consolida os relatórios: qualquer item que falhou vira uma anomalia rastreável
    failed = [r for r in reports if r["status"] == "FAILED"]
    decision = "REJECTED_WITH_FEEDBACK" if failed else "APPROVED"
    return {"decision": decision, "anomalies": failed, "total": len(reports)}
```

Cada worker processa um sub-problema isolado e devolve um veredito estruturado (não texto livre) — é essa estrutura verificável que permite ao orquestrador consolidar o resultado sem precisar de outro agente para "interpretar" a saída.

## Checklist

- Antes de paralelizar, confirme que o domínio é verificável — se não há um critério objetivo de sucesso, paralelizar só multiplica custo.
- Cada sub-problema decomposto devolve um veredito estruturado (schema fixo), não texto livre a ser reinterpretado.
- O papel de corrigir (Resolver) é separado do papel de julgar (Reviewer) — o mesmo agente não faz as duas coisas.

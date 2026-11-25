# O Ciclo de Melhoria Contínua

Fonte canônica única deste ciclo — referenciada (não copiada) por `../references/tracing-inputs-outputs.md` e `../references/assertiveness-and-performance-metrics.md`. Traces e métricas não são só ferramentas de depuração reativa — são o combustível para a evolução ativa do comportamento de um agente ao longo do tempo.

## O ciclo

```
1. TELEMETRIA ATIVA        → tracing de spans, captura de erros
2. TRIAGEM / CURADORIA     → filtro de falhas, isolamento de causa raiz
3. CURADORIA DE DATASETS   → exemplos positivos (few-shot) e negativos (guardrails)
4. FINE-TUNING / PROMPTS   → treino local ou ajuste de prompt com dados reais
5. DEPLOY MONITORADO       → shadow deployment, teste canário
6. EVALS EM PRODUÇÃO       → valida se a mudança realmente melhorou, fecha o ciclo
```

## Curadoria de exemplos

- **Exemplos positivos (golden paths):** traces classificados com nota de excelência por um Juiz (ver `llm-as-a-judge-pattern.md`) são higienizados e passam a compor bibliotecas de exemplos de poucas tentativas (*few-shot*) — o comportamento exemplar do passado guia execuções futuras.
- **Exemplos negativos (guardrails cognitivos):** traces de execuções que resultaram em falha grave, loop de erro ou estouro de custo são documentados e inseridos como aviso explícito: "em execuções anteriores, o agente falhou ao fazer X — evite esse caminho".

## Por que não pular direto para fine-tuning

Adicionar exemplos ao prompt (few-shot) é reversível, barato e imediato — a primeira linha de defesa contra um padrão de erro recorrente. Fine-tuning de um modelo menor com dados reais só compensa depois de acumular um volume estatisticamente representativo de traces higienizados — é a ferramenta de última milha para reduzir custo transferindo conhecimento de um modelo caro para um modelo pequeno especializado, não o primeiro recurso diante de um erro pontual.

## Higiene obrigatória antes de qualquer curadoria

Nenhum trace entra em um dataset de treino ou few-shot sem antes passar por redação de PII e segredos — ver o desenvolvimento completo desse controle na skill de Segurança e Confiabilidade desta coleção, se disponível. Um dataset de melhoria contínua que vaza dados de cliente é, ele mesmo, um incidente de segurança.

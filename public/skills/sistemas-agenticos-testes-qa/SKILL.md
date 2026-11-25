---
name: sistemas-agenticos-testes-qa
description: Planeje, revise e audite estratégias de Testes e QA orientadas a risco para software convencional e sistemas agênticos. Use quando for necessário definir níveis e técnicas de teste, montar release gates, investigar regressões, avaliar ferramentas/estado/trajetórias de agentes, desenhar checklists de go-live ou transformar incidentes em regressões. Encaminhe para ai-evals quando a tarefa principal for implementar harnesses, métricas ou rubricas de eval; encaminhe para ai-stress-testing quando for carga, stress, spike, soak ou performance.
---

# Testes & QA

## Overview

Produza evidência útil sobre qualidade e risco; não trate um teste verde, cobertura ou benchmark como prova universal de correção. Para software comum, combine processo de QA, controle de produto, testes em níveis adequados e exploração. Para agentes, avalie `tarefa -> trajetória -> estado final`, incluindo side effects, política, segurança, variabilidade e capacidade de escalar.

## Roteamento

Use esta skill como coordenadora de estratégia. Consulte as referências somente conforme o caso:

- `references/software-testing-foundations.md`: software determinístico, técnicas de design, exploração, performance e segurança.
- `references/agentic-quality-evaluation.md`: agentes, trials, traces, tool calls, estado, segurança e falhas.
- `references/checklists-and-templates.md`: checklists e templates para registrar testes/evals.
- `references/evidence-and-sources.md`: fontes, proveniência e limites de interpretação.
- `references/kanban-dashboard.md`: dashboard kanban local (opcional) para visualizar e mover manualmente o status dos casos de teste do template acima.

Não duplique especialidades:

- Métricas, datasets, LLM-as-Judge, faithfulness e gates de eval: use `ai-evals`.
- Load, stress, spike, soak, race condition e capacidade: use `ai-stress-testing`.
- Autorização, threat model, isolamento ou enforcement de permissões: use `sistemas-agenticos-seguranca`.
- SLOs, retries, degradação controlada e contratos de integração: use `sistemas-agenticos-resiliencia`.
- Tracing, métricas de assertividade/performance e human-in-the-loop em produção: use `sistemas-agenticos-observabilidade`.

Esta skill faz parte da coleção `sistemas-agenticos-*` (ver `../sistemas-agenticos-README.md`) — mesmas regras de composição: referencie as demais skills da coleção pela interface com o tema de testes, nunca duplique a política canônica delas aqui.

## Workflow de estratégia

### 1. Delimitar objetivo, risco e evidência

Registre antes de escolher testes:

- objetivo de negócio ou de segurança;
- evento indesejado, impacto e prioridade;
- test basis: requisito, história, contrato, arquitetura, política ou incidente;
- objeto e fronteiras sob teste;
- ambiente, dados, estado inicial e dependências;
- oráculo: resultado esperado, estado esperado, invariantes e evidência;
- critério de saída e responsável.

Se não houver oráculo ou estado observável suficiente, marque a avaliação como `blocked` ou `inconclusive`; não invente um resultado esperado.

### 2. Selecionar o portfólio

Escolha o teste menor que detecte o risco com fidelidade suficiente e complemente-o quando necessário:

- componente: regras locais, bordas, exceções e cálculos;
- integração/contrato: schemas, serialização, auth, timeout, retry, idempotência e dependências;
- sistema/E2E: jornadas críticas, configuração e side effects;
- aceitação: valor, operação, suporte e critérios do usuário;
- exploratório: riscos desconhecidos usando `SFDIPOT` e fontes de consistência como `FEW HICCUPPS`;
- não funcional: capacidade, estabilidade, segurança, recuperação e degradação controlada.

Use particionamento de equivalência e valores-limite para domínios; tabelas de decisão para combinações; transições de estado para comportamento dependente do histórico. Use TDD para design local, ATDD/BDD para esclarecer aceitação e shift-left quando a ambiguidade puder ser removida antes do código.

Não imponha proporções universais à pirâmide. Otimize velocidade, fidelidade, diagnóstico e custo de manutenção. Se um teste menor detectar o mesmo risco que um E2E, prefira o menor e mantenha E2E para jornadas cujo risco depende do sistema completo.

### 3. Executar e preservar evidência

Para cada execução, preserve comando/configuração, versão, ambiente, dados, resultado, logs e artefatos suficientes para diagnóstico. Diferencie:

- `pass`: critério e evidência atendidos;
- `fail`: critério não atendido, com evidência reproduzível;
- `blocked`: não foi possível executar ou observar o critério;
- `inconclusive`: execução ocorreu, mas a evidência não sustenta uma decisão.

Não transforme rerun até passar em correção de flaky test. Investigue se a variância vem do produto, teste, grader, ambiente, dependência externa ou estado residual.

Para acompanhar visualmente a execução de um caderno com muitos casos, `references/kanban-dashboard.md` documenta uma ferramenta opcional (dashboard kanban local, sem framework) que lê os casos escritos no template desta seção e permite movê-los manualmente entre colunas de status — não substitui o registro de `RESULTADO` no `.md` de cada caso, só dá uma visão movível sobre ele.

### 4. Acrescentar a camada agêntica

Quando houver LLM, memória, ferramentas, autonomia ou coordenação:

1. Congele e versione modelo, prompts, harness, schemas, políticas, dataset, grader, ambiente e estado inicial.
2. Separe `outcome` real de transcript e resposta declarada pelo agente.
3. Verifique o estado final diretamente e confira side effects permitidos e proibidos.
4. Teste necessidade, seleção, argumentos, autorização, resultados vazios/contraditórios, timeout, retry, idempotência e confirmação humana de tool calls.
5. Execute trials independentes quando houver variabilidade; compare distribuição, famílias de falha, severidade, custo e eficiência, não apenas uma execução.
6. Preserve trace com mensagens relevantes, tool calls/outputs, handoffs, guardrails, confirmações, mutações e estado final.
7. Para multi-turn ou long-horizon, teste retenção de objetivo/restrições, compaction, interrupção, retomada, loops, término e escalada.
8. Para multi-agente, teste routing, handoff, autoridade, estado compartilhado, duplicação, deadlock, conflito e atribuição causal.
9. Teste conteúdo não confiável, prompt injection direta/indireta, exfiltração, memória contaminada, permissões excessivas e escape de isolamento conforme o escopo.

Não exija uma sequência exata de tool calls se existirem caminhos legítimos alternativos. Torne invariantes de segurança, autorização, aprovação humana e side effects obrigatórios quando forem requisitos do processo.

### 5. Julgar e fechar o ciclo

Prefira, nesta ordem, verificadores determinísticos para schema/estado/política, rubric/model judge para semântica aberta e humanos para calibração, alto risco ou arbitragem. Separe outcome, processo/trajetória, segurança, política, eficiência e custo; nunca esconda uma falha crítica em uma média.

Classifique a falha causal — intenção, planejamento, seleção/invocação/interpretação de ferramenta, grounding, estado, recuperação, política, autorização, coordenação, sistema, terminação ou segurança — e registre a primeira etapa causal conhecida. Um incidente reproduzível deve gerar caso de teste, evidência de referência, invariante, regressão e decisão documentada.

## Gate de release

Antes de recomendar go-live, confirme:

- requisitos e riscos críticos possuem oráculos verificáveis;
- regressões de baixo tempo de execução, contratos, integrações e jornadas críticas foram executados;
- não funcionais e segurança foram cobertos conforme o risco;
- ambiente, dados e estado inicial são reproduzíveis ou as limitações estão explícitas;
- agentes têm outcome/estado, trajetória, permissões, orçamento e trials avaliados;
- falhas críticas têm owner, rollback/recuperação e observabilidade;
- incidentes relevantes alimentam a suite.

Se um requisito crítico estiver falhando, sem evidência ou sem controle de recuperação, recomende `não liberar` ou `liberação condicionada` com o risco explícito.

## Recursos

- [Fundamentos de software](references/software-testing-foundations.md)
- [Avaliação agêntica](references/agentic-quality-evaluation.md)
- [Checklists e templates](references/checklists-and-templates.md)
- [Evidência e fontes](references/evidence-and-sources.md)
- [Dashboard kanban do caderno de testes](references/kanban-dashboard.md). Para criar uma cópia local com Node.js e permissão de escrita no destino, use o script [instantiate-kanban-dashboard.mjs](scripts/instantiate-kanban-dashboard.mjs) na raiz do pacote. Sem terminal, siga a opção de cópia manual.

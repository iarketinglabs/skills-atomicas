---
name: sistemas-agenticos-autoaprimoramento
description: "Use when designing, evaluating, or governing iterative self-improvement in AI agents, including prompt or program optimization, workflow changes, skill or memory updates, self-generated training data, continual learning, or code/weight self-modification. Apply this skill whenever an agent's persistent behavior or improvement process may change; distinguish a one-off response edit from a durable system change."
---

# Autoaprimoramento de Sistemas Agênticos

Conduza ciclos de melhoria com evidência reproduzível, limites explícitos e reversão preparada. Uma proposta do próprio agente é uma hipótese; só há melhoria demonstrada quando uma avaliação adequada, independente e fora do processo de seleção confirma o ganho sem ultrapassar os limites de risco definidos.

## Escopo

Use esta skill para alterações persistentes ou repetidas em agentes: instruções, prompts, estratégias, ferramentas, código, habilidades, memória, dados de treino, pesos, mecanismo de avaliação ou processo que propõe e aprova mudanças. Para editar uma resposta isolada sem alterar comportamento futuro, conclua apenas a tarefa corrente.

Não assuma fornecedor, modelo, stack, jurisdição, tamanho da organização ou disponibilidade de memória, sandbox, avaliador automático ou aprovação humana. Se um controlo não existir no runtime, registe a lacuna e reduza o escopo/autonomia da experiência.

## Regras de segurança e evidência

- Separe quem propõe a mudança de quem mede e aprova o resultado. Um agente pode ajudar a criticar a própria proposta, mas a autocrítica não substitui um sinal externo adequado à tarefa.
- Preserve a versão atual e o avaliador antes de começar. O candidato não pode editar, ler respostas futuras ou escolher os casos do conjunto usado para decidir sua promoção.
- Defina métrica, efeito mínimo relevante, guardrails e regra de parada antes de observar o resultado. Score maior por si só não basta.
- Limite iterações e pelo menos um recurso operacional (tempo, tokens ou custo). Interrompa ao atingir o limite, diante de falha crítica, evidência inválida, divergência não resolvida ou regressão acima do tolerado.
- Execute código ou mudanças de alto impacto em ambiente isolado, com privilégio mínimo e sem credenciais de produção. Separe desenvolvimento, avaliação e produção.
- Não persista uma observação como regra geral sem proveniência, escopo, finalidade autorizada, proprietário e processo de revisão/retirada.
- Exija aprovação humana antes de alterar pesos, avaliadores, código com efeitos externos, memória partilhada ou comportamento de alto impacto, e antes de alargar um rollout que a política da organização classifique como sensível.
- A skill e os scripts ajudam a organizar evidência; não certificam segurança, causalidade, validade estatística, conformidade legal ou autorização de lançamento.

## Ciclo de trabalho

1. **Defina a decisão.** Registe o problema observado, quem é afetado, a tarefa e distribuição de uso, a versão atual, o dono do sistema e a decisão que a evidência deve suportar. Separe factos, hipóteses e preferências.
2. **Escolha a menor superfície de mudança.** Classifique a proposta como ajuste de saída, instrução/contexto, memória/habilidade, workflow/ferramenta, código/avaliador ou pesos. Prefira a camada menos persistente e menos privilegiada que possa resolver o problema. Consulte `references/change-surfaces.md`.
3. **Prepare a linha de base.** Fixe versões do agente, ferramentas, dados e avaliador. Defina métrica principal, efeito mínimo prático, guardrails, casos críticos, critério de aceitação e rejeição e orçamento máximo. Registe como os exemplos foram selecionados e quais foram usados para desenvolver a mudança.
4. **Proteja a avaliação.** Mantenha casos de desenvolvimento separados dos casos usados para decisão final. Use a mesma amostra para comparar baseline e candidato quando fizer sentido; verifique leakage, duplicados, dependências e reuso adaptativo. Use avaliadores externos/determinísticos quando disponíveis e revisão humana para critérios semânticos ou de impacto. Consulte `references/evaluation-protocol.md`.
5. **Proponha e limite o ciclo.** Faça uma mudança por vez ou registe claramente as mudanças agrupadas. Defina `max_iterations` e tetos de tempo, tokens ou custo. Termine quando o ganho marginal ficar abaixo do efeito mínimo, quando não houver progresso após o orçamento, ou quando surgir qualquer condição de interrupção.
6. **Execute com contenção.** Mantenha o candidato num branch, snapshot, cópia ou ambiente isolado. Restrinja ferramentas, identidade, dados e rede ao necessário. Nunca permita que o agente candidato altere o baseline, o conjunto protegido, o avaliador ou o registo de auditoria.
7. **Avalie sem esconder perdas.** Compare a mesma tarefa em condições comparáveis; reporte média e distribuição, tamanho da amostra, incerteza/método, custos e falhas críticas. Analise tarefas importantes e guardrails separadamente. Ganho médio não compensa regressão crítica. Não chame um score selecionado no conjunto de desenvolvimento de ganho generalizável.
8. **Tome uma decisão explícita.** Escolha `promote`, `hold` ou `reject` e ligue a decisão aos critérios definidos antes do ensaio. `Hold` quando a evidência é insuficiente; `reject` quando há dano ou falha de gate. Promoção requer artefacto versionado, referência de rollback, aprovador adequado ao risco e plano de rollout. Nunca trate a saída de `validate_cycle.py` como autorização automática.
9. **Faça rollout controlado e aprenda.** Comece em modo sombra ou numa população limitada quando viável. Acompanhe métricas de resultado, segurança, custo e sinais de falha; defina quem pode interromper. Reverta se uma condição for acionada. Só transforme o resultado em memória/habilidade reutilizável depois de confirmar o escopo, guardar proveniência e definir revisão ou expiração.

## Nível de controlo por risco

| Superfície/impacto | Controlo mínimo antes de promover |
|---|---|
| Resposta isolada, sem persistência | Verificar factos e cumprir o pedido; não iniciar ciclo de mudança durável. |
| Instrução, contexto ou habilidade reutilizável | Baseline e regressões em tarefas representativas; versão, escopo, dono e reversão. |
| Memória partilhada ou mudança de workflow/ferramenta | Proveniência e autorização dos dados, isolamento de escopo, avaliação independente e aprovação conforme política. |
| Código executável, avaliador, pesos ou ação externa | Sandbox, menor privilégio, avaliador/conjunto imutáveis, orçamento estrito, testes de segurança e regressão, aprovação humana e rollback testável antes do rollout. |

Esta tabela é um ponto de partida operacional, não uma classificação normativa. A organização deve elevar o controlo quando o impacto potencial, a irreversibilidade, a exposição de dados ou a autonomia aumentarem.

## Parar e escalar

Suspenda promoção e preserve os artefactos quando ocorrer qualquer um destes casos:

- O agente ou uma pessoa alterou o avaliador, os casos protegidos ou o critério de sucesso durante a seleção.
- A melhoria existe apenas no conjunto de desenvolvimento, em amostra pequena enviesada, num único juiz ou em repetições não contabilizadas.
- Uma falha crítica, violação de privacidade, acesso indevido, comportamento não autorizado ou regressão relevante apareceu.
- Não há versão anterior restaurável, contenção adequada, dono responsável ou autorização para a ação proposta.
- O limite de iterações/recursos foi atingido, o resultado é inconclusivo, ou o agente tenta ampliar o seu próprio acesso ou a sua autonomia.

Não reinicie o mesmo ciclo com critérios mais permissivos para resgatar um resultado. Faça nova proposta, versão de avaliação e autorização quando a causa estiver compreendida.

## Entrega recomendada

Para uma decisão de melhoria durável, apresente nesta ordem:

1. **Decisão:** problema, superfície alterada, estado `promote` / `hold` / `reject`.
2. **Evidência:** baseline, candidato, amostra, método, avaliador, métrica, guardrails, falhas e incerteza.
3. **Limites:** iterações e recursos usados/permitidos; casos não cobertos.
4. **Risco e governação:** contenção, dados, permissões, aprovador e pendências.
5. **Operação:** rollout, monitorização, condições de parada e rollback.
6. **Aprendizagem persistente:** o que pode ser reutilizado, em que âmbito, com que proveniência e data de revisão/expiração.

## Recursos da skill

Leia apenas a referência necessária à tarefa:

- `references/change-surfaces.md` — tipos de mudança, profundidade e trade-offs.
- `references/evaluation-protocol.md` — linha de base, conjunto protegido, comparação e critérios de aceitação.
- `references/governance-and-containment.md` — papéis, segurança, privacidade, aprovação, rollout e rollback.
- `references/evidence-and-sources.md` — limitações das evidências recebidas e leituras primárias.
- `references/cycle-record.md` — formato do registo e uso dos scripts.

Modelos e ferramentas:

- `assets/improvement-charter.template.md` para iniciar e delimitar um ciclo.
- `assets/cycle-record.template.json` e `assets/cycle-record.example.json` para registo auditável.
- `assets/paired-evals.example.json` para comparar resultados pareados.
- `scripts/validate_cycle.py` verifica estrutura e gates declarados; `scripts/compare_paired_results.py` resume diferenças pareadas. Ambos usam apenas a biblioteca padrão Python 3.
- `evals/evals.json` e `evals/rubric.md` contêm cenários e critérios de avaliação reutilizáveis.

## Verificação final

Antes de recomendar uma promoção, confirme: mudança e versões identificadas; linha de base reproduzível; avaliador e dados de decisão protegidos; orçamento respeitado; efeito mínimo e guardrails satisfeitos; falhas críticas resolvidas; dados/memória autorizados; aprovação necessária registada; rollout limitado; observabilidade e reversão disponíveis. Se algo faltar, mantenha `hold` e diga exatamente qual evidência ou controlo falta.

# Checklists e Templates

## Release de software convencional

- [ ] Requisitos, critérios de aceitação, riscos e oráculos estão claros.
- [ ] Partições, limites, decisões, estados e exceções críticas foram cobertos.
- [ ] Contratos, serialização, autenticação, timeouts, retries e idempotência foram testados.
- [ ] Jornadas críticas têm E2E; testes menores cobrem o que não depende do sistema completo.
- [ ] Estado inicial, dados e dependências são isoláveis ou suas limitações estão registradas.
- [ ] Exploração tem charter e usa SFDIPOT/FEW HICCUPPS quando apropriado.
- [ ] Performance, segurança, recuperação e degradação foram avaliadas conforme o risco.
- [ ] Flaky tests têm investigação e owner; não são apenas repetidos até passar.
- [ ] Falhas geram artefatos diagnósticos, rollback/recuperação e owner.

## Go-live de sistema agêntico

- [ ] Task ID, hipótese, outcome, ações proibidas e invariantes estão versionados.
- [ ] Modelo, prompts, harness, memória, políticas, schemas, dataset e grader têm versão.
- [ ] Estado inicial, reset, ground truth, clock/timezone e dependências estão controlados.
- [ ] Há trials independentes e análise de variância/famílias/severidade.
- [ ] Estado final e side effects são verificados diretamente.
- [ ] Trace contém mensagens relevantes, tools, outputs, handoffs, guardrails, aprovações e mutações.
- [ ] Tool calling cobre no-call, seleção, argumentos, autorização, erros, retry e duplicação.
- [ ] Multi-turn/long-horizon cobre retenção, recuperação, loops, término e escalada.
- [ ] Multi-agente cobre routing, handoff, autoridade, concorrência, conflitos e atribuição.
- [ ] Injeção direta/indireta, exfiltração, memória, permissões e isolamento foram testados.
- [ ] Graders determinísticos precedem judges; judges têm rubrica e calibração humana.
- [ ] Budget, timeout, turns, tool calls e custo estão registrados.
- [ ] Regressão, monitoramento, disable/kill path, rollback e owner de incidente existem.

## Red team e operação contínua

- [ ] Ativos, trust boundaries, credenciais, tools com side effect e fontes não confiáveis estão mapeados.
- [ ] Ataques cobrem usuário, conteúdo externo, tool output, memória, peer e pedido de bypass.
- [ ] Defesa cobre provenance, autorização fora do modelo, least privilege, sandbox, egress e aprovação.
- [ ] Incidentes podem ser reproduzidos em ambiente seguro e sanitizados em eval.
- [ ] Mudanças de modelo, prompt, tool schema, permissão ou canal acionam regressão apropriada.
- [ ] Alertas têm owner; safe shutdown e plano de recuperação são testados.

## Template de caso de teste

```text
TEST_ID:
TÍTULO:
OWNER:
TEST_BASIS: requisito | história | contrato | arquitetura | incidente
RISCO: evento | impacto | prioridade
OBJETO E FRONTEIRAS:
NÍVEL: componente | integração | sistema | aceitação
TÉCNICA: partição | limite | decisão | transição | caixa-branca | exploratório
PRECONDIÇÕES E DADOS:
ESTADO_INICIAL:
PASSOS/AÇÃO:
ORÁCULO: resultado | estado | invariantes
AMBIENTE:
EVIDÊNCIA: logs | resposta | banco | trace | screenshot
RESULTADO: pass | fail | blocked | inconclusive
FALHA/CAUSA/OWNER:
VERSÕES E ÚLTIMA EXECUÇÃO:
```

## Template de eval agêntico

```text
EVAL_ID / OWNER / RISK_CLASS:
BUSINESS_GOAL / HYPOTHESIS:
TASK: input | contexto | ground truth oculto
CONFIG: modelo | prompt | harness | memória | política
TOOLS: nomes | schemas | permissões | credenciais escopadas
ENVIRONMENT: snapshot | estado inicial | reset | serviços
BUDGET: turns | tools | compute/tokens | timeout | retry
PERTURBATION: none | injection | erro | output envenenado | memória | peer
SUCCESS: resposta | estado final | side effects proibidos
INVARIANTS: must_do | must_not_do | aprovação humana
GRADERS: determinístico | model-based | humano
TRIALS: quantidade | independência | variáveis controladas
TRACE: mensagens | tools | handoffs | guardrails | mutações | estado final
RESULTS: outcome | segurança | política | tools | recovery | eficiência | variância
FAILURE_CLASS / FIRST_CAUSAL_STEP / ROOT_CAUSE:
REGRESSION_DECISION / PRODUCTION_LINK:
VERSÕES: dataset | grader | última execução
```

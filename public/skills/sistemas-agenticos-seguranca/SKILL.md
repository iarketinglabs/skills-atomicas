---
name: sistemas-agenticos-seguranca
description: "Framework para proteger sistemas com agentes contra vazamento, abuso de identidade, prompt injection, uso indevido de ferramentas, memória contaminada, supply chain e efeitos externos. Use ao definir threat model, capability envelope, autorização fora do modelo, sandbox, egress, PII, MCP, aprovação, auditoria ou contenção. Não substitui implementação, auditoria formal ou política final de produção."
---

# Segurança de Sistemas Agênticos

## Quando usar

- Modelar risco quando um sistema combina modelo, harness, memória, dados, ferramentas e efeitos externos.
- Definir identidade, delegação, menor privilégio e menor agência de agentes e subagentes.
- Conter prompt injection direta ou indireta, confused deputy, exfiltração, execução de código e ações destrutivas.
- Avaliar MCP, plugins, skills, dependências, modelos, schemas, RAG e outros componentes da cadeia de suprimentos.
- Projetar gates de memória, validação de output, sandbox, egress, aprovação humana, auditoria e revogação.
- Transformar incidentes e riscos em controles verificáveis e regressões de segurança.

## Quando não usar

- Para escrever a configuração final de RLS, IAM, sandbox, pipeline ou ferramenta específica.
- Para escolher fornecedor de tracing, banco, modelo ou plataforma.
- Para definir SLOs, retries ou degradação sem uma decisão de segurança; encaminhe para `sistemas-agenticos-resiliencia`.
- Para implementar harness, memória, observabilidade ou evals completos; use as skills irmãs e mantenha aqui a política de segurança.

## Modelo mental

Um agente não é apenas um LLM. O risco operacional emerge da composição:

`modelo + instruções + harness + memória + dados + ferramentas + identidade + ambiente + efeitos`

A **Tríade Letal** localiza rapidamente o risco quando coexistem:

1. acesso a dados privados;
2. exposição a conteúdo não confiável;
3. capacidade de ação externa.

Quebrar uma perna reduz o impacto, mas não elimina a necessidade de defesa em profundidade. System prompts e detectores de injection são sinais auxiliares; autorização, validação e isolamento devem existir fora do modelo.

## Fluxo operacional de segurança

Aplique esta ordem e registre as decisões:

1. **Ativos e impacto:** dados, segredos, recursos, efeitos e reversibilidade.
2. **Fronteiras de confiança:** usuário, agente, subagente, ferramenta, servidor, fonte recuperada, memória e ambiente.
3. **Identidade e delegação:** quem iniciou, em nome de quem, qual intenção, qual cadeia de delegação e qual recurso será afetado.
4. **Capability envelope:** operações, objetos, domínios, volume, duração, egress e limites que o agente pode usar nessa tarefa.
5. **Autorização determinística:** política externa ao LLM, validação de argumentos, reautorização contextual e deny-by-default para efeitos destrutivos.
6. **Validação de entrada e saída:** separar dados de instruções, validar schema, escapar conteúdo e rejeitar resultados ambíguos ou fora do contrato.
7. **Telemetria segura:** registrar identidade, decisão de política, proveniência, aprovação, ferramenta, efeito e erro sem payload sensível.
8. **Contenção:** revogar identidade, bloquear capacidades, abrir circuito, isolar dependência e preservar evidência.

Para uma implementação detalhada do fluxo, leia `references/agentic-security-control-plane.md`.

## Princípios de decisão

- **Menor privilégio:** conceda apenas acesso necessário ao recurso necessário.
- **Menor agência:** reduza funções, autonomia, duração, volume e reversibilidade, mesmo quando a identidade é legítima.
- **Policy outside the model:** o modelo pode propor uma ação; um policy engine decide se ela é permitida.
- **Reautorização contextual:** reavalie a autorização quando mudarem objetivo, recurso, destinatário, escopo ou efeito.
- **Validação na fronteira:** valide schema, tipos, valores, destino, estado e idempotência antes de cada side effect.
- **Proveniência:** preserve origem, versão, integridade, confiança e caminho de correção para conteúdo, ferramentas e memória.
- **Fail closed e revogação dentro do prazo definido:** ausência de política, identidade, confirmação ou dependência íntegra deve bloquear ou degradar sem ampliar dano.
- **Observabilidade sem vazamento:** telemetria deve provar o que ocorreu sem copiar segredos, PII, prompts privados ou tokens.

## Mapa de referências

| Decisão | Referência |
|---|---|
| Plano de controle, capability envelope e riscos agênticos | `references/agentic-security-control-plane.md` |
| Evidência temporal, frameworks e debates | `references/security-evidence-and-frameworks.md` |
| Autenticação versus autorização | `references/authentication-vs-authorization.md` |
| Identidade e cadeia de delegação | `references/agent-identity.md` |
| Escopos, confused deputy e efeitos externos | `references/api-scoping-and-permissions.md` |
| Conteúdo não confiável e prompt injection | `references/prompt-injection-prevention.md` |
| MCP e supply chain | `references/malicious-mcp-monitoring.md` |
| Memória, PII e dados persistentes | `references/pii-redaction.md` e `../sistemas-agenticos-memoria/references/memory-lifecycle-and-provenance.md` |
| Sandbox e egress | `references/sandbox-isolation-data-protection.md` |
| Output handling e verificações | `references/agentic-threat-modeling-and-verification.md` e `references/testing-unit-and-e2e.md` |

## Interfaces com a coleção

- **Harness:** consulte `sistemas-agenticos-harness` para execução, orquestração e isolamento; esta skill define o que precisa ser enforced fora do modelo.
- **Memória:** consulte `sistemas-agenticos-memoria` para retenção e retrieval; escritas privilegiadas, proveniência, quarentena, expiração e purge são requisitos de segurança.
- **Observabilidade:** consulte `sistemas-agenticos-observabilidade` para traces e métricas; identidade, política, proveniência, side effect e revogação devem ser correlacionáveis sem registrar dados sensíveis.
- **Resiliência:** consulte `sistemas-agenticos-resiliencia` para circuit breaker, bulkhead e degradação; use-os como mecanismos de contenção, não como autorização.
- **Testes/QA:** consulte `sistemas-agenticos-testes-qa` para estratégia e evidência; converta cada controle crítico em invariante ou regressão.

## Como usar

1. Classifique o pedido por ativo, fronteira de confiança e efeito possível.
2. Leia apenas as referências necessárias e combine-as quando o risco cruzar dados, conteúdo e ação.
3. Separe controles normativos estáveis de hipóteses, números, frameworks e alegações dependentes de versão.
4. Especifique enforcement, evidência esperada, owner, condição de bloqueio e caminho de revogação.
5. Teste a política com entradas confiáveis, adversariais, ambíguas, vazias, duplicadas e fora de escopo.

## Anti-padrões

| Anti-padrão | Sintoma | Referência |
|---|---|---|
| Instructions as boundary | Confiar apenas em system prompt ou guardrail textual | `references/instructions-are-not-security-boundaries.md` |
| Confused deputy | Agente legítimo usa autoridade em favor de instrução não autorizada | `references/api-scoping-and-permissions.md` |
| Excessive agency | Função, permissão, autonomia e duração amplas por conveniência | `references/agentic-security-control-plane.md` |
| Memory poisoning | Conteúdo externo vira fato, regra ou skill sem proveniência e revisão | `../sistemas-agenticos-memoria/references/memory-lifecycle-and-provenance.md` |
| Output trust | Resultado do modelo ou de outro agente é executado sem schema e policy check | `references/agentic-threat-modeling-and-verification.md` |
| Supply-chain trust | Ferramenta, skill, modelo ou schema é carregado sem inventário, integridade ou allowlist | `references/malicious-mcp-monitoring.md` |
| Shadow identity | Agente ou subagente opera sem registro, escopo e trilha de delegação | `references/agent-identity.md` |
| Confirmation fatigue | Aprovações frequentes viram cliques automáticos | `assets/trust-ladder.md` |

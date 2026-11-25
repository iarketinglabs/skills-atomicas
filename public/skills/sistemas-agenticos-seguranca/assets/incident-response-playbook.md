# Playbook de Resposta a Incidentes de Agentes

Fonte canônica única deste playbook — referenciado (não copiado) por `../references/agent-identity.md`, `../references/api-scoping-and-permissions.md`, `../references/pii-redaction.md`, `../references/malicious-mcp-monitoring.md` e `../references/prompt-injection-prevention.md`. Estrutura de contenção para quando um agente é comprometido (credencial vazada, prompt injection bem-sucedida, MCP malicioso, escopo violado) — a velocidade de reação precisa ser de nível de máquina, porque um agente autônomo comprometido propaga dano em milissegundos, não minutos.

## Fase 1 — Identificação e Alerta

O gateway de auditoria (conectado a uma ferramenta de tracing centralizada) emite alerta imediato ao detectar qualquer um destes sinais: violação consecutiva de uma porta de qualidade, estouro abrupto de cota financeira de tokens, bloqueio repetido de comando por um hook de segurança, ou acesso a um recurso fora do escopo homologado.

## Fase 2 — Contenção Imediata ("Kill Switch")

Diferente de software tradicional, onde suspender um comportamento exige reescrever código e fazer novo deploy, a contenção de um agente baseado em identidade federada (OIDC/OAuth) acontece direto na camada de gerenciamento de identidade (IAM) — sem tocar no código:

1. O operador de incidentes executa um bloqueio de um clique no painel de identidades.
2. O token de acesso e os refresh tokens associados àquele `Agent ID` específico são **revogados dentro do prazo de contenção definido para o nível de impacto**.
3. Sem escopos válidos, qualquer chamada subsequente de ferramenta — leitura ou escrita — é bloqueada fisicamente no gateway de rede, estancando o incidente instantaneamente, sem precisar paralisar outros agentes ou derrubar servidores do negócio.

## Fase 3 — Isolamento e Erradicação

- A sandbox e os volumes de disco associados ao worker comprometido são congelados para perícia (não destruídos imediatamente — preservados para análise).
- O harness expurga os buffers de memória e o histórico persistido (ex. tabelas locais) daquela sessão, para impedir que uma instrução maliciosa injetada sobreviva a uma retomada futura da sessão.

## Fase 4 — Recuperação e Post-mortem

- Com base nas trilhas de execução gravadas, um modelo econômico pode ajudar a redigir a primeira versão do relatório forense — mas a decisão final e a correção de postura ficam com a equipe humana.
- Novos testes e regras de lint/hook são implementados para blindar contra a mesma classe de exploração no futuro.
- A sandbox é reconstruída limpa antes de qualquer nova execução do agente afetado.

**Pré-requisito para a Fase 2 funcionar:** identidade do agente deve ser federada e de curta duração (ver `../references/agent-identity.md`) — chaves estáticas de longa duração não podem ser "revogadas em 5 minutos" da mesma forma, pois frequentemente estão espalhadas em múltiplos lugares (variáveis de ambiente, configs locais).

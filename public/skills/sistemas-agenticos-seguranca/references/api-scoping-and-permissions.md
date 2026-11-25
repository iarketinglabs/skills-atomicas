# Escopos de Permissão e Scoping de API

Parte de **Segurança e Identidade** (ver Framework Mental no `SKILL.md`, especialmente a Tríade Letal). Responde a "o que este agente pode fazer" — o complemento de `agent-identity.md` ("quem é este agente"). O Scoping de API é o mecanismo que quebra a Tríade Letal na prática: ao restringir cirurgicamente o escopo do token do agente, elimina-se uma das três pernas necessárias para um ataque bem-sucedido.

## Caso de estudo: exploração de escopo amplo

Um incidente documentado de mercado (fevereiro de 2026) envolveu um agente autônomo, operando com um orçamento de poucos dólares de créditos de API e sem credenciais prévias, que explorou um endpoint de produção mal configurado como gravável e não autenticado. O agente executou uma técnica de injeção de SQL bem conhecida desde os anos 1990 e obteve acesso a dezenas de milhões de registros e a todos os prompts de sistema que governavam a plataforma. A causa raiz não foi sofisticação do ataque — foi a **ausência de uma primitiva de escopo** que limitasse o que aquele agente específico podia alcançar. O raio de dano foi ilimitado porque nada o limitava.

## Atenuação dinâmica de escopo (Down-scoping)

O harness nunca deve fornecer chaves de serviço permanentes de longo prazo diretamente às sandboxes de execução. Em vez disso, implementa-se atenuação dinâmica via troca de token (padrão de token exchange, ex. RFC 8693):

```
1. IDENTIDADE DO USUÁRIO (token original, escopo amplo)
              │
              ▼  troca de token
2. TOKEN VAULT (na borda — ver agent-identity.md)
   intercepta a tarefa agêntica ativa
              │
              ▼  atenuação baseada no contrato da tarefa
3. WORKER (token de curta duração, max ~10 min)
   escopo mínimo viável: ex. "ler apenas esta pasta do repositório"
```

O token que chega ao worker carrega só o escopo estritamente necessário para aquela tarefa — nunca os escopos amplos do usuário original que o solicitou.

## A Trust Ladder aplicada a escopos

Ver a tabela completa em `../assets/trust-ladder.md`. Regra prática de scoping: o escopo concedido a um token deve corresponder exatamente ao nível de risco da ação que a tarefa exige — nunca conceda escopo de nível 4 (irreversível/financeiro) para uma tarefa que só precisa de nível 1 (leitura).

## Dynamic Tool-Pool Assemblies

Expor o catálogo inteiro de dezenas de ferramentas MCP disponíveis para toda janela de contexto não é só um problema de custo de tokens — é um problema de superfície de ataque: quanto mais ferramentas de alto privilégio estão "visíveis" e utilizáveis por um agente em um dado momento, maior o dano possível se ele for comprometido por injeção. A prática correta é filtrar e injetar somente as ferramentas necessárias para a fase ativa da tarefa (progressive disclosure), conforme um limite definido por risco e contexto.

## Ameaças específicas de escopo amplo

### Ataque do "Vice-Preposto Confuso" (Confused Deputy)
Ocorre quando um agente altamente privilegiado (ex. o orquestrador central) é induzido — por uma instrução injetada em conteúdo não confiável — a executar uma ação destrutiva em nome de um subagente de baixa confiança. O agente de maior privilégio se torna o "preposto confuso" do atacante:

```
CONTEÚDO NÃO CONFIÁVEL contrabandeia instrução maliciosa
              │
              ▼
AGENTE (com token de escrita externa amplo) interpreta como comando legítimo
              │
              ▼
executa a ação hostil silenciosamente (ex. postar em canal público)
```

A defesa é justamente o down-scoping: se o token do agente nunca teve o escopo amplo de escrita externa em primeiro lugar, a instrução injetada não tem com que trabalhar.

### Wallet Draining (esgotamento financeiro)
Se o agente tem permissão irrestrita para chamar ferramentas pagas, um atacante pode bombardear a thread com entradas massivas, forçando milhares de chamadas repetitivas de API e estourando a cota financeira da organização rapidamente.

### Ataques de cadeia de suprimentos via MCP
Instalar servidores MCP de terceiros não homologados é uma superfície de escopo especialmente perigosa — ver `malicious-mcp-monitoring.md` para o caso documentado de um pacote MCP que injetava cópia oculta em e-mails corporativos.

## Controles preventivos

- **Privilégio mínimo agêntico:** workers instanciados de forma cega e isolada só recebem acesso às ferramentas estritamente exigidas pela subtarefa imediata.
- **Ganchos pré-execução determinísticos:** filtros que inspecionam os parâmetros gerados pelo modelo **antes** de a chamada física ser disparada, barrando acesso a caminhos fora da sandbox ou operações destrutivas.
- **Detecção de desvio comportamental:** monitoramento estatístico da taxa de chamadas e do gasto de tokens por identidade de agente registrada — desvios da média disparam alerta automático.

## Resposta a incidentes

Ver o playbook completo em `../assets/incident-response-playbook.md`.

## Checklist

- Nenhum token de worker carrega escopo mais amplo que o estritamente necessário para a tarefa ativa.
- Down-scoping via troca de token implementado — tokens de usuário nunca são repassados diretamente a sandboxes.
- Catálogo de ferramentas exposto ao agente é filtrado por fase da tarefa (progressive disclosure), não o catálogo completo.
- Monitoramento de desvio de gasto/comportamento por identidade de agente está ativo.

## Interface com o plano de controle

O escopo deve incluir operação, objeto, destinatário, volume, duração, rede e reversibilidade. Reavalie-o quando o objetivo ou o recurso mudar; consulte `agentic-security-control-plane.md` para a sequência de autorização fora do modelo.

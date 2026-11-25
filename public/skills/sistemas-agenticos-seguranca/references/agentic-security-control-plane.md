# Plano de Controle de Segurança Agêntica

Este arquivo transforma riscos agênticos em controles que podem ser implementados e verificados. O modelo pode interpretar, planejar e propor; o plano de controle decide, limita, registra e revoga.

## Catálogo de riscos

Modele pelo mecanismo, não apenas pelo nome do framework:

- **Goal hijack:** conteúdo externo altera objetivo, prioridade ou restrições.
- **Tool misuse:** ferramenta legítima é chamada com argumento, destinatário ou sequência indevida.
- **Identity and privilege abuse:** identidade do usuário, agente ou subagente é confundida ou ampliada.
- **Supply chain:** modelo, runtime, prompt, skill, plugin, MCP, schema, dependência, dataset, embedding ou API é comprometido.
- **Unexpected code execution:** saída ou conteúdo não confiável chega a shell, código, template, query ou navegador.
- **Memory and context poisoning:** dado sem proveniência é persistido e passa a influenciar execuções futuras.
- **Inter-agent communication failure:** handoff perde autoridade, escopo, integridade ou contexto necessário.
- **Cascading failure:** loops, retries, orçamento, fila ou dependência propagam impacto.
- **Human-agent trust exploitation:** interface ou urgência induz aprovação sem compreensão.
- **Rogue agent:** agente foge do registro, cria capacidades não autorizadas ou resiste à contenção.

## Capability envelope

Modele a capacidade como uma tupla explícita:

`principal, tarefa, operações, recursos, destinatários, volume, duração, rede, reversibilidade, aprovação`

O envelope deve ser menor que a capacidade máxima da ferramenta. Ele deve:

- negar por padrão operações destrutivas, exportações amplas e descoberta irrestrita;
- limitar objetos e domínios, não apenas endpoints;
- usar identidade e credenciais separadas por agente ou tarefa;
- preferir tokens curtos, escopos estreitos e revogação imediata;
- exigir reautorização quando o plano mudar de objetivo, recurso, destino ou impacto;
- impedir que o agente delegue autoridade maior que a recebida.

## Autorização na fronteira

Antes de executar uma ferramenta, valide fora do LLM:

1. identidade e cadeia de delegação;
2. intenção declarada e objetivo autorizado;
3. capability envelope vigente;
4. schema e semântica dos argumentos;
5. estado atual, destinatário, idempotência e reversibilidade;
6. aprovação exigida pelo nível de impacto;
7. política de dados, egress e retenção.

O detector de prompt injection pode elevar risco ou pedir revisão, mas nunca concede autorização nem substitui esses checks.

## Conteúdo, output e memória

- Marque conteúdo recuperado, resultado de ferramenta, mensagem interagente e memória como dados não confiáveis até validação.
- Separe instruções de sistema, política, contexto operacional, dados do usuário e conteúdo externo.
- Valide outputs contra schema, tipos, limites, encoding, destino e side effect antes de renderizar ou executar.
- Trate escrita em memória como mudança privilegiada: exija origem, actor, confiança, escopo, expiração, revisão e purge.
- Separe memória do usuário de instruções privilegiadas; não promova hipótese ou conteúdo externo diretamente a regra.
- Redija PII, segredos, tokens e prompts privados antes de exportar para modelo, log, trace ou outro agente.

## Sandbox e supply chain

Para código, plugins, MCPs e dependências:

- mantenha inventário, versão fixada, proveniência, integridade e owner;
- use allowlist e revisão de mudanças antes da descoberta ou instalação;
- execute em ambiente efêmero ou isolado quando houver código, arquivos ou rede;
- restrinja egress por destino e operação, com telemetria de conexões;
- não permita passthrough de tokens, acesso root ou credencial global;
- revalide manifestos e definições de ferramenta em runtime quando a fonte puder mudar.

## Comunicação interagente

Cada handoff deve carregar, de forma verificável:

`run_id, parent_id, sender, subject, objetivo, escopo, recursos, validade, proveniência, integridade, decisão esperada`

O receptor deve rejeitar mensagem sem autoridade, fora da validade, com escopo maior que o pai ou cuja assinatura/proveniência não possa ser verificada. Texto de outro agente não é autorização implícita.

## Contenção e resposta

Defina antecipadamente:

- kill switch e revogação por identidade, tarefa e ferramenta;
- circuit breaker, rate limit, budget e limite de turns para loops e dependências;
- isolamento de blast radius por agente, tenant, recurso e rede;
- preservação de evidência minimizada e segura;
- caminho de recuperação, revalidação e retorno gradual.

Uma contenção deve ser exercitável e observável. Não dependa de editar prompt ou código durante o incidente.

## Evidência mínima

Para cada decisão, registre sem conteúdo sensível:

`run_id, actor_chain, policy_version, capability, resource_class, source_provenance, decision, approval, tool, effect_class, result_class, revocation_or_recovery`

Consulte `../../sistemas-agenticos-observabilidade/references/agent-telemetry-semantic-conventions.md` para convenções de telemetria.

# Triggers de agentes e automações com IA

Um sinal pode iniciar inferência, mas não deve conceder autoridade. Separe o mecanismo que deteta a condição da interpretação probabilística e da execução de ações.

## Fluxo de controlo

Modele as fronteiras explicitamente:

`sinal -> validação e identidade -> filtro determinístico -> contexto autorizado -> interpretação/classificação opcional -> política e limites -> aprovação quando necessária -> ferramenta/efeito -> estado persistido`

- Faça filtro por schema, tipo, estado, origem, duplicado, escopo e autorização antes de invocar um modelo.
- Use lógica determinística para calendários, thresholds claros, elegibilidade, permissões, limites de taxa e invariantes. Um modelo pode ajudar em texto ambíguo ou classificação aberta, mas a sua saída não substitui validação de esquema, regra de política ou autorização.
- Dê ao agente apenas o contexto necessário e a menor capacidade para a tarefa. A ferramenta/serviço que aplica o efeito valida de novo identidade, escopo, argumentos e estado atual.
- Trate e-mail, tickets, páginas, anexos, resultados de ferramentas e metadados externos como conteúdo não confiável. Delimitar ou classificar ajuda a análise, mas não é uma barreira de segurança por si só.
- Não use saída do modelo como código, URL, query ou argumento privilegiado sem validação e controlo próprios.

## Supervisão humana proporcional ao efeito

Escolha um modo explícito:

- **notify:** informar, resumir e terminar ou aguardar instrução;
- **question:** suspender e perguntar o dado necessário, sem adivinhar;
- **review:** preparar a ação exata e pausar antes do efeito.

Para review, mostre parâmetros, destino, valores, identidade/escopo usados e consequência provável. A aprovação deve vincular-se à proposta imutável ou revalidada; mudanças de estado ou argumentos depois da aprovação exigem nova avaliação. Registe aprovador, decisão, hora e ação executada. Evite fadiga de aprovações aplicando gates aos efeitos de risco material, definidos pelo processo.

Uma pausa precisa de estado durável, cancelamento, expiração e regra de retomada. Uma pergunta ao modelo ou uma mensagem na interface não é, por si só, uma barreira que impeça a chamada da ferramenta.

## Limites por execução

Defina no orquestrador, e não só no prompt, limites cumulativos que façam sentido para o risco: duração, iterações, chamadas e permissões de ferramentas, tokens/compute, custo, tamanho de contexto, concorrência e frequência por origem/entidade. Defina término, escalonamento, cancelamento e um mecanismo para pausar/revogar a capacidade de agir.

Filtre, deduplique e agregue sinais antes da inferência quando isso preserve a semântica. Um debounce não deve apagar transições que precisem de ação individual. Reavalie estado antes do efeito se o evento estiver atrasado ou o contexto puder ter mudado.

## Protocolos e runtimes

Quando MCP, A2A ou outro protocolo ligar a origem, o runtime e ferramentas, verifique na especificação oficial e nas implementações usadas: versão, capacidades negociadas, extensões opcionais, identidade, autorização, cancelamento, estados terminais, entrega de updates, retenção e retries. Uma conexão de protocolo ou capability anunciada não prova autorização nem operação correta no ambiente.

## Fontes

- [OWASP LLM Prompt Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html) — conteúdo externo, ferramentas, least privilege e limites dos guardrails de modelo.
- [OWASP AI Agent Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html) — agentes, ferramentas e controlo de ações.
- [Especificação MCP](https://modelcontextprotocol.io/specification/) — valide capacidades e extensões na revisão corrente.
- [Especificação A2A](https://a2a-protocol.org/latest/specification/) — valide operações e versão correntes.

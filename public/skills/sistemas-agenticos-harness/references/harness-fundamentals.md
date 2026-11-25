# Fundamentos de harness engineering

## O que o harness faz

Um harness é o software que enquadra a interação entre modelo, ferramentas, dados e aplicação. O termo não designa uma arquitetura única. Dependendo da solução, pode incluir montagem de contexto, ciclo de chamadas ao modelo, validação de pedidos de ferramenta, execução, gestão de estado, hooks, observabilidade e tratamento de falhas.

Descreva o sistema pelas suas responsabilidades reais, não apenas pelo nome do framework:

| Responsabilidade | Pergunta de desenho | Exemplo de evidência |
|---|---|---|
| Contexto | Que informação é selecionada, ordenada, filtrada ou resumida para cada chamada? | Mensagens efetivamente enviadas, orçamento medido, política de truncamento |
| Decisão | Que escolhas ficam para o modelo e quais ficam fixadas no código? | Workflow, classificador, política de roteamento ou decisão do agente |
| Ferramentas | Como se descobrem, validam, autorizam e executam ações? | Schema, identidade do chamador, verificação no servidor, trilha de auditoria |
| Estado | O que continua entre turnos, falhas ou sessões e onde é guardado? | Estado persistido, checkpoint, journal e procedimento de recuperação |
| Controlo | Como a execução progride, termina, pausa ou pede intervenção? | Transições, limite operacional, critério de parada e caminho de escalonamento |
| Feedback | Como se determina se o resultado cumpre o objetivo? | Testes, revisão humana, métricas, evals e inspeção de trajetória |

Não assuma que estas responsabilidades pertencem a um único processo. Um framework pode oferecer um loop e deixar identidade, autorização, política de domínio, persistência ou operação distribuída à aplicação.

## Determinismo e probabilidade

O modelo é adequado a tarefas de interpretação e escolha semântica quando há ambiguidade que não compensa codificar. Código convencional é adequado a contratos exatos, invariantes, autorização, cálculos, limites, transações e efeitos que precisam de comportamento previsível.

Uma fronteira prática é:

1. O modelo propõe uma classificação, plano, argumento ou próxima ação.
2. Código valida formato, domínio, identidade, autorização, pré-condições e orçamento.
3. Um componente autorizado executa o efeito e devolve um resultado observável.
4. A aplicação regista o que aconteceu e decide se o processo continua, termina ou escala.

Um workflow determinístico pode chamar um modelo; um loop agêntico pode conter validações e passos determinísticos; um grafo pode combinar ambos. “Workflow”, “agente” e “grafo” descrevem formas de controlo, não níveis universais de qualidade.

## Escolher a topologia mínima

| Forma | Adequada quando | Limite a observar |
|---|---|---|
| Função ou sequência fixa | Ordem e decisão são conhecidas antes da execução | Mudanças de requisito podem multiplicar ramificações |
| Workflow com decisões pontuais do modelo | A estrutura é previsível, mas algumas etapas exigem interpretação | Não delegar ao modelo invariantes que o código pode verificar |
| Loop de agente | A próxima ação depende do resultado de ferramentas ou de observações novas | Parada, orçamento, repetição, autorização e progresso precisam de controlo externo |
| Grafo de estados | Ramos, pausas, retomadas e evolução do estado precisam de representação explícita | Complexidade de estado, serialização, versionamento e efeitos repetidos |
| Composição | Fases diferentes exigem controlo diferente | Contratos claros entre componentes e dono de cada efeito |

Comece pela estrutura mais simples que satisfaça requisitos verificáveis. Adicione grafo, subagente, planner, memória ou camada de middleware quando resolver uma necessidade identificada e o benefício puder ser avaliado. A simplicidade não é um objetivo isolado: se a auditoria, retomada ou isolamento exigirem estrutura, inclua-a.

## Ferramentas como fronteira de autoridade

Uma chamada proposta pelo modelo é entrada não confiável. O componente que executa deve validar os argumentos e verificar a autorização com base na identidade e no estado atuais, no momento do efeito. Um prompt, um tipo ou um schema não substitui esse controlo.

Para cada ferramenta, documente finalidade, entrada, saída, permissões, efeitos, fontes de dados, limites, erros, timeout, repetição segura e auditoria. Reduza o escopo de cada capacidade ao mínimo necessário. Consulte `mcp.md` para protocolo e `sandbox-isolation.md` para execução isolada.

## Contexto e custo

Mais contexto não garante melhor resposta. Selecione material pela relevância para a tarefa, preserve proveniência quando necessária e distinga instruções de dados não confiáveis. Considere custo de tokens, latência, privacidade e qualidade da recuperação. Limites de janela, atenção, caching e degradação variam por modelo, endpoint, conteúdo e runtime; não use um percentual fixo como fronteira universal. Veja `context-injection.md`.

## Estado, memória e durabilidade

- **Histórico:** registo de interações ou mensagens que pode ser reutilizado como contexto.
- **Memória:** informação selecionada para influenciar interações futuras; pode ser derivada, editável ou sujeita a expiração.
- **Estado de execução:** dados necessários para continuar uma operação ou workflow.
- **Checkpoint:** snapshot recuperável do estado num ponto de execução.
- **Journal/event log:** registo ordenado de eventos ou efeitos observados, quando o desenho precisa dessa fonte de recuperação.
- **Execução durável:** comportamento mais amplo que pode incluir persistência, retomada, agendamento, retries e tratamento de falhas; o nome comercial, sozinho, não especifica as garantias.

Uma solução pode oferecer alguns destes recursos e não outros. Confirme o que é persistido, quando, por quanto tempo, como é recuperado, como os schemas evoluem e quais passos podem repetir-se. Um checkpoint não prova que um efeito remoto ocorreu uma única vez. Para isso, também importam a idempotência do destino, as chaves de deduplicação e a conciliação de resultados incertos. Consulte `sistemas-agenticos-resiliencia` quando disponível.

## Avaliação e comparação

Antes de comparar arquiteturas, fixe tarefa, conjunto de exemplos, critérios de sucesso, limites de risco, modelo, ferramentas, versão e orçamento. Avalie qualidade final e, quando relevante, trajetória, chamadas, falhas, intervenção humana, latência, custo e comportamento adversarial. Separe resultados medidos de garantias documentadas e opiniões.

Um benchmark publicado é evidência apenas para a tarefa, configuração, baseline e condições reportadas. Não transporte percentuais de redução de tokens ou ganho de acurácia para outra carga sem replicação. Use evals determinísticas para propriedades exatas, revisão humana para semântica ambígua e múltiplas fontes de evidência para decisões de alto impacto.

## Fontes para exemplos de arquitetura

Os perfis abaixo ilustram camadas e escolhas diferentes; não formam ranking e não são exaustivos:

- [Anthropic — Building effective agents](https://www.anthropic.com/research/building-effective-agents): workflows, agentes e padrões composáveis. O próprio artigo avisa que parte da paisagem de ferramentas descrita mudou desde 2024; use-o para princípios, não para estado atual de produtos.
- [Anthropic — Code execution with MCP](https://www.anthropic.com/research/code-execution-with-mcp): trade-offs de executar código sobre ferramentas e dados; ganhos reportados dependem do setup descrito.
- [Hermes Agent](https://github.com/NousResearch/hermes-agent): exemplo de runtime integrado; ver `hermes-agent.md`.
- [Pydantic AI](https://pydantic.dev/docs/ai/overview/): framework Python com agentes, ferramentas, dependências e resultados; ver `pydantic-ecosystem.md`.
- [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview): runtime de orquestração para agentes stateful e de longa duração; ver `langchain-ecosystem.md`.

Documentação e código evoluem. Para uma decisão de implementação, registe a URL, versão ou commit, data de consulta, configuração testada e evidência observada.

# Eliminação de Dependências Seriais

Parte de **Escalabilidade e Multi-Agentes** (ver Framework Mental no `SKILL.md` e o ciclo completo em `hierarchical-planner-worker.md`). O motivo empírico pelo qual a arquitetura de duas camadas existe: dados de mercado sobre por que coordenação plana (não hierárquica) degrada em vez de escalar.

## A descoberta: mais agentes pode piorar o resultado

Um estudo conjunto de pesquisa (dezembro de 2025) revelou um achado contraintuitivo: adicionar mais agentes a um sistema sem a devida segregação de infraestrutura pode **piorar** o desempenho global, não melhorá-lo.

- Quando a precisão de um único agente numa tarefa já excede ~45%, adicionar mais agentes horizontais gera retornos decrescentes ou puramente negativos.
- Em ambientes com mais de 10 ferramentas disponíveis simultaneamente para um mesmo agente, a eficiência de sistemas multi-agente planos cai de 2 a 6 vezes comparado a um agente individual — porque a densidade de opções degrada a acurácia de seleção de ferramenta, não porque falta capacidade.

## Por que a coordenação plana colapsa

Quando agentes de igual autoridade compartilham o mesmo workspace, arquivo ou ferramenta ativa, o sistema desenvolve três disfunções:

1. **Gargalo de fila:** a maior parte do tempo computacional é gasta esperando a liberação de travas lógicas em vez de produzir trabalho.
2. **Aversão a risco por difusão de responsabilidade:** sem hierarquia clara, os agentes evitam tarefas complexas e concentram esforço em alterações pequenas e seguras, só para inflar métricas de progresso — o trabalho difícil fica intocado.
3. **Colisão de escrita física:** dois agentes editando o mesmo arquivo ao mesmo tempo geram conflitos de merge que nenhum dos dois consegue resolver sozinho.

A solução não é reduzir o número de agentes — é eliminar a dependência serial que os força a competir pelo mesmo recurso. Ver a arquitetura de duas camadas completa em `hierarchical-planner-worker.md`.

## Fluxos baseados em grafos assíncronos

Frameworks modernos de orquestração representam o trabalho como um grafo de execução — nós e arestas lógicas, não uma conversa linear de turnos. Dois modos de operação:

- **Single-turn:** o sub-agente recebe a instrução, executa suas chamadas internas na sandbox, retorna o resultado e devolve o controle automaticamente ao coordenador — sem handoff interativo manual.
- **Task mode:** para tarefas de complexidade média onde o worker pode precisar de esclarecimento, ele tem permissão para pausar e perguntar — mas assim que a tarefa termina, o controle volta obrigatoriamente ao coordenador, nunca fica "solto" esperando o próximo passo do usuário.

## A fila de merge como fronteira assíncrona

Em vez de cada worker resolver conflitos de merge por conta própria (o que reintroduziria dependência serial), a consolidação de branches paralelas é delegada a uma fila de integração externa — os workers nunca bloqueiam uns aos outros esperando o merge de outro; a fusão acontece de forma assíncrona depois que cada um já terminou seu trabalho isolado.

## Observabilidade

Ver `../assets/agentic-observability-metrics.md`.

## Checklist

- Nenhum agente espera a liberação de uma trava de arquivo/ferramenta compartilhada com outro agente ativo — se isso acontece, há uma dependência serial não eliminada.
- O catálogo de ferramentas disponível para qualquer agente individual fica abaixo do limiar que degrada a seleção (referência: ~10 ferramentas).
- Merge de trabalho paralelo acontece em uma fila assíncrona externa, nunca como uma negociação síncrona entre os workers.
- Workers em modo single-turn devolvem o controle automaticamente ao terminar — nunca ficam "esperando" indefinidamente.

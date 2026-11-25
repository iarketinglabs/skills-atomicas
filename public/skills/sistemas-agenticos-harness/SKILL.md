---
name: sistemas-agenticos-harness
description: "Use ao desenhar ou rever o harness de um agente: contexto, ferramentas, estado, controlo, isolamento, segurança e avaliação. Ajuda a escolher entre workflows, loops, grafos e composição sem presumir fornecedor ou arquitetura de produto."
---

# Engenharia de harness para sistemas agênticos

## Quando usar

- Desenhar ou rever a infraestrutura que envolve um modelo para executar tarefas com ferramentas e estado.
- Decidir quais partes devem ser controladas por código e quais podem depender de decisão probabilística.
- Escolher entre workflow fixo, loop de agente, grafo de estados ou composição de padrões.
- Analisar contexto, ferramentas, memória, checkpoints, durabilidade, subagentes ou avaliação.
- Comparar runtimes e frameworks por capacidades, limites, dependências e custo operacional.

## Quando não usar

- Para implementar um runtime, servidor MCP, sandbox, workflow engine ou integração específica.
- Para definir políticas detalhadas de segurança, SLOs, telemetria ou avaliação de produção; use as referências especializadas quando disponíveis.
- Para executar um processo agêntico já definido. Esta skill orienta o desenho do sistema que o executa.

## Modelo mental

Um sistema agêntico inclui mais do que o modelo:

- **Modelo:** produz texto, decisões e propostas de chamadas a ferramentas.
- **Harness/runtime:** monta o contexto, conduz o ciclo de execução, despacha ferramentas e recolhe resultados. Pode combinar lógica determinística e decisões probabilísticas.
- **Aplicação:** define identidade, objetivos, regras de domínio, experiência, dados e efeitos permitidos. Algumas soluções incluem partes dessas responsabilidades no runtime; identifique explicitamente onde cada uma está.

O harness deve impor fora do texto do modelo as invariantes que exigem garantias de software: autorização, validação de argumentos, limites operacionais, persistência, aprovação e execução de efeitos externos. Consulte `references/harness-fundamentals.md` para separar essas responsabilidades.

## Mapa de referências

| Questão | Referência |
|---|---|
| Fundamentos, fronteiras e critérios de escolha | `references/harness-fundamentals.md` |
| Contexto, seleção e compactação | `references/context-injection.md` |
| Memória e estado partilhado | `references/shared-memory.md` |
| Workflows, loops e coordenação | `references/deterministic-orchestration.md` |
| Grafos, transições, pausa e retomada | `references/state-graphs-and-loop-control.md` |
| Ferramentas externas e MCP | `references/mcp.md` |
| Skills e peças reutilizáveis | `references/skills-as-building-blocks.md` |
| Subagentes e decomposição | `references/subagents.md` |
| Hooks e middlewares | `references/hooks-and-middlewares.md` |
| Terminal, filesystem e isolamento | `references/filesystem-and-terminal.md`, `references/sandbox-isolation.md` |
| Perfis de frameworks e runtimes | `references/hermes-agent.md`, `references/pydantic-ecosystem.md`, `references/langchain-ecosystem.md` |
| Harness e treino de modelos | `references/harness-vs-model-training.md` |

A comparação de building blocks está em `assets/building-blocks-comparison-table.md`. Para aprofundar segurança, resiliência, observabilidade ou autoaprimoramento, consulte as skills `sistemas-agenticos-seguranca`, `sistemas-agenticos-resiliencia`, `sistemas-agenticos-observabilidade` e `sistemas-agenticos-autoaprimoramento`, se existirem no ambiente. Estas referências são encaminhamentos opcionais, não dependências da skill.

## Fluxo de decisão

1. Defina o resultado esperado, limites de risco, dependências externas, duração, volume e quem pode aprovar efeitos.
2. Separe etapas previsíveis de decisões semânticas e escolha a menor topologia que cumpra os requisitos.
3. Determine quais dados entram no contexto, que estado precisa sobreviver ao turno e qual componente é dono da persistência.
4. Defina interfaces e permissões das ferramentas; valide entradas e efeitos no limite que os executa.
5. Defina condições de sucesso e parada, limites operacionais, recuperação e como a qualidade será avaliada.
6. Compare frameworks depois de fixar os requisitos. Registe capacidades observadas, versão consultada, dependências e lacunas que a aplicação terá de cobrir.

## Princípios de projeto

- Use workflows para sequências previsíveis; loops de agente quando a próxima ação depende de observações semânticas; grafos quando estados, ramos, interrupções ou retomadas precisam de representação explícita. Combine-os quando cada fase pedir um controlo diferente.
- Tipos e schemas ajudam a verificar contratos. Não provam que uma saída é verdadeira, autorizada ou segura.
- Distinga histórico de conversa, memória reutilizável, estado de execução, checkpoint, journal e execução durável.
- Mais ferramentas, agentes, middleware ou contexto não implicam um resultado melhor. Justifique cada componente com requisitos e avaliação.
- Trate documentação de fornecedor como descrição de capacidades, não como garantia aplicável a qualquer versão, configuração ou carga. Verifique o contrato e a versão usados.
- Compare opções no mesmo workload, com critérios, dados, limites, custos e procedimentos de avaliação equivalentes. Não transforme resultados isolados em constantes universais.

## Antipadrões

| Antipadrão | Risco | Referência |
|---|---|---|
| Carregar todas as ferramentas e todo o histórico | Consumo de contexto, ruído e instruções menos relevantes | `references/context-injection.md`, `references/mcp.md` |
| Deixar o modelo autorizar o próprio efeito | Uma proposta probabilística passa a ser autoridade sem validação externa | `references/sandbox-isolation.md` |
| Acrescentar agentes por persona ou moda | Custo e coordenação sem ganho demonstrado | `references/subagents.md` |
| Tratar checkpoint, memória e durabilidade como sinónimos | Recuperação ou continuidade com garantias presumidas | `references/shared-memory.md`, `references/state-graphs-and-loop-control.md` |
| Copiar métricas de benchmark sem contexto | Comparação enganosa entre tarefas, modelos, versões e runtimes | `references/harness-fundamentals.md` |
| Manter regras absolutas depois de trocar de modelo ou runtime | Restrições obsoletas ou garantias inexistentes | `references/harness-vs-model-training.md` |

# Métricas de Observabilidade Agêntica

Fonte canônica única destas métricas — referenciada (não copiada) por `../references/task-decomposition-and-verification.md`, `../references/parallelization-and-throughput.md`, `../references/eliminating-serial-dependencies.md` e `../references/simple-agent-coordination.md`. Quando um enxame de agentes roda de forma assíncrona e invisível em background, os analytics de produto tradicionais (cliques, page views) perdem o sentido — o monitoramento precisa focar em métricas de trabalho delegado.

## As duas métricas centrais

- **Completion Rate (Taxa de Conclusão):** percentual de tarefas concorrentes que atingiram a definição de "concluído" sem sofrer interrupção física (crash de sandbox, erro de rede) no meio do caminho.
- **Correction Rate (Taxa de Correção):** a frequência com que um humano precisa intervir no fluxo autônomo — revogar uma permissão, corrigir um rascunho, reverter um commit, reabrir uma tarefa marcada como concluída incorretamente. Uma Correction Rate acima de ~15% em um workflow específico é o sinal mais confiável de que os prompts ou a biblioteca de skills daquele domínio estão obsoletos e precisam de revisão — não que os agentes precisam de mais supervisão manual permanente.

## Rastreabilidade unificada

Toda a cadeia de eventos de uma execução — do prompt original do usuário, passando pelas chamadas de ferramenta, pela criação de sub-agentes paralelos, até a decisão final do revisor — deve herdar o mesmo identificador único de execução (**Agent Run ID**), persistido em uma ferramenta de tracing externa (não só no console local). Isso permite reconstruir a árvore genealógica completa de decisões de um enxame paralelo depois do fato, em vez de depender de logs de terminal dispersos e efêmeros.

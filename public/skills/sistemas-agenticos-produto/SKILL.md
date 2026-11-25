---
name: sistemas-agenticos-produto
description: "Use ao descobrir, avaliar, desenhar, posicionar, monetizar ou lançar produtos digitais com IA e agentes. Ajuda a ligar necessidades e evidência a escolhas de solução, experiência, avaliação, risco e modelo de negócio, incluindo quando decidir que uma regra, automação ou workflow simples é suficiente."
---

# Produto digital com IA e agentes

## Objetivo

Transformar uma oportunidade de produto em decisões e artefactos verificáveis. A skill aplica fundamentos de produto digital a funções probabilísticas e agentivas, sem presumir setor, país, empresa, cliente, stack ou fornecedor.

Use-a quando o pedido envolver descoberta de necessidades, priorização de oportunidades, definição de uma funcionalidade com IA, escolha entre regra/modelo/workflow/agente, desenho de métricas e evals, monetização por acesso/uso/execução/resultado, ou preparação de lançamento.

Não substitui implementação de produção, aconselhamento jurídico, avaliação independente de segurança ou um plano financeiro aprovado. Se o pedido se concentrar numa destas atividades, entregue a parte de produto necessária e, quando existirem no ambiente, encaminhe a execução técnica para as competências especializadas apropriadas.

## Regras de decisão

- Comece pelo progresso que a pessoa utilizadora ou compradora procura, não pela tecnologia proposta. Trate “adicionar um agente” como hipótese de solução até haver evidência do problema e do valor esperado.
- Separe observações, interpretações, hipóteses, estimativas e previsões. Preserve a origem e as limitações da evidência; não transforme uma síntese automática em evidência primária.
- Compare a solução proposta com a alternativa atual e com opções mais simples: processo manual, regra determinística, pesquisa, automação convencional, modelo com um passo, workflow com etapas fixas ou agente com decisões dinâmicas.
- Prefira a menor complexidade que satisfaça o resultado e os limites de qualidade, custo, latência, risco e manutenção.
- Torne explícitos os casos fora de âmbito, os modos de falha, o fallback e as ações que exigem revisão humana. Baseie autonomia na consequência e reversibilidade das ações, não no rótulo “agente”.
- Não use scores de priorização como decisões automáticas. Registe a evidência, a confiança e as dependências por detrás de cada estimativa.
- Não trate métricas de modelo como prova de valor de produto. Avaliações offline, comportamento real, operação e economia respondem a perguntas diferentes.
- Não presuma que uma tendência de mercado, preço, lei, standard ou capacidade de fornecedor se mantém atual. Quando a atualidade mudar a decisão, verifique fontes primárias disponíveis e indique data, jurisdição e incerteza.
- Mantenha os artefactos proporcionais à decisão. Use os modelos em assets como ponto de partida e remova campos sem utilidade para o caso.

## Fluxo de trabalho

Adapte a profundidade ao pedido. Não percorra todas as etapas quando o utilizador só precisa de uma decisão pontual.

1. **Enquadre a decisão.** Identifique o resultado pretendido, quem beneficia, quem compra ou opera, a decisão a tomar e o formato de entrega. Pergunte apenas por lacunas que mudem materialmente a solução. Caso contrário, declare pressupostos.
2. **Estabeleça o problema e a evidência.** Registe a tarefa atual, alternativas, frequência, impacto, contexto, baseline e evidência disponível. Distinga factos observados de interpretação e incerteza. Para discovery e priorização, consulte [discovery e priorização](references/discovery-and-prioritization.md).
3. **Compare opções de solução.** Considere não usar IA, regra, modelo, retrieval, workflow e agente conforme o problema. Identifique o ganho incremental esperado, dependências, casos que não serão resolvidos e razão para qualquer autonomia. Para arquitetura, interação, controlo e contexto, consulte [sistema de IA e experiência](references/ai-system-and-experience.md).
4. **Defina comportamento e medição.** Especifique entradas, saídas, limites, estados de erro, correção, fallback, métricas, casos de avaliação e critérios de lançamento. Separe evals do comportamento do sistema de experiências com utilizadores. Consulte [avaliação e medição](references/evaluation-and-measurement.md).
5. **Verifique risco e operação.** Analise dados, permissões, impacto, reversibilidade, revisão humana, acessibilidade, monitorização e resposta a incidentes. Para obrigações legais ou standards, confirme o enquadramento aplicável no momento. Consulte [risco, governação e lançamento](references/risk-governance-and-launch.md).
6. **Avalie a economia e a oferta se for relevante.** Defina quem paga, por que unidade de valor, como o evento é medido, como se atribui o resultado e o que acontece com variação de consumo e custo. Compare preço com custo total por tarefa concluída e aceite. Consulte [modelos de negócio e pricing](references/business-models-and-pricing.md). Para detalhe de tokens, cache ou routing de modelos, use a skill de eficiência apenas se estiver disponível.
7. **Entregue uma decisão legível.** Apresente recomendação, evidência, pressupostos, alternativas rejeitadas, riscos, próximos passos e critérios que fariam rever a decisão. Prefira o asset adequado: [brief de oportunidade](assets/opportunity-brief.md), [especificação de funcionalidade com IA](assets/ai-feature-spec.md), [caso de eval](assets/eval-case-template.json), [folha de economia e pricing](assets/pricing-economics-worksheet.md) ou [checklist de lançamento](assets/launch-checklist.md).

## Forma recomendada da resposta

Para análises curtas, use esta sequência:

1. Decisão ou pergunta em aberto.
2. Evidência disponível e principal lacuna.
3. Opções comparadas e recomendação condicional.
4. Métricas e limites de risco.
5. Próxima validação que mais reduz incerteza.

Para uma especificação ou plano, deixe claros o estado atual, o comportamento pretendido, os limites e os critérios de aceitação. Se houver vários públicos, países ou níveis de risco, explicite quais foram cobertos e quais precisam de avaliação própria.

## Referências de apoio

- Leia [discovery e priorização](references/discovery-and-prioritization.md) para investigar necessidades, organizar oportunidades e escolher métodos de priorização.
- Leia [sistema de IA e experiência](references/ai-system-and-experience.md) para comparar regras, modelos, retrieval, workflows e agentes, e desenhar a experiência perante incerteza.
- Leia [avaliação e medição](references/evaluation-and-measurement.md) para criar evals, métricas, experiências e gates de lançamento.
- Leia [modelos de negócio e pricing](references/business-models-and-pricing.md) para desenhar unidades de cobrança e analisar economics e atribuição.
- Leia [risco, governação e lançamento](references/risk-governance-and-launch.md) para graduar autonomia, proteger pessoas e dados e planear a operação.

## Avaliação da skill

Os cenários em [evals/evals.json](evals/evals.json) verificam se a skill mantém a descoberta centrada no utilizador, escolhe a complexidade adequada, separa métricas, calcula economics por tarefa e não faz afirmações universais sem evidência. As expectativas são critérios qualitativos para avaliar respostas, não uma promessa de desempenho automático.

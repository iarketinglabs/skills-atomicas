# Evidência, proveniência e atualização

## Classe cada afirmação

Ao recomendar uma técnica, capacidade ou expectativa de desempenho, distinga:

| Classe | O que sustenta | Limite |
|---|---|---|
| Pesquisa revisada por pares | Método e resultado nas tarefas e condições do estudo | Não prova ganho no tráfego de outra organização ou em versões atuais. |
| Preprint ou relatório técnico | Evidência preliminar e hipóteses de pesquisa | Identifique que não é resultado revisado por pares e procure replicação. |
| Benchmark independente | Comparação sob o pool, protocolo e critérios publicados | Verifique carga, versões, métricas, composição do pool e limitações. |
| Documentação oficial de projeto ou provedor | Contratos, endpoints, configuração, preço e suporte declarados | É específica à versão e não estabelece superioridade independente. |
| Alegação de fornecedor | Resultado divulgado pelo próprio fornecedor | Rotule como alegação; não generalize sem medição independente. |
| Inferência ou heurística | Hipótese operacional deduzida de evidência ou experiência | Declare suposições e teste antes de torná-la política. |
| Divergência | Fontes apresentam resultados ou interpretações diferentes | Preserve ambas com seu contexto; não force consenso. |

## Registo mínimo

Para cada afirmação que possa alterar uma decisão, guarde:

- título, autor ou publicador e link direto;
- classe de evidência, data da publicação e data de acesso;
- versão exata do modelo, provedor, ferramenta ou configuração;
- tarefa, dados, amostra, baseline, métricas e condições de cache;
- resultado observado e limitações;
- estado: confirmado, divergente, não verificado ou refutado.

Use um número de benchmark apenas junto com o dataset, a versão, o baseline, a configuração, a amostra e o tipo de evidência. Não transporte percentuais de economia ou velocidade para outra carga sem repetir a avaliação.

## Atualize capacidades de produto

Para qualquer gateway, API, versão de modelo, preço, limite, região, retenção, modalidade ou parâmetro:

1. consulte documentação oficial atual e a versão exata em uso;
2. guarde link, data de consulta e configuração;
3. confirme com uma chamada ou experimento permitido quando documentação não demonstrar comportamento real;
4. marque como desconhecido qualquer detalhe sem evidência;
5. reavalie a rota quando alias, preço, política ou comportamento do serviço mudar.

Não confunda nome de modelo estável com comportamento estável. Use testes de compatibilidade e avaliação do workload para detectar mudanças.

## Base de pesquisa e trilhas de leitura

Os relatórios usados como ponto de partida para esta skill têm data de referência 26 de novembro de 2026 e organizam o campo por fundamentos, métodos de decisão, ferramentas, avaliação e segurança. Tratam pesquisas acadêmicas, preprints e documentação de produto como tipos de evidência diferentes. Use as trilhas abaixo para aprofundar, sem interpretar resultados como regra operacional universal:

- Formulação de seleção de algoritmos: Rice, “The Algorithm Selection Problem” (1976).
- Roteamento e cascatas: Chen, Zaharia e Zou, “FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance”; Aggarwal et al., “AutoMix: Automatically Mixing Language Models”.
- Roteamento com dados de preferência: Ong et al., “RouteLLM: Learning to Route LLMs with Preference Data”.
- Avaliação comparativa: Hu et al., “RouterBench: A Benchmark for Multi-LLM Routing System”.
- Risco e governança: OWASP Top 10 for LLM Applications; NIST AI Risk Management Framework e Generative AI Profile.

Busque os títulos nos sites dos autores, periódicos, conferências, arXiv ou instituições responsáveis. Confira se a publicação é final ou preprint, e leia limitações antes de reutilizar números ou conclusões.

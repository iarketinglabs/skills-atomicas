# Protocolo de avaliação

Uma avaliação deve medir a tarefa pretendida sob condições que impeçam o agente de escolher as próprias provas. A robustez do ciclo depende do desenho da avaliação e da regra de promoção, não só da qualidade do proponente.

## Antes de gerar candidatos

Registe:

- Pergunta operacional e população de tarefas que a mudança pretende melhorar.
- Versões de baseline, modelo, prompt, ferramentas, dados, avaliador e dependências.
- Métrica principal, unidade, direção, efeito mínimo com valor prático e intervalo temporal.
- Guardrails independentes para segurança, correção, privacidade, custo, latência e tarefas que não devem piorar.
- Casos críticos, critério de falha e responsável por decidir.
- Conjunto de desenvolvimento, conjunto de decisão protegido e eventual conjunto de regressão; origem, seleção, datas e possíveis duplicados.
- Limite máximo de iterações e pelo menos um teto adicional de tempo, tokens ou custo; regra de parada antecipada.

Os limites e tamanhos de amostra dependem da variância, impacto e objetivo. Não existe um número universal de casos nem um limiar de score válido para todas as tarefas.

## Desenho do conjunto

1. Use exemplos de desenvolvimento para diagnosticar erros e propor mudanças.
2. Reserve casos que o proponente não consegue ler nem usar repetidamente para escolher candidatos. Se isso não for viável, limite e registe cada consulta; considere um método sequencial com controlo de erro adequado.
3. Cubra tarefas comuns, casos de fronteira, entradas ambíguas, tarefas que não devem mudar, casos adversariais proporcionais ao risco e grupos afetados relevantes.
4. Remova duplicação por entidade/conversa/documento quando amostras relacionadas inflariam artificialmente o tamanho efetivo.
5. Evite leakage entre desenvolvimento, memória, treino, validação e teste. Dados sintéticos gerados pelo próprio agente não são ground truth por definição.
6. Preserve o conjunto e a rubrica por versão, com acesso controlado. Não exponha respostas futuras ao agente que gera alterações.

## Comparação

- Compare baseline e candidato na mesma amostra sempre que a comparação pareada fizer sentido. Preserve entradas, configuração, orçamento de inferência e procedimento de scoring.
- Prefira verificadores determinísticos independentes quando a resposta tem critério objetivo (por exemplo, execução segura de uma prova, cálculo ou contrato). Para julgamento semântico, use rubrica explícita e revisão cega; mais de um avaliador pode ajudar, mas juízes correlacionados não criam independência por quantidade.
- Relate resultado global e por tarefa/grupo, dispersão, quantidade de casos, dados em falta, falhas críticas e custo de descoberta e execução. Inclua método de incerteza adequado ao desenho; não improvise significância estatística a partir de um score único.
- Diferencie dado observado, inferência, hipótese e alegação de fornecedor. Uma melhoria numa amostra selecionada não demonstra generalização ou causalidade.
- Faça regressão com competências anteriores. Para memória, instruções e pesos, teste também o que deve permanecer inalterado e a capacidade de retirar a mudança.

## Promoção

Promova apenas se todos os gates definidos previamente forem satisfeitos: ganho prático mínimo, limites de regressão, zero falhas críticas proibidas, integridade do processo de avaliação, orçamento cumprido, reversão disponível e aprovação exigida. Se a análise for exploratória ou inconclusiva, use `hold`; não ajuste a rubrica depois de ver o resultado para obter uma aprovação.

Se o mesmo conjunto for reutilizado para avaliar muitos candidatos, a seleção torna os resultados dependentes: uma regra gulosa de “manter se subiu” aumenta a chance de falso ganho. Rotacione/conserve um teste final protegido ou use um procedimento estatístico sequencial/adaptativo cuja validade e pressupostos sejam apropriados ao caso. Métodos de pesquisa como PACE e REUSE ilustram esse problema, mas não são uma política universal nem dispensam validar pressupostos.

## Interpretação e relatório

O relatório deve permitir a outra pessoa reproduzir a decisão. Inclua os resultados pareados por caso quando possível e a ligação entre cada afirmação, dado, cálculo e fonte. Diga explicitamente: “não testado”, “não replicado” ou “inconclusivo” quando aplicável. O script `compare_paired_results.py` fornece contagens e diferenças descritivas; não calcula intervalo de confiança, prova significância ou autoriza promoção.

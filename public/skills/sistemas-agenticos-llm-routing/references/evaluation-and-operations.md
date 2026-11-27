# Avaliação e operação de roteadores

## Formule a pergunta de avaliação

Registe antes do experimento:

- workload, população, período, distribuição de tráfego e unidade de sucesso;
- decisão ou hipótese a testar;
- requisitos obrigatórios, métrica primária e métricas de proteção;
- pool de candidatos, versões e configurações;
- comparação de referência;
- método de rotulagem, juiz e incerteza;
- custos incluídos, tratamento de cache e política de retentativas;
- tamanho e origem da amostra, segmentos relevantes e critério de conclusão.

Não misture perguntas distintas, como “reduz preço por token?”, “mantém qualidade?”, “cumpre p95?” e “aumenta tarefas concluídas?”. Apresente cada resultado.

## Conjunto de avaliação

- Amostre tarefas representativas do tráfego autorizado, inclusive casos fáceis, difíceis, longos, raros e de maior risco.
- Estratifique por domínio, intenção, idioma, modalidade, tamanho, classe de risco e segmento de uso quando forem relevantes e permitidos.
- Preserve exemplos de falha e casos fora de distribuição; não deixe que o volume de tarefas simples esconda regressões críticas.
- Separe treino, ajuste de limiares, calibração e teste. Divida por origem, tarefa ou tempo para reduzir vazamento e duplicatas.
- Não escolha o roteador final com os rótulos do conjunto de teste.
- Para qualidade sem referência objetiva, use rubrica escrita, avaliação humana ou juiz validado em amostra humana; registe divergências.
- Repita execuções quando a variância de geração puder alterar a conclusão.

## Referências e comparações

Compare na mesma carga, configuração e período:

1. política proposta;
2. melhor modelo fixo selecionado exclusivamente em validação;
3. política atual, se diferente;
4. limite inferior simples, se útil;
5. limite oráculo apenas como teto teórico que usa o resultado real, claramente marcado como não implantável.

Evite comparar o roteador apenas com o maior candidato, com uma escolha aleatória ou com um modelo escolhido depois de ver o teste. Congele e registe prompts, parâmetros, versão, ferramentas, modelo de avaliação, contexto, cache e concurrency.

## Métricas

| Dimensão | Exemplos de medidas |
|---|---|
| Qualidade | Acurácia, completude, aderência à rubrica, preferência pareada, erro semântico ou qualidade final da tarefa. |
| Sucesso | Tarefas concluídas, taxa de conclusão, retentativas e intervenção humana necessária. |
| Custo | Custo total e custo por tarefa concluída; inclua roteador, entrada, saída, raciocínio cobrado, verificadores, falhas, retentativas e perdas de cache. |
| Latência | Mediana e cauda, como p95 ou p99; tempo até primeiro token e tempo total, quando aplicáveis. |
| Política e segurança | Violações, roteamentos bloqueados, rebaixamentos de segurança, dados enviados fora da elegibilidade e tentativas de exceder teto. |
| Saúde do roteador | Distribuição por candidato, taxa de escalada, abstenção, erros do classificador, confiança, timeouts, indisponibilidade e drift. |

Preço por token é um insumo, não uma medida de economia operacional. Uma política que reduz custo por chamada mas causa mais falhas pode elevar custo por tarefa resolvida.

## Análise

- Mostre valores e incerteza, o tamanho da amostra e resultados por segmento, não só uma média agregada.
- Varra limites de custo, qualidade ou latência; uma política pode funcionar apenas em um ponto do trade-off.
- Identifique concentração inesperada em um candidato, em especial no mais caro, e examine dados, objetivo, limiar, calibragem e distribuição.
- Inspecione falsos aceites e falsas escaladas da cascata.
- Registe o efeito de cache frio e aquecido; não compare estratégias sob estados de cache diferentes sem explicitar a condição.
- Separe resultado medido, alegação externa, inferência e hipótese.

## Implantação gradual

1. Valide configuração e política em conjunto offline.
2. Se apropriado, faça modo sombra sobre metadados e sinais permitidos. Não duplique chamadas de modelos ou exponha dados sem necessidade, autorização e orçamento.
3. Faça canário com limites de gasto, segmento e duração definidos.
4. Monitore qualidade, custo por tarefa, p95, rotas, escaladas, falhas e violações de política.
5. Reverta ou pause quando um limite acordado for ultrapassado ou a telemetria essencial não permitir verificar segurança e qualidade.
6. Reavalie após mudança de modelo, alias, preço, prompt, gateway, distribuição, cache ou política.

Use assets/evaluation-plan-template.md para preparar um protocolo antes do experimento.

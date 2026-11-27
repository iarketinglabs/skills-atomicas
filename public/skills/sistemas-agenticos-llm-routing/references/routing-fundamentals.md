# Fundamentos de roteamento de modelos de linguagem

## Definição

Roteamento é uma política que usa sinais disponíveis sobre uma requisição, a sessão e o estado do sistema para escolher um candidato ou uma sequência de candidatos. A ação pode incluir modelo, provedor, prompt, orçamento de raciocínio ou modo de execução, mas cada dimensão acrescentada precisa de uma hipótese de benefício e de avaliação própria.

O problema combina seleção de algoritmos com uma decisão de produto e operação: qual resposta satisfaz os limites do workload, por que a seleção condicional é melhor que uma política fixa e a que custo?

## Objetivo e restrições

Considere a distribuição real de requisições, o conjunto de candidatos e o resultado esperado. Para cada par tarefa-candidato, estime qualidade, custo e latência. O roteador pode otimizar uma utilidade aprovada ou satisfazer limites de qualidade, custo e latência.

Uma forma restrita é:

- primeiro remover candidatos que violam regras obrigatórias;
- depois exigir a qualidade mínima e o SLO acordados;
- entre os restantes, otimizar o objetivo aprovado, por exemplo custo por tarefa concluída.

Uma soma ponderada pode ser útil em análise, mas exige medidas comparáveis e pesos deliberados. Uma única pontuação não deve ocultar violações de segurança, direitos, privacidade ou conformidade. Quando os stakeholders ainda não aprovaram pesos, mostre uma fronteira de Pareto ou resultados sob vários limites.

## Quando o roteamento pode ajudar

Procure evidência de heterogeneidade e complementaridade:

- Um candidato de menor custo atende bem a uma parcela identificável do tráfego.
- Candidatos especializados resolvem segmentos em que o modelo geral falha.
- A decisão consegue identificar esses segmentos com informação disponível antes da chamada ou por uma verificação de saída confiável.
- O ganho continua positivo depois de contabilizar roteador, validação, escaladas, retentativas, latência e estado de cache.

Roteamento pode não valer a pena quando candidatos têm padrões de erro semelhantes, não há volume ou diversidade suficientes, a estimativa de qualidade é ruidosa, os requisitos de latência são apertados ou a política estática já satisfaz qualidade, custo e risco. Mantenha o melhor candidato fixo quando a política condicional não o supera no teste.

## Identifique o que está sendo selecionado

Especifique separadamente:

- **Candidato:** modelo, serviço, sistema especialista ou versão.
- **Estratégia de inferência:** prompt, ferramentas, número de amostras ou orçamento de raciocínio.
- **Momento:** pré-geração, pós-geração, intra-geração ou multi-turno.
- **Observação:** metadados, texto, modalidade, sinais de dificuldade, resposta parcial, resultado de ferramenta, latência ou estado de sessão.
- **Restrição:** elegibilidade, risco, região, teto de gasto, prazo, formato ou capacidade.

Modelos e prompts podem interagir. Se diferentes candidatos exigirem prompts diferentes, avalie a combinação modelo-prompt em vez de presumir que o roteamento e a escolha do prompt são independentes.

## Separe estimativa e resultado

O roteador não observa a qualidade verdadeira antes da resposta. Ele estima a qualidade ou o custo com sinais que podem errar. Avalie:

- qualidade estimada versus resultado observado;
- erros de seleção por segmento e consequência;
- calibração de probabilidades, quando há probabilidades;
- abstenção e tratamento de casos fora de distribuição;
- robustez a variações de idioma, formato e adversários;
- mudança de distribuição e sensibilidade a limiares.

Um classificador sofisticado não compensa dados fracos, rótulos enviesados ou um objetivo mal definido. Simplicidade do mecanismo não implica qualidade da decisão; ambos devem ser medidos.

## Vocabulário operacional

| Termo | Uso nesta skill |
|---|---|
| Roteamento pré-geração | Escolha antes de observar uma resposta gerada. |
| Cascata ou roteamento pós-geração | Começa com um candidato e decide reter ou escalar após inspecionar a resposta ou um sinal de verificação. |
| Roteamento intra-geração | Despacho durante a geração, por exemplo entre tokens, blocos ou passos. |
| Roteamento multi-turno | Escolhas que consideram trajetória, estado, orçamento e continuidade entre turnos. |
| Afinidade de sessão | Preferência por manter a mesma réplica ou modelo para preservar contexto, estado e oportunidades de cache. |
| Modelo de decisão tipado | Modelo que escolhe entre saídas declaradas ou estruturadas; validade estrutural não prova correção semântica. |
| Modelo fixo de referência | Política sem roteamento condicional, escolhida em dados de validação para cumprir os mesmos requisitos. |
| Economia líquida | Diferença de custo total por tarefa concluída depois do overhead do roteamento e das falhas. |

## Regra prática

Comece pelo requisito e pelo baseline, não pela arquitetura de roteador. Adicione complexidade apenas quando uma avaliação representativa demonstrar melhoria líquida e quando a organização aceitar o custo de operação e manutenção.

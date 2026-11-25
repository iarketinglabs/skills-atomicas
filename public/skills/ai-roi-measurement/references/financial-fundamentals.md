# Fundamentos Financeiros

Use esta referência para o cálculo financeiro-base de qualquer mensuração de ROI de IA e para incorporar retorno intangível de forma disciplinada. Ela não substitui a política contábil, fiscal ou de investimento da organização.

## Métricas financeiras clássicas

Cada métrica responde a uma pergunta diferente. Escolha conforme o horizonte e a decisão, e declare sempre a taxa e o período usados.

| Métrica | Fórmula | Quando usar | Limitação principal |
| --- | --- | --- | --- |
| ROI simples | `(Ganho líquido − Custo) / Custo × 100%` | Comparação rápida entre iniciativas de horizonte semelhante | Ignora o valor do dinheiro no tempo e a distribuição do fluxo de caixa |
| Valor Presente Líquido (NPV) | Soma dos fluxos de caixa futuros descontados a uma taxa, menos o investimento inicial | Projetos plurianuais com fluxo de caixa não uniforme | Sensível à taxa de desconto escolhida; exige projeção confiável de fluxo |
| Taxa Interna de Retorno (IRR) | Taxa de desconto que zera o NPV | Comparar atratividade entre projetos de diferentes tamanhos | Pode gerar múltiplas soluções em fluxos não convencionais; não substitui o NPV |
| Payback Period | Tempo até o investimento ser recuperado pelo fluxo de caixa acumulado | Complemento de liquidez e risco, especialmente em orçamento restrito | Ignora o que acontece após o payback e o valor do dinheiro no tempo |
| Custo Total de Propriedade (TCO) | Soma de todos os custos do ciclo de vida: implementação, operação, manutenção e descomissionamento | Comparar alternativas de infraestrutura ou plataforma no longo prazo | Não mede benefício; precisa ser combinado com uma métrica de retorno |
| Valor Econômico Agregado (EVA) | `NOPAT − (Custo de capital × Capital investido)` | Avaliação de desempenho gerencial e de unidades de negócio | Exige definição confiável de custo de capital (WACC) e capital investido |

Use ROI simples para comparações rápidas, NPV/IRR quando o horizonte passar de um ciclo orçamentário, payback como informação complementar de liquidez, TCO sempre que houver decisão de infraestrutura ou plataforma, e EVA quando a avaliação for de desempenho gerencial recorrente, não de um projeto isolado.

Para IA especificamente, o TCO costuma incluir categorias que orçamentos de tecnologia tradicionais subestimam: consumo variável de API ou inferência, capacitação e adoção, integração com dados e sistemas existentes, curadoria e qualidade de dados, e o custo humano de revisão e supervisão contínua. Trate a ausência de qualquer uma dessas categorias como uma premissa a declarar, não como custo zero.

## Capacidade, benefício e dupla contagem

Separe três estados que costumam ser confundidos:

| Estado | O que significa | Tratamento financeiro |
| --- | --- | --- |
| Produtividade potencial | A tarefa passou a consumir menos tempo ou esforço em observação comparável | Indicador operacional; não é economia ou receita realizada por si só |
| Capacidade realizada | A capacidade foi formalmente realocada ou absorveu demanda sem custo proporcional | Benefício plausível, sujeito a comprovação do uso |
| Benefício financeiro capturado | O efeito aparece em custo evitado verificável, despesa reduzida ou receita incremental atribuível | Pode entrar no cálculo financeiro uma única vez |

Defina uma unidade de benefício e um dono econômico para cada valor monetizado. Não conte a mesma hora poupada como economia de pessoal, capacidade para crescimento e melhoria de margem ao mesmo tempo. Quando houver rotas alternativas de captura, trate-as como cenários mutuamente exclusivos até que uma seja efetivada.

Retorno intangível continua relevante quando não puder ser monetizado com base razoável. Registre-o como evidência complementar, sem adicioná-lo ao numerador financeiro apenas para completar o caso de negócio.

## Balanced Scorecard e retorno intangível

Retorno de IA raramente é só financeiro. O Balanced Scorecard organiza indicadores em quatro perspectivas conectadas por uma cadeia causal: capacidade aprendida hoje habilita processo melhor, processo melhor habilita experiência do cliente melhor, experiência do cliente melhor habilita resultado financeiro.

| Perspectiva | Pergunta que responde | Exemplos de indicador ligado a IA |
| --- | --- | --- |
| Aprendizado e crescimento | A organização está construindo capacidade para sustentar o uso? | Letramento de dados, capacidade analítica da equipe, maturidade de infraestrutura |
| Processos internos | O trabalho está sendo executado de forma diferente e melhor? | Gargalos removidos, qualidade de saída, risco de conformidade |
| Cliente | A experiência de quem é atendido melhorou? | Tempo de resposta, personalização, retenção e satisfação |
| Financeira | O resultado financeiro capturou o ganho? | Margem, produtividade de ativos, expansão de receita |

Ao usar o Balanced Scorecard, declare para cada indicador se ele já foi convertido em valor monetário (e como) ou se permanece como evidência intangível a ser monitorada. Não some indicadores de perspectivas diferentes em um único número sem explicitar o método de conversão.

## Capital humano vs. tecnologia

Investimento em tecnologia tende a ter custo e depreciação mensuráveis; investimento em capital humano (capacitação, mudança de papel, curva de aprendizado) tem retorno mais indireto e defasado no tempo. Ao montar a mensuração:

- separe o custo de tecnologia do custo de capacitação e mudança, mesmo quando vierem do mesmo orçamento;
- reconheça que o retorno de capital humano costuma aparecer depois do retorno de tecnologia, não ao mesmo tempo;
- não atribua a uma única categoria um ganho que dependeu das duas — declare a interdependência como premissa.

## Evidência externa

Quando citar uma métrica, fórmula ou nome de framework financeiro amplamente reconhecido (por exemplo, Balanced Scorecard de Kaplan &amp; Norton, ou a definição de TCO consolidada por analistas de mercado), use-o apenas como vocabulário de referência para situar a conversa com quem já o conhece. A aplicabilidade exata, a taxa de desconto correta e o tratamento contábil de cada categoria de custo exigem sempre validação financeira e contábil local, como já indicado nos guardrails da skill.

# Camadas de Valor em Marketing

Use esta referência quando a iniciativa de IA em avaliação for de marketing, vendas ou atendimento. Ela organiza indicadores em camadas para evitar que o retorno seja reduzido a uma única métrica de topo, e trata a atribuição de causalidade como algo a testar, não a presumir. Ela não substitui o cálculo financeiro de [fundamentos financeiros](financial-fundamentals.md).

## O problema da atribuição em marketing

A erosão de rastreamento entre canais (privacidade, cookies, cliques zero) tornou a atribuição multitoque cada vez menos confiável isoladamente. Por isso, a mensuração de ROI de IA em marketing deve combinar mais de uma fonte de evidência em vez de depender de um único painel de atribuição — ver "Triangulação e causalidade" abaixo antes de reportar qualquer número de impacto.

## Modelo de cinco camadas

Organize os indicadores da saída mais direta ao resultado mais distante, e reporte cada camada com sua própria linha de base — não infira automaticamente que uma melhoria em uma camada se traduziu integralmente na camada seguinte.

| Camada | Pergunta que responde | Exemplos de evidência |
| --- | --- | --- |
| 1. Performance de campanha (saída direta) | O canal ou campanha individual melhorou? | Taxa de conversão, custo por aquisição, taxa de clique, ROAS do canal |
| 2. Impacto no pipeline | O ganho de campanha virou oportunidade de negócio? | Volume e velocidade de leads qualificados, taxa de avanço no funil, valor de pipeline atribuído à iniciativa |
| 3. Resultado de negócio | O pipeline virou receita ou eficiência real? | Receita incremental, valor de vida do cliente (LTV), Índice de Eficiência de Marketing (Receita Total / Investimento de Marketing), velocidade de entrada em mercado |
| 4. Produtividade e velocidade | A equipe produziu mais ou mais rápido com a mesma ou menor capacidade? | Horas poupadas por semana, volume de conteúdo produzido, número de testes executados, taxa de retrabalho |
| 5. Governança, risco e adoção | O uso está sendo feito de forma segura e sustentável? | Taxa de adoção da ferramenta aprovada, taxa de aprovação na primeira revisão, incidentes de qualidade ou conformidade evitados, uso de ferramentas não homologadas |

Ao montar o painel, limite-se a um número pequeno de indicadores primários por camada (o suficiente para uma decisão, não um catálogo completo) e declare, para cada um, fonte, período, população e limitação conhecida.

## Fórmulas como estrutura, não como benchmark

Estas fórmulas ajudam a organizar o cálculo; os componentes precisam ser preenchidos com dados reais da iniciativa, nunca com um percentual de mercado citado como se fosse o resultado esperado.

**ROI algorítmico** (quando o ganho vem principalmente de otimização de decisão automatizada, como precificação, recomendação ou segmentação):

```
ROI Algorítmico = ((Receita Incremental + Economia Operacional + Mitigação de Risco) − Custo Total da IA) / Custo Total da IA × 100
```

- *Receita incremental*: receita atribuível à otimização algorítmica, isolada por triangulação (ver seção seguinte).
- *Economia operacional*: tempo de produção reduzido, custo de agência ou terceiro evitado.
- *Mitigação de risco*: multa ou dano evitado por erro de conformidade ou de marca, quando houver base razoável para estimar.
- *Custo total da IA*: TCO conforme definido em fundamentos financeiros, incluindo consumo variável de API/inferência.

**Receita por FTE de marketing** (quando o ganho vem principalmente de redesenho de capacidade de equipe):

```
Receita por FTE = Receita Líquida Total Atribuível a Marketing / Total de FTEs de Marketing
```

Ao usar esta métrica, declare se a mudança no denominador (redução ou realocação de equipe) já foi decidida e efetivada, ou se é apenas uma capacidade teoricamente liberada — capacidade liberada e não realocada não deveria contar como ganho de produtividade realizado. Ver o tema da hora liberada não monetizada em [maturidade, governança e realização de valor](maturity-governance-realization.md).

## Triangulação e causalidade

Antes de atribuir um resultado à IA, combine mais de uma fonte:

- **Dados de plataforma**: métricas nativas de canal e ferramenta.
- **Modelagem de mix de marketing (MMM)**: para separar o efeito de diferentes investimentos e variáveis externas ao longo do tempo.
- **Teste de incrementalidade (grupo de controle/holdout)**: padrão mais confiável para isolar causalidade quando viável — comparar um grupo exposto à iniciativa de IA com um grupo comparável não exposto.

Quando não houver teste de incrementalidade disponível, declare essa limitação explicitamente e trate o número como correlação, não como causalidade comprovada. Sazonalidade, mudança de mercado e outras campanhas simultâneas são as causas mais comuns de má atribuição — verifique-as antes de reportar um ganho como resultado da IA.

## Desenho mínimo de evidência

Antes de iniciar a intervenção ou a comparação, registre hipótese, população elegível, unidade de comparação, intervenção, grupo ou período comparador, métrica primária, período de observação, eventos de exclusão e responsável. Isso evita escolher o recorte mais favorável depois de conhecer o resultado.

Use a evidência mais forte que o contexto permitir:

1. teste controlado ou holdout comparável, para afirmação causal dentro do escopo testado;
2. quase-experimento por período, região ou processo, com fatores externos documentados, para estimativa causal condicionada;
3. série histórica com baseline e triangulação independente, para associação estimada;
4. painel isolado, relato operacional ou percepção, apenas como sinal exploratório.

Não some o mesmo ganho em múltiplas camadas. Uma melhora de campanha pode sustentar uma hipótese sobre pipeline; somente a receita incremental efetivamente isolada entra como benefício financeiro. Mantenha a cadeia entre camadas visível em vez de converter cada etapa em receita.

## Evidência externa

Faixas de ganho citadas em pesquisas de mercado (por exemplo, percentuais de aumento de receita, redução de custo por aquisição, ou horas poupadas por semana) variam por setor, maturidade e método de medição do estudo original. Cite-as apenas com fonte, data e escopo, e não as apresente como o resultado esperado da iniciativa em avaliação — converta-as em hipótese a testar com os dados reais disponíveis, conforme os guardrails da skill.

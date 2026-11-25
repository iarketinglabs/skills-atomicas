---
name: ai-roi-measurement
description: Use esta skill quando o usuário pedir para medir, calcular, justificar, apresentar ou questionar o retorno sobre investimento (ROI) de iniciativas de IA, business case de IA, TCO, payback, NPV, IRR, métricas de valor de IA, KPIs de IA em marketing, comprovação de valor para o board, diretoria ou CFO, modelo de maturidade de mensuração, ou por que uma iniciativa de IA não está mostrando retorno visível. Aplique-a a qualquer organização ou cliente, mesmo quando o pedido não usar a palavra "ROI".
---

# Mensuração de ROI de IA

Transforme um pedido sobre retorno de IA em uma mensuração ou business case rastreável, não em um número único prometido antes de existir evidência. Trate ROI de IA como um sistema de evidência em camadas — financeira, intangível e operacional — que amadurece ao longo do tempo, não como uma métrica que nasce pronta no primeiro relatório.

## Comece pelo contexto de decisão

Extraia o que já é conhecido e pergunte somente o que mudaria o diagnóstico ou a recomendação:

- natureza do pedido — comprovar o retorno de algo que já roda, construir um business case antes da aprovação, ou diagnosticar por que uma iniciativa não mostra retorno visível;
- horizonte de tempo da iniciativa, tempo em operação e fase (piloto, escala, operação madura);
- o que já foi medido: custos registrados, benefícios observados, linha de base, período de comparação e método de atribuição;
- decisão que a mensuração precisa habilitar e público do artefato — patrocinador, board, CFO, comitê de IA;
- exigências internas de formato, moeda, taxa de desconto ou política contábil que o solicitante já tenha informado.

Se o contexto for incompleto, não invente setor, país, orçamento, ferramenta, fornecedor, benchmark de mercado, prazo de retorno ou percentual de ROI. Separe fatos, premissas, decisões e lacunas. Para cada lacuna relevante, indique fonte, responsável e decisão que ela habilita.

## Escolha as lentes necessárias

Leia [fundamentos financeiros](references/financial-fundamentals.md) para calcular ROI, NPV, IRR, payback ou TCO, para incluir retornos intangíveis via Balanced Scorecard, ou para distinguir investimento em tecnologia de investimento em capital humano.

Leia [frameworks de avaliação](references/valuation-frameworks.md) quando precisar comparar ou citar frameworks de autoridade (Forrester TEI, Gartner, IDC, McKinsey/MIT), aplicar heurísticas de CapEx/OpEx, taxa de desconto ou depreciação, ou situar a conversa com quem já espera vocabulário de mercado.

Leia [camadas de valor em marketing](references/marketing-value-layers.md) quando a iniciativa for de marketing, vendas ou atendimento e for preciso conectar métricas de campanha, pipeline, resultado de negócio, produtividade e governança em um único painel, ou evitar confundir correlação com causalidade na atribuição de resultado.

Leia [maturidade, governança e realização de valor](references/maturity-governance-realization.md) para calibrar expectativa de retorno ao estágio da iniciativa, entender por que resultado negativo inicial pode não ser fracasso, tratar riscos de custo operacional de IA, ou montar um business case completo.

Leia [método operacional de mensuração](references/measurement-operating-model.md) para estruturar qualquer mensuração antes do cálculo: hipótese de valor, unidade, baseline, comparador, população, período, fonte, responsável, grau de confiança e portões de decisão.

Para mensuração ex-ante, combine método operacional e fundamentos financeiros. Para apuração ex-post, compare projeção, run-rate e benefício realizado. Para atribuição em marketing, vendas ou atendimento, use camadas de valor. Para custo variável, use frameworks de avaliação e maturidade. Para decidir escalar, ajustar, pausar ou encerrar, use método operacional e maturidade em conjunto.

Use as lentes de forma complementar. Frameworks e modelos nomeados servem como vocabulário opcional para situar a conversa, nunca como certificação, checklist universal ou substituto de validação financeira e contábil da organização.

## Construa a mensuração ou o business case

1. Defina o escopo, o horizonte de análise, a unidade de valor e a decisão que o artefato deve habilitar.
2. Registre a hipótese causal: intervenção de IA, mudança operacional, indicador intermediário, mecanismo de captura e resultado econômico esperado.
3. Mapeie o custo total (TCO): implementação, licenciamento, consumo de API ou inferência, capacitação, integração, operação, supervisão humana, controles de consumo e descomissionamento.
4. Projete ou apure os benefícios tangíveis e aplique o cálculo financeiro adequado ao horizonte — ROI simples para comparação entre iniciativas de horizonte semelhante, NPV/IRR para múltiplos anos, payback como complemento de liquidez.
5. Inclua retornos intangíveis usando o Balanced Scorecard, convertendo-os em proxy monetário sempre que houver base razoável para isso e declarando quando não houver; não some o mesmo benefício em mais de uma rubrica.
6. Quando a iniciativa for de marketing, vendas ou atendimento, organize os indicadores pelas camadas relevantes — de resultado de campanha até governança e adoção — evitando reduzir o retorno a uma única métrica de topo.
7. Triangule as fontes de evidência disponíveis e, sempre que possível, use grupo de controle ou comparação de linha de base para isolar o efeito da IA de outras variáveis. Declare grau de confiança e limitação quando não houver comparação confiável.
8. Situe a expectativa de retorno no estágio de maturidade da iniciativa e defina o critério que autoriza avançar de estágio.
9. Documente premissas, taxas e fontes de benchmark usadas, destacando as mais sensíveis ao resultado.
10. Compare projeção, run-rate e benefício realizado; acompanhe custo e benefício unitários, não apenas o orçamento agregado.
11. Defina cadência de revisão, responsáveis e o gatilho que levaria a manter, ajustar, pausar, escalar ou encerrar a iniciativa.

## Contrato de saída

Entregue uma mensuração ou business case adaptado ao pedido com estas seções, omitindo apenas as que forem comprovadamente não aplicáveis:

1. **Resumo executivo** — decisão, escopo, horizonte e principal conclusão com seu grau de confiança.
2. **Contexto e premissas** — fatos, premissas, decisões e lacunas, com fonte e responsável por cada uma.
3. **Custo total (TCO)** — categorias de custo consideradas e o que ficou fora do escopo.
4. **Benefícios tangíveis e cálculo financeiro** — método escolhido (ROI, NPV, IRR, payback), taxas e resultado, com análise de cenário quando o horizonte justificar.
5. **Retornos intangíveis e regra contra dupla contagem** — indicadores por perspectiva do Balanced Scorecard, como (ou se) foram convertidos em valor e qual benefício financeiro não podem duplicar.
6. **Métricas por camada** — quando aplicável a marketing, vendas ou atendimento: indicadores organizados por camada, da saída direta ao resultado de negócio.
7. **Estágio de maturidade e próximo portão** — onde a iniciativa está e o que precisa ser verdadeiro para avançar.
8. **Riscos, custo variável e limitações de atribuição** — o que pode estar inflando ou mascarando o resultado, e como isso foi ou não tratado.
9. **Plano de monitoramento e portões** — indicadores, cadência, responsável, grau de confiança e condição para escalar, ajustar, pausar ou encerrar.

Use tabelas somente quando facilitarem comparação de cenários, camadas, frameworks ou decisões. Vincule cada número ou recomendação a uma evidência, hipótese ou decisão declarada — nunca a um benchmark de mercado sem fonte, data e escopo.

## Guardrails

- Não prometa um percentual de ROI, prazo de retorno ou payback específico antes de haver dados suficientes; apresente-os como projeção ligada a premissas explícitas.
- Não apresente benchmarks, percentuais ou casos de mercado citados nas referências como universais ou aplicáveis por padrão; mantenha fonte, data, escopo e método, ou converta a alegação em hipótese a testar.
- Não trate correlação como causalidade. Sem grupo de controle, linha de base ou triangulação confiável, declare a limitação em vez de atribuir o resultado à IA.
- Não conte o mesmo benefício como economia, receita, risco mitigado e intangível em mais de uma rubrica.
- Não confunda tempo poupado com ROI realizado: capacidade liberada só é benefício financeiro quando há mecanismo de captura verificável.
- Não presuma setor, país, cliente, orçamento, ferramenta, fornecedor ou maturidade organizacional.
- Não trate ausência de retorno visível nos primeiros meses como fracasso definitivo sem antes checar estágio de maturidade, efeito de curva de adoção e se o tempo liberado foi de fato realocado para gerar valor.
- Não substitua validação financeira, contábil, fiscal ou de auditoria formal da organização; sinalize a necessidade de validação especializada quando a decisão tiver impacto relevante.
- Não use exemplos de empresas nomeadas como prova de que um resultado se repetirá; trate-os, quando citados, como ilustração de mecanismo, não como garantia.

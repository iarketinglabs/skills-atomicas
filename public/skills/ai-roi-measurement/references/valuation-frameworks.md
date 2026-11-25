# Frameworks de Avaliação

Use esta referência como vocabulário opcional para situar a conversa com quem já espera termos de mercado, e como fonte de heurísticas orçamentárias. Nenhum framework aqui substitui o cálculo financeiro descrito em [fundamentos financeiros](financial-fundamentals.md); eles complementam a leitura de valor, sobretudo onde o cálculo puro subestima benefício ou risco.

## Panorama comparativo

| Framework | Foco analítico | Pontos fortes | Limitações |
| --- | --- | --- | --- |
| Forrester Total Economic Impact (TEI) | Benefícios, custos, flexibilidade e risco em conjunto, geralmente via entrevistas estruturadas | Metodologia explícita; incorpora valor de opção (flexibilidade futura) e ajuste de risco | Estudos são frequentemente patrocinados por um fornecedor específico; tratar como ilustrativo, não como prova |
| Gartner (Hype Cycle e métricas de ROI) | Estágio de maturidade da tecnologia no mercado e expectativa associada | Ajuda a calibrar expectativa de retorno ao estágio de adoção do mercado | Não é uma fórmula de ROI própria; é leitura de maturidade, não substituto de cálculo financeiro |
| IDC Business Value Framework | Nove dimensões de impacto (entre elas geração de receita, experiência do cliente, sustentabilidade, tempo de mercado, resiliência do negócio) | Evita subestimar valor por medir só custo e produtividade, as duas dimensões mais comuns | Exige disciplina para de fato medir as dimensões menos óbvias, não só as mais fáceis |
| Modelos McKinsey/MIT baseados em tarefa | Decomposição do trabalho em tarefas automatizadas vs. aumentadas, com custo marginal de mão de obra vs. de computação | Granularidade útil para identificar onde o ganho realmente ocorre | Exige mapeamento detalhado de tarefas, nem sempre disponível no início de uma iniciativa |

Ao citar qualquer um desses frameworks, informe a fonte e, quando disponível, a data do estudo ou pesquisa referenciada. Trate estatísticas de adoção e ROI de mercado (por exemplo, taxas de adoção, percentual de empresas que reportam ganho de EBIT, ou percentual de projetos abandonados) como evidência externa datada, não como taxa esperada para a iniciativa em avaliação — o guardrail da skill contra apresentar benchmark como universal se aplica igualmente aqui.

## Heurísticas orçamentárias

- **CapEx vs. OpEx**: infraestrutura de TI tradicional costuma ser financiada como CapEx amortizado ao longo de vários anos; iniciativas de IA baseadas em consumo (API, tokens, inferência) tendem a ser OpEx elástico, que varia com o volume de uso. Ao montar o TCO, não trate os dois regimes com a mesma lógica de depreciação.
- **Custo unitário variável**: para iniciativas de IA generativa ou agentic, compare o custo marginal por unidade de trabalho executada pela IA (custo de inferência) com o custo marginal equivalente de mão de obra humana, em vez de comparar apenas o orçamento total.
- **Taxa de desconto:** use a taxa definida pela política financeira ou pela decisão em análise. Quando não estiver disponível, registre a taxa escolhida, sua justificativa e o efeito dela no cenário; não a embuta silenciosamente no resultado.
- **Vida útil e tratamento contábil:** defina amortização, depreciação ou tratamento de despesa conforme a natureza do ativo e a política local. Não extrapole o ciclo de vida de outra tecnologia como regra para a iniciativa avaliada.
- **Construção faseada do business case**: prefira validar a hipótese de valor em fases (protótipo → piloto controlado → escala) a comprometer o orçamento total de uma vez; cada fase deve gerar evidência que reduz a incerteza da fase seguinte.
- **Ajuste de risco**: ao projetar benefício futuro, é comum aplicar um desconto conservador sobre ganhos projetados (e inflar levemente a provisão de custo) para compensar incerteza de estimativa — declare esse ajuste como premissa, com o percentual usado, em vez de embuti-lo silenciosamente no número final.

## FinOps e custo variável de IA

Em iniciativas com custo de uso variável, acompanhe a economia da operação junto do resultado de negócio:

- defina a unidade de trabalho relevante e apure custo por unidade concluída com qualidade aceita, não apenas custo por chamada;
- compare consumo real, custo unitário e volume com a projeção em cada revisão;
- inclua tentativas repetidas, erros, reprocessamentos, armazenamento, observabilidade e supervisão humana no custo total;
- estabeleça limites de gasto, alertas e condição de interrupção para evitar que falhas operacionais se tornem perdas não percebidas;
- reporte ganho marginal de qualidade ou velocidade ao lado do custo marginal quando houver alternativas de execução.

Esses controles não pressupõem ferramenta ou arquitetura. Eles tornam visível se a variação de custo acompanha valor realizado ou apenas volume de uso.

## Evidência externa

Cite nomes de framework, firma de análise ou estudo apenas como vocabulário de referência para situar a conversa com quem já os conhece. Números específicos de estudos de caso (por exemplo, um estudo de TEI patrocinado por um fornecedor de nuvem ou de analytics) devem ser tratados como exemplo de mecanismo, não como taxa de retorno esperada — o patrocínio do estudo por um fornecedor é, por si, uma razão para tratá-lo como potencialmente enviesado. A aplicabilidade de qualquer framework ao caso em avaliação exige sempre validação local de negócio e finanças, como já indicado nos guardrails da skill.

# Estatística, Experimentação e Machine Learning

## Declare a Pergunta

Separe três objectivos antes de escolher dados ou métricas:

- **Descritivo:** o que aconteceu na população observada?
- **Preditivo:** que resultado futuro se pretende estimar para casos novos?
- **Causal:** que mudança teria sido causada por uma intervenção definida?

Um modelo preditivo com bom desempenho não identifica, por si só, o efeito de uma intervenção. Se a pergunta for causal, declare população, intervenção, comparador, resultado e horizonte; documente hipóteses de identificação e possíveis confundidores. Prefira randomização quando for viável e ética; em dados observacionais, declare os limites do desenho.

## Preparação e Divisão

- Defina a unidade de análise, critérios de inclusão/exclusão, período e população-alvo.
- Use divisões por tempo ou entidade quando isso imitar o uso futuro e impedir fuga entre treino e teste.
- Ajuste imputação, normalização, selecção de variáveis e qualquer transformação aprendida usando apenas treino dentro do processo de validação.
- Mantenha teste final sem uso repetido para selecção. Se o conjunto já orientou escolhas, assinale a contaminação e obtenha uma avaliação nova.
- Verifique target leakage, features posteriores ao resultado, duplicatas entre partições, seleção de sobreviventes e mudanças de definição.

## Métricas e Incerteza

Escolha métricas que representem custo e consequência de erro, incluindo baseline, taxa-base, limiar de decisão e segmentos relevantes. Reporte tamanho da amostra, janela, população, incerteza e missingness. Um valor-p não é a probabilidade de a hipótese ser verdadeira; significância estatística não garante relevância prática.

Em experiências online, pré-defina unidade de randomização, hipótese, métrica primária, métricas de guarda, tamanho/duração ou regra válida de paragem, exclusões e análise de segmentos. Confira contaminação entre grupos, novelty effects, alterações simultâneas e validade do instrumento. Não anuncie um “uplift causal” quando a alocação ou o controlo não sustentam a inferência.

## Modelos em Produção

Versione os dados, features, código, configuração, modelo e métricas de treino. Monitorize qualidade e mudança da distribuição no tempo e por segmentos, sem misturar drift de entrada com degradação do resultado. Defina política para reavaliação, rollback e owner. Para decisão de alto impacto, não substitua revisão e validação apropriadas por uma métrica agregada.

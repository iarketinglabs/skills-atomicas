# Avaliação e medição

## Quatro perguntas diferentes

Organize a medição em camadas para não atribuir a uma única métrica respostas que ela não dá:

1. **Qualidade do comportamento:** o sistema executa a tarefa conforme a rubrica?
2. **Valor de produto:** a pessoa conclui melhor a tarefa e volta a obter valor?
3. **Operação:** qual é a latência, disponibilidade, falha, revisão e custo?
4. **Risco e proteção:** que danos, violações, enviesamentos ou ações indevidas ocorrem?

Escolha uma métrica de resultado central para a decisão e métricas de apoio adequadas. AARRR pode organizar o ciclo de aquisição, ativação, retenção, referência e receita; HEART pode estruturar perguntas de experiência; uma North Star pode expressar valor recorrente entregue. Nenhum destes modelos é uma métrica universal nem substitui os sinais de qualidade, risco e custo de IA.

## Desenhar um eval útil

Defina o objeto avaliado: modelo, prompt, retrieval, chamada de ferramenta, trajetória agentiva ou sistema de ponta a ponta. Cada caso deve representar uma tarefa real e conter:

- intenção ou cenário e slice relevante;
- entrada minimizada ou uma referência segura à entrada;
- comportamento esperado ou rubrica observável;
- severidade e consequência da falha;
- fonte ou responsável pela expectativa, quando aplicável;
- versão do sistema e resultado da avaliação.

Inclua casos frequentes, difíceis, ambíguos, contraditórios e de cauda; casos seguros e adversariais; línguas, populações, fontes e modos de interação relevantes. Não deixe a média agregada esconder um slice crítico.

Versione casos, rubricas e resultados. Separe exemplos usados para desenvolver de casos protegidos para comparação final. Adicione falhas reais observadas, com os dados pessoais e sensíveis removidos ou protegidos conforme a política aplicável. Evite afinar o sistema apenas para os exemplos conhecidos.

## Julgamento humano e avaliação automática

Use revisores humanos para criar ou calibrar rubricas em tarefas subjetivas e de alto impacto. Se usar um modelo como avaliador:

- compare uma amostra com avaliação humana;
- especifique critérios concretos e o que constitui evidência;
- verifique enviesamento por posição, estilo, comprimento e família de modelo;
- reporte desacordos e falhas por segmento;
- mantenha revisão humana onde um erro de avaliação teria consequências materiais.

Uma concordância média elevada não prova validade para todos os casos. Em tarefas sem resposta única, represente desacordo ou intervalos de julgamento em vez de inventar um ground truth inequívoco.

## Métricas de produto e operação

Escolha conforme a tarefa. Exemplos a considerar:

- conclusão bem-sucedida e qualidade aceite;
- erro factual ou resposta sem suporte quando grounding é necessário;
- taxa de abstenção, escalonamento, correção, repetição e abandono;
- ações aprovadas, canceladas, revertidas ou incorretas;
- p50 e p95 de latência, timeouts, retries e disponibilidade;
- custo total por tentativa, por tarefa concluída e por resultado aceite;
- distribuição dos resultados por intenção, risco, idioma, fonte e tipo de utilizador.

Defina baseline sem IA ou com a solução atual. Registe definições, denominadores, janela e segmentos. Não otimize custo ou volume sem uma barra de qualidade e proteção.

## Decidir sobre rollout

Antes do lançamento, associe cada métrica a um limite, dono e resposta. Declare quais falhas bloqueiam release, quais exigem revisão e quais são monitorizadas por amostragem. Faça rollout gradual quando reduzir exposição e permitir interromper ou reverter.

Mudanças de modelo, prompt, retrieval, ferramentas, dados, políticas ou interface podem alterar comportamento. Reexecute evals relevantes, registe versões e investigue regressões antes de ampliar tráfego. Monitorize a distribuição real de pedidos e resultados; reabra discovery quando o uso divergir da hipótese inicial.

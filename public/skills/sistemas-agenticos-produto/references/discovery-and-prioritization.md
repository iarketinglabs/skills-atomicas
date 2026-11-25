# Discovery e priorização

## Começar pelo resultado

Formule primeiro:

- Quem tenta progredir e em que circunstância?
- Que tarefa está a tentar concluir?
- Que resultado quer melhorar e como reconheceria a melhoria?
- Como resolve a tarefa hoje, incluindo trabalho manual, serviços, folha de cálculo ou outros produtos?
- O que acontece quando a tarefa falha, atrasa ou exige retrabalho?

Use Jobs-to-be-Done para descrever a tarefa e o contexto sem embutir uma funcionalidade na definição. Quando forem úteis, formule resultados desejados como mudanças observáveis em tempo, esforço, erro, previsibilidade ou taxa de conclusão. Não confunda aquilo que a pessoa declara querer com comportamento observado ou disposição para pagar.

## Recolher e preservar evidência

Combine fontes conforme a pergunta: entrevistas, observação da tarefa, dados de utilização, suporte, pesquisa, testes de conceito, experiências ou registos operacionais. Registe período, população, método e limitações. Uma amostra de conveniência pode revelar mecanismos e linguagem; não estima necessariamente prevalência no mercado.

Use IA para procurar, resumir ou agrupar material, mas preserve ligações aos registos originais e amostre os resultados. Clusters coerentes não provam frequência, importância causal ou valor económico. Mantenha opiniões divergentes e casos negativos em vez de os apagar numa síntese única.

## Organizar oportunidades

Uma Opportunity Solution Tree ou mapa equivalente liga:

1. Resultado de produto ou negócio.
2. Necessidades, problemas ou oportunidades que podem influenciar esse resultado.
3. Soluções alternativas para cada oportunidade.
4. Testes que distinguem as hipóteses.

Não salte diretamente de um objetivo para uma solução. Cada oportunidade importante deve apontar para evidência e cada solução deve apontar para uma hipótese testável. Evite mapas extensos sem consequência de decisão.

## Priorizar sem falsa precisão

Escolha o método pela pergunta:

| Método | Use quando | Limite a explicitar |
|---|---|---|
| RICE | É preciso comparar alcance, impacto, confiança e esforço entre itens relativamente comparáveis. | As estimativas podem dominar o ranking; dependências e obrigações podem sobrepor-se ao score. |
| ICE | É necessária uma triagem rápida de muitas hipóteses. | Impacto, confiança e facilidade podem ser subjetivos e inconsistentes. |
| Kano | A pergunta é como diferentes atributos afetam satisfação e expectativas. | Categorias mudam com o tempo e dependem da formulação; não é um modelo de ROI. |
| WSJF ou custo do atraso | O custo de adiar e o tamanho relativo do trabalho são úteis para ordenar uma fila partilhada. | Scores ordinais não são valores financeiros precisos. |

Registe a origem de cada estimativa e faça análise de sensibilidade: se o alcance ou a confiança mudar, a recomendação muda? Reserve espaço para requisitos legais, dependências, riscos, reversibilidade e compromissos já assumidos.

## Descoberta contínua e delivery

Discovery e entrega são trabalhos recorrentes da equipa, não um funil em que uma equipa entrega requisitos fechados a outra. Use o artefacto que responde à incerteza atual: conversa, mapa, protótipo, especificação, teste, eval ou implementação limitada.

Protótipos gerados rapidamente podem ajudar a explorar interação e obter feedback. Não demonstram segurança, escalabilidade, acessibilidade, manutenção ou prontidão para produção. Uma especificação curta continua útil para explicitar critérios de aceitação, dados, estados de falha e restrições que o protótipo não mostra.

## Experiências

Antes de um teste A/B, defina hipótese, população, unidade de randomização, métrica primária, métricas de proteção, efeito mínimo que mudaria a decisão, janela, tamanho de amostra e regras de paragem. Verifique a qualidade da instrumentação e possíveis interferências.

Use um A/B quando a randomização é viável e a pergunta causal justifica amostra e exposição. Para baixo volume, alto risco ou efeitos lentos, considere rollout gradual, comparação qualitativa, estudo de tarefa, análise por coorte ou outra abordagem; declare o que essa evidência permite e não permite concluir.

Num produto com IA, separe:

- **Qualidade do sistema:** o comportamento melhorou em casos representativos?
- **Valor para a pessoa:** a tarefa tornou-se mais eficaz, rápida ou satisfatória?
- **Viabilidade operacional:** qualidade, latência, custo e segurança permanecem aceitáveis?

Uma resposta melhor num benchmark offline não prova melhoria no comportamento real. A ausência de significância também não prova ausência de efeito quando o teste tem baixa potência.

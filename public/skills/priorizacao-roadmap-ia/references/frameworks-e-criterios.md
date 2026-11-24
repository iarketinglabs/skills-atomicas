# Frameworks e critérios de priorização

## Sumário

1. Fundamentos
2. Seleção do framework
3. Critérios adicionais para IA
4. Scorecard e leitura de evidência
5. Governança e FinOps

## 1. Fundamentos

Priorizar é alocar capacidade escassa sob incerteza. A análise deve considerar simultaneamente:

| Fundamento | Pergunta operacional |
| --- | --- |
| Incerteza | O que é fato, hipótese, estimativa ou desconhecido? |
| Custo de oportunidade | Qual alternativa deixa de receber a mesma capacidade? |
| Valor do tempo | O valor cai, cresce ou permanece estável se houver atraso? |
| Fluxo/WIP | Quantos itens podem avançar sem aumentar o lead time? |
| Racionalidade limitada | A escala e os dados tornam o score comparável ou apenas mais preciso na aparência? |
| Opção de aprendizagem | Um experimento barato pode evitar compromisso irreversível? |

Use a Lei de Little (`L = λW`) como alerta de fluxo: com throughput estável, mais trabalho em andamento tende a aumentar o tempo médio no sistema. Um ranking sem capacidade e WIP é apenas um backlog ordenado.

## 2. Seleção do framework

| Pergunta | Método | O que entrega | O que não entrega |
| --- | --- | --- | --- |
| Qual item deve vir antes entre alternativas comparáveis? | RICE | Reach × Impact × Confidence ÷ Effort, com horizonte definido | Verdade causal, dados confiáveis ou capacidade por si só |
| Como triar muitos experimentos rapidamente? | ICE | Impact, Confidence e Ease em escala explicitada | Fórmula canônica universal; não invente uma |
| Que tipo de valor/satisfação o atributo produz? | Kano | Básico, desempenho, atrativo e outras categorias de expectativa | Ranking econômico, esforço ou Cost of Delay |
| O que é indispensável para manter a entrega viável? | MoSCoW | Must, Should, Could, Won't this time | Ranking fino dentro de cada grupo |
| Qual atraso custa mais e qual trabalho libera valor mais cedo? | Cost of Delay/WSJF | Custo relativo do atraso dividido pela duração relativa | Validação do problema ou da solução |
| Qual oportunidade merece discovery antes da solução? | Opportunity Solution Tree | Outcome → oportunidades → soluções → testes | Alocação completa de capital |
| Qual entrega sustenta que mudança de comportamento? | Impact Mapping | Goal → actors → impacts → deliverables | Probabilidade, esforço ou retorno automaticamente |
| Como comunicar compromisso e incerteza? | Now-Next-Later | Horizonte de certeza decrescente | Score econômico ou cronograma garantido |

Combine somente métodos ortogonais. Um arranjo comum é `OST/Impact Mapping` para causalidade, `RICE ou WSJF` para decisão de capacidade e `Now-Next-Later` para comunicação.

## 3. Critérios adicionais para IA

Pontue ou descreva cada item nos eixos abaixo. Não some dimensões sem declarar pesos; em casos de alto risco, um veto ou gate pode ser mais apropriado que uma média.

| Eixo | Evidência esperada | Sinal de risco |
| --- | --- | --- |
| Workflow | Frequência, repetição, fronteira e handoffs | Processo instável ou dívida de workflow |
| Valor | Custo, margem, receita, qualidade, SLA ou risco afetado | Caso de uso sem outcome mensurável |
| Dados | Fonte, acesso, qualidade, atualização e escopo | Dado ausente, sensível ou não auditável |
| Baseline | Medição antes da intervenção e unidade | Percentual sem período, população ou denominador |
| Erro | Reversibilidade, tolerância, fallback e revisão | Ação irreversível ou dano difícil de detectar |
| Autonomia | Assistência, recomendação, ação ou decisão | Poder operacional maior que a evidência |
| Integração | Sistemas, ferramentas, permissões e dependências | Muitos sistemas atravessados e falhas acumuladas |
| Pessoas | Owner, literacia, change load, incentivos e accountability | Treinamento isolado sem mudança no trabalho |
| Economia | Custo total, consumo, adoção e tempo até valor | ROI baseado só em uso ou benefício bruto |

Trate `workflow debt` antes de automatizar: remova handoffs redundantes, aprovações sem propósito e workarounds históricos quando isso for parte do problema.

## 4. Scorecard e evidência

Use uma escala simples e documente a régua:

```text
valor: 0-5       confiança: 0-5       Cost of Delay: 0-5
esforço: 0-5     risco: 0-5            change load: 0-5
reversibilidade: 0-5                  prontidão de dados: 0-5
```

Uma fórmula possível é `valor ajustado = (valor × confiança × urgência × reversibilidade) / (esforço × risco)`, mas ela é uma heurística local, não um padrão universal. Use-a somente se os itens forem comparáveis, declare pesos e mostre a análise de sensibilidade. Para iniciativas de alto dano potencial, aplique gates mínimos de governança antes do ranking.

Classifique cada claim como:

- `VERIFICADA`: duas ou mais fontes independentes ou fonte primária apropriada;
- `FONTE ÚNICA`: observação de uma pesquisa, fornecedor ou população específica;
- `CASO OBSERVADO`: resultado local sem generalização;
- `INFERÊNCIA`: conclusão derivada, não uma afirmação publicada;
- `[PENDENTE]`: dado necessário ainda não coletado.

Ao comparar números divergentes, normalize população, data, definição, unidade, maturidade, denominador e interesse da fonte. Uma pesquisa sobre organizações em estágio avançado pode coexistir com outra sobre organizações em piloto sem que uma invalide a outra.

## 5. Governança e FinOps

Mapeie a autonomia na sequência:

```text
assistência sem ação → recomendação → ação reversível → ação transacional → decisão material/irreversível
```

Movendo-se para a direita, exija progressivamente identidade, menor privilégio, logs, explicabilidade, revisão humana, limites, testes, rollback, segregação de funções e responsável por incidentes.

Inclua no custo total: modelo/compute, integração, dados, engenharia, revisão humana, monitoramento, governança, suporte, retrabalho e change management. Use limites de consumo, detecção de loops e atribuição por workflow quando houver execução recursiva. A infraestrutura de controle não deve ser presumida como obrigatória para todo caso, mas a necessidade de visibilidade e limites deve ser decidida antes da produção.

## Fontes-base consultadas

Os documentos-fonte triangulam fundamentos de decisão, custo de oportunidade, Lei de Little e opções reais com materiais canônicos de RICE, MoSCoW, WSJF, Kano, Opportunity Solution Tree, Impact Mapping e Now-Next-Later. Para IA, sintetizam evidências recentes de McKinsey, Bain, BCG, Deloitte, Gartner, Stanford HAI, Anthropic e dados específicos de fornecedores. Revalide claims temporais, percentuais e disponibilidade antes de tratá-los como atuais.

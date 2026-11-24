---
name: priorizacao-roadmap-ia
description: "Use esta skill sempre que for necessário priorizar iniciativas, produtos, projetos ou casos de uso de IA, comparar frameworks de decisão, avaliar quick wins, transformar um backlog em roadmap ou justificar uma sequência de investimento. Aplique-a mesmo quando o pedido disser apenas 'organizar prioridades', 'montar roadmap' ou 'escolher os melhores casos de IA'."
---

# Priorização e Roadmap de IA

Transforme alternativas concorrentes em decisões explícitas de investimento, com valor, custo de oportunidade, tempo, capacidade, incerteza e risco visíveis. Use as referências desta skill para selecionar o método adequado e não tratar um score como verdade objetiva.

## Fluxo operacional

### 1. Defina a decisão antes do ranking

Esclareça, a partir do pedido e dos dados disponíveis:

- qual outcome, problema ou restrição motivou a decisão;
- qual unidade está sendo priorizada: iniciativa, oportunidade, solução, experimento, requisito ou capacidade;
- horizonte e capacidade reais: pessoas, tempo, orçamento, dependências e limite de trabalho em progresso (WIP);
- quem decide, quem executa e qual é o critério de parada ou aprovação.

Se faltarem dados que mudem materialmente a ordem, marque-os como `[PENDENTE]` e produza uma priorização provisória com suas premissas. Não invente capacidade, ROI, alcance, baseline ou aprovação.

### 2. Normalize cada alternativa

Converta cada item para uma ficha comparável:

```text
id | problema/outcome | proposta | beneficiário | valor esperado
evidência | confiança | esforço/duração | urgência/Cost of Delay
dependências | reversibilidade | risco | owner | métrica e baseline
```

Separe problema de solução. Quando o item ainda for hipótese, registre o experimento ou a aprendizagem necessária antes de prometer execução.

### 3. Escolha o método pela pergunta

Leia `references/frameworks-e-criterios.md` e escolha um método principal. Use métodos complementares apenas quando respondem a perguntas diferentes:

- **Ordenar alternativas comparáveis:** RICE; ICE somente como triagem leve e sem presumir uma fórmula universal.
- **Entender o tipo de valor para o usuário:** Kano.
- **Proteger escopo mínimo de uma entrega/timebox:** MoSCoW.
- **Sequenciar considerando atraso e duração:** Cost of Delay/WSJF.
- **Explorar o problema antes de fixar solução:** Opportunity Solution Tree.
- **Explicitar a cadeia causal até o outcome:** Impact Mapping.
- **Comunicar horizonte e incerteza:** Now-Next-Later.

Não aplique todos à mesma lista para eleger um vencedor. Explique qual pergunta cada método responde e onde sua saída não é suficiente.

### 4. Calcule, critique e ajuste

Use unidades, horizontes e escalas consistentes. Mostre fórmula, entradas, fonte e confiança. Depois faça uma revisão qualitativa para identificar:

- pontuações com falsa precisão ou `confidence theater`;
- alcance, impacto ou esforço sem baseline;
- urgência confundida com magnitude de valor;
- dependências, WIP ou capacidade omitidos;
- benefício positivo, mas inferior ao melhor uso alternativo da mesma capacidade;
- uma etapa de descoberta que compra informação e reduz um compromisso irreversível.

Nunca ajuste um score silenciosamente. Registre a razão, o dado que mudaria a decisão e se o resultado é `VERIFICADO`, `FONTE ÚNICA`, `CASO OBSERVADO`, `INFERÊNCIA` ou `[PENDENTE]`.

### 5. Faça a triagem específica de IA

Para cada caso de IA, acrescente:

1. frequência e repetibilidade do workflow;
2. valor operacional ou empresarial identificável;
3. acesso, qualidade e delimitação dos dados;
4. baseline de tempo, qualidade, custo, throughput ou conversão;
5. erro reversível/controlável e possibilidade de revisão humana;
6. saúde do processo: não automatizar `workflow debt` sem antes redesenhá-lo;
7. owner operacional, change load, literacia e incentivos necessários;
8. autonomia, ferramentas, permissões, sistemas atravessados, observabilidade e rollback;
9. custo total, limites de consumo e caminho de atribuição do valor.

Use a sequência de governança `assistência sem ação → recomendação → ação reversível → ação transacional → decisão material/irreversível`. Quanto mais à direita, maior a exigência de identidade, menor privilégio, logs, aprovação, limites, testes, segregação de funções e accountability.

Um quick win não é apenas uma implementação tecnicamente pequena. Prefira workflow frequente, dados acessíveis, baseline mensurável, fronteira clara, risco controlável e dono definido. Reduza autonomia inicial quando isso permitir comprar evidência antes de conceder poder operacional.

### 6. Converta a ordem em roadmap

Leia `references/modelo-de-saida.md` e produza horizontes que expressem certeza, não datas fictícias:

- **Now:** compromisso executável, owner, capacidade reservada, métrica e gate;
- **Next:** próxima aposta condicionada a evidência e dependências explícitas;
- **Later:** direção ou opção de aprendizagem, sem compromisso de escopo/datas.

Quando houver demanda por prazos, associe cada horizonte a uma condição de entrada, saída e replanejamento. Limite WIP e explicite o que será adiado ou abandonado para liberar capacidade.

Todo piloto deve ter hipótese, baseline, janela de medição, critério binário de sucesso, kill criteria, revisão humana e decisão seguinte. Inclua mudança organizacional, dados, governança e operação no mesmo roadmap técnico.

### 7. Entregue decisão auditável

Use o contrato de `references/modelo-de-saida.md`. Apresente primeiro a recomendação e depois o raciocínio. Inclua alternativas rejeitadas, premissas, evidências, incertezas, trade-offs, dependências, capacidade, riscos e gatilhos de revisão.

Se claims de mercado divergirem, compare população, período, definição, denominador, nível de maturidade e interesse da fonte antes de concluir que há contradição. Não transforme uma estatística de survey, vendor ou grupo de alto desempenho em expectativa mediana.

## Guardrails

- Priorize outcomes e problemas antes de features ou ferramentas.
- Não confunda adoção, prompts, tokens, licenças ou velocidade de uma tarefa com ROI empresarial.
- Não trate governança como checklist posterior: ela altera custo, tempo, risco e prioridade.
- Não recomende agente autônomo sem autoridade, permissões, logs, fallback, owner e aprovação proporcionais ao dano possível.
- Não automatize processo quebrado para produzir um piloto visualmente impressionante.
- Não use datas exatas para esconder incerteza; use horizontes e condições.
- Não apresente evidência parcial como fato consolidado; preserve a proveniência.
- Mantenha esta skill cliente-agnóstica: use placeholders e descubra ferramentas, restrições e jurisdição no contexto real.

## Neutralidade de cliente

Ao adaptar esta skill ou qualquer saída produzida por ela, não copie nem transforme em regra permanente informações de um caso concreto, incluindo:

- nome da organização, pessoas, produtos, marcas, unidades, mercados ou vertical;
- processos, métricas, volumes, preços, metas, contratos, decisões ou evidências locais;
- sistemas, fornecedores, URLs, caminhos de arquivo, IDs, credenciais ou nomes de canais;
- jurisdição, política interna, arquitetura ou requisito regulatório que não tenha sido informado para o novo contexto.

Use `[ORGANIZAÇÃO]`, `[ÁREA]`, `[PROCESSO]`, `[SISTEMA]`, `[MÉTRICA]` e `[OWNER]` em exemplos. Separe método reutilizável de evidência do caso: evidência local pertence ao relatório do cliente, não ao `SKILL.md`, às referências ou aos testes desta skill. Antes de entregar uma revisão, faça uma busca literal por nomes próprios, caminhos, identificadores e termos proibidos fornecidos pelo contexto.

## Referências

- Para fundamentos, seleção de framework, scorecard de IA, governança e leitura de evidência: `references/frameworks-e-criterios.md`.
- Para o formato de decisão, roadmap, piloto, métricas e ledger: `references/modelo-de-saida.md`.

---
name: sistemas-agenticos-llm-routing
description: "Use ao desenhar, avaliar ou operar roteamento entre modelos de linguagem e provedores: seleção por requisição, cascatas, roteamento semântico, orçamento de raciocínio, afinidade de sessão, fallback, custo, latência ou qualidade. Também use ao comparar um roteador com um modelo fixo ou investigar concentração de rotas, deriva e escalada indevida."
---

# Roteamento de modelos de linguagem

## Objetivo

Ajude a decidir se uma aplicação deve rotear cada requisição entre modelos, provedores, prompts ou orçamentos de inferência e, se sim, qual política satisfaz os requisitos com o menor risco e custo total. Trate roteamento como uma política de seleção condicionada ao pedido e ao estado relevante, não como um ranking universal de modelos.

Use a política mais simples que demonstre benefício líquido no workload real. Um roteador só acrescenta valor quando candidatos elegíveis têm desempenho complementar e o ganho medido supera o custo e a complexidade do próprio roteamento.

## Quando usar

- Ao escolher entre um modelo fixo, regras, roteamento preditivo, cascata ou despacho em várias etapas.
- Ao rever o uso de custo, latência, qualidade, orçamento de raciocínio, cache ou afinidade de sessão.
- Ao desenhar uma avaliação de roteadores ou comparar roteamento com modelos fixos.
- Ao investigar concentração em um candidato, escaladas frequentes, regressões de qualidade, custo inesperado ou deriva.
- Ao examinar gateways, bibliotecas ou serviços de roteamento e mapear suas capacidades para um workload concreto.

Não presuma acesso a terminal, navegador, código, telemetria ou documentação atual. Use apenas os recursos presentes no runtime; identifique o que precisa ser medido ou verificado por outra pessoa.

## Fluxo de trabalho

1. **Defina o workload e os limites.** Descreva a tarefa, a unidade de sucesso, a população, volume, modalidades, idiomas, riscos e padrões de tráfego. Registe requisitos obrigatórios separados dos objetivos negociáveis. Consulte references/routing-fundamentals.md.
2. **Inventarie candidatos com evidência.** Para cada candidato, registe identificador e versão exatos, modalidades, limites relevantes, tratamento e localização de dados, preço, latência observada e capacidades exigidas. Anote a fonte, a configuração e a data de verificação. Não complete lacunas com suposições.
3. **Teste se há complementaridade.** Compare os candidatos nas mesmas tarefas e condições. Determine se algum candidato de menor custo satisfaz os requisitos em segmentos onde os demais são excessivos ou se algum candidato especializado resolve falhas dos restantes. Inclua o custo do roteador, verificadores, chamadas repetidas, cache perdido e infraestrutura.
4. **Fixe a referência.** Escolha em validação o melhor modelo único ou política estática para os requisitos. Mantenha o conjunto de teste separado até a comparação final. Não use apenas o modelo mais caro, o mais barato ou um resultado de benchmark público como referência.
5. **Aplique elegibilidade antes da pontuação.** Filtre candidatos por política determinística: autorização, privacidade, residência de dados, modalidade, formato, risco, orçamento e disponibilidade. A decisão probabilística só pode escolher entre candidatos elegíveis. Se a política não puder ser aplicada ou a lista ficar vazia, siga um fallback explícito e seguro.
6. **Escolha o momento e mecanismo mínimos.** Decida se a seleção ocorrerá antes da geração, depois de inspecionar uma resposta, durante a geração ou ao longo de uma trajetória multi-turno. Use a referência methods-and-decision.md para comparar sinais observáveis, latência, custo e modos de falha.
7. **Calibre a decisão e o fallback.** Use dados representativos para calibrar limiares, confiança, verificadores e abstenção. Não trate uma confiança declarada pelo modelo, saída tipada ou JSON válido como prova de correção. Valide separadamente a semântica e qualquer condição que possa causar dano.
8. **Avalie o resultado completo.** Compare com a referência no mesmo workload, configuração, janela e política de cache. Meça qualidade e sucesso da tarefa, custo por tarefa concluída, latência de cauda, escaladas, retentativas, falhas, violações de política e desempenho por segmento. Use references/evaluation-and-operations.md e assets/evaluation-plan-template.md.
9. **Prepare a operação.** Defina tetos por pedido e sessão, número máximo de escaladas, comportamento de timeout, fallback, telemetria mínima, responsável pela política e gatilhos de pausa ou reversão. Aplique references/security-and-policy.md. Faça uma implantação gradual apenas quando a política de dados e os controles permitirem.
10. **Registe a decisão.** Entregue o objetivo, limites duros, candidatos e evidências, referência estática, método, custos incluídos, resultado medido, riscos, fallback, plano de validação e lacunas ainda abertas. Use assets/routing-policy-template.yaml para estruturar a configuração.

## Regras de decisão

- Trate segurança, autorização, residência de dados, privacidade e tetos de gasto como restrições duras. Não os compense com uma pontuação de qualidade ou economia.
- Prefira limites explícitos, como qualidade mínima, custo máximo e latência p95 máxima, quando pesos entre objetivos não foram aprovados.
- Se usar uma função de utilidade ponderada, documente unidades, normalização, origem dos pesos e sensibilidade da decisão a esses pesos.
- Inclua todos os custos incrementais. Uma chamada barata não representa economia se exigir validação cara, nova tentativa, escalada ou recomputação de contexto.
- Se não houver rótulos confiáveis, métricas úteis ou complementaridade demonstrada, não treine um roteador aprendido com rótulos improvisados. Recolha evidência, mantenha uma política simples e declare a incerteza.
- Não declare um vencedor universal entre métodos, modelos, provedores ou gateways. A escolha depende dos requisitos, das versões e do workload.

## Referências da skill

- Fundamentos, formulação do objetivo e condições para rotear: references/routing-fundamentals.md.
- Métodos por momento de decisão: references/methods-and-decision.md.
- Desenho de avaliação e operação: references/evaluation-and-operations.md.
- Restrições, segurança, falhas e abuso de custo: references/security-and-policy.md.
- Evidência, alegações de fornecedor e manutenção de informação atual: references/evidence-and-currentness.md.
- Perfil de política e plano de avaliação preenchíveis: pasta assets/.

## Entrega recomendada

Apresente a decisão neste formato:

1. **Workload e sucesso:** tarefa, população e unidade concluída.
2. **Restrições duras:** política, dados, risco, orçamento e SLO.
3. **Referência:** candidato ou política estática e como foi escolhido.
4. **Política proposta:** ponto de decisão, método, sinais e conjunto elegível.
5. **Evidência:** versão, fonte, amostra, período, métricas e incerteza.
6. **Economia líquida e qualidade:** inclui overhead e custo por tarefa concluída.
7. **Falhas e controles:** limites, fallback, monitoramento e reversão.
8. **Lacunas:** dados ou verificações necessários antes de automatizar.

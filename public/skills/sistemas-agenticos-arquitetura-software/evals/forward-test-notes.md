# Observações da execução com a skill

## Contexto

- **Data:** 2026-11-20
- **Execução inicial:** um agente independente respondeu aos quatro cenários de `evals.json` com a skill e as referências relevantes.
- **Revisão:** após uma lacuna observada no cenário de compras, foi reforçado no formato de entrega o requisito de explicitar limites, término, custo e falhas em fluxos agênticos; um segundo agente independente respondeu ao cenário novamente.
- **Limite:** revisão qualitativa de exemplos; não é benchmark estatístico nem garantia de comportamento em todos os runtimes.

## Resultado observado

- **Topologia:** a resposta comparou monólito modular e serviços, relacionou a recomendação às fronteiras, disponibilidade, latência e operação e tratou o esforço prévio como custo incorrido. Incluiu medições e condições para rever a escolha, sem converter o tamanho da equipa num limiar universal.
- **Compras com agente:** as respostas separaram identidade, recuperação, proposta, regras, aprovação e envio; negaram autoridade de execução ao modelo; aplicaram ACL antes da recuperação; e consideraram conteúdo hostil, auditoria, idempotência e falha de envio. A primeira resposta não tornou limites de execução e custo suficientemente explícitos. Após o reforço, a nova resposta incluiu limites de passos, tempo, contexto e custo, condição de término, falhas seguras e reconciliação antes de repetir um envio incerto.
- **Recuperação:** a resposta comparou contexto longo, recuperação e híbrido; recomendou avaliar tarefas e permissões representativas, incluindo frescura, citações, custo, latência e acesso indevido. A recomendação foi condicionada às características do cenário.
- **Auditoria:** a resposta distinguiu corretamente histórico de alterações, CQRS e event sourcing e manteve a solução proporcional ao requisito de desfazer alterações.

## Conclusão de avaliação

Os cenários exercitaram a orientação central da skill: justificar arquitetura por requisitos e evidência, explicitar trade-offs e aplicar controlos fora do modelo quando existem efeitos relevantes. A atualização posterior melhorou a cobertura observada para limites e falhas em fluxos de agente. Volte a executar os cenários quando a skill ou os seus requisitos mudarem; não extrapole uma amostra pequena para uma taxa geral de conformidade.


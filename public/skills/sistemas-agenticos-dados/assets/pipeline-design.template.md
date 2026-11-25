# Desenho de Pipeline

> Preencha campos confirmados; identifique explicitamente hipóteses e decisões por validar.

## Objectivo e Requisitos

- **Resultado/consumidor:** [decisão, aplicação, dashboard, modelo ou agente]
- **Fontes de autoridade:** [sistemas e owners]
- **SLO de dados:** [frescura, completude, disponibilidade e janela]
- **Escala/custo:** [volume actual, crescimento, pico, retenção, orçamento]
- **Restrições:** [privacidade, residência, acesso, tecnologia, competências]

## Fluxo

| Etapa | Entrada e grão | Transformação/contrato | Destino e owner | Evidência/controlo |
|---|---|---|---|---|
| [origem] | [tipo] | [regra] | [destino] | [validação] |
| [ingestão] | [tipo] | [batch/stream/CDC] | [destino] | [offset/contagem] |
| [modelo] | [tipo] | [semântica] | [consumidor] | [teste/linhagem] |

## Semântica Temporal e Idempotência

- **Chave de deduplicação:** [chave e janela]
- **Tempo do evento vs. ingestão:** [regra]
- **Atrasos e fora de ordem:** [watermark/janela/acção]
- **Deletes e correcções:** [semântica]
- **Retry, replay e backfill:** [idempotência, cursor, limites]
- **Evolução de schema:** [compatibilidade e migração]

## Segurança e Qualidade

- **Classificação/minimização:** [dados necessários e tratamento]
- **Acesso:** [identidade, escopo, grants/policies, revogação]
- **Verificações:** [regra, população, limite, severidade, owner]
- **Proveniência e logging:** [metadados registados; campos excluídos]
- **Eliminação/retenção:** [prazo, dependências e evidência]

## Operação e Recuperação

- **Orquestração/observabilidade:** [runs, métricas, alertas]
- **Falhas cobertas:** [fonte indisponível, dados inválidos, quota, etc.]
- **Reconciliação:** [comparação de entrada, destino e consumidores]
- **Migração/rollout/rollback:** [etapas e condição de paragem]
- **Custo observado ou estimado:** [componentes, período, incerteza]

## Decisões e Pendências

| Decisão | Alternativas | Evidência/trade-off | Owner | Condição para rever |
|---|---|---|---|---|
| [decisão] | [opções] | [evidência] | [função] | [sinal] |

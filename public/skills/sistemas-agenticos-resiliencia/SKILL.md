---
name: sistemas-agenticos-resiliencia
description: "Framework para decidir como sistemas com agentes de IA permanecem úteis diante de falhas, sobrecarga e integrações distribuídas. Use quando o pedido envolver SLO, SLI, error budget, alerta, timeout, retry, backoff, jitter, idempotência, webhook, fila, circuito aberto, degradação, outbox, DLQ, incidente ou teste de contrato. Cobre critérios e trade-offs; não substitui a configuração ou a operação do ambiente real."
---

# Resiliência Operacional e Integrações Confiáveis

## Quando usar

- Definir um objetivo de confiabilidade, alerta acionável ou orçamento de erro.
- Decidir se uma chamada remota pode receber timeout, retry, backoff ou falhar rapidamente.
- Projetar uma operação mutável que possa ser repetida sem duplicar efeitos.
- Integrar APIs, webhooks, filas ou eventos sob entrega duplicada, atraso e falha parcial.
- Limitar blast radius com isolamento, circuit breaking, rate limiting, load shedding ou degradação deliberada.
- Estruturar resposta e aprendizado após incidente.

## Quando não usar

- Para autorizar uma ação, gerir identidade ou conter prompt injection: use `sistemas-agenticos-seguranca`.
- Para instrumentar traces e métricas de execução: use `sistemas-agenticos-observabilidade`.
- Para decidir o modelo, cache ou compactação de contexto: use `sistemas-agenticos-eficiencia`.

## Modelo mental

Confiabilidade é uma decisão econômica e de produto, não uma promessa abstrata de disponibilidade total. Toda defesa deve responder quatro perguntas: qual resultado ao usuário protege, qual falha admite, qual efeito colateral pode repetir e como provará que funcionou. Prefira falhas contidas e observáveis a recuperações automáticas que aumentem carga ou corrompam estado.

## Mapa da taxonomia

| Tema | Referência |
|---|---|
| SLOs, error budgets e alertas | `references/slo-error-budget-and-alerting.md` |
| Timeouts, retries e idempotência | `references/timeouts-retries-and-idempotency.md` |
| Isolamento, circuit breaking e degradação | `references/failure-isolation-and-degradation.md` |
| Eventos, outbox e DLQ | `references/event-delivery-outbox-and-dlq.md` |
| APIs, webhooks e contratos | `references/integration-contracts-and-webhooks.md` |
| Incidentes e postmortems | `references/incident-response-and-postmortems.md` |
| Orçamentos de loop e escalonamento | `references/loop-budgets-and-human-escalation.md` |

## Como usar esta skill

1. Identifique o efeito que não pode se repetir e o resultado mínimo que continua útil.
2. Leia a referência de operação síncrona, assíncrona ou de capacidade correspondente.
3. Registre a política: classificação de falha, limite de tentativa, dono do retry, idempotency key, observabilidade e caminho de recuperação.
4. Teste a política sob indisponibilidade, duplicidade, atraso e sobrecarga antes de depender dela em produção.

## Anti-padrões

| Anti-padrão | Risco | Referência |
|---|---|---|
| Retry em todas as camadas | Amplifica uma falha transitória em cascata | `references/timeouts-retries-and-idempotency.md` |
| Dual write | Estado e evento divergem após uma interrupção | `references/event-delivery-outbox-and-dlq.md` |
| Fallback não exercitado | Caminho de recuperação falha no primeiro incidente | `references/failure-isolation-and-degradation.md` |
| Alerta sem ação | Fadiga e perda de sinal operacional | `references/slo-error-budget-and-alerting.md` |
| Webhook tratado como entrega única | Efeitos duplicados ou trabalho perdido | `references/integration-contracts-and-webhooks.md` |

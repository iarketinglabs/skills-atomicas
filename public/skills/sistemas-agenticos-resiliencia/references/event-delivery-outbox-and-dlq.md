# Entrega de Eventos, Outbox e DLQ

Entrega assíncrona normalmente é pelo menos uma vez. Portanto, consumidores precisam ser idempotentes, e ordenação precisa ser um requisito explícito, não uma suposição.

Quando uma mudança de estado e a publicação de evento precisam ser logicamente indivisíveis, grave ambas na mesma transação local e publique depois por um relay: é o transactional outbox. Não prometa exactly-once sem identificar o mecanismo de deduplicação, atomicidade e reconciliação.

Uma DLQ é uma fila de trabalho visível, não uma lixeira. Defina retenção, owner, critérios de replay, limite de tentativas e procedimento para mensagens tóxicas.

## Fontes primárias

- [Microsoft: Transactional Outbox](https://learn.microsoft.com/en-sg/azure/architecture/databases/guide/transactional-outbox-cosmos)
- [Microsoft: Choreography pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/choreography)

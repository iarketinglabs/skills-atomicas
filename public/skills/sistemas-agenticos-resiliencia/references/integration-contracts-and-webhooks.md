# APIs, Webhooks e Contratos

Uma integração remota pode atrasar, duplicar, reordenar ou perder confirmação. Contratos devem declarar autenticação, versão, timeout, idempotência, limites, esquema de erro e política de compatibilidade.

- Responda rapidamente a webhooks e desacople trabalho pesado quando o protocolo permitir.
- Valide autenticidade antes de processar payloads e preserve o identificador de entrega para deduplicação.
- Use testes de contrato para expectativas críticas entre consumidor e provedor; reserve E2E para fluxos de alto valor que atravessam fronteiras reais.
- Evolua contratos com expansão compatível, migração de consumidores e contração posterior; comunique deprecação antes da remoção.

## Fontes primárias

- [Stripe: Webhooks](https://docs.stripe.com/webhooks)
- [Martin Fowler: Testing Strategies in a Microservice Architecture](https://martinfowler.com/articles/microservice-testing/)
- [IETF RFC 8594: Sunset HTTP Header](https://datatracker.ietf.org/doc/html/rfc8594)

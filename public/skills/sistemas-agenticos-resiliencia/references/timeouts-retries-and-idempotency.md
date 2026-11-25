# Timeouts, Retries e Idempotência

Timeout limita espera; retry trata falha transitória; idempotência protege o efeito. Não são sinônimos e não devem ser habilitados como padrão cego.

## Matriz de decisão

| Situação | Decisão preferida | Evitar |
|---|---|---|
| Erro de validação ou permissão | Falhar rapidamente e devolver causa | Retry automático |
| Falha transitória em leitura ou operação idempotente | Retry limitado com backoff e jitter | Repetição concorrente ilimitada |
| Mutação com identificador de intenção | Persistir e reutilizar uma idempotency key | Inferir duplicidade somente pelo payload |
| Efeito irreversível sem deduplicação | Exigir reconciliação ou aprovação | Presumir que timeout significa ausência de efeito |

Defina uma única camada responsável pelo retry. O orçamento end-to-end deve comportar timeout, tentativas e uma resposta útil ao chamador. Se uma tentativa pode ter produzido efeito, a resposta de repetição deve permitir reconciliação auditável.

## Fontes primárias

- [AWS: Timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/)
- [AWS: Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/)

# Isolamento de Falhas e Degradação

Circuit breaker interrompe chamadas a uma dependência persistentemente falha; bulkhead isola recursos; rate limiting e load shedding admitem somente trabalho que o sistema consegue atender. Escolha o mecanismo pelo modo de falha, não pela popularidade do padrão.

## Trade-offs

- Bulkheads preservam partes do serviço, mas podem reduzir a utilização média e aumentar operação.
- Degradação só é válida quando o resultado reduzido permanece semanticamente honesto para o usuário.
- Fallback precisa de teste e observabilidade frequentes. Se só existe em diagramas, não é uma defesa confiável.
- Circuit breaker exige sinais de abertura e recovery probes; sem isso pode mascarar recuperação ou ampliar indisponibilidade.

## Fontes primárias

- [Google SRE: Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/)
- [Microsoft: Bulkhead pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead)
- [Microsoft: Circuit Breaker pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker)

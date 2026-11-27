# Execução durável e recuperação

Uma aceitação de trigger só é útil se o trabalho sobreviver às falhas esperadas e se for possível saber o que pode ser repetido.

## Registo durável e execução

Defina estados de trabalho e transições observáveis, por exemplo: recebido, validado, rejeitado, aceite, pendente, em execução, concluído, omitido, cancelado e falhado. Guarde chave, versão da regra, janela/cursor, tentativa, timestamps e resultado necessário para retomar. Evite guardar mais payload sensível que o requisito permite.

Escolha execução em linha, fila ou motor durável conforme o tempo de execução, esperas externas/humanas, necessidade de pausa/retoma, volume, diagnóstico e recuperação. Confirme limites e garantias da versão/configuração. Persistência de estado de workflow não torna automaticamente idempotentes os efeitos externos.

## Falhas e retentativas

- Classifique erros transitórios, permanentes, de política e resultado incerto. Não retente erro de validação ou autorização sem mudança de condição.
- Use timeout explícito por chamada e por execução. Retente operações transitórias apenas se a repetição for segura, com backoff limitado e jitter; respeite instruções do protocolo quando existirem.
- Antes de repetir um efeito externo após timeout, determine se a origem concluiu a ação, use API de consulta ou chave de idempotência do destino quando suportada, ou suspenda para reconciliação humana.
- Evite retries em cascata e concorrência ilimitada; aplique limites, backpressure e pausa da dependência quando necessário.
- Defina limite e retenção de tentativas, DLQ/quarentena, alarme, responsável e procedimento. A fila de falhas sem triagem e resolução não é uma estratégia de recuperação.

## Replay, backfill e compensação

Antes de replay, determine se a ação já ocorreu, se continua autorizada, se o estado de destino mudou e se o código/contrato atual é compatível com o evento antigo. Preserve motivo, lote, escopo e identidade do replay. Reuse a mesma chave de deduplicação de negócio; não crie uma chave nova só para contornar duplicidade.

Para efeitos irreversíveis ou externos, prefira reconciliação de estado, operação compensatória aprovada ou replay em modo de simulação antes de nova execução. Compensação não apaga o efeito original; documente a consequência e auditoria.

## Fontes de referência

- [AWS Builders' Library: timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — princípios operacionais; os parâmetros continuam dependentes do serviço.
- [Transactional Outbox](https://microservices.io/patterns/data/transactional-outbox.html) — consistência de publicação local e possíveis duplicados do relay.
- [Temporal: durable execution](https://docs.temporal.io/durable-execution) — exemplo de documentação de execução durável; confirme recursos e limites da versão em uso.

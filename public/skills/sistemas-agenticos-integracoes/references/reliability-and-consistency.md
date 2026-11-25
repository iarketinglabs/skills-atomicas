# Fiabilidade e consistência

Desenhe a fiabilidade a partir do efeito de negócio. Uma entrega de transporte pode ser repetida, atrasada, perdida ou confirmada antes de o resultado final ser conhecido.

## Idempotência e resultado incerto

- Identifique a ação que não pode duplicar, a identidade de negócio que a torna única e o período de deduplicação necessário.
- Guarde a chave de idempotência com o estado/resultado necessário para responder a uma repetição de modo consistente. Defina escopo, retenção e conflito entre a mesma chave e payloads diferentes.
- Use identificadores de evento/ação estáveis. Deduplique no sistema que tem autoridade para o efeito, não apenas numa fila volátil.
- Se um timeout ocorrer depois de enviar um comando, não conclua que falhou. Consulte o estado, concilie ou apresente a incerteza antes de reenviar uma operação com efeito externo.
- Não prometa "exactly once" de ponta a ponta apenas porque uma fila, broker ou consumidor possui uma configuração com esse nome. Explique o limite transacional real.

## Timeouts e retries

- Defina prazo total e timeouts por etapa; propague o tempo restante em chamadas encadeadas.
- Retente apenas falhas plausivelmente transitórias. Não retente erros permanentes, validações rejeitadas ou pedidos cujo efeito possa duplicar sem idempotência/reconciliação.
- Limite tentativas e duração total; use espera crescente com jitter quando adequado, respeite instruções de atraso do destino e aplique quota global para não amplificar uma falha.
- Distinga retry do emissor, retry da fila e retry do consumidor para evitar multiplicar tentativas.
- Use circuit breaker, concorrência limitada ou bulkhead quando isolamento de falha realmente proteger recursos partilhados. Defina como recuperar e evitar bloquear permanentemente tráfego saudável.

## Mensagens, eventos e sincronização

- Declare a garantia de entrega e confirme que consumidores aceitam duplicação conforme essa garantia.
- Especifique a chave e o âmbito de ordenação; ordenação global é rara e pode limitar paralelismo.
- Considere atrasos, eventos fora de ordem, correções, tombstones/eliminação, replay e alteração de schema.
- Encaminhe falhas permanentes para um fluxo inspecionável com motivo seguro e procedimento de correção/redrive; uma dead-letter queue sem responsável não é recuperação.
- Para polling/CDC, guarde cursor/checkpoint durável, trate paginação e cursores expirados, e verifique total ou parcialmente a origem para detetar desvios.
- Para webhook, verifique autenticidade antes do processamento, responda segundo o contrato do emissor e processe fora do ciclo HTTP quando a ação demorar.

## Transações distribuídas

- Uma **outbox** pode tornar atómica a gravação local e a intenção de publicar; o relay pode publicar repetidamente, portanto o consumidor ainda precisa de deduplicação.
- Uma **inbox** pode guardar identificadores de mensagens processadas junto da atualização local, segundo a transação possível nessa fronteira.
- Uma **Saga** coordena etapas locais de uma tarefa longa. Compensação não é rollback perfeito: pode falhar, ser tardia ou requerer ação humana. Persista progresso e defina estados intermédios e recuperação.
- Inclua reconciliação entre estado de origem e destino sempre que efeitos incertos, retenção limitada ou intervenção manual possam criar divergência.

## Degradação segura

Decida quando continuar com dados em cache, adiar trabalho, rejeitar tráfego, reduzir funcionalidade ou parar. Use dados antigos apenas quando a decisão de negócio permite e indique a frescura. Não esconda uma falha material como sucesso vazio. Defina quando retomar, quem verifica e como recuperar sem efeitos duplicados.

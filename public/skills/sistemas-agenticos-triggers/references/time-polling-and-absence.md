# Agendamento, polling e ausência

Triggers temporais e de polling precisam de uma posição durável. Uma execução que não ocorreu não deve desaparecer sem deixar estado observável.

## Calendário e janelas

Registe o instante ou calendário, fuso IANA quando o negócio define hora local, precisão, janela lógica e tolerância a atraso. Decida explicitamente:

- o que acontece com hora local inexistente ou repetida na mudança de horário de verão;
- se uma execução perdida é ignorada, reposta, agregada numa só ou processada por cada janela em falta;
- se duas janelas podem sobrepor-se e se execuções são serializadas por recurso;
- como uma execução manual/backfill identifica a janela histórica;
- como são tratados feriados, calendários e mudanças de regra de fuso horário.

Guarde uma chave de execução derivada de `job + janela lógica + âmbito`. Uma repetição do mesmo instante lógico deve produzir a mesma chave. Se a execução não puder ser idempotente, defina exclusão mútua, reconciliação ou aprovação antes do efeito.

Uma expressão cron não define sozinha a política de recuperação, concorrência, fuso ou idempotência. Confirme a semântica do scheduler ativo, incluindo `misfire`, catch-up, suspensão, limites e precisão.

## Polling incremental

- Prefira cursor opaco estável se a API o fornecer; persista-o com o último lote confirmado.
- Se só houver timestamp, estabeleça uma sobreposição temporal para absorver atraso e consistência eventual, use limite inclusivo se compatível, e elimine duplicados por ID. Confirme ordenação, paginação e semântica `updated_since` diretamente com a origem.
- Avance o cursor apenas depois de processar/persistir o lote de forma durável. Um cursor avançado antes de confirmar o trabalho pode perder registos; um cursor atrasado pode repetir trabalho.
- Defina snapshot inicial, estratégia de backfill, marcadores de exclusão/tombstone e verificação de completude. `updated_at` pode não representar deletes nem todas as transições.
- Monitorize saúde do poller, última leitura bem-sucedida, atraso do cursor, páginas pendentes, rate limit e ausência de progresso.

Não calcule uma cadência pelo volume total sem considerar cardinalidade, custo da chamada, paginação, quota, consistência, custo de transformação e latência aceitável.

## Detetar ausência

Uma ausência é uma afirmação temporal: “para esta entidade, era esperado um sinal sob estas condições antes deste prazo, mas não foi observado”. Defina:

1. entidade/fonte que devia emitir e evento esperado;
2. janela ou deadline a partir do tempo correto (ocorrência, receção ou início de negócio);
3. período de tolerância para atraso, jitter, pausas e indisponibilidade;
4. cancelamento quando a expectativa já não se aplica;
5. estado de disparo/alarme para que o mesmo silêncio não gere uma tempestade;
6. verificação de estado e caminho de recuperação antes de agir.

Um heartbeat expirado pode indicar falha de monitor, rede ou emissor; não prova isoladamente que o evento de negócio falhou. Apresente a inferência e a evidência que a sustenta.

## Fontes

- [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339) para intercâmbio de timestamps.
- [Base de fusos horários IANA](https://www.iana.org/time-zones) para regras de hora civil.
- [Kubernetes CronJob](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/) como exemplo de documentação específica de runtime; consulte a versão ativa antes de assumir políticas.

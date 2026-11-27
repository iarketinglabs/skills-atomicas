# Contratos de eventos e entrega

Um trigger é uma fronteira de contrato. O evento deve explicar o que aconteceu e permitir que consumidores decidam se devem agir, sem transformar um texto recebido em autorização.

## Defina o contrato

Registe, conforme aplicável:

- identificador estável e único no seu âmbito; origem e tipo do evento;
- versão do contrato e regra de compatibilidade;
- entidade afetada e referência à fonte de verdade;
- tempo de ocorrência e, quando útil, tempo de emissão/observação;
- conteúdo, codificação, tamanho máximo e campos sensíveis;
- identificadores de correlação e causalidade;
- validação, rejeição, confirmação, retenção e regra para campos desconhecidos.

Distinga **evento** (algo que já ocorreu), **comando** (pedido para fazer algo) e **consulta** (pedido de estado). Não dê a um evento uma semântica de comando só porque o consumidor reage a ele.

CloudEvents é uma opção de formato comum para contexto de eventos; use-o quando melhorar interoperabilidade e mapeie os atributos às semânticas da organização. Não presuma que toda a origem ou runtime o implementa. Veja [CloudEvents](https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md) e o envelope ilustrativo em [assets/event-envelope.example.json](../assets/event-envelope.example.json).

## Garantias e confirmação

Não generalize a semântica de todos os componentes. Documente por fronteira: possibilidade de perda, repetição, ordem, prazo de retentativas, retenção, condição de confirmação e como recuperar uma lacuna. Um SDK, fila ou plataforma pode dar garantias distintas por configuração, versão, origem e consumidor.

Na receção assíncrona, confirme depois de autenticar, validar e gravar de forma durável o evento ou trabalho aceite. Se não houver armazenamento durável, não prometa que um `2xx` significa processamento concluído. Para trabalhos síncronos, alinhe a resposta com a operação que realmente terminou. Consulte a política da origem para retries e timeout: não invente uma janela fixa.

## Duplicados, idempotência e atomicidade

- Defina deduplicação por identidade do evento no âmbito correto, normalmente uma combinação de origem e ID estável.
- Defina idempotência de negócio separadamente: dois eventos diferentes podem pedir o mesmo efeito; um único evento pode precisar de efeitos distintos por destino.
- Persista a chave e o resultado do efeito na mesma fronteira transacional possível. Antes de repetir uma chamada externa cujo resultado ficou incerto, consulte o estado ou use uma chave de idempotência do destino, se suportada.
- Para job temporal, derive uma chave da identidade do job e da janela lógica, não apenas da hora em que um worker começou.
- TTL de deduplicação deve cobrir a janela real de repetição/replay e os requisitos de negócio; não o escolha por conveniência sem documentar a retenção da origem.

Uma garantia “exactly once” numa camada de transporte não prova um único efeito através de banco de dados, filas, modelo e serviços externos. Analise commits, retries, timeouts e efeitos em cada limite.

## Publicação consistente

Se uma alteração local e a publicação de um evento têm de concordar, avalie um **transactional outbox**: grave a alteração e a intenção de publicação na mesma transação; um relay separado publica depois. O relay pode publicar de novo se falhar antes de registar a publicação, pelo que consumidores continuam a precisar de idempotência. Um padrão inbox pode persistir a aceitação e a deduplicação no consumidor.

CDC lê alterações do log da base. Diferencie CDC de tabelas de estado (que pode expor detalhes físicos e exigir estratégia para deletes) de CDC de uma outbox com semântica de domínio. Defina snapshot inicial, posição do log, retenção, evolução e recuperação do conector.

## Ordem, atraso e evolução

- Defina se a ordem global é necessária ou se basta por entidade/agregado. Ordenação por partição, fila ou sequência não é necessariamente global.
- Use versão/sequence por entidade ou compare com estado atual quando eventos podem chegar fora de ordem.
- Decida o que fazer com evento tardio, estado obsoleto, schema desconhecido e evento malformado: rejeitar, colocar em quarentena, adaptar ou escalar.
- Preserve payload original apenas se necessário, com controlo de acesso e retenção; minimize dados em logs e traces.
- Documente compatibilidade e rollout de produtores/consumidores. Um schema válido não prova semântica compatível.

## Referências

- [CloudEvents specification](https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md)
- [Transactional Outbox](https://microservices.io/patterns/data/transactional-outbox.html)
- [AWS Builders' Library: making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) — princípios de idempotência; não implica que o fornecedor de destino implemente a mesma interface.

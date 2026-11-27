# Seleção do padrão de disparo

Escolha pelo requisito que domina o caso e pelos modos de falha que a equipa consegue operar. O rótulo "event-driven" não decide por si só o transporte, a semântica do evento ou o modelo de consistência.

## Padrões

| Padrão | Como detecta | Favorece | Custos e riscos a considerar |
|---|---|---|---|
| Push por evento (webhook, broker ou stream) | A origem publica um evento ou notificação | Baixa latência e pouco trabalho vazio | Receção, autenticação, duplicados, reordenação, retries da origem, exposição de rede e reconciliação |
| Pull/polling | O consumidor consulta uma API ou fila | Controlo do ritmo, rede de saída, backfill e integração com fontes sem push | Atraso, chamadas vazias, rate limits, paginação, cursores perdidos e ausência de execução do poller |
| Agendamento | Um relógio inicia uma execução segundo calendário ou intervalo | Tarefas por período, relatórios, reconciliação e deadlines | Fuso e DST, execuções perdidas, sobreposição, atraso do scheduler e repetição da mesma janela |
| CDC | Um conector lê alterações do log de transações da origem | Captura contínua de alterações confirmadas sem sondar cada entidade | Acoplamento ao esquema físico, retenção/saúde do log, snapshots, exclusões, evolução do schema e carga operacional |
| Consulta contínua/condição | Um motor acompanha predicados sobre estado ou eventos | Limiar, combinações de fontes e condição que persiste | Estado da consulta, semântica temporal, late data, custo contínuo e dependência do motor |
| Híbrido | Combina dois ou mais mecanismos | Baixa latência com verificação de completude, ou estado contínuo com tarefas agendadas | Duplicação entre caminhos, estado/cursor compartilhado e maior complexidade de operação |

## Perguntas de decisão

1. O requisito descreve um facto novo, uma consulta ao estado atual, um calendário, uma transição, ou uma ausência? Se a resposta for “não aconteceu até ao prazo”, modele a expectativa e o prazo explicitamente; não transforme silêncio de um componente numa prova automática de ausência na origem.
2. Qual é o atraso máximo aceitável e como é medido: desde a ocorrência na origem ou desde a observação pelo consumidor?
3. A origem oferece um feed durável, API paginada com cursor ou apenas estado consultável? Que retenção e limites declara para a versão em uso?
4. O consumidor pode receber tráfego de entrada? Que restrições de rede, disponibilidade e autenticação se aplicam?
5. O que acontece se o sinal se perder, chegar repetido, tarde ou fora de ordem? Como se encontra e corrige uma lacuna?
6. A operação iniciada é reversível, idempotente e limitada? Quem atende a fila de falhas e a execução parada?

Se a taxa de mudança é baixa e a tolerância ao atraso é ampla, polling ou agendamento podem ser mais simples. Se a frescura importa e a fonte emite eventos confiáveis, push pode reduzir atraso e leituras vazias. Se a completude ou a recuperação importam, avalie reconciliação por pull no mesmo caminho idempotente. São hipóteses iniciais, não regras universais.

## Estimativa de polling

Para polling periódico com intervalo `T`, duração `D` e mudanças uniformemente distribuídas entre leituras, o atraso médio de deteção aproxima-se de `T/2`, o pior caso aproxima-se de `T`, e as leituras por recurso aproximam-se de `ceil(D/T)`. A estimativa não inclui paginação, retentativas, throttling, jitter, consistência eventual ou custo da origem. Use medidas e limites documentados para dimensionar; não apresente a fórmula como SLO ou garantia.

## Payload magro ou completo

- Uma **notificação magra** transporta identidade, tipo e referência; reduz acoplamento e tamanho, mas depende de a origem conservar e servir o estado consultado. A consulta pode devolver estado posterior ao evento.
- Um **evento com estado** inclui mais dados para o consumidor trabalhar localmente; reduz consultas e pode preservar o estado observado na origem, mas aumenta o tamanho, a exposição de dados e o acoplamento ao schema.
- A escolha depende da semântica exigida: estado do momento do evento ou estado mais recente. Documente a diferença e valide-a em eventos tardios.

## Quando usar combinações

Considere um fluxo híbrido quando a entrega rápida e a completude têm requisitos diferentes: aceitar push rapidamente, persistir o evento e agendar reconciliação por cursor. Ambos os caminhos devem normalizar para o mesmo contrato e partilhar identidade/idempotência. Para um job agendado com uma fonte sem API, registe a janela processada e o mecanismo de backfill. Não acrescente um segundo mecanismo sem um modo de falha concreto que ele resolve.

## Fontes de orientação

- [CloudEvents: especificação de eventos neutra de fornecedor](https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md) — use apenas se a interoperabilidade do envelope for útil.
- [Chris Richardson: padrão Transactional Outbox](https://microservices.io/patterns/data/transactional-outbox.html) — contexto, relay e duplicados do relay.
- Para uma comparação de recursos de produto ou limites, consulte a documentação oficial das versões efetivamente utilizadas; esta matriz descreve famílias de desenho, não capacidades de plataforma.

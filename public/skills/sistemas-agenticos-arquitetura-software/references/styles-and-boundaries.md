# Estilos, fronteiras e contratos

Use esta referência para decompor sistemas, comparar topologias ou rever dependências. Os nomes descrevem famílias de soluções, não níveis de maturidade.

## Comece pela coesão e pelas razões de mudança

Uma decomposição útil esconde decisões com probabilidade de mudar e mantém juntas as regras que mudam em conjunto. Organize fronteiras em torno de capacidades e conceitos de domínio, não apenas de camadas técnicas, equipas atuais ou endpoints.

Um bounded context define onde um modelo e a sua linguagem têm significado consistente. Um limite de módulo pode coincidir com esse contexto sem exigir um serviço, processo ou equipa separados. Identifique quem mantém os dados e as regras de cada fronteira; uma interface sem propriedade clara é uma fronteira fraca.

## Comparar estilos

| Estilo | Pode servir quando | Custos e falhas a considerar |
|---|---|---|
| **Monólito modular** | As partes beneficiam de implantação e transações comuns, mas precisam de limites internos explícitos. | Fronteiras degradam se forem apenas convenção; uma publicação afeta o conjunto. |
| **Serviços distribuídos** | Autonomia de implantação, isolamento, escala ou tecnologia por capacidade tem valor suficiente e existe operação para o suportar. | Rede falha, latência, consistência, descoberta, versionamento, observabilidade e suporte tornam-se parte do desenho. |
| **Camadas** | Separar responsabilidades de apresentação, aplicação, domínio e infraestrutura torna dependências mais claras. | Camadas podem virar encaminhadores sem encapsular decisões; regras de negócio podem ficar espalhadas. |
| **Ports and adapters / arquitetura hexagonal** | O núcleo de regras precisa de permanecer testável e desacoplado de interfaces externas. | Abstrações duplicadas ou portas que apenas reproduzem a API de uma dependência criam cerimónia sem isolamento real. |
| **Microkernel / plugins** | Existe um núcleo estável e extensões substituíveis fazem parte do produto. | O núcleo pode ficar acoplado a plugins ou crescer uma API interna que não protege fronteiras. |
| **Orientado a eventos** | Produtores e consumidores precisam de desacoplamento temporal ou distribuição assíncrona. | Causalidade, ordenação, redelivery, contratos e diagnóstico tornam-se menos diretos. |

Um monólito pode ser modular; vários serviços podem formar um monólito distribuído. Escolha implantação distribuída quando ela compra uma capacidade necessária, não como sinónimo de modularidade.

## Domínio, dados e consistência

- Dê a cada conceito e conjunto de dados um responsável explícito. Evite múltiplos serviços a alterar diretamente as mesmas tabelas sob o rótulo de propriedade distribuída.
- Determine quais as invariantes que precisam de ser garantidas numa única transação e quais podem tolerar atraso ou reconciliação.
- A consistência eventual é uma decisão visível ao produto: estados intermédios, atraso, conflitos e compensações precisam de representação e tratamento.
- Evolua contratos e esquemas com consumidores existentes em mente. Defina compatibilidade, período de transição, versão e estratégia para consumidores atrasados.
- Trate retries e redelivery como parte do comportamento normal em sistemas distribuídos; use idempotência onde repetir uma operação poderia duplicar efeitos.
- Diferencie **evento** (facto que ocorreu) de **comando** (pedido para alguém agir). Mensagens desacoplam tempo, mas não removem dependências semânticas.

## CQRS, event sourcing e integração

- **CQRS** separa caminhos ou modelos de escrita e leitura quando a diferença resolve uma necessidade observada. Não implica microserviços nem event sourcing.
- **Event sourcing** usa uma sequência de eventos como fonte de verdade para reconstruir estado. Um histórico de auditoria pode, em vez disso, registar alterações ao lado de um modelo atual convencional.
- Antes de adotar event sourcing, desenhe evolução de eventos, projeções, replay, correções históricas, privacidade, retenção e tratamento de efeitos externos durante reprocessamento.
- Use uma **transactional outbox** quando uma alteração persistida e a intenção de publicar uma mensagem têm de ser gravadas atomicamente em sistemas separados. Inclua publicação, duplicação, retenção e monitorização no desenho.
- Use uma **saga** quando uma operação de negócio atravessa transações independentes e pode avançar por estados intermédios. Defina compensações; elas não equivalem a rollback global nem garantem isolamento transacional.
- Use filas ou streams quando o desacoplamento assíncrono responde a requisitos de pico, latência, durabilidade ou integração. Defina limites de fila, ordenação, backpressure, poison messages e reconciliação.

Esses padrões são opções locais. Adotar um deles não exige adotar os restantes.

## Escolha de interfaces

Escolha o tipo de interação conforme os participantes e as propriedades desejadas:

- pedido/resposta síncrono para resposta imediata e dependência explícita;
- API HTTP ou RPC tipada quando os participantes precisam de contrato e validação;
- publicação/consumo assíncrono quando a independência temporal tem valor;
- transferência de ficheiros ou lote quando o volume e a cadência justificam processamento diferido.

Especifique autenticação, autorização, timeout, semântica de erro, idempotência, compatibilidade e observabilidade. Escolha uma notação de contrato que a equipa consiga manter; nenhum formato é universal.

## Sinais para separar uma fronteira

Uma extração ou implantação autónoma torna-se mais plausível quando dados demonstram uma ou mais necessidades fortes, como:

- escalabilidade muito diferente que não se resolve adequadamente na unidade atual;
- exigência de isolamento de falha, segurança, jurisdição ou ciclo de vida;
- bloqueios frequentes porque uma capacidade precisa de publicar independentemente;
- equipa responsável por regras e dados coesos, com contrato de integração estável;
- necessidade concreta de tecnologia ou perfil operacional incompatível com o restante sistema.

Antes de separar, confirme propriedade de dados, contrato, observabilidade, capacidade de entrega, suporte e estratégia de migração. Os sinais são critérios para análise, não um limiar universal nem uma lista de requisitos cumulativos.


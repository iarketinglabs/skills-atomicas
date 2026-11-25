# Seleção do padrão de integração

Escolha o mecanismo que cumpre a necessidade de negócio com o menor acoplamento e custo operacional aceitáveis. Comece pela semântica e pela janela de resposta; depois compare protocolos e produtos concretos.

## Perguntas que mudam a escolha

- O consumidor precisa de resposta imediata para continuar a interação ou pode processar mais tarde?
- Qual é a frescura realmente necessária? A janela vem de uma decisão de negócio ou de uma preferência técnica?
- Uma falha do destino deve bloquear a origem? A origem pode guardar trabalho pendente?
- O fluxo representa uma consulta, um comando, um facto ocorrido ou uma cópia de dados?
- É necessária entrega ordenada, fan-out, replay, histórico, consulta seletiva ou transformação?
- Qual sistema é autoridade para cada campo? Como são corrigidos dados já enviados?
- Os participantes conseguem receber chamadas externas, manter uma fila, expor uma API ou operar processamento contínuo?
- Quem opera credenciais, contratos, compatibilidade, filas, alertas e recuperação?

## Opções e compromissos

| Forma | Considere quando | Custos e falhas a avaliar |
|---|---|---|
| Pedido/resposta síncrono, por exemplo HTTP/REST, GraphQL ou RPC | O chamador precisa do resultado na mesma interação e os participantes conseguem cumprir a latência | Acoplamento temporal, timeouts em cascata, dependência de disponibilidade, limites, fan-out e custo de consultas |
| Fila ou fluxo de eventos | É útil desacoplar produtores e consumidores, absorver picos, distribuir factos ou reprocessar trabalho | Duplicação, ordenação, atraso, retenção, crescimento da fila, evolução de schema, replay e operação do broker |
| Webhook | O fornecedor pode notificar o consumidor quando ocorre uma mudança e o consumidor pode receber chamadas | Entrega repetida, endpoint indisponível, autenticação da origem, replay, fila de entrega, reconciliação e exposição da URL |
| Polling | O sistema de origem não oferece eventos, o consumidor não pode receber chamadas, ou uma cadência simples atende à frescura necessária | Latência determinada pelo intervalo, carga vazia, rate limits, paginação e cursores, ausência de mudanças perdidas e estado do último sync |
| Batch, ficheiro ou transferência gerida | O volume pode ser processado em lotes e a janela permite transferências periódicas | Atraso, ficheiros parciais, reenvio, checksums, controlo de acesso, schema, retenção e recuperação do lote |
| CDC ou ELT | É preciso propagar alterações ou disponibilizar dados para análise com frescura conhecida | Semântica do log, retenção, estado do conector, evolução do schema, privacidade, carga na origem e reconciliação |
| CLI ou automação de operador | A tarefa é administrativa, ocasional ou parte de um pipeline controlado | Dependência do ambiente e credenciais, estabilidade da saída, códigos de erro, concorrência e supervisão |
| Interface de ferramenta para IA | Um modelo/agente precisa de capacidades limitadas de leitura ou ação sobre um sistema | Identidade e autorização, descrição e esquema de argumentos, validação independente, injeção, efeitos colaterais, aprovação e rastreabilidade |
| Protocolo agente-a-agente | Agentes independentes precisam de descobrir capacidades ou delegar trabalho através de uma fronteira explícita | Identidade, confiança, prazo e estado da tarefa, opacidade, cancelamento, transferência de dados e responsabilidade pelo resultado |

REST, GraphQL, gRPC, MCP, A2A, AsyncAPI, formatos de eventos e outras opções são meios, não objetivos. Verifique o suporte real de ambos os lados e a especificação oficial atual antes de depender de uma funcionalidade específica.

## Escolha e registo

1. Elimine opções que não satisfazem a janela, a direção, a segurança ou as capacidades dos participantes.
2. Compare as opções restantes em acoplamento, latência, volume/picos, custo total, governança, observabilidade e recuperação.
3. Prefira uma solução direta quando uma camada extra não resolve um requisito demonstrado. Um gateway pode aplicar políticas transversais; não deve esconder semântica de domínio nem ser ponto único sem plano de continuidade.
4. Defina o fallback e o comportamento em degradação. Se não houver fallback seguro, falhe de forma explícita e observável.
5. Registe a condição que levaria a rever a decisão: picos, nova exigência de frescura, novos consumidores, mudança de propriedade, limite de fornecedor ou custo operacional.

## Padrões de arquitetura

- **Orientação a eventos:** publique factos de negócio bem definidos; diferencie-os de comandos que pedem uma ação. Não presuma ordenação global ou entrega única.
- **Composição:** reutilize capacidades quando reduz duplicação sem criar dependências e ownership ambíguos. Um catálogo modular não substitui contratos nem governança.
- **CDC e sincronização:** use CDC se a origem e a semântica de alteração justificarem propagação incremental; use extração periódica se cumprir a janela com menor complexidade. Mantenha checkpoints recuperáveis e um método de comparação/reconciliação.
- **Orquestração e Saga:** use uma máquina de estados durável para processo de negócio longo e distribuído quando transação local não basta. Defina compensações como ações de negócio e considere estados intermediários visíveis.
- **Outbox/inbox:** considere-os para coordenar uma gravação local e a publicação/consumo sem depender de uma transação distribuída entre sistemas. Inclua deduplicação e limpeza com retenção definida.
- **APIOps:** automatize validação, revisão e publicação de contratos/políticas quando o número e o ciclo de vida das APIs justificarem essa governança.

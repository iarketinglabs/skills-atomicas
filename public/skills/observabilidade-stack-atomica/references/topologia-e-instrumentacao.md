# Topologia, sinais e instrumentação

## Selecione por capacidade

| Sinal | Caminho típico | Decisão |
|---|---|---|
| Traces | SDK OpenTelemetry → OTLP → Collector ou destino gerido → Tempo, Jaeger ou outro backend compatível | Defina propagação, limite de atributos e sampling. Valide se spans assíncronos preservam o vínculo esperado. |
| Métricas de aplicação | Exportação OpenTelemetry ou endpoint Prometheus → backend de séries | Escolha push ou scrape por ambiente. Identifique tipo, unidade e conversão, além de janela e identidade de série. |
| Logs | JSON para stdout → agente de logs, ou SDK → OTLP → backend como Loki | Declare origem canônica. Correlacione com trace em campos de contexto. Restrinja rótulos indexados a conjuntos limitados. |
| Exceções | Captura de erros e release no Sentry, quando adotado | Verifique redaction, retenção, mapping de release e envio duplicado de eventos. |
| Visualização | Grafana ou painel do provedor sobre backends configurados | O painel precisa de dados, acesso, queries corretas e fuso definido. Confirme como alertar e roteie para o responsável. |

O OpenTelemetry padroniza instrumentação e transporte. O Collector recebe, processa e exporta sinais, com componentes dependentes da distribuição. Ele precisa de um backend para consultar dados históricos. Uma equipe pequena pode usar ingestão gerida ou um coletor simples. Compare propriedade operacional, recuperação, quotas, custos por volume, residência e retenção antes de escolher.

## Aplicações e integrações

| Ambiente | Primeiro passo | Evidência esperada |
|---|---|---|
| Next.js | Confira a convenção `instrumentation.ts` no projeto e na versão alvo. Use o wrapper ou SDK compatível com o runtime e o destino. Restrinja imports exclusivos de Node à execução em Node. | Aparecem spans de uma rota de teste com serviço, ambiente e filhos esperados. Produção e desenvolvimento são validados separadamente. |
| Python | Inicialize uma vez o SDK e o exportador, auto ou manualmente conforme o framework. Emita contexto nos logs estruturados. Propague em clientes HTTP e mensagens quando ambas as pontas suportarem o protocolo. | Um pedido de teste chega ao worker com a correlação definida. Jobs breves observam o flush e o encerramento dos exportadores. |
| n8n | Confirme se a instalação é Cloud ou self-hosted e qual papel cada processo executa. Verifique separadamente endpoints de saúde, prontidão e métricas. Consulte a opção de métricas para instalação self-hosted. | Colete no alvo correto, confira o estado de um workflow sintético e verifique quais sinais são observáveis para workers. |
| Supabase | Para serviço gerido, use o guia da Metrics API, confirme disponibilidade, método de autenticação e métricas expostas. Em self-hosted, inventarie os componentes e configure a coleta compatível correspondente. | Diferencie a scrape autenticada de métricas de banco dos spans emitidos pela aplicação. Valide onde as métricas representam o banco e onde faltam dados do produto. |

[Next.js OpenTelemetry](https://nextjs.org/docs/app/guides/open-telemetry) · [OpenTelemetry Python](https://opentelemetry.io/docs/languages/python/) · [Monitoramento n8n](https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/monitor-n8n) · [Supabase Metrics API](https://supabase.com/docs/guides/observability/metrics) · [Configuração do Collector](https://opentelemetry.io/docs/collector/configuration/) · [Ingestão OTLP no Loki](https://grafana.com/docs/loki/latest/send-data/otel/)

## Fronteiras e orçamento

- Registre `service.name`, ambiente, versão, operação e resultado em nomes com semântica estável. Confirme a versão das convenções, sobretudo para atributos marcados como experimentais. [Convenções semânticas](https://opentelemetry.io/docs/specs/semconv/)
- Propague o contexto conhecido entre serviços e filas. Em uma fila com vários produtores ou operações agrupadas, defina quando usar vínculo entre spans. Valide a hipótese com o identificador de uma transação sintética. [Contexto W3C](https://www.w3.org/TR/trace-context/)
- Identificadores de pedido, usuário, trace, prompt e URL integral multiplicam cardinalidade ou revelam dados. Mantenha-os fora dos rótulos de série ou indexação. Use correlação com IDs técnicos de retenção limitada, somente quando necessários. Omita corpos e segredos desde a origem.
- Restrinja a recepção e o acesso a backends por rede, identidade, escopo e retenção. Use TLS na transferência remota e credenciais geridas. Teste o fluxo entre tenants quando houver segmentação.
- Limite fila, memória, retentativas e volume do Collector. Dimensione por carga e falha do destino. Se usar amostragem no fim do trace, o processamento precisa receber os spans necessários para decidir. Em produção, confira se a distribuição oferece memory_limiter e coloque-o no início dos processadores da pipeline quando adotado. Ajuste fila e retentativas com base em capacidade medida. Fila cheia, prazo esgotado ou reinício podem descartar dados. Monitore perda, fila e entrega além da saúde do processo.

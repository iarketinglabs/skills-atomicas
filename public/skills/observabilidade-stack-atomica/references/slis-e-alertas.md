# SLIs, painéis e alertas

## Instrumente a experiência

| Jornada | Exemplo de indicador | Armadilha a evitar |
|---|---|---|
| Pedido HTTP elegível | Requisições bem-sucedidas / requisições elegíveis | Defina códigos e exclusões por operação. Um HTTP 200 pode ocultar falha no conteúdo. |
| Prazo de resposta | Proporção dentro do prazo registrado em histograma ou contador | Não some nem calcule a média de p95 individuais. Use buckets e agregação compatíveis. |
| Job de fila | Jobs concluídos no prazo / jobs elegíveis, mais idade do job pendente mais antigo | Contar somente jobs finalizados deixa os que nunca terminam fora do indicador. Defina o que conta como atraso, repetição ou cancelamento. |
| Disponibilidade do sinal | Exportador e scrape recentes, erro ou perda no pipeline e tráfego conhecido | Zero eventos e ausência de dados têm significados diferentes. |

Defina a meta de cada SLO com o responsável e uma janela. O orçamento de erro, como fração, é `1 − SLO`. Se 0,5% é a fração de falhas observada e o orçamento é de 0,1% no mesmo recorte, a taxa de consumo é 5 vezes a nominal. As dimensões de versão e ambiente precisam ter significado equivalente entre consultas.

## Consultas de exemplo

Nomes ilustrativos para uma série com rótulo `service` e histograma clássico. Adapte aos nomes, tipos e unidades observados no backend.

```promql
sum by (service) (rate(http_server_request_duration_seconds_count[5m]))
```

```promql
histogram_quantile(
  0.95,
  sum by (service, le) (
    rate(http_server_request_duration_seconds_bucket[5m])
  )
)
```

Escolha buckets que distingam o limiar do SLO. Para uma meta expressa em proporção dentro do objetivo, use o contador de observações até o limite sobre o total de observações elegíveis. Para tráfego baixo, avalie janelas mais longas, volume mínimo observado ou sondas sintéticas. Mantenha separado o alerta de ausência de telemetria.

## Do painel à ação

1. Em cada tela, mostre janela, unidade, ambiente e versão. Comece por taxa de sucesso, erros, volume e latência. Acrescente profundidade e idade da fila ou saturação se mudarem a resposta ao incidente.
2. Diferencie investigação assíncrona e alerta urgente. Para um SLO com volume suficiente, use janelas curta e longa de consumo de orçamento adequadas à urgência e ao volume.
3. Inclua no alerta impacto esperado, serviço e ambiente, janela, painel, runbook e destino responsável. Limite agrupamento e duplicação. Defina o comportamento sem dados e ante falha da própria notificação.
4. Em teste, gere violação e recuperação sintéticas. Confira estado de disparo, destinatário de teste, legibilidade da mensagem e retorno ao normal. Registre quando só a consulta ou a regra estiver validada.

[Histogramas no Prometheus](https://prometheus.io/docs/practices/histograms/) · [Alertas com base em SLO](https://sre.google/workbook/alerting-on-slos/) · [Alertas Prometheus](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/)

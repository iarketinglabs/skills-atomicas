# Validação por trecho e resposta a incidentes

## Saúde e prontidão

- **Inicialização.** Quando o runtime oferece uma probe de startup, reserve tempo para migrações ou aquecimento controlado antes de avaliar vida. Considere limites para inicializações que ficam travadas.
- **Vida.** Prove que o processo consegue progredir. Uma falha reinicia o processo em alguns orquestradores. Evite transformar uma oscilação temporária de banco ou fila em reinícios de toda a frota.
- **Prontidão.** Indique se deve receber tráfego agora, conforme as dependências realmente críticas. Use timeouts curtos, evite trabalho com efeito colateral e documente cenários degradados que ainda servem.
- **Jornada sintética externa.** Confirme a experiência mínima do usuário com dados de teste e baixa frequência, inclusive roteamento e dependências. O êxito de uma probe interna não prova que isso funciona.
- **Saúde da telemetria.** Monitore rejeição, atraso e perda no coletor/exportador. Um painel vazio exige investigação do sinal e da origem do tráfego.

Conferir a semântica de probes e a compatibilidade do runtime escolhido. [Configuração de probes no Kubernetes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/) · [Monitoramento n8n](https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/monitor-n8n)

## Quando um sinal desaparece

| Trecho | Pergunta verificável | Evidência mínima |
|---|---|---|
| Origem | A versão implantada emite este sinal e há tráfego elegível? | Evento sintético e código/configuração que seleciona o runtime. |
| Transporte | O destino recebe com o protocolo, caminho e autenticação esperados? | Métrica ou log redigido de sucesso/erro, sem divulgar cabeçalhos. |
| Processamento | Um filtro, regra de sampling ou pressão de memória suprimiu o sinal? | Contadores de recebimento, descarte, fila e exportação antes/depois. |
| Armazenamento | O backend aceitou a série, o span ou o log? | Consulta por janela e dimensões que batam com a origem. |
| Consumo | O painel e a regra consultam o índice, tenant, ambiente e intervalo corretos? | Reexecução da consulta e evidência do destino de teste do alerta. |

Em implantação recente, compare a versão atual e a anterior com a mesma intervenção sintética. Se precisar mudar a configuração, aplique primeiro numa parcela controlada, monitore e combine a reversão. Uma mudança de label que quebre a query ou uma exportação duplicada não deve passar para toda a frota.

Use a fixture [Collector local](../assets/collector-local.yaml) com dados sintéticos para isolar recepção e exportação de traces. A fixture usa OTLP HTTP no loopback e exportador `debug`. Confirme se a distribuição instalada inclui ambos. Execute a validação usando `otelcol validate --config=assets/collector-local.yaml` ou o nome do binário instalado, na raiz deste pacote. Emita um span sintético para o receptor e confira a saída local. A fixture exclui persistência e roteamento de alertas. Mantenha-a fora de produção.

[Configuração do Collector](https://opentelemetry.io/docs/collector/configuration/) · [Telemetria interna do Collector](https://opentelemetry.io/docs/collector/internal-telemetry/)

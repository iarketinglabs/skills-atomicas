---
name: observabilidade-stack-atomica
description: Use para planejar, implementar ou diagnosticar a stack de observabilidade de um serviço com OpenTelemetry, Prometheus, Grafana, Loki ou Sentry. Aplica-se a logs estruturados, tracing distribuído, métricas, SLOs, alertas e health checks em aplicações web, workers, n8n e Supabase.
---

# Observabilidade de serviços com a stack Atomica

Mapeie a experiência que o serviço precisa entregar e instrumente o menor percurso capaz de demonstrá-la. Adapte a stack aos componentes que já existem. Esta skill trata de telemetria e operação de serviços. Para medir se um agente tomou boas decisões ou produziu uma resposta correta, consulte `sistemas-agenticos-observabilidade` quando disponível.

## Entradas

Liste jornadas ou jobs críticos, serviços e limites entre eles, ambientes, versões e runtimes, sinais já disponíveis, responsabilidades operacionais e restrições de retenção, volume e sigilo. Se faltarem metas de serviço, proponha indicadores e deixe os alvos para decisão do responsável.

Com acesso de leitura, revise código e configuração. Para instrumentar, implantar ou disparar testes com efeitos, use o ambiente e as permissões que o usuário autorizou. Sem ferramentas de execução, entregue configuração proposta, comandos de validação e verificações pendentes.

## Fluxo

1. **Defina sucesso e falha.** Escolha um SLI por jornada crítica. Documente unidade, numerador, denominador, elegibilidade, janela e como interpretar ausência de sinal. Separe tempo HTTP, tempo de espera na fila e prazo de conclusão do job.
2. **Desenhe o caminho do sinal.** Comece por um serviço e uma transação sintética. Use a [topologia e matriz de instrumentação](references/topologia-e-instrumentacao.md) para decidir como cada sinal chega ao backend. Evite enviar o mesmo contador por scrape e OTLP para o mesmo conjunto de séries.
3. **Instrumente e minimize.** Nomeie serviços e recursos de modo consistente. Correlacione traces e logs com IDs de execução e use atributos de rota normalizada, versão e ambiente quando úteis. Filtre conteúdo sensível antes da exportação. Revise cardinalidade, sampling, retenção e acesso por sinal.
4. **Defina painéis e alertas.** Comece com sucesso, latência, volume e saturação. Vincule a versão do serviço, responsável, runbook e ação possível. Use [SLIs, consultas e alertas](references/slis-e-alertas.md) para justificar limites e tratar baixo volume ou ausência de dados.
5. **Valide de ponta a ponta.** Gere tráfego sintético com sucesso, erro e atraso em ambiente autorizado. Observe coleta, roteamento, consulta, correlação e entrega de notificação de teste. Use o [modelo de aceitação](assets/aceitacao-operacional.md). Registre o que ficou por validar.
6. **Diagnostique sinais ausentes.** Siga a cadeia emissão → transporte → coletor → armazenamento → consulta. Meça perda e fila do coletor. Use contraprovas de tráfego e tempo. Para falha após release, compare com a linha de base e prepare reversão da configuração com o responsável.

## Entrega

Inclua uma tabela sinal → fonte → transporte → backend → retenção, com o motivo de cada escolha e as versões verificadas. Anexe a definição dos SLIs, os painéis e alertas propostos, evidências de aceitação e riscos pendentes. Use o [procedimento de validação e incidentes](references/validacao-e-incidentes.md) para separar processo vivo, pronto, experiência funcional e saúde da própria telemetria.

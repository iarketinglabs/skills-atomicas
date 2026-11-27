---
name: sistemas-agenticos-triggers
description: "Use ao conceber, implementar, rever ou diagnosticar gatilhos que iniciam automações, workflows ou agentes em resposta a eventos, horários, alterações de dados, condições ou ausência de sinais. Ajuda a escolher push/webhooks, polling, CDC, agendamento ou combinações e a definir entrega, deduplicação, segurança, limites, aprovação humana, observabilidade e recuperação. Não use para desenho geral de prompts ou agentes sem um problema de ativação ou início de execução."
metadata:
  short-description: "Desenho e operação de triggers"
---

# Sistemas Agênticos: Triggers

Ajude a escolher e operar o mecanismo que inicia um fluxo de automação ou agente quando ocorre um evento ou uma condição. Aplique a profundidade adequada ao risco. Não pressuponha organização, indústria, fornecedor, stack, runtime, jurisdição ou arquitetura; trate-os como dados do contexto quando forem relevantes.

Use esta skill quando uma execução começa por um sinal externo, uma alteração de estado, um horário, uma condição persistente ou a ausência de um sinal esperado. Inclui fluxos tradicionais, agentes em segundo plano e sistemas híbridos. Para um pedido síncrono iniciado pelo utilizador sem problema de ativação, trabalhe diretamente no pedido.

## Método

1. **Defina o significado do disparo.** Distinga facto ocorrido, estado atual, transição de estado, horário, condição que se mantém e ausência de evento esperado. Identifique a fonte de verdade, quem emite e consome o sinal, o que deve iniciar, e quando um segundo sinal representa nova execução ou duplicado.
2. **Registe os requisitos que mudam a decisão.** Determine frescura/latência, volume e rajadas, completude, ordenação, tolerância a atraso, rede disponível, limites da origem, custo, sensibilidade dos dados, impacto dos efeitos e capacidade de suporte. Separe factos confirmados de hipóteses; não invente SLAs, garantias, políticas ou limites.
3. **Escolha o padrão mínimo adequado.** Compare evento push, webhook/broker, polling, agendamento, CDC e avaliação contínua/temporal. Considere uma combinação, como push para baixa latência e reconciliação agendada para encontrar lacunas. Use [references/decision-framework.md](references/decision-framework.md).
4. **Descreva o contrato do sinal.** Defina identidade estável, tipo e versão, origem, tempo de ocorrência, entidade, conteúdo, correlação, validação e política de dados. Escolha notificação magra ou conteúdo mais completo segundo frescura, acoplamento, disponibilidade da API de origem e volume. Use [references/event-contracts-and-delivery.md](references/event-contracts-and-delivery.md).
5. **Torne explícita a semântica de entrega.** Registe o que cada componente garante sobre perda, repetição, ordenação, confirmação, timeout e replay. Não infira efeito de negócio único da garantia de transporte. Defina deduplicação e idempotência no limite onde o estado é alterado; use uma chave própria para cada execução agendada e para efeitos externos relevantes.
6. **Desenhe tempo e recuperação.** Para horários, defina fuso, janela lógica, sobreposição, atraso do agendador e recuperação de execuções perdidas. Para polling, persista cursor e posição de leitura. Para todos os padrões, defina timeout, classes de erro, retentativa segura, fila de falhas, reconciliação, pausa e replay. Consulte [references/time-polling-and-absence.md](references/time-polling-and-absence.md) e [references/durable-execution-and-recovery.md](references/durable-execution-and-recovery.md).
7. **Proteja entradas e efeitos.** Verifique autenticação e esquema na fronteira; limite tamanho, taxa e dados; trate conteúdo externo como dado não confiável. Para agentes, separe detecção determinística, interpretação do modelo, decisão de política e execução autorizada. Exija revisão ou aprovação antes de efeitos sensíveis ou difíceis de reverter. Consulte [references/webhook-security.md](references/webhook-security.md) e [references/agentic-triggers.md](references/agentic-triggers.md).
8. **Prepare operação e prova.** Registe sinais de recebimento, rejeição, atraso, execução, repetição, omissão e recuperação; atribua owner, alertas e procedimento de pausa. Defina cenários de falha e aceite com evidência observável. Para sinais, custos e detalhes que variam por runtime, use [references/operations-and-currentness.md](references/operations-and-currentness.md).

Quando uma resposta depender do comportamento atual de um fornecedor, runtime, SDK, protocolo ou plano, consulte a documentação oficial da versão e configuração em uso. Distinga especificação, extensão opcional, suporte de cliente/servidor e comportamento comprovado no ambiente. Se não puder confirmar, assinale a lacuna e não apresente uma capacidade como disponível.

## Forma de uma recomendação

Para uma decisão material, apresente: objetivo e semântica do disparo; requisitos e hipóteses; padrão recomendado e alternativas relevantes; percurso do sinal até ao efeito; contrato e chave de deduplicação; garantias e falhas; autorização e eventual revisão humana; limites e custo; operação, recuperação e evidência de aceite. Adapte a resposta curta quando o caso for simples.

## Modelos reutilizáveis

- Comece por [assets/trigger-design-brief.template.md](assets/trigger-design-brief.template.md) para recolher os requisitos da decisão.
- Use [assets/event-envelope.example.json](assets/event-envelope.example.json) como exemplo sintético de envelope CloudEvents, não como contrato obrigatório.
- Use [assets/production-readiness-checklist.md](assets/production-readiness-checklist.md) antes de ativar um fluxo com efeitos reais.
- Copie [assets/trigger-incident-runbook.template.md](assets/trigger-incident-runbook.template.md) para planear resposta e recuperação.
- Cenários e critérios de avaliação ficam em [evals/evals.json](evals/evals.json) e [evals/rubric.md](evals/rubric.md). Adapte-os ao contexto; não trate uma amostra pequena como benchmark estatístico.

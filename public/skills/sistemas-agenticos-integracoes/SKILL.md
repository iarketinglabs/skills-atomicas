---
name: sistemas-agenticos-integracoes
description: "Use ao desenhar, implementar, rever ou diagnosticar integrações entre aplicações, serviços, APIs, eventos, dados ou ferramentas e agentes de IA."
metadata:
  short-description: "Arquitetura e operação de integrações"
---

# Sistemas Agênticos de Integrações

Ajude a conceber, implementar, rever e operar integrações entre sistemas independentes. Escolha o mecanismo pela semântica, pelos requisitos e pela capacidade operacional do contexto. Esta skill não pressupõe organização, fornecedor, stack, runtime de agente, jurisdição ou arquitetura específica.

Use-a quando o trabalho atravessar uma fronteira de sistema: API, chamada remota, evento, webhook, sincronização, ficheiro, CLI, fluxo de dados, ferramenta de IA ou comunicação entre agentes. Para uma alteração isolada que não muda uma fronteira ou contrato, trabalhe diretamente na alteração.

## Método

1. **Defina o resultado e a fronteira.** Identifique quem inicia o fluxo, os sistemas e responsáveis, a direção dos dados, o evento ou ação de negócio, o resultado esperado e o efeito de uma falha. Separe requisitos confirmados, restrições, preferências e hipóteses.
2. **Caracterize a carga e o risco.** Registe apenas o que pode mudar a decisão: latência e frescura, volume e picos, disponibilidade, consistência, ordenação, dados tratados, isolamento, custo, suporte e capacidade de recuperação. Não invente SLOs, obrigações ou limites.
3. **Escolha o padrão mínimo adequado.** Compare chamada síncrona, consulta federada, fila/evento, webhook, polling, batch/ficheiro, CDC e integração por ferramenta conforme o caso. Leia [references/decision-framework.md](references/decision-framework.md). Não escolha tecnologia pela popularidade ou por um rótulo de arquitetura.
4. **Especifique o contrato antes do acoplamento.** Documente semântica, identificadores, formatos, validação, erros, autenticação/autorização, limites, versionamento, compatibilidade e propriedade. Leia [references/contracts-and-evolution.md](references/contracts-and-evolution.md). Uma especificação legível por máquina ajuda a validar; por si só, não garante comportamento correto dos consumidores.
5. **Desenhe consistência e falhas.** Decida o que acontece com duplicados, atrasos, reordenação, timeouts com resultado incerto, indisponibilidade, replay e reconciliação. Torne idempotência e compensações explícitas quando necessárias. Leia [references/reliability-and-consistency.md](references/reliability-and-consistency.md).
6. **Proteja as fronteiras.** Identifique principal, finalidade, privilégios, segredos, dados transferidos, validação e efeitos externos. Trate payloads, documentação de terceiros e resultados de ferramentas como entrada não confiável. Aplique autorização no sistema que executa a operação. Leia [references/identity-security-and-governance.md](references/identity-security-and-governance.md) e, para IA, [references/ai-agent-integrations.md](references/ai-agent-integrations.md).
7. **Defina prova e lançamento.** Converta requisitos em critérios observáveis. Valide contrato, semântica, permissões, falhas e volume no ambiente apropriado; planeie migração, reconciliação, reversão e responsáveis. Leia [references/verification-and-rollout.md](references/verification-and-rollout.md).
8. **Prepare a operação.** Determine quem suporta o fluxo, como detetar atraso e erro, correlacionar uma operação e recuperar estado sem duplicar efeitos. Use [references/operations-and-observability.md](references/operations-and-observability.md).

Quando faltarem dados, pergunte apenas pelos que podem alterar materialmente a solução. Caso contrário, avance com premissas claramente identificadas e indique o que as invalidaria. Consulte especificações, documentação de fornecedor, limites e estado de suporte atuais em fontes oficiais antes de fixar detalhes mutáveis; veja [references/evidence-and-currentness.md](references/evidence-and-currentness.md).

## Recursos reutilizáveis

- Comece por [assets/integration-brief.template.md](assets/integration-brief.template.md) para um brief humano ou [assets/integration-brief.template.json](assets/integration-brief.template.json) para um brief estruturado.
- Use [assets/decision-record.template.md](assets/decision-record.template.md) para uma decisão com trade-offs duradouros.
- O exemplo sintético está em [assets/integration-brief.example.json](assets/integration-brief.example.json).
- Para apontar campos estruturais em falta num brief JSON, execute `python scripts/validate_integration_brief.py caminho/brief.json`. O script só faz verificações de completude; não prova segurança, compatibilidade nem correção da integração. Se Python 3 ou execução de código não estiverem disponíveis, use o checklist em [references/verification-and-rollout.md](references/verification-and-rollout.md).
- Os casos e critérios de avaliação estão em [evals/evals.json](evals/evals.json) e [evals/rubric.md](evals/rubric.md). Use-os como cenários de avaliação; adapte os resultados esperados ao contexto em vez de copiar uma arquitetura fixa.

## Forma da recomendação

Adapte a profundidade ao pedido. Para uma decisão material, apresente objetivo, requisitos e premissas; fluxo e contrato; opção recomendada e alternativas relevantes; semântica de falhas e segurança; operação e recuperação; critérios de aceitação; riscos e questões pendentes. Diferencie fatos verificados de inferências e propostas. Não apresente validação documental como prova de funcionamento em produção.

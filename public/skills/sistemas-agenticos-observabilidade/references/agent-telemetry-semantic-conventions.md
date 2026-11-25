# Convenções de Telemetria Agentic

Use convenções semânticas para que traces, logs e métricas continuem comparáveis entre componentes e releases. Registre o identificador de execução, versão do sistema, operação de modelo, uso de tokens, ferramenta, resultado e classificação de erro — minimizando ou redigindo conteúdo sensível antes da exportação.

Quando houver risco de segurança, acrescente campos estruturados para `actor_chain`, `policy_version`, `capability`, `resource_class`, `source_provenance`, `approval`, `revocation` e `effect_class`. Esses campos devem permitir correlacionar a decisão com o efeito sem copiar prompt privado, PII, segredo, token ou payload bruto.

Registre decisões de política e bloqueios, não apenas sucessos. Preserve a distinção entre intenção declarada, chamada de ferramenta, resultado observado e side effect confirmado. Uma resposta bem formada não prova autorização nem integridade da trajetória.

Avalie separadamente o resultado final e a trajetória quando ferramentas ou efeitos externos importarem. Uma resposta correta não prova que o agente escolheu ferramentas ou permissões de forma aceitável.

Convenções evoluem. Fixe a versão adotada, aceite extensões específicas de fornecedor em namespace separado e revise mudanças antes de comparar séries históricas.

## Fontes primárias

- [OpenTelemetry: GenAI Observability](https://opentelemetry.io/blog/2026/genai-observability/)
- [OpenTelemetry: AI Agent Observability](https://opentelemetry.io/blog/2025/ai-agent-observability/)

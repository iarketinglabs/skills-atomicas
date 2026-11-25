# Threat Modeling e Controles Verificáveis

Modele agentes como principals de software: identifique dados, conteúdo não confiável, ferramentas, efeitos externos e fronteiras de confiança. A Tríade Letal é um atalho útil para localizar risco, mas não substitui a análise de fluxo real.

- Prefira ferramentas estreitas e tipadas a interfaces genéricas com privilégios amplos.
- Aplique autorização determinística no tool boundary; detector de prompt injection é sinal complementar, não autorização.
- Conceda privilégio mínimo por tarefa e reduza ou revogue escopos quando o contexto mudar.
- Converta controles obrigatórios em verificações de pipeline ou runtime, incluindo tentativas de injeção, negação de permissão e exfiltração.

Para riscos de goal hijack, tool misuse, memória contaminada, comunicação interagente e supply chain, use o catálogo e a matriz de evidência em `agentic-security-control-plane.md`.

## Fontes primárias

- [OpenAI: Designing Agents to Resist Prompt Injection](https://openai.com/index/designing-agents-to-resist-prompt-injection/)
- [NIST SP 800-207: Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)

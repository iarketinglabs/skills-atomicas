---
name: sistemas-agenticos-observabilidade
description: "Framework para instrumentar, avaliar e melhorar agentes de IA em produção. Use ao decidir traces, métricas, avaliação de resposta e trajetória, aprovação humana ou versionamento de mudanças comportamentais. Usa o ciclo Trace → Avaliar → Melhorar e não prescreve um fornecedor de observabilidade."
---

# Observabilidade e Melhoria Contínua

## Quando Usar

- Instrumentar um agente para reconstruir a trajetória observável de uma execução que falhou.
- Decidir quais métricas realmente indicam se um agente está funcionando bem.
- Desenhar quando e como um agente deve pedir aprovação humana, sem travar toda a automação.
- Auditar e reverter ações de um agente no nível do sistema de arquivos.
- Versionar uma mudança de prompt ou de topologia multi-agente antes de expor a usuários reais.

## Quando NÃO Usar

- Para escolher a ferramenta de tracing/APM específica do seu projeto — esta skill orienta a arquitetura e as métricas, não substitui a avaliação de fornecedores.
- Para o desenho de sandboxing, identidade de agente, ou o mecanismo físico de revogação de credenciais — isso é escopo canônico da skill de Segurança e Confiabilidade desta coleção, se disponível; aqui só se referencia onde relevante.

## Framework Mental: Trace → Avaliar → Melhorar

### Por que agentes quebram as métricas de software tradicional
Um erro de software tradicional pode quebrar com uma exceção visível e diretamente capturável. Um agente também pode falhar de forma silenciosa: gera texto bem formatado, código que compila ou uma resposta educada, mas logicamente errada ou fora de escopo. Como o mesmo objetivo pode ser alcançado por caminhos de ferramentas distintos, comparar uma execução contra um único caminho esperado gera falsos negativos. Isso exige um ciclo de observação diferente do APM convencional.

### O ciclo de três estágios
1. **Trace:** registrar operações observáveis, resultados, versões e efeitos sob uma referência de execução. Colete o mínimo necessário e inspecione o que a instrumentação realmente exporta. Ver `references/tracing-inputs-outputs.md`.
2. **Avaliar:** medir se o que aconteceu foi bom — nos três eixos de assertividade, performance e custo, com um avaliador independente (LLM-as-a-Judge) fazendo a checagem de qualidade que uma métrica numérica sozinha não captura. Ver `references/assertiveness-and-performance-metrics.md` e `assets/llm-as-a-judge-pattern.md`.
3. **Melhorar:** transformar o que foi observado em mudança real — curadoria de exemplos, ajuste de prompt versionado, calibração de quanto o agente pode operar sozinho. Ver `assets/continuous-improvement-loop.md`, `references/human-in-the-loop-approval-gates.md` e `references/prompt-and-architecture-versioning.md`.

`references/audit-loops-os-skills.md` atravessa os três estágios pela lente física: como interceptar, validar e reverter uma ação no sistema de arquivos em tempo real, não só depois do fato.

## Mapa da Taxonomia

| Sub-tópico | Arquivo de referência |
|---|---|
| Tracing de Inputs e Outputs | `references/tracing-inputs-outputs.md` |
| Métricas de Assertividade e Performance | `references/assertiveness-and-performance-metrics.md` |
| Loops de Auditoria (OS Audit Skills) | `references/audit-loops-os-skills.md` |
| Human-in-the-Loop e Portas de Aprovação | `references/human-in-the-loop-approval-gates.md` |
| Versionamento de Prompts e Arquiteturas | `references/prompt-and-architecture-versioning.md` |
| Convenções de Telemetria Agentic | `references/agent-telemetry-semantic-conventions.md` |

## Observabilidade e Melhoria Contínua

- **Tracing de Inputs e Outputs:** a arquitetura de spans hierárquicos (DAG) que sustenta tudo o resto — sem isso, não há dado para medir nem para melhorar. Ver `references/tracing-inputs-outputs.md`.
- **Métricas de Assertividade e Performance:** a taxonomia completa do que medir sobre os traces capturados — o quê, como e quanto. Ver `references/assertiveness-and-performance-metrics.md`.
- **Loops de Auditoria (OS Audit Skills):** a camada física — interceptação de comandos e File-Integrity Monitoring com rollback automático. Ver `references/audit-loops-os-skills.md`.
- **Human-in-the-Loop e Portas de Aprovação:** quando e como pedir validação humana sem travar o throughput, e como calibrar autonomia ao longo do tempo. Ver `references/human-in-the-loop-approval-gates.md`.
- **Versionamento de Prompts e Arquiteturas:** tratar o comportamento cognitivo do agente com o mesmo rigor de uma mudança de infraestrutura — versionado, testado, revertível. Ver `references/prompt-and-architecture-versioning.md`.
- **Convenções de Telemetria Agentic:** padronizar atributos de modelo, tokens, ferramentas, resultado e release sem acoplamento a fornecedor. Ver `references/agent-telemetry-semantic-conventions.md`.

## Como Usar Esta Skill

Na ausência de acesso autorizado ao runtime ou ao backend, entregue o desenho da instrumentação e os critérios de prova. Para configurar coleta, painéis e sondas de serviços, consulte a skill observabilidade-stack-atomica quando disponível.

1. Leia o Framework Mental antes de abrir qualquer reference — o ciclo Trace → Avaliar → Melhorar é a lente que organiza os cinco arquivos.
2. O padrão LLM-as-a-Judge e o Ciclo de Melhoria Contínua são assets compartilhados por múltiplos arquivos — leia-os uma vez, não a cada reference que os cita.
3. Abra só a(s) reference(s) relevante(s) à pergunta ativa.
4. Para questões de segurança de credenciais, sandboxing profundo ou identidade de agente citadas como cross-reference, consulte a skill de Segurança e Confiabilidade desta coleção, se disponível — esta skill não duplica esse conteúdo.
5. Para rastrear mudanças cognitivas, leia `references/configuration-provenance-in-traces.md`.

## Anti-Padrões de Observabilidade

| Anti-Padrão | Sintoma / Risco | Ver |
|---|---|---|
| Monolithic Logging | Histórico bruto salvo sem rotação, esgotando disco e travando o agente em runs longas | `references/tracing-inputs-outputs.md` |
| Blocking Trace Shippers | Telemetria enviada de forma síncrona, congelando a execução se o servidor de tracing oscilar | `references/tracing-inputs-outputs.md` |
| Correlated Judgment | O mesmo modelo/contexto avaliando o próprio trabalho, sem independência de contexto ou de família | `assets/llm-as-a-judge-pattern.md` |
| Métrica Única de Sucesso | Medir só taxa de conclusão, ignorando custo, latência e taxa de erro de ferramenta | `references/assertiveness-and-performance-metrics.md` |
| Auditoria Só Preventiva | Bloquear comandos perigosos na entrada, mas não monitorar nem reverter corrupção já escrita | `references/audit-loops-os-skills.md` |
| Babysitting Síncrono | Humano aprovando cada micro-passo, anulando o ganho de tempo da automação e gerando fadiga | `references/human-in-the-loop-approval-gates.md` |
| Fadiga de Aprovação | Excesso de gates faz o operador clicar "aprovar" mecanicamente, sem ler o conteúdo | `references/human-in-the-loop-approval-gates.md` |
| Prompt Drift sem Versionamento | Editar comportamento de produção fora do Git, tornando incidentes irreversíveis por falta de rollback | `references/prompt-and-architecture-versioning.md` |
| Dependency Wildcarding | Sempre puxar a versão mais recente de uma dependência cognitiva externa, sem fixar uma versão testada | `references/prompt-and-architecture-versioning.md` |

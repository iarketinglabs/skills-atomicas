---
name: sistemas-agenticos-instrucoes
description: "Framework para projetar instruções de agentes como artefatos de configuração: system prompt, hierarquia de autoridade, contexto recuperável, skills e lifecycle de mudança. Use ao criar, revisar, versionar ou depurar system prompts, decidir o que pertence ao prompt, skill ou contexto, ou tratar conflito entre instruções. Não define cache/tokens, sandbox/ferramentas ou autorização."
---

# Engenharia de Instruções Agentic

## Quando usar

- Projetar ou revisar um system prompt para um agente em produção.
- Separar invariantes, políticas, procedimentos e contexto específico de tarefa.
- Definir precedência, proveniência e carregamento just-in-time de instruções.
- Decidir se um procedimento recorrente deve se tornar uma skill.
- Versionar e avaliar mudança de prompt junto com modelo e harness.

## Quando não usar

- Para cache, compactação, orçamento de tokens ou escolha de modelo: use `sistemas-agenticos-eficiencia`.
- Para sandbox, execução de ferramentas, state machine ou MCP: use `sistemas-agenticos-harness`.
- Para permissões, conteúdo não confiável ou enforcement: use `sistemas-agenticos-seguranca`.

## Modelo mental

Instruções são configuração comportamental de um componente probabilístico, não uma barreira de segurança nem um depósito de documentação. Mantenha o prompt-base pequeno e estável; carregue procedimentos e contexto quando forem necessários; aplique regras críticas fora do modelo.

| Tipo | Finalidade | Local preferido |
|---|---|---|
| Constituição | Identidade, limites persistentes e invariantes | System prompt estável |
| Policy | Regras verificáveis e requisitos de risco | Controle determinístico + prompt resumido |
| Procedure | Fluxo especializado reutilizável | Skill carregada sob demanda |
| Task context | Dados e estado relevantes à tarefa atual | Montagem just-in-time |

## Referências

| Tema | Arquivo |
|---|---|
| System prompt como configuração | `references/system-prompt-as-configuration.md` |
| Autoridade e montagem de contexto | `references/instruction-authority-and-context-assembly.md` |
| Disclosure progressivo e seleção de skills | `references/progressive-disclosure-and-skill-selection.md` |
| Lifecycle e avaliação de prompts | `references/prompt-lifecycle-and-evaluation.md` |

## Como usar

1. Classifique cada instrução na tabela acima e remova duplicações.
2. Declare a origem, a precedência e a validade do contexto antes de entregá-lo ao modelo.
3. Versione a configuração completa que altera comportamento: prompt, modelo, harness, skills e políticas relevantes.
4. Avalie resultado e trajetória antes de promover uma mudança; consulte Observabilidade para os sinais e Segurança para enforcement.

## Anti-padrões

| Anti-padrão | Risco |
|---|---|
| Megaprompt | Custo, conflito e instruções irrelevantes a cada chamada |
| Prompt como controle de acesso | Conteúdo ou modelo contorna uma regra que deveria ser determinística |
| Contexto sem proveniência | Dado obsoleto ou não confiável ganha autoridade indevida |
| Otimização sobre um único caso | Regressão fora do conjunto que gerou a mudança |

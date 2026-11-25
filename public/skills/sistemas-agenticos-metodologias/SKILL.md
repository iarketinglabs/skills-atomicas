---
name: sistemas-agenticos-metodologias
description: "Framework para especificar, organizar e evoluir projetos assistidos por agentes. Use para decidir limites de mudança, spec versus arquitetura, diretivas, scripts determinísticos, compatibilidade, rollout ou rollback. Apresenta disciplina de planejamento como padrão proporcional ao risco; não substitui a especificação do projeto real."
---

# Metodologias de Desenvolvimento

## Quando Usar

- Decidir se algo pertence a `spec.md` (temporário, por feature) ou `architecture.md` (permanente, constituição do repositório).
- Estruturar a especificação de uma nova funcionalidade antes de deixar um agente codificar.
- Organizar as regras e scripts de um repositório para que agentes leiam de forma previsível.
- Evitar que a correção de um comportamento quebre outro silenciosamente.
- Decidir se uma tarefa deve ser resolvida por um agente raciocinando ou por um script determinístico.

## Quando NÃO Usar

- Para escrever o conteúdo real de `spec.md`/`architecture.md` de um projeto específico — esta skill orienta a estrutura e a disciplina, não substitui a redação humana da especificação real.
- Para questões de eficiência de tokens/contexto de uma sessão em andamento — isso é escopo da skill de Eficiência desta coleção, se disponível.
- Para o desenho de sandboxing, segurança de credenciais, ou prevenção de bypass de comandos em profundidade — isso é escopo canônico da skill de Segurança e Confiabilidade desta coleção, se disponível.

## Framework Mental: Duas Disciplinas de Separação

Toda esta skill deriva de duas separações de responsabilidade que se repetem em formas diferentes através dos seis arquivos.

### "Don't Code Before Spec"
A disciplina de Spec Driven Development recomenda que código de produção de risco relevante seja precedido por um plano persistido e validado. Isso desacopla o **Planejamento Cognitivo** (ambíguo, feito com um modelo de raciocínio pesado em parceria com um humano) da **Execução Sintática** (mecânica, delegável a um modelo de menor custo quando a tarefa permitir).

Dentro dessa disciplina, dois documentos têm papéis e ciclos de vida opostos:

| | `spec.md` / `specs.md` | `architecture.md` |
|---|---|---|
| Natureza temporal | Temporário — por feature, descartado ao final | Permanente — constituição do repositório |
| Escopo | O que construir | Como construir |
| Quem escreve | Pode ser gerado com um modelo de raciocínio pesado | Nunca escrito por um agente — só por um humano sênior |

Ver o desenvolvimento completo em `references/planning-before-execution.md` e `references/architecture-md.md`.

### Camada Cognitiva vs. Camada de Execução
A segunda separação organiza o repositório em si: **Directives** (o que fazer e por quê — playbooks em linguagem natural, lidos pelo agente para decidir) e **Executions** (como executar — scripts determinísticos, invocados pelo agente mas nunca reescritos por ele em tempo real). Um agente nunca deve "imaginar" o resultado de uma operação matematicamente precisa — ele invoca um script testado. Ver `references/directives.md` e `references/executions.md`.

## Mapa da Taxonomia

| Ramo | Sub-tópico | Arquivo de referência |
|---|---|---|
| Spec Driven Development | Planejamento Antes da Execução | `references/planning-before-execution.md` |
| Spec Driven Development | Architecture MD | `references/architecture-md.md` |
| Spec Driven Development | Specs.md para Persistência | `references/specs-for-persistence.md` |
| Spec Driven Development | Decisões e Evolução Compatível | `references/decision-records-and-compatible-change.md` |
| Organização de Projetos | Directives (Estratégia/Playbook) | `references/directives.md` |
| Organização de Projetos | Executions (Scripts Determinísticos) | `references/executions.md` |
| Organização de Projetos | Isolamento de Comportamentos | `references/behavior-isolation.md` |

## Spec Driven Development

Como planejar antes de codificar, e o que vai em cada documento:

- **Planejamento Antes da Execução:** a anatomia genérica de um `spec.md` e o loop de planejamento assimétrico (arquiteto + validador hostil). Ver `references/planning-before-execution.md`.
- **Architecture MD:** o documento permanente que rege como o repositório é organizado — e a distinção canônica entre `spec.md` e `architecture.md`. Ver `references/architecture-md.md`.
- **Specs.md para Persistência:** a aplicação do planejamento à camada de dados especificamente — esquema, controle de acesso, cache. Ver `references/specs-for-persistence.md`.
- **Decisões e Evolução Compatível:** como registrar decisões caras de reverter, usar rollout graduado e migrar contratos sem big-bang. Ver `references/decision-records-and-compatible-change.md`.

## Organização de Projetos

Como estruturar o repositório para que agentes operem de forma previsível:

- **Directives:** o playbook estratégico — regras de negócio e comportamento em linguagem natural, modularizadas por diretório. Ver `references/directives.md`.
- **Executions:** os scripts determinísticos que um agente invoca em vez de improvisar no terminal. Ver `references/executions.md`.
- **Isolamento de Comportamentos:** a estrutura de diretórios e o fluxo de decomposição de tarefas que impedem que uma correção quebre outra funcionalidade. Ver `references/behavior-isolation.md`.

## Como Usar Esta Skill

1. Leia o Framework Mental antes de abrir qualquer reference — as duas separações (spec vs. architecture; directives vs. executions) são o vocabulário compartilhado por todos os seis arquivos.
2. Se a dúvida for "isso vai em qual arquivo", comece por `architecture-md.md` (tem a tabela comparativa completa) ou `directives.md` (tem a estrutura de pastas completa).
3. Abra só a(s) reference(s) relevante(s) à pergunta ativa.
4. Se a pergunta cruzar dois ramos (ex. "como decompor uma spec em issues isoladas por comportamento"), sintetize a interseção — `behavior-isolation.md` e `planning-before-execution.md` já se cross-referenciam para esse caso.
5. Para ADR, rollout e rollback de prompts, skills e grafos, leia `references/cognitive-configuration-governance.md`.

## Anti-Padrões de Metodologia

| Anti-Padrão | Sintoma / Risco | Ver |
|---|---|---|
| Vibe Coding | Codificar direto no chat sem plano validado, produzindo código que "parece certo" mas falha sob pressão | `references/planning-before-execution.md` |
| Architecture.md Escrito por IA | Documento de governança permanente gerado ou editado por um agente, perdendo o "gosto" e a senioridade humana que deveria refletir | `references/architecture-md.md` |
| Especificação Sem Mapa de Diretório | Instrução genérica sem caminho de arquivo explícito, agente espalha arquivos arbitrários pelo repositório | `references/specs-for-persistence.md` |
| YOLO Scripting | Agente escreve e executa scripts improvisados no terminal em vez de invocar uma execution testada | `references/executions.md` |
| Trapaça na Linha de Chegada | Agente comenta asserções de teste ou insere tipagem fraca para forçar aprovação artificial | `references/specs-for-persistence.md`, `references/executions.md` |
| Efeito Cobertor de Pobre | Correção em um comportamento quebra outro silenciosamente por falta de isolamento de diretório | `references/behavior-isolation.md`, `references/architecture-md.md` |
| Diretriz Monolítica | Um único arquivo de regras gigante injetado inteiro em toda sessão, em vez de modularizado por diretório | `references/directives.md` |
| Memória Presa no Chat | Decisões e progresso vivendo só no histórico de conversa de um provedor, perdidos ao trocar de ferramenta ou sessão | `assets/sovereign-context-layer.md` |

---
name: sistemas-agenticos-memoria
description: "Framework para memória persistente, recuperação e aprendizagem de agentes de IA. Use ao decidir o que reter entre sessões, como registrar decisões, corrigir memórias, criar backups ou transformar aprendizado recorrente em uma skill. Distingue contexto transitório de memória durável e não substitui a implementação de armazenamento ou RAG."
---

# Memória e Aprendizado de Longo Prazo

## Quando Usar

- Projetar como um agente retém fatos operacionais e preferências entre sessões, sem depender de reler o histórico bruto inteiro.
- Desenhar um loop fechado que otimiza prompts ou procedimentos automaticamente, sem tuning manual constante.
- Decidir quando e como uma execução bem-sucedida deve virar uma skill reutilizável, e como evitar que o repositório de skills degrade com o tempo.
- Definir a arquitetura de backup, versionamento e rollback de um workspace onde um agente escreve de forma autônoma.

## Quando NÃO Usar

- Para o desenho físico de sandboxing, isolamento de kernel ou identidade de agente — isso é escopo canônico da skill de Segurança e Confiabilidade desta coleção, se disponível; aqui só se referencia onde relevante.
- Para a anatomia completa de diretório de uma skill, seu pipeline de compilação a partir de traces em detalhe técnico, e a taxonomia geral de building blocks (skill vs. MCP vs. sub-agente) — isso é escopo canônico da skill de Harness Engineering desta coleção, se disponível; aqui o ângulo é especificamente memória de longo prazo, não a mecânica de construção.
- Para escolher a métrica de sucesso, o formato de tracing ou a escala de calibração de autonomia por score de confiança — isso é escopo canônico da skill de Observabilidade desta coleção, se disponível.

## Framework Mental: O Paradoxo de Memento e o Ciclo de Sonho

### O problema: amnésia estrutural

Modelos de linguagem são stateless por definição — a cada nova sessão ou reinicialização, um agente acorda sem saber quem é o usuário, quais são as metas organizacionais ou o que foi decidido no turno anterior. É o mesmo problema do personagem do filme *Memento*: sem um mecanismo externo de registro, cada despertar é uma folha em branco, forçada a redescobrir do zero o que já foi resolvido.

A resposta ingênua — empacotar todo o histórico bruto na janela de contexto — não escala: gera poluição de atenção, degrada a precisão do modelo e infla o custo de cada chamada. A resposta estrutural exige separar dois papéis:

> **Alugue a inteligência, seja dono da memória.** O modelo de linguagem é uma unidade de processamento cognitivo volátil, contratada para a tarefa corrente — ele pode ser trocado de provedor ou de versão sem perda. O conhecimento acumulado — fatos, procedimentos, decisões — precisa residir em uma camada própria, persistente e sob controle direto, independente de qual modelo está processando a tarefa naquele instante.

### O mecanismo compartilhado: o Ciclo de Sonho (Dreaming Loop)

Os quatro sub-tópicos desta skill parecem tratar de coisas diferentes — fatos, prompts, skills, notas — mas todos resolvem o problema de retenção com a mesma sequência de três estágios, aplicada a um substrato diferente:

```
1. CAPTURA DURANTE A SESSÃO ATIVA
   histórico bruto de decisões, ferramentas e correções acumula em log

2. CONSOLIDAÇÃO EM SLEEP-TIME (o "sonho")
   quando a sessão termina ou a fila de tarefas fica ociosa, um processo em
   background varre o log bruto: deduplica, resolve contradições por
   recência, funde variantes redundantes, aplica decaimento temporal a
   registros frios

3. PERSISTÊNCIA ESTRUTURADA
   o resultado da consolidação vira um registro limpo, denso e barato de
   reler na próxima sessão — nunca o log bruto original
```

Essa sequência nunca roda de forma síncrona durante a tarefa ativa do usuário — rodar consolidação em tempo real desperdiçaria ciclos e arriscaria descartar algo que a sessão corrente ainda está usando. Ela roda em lote, em uma janela dedicada, sobre o que foi acumulado desde a última consolidação.

Cada referência desta skill aplica esse ciclo a uma unidade diferente:

| Referência | O que é capturado | O que é consolidado |
|---|---|---|
| `holographic-memory-local.md` | Transcrições de sessão | Fatos operacionais estruturados |
| `self-improvement-learning-loops.md` | Rastros de execução e falhas | Prompts e regras de comportamento |
| `autonomous-skill-creation.md` | Sequências de ferramentas bem-sucedidas | Procedimentos reutilizáveis (skills) |
| `persistent-backups.md` | Logs de decisão e diários de execução | Notas versionadas e snapshots de código |

O mecanismo comum de envelhecimento e poda que sustenta a etapa de consolidação — `trust_score`, decaimento temporal, limiares de fusão — está centralizado em `assets/temporal-decay-and-trust-score.md`, para não repetir a mesma fórmula em quatro lugares.

## Mapa da Taxonomia

| Sub-tópico | Arquivo de referência |
|---|---|
| Memória Holográfica Local | `references/holographic-memory-local.md` |
| Learning Loops de Auto-aperfeiçoamento | `references/self-improvement-learning-loops.md` |
| Criação Autônoma de Skills | `references/autonomous-skill-creation.md` |
| Backups Persistentes | `references/persistent-backups.md` |

## Memória e Aprendizado de Longo Prazo

- **Memória Holográfica Local:** como transformar transcrições brutas de sessão em fatos estruturados, pesquisáveis e baratos de reler — com recuperação em duas etapas (recência injetada + busca semântica sob demanda) para manter o bootstrap de contexto enxuto. Ver `references/holographic-memory-local.md`.
- **Learning Loops de Auto-aperfeiçoamento:** o duto fechado que separa quem executa a tarefa (Agente de Tarefa) de quem otimiza o comportamento (Meta-Agente), com um Juiz independente validando cada mutação de prompt antes de aceitá-la. Ver `references/self-improvement-learning-loops.md`.
- **Criação Autônoma de Skills:** como uma execução bem-sucedida vira uma capacidade procedural persistente, com a seção de Gotchas como o componente de maior valor, e governança por nível de risco antes de qualquer skill entrar em produção. Ver `references/autonomous-skill-creation.md`.
- **Backups Persistentes:** a arquitetura híbrida de vault de notas + controle de versão que serve como máquina do tempo determinística para qualquer agente com permissão de escrita autônoma. Ver `references/persistent-backups.md`.

## Como Usar Esta Skill

1. Leia o Framework Mental antes de abrir qualquer reference — o Ciclo de Sonho é a lente que organiza os quatro arquivos; sem ele, cada um parece tratar de um sistema não relacionado aos outros.
2. `assets/temporal-decay-and-trust-score.md` é citado por três dos quatro arquivos — leia-o uma vez, não a cada reference que o menciona.
3. Abra só a(s) reference(s) relevante(s) à pergunta ativa.
4. Para a mecânica de compilação de skills em detalhe técnico (anatomia de diretório, pipeline completo de trace-para-skill), para a escala de calibração de autonomia por score de confiança, ou para o desenho físico de sandboxing e identidade de agente citados como cross-reference, consulte as skills de Harness Engineering, Observabilidade e Segurança e Confiabilidade desta coleção, se disponíveis no seu ambiente — esta skill não duplica esse conteúdo.
5. Leia `references/memory-lifecycle-and-provenance.md` antes de recomendar retenção, recuperação ou descarte.
6. Para escolher a forma de memória e governar retrieval, leia `references/memory-types-and-governed-retrieval.md`.

## Anti-Padrões de Memória e Aprendizado

| Anti-Padrão | Sintoma / Risco | Ver |
|---|---|---|
| Amnesia Loops | Ausência de injeção síncrona de contexto imutável no início da sessão — o agente redescobre as mesmas premissas repetidamente | `references/holographic-memory-local.md` |
| Memory Poisoning | Um documento externo malicioso é lido e seu conteúdo é gravado cegamente como fato ou skill persistente, contaminando execuções futuras | `references/holographic-memory-local.md`, `references/autonomous-skill-creation.md` |
| Unowned Context Accumulation | Registros de memória crescem sem poda de relevância nem decaimento temporal, degradando a qualidade do output com o tempo | `assets/temporal-decay-and-trust-score.md` |
| "Leaderboard Game" | O Meta-Agente reescreve prompts para burlar a métrica de avaliação em vez de resolver o problema real | `references/self-improvement-learning-loops.md` |
| Skill Drift / Bloat | Criação livre de skills sem consolidação periódica — dezenas de variantes redundantes confundem a seleção em runtime | `references/autonomous-skill-creation.md` |
| Jailbreak Persistente | Um agente comprometido compila uma skill maliciosa que sobrevive fisicamente no repositório, além da sessão que a originou | `references/autonomous-skill-creation.md` |
| Commit Spamming | Um snapshot é criado a cada micro-interação, poluindo o histórico e inviabilizando auditoria humana de diff | `references/persistent-backups.md` |
| Memória Monolítica | Todo o aprendizado do ecossistema empilhado em um único registro gigante, inundando a janela de contexto de qualquer consulta | `references/persistent-backups.md` |

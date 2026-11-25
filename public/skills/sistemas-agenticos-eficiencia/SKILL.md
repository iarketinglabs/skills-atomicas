---
name: sistemas-agenticos-eficiencia
description: "Framework para decidir custo, contexto, cache e seleção de modelos em agentes de IA. Use quando o pedido envolver tokens, compactação, handoff, tiering, cache de prompts ou latência de inferência. Aplica custo por resultado aceito e exige medir qualidade antes de otimizar; não substitui benchmarks do ambiente real."
---

# Eficiência e Gestão de Tokens

## Quando Usar

- Decidir a estratégia de cache de prompt e a ordem de montagem do contexto de um agente.
- Escolher entre compactar uma sessão longa ou fazer handoff para uma sessão nova.
- Decidir qual classe de modelo usar para uma tarefa específica, ou desenhar um pipeline de tiering.
- Diagnosticar por que os custos de token de um agente estão fora de controle.
- Evitar releitura redundante de arquivos ou reenvio de documentos volumosos brutos.
- Definir quando uma sessão de agente deve terminar e outra começar.

## Quando NÃO Usar

- Para implementar o código de um middleware de cache/compressão específico de uma stack — esta skill orienta o padrão e o trade-off, não substitui a implementação.
- Para decidir a arquitetura geral de segurança ou orquestração de um agente — isso é escopo das skills irmãs desta coleção (Harness Engineering, Segurança e Confiabilidade), se disponíveis no seu ambiente.

## Framework Mental: Outcome Maxxing e a Física da Dumb Zone

Duas ideias sustentam todas as references desta skill.

### Outcome Maxxing: a métrica certa
Medir eficiência pelo preço de tabela por token (*sticker price*) é uma ilusão em ambientes agênticos, onde loops de correção e retentativas dominam o custo real. A métrica correta é o **Custo por Tarefa Aceita**: um modelo mais barato por token que precisa de 5 tentativas a mais para acertar pode ser mais caro no balanço final do que um modelo premium que resolve de primeira. Ver `references/outcome-maxxing.md` para a fórmula completa e a taxonomia de onde os tokens de uma organização realmente vão.

### A física da Dumb Zone
Janelas de contexto de centenas de milhares ou milhões de tokens dão uma falsa sensação de segurança. Na prática, a qualidade da resposta degrada **muito antes** do limite físico:

- **Context Bloat:** metadados irrelevantes, esquemas de ferramentas e logs se acumulam silenciosamente, forçando o processamento de tokens inúteis a cada turno.
- **Context Rot:** conforme o volume cresce, o modelo perde a capacidade de localizar o que importa em meio ao ruído ("lost-in-the-middle") e passa a ignorar regras e repetir erros.
- **Dumb Zone:** o limiar em que a degradação se torna perceptível — pode ocorrer antes em modelos com menor orçamento de inferência do que em modelos de raciocínio pesado (ver a comparação detalhada em `references/model-selection-and-tiering.md`).
- **Context Anxiety:** ao se aproximar da saturação, o modelo pode simplificar lógica, pular validação ou encerrar prematuramente.

**Regra prática:** manter o uso ativo da janela bem abaixo do limiar de degradação (referência recorrente nas fontes: ~50-70% da capacidade) é mais barato e mais confiável do que deixar a sessão se arrastar e depois tentar recuperar a qualidade.

## Mapa da Taxonomia

| Ramo | Sub-tópico | Arquivo de referência |
|---|---|---|
| Token Efficiency | Outcome Maxxing | `references/outcome-maxxing.md` |
| Token Efficiency | Caching e Breakpoints | `references/prompt-caching-and-stable-context.md` |
| Token Efficiency | Seleção de Modelos (Opus vs Sonnet) | `references/model-selection-and-tiering.md` |
| Manutenção de Contexto | Comando Compact | `references/compaction-and-clipping.md` |
| Manutenção de Contexto | Handoff Documentation | `references/handoff-documentation.md` |
| Manutenção de Contexto | Sessões Focadas por Tarefa | `references/focused-task-sessions.md` |
| Eficiência e Gestão de Contexto | Compactação e Clipping de Diálogos | `references/compaction-and-clipping.md` |
| Eficiência e Gestão de Contexto | Deduplicação de Leituras de Arquivos | `references/file-read-deduplication.md` |
| Eficiência e Gestão de Contexto | Seleção de Modelos por Complexidade (Tiering) | `references/model-selection-and-tiering.md` |
| Eficiência e Gestão de Contexto | Redução de Tokens (Língua-2/Redutores) | `references/local-token-reducers.md` |
| Eficiência e Gestão de Contexto | Contexto Estável e Cache de Prompts | `references/prompt-caching-and-stable-context.md` |

Note que três sub-tópicos aparecem duas vezes na taxonomia (Caching/Contexto Estável, Seleção de Modelos/Tiering, Compact/Compactação) — são pares de "duas lentes" do mesmo tema visto pelos dois documentos-fonte, por isso apontam para o mesmo arquivo em vez de conteúdo duplicado.

## Token Efficiency

Como gastar menos por resultado equivalente:

- **Outcome Maxxing:** a métrica e a filosofia que justificam investir em tudo abaixo. Ver `references/outcome-maxxing.md`.
- **Caching e Breakpoints:** a mecânica financeira do prompt caching e como não quebrá-la sem querer. Ver `references/prompt-caching-and-stable-context.md`.
- **Seleção de Modelos:** quando usar um modelo de raciocínio pesado versus um modelo de menor custo, e como isso afeta o cache. Ver `references/model-selection-and-tiering.md`.

## Manutenção de Contexto

Como manter uma sessão de trabalho longa sob controle sem perder precisão:

- **Comando Compact:** a mecânica e as patologias da compactação nativa de histórico. Ver `references/compaction-and-clipping.md`.
- **Handoff Documentation:** o que colocar em um documento de passagem de bastão entre sessões (ou entre ferramentas de agente). Ver `references/handoff-documentation.md`.
- **Sessões Focadas por Tarefa:** quando encerrar uma sessão e começar outra — a disciplina de "nova tarefa, nova sessão". Ver `references/focused-task-sessions.md`.

## Eficiência e Gestão de Contexto

Os padrões técnicos de infraestrutura que sustentam tudo acima:

- **Compactação e Clipping de Diálogos:** trimming, compaction e sumarização ancorada como três técnicas com trade-offs distintos. Ver `references/compaction-and-clipping.md`.
- **Deduplicação de Leituras de Arquivos:** evitar reinjetar o mesmo arquivo inalterado repetidamente. Ver `references/file-read-deduplication.md`.
- **Seleção de Modelos por Complexidade:** o framework de tiering completo (regra de alocação, arquitetura cérebro/músculo, cascade fallback). Ver `references/model-selection-and-tiering.md`.
- **Redução de Tokens com Redutores Locais:** comprimir documentos volumosos com um modelo local antes de gastar tokens pagos. Ver `references/local-token-reducers.md`.
- **Contexto Estável e Cache de Prompts:** a arquitetura de 5 camadas que maximiza o aproveitamento de cache. Ver `references/prompt-caching-and-stable-context.md`.

## Como Usar Esta Skill

1. Leia o Framework Mental (Outcome Maxxing + física da Dumb Zone) antes de abrir qualquer reference — é o vocabulário e a métrica compartilhados por todos os arquivos.
2. Se a pergunta for "por que o custo está alto", comece por `outcome-maxxing.md` para garantir que a métrica de avaliação está certa antes de otimizar a técnica errada.
3. Abra só a(s) reference(s) relevante(s) à pergunta ativa — não é necessário ler os 8 arquivos para uma dúvida pontual.
4. Se a pergunta cruzar duas ou mais references (ex. "handoff + troca de modelo" toca `handoff-documentation.md` e `model-selection-and-tiering.md`), sintetize a interseção explicitamente.
5. Antes de recomendar uma redução de custo, leia `references/measurement-before-optimization.md` e declare o baseline, a quality bar e o efeito esperado.
6. Para cascata de modelos em tarefas longas, leia `references/trajectory-aware-routing.md` e avalie a decisão por etapa, não só por request.

## Anti-Padrões de Eficiência e Gestão de Tokens

| Anti-Padrão | Sintoma / Risco | Ver |
|---|---|---|
| Token Maxxing | Medir sucesso por volume de tokens consumidos em vez de resultado de negócio entregue | `references/outcome-maxxing.md` |
| Token Anxiety | Autocensura no uso de IA por medo de estourar cota — o pêndulo oposto do Token Maxxing | `references/outcome-maxxing.md` |
| Cache Busting Involuntário | Timestamp dinâmico ou troca de modelo no meio da thread invalidando o cache inteiro | `references/prompt-caching-and-stable-context.md`, `references/model-selection-and-tiering.md` |
| Monolithic Prompt Packing | Empacotar manuais inteiros no prompt base "por garantia", em vez de carregamento sob demanda | `references/prompt-caching-and-stable-context.md` |
| Lobotomização de Sessão | Compactação agressiva demais sem âncoras, apagando decisões e preferências importantes | `references/compaction-and-clipping.md` |
| Conversa Imortal | Uma única thread reaproveitada para tarefas semanticamente distintas ao longo de dias | `references/focused-task-sessions.md` |
| Caçando Sticker Price | Escolher modelo pelo preço nominal por token, ignorando o custo real por tarefa aceita | `references/model-selection-and-tiering.md` |
| Releitura Cega de Arquivos | Reinjetar o conteúdo completo de um arquivo inalterado a cada turno | `references/file-read-deduplication.md` |
| Cache Poisoning por Hash Preguiçoso | Confiar em hash/timestamp em memória em vez de recalcular no disco real a cada leitura | `references/file-read-deduplication.md` |
| YOLO Scripting de Compressão | Enviar documentos brutos e volumosos direto ao modelo pago sem redução local prévia | `references/local-token-reducers.md` |

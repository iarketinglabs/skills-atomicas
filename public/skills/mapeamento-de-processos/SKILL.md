---
name: mapeamento-de-processos
description: Metodologia agnóstica de cliente para mapear o estado atual (AS-IS) de um processo de negócio, criar um processo do zero, ou redesenhar (TO-BE) um processo existente — incluindo diagnóstico voltado a oportunidades de IA/automação. Cobre fundamentos (processo vs. função vs. procedimento, elementos estruturais, métricas), os principais frameworks de referência mundial (BPMN, ABPMP CBOK, APQC PCF, Lean/Value Stream Mapping, Six Sigma DMAIC, Teoria das Restrições, Kanban, Heurísticas de Redesenho de Dumas) e o diagnóstico de processos para IA (Process Mining, Task Mining, framework Desconstruir-Redistribuir-Reconstruir, human-in-the-loop). Use SEMPRE que o usuário pedir para "mapear um processo", "documentar o AS-IS", "desenhar/criar um processo novo", "redesenhar/otimizar um processo", "identificar gargalos", "escolher a metodologia certa (Lean, Six Sigma, TOC, BPMN, Kanban)", "montar um roteiro de entrevista de processo" ou "diagnosticar processos para oportunidades de automação/IA". Aplica-se a qualquer área (comercial, operações, atendimento, RH etc.) e a qualquer cliente da Atomica.
---

# Mapeamento, Criação e Reestruturação de Processos

Skill de método — não de conteúdo de um cliente específico. Ensina como mapear o estado atual de um processo, como criar um processo novo do zero, como redesenhá-lo, e como usar esse mapeamento como base para diagnosticar oportunidades de automação/IA. Não codifique aqui nomes de clientes, áreas, ferramentas ou decisões concretas de um projeto real — use placeholders (`<processo>`, `<área>`, `<papel>`, `<sistema>`) sempre que precisar exemplificar.

## Quando usar

- Mapear o AS-IS de um processo (de qualquer área: comercial, operações, atendimento, RH, financeiro etc.).
- Criar um processo novo (TO-BE do zero, sem AS-IS prévio).
- Redesenhar/otimizar um processo existente para reduzir tempo, custo, retrabalho ou variação.
- Escolher qual framework/metodologia aplicar diante de um objetivo específico (ex.: "o gargalo é óbvio, qual método uso?").
- Montar um roteiro de entrevista para levantar um processo com quem executa.
- Diagnosticar um processo já mapeado para identificar onde IA/automação faz sentido — e onde não faz.

## Quando NÃO usar

- Para conduzir o diagnóstico de IA B2B completo de um cliente (6 fases, scorecard de readiness, ROI/TCO, roadmap de governança) — isso é a skill `b2b-diagnostic-audit`, que usa esta skill como base metodológica na sua fase de mapeamento AS-IS e na fase de oportunidades/arquitetura TO-BE.
- Para organizar a base documental viva de um diagnóstico em andamento (matriz de evidências, changelog, árvore de pastas) — isso é a skill `diagnostico-base-documental`.
- Para escolher ferramenta, vendor ou stack técnica de automação — esta skill é sobre método de mapeamento e redesenho, não sobre seleção de tecnologia.

## Passo 1 — Fundamentos, antes de qualquer mapeamento

Leia `references/fundamentos-e-elementos.md`. Antes de escrever qualquer linha sobre um processo, confirme:

1. É de fato um **processo** (horizontal, multifuncional) ou um **procedimento** (restrito a uma função)? Isso muda a granularidade e as métricas certas.
2. Em que categoria macro ele se encaixa: primário, de suporte ou de gestão?
3. Quais dos elementos estruturais (inputs, atividades, outputs, atores, handoffs, regras de negócio, momentos da verdade, controles) já são conhecidos e quais estão em aberto?

## Passo 2 — Escolher o framework certo para o objetivo

Leia `references/frameworks-e-metodologias.md`. Não aplique um framework "porque é o mais conhecido" — escolha pelo objetivo:

- Problema de **desperdício/tempo de ciclo** → Lean / Value Stream Mapping.
- Problema de **variação/qualidade** com dado quantitativo disponível → Six Sigma (DMAIC).
- **Gargalo de capacidade evidente** → Teoria das Restrições (Cinco Passos de Focalização).
- Trabalho de **conhecimento/suporte com alta variabilidade de escopo** → Kanban.
- Necessidade de **diagrama formal** para comunicação negócio-TI ou automação → BPMN.
- Necessidade de **taxonomia/governança** de um portfólio inteiro de processos → ABPMP CBOK / APQC PCF.
- Já se sabe onde atuar e falta **como redesenhar o fluxo lógico** → Heurísticas de Redesenho de Dumas (seção 8 da referência), sempre declarando o trade-off do Quadrângulo do Diabo (Tempo/Custo/Qualidade/Flexibilidade).

## Passo 3 — Levantar o AS-IS

Leia `references/guia-elicitacao-as-is.md` para o roteiro de perguntas por elemento estrutural, e use `references/template-as-is.md` para estruturar o resultado.

Regras inegociáveis:

- **Nunca mapeie só pela documentação oficial** (SOP, fluxograma existente) — ela costuma estar desatualizada. Triangule com entrevista de quem executa (não só de quem gerencia) e, quando houver acesso, com dado de sistema (process mining).
- **Classifique a confiabilidade de cada achado** (factual / hipótese / pendente / contradição / caso observado) — nunca apresente hipótese ou caso isolado como fato consolidado.
- **Distinga AS-IS preliminar de consolidado**: só declare "consolidado" quando o mapeamento cobrir todos os elementos estruturais e tiver sido validado com quem executa o processo.

## Passo 4 — Redesenhar (TO-BE) ou criar do zero

Ao propor um TO-BE (seja redesenho de processo existente ou criação nova):

1. Rode o teste de valor agregado em cada atividade (`fundamentos-e-elementos.md`, seção 5) — elimine antes de automatizar.
2. Aplique as heurísticas de Dumas pela categoria pertinente (cliente / operação / comportamento / organização / informação-tecnologia) e declare explicitamente o trade-off no Quadrângulo do Diabo.
3. Se houver um gargalo evidente, aplique os Cinco Passos de Focalização da TOC antes de redesenhar qualquer outra parte do fluxo.
4. Valide o TO-BE contra os handoffs do AS-IS — cada handoff eliminado ou simplificado deve estar listado explicitamente como ganho, com a justificativa.

## Passo 5 — Diagnosticar oportunidades de IA (quando aplicável)

Leia `references/diagnostico-ia-e-redesenho.md`. Só entre nesta etapa depois de ter um AS-IS (Passo 3) e, idealmente, uma primeira passada de redesenho (Passo 4) — propor automação antes de mapear o problema é o erro mais citado em iniciativas de IA que não convertem em valor.

Pontos centrais a aplicar:

- Prefira **redesenhar o processo com IA já incorporada ao desenho** a simplesmente sobrepor uma ferramenta de IA ao fluxo atual ("bolting-on").
- Combine **Process Mining** (dado de sistema, escopo macro) e **Task Mining** (interação do usuário, escopo micro) quando houver acesso a dados; na ausência, use a triangulação de entrevista como substituto de menor confiabilidade e identifique-a como tal.
- Use o framework **Desconstruir → Redistribuir → Reconstruir** para decidir, tarefa a tarefa, o que é candidato a IA e o que deve permanecer humano.
- Toda tarefa de decisão com impacto direto e irreversível no cliente (aprovação, recusa, atribuição de valor) exige **human-in-the-loop** explícito no desenho — não como item de compliance adicionado depois.
- Nunca apresente estatística de mercado (ex.: "IA reduz custo em 60%") como garantia para o caso específico — é indicativo de mercado, sempre citado com fonte.

## Anti-padrões

| O que não fazer | Por quê |
|---|---|
| Documentar um procedimento como se fosse um processo (ou vice-versa) | Distorce granularidade e métricas; ver Passo 1. |
| Mapear o AS-IS só pela documentação oficial | Documentação desatualizada esconde o trabalho real. |
| Aplicar um framework "porque é o mais conhecido" em vez de pelo objetivo | Lean não resolve problema de variação; Six Sigma não resolve gargalo de capacidade; cada framework tem uso certo (Passo 2). |
| Redesenhar sem declarar o trade-off do Quadrângulo do Diabo | Toda melhoria em um eixo (tempo/custo/qualidade/flexibilidade) tem custo em outro — omitir isso engana quem decide. |
| Automatizar uma etapa antes de testar se ela agrega valor | Acelera desperdício em vez de eliminá-lo. |
| Propor "agente com autonomia total" sem matriz de decisão humana | Viola o pré-requisito de human-in-the-loop para decisões de risco/impacto ao cliente. |
| Apresentar hipótese ou caso isolado como fato consolidado no AS-IS | Compromete qualquer priorização ou business case construído em cima do mapeamento. |
| Saltar direto para "qual ferramenta de IA comprar" sem AS-IS e redesenho prévios | Causa mais citada de iniciativas de IA que não convertem em valor real. |

## Ver também

- Skill `b2b-diagnostic-audit` — usa esta skill como método na fase de Mapeamento AS-IS e na fase de Oportunidades/Arquitetura TO-BE de um diagnóstico de IA B2B completo.
- Skill `diagnostico-base-documental` — governa onde e como o resultado deste mapeamento é registrado e rastreado ao longo de um diagnóstico em andamento.

# Diagnóstico de Processos para Iniciativas de IA

Como usar o mapeamento de processos como base para identificar onde e como aplicar IA — evitando o erro mais comum: sobrepor IA a um processo ineficiente em vez de redesenhá-lo.

## 1. Por que redesenhar antes de automatizar

Pesquisas recentes convergem num ponto: aplicar IA sobre um fluxo de trabalho antigo sem redesenhá-lo ("bolting-on") captura só uma fração do valor potencial — tipicamente até ~20% de ganho, quando gera ganho real. Redesenhar o processo de ponta a ponta com a IA já incorporada ao desenho (não acoplada depois) é o que historicamente separa ganhos modestos de ganhos de várias vezes (relatos de mercado citam de 2x a 3x em produtividade e de 60% a 80% de redução de custo/tempo em iniciativas bem estruturadas — trate esses números como indicativos de mercado, não como garantia, e sempre cite a fonte quando usá-los num relatório para cliente).

**Implicação prática**: nunca pule direto para "quais ferramentas de IA comprar" ou "qual etapa automatizar" sem antes ter um AS-IS completo (ver `fundamentos-e-elementos.md`) e ter aplicado ao menos uma passada de heurísticas de redesenho (ver `frameworks-e-metodologias.md`, seção 8). Propor automação antes de mapear o problema é a causa mais citada de iniciativas de IA que não convertem em valor real.

## 2. Process Mining vs. Task Mining

Duas técnicas complementares de diagnóstico assistido por dados — usadas quando há sistemas ou logs disponíveis, e não apenas relatos de entrevista.

| Técnica | Fonte de dados | Escopo | Objetivo |
|---|---|---|---|
| **Process Mining** | Logs de eventos com timestamp/ID extraídos de sistemas transacionais (ERP, CRM, sistemas de tickets). | Macro, multifuncional, "backend". Reconstrói o fluxo real de ponta a ponta. | Revela variações, exceções, ciclos de retrabalho e gargalos sistêmicos que a documentação oficial não mostra. |
| **Task Mining** | Interações do usuário na própria máquina: cliques, telas, tempo em cada aplicativo. | Micro, individual, "frontend". | Identifica fragmentação no trabalho manual (ex.: copiar dado de um sistema para uma planilha) — a matéria-prima para desenhar automações táticas. |

As duas técnicas se complementam: process mining não enxerga o que acontece em planilhas paralelas e e-mails; task mining não enxerga o impacto sistêmico/lead time de ponta a ponta. Combine-as sempre que houver acesso a dados — na ausência deles, a triangulação por entrevista + documentação + observação direta (Gemba) é o substituto válido, mas deve ser identificada como tal (menor confiabilidade que dado de sistema).

**Nunca mapeie o AS-IS só pela documentação oficial** (SOPs, fluxogramas existentes) — ela costuma estar desatualizada frente ao que as pessoas realmente fazem. Triangule sempre entre entrevista, documentação e, quando disponível, mineração de dados.

## 3. Framework de redesenho: Desconstruir → Redistribuir → Reconstruir

Modelo para diagnosticar processos com foco em IA sem simplesmente substituir caixas de um fluxograma por "agente de IA":

1. **Desconstruir**: quebre funções/papéis rígidos nas tarefas componentes elementares. Para cada tarefa, avalie sua natureza — exige análise estatística/repetição de padrão (candidata a máquina) ou exige cognição fluida, empatia, julgamento sobre ambiguidade imprevista (deve continuar humana)?
2. **Redistribuir**: reatribua capacidade humana e artificial com base nessa análise. IA absorve pesquisa, conciliação de dados e redação de volume; esforço humano liberado migra para supervisão estratégica e interação empática com o cliente — não para ficar ocioso.
3. **Reconstruir**: redesenhe o processo a partir do resultado desejado (não a partir do fluxo atual). O novo desenho deve ter handoffs orquestrados explicitamente entre agentes especialistas (IA) e supervisores humanos de garantia/conformidade.

## 4. Níveis de adoção de IA em processos

Útil para posicionar onde um cliente está e para onde deveria caminhar, sem prometer um salto que a maturidade atual não sustenta:

1. **Adoção superficial**: ferramentas prontas instaladas sobre a estrutura atual, sem transformação processual. Retorno modesto a nulo — muitas vezes negativo quando se soma o custo de licença/inferência ao ganho real.
2. **Redesenho do processo**: fluxos e regras são desfeitos e redesenhados com orquestração de IA como parte central do desenho. É o nível-alvo inicial correto para a maioria das iniciativas — produz ganho visível, auditável e seguro.
3. **Transformação radical do negócio**: incorporação plena de IA permite conceber modelos de produto/rentabilidade inéditos, não apenas otimizar o que já existia. Só faz sentido como destino de médio prazo depois de consolidar o nível 2 — pular direto para cá sem ter passado pelo redesenho estruturado tende a gerar "dívida técnica" e pilotos estagnados.

## 5. Human-in-the-loop é pré-requisito, não opcional

Ao desenhar qualquer processo redesenhado com IA/agentes, separe explicitamente:

- **Tarefas de leitura/orientação/simplificação** (explicar uma norma, apoiar uma decisão com informação): tendem a ser bem aceitas mesmo com autonomia alta.
- **Tarefas de decisão com impacto direto no cliente** (aprovação, recusa, atribuição de valor/prêmio/penalidade): exigem revisão humana explícita antes de executar quando a decisão é irreversível ou tem impacto financeiro/legal relevante — a ausência de arbítrio humano nessas tarefas tende a gerar rejeição e risco reputacional, independentemente da precisão técnica do modelo.

Todo processo redesenhado com IA agêntica deve prever, desde o desenho: (a) rastro auditável das decisões do agente, (b) critério explícito de quando escalar para um humano, e (c) fallback definido para quando a confiança do sistema cair abaixo de um limiar. Não trate isso como item de compliance a ser adicionado depois — é decisão de arquitetura do processo, tomada junto com o redesenho.

## 6. Anti-padrões no diagnóstico de IA sobre processos

| Anti-padrão | Por que evitar |
|---|---|
| Automatizar uma etapa antes de perguntar se ela agrega valor | Acelera desperdício em vez de eliminá-lo (ver `fundamentos-e-elementos.md`, seção 5). |
| Mapear o AS-IS só pela documentação oficial | Documentação desatualizada esconde o trabalho real e o Shadow AI/workarounds já em uso. |
| Tratar Task Mining e Process Mining como substitutos um do outro | Cada um tem um ponto cego que só o outro cobre. |
| Propor "agente com autonomia total" sem matriz de decisão humana | Viola o pré-requisito de human-in-the-loop para decisões de risco (seção 5). |
| Saltar do nível 1 (adoção superficial) direto para o nível 3 (transformação radical) | Gera dívida técnica e pilotos estagnados sem a base de redesenho do nível 2. |
| Apresentar ganhos de mercado ("3x produtividade", "60% de redução de custo") como garantia para o cliente específico | São indicativos de iniciativas bem estruturadas em outras empresas, não uma previsão validada para o caso em análise — sempre cite a fonte e o contexto. |

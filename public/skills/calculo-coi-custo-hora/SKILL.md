---
name: calculo-coi-custo-hora
description: Use esta skill quando o usuário pedir para calcular custo-hora carregado, COI (custo de oportunidade ou custo de ineficiência), estimar o custo de horas de trabalho, converter remuneração em custo por hora ou justificar a automação de uma tarefa manual. Aplique a qualquer cliente ou organização, mesmo quando o pedido não usar o termo "COI" ou "custo-hora" explicitamente — por exemplo "quanto essa equipe gasta fazendo isso à mão" ou "vale a pena automatizar esse relatório".
---

# Cálculo de COI a partir de Custo Homem/Hora

Transforme remuneração e custos do empregador em custo-hora carregado, e custo-hora em COI (Custo de Oportunidade / Custo de Ineficiência) de uma tarefa ou processo manual. O objetivo é sempre uma memória de cálculo rastreável — fórmula, números intermediários, fonte e data de cada premissa — nunca um número final sem lastro.

## Quando usar / Quando NÃO usar

Use esta skill para: converter remuneração e custos patronais informados em custo-hora; estimar custo-hora com dados salariais públicos atuais e comparáveis quando o usuário aceitar essa aproximação; calcular COI de uma tarefa manual (único papel ou processo com múltiplos papéis); calcular ROI/payback simples de automatizar essa tarefa quando já há custo-hora e custo de automação.

Não use para montar um business case completo de iniciativa de IA (TCO multi-categoria, NPV/IRR, Balanced Scorecard, estágio de maturidade, plano de monitoramento) — nesse caso, use `ai-roi-measurement` e, se aplicável, a referência de valor e roadmap de `b2b-diagnostic-audit`. Esta skill resolve o insumo "custo-hora → COI" que alimenta esses business cases; não substitui a análise financeira completa deles.

## Passo 1 — Levantar a variável central

Antes de calcular, obtenha (ou pergunte, se ausente e relevante para o resultado):
- cargo/nível (Estagiário, Assistente/Trainee, Analista Jr, Analista Pleno/Sênior, Coordenador/Especialista, Gerente, Head/Diretor, C-Level/CMO);
- país/jurisdição, moeda e regime de trabalho;
- remuneração e componentes do custo do empregador informados pelo cliente; se ausentes, pergunte se aceita pesquisa em fonte pública atual e comparável;
- porte da empresa e segmento, se o cálculo precisar de ajuste fino.

Nunca presuma país, moeda, nível ou salário quando não informado — pergunte ou declare a lacuna explicitamente.

## Passo 2 — Converter salário em custo-hora

Leia [fórmula de custo-hora](references/formula-custo-hora.md) para calcular a partir dos custos anuais aplicáveis e das horas efetivamente disponíveis. Use as regras e componentes da jurisdição informada; não presuma percentuais legais ou horas padrão.

Se não houver dados salariais, leia [pesquisa de remuneração](references/benchmark-remuneracao-marketing.md). Só use uma estimativa externa se o usuário a aceitar e se houver fonte pública atual, geografia e função comparáveis; caso contrário, marque N/D e solicite os dados necessários. Nunca trate uma estimativa de mercado como o custo real de uma pessoa ou empresa.

## Passo 3 — Calcular COI e, se pedido, ROI/payback

Leia [fórmula de COI e ROI](references/formula-coi-roi.md) para:
- COI de uma única tarefa/papel, ou de um processo com múltiplos papéis (soma por papel);
- custo de uma alternativa automatizada, quando o usuário quiser comparar;
- ROI e payback, distinguindo economia de caixa, capacidade liberada e custo de oportunidade — nunca tratando as três como sinônimos.

## Contrato de saída

Entregue sempre:
1. **Premissas usadas** — cargo, jurisdição, remuneração, regime, componentes do custo patronal e fonte/data de qualquer dado externo.
2. **Memória de cálculo do custo-hora** — fórmula e componentes aplicados, custo anual total, horas anuais efetivamente disponíveis, resultado.
3. **Memória de cálculo do COI** — fórmula aplicada (single-task ou multi-papel), tempo, frequência, número de pessoas, resultado anual.
4. **ROI/payback, se solicitado** — fórmula aplicada, com a distinção explícita entre economia de caixa, capacidade liberada e custo de oportunidade.
5. **Lacunas e limitações** — o que foi assumido, o que é benchmark vs. dado real, e qualquer N/D relevante.

## Guardrails

- Nunca estime o custo carregado a partir apenas do salário sem identificar os custos aplicáveis ao empregador e as horas anuais usadas. Não presuma multiplicadores, contribuições, férias ou jornadas padronizadas.
- Nunca trate tempo liberado como economia de caixa automática; declare se o benefício é caixa, capacidade ou oportunidade antes de apresentar ROI.
- Nunca apresente um dado salarial externo como custo real do cliente; sempre rotule fonte, data, escopo e limitações.
- Nunca preencha lacunas de remuneração, encargos ou horas com um fator implícito. Declare N/D e solicite a premissa ou fonte apropriada.
- Não use estimativas fixas das referências como benchmark; recalcule com dados atuais e aplicáveis ao caso.
- Para qualquer jurisdição, consulte fonte oficial atual para regras de encargos quando elas forem necessárias; se não conseguir verificá-las, peça os custos patronais ao utilizador ou declare a limitação.
- Para business case completo de IA (TCO, NPV, Balanced Scorecard, maturidade), direcione para `ai-roi-measurement` em vez de expandir esta skill para cobrir esse escopo.

## Ver também

- `ai-roi-measurement` — mensuração de ROI de IA e business case completo (TCO, NPV/IRR, Balanced Scorecard, maturidade).
- `b2b-diagnostic-audit` (fase de avaliação de valor) — modelo financeiro de TCO/ROI para diagnóstico B2B.

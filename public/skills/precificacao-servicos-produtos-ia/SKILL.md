---
name: precificacao-servicos-produtos-ia
description: "Defina, revise ou audite o preço de um serviço B2B ou produto B2C2B/SaaS a partir do valor percebido pelo cliente, não do custo. Use para escolher modelo de cobrança (hora, retainer, projeto fechado, outcome-based, freemium, tiered, usage-based, híbrido), estruturar propostas com ancoragem e cercas de preço, ou avaliar benchmarks de mercado — incluindo o nicho de consultoria/produtos de IA. Não use para calcular metas ou cotas comerciais a partir de um preço já definido."
---

# Precificacao Servicos Produtos IA

Defina um preço que capture o valor que o cliente percebe, não o custo do fornecedor. O resultado deve ser uma decisão de preço auditável: método, premissas, opções apresentadas, evidências usadas e prazo de validade explícitos.

## Delimite a decisão

Antes de precificar, identifique:

- o que está sendo vendido — serviço por escopo/projeto, retainer, produto/SaaS, ou uma combinação;
- quem é o comprador e qual é a melhor alternativa disponível a ele hoje (status quo, concorrente, solução interna);
- geografia, moeda e data de referência da decisão;
- se a oferta é relacionada a IA (consultoria, agente, treinamento, governança, comunidade) — nesse caso, pesquise referências comparáveis atuais pelo método documentado, sem assumir uma faixa pronta.

Não invente valor econômico sem dado. Se uma variável impedir uma estimativa responsável, registre-a como pendência com dono e fonte esperada.

## Conduza o workflow

1. Estime o Valor Econômico para o Cliente (EVC): melhor alternativa disponível somada ao valor incremental que a oferta gera — economia, receita adicional ou risco mitigado.
2. Decida a fração do EVC a capturar. Nunca aponte para 100% do teto; use isso para montar um range de preço, não um número único.
3. Escolha o modelo de cobrança adequado ao tipo de oferta — hora, retainer, projeto fechado, outcome-based para serviços; freemium, tiered, usage-based ou híbrido para produtos/SaaS.
4. Estruture a proposta com duas a três opções ancoradas (âncora alta) e, quando houver segmentos com disposição a pagar distinta, adicione cercas de preço que os separem sem canibalizar o plano premium.
5. Se a oferta for de IA e referências de mercado forem relevantes, use o método de pesquisa em `references/benchmarks-precificacao-ia.md`. Não use uma faixa fixa; se não houver fonte comparável e verificável, declare N/D.
6. Registre toda alegação externa usada na decisão no ledger de evidências, incluindo fonte, data, escopo e limitação.
7. Defina o gatilho de revisão: o que muda (custo de entrega, concorrência, valor percebido, regulação) que obriga reprecificar.

Leia [fundamentos de precificação](references/fundamentos-de-precificacao.md) para a lógica de EVC, ancoragem e cercas de preço. Leia [modelos B2B e B2C2B](references/modelos-b2b-e-b2c2b.md) para escolher entre os modelos de cobrança de serviços e de produtos. Leia [pesquisa de preços de IA](references/benchmarks-precificacao-ia.md) quando referências atuais de mercado forem relevantes. Leia [governança de evidências](references/governanca-de-evidencias.md) sempre que usar um benchmark, dado de mercado ou fonte externa na decisão.

## Regras de qualidade

- Nunca apresente cost-plus como método final sem antes checar se ele deixa valor na mesa frente ao EVC estimado.
- Nunca cite um benchmark de preço, margem ou câmbio sem fonte, data, geografia e escopo explícitos.
- Alerte sobre o atrito de fluxo de caixa e de reconhecimento de receita ao migrar uma oferta inteira para outcome-based de uma vez; prefira migração gradual ou modelo híbrido quando a linha de base de métricas ainda não estiver madura.
- Calcule a margem com os custos reais ou estimados da oferta, incluindo inferência, infraestrutura, suporte e operação. Não assuma uma margem universal para SaaS ou IA.
- Quando duas fontes divergirem sobre o mesmo número, exponha as duas; não calcule uma média artificial nem escolha a mais conveniente sem justificar.
- Sempre ofereça mais de uma opção de preço quando a decisão for uma proposta comercial — uma única opção desperdiça ancoragem e efeito centro de palco.

## Formato de entrega

Entregue em Markdown, conciso e rastreável, contendo:

1. contexto da decisão — o que é a oferta, comprador, geografia/moeda, data;
2. EVC estimado, melhor alternativa disponível e premissas usadas;
3. modelo(s) de cobrança recomendado(s), com racional de por que se encaixa na oferta;
4. duas a três opções de proposta com âncora, e cercas de preço se houver segmentação;
5. riscos e armadilhas do modelo escolhido;
6. ledger de evidências, sempre que houver benchmark ou alegação externa relevante;
7. validade da decisão e gatilho de revisão.

Quando o pedido for uma auditoria de um preço já existente, mantenha a estrutura vigente e classifique cada componente como sustentado, frágil, não verificável ou inconsistente, explicando a correção mínima necessária.

## Ferramentas

Calcule cenários a partir das premissas verificáveis. Sem acesso a resultados, custos ou termos atuais do fornecedor, mantenha a premissa explícita, teste sensibilidade e identifique o dado necessário para fechar preço.

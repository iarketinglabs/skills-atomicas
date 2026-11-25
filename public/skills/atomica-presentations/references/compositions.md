# Biblioteca de composições

Todos os tipos aceitam `eyebrow`, `title`, `subtitle`, `source` e `notes`. Os textos dos exemplos são sintéticos. Em `image`, o título identifica a tela na fonte e nas notas, sem aparecer sobre a imagem.

| type | Função | Campos adicionais |
|---|---|---|
| cover | Abrir com promessa e contexto | nenhum; motivo orbital local à direita |
| message | Fixar uma conclusão | `items`: 1–3 cards |
| comparison | Comparar duas escolhas na mesma base | `items`: exatamente 2 cards |
| indicators | Mostrar medidas e definições | `items`: 1–3 cards com `value` |
| process | Explicar uma sequência | `items`: 2–3 etapas numeradas |
| chart | Comparar valores positivos | `items`: 2–6, cada um com `title`, `value` numérico e `text` opcional; `unit` |
| architecture | Mostrar camadas e relações | `items`: 2–3 camadas; `text` explica cada relação |
| team | Mostrar papéis e responsabilidades | `items`: 1–3 com `title`, `text`, `initials` opcional |
| closing | Encerrar com próximo passo concreto | `items`: 1–3 ações |
| timeline | Associar fases, atividades e entregáveis | `items`: 2–3 com `label`, `title`, `text` e `icon` opcional |
| image | Dar destaque a um infográfico ou ilustração completa | `image`: caminho local relativo e `alt`; header, imagem e crédito quando fornecido |
| split | Explicar com imagem lateral e linhas de conteúdo | `image` + `items`: 1–3; texto curto em cada linha |

Card: `title`, `text`, `value` opcional para indicador, `label` opcional e `icon` opcional. Ícones disponíveis: `search`, `settings`, `learn`, `time`, `check`, `chart`, `link`. Não aceite SVG arbitrário na entrada. Ícones explicam a função, não preenchem espaço vazio.

Em `cover`, `image` é opcional. `image_mode: "inset"` mantém a imagem em painel; `"bleed-right"` usa toda a altura e a borda direita com divisão inclinada. O motivo orbital permanece como alternativa quando não há imagem.

Cada etapa ou card tem um único argumento. Não imponha número ou sequência de slides. Alterne ritmo quando a função mudar; repetir uma composição é válido quando a comparação ajuda. Uma imagem em destaque pode servir de pausa entre conceito e operação.

Proposta: contexto → comparação → processo → investimento/indicadores → ação. Relatório: mensagem → indicadores → gráfico → decisão. Treinamento: objetivo → processo → comparação → exercício/ação. São exemplos de raciocínio editorial, não roteiros obrigatórios.

Se uma mensagem exigir fotografia, tabela complexa ou um gráfico incompatível, estenda o template usando os mesmos tokens e valide os novos limites. Não simule suporte inexistente no JSON.

## Cronogramas e condições comerciais

Ao consolidar telas, preserve entregáveis, responsáveis, dependências e critérios de aceite; não apenas some os parágrafos. Mantenha fase, período e atividade próximos. Percentuais, sessões, horas e prazos vêm do briefing, nunca do exemplo. Não use larguras de fases como escala temporal se não forem proporcionais.

Descontos exigem base confirmada: diferencie preço original de preço final, confira percentual e parcelas. Mostre original riscado, benefício e condição próximos, preço final dominante e recorrência separada. Não invente preço de tabela, desconto, quantidade de clientes ou regra comercial. O builder não calcula nem oferece uma composição específica de preços: adapte localmente e valide os números.

# Arquitetura do Wizard (HTML/CSS/JS sem build)

Padrão técnico para um formulário estático, paginado por bloco, sem framework/build step — só HTML + CSS + JS vanilla, publicável como arquivo estático (GitHub Pages ou equivalente). Use `assets/index.html.template`, `assets/form.css.template` e `assets/form.js.template` como esqueleto já implementando este padrão; esta referência explica o "porquê" de cada peça para que você saiba adaptar sem quebrar a lógica.

## Estrutura de Steps (Blocos)

Cada bloco do spec vira um `.step-panel` com `data-step="N"` (um número sequencial de 0 a N) e `data-block="A".."H"` (a letra do bloco, quando aplicável). O passo 0 é tipicamente uma tela de introdução/identificação de quem responde; o último passo é um fechamento (nota final, agradecimento).

Um `<nav>` de "badges" de step (um botão por bloco) permite navegar diretamente para qualquer bloco — **essa navegação não valida nada**, é intencionalmente livre, para o usuário poder revisar/pular. A validação de completude (ver abaixo) só acontece no botão "Avançar" do fluxo linear.

## Mapeamento de Dados: `data-path`

Todo campo respondível carrega um atributo `data-path="BLOCO.grupo_da_pergunta.subcampo"` (ex.: `data-path="A.A1_clientes_ativos"` ou `data-path="B.B1_ferramentas.custo_mensal"`). Dois helpers genéricos serializam/hidratam o formulário inteiro para/de um objeto JS aninhado a partir desse path:

```js
function setPath(obj, path, value) { /* percorre path.split(".") criando objetos intermediários */ }
function getPath(obj, path) { /* percorre path.split(".") lendo valores */ }
```

Checkboxes usam `data-type="checkbox"` (porque `el.value` de um checkbox HTML não é o booleano marcado/desmarcado — é preciso checar `el.checked` explicitamente).

## Tabelas Repetíveis: `data-array-path` + `<template>`

Quando uma pergunta é uma tabela (linhas fixas pré-preenchidas + linhas extras "adicionar mais"), use:

- `<table data-array-path="BLOCO.grupo_da_pergunta">` marca a tabela como um array a serializar/hidratar.
- Um `<template id="template-nome-da-linha">` define o HTML de uma linha, com células carregando `data-field="subcampo"` (path relativo dentro do objeto da linha) e, quando a linha representa um item fixo pré-definido (ex.: nome de uma ferramenta já conhecida), `data-fixed="Valor Fixo"` no lugar de um input editável.
- Uma função `addRow(tbody, templateId, fixedName)` clona o `<template>` e insere no `<tbody>`.
- Linhas extras/opcionais (ex.: "outra ferramenta", "adicionar mais uma pessoa") recebem `data-optional-row="true"` — isso as exclui da checagem de completude estrita (ver abaixo). Marque isso tanto nas linhas já existentes no HTML quanto nas adicionadas dinamicamente pelo botão "+ Adicionar".

## Revelação Condicional

Um grupo de radio buttons que revela um campo extra (ex.: "Sim/Não/Não sei" + detalhe de texto só se "Sim") usa:

- `data-conditional-group` no container do grupo de radio.
- `data-reveals="id-do-elemento-condicional"` em cada radio, apontando para o `id` do elemento a mostrar/esconder.
- O elemento condicional recebe a classe `.conditional-field` e o atributo `hidden` por padrão; o JS troca `hidden` conforme o valor escolhido.
- **Importante para completude:** um campo dentro de um `.conditional-field` escondido nunca é obrigatório; um campo dentro de um `.conditional-field` visível é obrigatório como qualquer outro (ver `isElementRequired` abaixo).

## Grupos de Pergunta e as Duas Noções de Completude

`buildQuestionGroups()` varre todos os `[data-path]` (e `[data-array-path]`) e agrupa por `groupId` = segundo segmento do path (ex.: `A1_clientes_ativos`). Isso cria, para cada pergunta numerada, um objeto `{ type: "fields", els: [...] }` ou `{ type: "table", table: <elemento> }`.

Existem **duas** noções de completude, propositalmente distintas — não confunda uma com a outra:

1. **`isGroupAnswered(groupId)`** — "algum campo do grupo tem valor?". Usada só para a **barra de progresso** (ponderada por tempo estimado de cada pergunta, `QUESTION_TIME_ESTIMATES`), como sinal de "o usuário já começou isso".
2. **`isGroupComplete(groupId)` / `isElementRequired(el)` / `markGroupErrors(groupId)`** — "**todos** os campos obrigatórios do grupo têm valor?", excluindo elementos marcados como não-obrigatórios:
   - Elementos dentro de um `.estimate-flag` (checkbox de "isto é uma estimativa") nunca são obrigatórios.
   - Elementos dentro de um `.conditional-field` escondido nunca são obrigatórios.
   - Linhas de tabela com `data-optional-row="true"` são excluídas da checagem.
   - Grupos de radio contam como satisfeitos se **algum** radio do mesmo `name` estiver marcado (não todos).

   Esta segunda noção é a que **bloqueia o avanço de etapa** (`validateStep(n)` no botão "Avançar") e a que decide a cor do badge de navegação: **preto/completo** = grupo 100% completo; **vermelho/atenção** = etapa já visitada e incompleta (parcial ou vazia); **neutro** = etapa ainda não visitada. Implemente essa gate **desde o primeiro commit** — é o retrofit mais caro de fazer depois.

## Tipografia: Separe "Texto da Pergunta" de "Label de Campo"

Use uma classe CSS dedicada (ex.: `.question-label`) para o texto da pergunta em si (a frase numerada, "A1. Quantos..."), diferente da classe usada para labels de campo individuais dentro da pergunta (ex.: sub-labels como "Volume/mês", "Fonte do dado"). Defina explicitamente `font-family`, `text-transform` e `font-size` da classe de pergunta — **não deixe que ela herde por acidente** o estilo pensado para labels de campo (ex.: uppercase, peso bold, tamanho pequeno de UI). Tratar os dois como a mesma coisa é a causa mais comum de retrabalho de tipografia depois que o formulário já está "pronto".

## Header Sticky sem Gap

Se o header for `position: sticky`, sincronize a variável CSS de altura do header via JS (`documentElement.style.setProperty("--header-h", header.offsetHeight + "px")`) no load e no resize, em vez de fixar um valor estático — texto/branding responsivo muda de altura entre breakpoints, e um valor fixo abre um espaço visível entre o header e o próximo elemento sticky (ex.: a nav de steps).

## Salvamento Local (Autosave)

Use autosave apenas em sessionStorage e somente para formulários sem dados sensíveis. O rascunho fica no separador atual e não é enviado ao servidor. Desative-o para dispositivos partilhados, dados sensíveis ou formulários cujo aviso de privacidade não cubra armazenamento local. Limpe o rascunho após um envio confirmado.

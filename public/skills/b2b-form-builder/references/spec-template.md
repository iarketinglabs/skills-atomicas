# Template de Spec de Perguntas

Use este formato para fechar o conteúdo do formulário **antes** de escrever qualquer HTML (Passo 1 do `SKILL.md`). O objetivo é que qualquer pessoa (inclusive o próprio cliente, se necessário) consiga revisar e aprovar a numeração e o tipo de cada campo sem precisar ler código.

Salve o ficheiro preenchido numa pasta de documentação adequada ao projeto ou num registo de execução com acesso apropriado.

## Estrutura

```markdown
# <Nome do Formulário>

**Enviar para:** <destinatário(s)> — <individual ou compartilhado>

**Tempo estimado:** ~<N> minutos.

**Objetivo:** <por que este formulário existe, o que ele NÃO precisa cobrir por já ter sido coletado em outro lugar (call, entrevista, documento)>.

**Instruções gerais:** <regras de preenchimento — ex.: "se não souber, escreva 'não sei' e indique quem pode confirmar", "marque claramente qualquer estimativa">.

---

## Bloco A — <Nome do Bloco>

**A1. <Pergunta completa, como vai aparecer no formulário>**
*Tipo de campo: <ver tabela de tipos abaixo>.*

**A2. <Pergunta completa>**
*Tipo de campo: <...>.*

---

## Bloco B — <Nome do Bloco>

...
```

## Tabela de Tipos de Campo Suportados

Use exatamente um destes rótulos em cada `*Tipo de campo: ...*` — eles mapeiam direto para a implementação HTML no Passo 2 (ver `references/wizard-architecture.md`):

| Tipo de campo (spec) | Implementação (Passo 2) | Observação |
|---|---|---|
| Texto curto | `<input type="text">` | Uma linha, sem formatação especial |
| Texto longo | `<textarea>` | Resposta aberta, pode ter várias frases |
| Numérico inteiro | `<input type="number" step="1" min="0">` | Contagens, volumes, headcount |
| Monetário | `<input type="number" step="0.01" min="0">` + sufixo de moeda no label (`(€)`, `(R$)`) | Nunca usar `type="text"` para valor monetário |
| Percentual | `<input type="number" step="0.1" min="0" max="100">` + sufixo `(%)` no label | Evita usuário digitar "20%" como string |
| Data | `<input type="date">` | |
| Escolha única | Grupo de `<input type="radio">` com mesmo `name` | Sempre listar as opções no spec, incluindo "Não sei" quando aplicável |
| Múltipla escolha / faixa | Grupo de `<input type="radio">` (faixas são mutuamente exclusivas) ou `<select>` | Preferir `<select>` quando houver mais de 5 opções |
| Tabela com colunas tipadas | `<table data-array-path>` + `<template>` (ver arquitetura) | Sempre listar as colunas e o tipo de cada uma; marcar explicitamente quais linhas são fixas/obrigatórias e quais são extras/opcionais |
| Condicional | Campo que só aparece se outra resposta for um valor específico | Sempre descrever a condição de exibição (ex.: "aparece só se a pergunta anterior for 'Sim'") |

## Regras ao Preencher o Spec

- **Numeração final desde o início.** Não deixe "a definir" na numeração — se uma pergunta pode ser removida ou substituída, decida isso agora, não depois de codar.
- **Marque explicitamente o que é opcional/adicional.** Em tabelas, diga quais linhas são fixas (sempre existem) e quais são "outra opção"/"adicionar mais" (não contam como obrigatórias para efeito de completude no Passo 2). Em campos isolados, diga se são obrigatórios ou opcionais.
- **Nunca invente valor de exemplo do cliente.** Se uma resposta-modelo ajuda a explicar o formato esperado, use um placeholder genérico (`ex.: 20%` ou `ex.: não sei`), nunca um dado real do cliente.
- **Revise com o usuário até fechar.** Este arquivo é o contrato entre o pedido e a implementação — trate qualquer mudança de conteúdo depois do Passo 2 já iniciado como uma operação deliberada, não um ajuste trivial.

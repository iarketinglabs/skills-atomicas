# Schema de Resumo Ancorado (Anchored Iterative Summarization)

Fonte canônica única deste schema — referenciado (não copiado) por `../references/compaction-and-clipping.md` e `../references/prompt-caching-and-stable-context.md`. Resolve o efeito "telefone sem fio" da sumarização monolítica (resumir o resumo do resumo repetidamente, mutando detalhes a cada ciclo) ao manter uma estrutura rígida de campos que só é atualizada incrementalmente, nunca reescrita do zero.

## Os quatro campos imutáveis

```
Session Intent        → a meta estratégica ativa definida pelo usuário
File Modifications     → inventário preciso de arquivos e caminhos alterados
Key Decisions Made     → decisões de design e regras operacionais acordadas
Next Immediate Steps   → próximas ações técnicas planejadas
```

## Mecânica de atualização incremental

1. Quando o limiar de tokens configurado é cruzado (referência de mercado: proativamente a partir de ~70% de preenchimento da janela), apenas o **bloco mais antigo recém-truncado** da conversa é enviado para resumo — nunca o histórico inteiro.
2. Um modelo de utilidade rápido e barato processa esse bloco truncado e extrai atualizações para os quatro campos.
3. O resultado é **mesclado deterministicamente** à estrutura de âncoras já existente — atualiza os registros sem reescrever de forma cega as conclusões estáveis anteriores.
4. Dados verdadeiramente imutáveis (especificação técnica, regras do arquivo mestre de instruções) **nunca** entram nesse ciclo de resumo — residem em arquivos físicos separados, e a janela de compressão conversacional fica reservada só a registrar o comportamento recente do diálogo.

Esse desenho evita tanto a "lobotomização" de uma compactação agressiva demais quanto a deriva progressiva de detalhes finos de uma sumarização recursiva sem âncoras.

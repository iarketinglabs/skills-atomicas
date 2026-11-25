# Checklist de Equilíbrio — Profundidade × Legibilidade

A documentação viva tem um ponto ótimo entre duas falhas simétricas:

- **Superficial demais:** frases genéricas que não ajudam ninguém a entender ou operar o sistema de fato ("o sistema processa mensagens e cria tarefas" sem dizer como).
- **Excesso de informação:** tanto detalhe de implementação, ressalva e caso de borda que a visão do todo se perde — o leitor não consegue mais responder "o que isso faz, em uma frase".

Este checklist ajuda a calibrar cada arquivo antes de considerá-lo pronto.

## Antes de salvar um arquivo (ou uma atualização), pergunte:

1. **Uma frase de abertura resume o assunto?** Quem lê só o primeiro parágrafo já entende do que se trata, mesmo sem ler o resto.
2. **O nível de detalhe combina com o público da pasta?** Um arquivo em `00-visao-geral/` ou `04-fluxos/` (PM e Dev) não deveria exigir conhecimento de código para ser útil; um arquivo em `02-integracoes/` ou `03-modelo-de-dados/` (Dev) pode ser mais técnico.
3. **Cada informação incluída muda o entendimento ou o comportamento de quem lê?** Se removê-la não faz diferença para quem vai operar/entender o sistema, ela provavelmente não deveria estar ali.
4. **Existe uma referência cruzada em vez de repetição?** Se o mesmo conceito já está explicado em outro tópico, linke — não copie.
5. **O arquivo ainda é sobre um assunto só?** Se ao reler você percebe dois assuntos misturados, é sinal de que precisa virar dois arquivos.
6. **Um exemplo concreto (payload, comando, trecho) comunica melhor do que a descrição em prosa?** Se sim, use o exemplo — mas mantenha-o curto, só o suficiente para ilustrar.
7. **Faltou algo que impediria alguém de operar/entender o sistema sem perguntar a quem construiu?** Esse é o teste final — a documentação existe para eliminar essa dependência.

## Sinais de que um arquivo passou do ponto

- Mais de um "por outro lado", "mas atenção que", "exceto quando" empilhados sem estrutura — provavelmente vira uma seção de casos especiais ou um arquivo separado.
- Trechos de código colados sem explicação do porquê — cole só o necessário, explique o resto.
- Histórico de mudanças misturado com a descrição atual ("antes fazia X, agora faz Y, mas em algum momento pode voltar a fazer Z") — a documentação viva descreve o estado atual; histórico de decisão vai para `06-decisoes/`.

## Sinais de que um arquivo está raso demais

- Título e conteúdo dizem basicamente a mesma coisa, sem acrescentar informação.
- Não responde "como" — só "o que" (ex.: diz que existe uma integração com um provedor, mas não diz como ela autentica ou quais dados troca).
- Ninguém conseguiria usar o arquivo para operar, debugar ou estender aquele componente sem perguntar a outra pessoa.

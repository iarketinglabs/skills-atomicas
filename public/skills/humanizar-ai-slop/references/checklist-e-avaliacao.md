# Checklist, severidade e avaliação

## Severidade

Use a severidade para ordenar o trabalho, não para atribuir uma nota ao texto.

- **P0, credibilidade:** fatos inventados, placeholders publicados, citação vazada, parâmetro de rastreamento, autoridade sem possibilidade de conferência, causalidade ou resultado sem suporte.
- **P1, sinal forte:** promoção vazia, inflação de importância, estruturas binárias repetidas, análise em gerúndio, contraste falso, ritmo mecânico, metacomentário e listas simétricas sem conteúdo.
- **P2, acabamento:** transições automáticas, título em Title Case, negrito ornamental, repetição da tese, hashtags excessivas, conclusão genérica e escolha cosmética de pontuação.

Corrija P0 antes de estilizar. Se uma correção P1 ou P2 ameaçar a voz, o locale ou um fato, preserve o original e explique.

## Checklist antes da resposta

### Integridade

- A versão final contém somente fatos, números, nomes, datas, citações e opiniões presentes na fonte ou fornecidos pelo usuário?
- Quando uma frase foi cortada, o espaço ficou vazio ou foi preenchido apenas por material já autorizado, sem conselho ou opinião nova?
- Algum código, frontmatter, dado, link, título, nome próprio ou citação atribuída foi alterado sem autorização?
- Uma hipótese continua marcada como hipótese? Uma lacuna continua marcada como lacuna?

### Voz e locale

- O autor reconheceria vocabulário, cadência, humor, hesitação e grau de polimento?
- A variante pt-BR ou pt-PT está consistente?
- A edição deixou alguma aspereza humana útil em vez de uniformizar todos os parágrafos?

### Conteúdo e estrutura

- Cada parágrafo acrescenta fato, mecanismo, consequência, exemplo ou julgamento?
- A abertura chega ao ponto sem apagar uma cena ou contexto que dá sentido ao texto?
- A conclusão termina em fato, decisão, limite ou ação, e não em slogan?
- As listas, cabeçalhos e emojis têm função no canal?

### Superfície

- Os verbos são diretos sem forçar voz ativa quando a passiva é a melhor escolha?
- Foram removidos intensificadores e transições vazios, não palavras legítimas por aparecerem numa lista?
- O ritmo foi lido em voz alta e não ficou metronômico?
- Travessões, dois-pontos, aspas e negrito servem ao texto?

### Modo

- `detect` não contém reescrita nem pontuação global.
- `rewrite` contém a versão final e o relatório pedido, sem expor rascunhos internos desnecessários.
- `edit` alterou apenas a prosa autorizada e foi relido depois.
- `embedded` devolve somente a saída solicitada.

## Falsos positivos

Não sinalize isoladamente:

- gramática correta, vocabulário formal, texto seco ou mistura de registros;
- uma ocorrência de `contudo`, `importante`, aspas curvas, emoji, travessão ou lista de três itens;
- passiva útil, fragmento de documentação, código, título, citação, nome próprio ou termo técnico;
- texto sem fontes, se a tarefa não exigir checagem factual;
- uma frase curta que cria ênfase sem formar uma sequência dramática.

Procure clusters e compare com a amostra do autor. Se o contexto não permitir decidir, descreva o sinal e deixe a escolha explícita.

## Testes de aceitação

Para cada caso de avaliação, confira:

1. **Fidelidade:** não há afirmação nova nem número alterado.
2. **Voz:** a versão continua reconhecível como o texto de entrada.
3. **Locale:** pt-BR e pt-PT não se misturam sem motivo.
4. **Proteção:** código, frontmatter, links e citações permanecem intactos.
5. **Modo:** a forma de saída corresponde ao pedido.
6. **Concretude:** clichês viram fatos, mecanismos ou consequências; quando isso é impossível, são cortados.
7. **Ritmo:** frases e parágrafos variam sem staccato artificial.
8. **Não autoria:** o relatório fala em padrões e decisões editoriais, nunca em "texto escrito por IA".

## Ciclo RED-GREEN-REFACTOR

- **RED:** rode cada prompt sem a skill e registre escolhas, falhas e racionalizações literais.
- **GREEN:** escreva apenas as instruções necessárias para corrigir essas falhas e rode os mesmos prompts com a skill.
- **REFACTOR:** se o agente preservar um clichê, apagar uma voz regional, editar um trecho protegido ou reescrever em modo `detect`, registre a brecha, corrija a instrução e repita.

Não use apenas contagem de palavras proibidas como teste. Leia todas as ocorrências sinalizadas e avalie o texto completo.

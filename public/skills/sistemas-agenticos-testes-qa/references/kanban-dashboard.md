# Dashboard Kanban do Caderno de Testes

Ferramenta opcional de visualização: um quadro kanban local (HTML/CSS/JS sem framework, sem dependências) que lê os casos de teste escritos com o template de `checklists-and-templates.md` e os mostra como cards arrastáveis entre colunas de status, com um painel lateral de detalhe completo por caso. 100% agnóstica a cliente/projeto — a base fica em `assets/kanban-dashboard/`, pronta para ser copiada para qualquer projeto.

## Quando usar

Depois que os casos de teste já foram escritos (ver "Template de caso de teste" em `checklists-and-templates.md`) e a equipe quer uma forma visual e movível de acompanhar execução — sem depender de uma ferramenta de PM externa, sem custo, rodando localmente. Especialmente útil quando o caderno tem dezenas de casos espalhados por vários arquivos e a pergunta recorrente é "o que ainda falta rodar" ou "quantos testes manuais restam".

Não substitui o registro oficial de resultado — esse continua sendo o campo `RESULTADO` escrito no `.md` de cada caso (ver seção "3. Executar e preservar evidência" do `SKILL.md`). O dashboard é uma lente sobre esse registro, não uma segunda fonte de verdade.

## O contrato que o parser espera

O parser (`assets/kanban-dashboard/build-data.mjs`) procura, em qualquer arquivo `.md` da pasta do caderno, blocos cercados por ` ```text ` contendo uma ou mais entradas delimitadas por uma linha `TEST_ID: <algo>`. Cada entrada é um caso de teste; os campos reconhecidos são os do template canônico (mais as variantes simplificadas mais comuns):

```text
TEST_ID:
TÍTULO:
OWNER:
TEST_BASIS: requisito | história | contrato | arquitetura | incidente
RISCO: evento | impacto | prioridade
OBJETO E FRONTEIRAS:
NÍVEL: componente | integração | sistema | aceitação
TÉCNICA: partição | limite | decisão | transição | caixa-branca | exploratório
PRECONDIÇÕES E DADOS:        (aceita também PRECONDIÇÕES)
ESTADO_INICIAL:
PASSOS/AÇÃO:                 (aceita também PASSOS)
ORÁCULO: resultado | estado | invariantes
AMBIENTE:
EVIDÊNCIA: logs | resposta | banco | trace | screenshot
RESULTADO: pass | fail | blocked | inconclusive
FALHA/CAUSA/OWNER:
VERSÕES E ÚLTIMA EXECUÇÃO:   (aceita também VERSÕES)
```

Um caderno não precisa preencher todos os campos — os ausentes simplesmente não aparecem no painel lateral. O que importa é: (a) usar exatamente esses rótulos de campo (o parser casa por texto, renomear um rótulo faz o parser não reconhecê-lo) e (b) manter cada caso dentro de um bloco ` ```text `.

Exemplo mínimo (domínio genérico, só para ilustrar o formato — não é um caso real):

```text
TEST_ID: AUTH-03
TÍTULO: Login rejeita senha incorreta sem revelar se o usuário existe
TEST_BASIS: requisito de segurança
RISCO: enumeração de usuários válidos por mensagem de erro | impacto médio | prioridade alta
NÍVEL: integração
TÉCNICA: partição de equivalência
PASSOS: enviar POST /login com e-mail válido e senha errada; repetir com e-mail inexistente
ORÁCULO: as duas respostas têm o mesmo código HTTP e a mesma mensagem genérica de erro
EVIDÊNCIA: resposta HTTP das duas chamadas
RESULTADO: a executar
```

## Como o `RESULTADO` vira coluna do quadro

O dashboard tem 5 colunas. As primeiras 4 usam o vocabulário já oficial da skill (ver `SKILL.md`, seção "3. Executar e preservar evidência"); a quinta é o estado natural de backlog antes de qualquer execução:

| Coluna | Quando o `RESULTADO` do caso... |
|---|---|
| A Executar | está vazio, começa com "a executar", ou não bate com nenhuma das opções abaixo |
| Bloqueado | começa com `blocked` |
| Aprovado | começa com `pass` |
| Reprovado | começa com `fail` |
| Inconclusivo | começa com `inconclusive`/`inconclusivo` |

Se o caso tiver um resultado composto (ex.: um nível já verificado por teste automatizado e outro nível ainda pendente de execução manual, escrito como `pass (parte componente) / a executar (parte sistema)`), o dashboard não usa simplesmente a primeira cláusula — ele dá prioridade a qualquer cláusula que ainda não rodou (`a executar`/`blocked`) sobre uma que já rodou (`pass`/`fail`), e só mostra `aprovado`/`reprovado` quando **todas** as cláusulas do resultado já foram executadas. Isso evita um card aparecer como "pronto" quando só uma parte dele foi de fato verificada. O texto completo, com todas as cláusulas, continua visível no painel lateral.

## Ordem lógica de execução (opcional) — `sequence.json`

Por padrão, os cards de cada coluna aparecem em ordem alfabética de `TEST_ID` — raramente é a ordem em que faz sentido um humano executar os testes (ex.: um caso de "mensagem vira tarefa" pode precisar rodar depois de um caso de "grupo ativado", mesmo que o ID do segundo venha depois alfabeticamente). Para definir uma ordem melhor, crie um arquivo `sequence.json` na mesma pasta do `build-data.mjs` instanciado:

```json
{
  "phases": [
    { "label": "Fase 0 — Checagens sem dependência", "ids": ["AUTH-01", "AUTH-02"] },
    { "label": "Fase 1 — Fluxo principal", "ids": ["AUTH-03", "CHECKOUT-01"] }
  ]
}
```

Cada `label` vira um divisor visual dentro das colunas do quadro (e aparece no painel lateral de cada card, campo "Fase da jornada de teste"). A ordem dentro de cada `ids` é a ordem de exibição; um `TEST_ID` que não aparecer em nenhuma fase cai no fim do quadro, em ordem alfabética entre si — então o arquivo pode cobrir só os casos mais importantes de ordenar, sem precisar listar os 100% deles. Sem `sequence.json`, o comportamento é o de sempre (alfabético).

## Como instanciar num projeto novo

```bash
# a partir da raiz do pacote da skill
node scripts/instantiate-kanban-dashboard.mjs --target /caminho/do/projeto/.../dashboard
cd /caminho/do/projeto/.../dashboard
node build-data.mjs
node server.mjs
```

O script de instanciação é idempotente — nunca sobrescreve um arquivo já existente no destino, só cria o que falta. Alternativa manual: copiar `assets/kanban-dashboard/` inteira para dentro do projeto do cliente, como subpasta da pasta onde vivem os `.md` do caderno de testes (o parser assume, por padrão, que os `.md` estão na pasta imediatamente acima; use `node build-data.mjs --source <caminho>` para apontar para outro lugar).

Depois de instanciado, o dashboard passa a ser mantido dentro do projeto do cliente (não mais dentro da skill) — customizações de nome/cor ficam lá, não aqui. Ver `assets/kanban-dashboard/README.md` para o guia completo (como rodar, como regenerar, como mover cards, limitações) e os pontos de customização (nome do projeto, paleta de cores, vocabulário de status/execução).

## Pontos de customização mais comuns

- **Nome do projeto/cliente** e **paleta de cores** — marcados com comentário `TODO`/placeholder em `index.html` e `styles.css` da cópia instanciada.
- **Vocabulário de `RESULTADO` ou de `NÍVEL` diferente do padrão** — ajustar `normalizeStatus`/`classifyExecutionKind` em `build-data.mjs` da cópia instanciada.
- **Casos de teste em subpastas, não direto na pasta do caderno** — `node build-data.mjs --source <caminho>`.
- **Ordem dos cards nas colunas** — criar/editar `sequence.json` (ver seção acima); sem ele, a ordem é alfabética por `TEST_ID`.

## Limitações

- Ferramenta local, sem autenticação, vinculada apenas a 127.0.0.1; não encaminhe a porta nem exponha o dashboard publicamente.
- Mover um card no quadro só grava no `localStorage` do navegador; não reescreve o `.md` de origem. O ciclo de volta (`.md` → resultado real de execução) continua manual, como o resto do registro de evidência da skill.

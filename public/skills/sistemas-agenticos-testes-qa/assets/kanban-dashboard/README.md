# Dashboard Kanban — Caderno de Testes (Atomica)

Visualização kanban, local, dos casos de teste escritos com o template de caso de teste da skill `sistemas-agenticos-testes-qa` (ver `references/checklists-and-templates.md` e `references/kanban-dashboard.md`). Sem framework, sem build step, sem dependências — só Node.js e o navegador. 100% agnóstico a projeto/cliente.

## Como instanciar num projeto novo

Normalmente esta pasta chega ao projeto do cliente via `scripts/instantiate-kanban-dashboard.mjs` da skill (ver o `SKILL.md`/`references/kanban-dashboard.md` para o comando exato). Se preferir copiar manualmente: copie esta pasta inteira (`build-data.mjs`, `server.mjs`, `index.html`, `styles.css`, `app.js`, este `README.md`) para dentro do caderno de testes do projeto, como uma subpasta dele (ex.: `.../caderno-de-testes/dashboard/`) — o parser assume, por padrão, que os arquivos `.md` com os casos de teste estão na pasta **imediatamente acima** desta.

## Como rodar

```bash
cd <pasta-onde-esta-copia-ficou>
node build-data.mjs   # lê os .md da pasta-mãe e gera data.json
node server.mjs        # sobe um servidor estático em http://127.0.0.1:4545
```

Abra `http://127.0.0.1:4545` no navegador. `Ctrl+C` no terminal para parar o servidor.

Se os arquivos `.md` do caderno não estiverem na pasta imediatamente acima (ex.: outra estrutura de pastas), rode `node build-data.mjs --source <caminho-relativo-ou-absoluto>`.

**Por que um servidor e não abrir `index.html` direto (`file://`):** o carregamento de `data.json` via `fetch()` é bloqueado pela política de segurança do navegador quando a página é aberta como arquivo local — precisa vir de `http://`.

## Regenerar depois de editar o caderno

Qualquer mudança nos arquivos `.md` do caderno só aparece no dashboard depois de rodar `node build-data.mjs` de novo (e recarregar a página — não precisa reiniciar o `server.mjs`).

## Como funciona

- **`build-data.mjs`** — parser que lê todo `.md` da pasta-mãe (ou de `--source`), procura blocos ` ```text ` contendo entradas `TEST_ID:` (mesmo template `TEST_ID/TÍTULO/.../RESULTADO` de `references/checklists-and-templates.md`), monta um objeto por caso e grava tudo em `data.json`. Um arquivo `.md` só é considerado "arquivo de casos" se realmente contiver pelo menos um caso — não há suposição de nome de arquivo. O rótulo de área de cada card vem do próprio nome do arquivo (função `humanizeFilename`). O campo `RESULTADO` de cada caso é normalizado para uma das 5 colunas do quadro (`a_executar`, `bloqueado`, `aprovado`, `reprovado`, `inconclusivo` — ver função `normalizeStatus`), reaproveitando o vocabulário `pass/fail/blocked/inconclusive` que já é o vocabulário oficial da skill. O campo `NÍVEL` também alimenta uma classificação heurística de "tipo de execução" (manual/automatizado/revisão de código — função `classifyExecutionKind`), usada no filtro "Execução" do dashboard.
- **`server.mjs`** — servidor HTTP estático minimalista (só `node:http`/`node:fs`), serve os arquivos desta pasta.
- **`index.html` / `styles.css` / `app.js`** — o dashboard em si: quadro kanban com 5 colunas, cards arrastáveis (HTML5 drag-and-drop nativo, sem biblioteca), painel lateral direito com a descrição completa do caso ao clicar num card, busca por ID/título, filtro por área e filtro por tipo de execução.
- **`sequence.json`** (opcional, não vem criado por padrão) — define uma ordem lógica de execução para os cards dentro de cada coluna (em vez da ordem alfabética de `TEST_ID`), agrupada em fases com um rótulo que aparece como divisor visual nas colunas. Ver `references/kanban-dashboard.md` da skill para o formato.

## Movimentar cards

Arraste um card para outra coluna para mudar seu status manualmente. Essa mudança fica salva no `localStorage` do navegador (por isso sobrevive a um recarregamento de página, mas é local a este navegador/computador — não é sincronizada com ninguém, nem reescreve os arquivos `.md` de origem). Um card movido mostra, no painel lateral, tanto o status atual no quadro quanto o status originalmente documentado no caderno.

- **Resetar** (barra superior): descarta todas as movimentações manuais, volta o quadro ao que está documentado nos arquivos `.md`.
- **Exportar** (barra superior): baixa um `.json` com o estado atual de cada card (documentado vs. atual) — útil para registrar o resultado de uma sessão de QA em algum outro lugar (ex.: anexar numa ata, colar numa issue).

## Customização

- **Nome do projeto/cliente:** troque o `<title>` e o texto de `.brand-project` em `index.html` (marcado com `TODO:`).
- **Cores/identidade visual:** variáveis no topo de `styles.css` (`--accent`, `--bg`, etc.) — comentário no arquivo já indica que é um placeholder.
- **Palavras-chave de status/execução:** se o caderno do projeto usar um vocabulário diferente de `pass/fail/blocked/inconclusive` ou de `manual/automatizado/revisão de código`, ajuste `normalizeStatus`/`classifyExecutionKind` em `build-data.mjs`.

## Limitações conhecidas

- É uma ferramenta de visualização/acompanhamento, não o registro oficial — o registro oficial de resultado de cada caso continua sendo o campo `RESULTADO` escrito no `.md` correspondente. Depois de uma sessão de teste real, atualize o `.md` do caso com o resultado encontrado; o dashboard não faz esse caminho de volta automaticamente.
- Sem autenticação/backend: o servidor escuta somente em 127.0.0.1. Não encaminhe a porta nem exponha o dashboard publicamente.

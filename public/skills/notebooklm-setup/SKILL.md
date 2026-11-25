---
name: notebooklm-setup
description: Cria (ou reaproveita) um notebook no NotebookLM para um cliente e sobe nele as fontes já padronizadas em directives/ (meetings, presentations, sales-intelligence e demais subpastas com conteúdo real), transformando o material disperso em uma base de conhecimento consultável via MCP notebooklm-mcp. Use SEMPRE que o usuário pedir para "criar o NotebookLM do cliente", "montar a base de conhecimento no NotebookLM", "subir os documentos/fontes pro NotebookLM", "centralizar transcrições e apresentações no NotebookLM", "sincronizar directives com o NotebookLM" ou "deixar o material do cliente pesquisável no NotebookLM". Roda DEPOIS da skill populate-directives (que preenche directives/ com dados reais) e tipicamente após o kickoff, quando a decisão de usar NotebookLM como base central já foi registrada.
---

# Configurar NotebookLM como Base de Conhecimento do Cliente

Skill para transformar o conteúdo já padronizado em `directives/` em um notebook consultável no NotebookLM, via MCP `notebooklm-mcp`.

## Quando Usar

- A equipe decidiu (em reunião, ata ou pedido explícito do usuário) centralizar transcrições, propostas e inteligência comercial de um cliente em um notebook do NotebookLM.
- O usuário pede para criar o notebook do cliente, subir fontes, ou sincronizar `directives/` com o NotebookLM.
- `directives/` já tem conteúdo real (não apenas os `README.md` de scaffold de cada subpasta).

## Quando NÃO Usar

- Antes de `directives/` estar populada com dados reais — rode primeiro a skill `populate-directives`.
- Para gerar a pauta de kickoff em si — isso é a skill `b2b-kickoff-agenda`. Esta skill não substitui aquela; elas podem rodar em sequência ou em paralelo.
- Se não houver nenhum registro de que o cliente/equipe decidiu usar NotebookLM — confirme com o usuário antes de criar um notebook novo, em vez de assumir a ferramenta.

## Pré-requisito e Portabilidade

- Conector MCP `notebooklm-mcp` autorizado na sessão. Se uma chamada falhar por autenticação, oriente o usuário a rodar `nlm login` no terminal (ou `nlm login switch <profile>` para trocar de conta Google) — não peça tokens ou códigos de autorização diretamente.
- `directives/` deve existir e ter conteúdo real em pelo menos uma subpasta. Se só houver `README.md` de scaffold, avise o usuário em vez de criar um notebook vazio.
- Esta skill é agnóstica a cliente: nunca hardcode nome de cliente, decisor ou caminho de projeto — sempre derive do projeto atual.

## Passo 1 — Confirmar Nome do Cliente e Escopo de Fontes

Obtenha o nome do cliente a partir do nome do projeto/diretório atual ou de `directives/sales-intelligence/` (dossiê já existente). Confirme com o usuário:

- O padrão de título do notebook (padrão sugerido: `<Nome do Cliente> + Atomica`; ajuste se o usuário indicar outro).
- Se é para subir todas as subpastas de `directives/` com conteúdo real, ou só um subconjunto (ex.: só `meetings/` e `sales-intelligence/`).

## Passo 2 — Checar Notebook Existente (Idempotência)

Antes de criar, rode `notebook_list` e procure por um notebook cujo título já corresponda ao cliente. Se existir:

- Reaproveite o `notebook_id` encontrado em vez de criar um duplicado.
- Rode `notebook_get(notebook_id)` para listar as fontes já presentes (por título) — isso alimenta a deduplicação do Passo 5.

Se não existir, siga para o Passo 3.

## Passo 3 — Criar o Notebook

Use `notebook_create` com o título confirmado no Passo 1. Guarde o `notebook_id` e a `url` retornados — serão usados nos passos seguintes e no resumo final.

## Passo 4 — Selecionar as Fontes

Percorra as subpastas de `directives/` combinadas no Passo 1. Para cada subpasta, ignore arquivos que sejam apenas o `README.md` de scaffold (placeholder vazio da subpasta) — só entram arquivos com conteúdo real.

Regra de par `.md` + binário (ex.: `proposta.md` + `proposta.pdf`): suba o `.md` por padrão — o NotebookLM extrai e indexa texto melhor do que faz parsing de layout de slide/planilha para Q&A. Só suba o binário também quando:
- a extensão for suportada nativamente (ver `references/formatos-suportados.md`), **e**
- o usuário pedir explicitamente preservação visual (gráficos, diagramação, fotos) para uso em Studio (áudio/vídeo overview).

Formatos sem suporte nativo (ex.: `.pptx`, `.xlsx`) nunca devem ser enviados diretamente — o `.md` irmão já é o substituto válido. Detalhes completos da lista de extensões suportadas e da tabela de prioridade por subpasta estão em `references/formatos-suportados.md`.

## Passo 5 — Deduplicar

Compare a lista de arquivos selecionada no Passo 4 com os títulos de fontes já presentes no notebook (Passo 2, se reaproveitado). Pule qualquer arquivo cujo título já exista — não recrie a fonte. Se o conteúdo local mudou desde o último envio, sinalize ao usuário em vez de decidir sozinho se deve substituir (o MCP não expõe um "update" de fonte; a alternativa é apagar e reenviar, o que é uma decisão do usuário).

## Passo 6 — Upload em Lote

Para cada arquivo novo, use `source_add` com `source_type=file` e `file_path` absoluto (caminho local acessível pelo processo que roda o servidor MCP). Como os uploads são independentes entre si, dispare as chamadas em paralelo em vez de uma por vez.

`source_add` retorna `ready:false` — isso é o estado inicial normal enquanto o NotebookLM processa a fonte de forma assíncrona. Não é necessário aguardar (`wait=True`) nem bloquear a resposta ao usuário por isso.

## Passo 7 — Resumo Final

Reporte ao usuário, sem gerar arquivo extra a menos que peçam:

- Link do notebook (`notebook.url` do Passo 2 ou 3).
- Quantas fontes novas foram enviadas, por subpasta.
- Quantas foram puladas por já existirem (Passo 5).
- Quais subpastas foram ignoradas por não terem conteúdo real, ou quais formatos foram pulados por falta de suporte nativo (Passo 4).

## Anti-Padrões

| O que NÃO fazer | Por quê |
|---|---|
| Criar um notebook novo a cada execução sem checar `notebook_list` primeiro | Fragmenta a base de conhecimento do cliente em vários notebooks duplicados |
| Subir `README.md` de scaffold de subpasta vazia | Polui a base de conhecimento com ruído sem conteúdo |
| Subir o binário (`.pptx`, `.docx` grande, `.pdf`) quando existe um `.md` irmão, sem pedido explícito de preservação visual | O `.md` já indexa melhor o texto para perguntas e respostas; o binário é complemento, não substituto |
| Tentar enviar `.pptx`/`.xlsx` diretamente como `file` | Extensão não suportada pelo upload de arquivo do NotebookLM — ver `references/formatos-suportados.md` |
| Assumir que o cliente usa NotebookLM sem nenhuma decisão registrada | Pode não ser a ferramenta de conhecimento acordada com o cliente |
| Rodar antes de `directives/` estar populada com dados reais | O notebook fica vazio ou incompleto — rode `populate-directives` antes |
| Pedir token, código de autorização ou callback URL ao usuário quando o MCP não está autenticado | O fluxo de autenticação correto é `nlm login` no terminal, nunca coletar credenciais na conversa |

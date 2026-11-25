# Criação e operação

## Contrato de entrada

JSON UTF-8 com `title`, `lang` (`pt`, `pt-BR`, `pt-PT` ou `en`), `footer` e `slides`. Cada slide segue a biblioteca de composições. `notes` é uma string privada com falas e observações; não inclua notas em `text`, `source` ou `footer`. Strings são escapadas como texto, nunca interpretadas como HTML. O builder rejeita campos desconhecidos para evitar conteúdo descartado silenciosamente.

`chart.value` é número finito maior ou igual a zero; ao menos um valor deve ser positivo. Indicadores aceitam `value` textual. `source` contém origem, período, unidade ou a marca “Exemplo fictício”. Não há busca ou validação factual automática.

## Comandos

Imagens em `cover`, `image` ou `split` usam `image: {"path": "imagens/ilustracao.png", "alt": "Descrição do conteúdo"}`. O caminho é relativo à pasta do JSON e fica dentro dela; PNG, JPEG e WebP são aceitos. O builder verifica arquivos e copia as imagens indicadas para `assets/media/`, sem depender do local original. Caminhos absolutos, travessia e links simbólicos para fora da pasta são rejeitados. Não existe URL remota na entrada de imagem.

Vídeos em `cover`, `image` ou `split` usam `video: {"path": "media/animacao.webm", "poster": "media/animacao.png", "alt": "Descrição da animação"}`. Ambos os caminhos são locais e relativos ao diretório do JSON. A construção copia os arquivos para `assets/media/`. Escolha imagem ou vídeo para cada slide. Leia [Vídeo em loop](loop-video-assets.md) para o aceite.

O HTML gerado reproduz o vídeo apenas no slide ativo. `prefers-reduced-motion`, falha de reprodução e impressão mostram o poster local. A área do vídeo usa `object-fit: contain` e fundo transparente para preservar a animação inteira e o background do slide. Leia `references/loop-video-assets.md` antes de ajustar a composição ou o CSS do vídeo.

Em capas ilustradas, `image_mode` aceita `inset` ou `bleed-right`. Ícones e etiquetas seguem `references/compositions.md`. [Exemplo editorial](../assets/editorial-example.json) e [Exemplo de slide único](../assets/image-only-example.json) usam ilustração fictícia local. Copie o JSON e a ilustração para o mesmo diretório de trabalho antes de editar.

Execute a partir da raiz desta skill, ou use caminhos absolutos dos scripts:

```powershell
python scripts/deck.py init trabalho/briefing.json
python scripts/deck.py build trabalho/briefing.json trabalho/deck --fonts-dir trabalho/fontes
python -m pip install -r scripts/requirements.txt
python scripts/verify.py trabalho/deck --pdf --channel chrome
```

Prepare os arquivos de fonte e avisos conforme [Recursos do pacote](assets.md). Se omitir `--fonts-dir`, o builder procura a pasta `fonts` junto ao JSON. Use `python -m playwright install chromium` e omita `--channel chrome` quando tiver somente o Chromium do Playwright.

`init` e `build` recusam sobrescrever arquivos/diretórios. Para revisar, gere uma nova pasta. O resultado pode ser aberto diretamente em `index.html`; não precisa de servidor. `presenter.html` carrega as mesmas mídias e revela as notas com S. Distribua apenas `index.html`, `assets/` e PDF. Capturas e relatório são evidência de QA; revise-os antes de distribuição.

O verificador exige que o navegador já esteja instalado. Ele bloqueia requisições HTTP, HTTPS e WebSocket, espera fontes e imagens e falha em erros de JavaScript, recursos ausentes ou geometria inválida. O PDF usa CSS de impressão, sem transições e sem painéis privados. O diretório `qa/` contém capturas por slide e página PDF e relatório JSON; o relatório registra os testes realmente executados.

## Editorial

Defina o resultado esperado e a decisão do público antes do layout. Escreva títulos como conclusões, evite jargão e mantenha detalhes de apoio nas falas. Aprove textos e números antes de congelar o PDF. Registre pressupostos e pendências; não invente clientes, retorno financeiro ou resultados para preencher uma composição.

# Aceite

## Automático

- Frontmatter válido, nome igual à pasta, descrição abaixo de 1024 caracteres e referências existentes.
- Entrada validada; tipo desconhecido, campos desconhecidos, dados inválidos e destino existente produzem erro.
- HTML público sem `notes`, sem painel privado e sem texto das notas. O verificador compara com os valores de notas do arquivo privado.
- Fontes locais realmente carregadas, todas as imagens completas, zero erros de script e zero recursos externos necessários.
- Todos os slides dentro de 1920×1080, sem texto transbordando sua caixa, sem colisões entre cards ou entre área de título e corpo. Layout a 1920×1080 e 390×844 com escala proporcional; em telefone, é apresentação reduzida, não página de leitura refluída.
- Caixas de imagem, SVG, vídeo, canvas e figuras dentro do canvas. Sangria pode atravessar a margem segura, nunca a borda externa; `verify.py` deve reportar mídia fora do slide.
- Teclas de navegação, Home/End, ajuda, notas e reinício do cronômetro funcionando. Fullscreen depende da permissão do navegador e precisa de teste interativo quando não disponível no modo automatizado.
- Botões visíveis e acessíveis de avançar e voltar no desktop e no celular; inativos nos respectivos limites e ocultos na impressão. Teste as setas do teclado, scroll vertical nos dois sentidos e deslize horizontal nos dois sentidos, sem saltos múltiplos nem bloquear controles interativos. A simulação de toque não substitui um teste em aparelho físico quando ele for exigido.
- Movimento reduzido sem animação. Impressão com tudo visível; PDF com uma página 16:9 por slide, texto e gráficos completos e sem notas.
- Símbolo isolado no header, sem duplicação do nome dentro do ícone. Barra com largura correspondente à posição atual, início/fim e retorno verificados.
- Atomica sem acento; AndROI, quando presente, mantém caixa e ROI serifado, negrito e itálico, com fonte local carregada e incorporada ao PDF.
- Imagens locais copiadas, sem dependência do diretório original. Confirme título/número do slide pedido, `src` no HTML final, proporção, corte e conteúdo preservado. Uma imagem gerada mas não referenciada no HTML não foi aplicada; inserir uma imagem não remove texto, dados ou framework aprovado.
- Sangria não cobre texto importante; infográficos ficam inteiros. Quando uma imagem deve sobrepor o rodapé, confira a captura e a página do PDF: z-index sozinho não prova cobertura, especialmente com transparência. Verifique a ordem das camadas e que a imagem continue dentro do canvas.

## Vídeos em loop

Para slides com vídeo, acrescente à revisão manual os critérios de `references/loop-video-assets.md`: a origem e o poster locais são os pretendidos; em navegador com movimento normal o vídeo toca, repete e preserva alfa sobre o fundo, sem card preto nem corte da figura; fora do slide ativo pausa; movimento reduzido e PDF apresentam o poster transparente. Revise cada slide com vídeo em captura HTML e página PDF, inclusive colisões com conteúdo e footer. O verificador usa movimento reduzido, portanto as suas capturas e o PDF confirmam o fallback visual, mas não substituem a conferência de reprodução no navegador.

## Visual humano

Abra cada captura de slide e cada página do PDF. Confira hierarquia, texto legível, área segura, logo proporcional, retícula discreta, gráficos coerentes, acentos, fontes e alinhamento. Contact sheets ajudam na comparação do conjunto, mas use páginas individuais quando houver densidade ou dúvida. Registre falhas por slide, correções e evidência revista. Não declare aprovação visual humana com base apenas em contadores automáticos.

Confira variedade de composição, pertinência das imagens, direções e destinos de conectores em diagramas e fidelidade de logos. Compare títulos, ordem e itens obrigatórios com a fonte para detectar slides ou conteúdo sacrificados durante a renderização. Valide condições comerciais e cronogramas contra a fonte atual. Quando houver serviço local ou remoto, confira a URL entregue e os arquivos realmente servidos, não apenas a pasta de build.

Use o mapa visual para detectar estruturas repetidas sem intenção e espaços grandes sem função. Prefira ampliar imagem, diagrama ou dados que carregam a mensagem; não preencha por decoração.

## Testes de portabilidade

Copie somente a skill para uma pasta fora do projeto. Gere proposta comercial, relatório executivo, treinamento e exemplo editorial com português e inglês. Execute com rede bloqueada. O cenário editorial exercita imagens empacotadas, capa com sangria, split, cronograma, ícones e a serifada de marca; não exige geração de imagem.

Configure a variável de ambiente `DECK_FONTS_DIR` com a pasta descrita em [Recursos do pacote](assets.md). Execute `python -m unittest discover -s scripts -p "test_*.py"` para validar contrato, privacidade, cópia de mídia e navegação. Os testes de montagem dependem das fontes e os de navegação do navegador instalado.

Rode `python scripts/verify.py trabalho/deck --pdf --channel chrome` para as capturas, o PDF e o relatório técnico. Complete a conferência visual antes da entrega.

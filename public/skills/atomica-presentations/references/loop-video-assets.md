# Vídeo em loop

Use WebM e poster PNG locais, com paths relativos ao JSON. Coloque ambos numa pasta sob o diretório de entrada. Indique `alt` que descreva o que a pessoa precisa entender. Reserve a composição por objetivo: capa ilustrada, imagem de destaque ou faixa lateral. Use material aprovado para o destino e mantenha fontes originais privadas.

O builder copia ambos para a saída. O player reproduz o loop mudo no slide ativo e usa o poster em impressão, movimento reduzido e falha de reprodução. O PDF depende do poster. Confirme que este contém a informação que a animação comunica.

Caso o vídeo tenha recorte transparente, compare o WebM e o poster contra o fundo real. Propriedades reportadas por uma ferramenta isolada podem omitir alfa. Teste enquadramento, texto, reprodução, pausa fora do slide, movimento reduzido e impressão. Se a mídia falhar durante QA, substitua-a por material autorizado ou remova a referência e recompose o slide antes de publicar.

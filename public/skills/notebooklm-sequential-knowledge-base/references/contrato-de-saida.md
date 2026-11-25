# Contrato de saída e verificação

## Pergunta por tópico

> Desenvolva o conteúdo final de um guia sobre [tópico], no contexto [eixo]. Use as fontes selecionadas. Inclua os conceitos necessários, exemplos práticos e limites. Associe as afirmações decisivas à fonte e separe o que as fontes não sustentam. Entregue o guia nesta resposta.

Se o notebook fornecer apenas um esboço ou oferecer criar outro artefato, peça a resposta final em uma única tentativa por vez. A extensão depende do escopo. Uma resposta curta pode ser suficiente se tratar o tópico e os limites com evidência.

## Documento

O arquivo começa com um H1, seguido do conteúdo final em Markdown. Use H2 a H6 para organizar o corpo. Preserve blocos de código, listas, tabelas e atribuições. Ajuste somente o invólucro, títulos duplicados e ruído da interface. Preserve recuos e linhas em branco dentro de código. Remova uma oferta de geração apenas quando estiver separada do corpo e não constituir recomendação técnica.

Verifique visualmente o começo e o fim da resposta, os dados citados e o vínculo de afirmações com suas fontes. Quando os marcadores de citação só funcionarem na interface, registre no índice o título e a localização verificável, como seção ou página. Alterar o texto, extrapolar um achado ou compilar outro conteúdo é uma transformação separada que precisa de registro. Uma revisão que reutiliza o Markdown identifica sua origem no notebook sem promover a saída a fonte primária.

## Verificação local

O validador aceita um arquivo `.md` ou uma pasta exclusiva de respostas que será examinada recursivamente. Confere UTF-8, H1 inicial único fora de código, corpo não vazio, cercas de código fechadas e invólucros de transporte reconhecíveis. Saída `0` indica que essas regras passaram. Saída `1` lista falhas ou divergência de contagem. A opção `--expected-count` exige igualdade numérica. Compare também os nomes com o índice, pois a contagem pode bater com o item errado no lugar.

A avaliação humana ou pela skill precisa verificar suficiência, precisão, ausência de respostas provisórias, citações, revisão de informação sensível e autorização de uso. Um script estrutural não resolve essas decisões. Quando validar manualmente, aplique as mesmas regras e relate quantos arquivos foram efetivamente abertos.

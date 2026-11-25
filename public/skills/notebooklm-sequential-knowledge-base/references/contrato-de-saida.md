# Contrato de saída e verificação

## Pergunta por tópico

> Desenvolva o conteúdo final de um guia sobre [tópico], no contexto [eixo]. Use as fontes selecionadas. Inclua os conceitos necessários, exemplos práticos e limites. Associe as afirmações decisivas à fonte e separe o que as fontes não sustentam. Entregue o guia nesta resposta.

Se o notebook fornecer apenas um esboço ou oferecer criar outro artefato, peça a resposta final em uma única tentativa por vez. A extensão depende do escopo. Uma resposta curta pode ser suficiente se tratar o tópico e os limites com evidência.

## Documento

Na primeira linha, use um título com texto na sintaxe ATX, como `# Título da resposta`. Organize as seções do corpo com `##` a `######`. Use a mesma sintaxe ao normalizar títulos sublinhados do original. Uma linha feita só de `=` fora de código é rejeitada como possível marca de título Setext. Se a linha fizer parte de um exemplo técnico, mantenha-a dentro de um bloco de código.

Preserve blocos de código, listas, tabelas e atribuições. Ajuste somente o invólucro, títulos duplicados e ruído da interface. Preserve recuos e linhas em branco dentro de código. Remova uma oferta de geração apenas quando estiver separada do corpo e não constituir recomendação técnica.

Verifique visualmente o começo e o fim da resposta, os dados citados e o vínculo de afirmações com suas fontes. Quando os marcadores de citação só funcionarem na interface, registre no índice o título e a localização verificável, como seção ou página. Alterar o texto, extrapolar um achado ou compilar outro conteúdo é uma transformação separada que precisa de registro. Uma revisão que reutiliza o Markdown identifica sua origem no notebook sem promover a saída a fonte primária.

## Verificação local

O validador aceita um arquivo `.md` ou uma pasta exclusiva de respostas que será examinada recursivamente. Confere UTF-8, um único H1 ATX fora de código, cercas de código fechadas e corpo com conteúdo além dos cabeçalhos. Um bloco de código preenchido conta como conteúdo. Uma cerca vazia por si só não satisfaz essa verificação. A checagem de títulos usa a formatação ATX simples no nível do documento. Revise manualmente títulos em HTML ou em blocos aninhados.

O validador rejeita um objeto JSON que ocupe todo o corpo e combine campos característicos do envelope, como `answer` e `conversation_id`. Um exemplo JSON cercado como código é preservado. Se houver seções `Consulta` e `Resposta`, o script emite `REVIEW`. Leia as seções para distinguir uma pergunta repetida de conteúdo técnico legítimo. Mantenha o conteúdo quando os títulos fizerem parte do guia.

Saída `0` indica aprovação estrutural mesmo quando há uma nota `REVIEW`. Saída `1` indica falha de validação ou divergência de contagem. A opção `--expected-count` exige igualdade numérica. Compare também os nomes com o índice, pois a contagem pode bater com o item errado no lugar.

A avaliação humana ou pela skill precisa verificar suficiência, precisão, ausência de respostas provisórias, citações, revisão de informação sensível e autorização de uso. Quando validar manualmente, aplique as mesmas regras e relate quantos arquivos foram efetivamente abertos.

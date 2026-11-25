# Image-to-Video: Referência de Prompting

Use esta referência sempre que uma imagem participar como quadro inicial, quadro final, referência de personagem, cenário ou objeto. I2V não é T2V com uma imagem anexada: a referência já estabelece parte relevante da aparência e composição.

## Princípio central

Não redescreva o que a imagem já resolve. Direcione a evolução temporal:

```text
[subject motion] + [camera motion] + [secondary physics or dynamic light] +
[requested audio or dialogue] + [continuity and requested constraints]
```

Antes de escrever, identifique o papel de cada arquivo. Não chame uma imagem de `start frame`, `end frame`, `character reference` ou use tags se a plataforma não suportar esse papel ou essa sintaxe.

## Modos de referência

### Uma imagem inicial

Use quando a imagem define o estado inicial. Estenda uma ação já plausível no enquadramento, indicando direção, velocidade e término. Para uma cena sem corte, descreva explicitamente uma tomada contínua quando essa for a intenção do usuário.

### Imagem inicial e final

Use somente se o gerador aceitar os dois quadros. Descreva a transição física contínua do estado inicial ao final; é adequado para mudança de pose, iluminação, posição ou câmera que precisa chegar a um estado conhecido. Não afirme que o caminho intermediário será reproduzido exatamente.

### Referências múltiplas

Só use referências de personagem, ambiente ou objeto quando seus papéis e a capacidade da ferramenta forem conhecidos. Declare as invariantes relevantes — por exemplo, traços do personagem, figurino ou objeto — sem prometer identidade perfeita. Nunca invente `@tags` ou uma ordem de anexos.

## Movimento, câmera e física

- Priorize uma ação principal e, no máximo, movimentos secundários que reforcem essa ação.
- Associe física ao que a imagem permite: tecido acompanhando uma caminhada, vapor subindo, reflexos mudando ou chuva atravessando o quadro. Não adicione física que contradiga a imagem.
- Descreva câmera com trajetória e destino: `the camera slowly tilts up to reveal the stained-glass window`.
- Ajuste complexidade à duração. Ações com muitas etapas, rotações amplas e alterações bruscas de luz exigem mais tempo ou referências de estado adicionais.

## Continuidade e estabilidade

Verifique a imagem antes de animá-la: composição, anatomia, luz, objetos e identidade visíveis devem estar aceitáveis no quadro de partida. A geração de vídeo pode ampliar defeitos preexistentes.

Preserve apenas as invariantes que importam para o objetivo. Cite, por exemplo, `maintain the character's visible facial features and clothing continuity from the reference image`; não use termos como `exactly identical` ou promessas de preservação pixel a pixel.

## Áudio e texto

Inclua diálogo entre aspas apenas quando a pessoa o fornecer. Música, efeitos, legendas e lip-sync são condicionais à plataforma; trate-os como intenção do briefing, não como controles universais.

## Perguntas de alinhamento específicas de I2V

Pergunte, se ainda não estiver definido:

1. Qual é o papel da imagem: início, fim, personagem, ambiente ou objeto?
2. O que deve se mover e o que precisa permanecer visualmente consistente?
3. A cena deve ser uma tomada contínua ou inclui uma transição/corte permitido?
4. Qual duração, formato e prioridade criativa orientam a complexidade do movimento?

Não repita perguntas que já tenham sido respondidas no briefing geral.

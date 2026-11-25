# Cinematografia e Tempo para Prompts de Vídeo

Use esta referência para construir ou revisar prompts T2V e para escolher vocabulário de direção. Ela organiza intenção cinematográfica; não confirma recursos de uma plataforma específica.

## Estrutura semântica T2V

Organize a descrição por prioridade:

```text
[camera and framing] + [subject and physical action] + [environment] +
[lighting and color] + [audio or dialogue, if requested] + [constraints]
```

Comece com o que não pode falhar. Cada elemento precisa contribuir para uma ação observável ou para a leitura da cena.

## Direção de câmera

| Intenção | Linguagem útil | Complete com |
| --- | --- | --- |
| Aproximar | `slow dolly in` | o detalhe ou emoção revelada |
| Afastar | `dolly out` | o ambiente revelado |
| Acompanhar | `tracking shot`, `follow shot` | direção e velocidade do sujeito |
| Girar horizontalmente | `pan left`, `pan right` | o elemento que entra no quadro |
| Inclinar | `tilt up`, `tilt down` | o elemento revelado |
| Manter estável | `static camera`, `locked shot` | a ação que terá precedência |
| Alterar foco | `rack focus` | origem e destino do foco |

Evite rótulos vazios como `cinematic` ou `dynamic` quando não definirem enquadramento, trajetória, velocidade ou destino. Não use nomes de diretores, equipamentos ou resolução como atalho para direção visual.

## Ação e continuidade

- Descreva uma ação física com início, evolução e resultado: `she slowly turns toward the window and pauses`.
- Combine a ação com a câmera por uma relação temporal clara: `while the camera slowly pulls back to reveal the empty hall`.
- Limite a quantidade de mudanças relevantes ao tempo disponível. Uma sequência curta favorece uma ação contínua; não compacte levantar, caminhar, abrir uma porta e mudar de cenário em poucos segundos.
- Peça tomada contínua, cortes ou timestamps somente quando isso fizer parte da intenção e a plataforma suportar a forma escolhida.

## Luz, cor e atmosfera

Nomeie fontes e comportamento da luz em vez de adjetivos genéricos: `soft window light`, `side lighting with long shadows`, `warm highlights and muted neutral midtones`.

Use paleta e contraste apenas quando afetarem o resultado. Para reduzir excesso de saturação, descreva a intenção desejada, como `muted colors` ou `low contrast`, sem tratar o resultado como garantido.

## Áudio, diálogo e restrições

- Inclua fala literal entre aspas e indique o emissor e a intenção emocional quando houver diálogo.
- Mencione música, efeitos, legendas ou lip-sync apenas quando solicitados ou confirmados pela plataforma.
- Prefira uma condição descritiva à negação genérica: `clear blue sky` em vez de `no clouds`; `static camera` em vez de `do not move the camera`.
- Se houver campo negativo confirmado, liste somente artefatos ou exclusões materiais ao pedido.

## Estrutura temporal

Quando timestamps forem suportados e necessários, mantenha uma ação legível por intervalo e feche com invariantes globais.

```text
0-3s: <estado inicial e ação>
3-6s: <evolução contínua ou revelação>
Global continuity: <identidade, luz, cenário ou outra invariante relevante>
```

Não assuma que um modelo aceita timestamps, múltiplos cortes ou duração exata só porque o pedido os menciona.

---
name: engenharia-prompts-imagem
description: Use when someone asks to create, improve, adapt, compare, or debug a prompt for AI image generation or image editing, including photorealistic scenes, illustrations, ads, product images, UI mockups, infographics, reference-image edits, Midjourney, Stable Diffusion, Flux, ChatGPT Images, or GPT Image. Do not use merely to generate an image when the prompt is already approved.
---

# Engenharia de Prompts para Imagens

Transforme uma intenção visual em um prompt preciso e copiável. O objetivo é reduzir ambiguidade sem inventar requisitos e sem confundir a engenharia do prompt com a execução da imagem.

## Limite de responsabilidade

- Produza prompts; não gere, edite, salve ou publique imagens.
- Não prometa que um modelo preservará pixels, identidade, texto ou composição com perfeição.
- Trate recursos e sintaxes de plataformas como versionados. Só aplique um parâmetro quando a plataforma estiver identificada e ele for compatível.
- Se a pessoa já forneceu um prompt final aprovado e pede a imagem, encaminhe para a skill de geração de imagens disponível no runtime.

## Fluxo

1. Classifique o pedido: **geração**, **edição**, **adaptação entre plataformas**, **diagnóstico** ou **variações**.
2. Extraia do pedido o que já está definido: plataforma, uso, proporção, sujeito, ação, cenário, estilo, composição, luz, cores, texto literal, referências e restrições.
3. Pergunte apenas pelo que muda materialmente o resultado. Faça uma pergunta por vez; não repita informação já dada.
4. Estruture e entregue o prompt. Use inglês por padrão; mantenha o resumo do briefing em PT-BR.
5. Faça uma checagem final de conflitos, detalhes inventados, formato, texto literal, restrições e sintaxe da plataforma.

## Perguntas adaptativas

Pergunte somente se a lacuna impedir uma decisão visual relevante. Priorize nesta ordem:

| Situação | Pergunta útil |
| --- | --- |
| Plataforma ausente e houver sintaxe específica | “Em qual gerador você vai usar o prompt?” |
| Uso ou proporção ausente | “Onde a imagem será usada e qual proporção/formato você precisa?” |
| Sujeito ou ação vaga | “Qual é o sujeito principal e o que ele está fazendo?” |
| Edição sem alvo/referência visível | “Qual imagem será o alvo da edição e qual parte deve permanecer invariável?” |
| Texto na imagem | “Qual é o texto exato, incluindo acentos, maiúsculas e pontuação?” |

Se a plataforma não foi informada, produza um prompt agnóstico em linguagem natural e declare `Plataforma: a confirmar`; não invente flags.

## Construção do prompt

### Geração

Organize, quando relevante: sujeito concreto → ação → ambiente → meio/estilo → composição → iluminação → cor/clima → texto literal → restrições. Comece pelos elementos que não podem falhar. Use frases coesas, não uma lista de buzzwords.

Leia `references/linguagem-visual.md` quando precisar escolher ou explicar enquadramento, composição, luz, óptica, profundidade ou cor.

### Edição

Use este formato e peça a imagem-alvo caso ela não esteja disponível:

```text
Change: <uma alteração específica>.
Keep: <identidade, pose, enquadramento, perspectiva, iluminação e demais invariantes>.
Forbid: <adições, remoções ou artefatos a evitar>.
```

Faça uma mudança por prompt quando a preservação for crítica. Leia `references/padroes-e-anti-padroes.md` para preservar invariantes e evitar pedidos contraditórios.

### Adaptação de plataforma

Primeiro escreva um núcleo visual portátil. Depois adapte apenas a camada de sintaxe, parâmetros e negativos. Nunca copie flags de uma plataforma para outra.

Leia `references/plataformas.md` para Midjourney, Stable Diffusion e Flux. Leia `references/gpt-image-2-2-5.md` somente para ChatGPT Images ou GPT Image.

## Contrato de saída

Use exatamente esta ordem:

```markdown
## Diagnóstico
<tipo de pedido e plataforma>

## Briefing consolidado
- Uso: ...
- Formato: ...
- Direção visual: ...
- Referências e restrições: ...

## Prompt final (English)
```text
<prompt pronto para copiar>
```

## Suposições e limites
- <somente lacunas preenchidas ou limitações relevantes>
```

Quando adaptar para mais de uma plataforma, repita apenas a seção `Prompt final (English)` com um subtítulo por plataforma e mantenha um único briefing consolidado.

## Erros recorrentes

- Não adicione nacionalidade, idade, roupa, etnia, objetos, pose ou narrativa sem pedido explícito.
- Não use `8k`, `award-winning`, nomes de estúdio, câmeras ou lentes como substitutos da direção visual.
- Não trate uma proporção escrita no texto como parâmetro garantido: adapte-a à plataforma confirmada.
- Não use prompt negativo como remédio genérico; nomeie apenas artefatos ou exclusões relevantes.
- Não afirme que JSON, seed, pesos, busca web ou geração em lote são suportados sem confirmação da plataforma.

## Referências

- `references/linguagem-visual.md`: gramática visual para geração.
- `references/plataformas.md`: diferenças de adaptação por plataforma.
- `references/gpt-image-2-2-5.md`: ChatGPT Images e GPT Image.
- `references/padroes-e-anti-padroes.md`: diagnóstico, restrições e preservação em edição.

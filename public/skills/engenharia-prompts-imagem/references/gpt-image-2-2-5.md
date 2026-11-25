# ChatGPT Images e GPT Image 2.0–2.5

Esta referência cobre o uso conversacional de ChatGPT Images e os modelos GPT Image disponíveis no runtime. Consulte a documentação atual antes de converter recursos da interface em parâmetros de API.

## Capacidades confirmadas

ChatGPT Images permite criar uma imagem a partir de uma descrição e editar uma imagem gerada ou enviada. O pedido pode especificar texto, detalhes, transparência e proporção. Para uma edição localizada, descreva a área ou selecione-a na interface quando essa ferramenta estiver disponível.

Fonte primária: [Images in ChatGPT](https://help.openai.com/en/articles/11084440-im). Para o catálogo de modelos de API, consulte [Models](https://platform.openai.com/docs/models/gpt-4-turbo-and-gpt-4).

## Geração

Organize o pedido nesta ordem quando ela ajudar a precisão:

```text
Scene: <setting, atmosphere, lighting>.
Subject: <concrete subject and action>.
Important details: <spatial relations, materials, exact text>.
Medium: <photography, illustration, diagram, UI mockup>.
Constraints: <aspect ratio, exclusions, readability, transparency>.
```

Mantenha texto literal entre aspas. Se a imagem receber copy depois, peça espaço negativo em vez de texto de preenchimento.

## Edição

Use uma solicitação curta e isolada:

```text
Change: change only <target> to <result>.
Keep: preserve <explicit invariants>.
Forbid: do not add, remove, move, or alter <protected elements>.
```

Para alterações sucessivas, valide o resultado atual antes de pedir a próxima. Se houver degradação ou perda de referência, reenvie a melhor versão disponível e declare novamente as invariantes. Isso reduz deriva, mas não garante correspondência pixel a pixel.

## Não presumir

Não trate como garantidos números fixos de imagens por pedido, busca web, modo de raciocínio, JSON, controles de seed, 4K, ferramentas de máscara ou fidelidade de referência. Esses recursos dependem de produto, plano, modelo e interface e exigem confirmação atual.

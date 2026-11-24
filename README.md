# Skills Atomicas

Catálogo público das skills da Atomica, servido pelo GitHub Pages em <https://iarketinglabs.github.io/skills-atomicas/>. As páginas de área e de skill têm endereços próprios e a documentação pode ser lida sem JavaScript.

## Trabalhar no portal

Use Node.js 24 e execute:

```sh
npm ci
npm run dev
npm test
npm run build
```

O servidor de desenvolvimento utiliza o caminho `/skills-atomicas/`. O build gera o site em `dist/` e cria um ZIP por pacote. Cada ZIP contém os ficheiros enumerados no catálogo, incluindo a licença. As imagens e fontes do portal estão separadas dos pacotes de skills.

## Catálogo público

O processo de promoção envia para este repositório apenas versões revistas. O manifesto `src/data/catalog.json` contém as categorias e as fichas aprovadas; os ficheiros de cada pacote ficam em `public/skills/<id>/`. Pedidos de inclusão e revisões de conteúdo são preparados em privado.

Referências externas sem autorização de redistribuição apresentam apenas a identificação e a ligação ao repositório original. A licença de cada pacote é disponibilizada na respetiva ficha e no próprio pacote.

O workflow valida o catálogo, executa os testes, constrói o site e entrega o artefacto de `main` ao ambiente `github-pages`.

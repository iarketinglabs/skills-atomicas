# Perfil visual de apresentações

## Perfil do canvas

Valores em pixels referem-se ao canvas lógico, antes da escala proporcional. Este perfil é independente de qualquer apresentação; ajuste a composição dentro da área segura sem reduzir fontes para acomodar excesso de texto.

| Papel | Valor |
|---|---|
| Canvas | 1920 × 1080; 16:9 |
| Margens de conteúdo | topo 150; laterais 150; base 130 |
| Marca | esquerda 150; topo 44; símbolo isolado 52 × 52 |
| Contador | direita 150; topo 52; 26px |
| Rodapé | laterais 150; base 48; 24px |
| Título | Bebas Neue 124px; peso 400; linha .98; tracking .01em |
| Etiqueta | Oswald 28px; tracking .18em; maiúsculas |
| Subtítulo | Jost 40px; linha 1.35 |
| Corpo | Jost 34px; linha 1.35 |
| Card | papel; borda 2px creme; raio 28px; padding 44px 48px |
| Título de card | Bebas Neue 64px; linha 1 |
| Texto de card | Jost 32px; linha 1.35 |
| Fonte de evidência | Jost 22px |
| Métrica de grande destaque | Bebas Neue; referência original 250px |

| Token | Valor |
|---|---|
| cream-100 / cream-300 | #FCF9F2 / #E5DBC7 |
| g900 / g700 / g500 / g300 | #1B1B1B / #3D3D3D / #686868 / #A9A9A9 |
| cyan-900 / cyan-700 / cyan-500 / cyan-100 | #005F64 / #008C94 / #67BBC0 / #E0F2F3 |
| yellow-500 / yellow-100 | #FCCA29 / #FEF8E4 |
| red-700 / red-500 | #D1283F / #FF304C |
| pulp / paper / solar | #F7EED7 / #FBF6E9 / #FCCA29 |

Texto principal e bordas estruturais são grafite; ciano organiza e destaca; amarelo marca um foco; vermelho fica reservado a alerta ou série de dados. Evite branco sobre ciano. Use a retícula em CSS para dar textura ao papel creme. Os cards ciano usam retícula sutil. Símbolo e divisor devem manter proporção.

A marca institucional escreve-se Atomica. O header combina símbolo decorativo isolado e nome. Quando aplicável, AndROI conserva a caixa com `ROI` em Libre Baskerville local, negrito e itálico; não aplique uppercase ao nome. A serifada é uma exceção de marca, não substitui as fontes do corpo ou dos títulos.

## Movimento observado e adaptação

Revelação .7s com deslocamento de 22px e curva `cubic-bezier(.16,1,.3,1)`. Barra superior de 12px, largura proporcional à posição, transição .8s e fluxo luminoso discreto. Movimento reduzido e impressão deixam tudo no estado final. Animação nunca é necessária para entender números. Navegação reversa e salto ao fim devem atualizar a largura corretamente.

## Diferenças deliberadas

O perfil de apresentações usa Bebas Neue, cards de borda 2px com raio 28px e nenhuma sombra dura obrigatória. Não misture silenciosamente outros perfis de website, fontes ou estilos de cards.

## Recomendações novas do template

Métricas em cards usam 150px para acomodar três colunas; títulos podem ter até duas linhas, com área reservada de 244px no layout padrão. Cronogramas e imagens usam geometria própria. Gráficos de barras têm escala comum; equipe usa iniciais quando não há fotos autorizadas. Divida slides densos. Não faça texto longo caber reduzindo fonte; adapte largura, título, padding ou sequência.

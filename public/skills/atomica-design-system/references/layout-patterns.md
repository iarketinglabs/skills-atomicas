# Padrões de Layout — Átomica

Tokens e padrões para páginas web Atomica. Adapte o componente à rota e ao conteúdo confirmados.

---

## 1. Container (confirmado)

```css
.container {
  width: min(100% - 64px, 1420px);
  margin-inline: auto;
}

@media (max-width: 760px) {
  .container { width: min(100% - 28px, 1420px); }
}
```

Isto **substitui** qualquer sistema de `max-width` fixo em rem (`48rem`/`64rem`/`72rem`/`80rem`) de versões anteriores desta skill — o real é uma única largura máxima (`1420px`) com margem lateral fluida via `min()`, sem níveis intermediários de container.

## 2. Section (confirmado)

```css
.section {
  padding: 72px 0;
}

@media (max-width: 760px) {
  .section { padding: 52px 0; }
}
```

Diferente de versões anteriores, `.section` **não** define `background-color` fixo — o fundo vem do body (creme com textura, ver §3) ou de uma variante explícita (`.section-cyan`, `.section-yellow`, ver abaixo). Não existe uma segunda escala `.section-lg`/`.section-md` com paddings diferentes — é um valor único (`72px`/`52px`).

### 2.1 Variantes de fundo (confirmado)

```css
.section-cyan {
  background:
    linear-gradient(rgba(99, 190, 194, 0.5), rgba(99, 190, 194, 0.5)),
    var(--texture-pulp);
  background-size: auto, 8px 8px;
}

.section-yellow {
  background:
    linear-gradient(rgba(247, 197, 40, 0.5), rgba(247, 197, 40, 0.5)),
    var(--texture-pulp);
  background-size: auto, 8px 8px;
}
```


## 3. Textura Pulp — técnica real de camada dupla


```css
:root {
  --texture-pulp: radial-gradient(rgba(27, 27, 27, .09) .7px, transparent 1px);
}

body {
  background:
    linear-gradient(rgba(247, 239, 217, 0.70), rgba(247, 239, 217, 0.70)),
    var(--texture-pulp);
  background-size: auto, 8px 8px;
}
```

Padrão: **duas camadas de `background`**, separadas por vírgula — primeiro um `linear-gradient` do mesmo tom repetido duas vezes (isso cria uma cor sólida translúcida, não um gradiente visual), depois a imagem de textura. Nunca `opacity` isolado na textura, nunca `background-blend-mode: multiply` (a única exceção confirmada é `.machinery-strip::after`, só na LP Consultoria B2B, que usa `mix-blend-mode: soft-light` para uma faixa decorativa específica — não generalize isso).

A retícula CSS do pacote usa células de `8px 8px` em fundos, cabeçalhos e cards. Se substituir a retícula por uma imagem autorizada, ajuste o tamanho de repetição à escala da superfície e teste a legibilidade.

A opacidade do tint (o valor alfa do `rgba()` na camada de gradiente) também varia por contexto — vai de `0.5` (seções coloridas) a `0.8` (cards) a `0.9` (header, mais opaco para garantir contraste do texto). Não fixe um único valor de opacidade para todas as superfícies.


## 4. Arquitetura de Camadas — Fundo de Partículas (confirmado, já estava correto)

```
body (fundo pulp/creme, sempre opaco, mesmo antes do JS montar)
  → .page-shell (position: relative; isolation: isolate; overflow: hidden)
      → .particle-stage (position: fixed; inset: 0; z-index: 0; pointer-events: none)
      → .page-content (position: relative; z-index: 2)
```

Ver `atomica-particle-field` para o componente completo. O ponto que já estava certo nesta skill: o conteúdo real fica **transparente de propósito**, deixando o fundo/partículas aparecerem nos espaços entre cards — cada card/seção que precisa de superfície opaca define seu próprio fundo (`.poster-card`, `.section-cyan` etc.), não a `.page-content` inteira.

## 5. Responsividade

Para o padrão de cabeçalho de seção, veja [Especificações de componentes](component-specs.md).

1. `.container` reduz a margem lateral (`64px` → `28px`).
2. `.section` reduz padding vertical (`72px` → `52px`).
3. `.section-title h2` reduz de tamanho (ver `typography-guide.md`).
4. `.tilt-left`/`.tilt-right`/`.tilt-soft` zeram.
5. Sombras de card colapsam para `5px 5px 0 var(--gunmetal)` uniformemente.
6. `.atomica-button` vira `width: 100%` e reduz a fonte.
7. A preferência de movimento reduzido esconde `.particle-stage`, independentemente da largura.

## 6. Z-Index

| Camada | Valor |
|---|---|
| `.particle-stage` | `0` |
| `.page-content` | `2` |
| Header sticky | `20` (convenção observada, não documentada explicitamente em variável) |
| Banner de cookies / modal (se implementado) | `50` (extrapolação — sem exemplo shippado) |

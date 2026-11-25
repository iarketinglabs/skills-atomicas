# Tipografia — Átomica

Guia de hierarquia tipográfica para páginas web Atomica. Os aliases de CSS permitem encaixar fontes autorizadas sem alterar nomes internos dos binários.

---

## 1. Mecanismo de Carregamento — self-hosted `@font-face`, com nomes prefixados


Os caminhos abaixo são exemplos do projeto de destino. Adicione apenas regras para fontes autorizadas e já presentes no projeto. O perfil principal pode usar uma Atomica Script autorizada, ou Caprasimo como alternativa. Os fallbacks mantêm a interface utilizável com fontes de sistema.

```css
@font-face {
  font-family: "Atomica Jost";
  src: url("/assets/fonts/Jost-VariableFont_wght.ttf") format("truetype");
  font-weight: 100 900;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Atomica Oswald";
  src: url("/assets/fonts/Oswald-VariableFont_wght.ttf") format("truetype");
  font-weight: 200 700;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Atomica Caprasimo";
  src: url("/assets/fonts/Caprasimo-Regular.ttf") format("truetype");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Atomica Bebas";
  src: url("/assets/fonts/BebasNeue-Regular.ttf") format("truetype");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Atomica Swanky";
  src: url("/assets/fonts/FontdinerSwanky-Regular.ttf") format("truetype");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```


## 2. Fonte por Papel — stacks reais

A interface usa Atomica Script quando fornecida com licença e Caprasimo como alternativa. Bebas identifica labels e botões, com Oswald como fallback.

| Papel | Classe/seletor real | Stack | Peso | Transform |
|---|---|---|---|---|
| Headline principal (h1, hero) | `.hero-title-tilt` / `.font-display` | `"Atomica Script", "Atomica Caprasimo", serif` | 400 | none |
| Título de seção (h2) | `.section-title h2` | `"Atomica Script", "Atomica Caprasimo", serif` | 400 | none |
| Labels, botões, tags | `.font-label`, `.atomica-button` | `"Atomica Bebas", "Atomica Oswald", sans-serif` | 600 (label) / 700 (botão) | uppercase |
| Eyebrow (categoria acima do título) | `.eyebrow` | `"Atomica Oswald", sans-serif` | 700 | uppercase |
| Wordmark da marca ("Atomica") | `.brand-wordmark` | `"Atomica Swanky", "Atomica Caprasimo", serif` | 400 | none — leva `text-shadow: 3px 3px 0 var(--ciano-light)` (footer usa `var(--ciano-dark)`) |
| Label de campo de formulário | `.field label` | `"Atomica Oswald", sans-serif` | 600 | uppercase |
| Corpo | `body`, `p` | `"Atomica Jost", sans-serif` | 400 (texto), 600–700 quando precisa de peso | none |

Regra que se mantém: **corpo sempre em Jost — nunca misture fontes no mesmo parágrafo.**

## 3. Tamanhos confirmados

| Elemento | Desktop | Mobile (≤760px) |
|---|---|---|
| `.hero-title-tilt` | `clamp(2.4rem, 5.5vw, 4.4rem)` (varia por hero específico, mas sempre `clamp()` responsivo — nunca um valor fixo único) | mesmo `clamp`, a inclinação reduz de `-1.1deg` para `-0.65deg` |
| `.section-title h2` | `3.1rem`–`3.45rem` conforme o projeto | `2.15rem`–`2.35rem` |
| `.eyebrow` | `1.2rem`–`1.35rem` | mesmo |
| `.atomica-button` (texto) | `1.45rem` | `1.15rem` |
| `.field label` | `0.86rem` | mesmo |
| Corpo | `1rem` | mesmo, ajustar por contexto |

`line-height` do `.section-title h2` é `1.08` — bem mais compacto que corpo de texto, típico de headline retrô "empilhado".

## 4. Inclinação como efeito tipográfico (real, substitui "outline stroke"/"vintage distress")


```css
.hero-title-tilt {
  display: inline-block;
  transform: rotate(-1.1deg);
  transform-origin: 52% 58%;
}

.tilt-left  { transform: rotate(-0.85deg); }
.tilt-right { transform: rotate(0.85deg); }
.tilt-soft  { transform: rotate(-0.45deg); }
```

Em mobile (`max-width: 760px`), `.tilt-left`/`.tilt-right`/`.tilt-soft` são **zeradas** (`transform: none`) e `.hero-title-tilt` reduz para `rotate(-0.65deg)` — a inclinação forte só faz sentido em telas largas.

Um efeito de sombra real que existe (não confundir com o acima): o `.brand-wordmark` usa `text-shadow: 3px 3px 0 var(--ciano-light)` (ou `var(--ciano-dark)` na variante de footer) — isso é específico do logotipo textual, não um padrão geral de headline.

## 5. Regras de Aplicação

1. Headline principal e título de seção sempre em `"Atomica Script", "Atomica Caprasimo", serif` — nunca Bebas ou Oswald nesses papéis.
2. Labels, botões e tags sempre em `"Atomica Bebas", "Atomica Oswald", sans-serif`, uppercase.
3. Eyebrow (a linha pequena acima de um título de seção) é `"Atomica Oswald"` sozinho, sem Bebas.
4. Corpo sempre em `"Atomica Jost"` — nunca misture fontes no mesmo parágrafo.
5. O efeito retrô de headline vem de inclinação (`.hero-title-tilt`/`.tilt-*`), não de contorno ou sombra decorativa.

## 6. Responsividade Tipográfica

- `.section-title h2` reduz para `2.15rem`–`2.35rem`.
- `.hero-title-tilt` mantém o mesmo `clamp()` (já é fluido) mas reduz a inclinação.
- `.tilt-left`/`.tilt-right`/`.tilt-soft` zeram.
- Sombras de card colapsam (ver `design-tokens.md` §8) — não é tipografia, mas acontece no mesmo breakpoint, vale lembrar ao implementar.

# Especificações de Componentes — Átomica

Amostras internas de projeto foram anonimizadas nesta versão pública.

---

## 1. Botões — `.atomica-button` (confirmado)

### 1.1 Base (aplica-se a todas as variantes)

```css
.atomica-button {
  display: inline-flex;
  min-height: 48px;
  align-items: center;
  justify-content: center;
  gap: 10px;
  border: 3px solid var(--gunmetal);
  border-radius: var(--radius);
  padding: 14px 22px;
  background: var(--ciano);
  color: var(--gunmetal);
  font-family: "Atomica Bebas", "Atomica Oswald", sans-serif;
  font-size: 1.45rem;
  font-weight: 700;
  text-transform: uppercase;
  text-decoration: none;
  cursor: pointer;
  box-shadow: 7px 7px 0 var(--gunmetal);
  transition: transform 160ms ease, box-shadow 160ms ease, background-color 160ms ease;
}

.atomica-button:hover {
  transform: translate(-2px, -2px);
  background: var(--ciano-light); /* #a8dee0 */
  color: var(--gunmetal);
  box-shadow: 9px 9px 0 var(--gunmetal);
}

.atomica-button:disabled {
  cursor: not-allowed;
  opacity: 0.55;
  transform: none;
  box-shadow: 7px 7px 0 var(--gunmetal);
}
```

**Correção importante em relação a versões anteriores desta skill**: o botão primário usa **texto `var(--gunmetal)` (escuro), não branco**, sobre fundo `var(--ciano)`. Texto branco sobre `#63bec2` reprova WCAG AA (contraste medido ≈2.2:1); texto gunmetal sobre a mesma cor passa com folga. Isso não é uma escolha estética — é a correção de um bug de contraste real encontrado ao auditar um projeto que copiou a versão antiga desta skill.

### 1.2 Modificadores reais (só existem estes três)

```css
.atomica-button.secondary { background: var(--amarelo); color: var(--gunmetal); }
.atomica-button.dark      { background: var(--gunmetal); color: var(--creme-100); }
.atomica-button.outline   { background: var(--creme-100); color: var(--gunmetal); }
```

Amostras internas de projeto foram anonimizadas nesta versão pública.

### 1.3 Mobile (`max-width: 760px`)

```css
.atomica-button {
  width: 100%;
  font-size: 1.15rem;
}
```

---

## 2. Cards (confirmado)

Nomenclatura real: `.poster-card`, `.poster-card-cyan`, `.poster-card-yellow`, `.image-frame` — **não** "Card Padrão/Destaque/Bônus/Missão/Preço" como em versões anteriores desta skill.

```css
.poster-card {
  border: 3px solid var(--gunmetal);
  border-radius: var(--radius);
  background:
    linear-gradient(rgba(247, 239, 217, 0.78), rgba(247, 239, 217, 0.78)),
    var(--texture-pulp);
  background-size: auto, 640px auto;
  box-shadow: 7px 7px 0 var(--amarelo);
}

.poster-card-cyan {
  border: 3px solid var(--gunmetal);
  border-radius: var(--radius);
  background:
    linear-gradient(rgba(247, 239, 217, 0.8), rgba(247, 239, 217, 0.8)),
    var(--texture-pulp);
  background-size: auto, 640px auto;
  box-shadow: 12px 12px 0 var(--ciano);
}

.poster-card-yellow {
  border: 3px solid var(--gunmetal);
  border-radius: var(--radius);
  background:
    linear-gradient(rgba(247, 239, 217, 0.8), rgba(247, 239, 217, 0.8)),
    var(--texture-pulp);
  background-size: auto, 640px auto;
  box-shadow: 7px 7px 0 var(--amarelo);
}

.image-frame {
  overflow: hidden;
  border: 4px solid var(--gunmetal);
  border-radius: 18px;
  background:
    linear-gradient(rgba(247, 239, 217, 0.72), rgba(247, 239, 217, 0.72)),
    var(--texture-pulp);
  background-size: auto, 640px auto;
  box-shadow: 14px 14px 0 var(--ciano);
}

.image-frame-yellow { box-shadow: 12px 12px 0 var(--amarelo); }
```

Amostras internas de projeto foram anonimizadas nesta versão pública.

**Mobile (`max-width: 760px`)**: toda sombra de `.poster-card`/`.poster-card-cyan`/`.poster-card-yellow`/`.image-frame` colapsa para `box-shadow: 5px 5px 0 var(--gunmetal)`.

### 2.1 Variante só confirmada na LP Consultoria B2B — `.mechanism-card`

```css
.mechanism-card {
  position: relative;
  z-index: 1;
  display: grid;
  grid-template-rows: auto auto 1fr;
  border: 3px solid var(--gunmetal);
  border-radius: 18px;
  background:
    linear-gradient(rgba(247, 239, 217, 0.76), rgba(247, 239, 217, 0.76)),
    var(--texture-pulp);
  background-size: auto, 640px auto;
  box-shadow: 8px 8px 0 var(--ciano);
}
```
Usado dentro de `.mechanism-machine` (uma faixa decorativa horizontal atrás dos cards — ver B2B para o padrão completo se for replicar).

---

## 3. Cabeçalho de Seção — `.eyebrow` + `.section-title` + `.retro-divider` (confirmado, sem equivalente em versões anteriores)

Amostras internas de projeto foram anonimizadas nesta versão pública.

```css
.eyebrow {
  color: var(--ciano-dark);
  font-family: "Atomica Oswald", sans-serif;
  font-weight: 700;
  text-transform: uppercase;
  font-size: 1.2rem; /* até 1.35rem em alguns projetos */
}

.section-title { max-width: 780px; }

.section-title h2 {
  margin: 10px 0 0;
  font-family: "Atomica Script", "Atomica Caprasimo", serif;
  font-size: 3.1rem; /* 3.45rem em alguns projetos */
  line-height: 1.08;
}

.script-red { color: var(--vermelho); } /* usado para destacar uma palavra dentro do título */

.retro-divider {
  position: relative;
  height: 18px;
  margin-top: 12px;
}
.retro-divider::before {
  content: "";
  position: absolute;
  left: 0; right: 0; top: 8px;
  height: 3px;
  background: var(--ciano-dark);
}
.retro-divider::after {
  content: "";
  position: absolute;
  left: 48%; top: 2px;
  width: 15px; height: 15px;
  border: 3px solid var(--ciano-dark);
  border-radius: 999px;
  background: var(--creme-100);
}
```

Ordem de leitura de uma seção: ícone/ornamento decorativo (opcional) → `.eyebrow` (categoria) → `.section-title h2` (título, com uma palavra em `.script-red` quando fizer sentido) → parágrafo de introdução.

Mobile (`≤760px`): `.section-title h2` reduz para `2.15rem`–`2.35rem`.

---

## 4. Formulários / Inputs — `.field` / `.field-control` (confirmado)

```css
.field { display: grid; gap: 6px; }

.field label,
.field legend {
  font-family: "Atomica Oswald", sans-serif;
  font-weight: 600;
  text-transform: uppercase;
  font-size: 0.86rem;
}

.field-control {
  width: 100%;
  border: 2px solid rgba(27, 27, 27, 0.78);
  border-radius: 4px;
  background: var(--creme-100);
  padding: 12px 14px;
  color: var(--gunmetal);
  outline: none;
}

.field-control:focus {
  box-shadow: 0 0 0 3px rgba(103, 187, 192, 0.36);
}

.field-control[aria-invalid="true"] {
  background: #ffe5e8;
  border-color: var(--vermelho);
}

.error-text {
  color: #b8122b;
  font-size: 0.86rem;
  font-weight: 700;
}
```

Note que o radius de input (`4px`) é bem menor que o de card/botão (`12px`, `var(--radius)`) — não use `var(--radius)` em campo de formulário, é um valor próprio.

### 4.1 Indicador de etapas — `.step-indicator` (confirmado, formulário de lead progressivo)

```css
.step-indicator { display: flex; align-items: center; gap: 0; margin-bottom: 24px; }
.step-indicator-item { display: flex; flex-direction: column; align-items: center; gap: 6px; flex: 1; }

.step-circle {
  display: flex; align-items: center; justify-content: center;
  width: 36px; height: 36px;
  border-radius: 50%;
  border: 2px solid var(--gunmetal);
  font-family: "Atomica Bebas", "Atomica Oswald", sans-serif;
  font-size: 1.05rem; font-weight: 700;
  background: var(--creme-100); color: var(--gunmetal);
  transition: background 0.22s ease, color 0.22s ease, border-color 0.22s ease;
}
.step-circle.active    { background: var(--ciano); box-shadow: 2px 2px 0 var(--gunmetal); }
.step-circle.completed { background: var(--gunmetal); color: var(--creme-100); }

.step-label {
  font-size: 0.72rem; font-weight: 700; text-transform: uppercase;
  color: var(--gunmetal-700); text-align: center; opacity: 0.6;
  transition: opacity 0.22s ease;
}
.step-label.active    { opacity: 1; color: var(--gunmetal); }
.step-label.completed { opacity: 0.9; }

.step-connector-wrap { flex: 1; padding-bottom: 22px; display: flex; align-items: center; }
.step-connector { height: 2px; width: 100%; background: var(--creme-300); transition: background 0.3s ease; }
.step-connector.completed { background: var(--gunmetal); }

@keyframes step-slide-in      { from { opacity: 0; transform: translateX(28px); }  to { opacity: 1; transform: translateX(0); } }
@keyframes step-slide-in-back { from { opacity: 0; transform: translateX(-28px); } to { opacity: 1; transform: translateX(0); } }
.step-enter      { animation: step-slide-in 0.26s ease both; }
.step-enter-back { animation: step-slide-in-back 0.26s ease both; }

@media (prefers-reduced-motion: reduce) {
  .step-enter, .step-enter-back { animation: none; }
}
```

Use com um formulário de várias etapas onde `key={etapaAtual}` no React remonta o wrapper para disparar a animação de entrada correta (`.step-enter` avançando, `.step-enter-back` voltando).

---

## 5. Microanimação de Entrada por Scroll — `.scroll-reveal` (confirmado)

```css
.scroll-reveal {
  opacity: 0;
  transform: translateY(28px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}
.scroll-reveal-visible { opacity: 1; transform: translateY(0); }

@media (prefers-reduced-motion: reduce) {
  .scroll-reveal { opacity: 1; transform: none; transition: none; }
}
```

A classe `.scroll-reveal-visible` é adicionada via `IntersectionObserver` (dispara uma única vez, `threshold: 0.15`), não via CSS puro — implemente o componente React/JS que observa o elemento e alterna a classe. **Auditoria visual**: um screenshot de página inteira tirado sem rolar antes vai capturar esse conteúdo com `opacity: 0`, porque o observer nunca disparou — role a página em incrementos antes de capturar.

## 6. Inclinações decorativas — `.tilt-*` (confirmado)

```css
.tilt-left  { transform: rotate(-0.85deg); }
.tilt-right { transform: rotate(0.85deg); }
.tilt-soft  { transform: rotate(-0.45deg); }

@media (max-width: 760px) {
  .tilt-left, .tilt-right, .tilt-soft { transform: none; }
}
```

Aplique a `.image-frame`/`.poster-card` isolados para quebrar o alinhamento rígido do grid — não abuse, 1-2 elementos inclinados por seção é o padrão observado.

---

## 7. Tags / Badges (extrapolação — sem exemplo shippado)

Amostras internas de projeto foram anonimizadas nesta versão pública.

```css
.tag {
  background: var(--amarelo-soft);
  color: var(--gunmetal);
  border: 1px solid var(--amarelo);
  border-radius: 9999px;
  padding: 0.25rem 0.75rem;
  font-family: "Atomica Oswald", sans-serif;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
}
```

## 8. Imagens e Mídia (confirmado, além de `.image-frame` da seção 2)

### 8.1 Facade de vídeo — `.video-facade` (confirmado)

```css
.video-facade {
  position: relative; width: 100%; aspect-ratio: 16 / 9;
  overflow: hidden; border: 3px solid var(--gunmetal); border-radius: 14px;
  background: var(--gunmetal); cursor: pointer;
}
.video-facade iframe { position: absolute; inset: 0; width: 100%; height: 100%; border: 0; }
.video-facade-play { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; }
.video-facade-play-icon {
  display: flex; align-items: center; justify-content: center;
  width: 64px; height: 64px; border-radius: 50%;
  border: 3px solid var(--gunmetal); background: var(--amarelo);
  box-shadow: 5px 5px 0 var(--gunmetal);
  transition: transform 160ms ease;
}
.video-facade:hover .video-facade-play-icon { transform: scale(1.08); }
```

O iframe só é montado no DOM depois do clique — antes disso, mostra a `.video-facade-play-icon` sobre uma thumbnail estática.

### 8.2 Avatar / retrato circular (extrapolação a partir de `.image-frame`)

```css
.avatar {
  border-radius: 9999px;
  border: 2px solid var(--gunmetal);
  object-fit: cover;
}
```

---

## 9. Navegação (extrapolação parcial)

Amostras internas de projeto foram anonimizadas nesta versão pública.

## 10. Modais, Toasts, Tabelas, Accordion (extrapolação — sem exemplo shippado)

Amostras internas de projeto foram anonimizadas nesta versão pública.

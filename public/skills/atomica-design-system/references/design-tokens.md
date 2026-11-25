# Design Tokens — Átomica

Amostras internas de projeto foram anonimizadas nesta versão pública.

---

## 1. Paleta de Cores Real

Amostras internas de projeto foram anonimizadas nesta versão pública.

```css
:root {
  --creme-100: #f7efd9;
  --creme-200: #f3e8cc;
  --creme-300: #dbc9a6;
  --gunmetal: #1b1b1b;
  --gunmetal-700: #3d3d3d;
  --ciano: #63bec2;
  --ciano-dark: #137a80;
  --ciano-soft: #e0f2f3;
  --ciano-light: #a8dee0;   /* token novo — ver nota abaixo */
  --amarelo: #f7c528;
  --amarelo-soft: #fef8e4;
  --vermelho: #b8302f;
  --radius: 12px;
  --texture-pulp: url("/assets/textures/pulp.papper-background.png");
}
```

Amostras internas de projeto foram anonimizadas nesta versão pública.

### 1.2 Tabela de uso

| Token | Hex | Uso confirmado no código real |
|---|---|---|
| `--creme-100` | `#f7efd9` | Fundo principal (body, cards) |
| `--creme-200` | `#f3e8cc` | Variação de fundo |
| `--creme-300` | `#dbc9a6` | Bordas sutis, divisórias |
| `--gunmetal` | `#1b1b1b` | Texto principal, bordas de card/botão, fundo escuro |
| `--gunmetal-700` | `#3d3d3d` | Texto secundário |
| `--ciano` | `#63bec2` | Cor de ação primária (botão, sombra de destaque) |
| `--ciano-dark` | `#137a80` | Hover de link, cor do `.eyebrow`, wordmark no footer |
| `--ciano-soft` | `#e0f2f3` | Fundo de blocos de destaque sutis |
| `--ciano-light` | `#a8dee0` | Hover do botão primário, sombra do wordmark |
| `--amarelo` | `#f7c528` | Destaque visual, sombra de card `.poster-card`/`.poster-card-yellow` |
| `--amarelo-soft` | `#fef8e4` | Fundo de seções de alerta/destaque |
| `--vermelho` | `#b8302f` | Texto de acento (`.script-red`), erro de campo |
| `--radius` | `12px` | Raio padrão de card e botão |

### 1.3 Correspondência com a versão anterior desta skill (para migrar código antigo)

Esta skill documentava, até a correção, um sistema de ramp que **não corresponde ao que foi de fato construído**. Se você está migrando um projeto que já usa os tokens antigos, esta é a tradução:

| Token antigo (não usar mais) | Hex antigo | → | Token real | Hex real | Mudou? |
|---|---|---|---|---|---|
| `color-creme-100` | `#FCF9F2` | → | `--creme-100` | `#f7efd9` | Sim |
| `color-creme-200` | `#F5F5F0` | → | `--creme-200` | `#f3e8cc` | Sim |
| `color-creme-300` | `#E5DBC7` | → | `--creme-300` | `#dbc9a6` | Sim |
| `color-gunmetal-900` | `#1B1B1B` | → | `--gunmetal` | `#1b1b1b` | **Não** (só o nome) |
| `color-gunmetal-700` | `#3D3D3D` | → | `--gunmetal-700` | `#3d3d3d` | **Não** (só o nome) |
Amostras internas de projeto foram anonimizadas nesta versão pública.
| `color-ciano-900` | `#006B70` (esta skill) ou `#005F64` (`atomica-key-visuals`, também corrigido) | → | `--ciano-dark` | `#137a80` | Sim — **nenhuma das duas versões antigas estava certa** |
| `color-ciano-700` | `#008C94` | → | *(sem equivalente)* | — | Removido — o sistema real só tem 3 tons de ciano |
| `color-ciano-500` | `#67BBC0` | → | `--ciano` | `#63bec2` | Sim, ligeiramente |
| `color-ciano-300` | `#A8DEE0` | → | `--ciano-light` | `#a8dee0` | **Não** (valor idêntico, ganhou nome de token) |
| `color-ciano-100` | `#E0F2F3` | → | `--ciano-soft` | `#e0f2f3` | **Não** (valor idêntico, só o nome) |
| `color-amarelo-500` | `#FCCA29` | → | `--amarelo` | `#f7c528` | Sim |
| `color-amarelo-300` | `#FDE68A` | → | *(sem equivalente)* | — | Removido |
| `color-amarelo-100` | `#FEF8E4` | → | `--amarelo-soft` | `#fef8e4` | **Não** (valor idêntico, só o nome) |
| `color-vermelho-500` | `#FF304C` | → | `--vermelho` | `#b8302f` | Sim, bastante — o antigo é rosa-vermelho vibrante, o real é vermelho tijolo escuro |
| `color-vermelho-300` / `-100` | `#FF8C9B` / `#FFE5E8` | → | *(sem equivalente)* | — | Removidos |

Se algum componente desta skill (seções sem equivalente real confirmado, como modais, toasts, tabelas) ainda referenciar um dos tokens da coluna esquerda, trate como uma extensão não confirmada no código shippado — aplique a cor real mais próxima da tabela acima, não o hex antigo.

---

## 2. Tipografia — Tamanhos

Ver `references/typography-guide.md` para a tabela completa com fonte por papel. Os tamanhos abaixo são os confirmados no código real (desktop / mobile ≤760px):

| Elemento | Desktop | Mobile |
|---|---|---|
| `.hero-title-tilt` (h1) | `clamp(2.4rem, 5.5vw, 4.4rem)` | tilt reduzido, mesmo `clamp` |
| `.section-title h2` | `3.1rem`–`3.45rem` (varia por projeto) | `2.15rem`–`2.35rem` |
| `.eyebrow` | `1.2rem`–`1.35rem` | mesmo |
| `.font-label` (labels, botões) | `1.45rem` em botão; menor em label de campo | reduz proporcionalmente |
| `.field label` | `0.86rem` | mesmo |
| Corpo (`body`) | `1rem` | mesmo |

## 3. Line Heights

| Token | Valor | Uso |
|---|---|---|
| `leading-tight` | `1.08`–`1.25` | Headlines (`.section-title h2` usa `1.08`) |
| `leading-normal` | `1.5` | Corpo de texto padrão |
| `leading-relaxed` | `1.6`–`1.7` | Parágrafos longos |

## 4. Letter Spacing

Amostras internas de projeto foram anonimizadas nesta versão pública.

## 5. Espaçamento

| Token | Valor | Uso |
|---|---|---|
| `space-1` | `0.25rem` (4px) | Micro-espaçamentos |
| `space-2` | `0.5rem` (8px) | Gaps pequenos, ícones |
| `space-3` | `0.75rem` (12px) | — |
| `space-4` | `1rem` (16px) | Base unit |
| `space-6` | `1.5rem` (24px) | Gap de grid padrão |
| `space-8` | `2rem` (32px) | Gap de grid amplos |

## 6. Padding de Sections (real)

| Token | Valor | Uso |
|---|---|---|
| `section-py` | `72px 0` | `.section` padrão (não 4rem/5rem como versões antigas) |
| `section-py-mobile` | `52px 0` | `.section` em `max-width: 760px` |

Ver `references/layout-patterns.md` para o `.container` real (`min(100% - 64px, 1420px)`, não um `max-width` fixo em rem).

## 7. Formas e Bordas (real)

| Token | Valor | Uso confirmado |
|---|---|---|
| `--radius` | `12px` | Botões e `.poster-card`/`.poster-card-cyan`/`.poster-card-yellow` |
| Radius de `.image-frame` | `18px` (hardcoded, não `var(--radius)`) | Molduras de imagem em destaque |
| Radius de `.image-frame-clean` | `14px` (hardcoded) | Molduras de imagem menores |
| Radius de `.machinery-strip` | `22px` (hardcoded) | Faixa decorativa (só confirmado na LP Consultoria B2B) |
| `border-width` de card (`.poster-card*`) | `3px` (não 2px) | Todas as variantes de poster-card |
| `border-width` de `.image-frame` | `4px` | Molduras de imagem |
| `border-width` de `.atomica-header` | `2px` (só `border-bottom`) | Header |
| `border-color` padrão | `var(--gunmetal)` (`#1b1b1b`) | Todas as bordas estruturais |

## 8. Sombras — Estilo Offset Retrô (real)

Amostras internas de projeto foram anonimizadas nesta versão pública.

| Elemento | Sombra | Hover |
|---|---|---|
| `.poster-card` | `7px 7px 0 var(--amarelo)` | — |
| `.poster-card-cyan` | `12px 12px 0 var(--ciano)` | — |
| `.poster-card-yellow` | `7px 7px 0 var(--amarelo)` | — |
| `.image-frame` | `14px 14px 0 var(--ciano)` | — |
| `.image-frame-yellow` | `12px 12px 0 var(--amarelo)` | — |
| `.mechanism-card` (só B2B) | `8px 8px 0 var(--ciano)` | — |
| `.machinery-strip` (só B2B) | `12px 12px 0 rgba(247,197,40,.9)` | — |
| `.atomica-button` | `7px 7px 0 var(--gunmetal)` | `translate(-2px,-2px)` + `9px 9px 0 var(--gunmetal)` |
| `.atomica-header` | `0 3px 0 rgba(27,27,27,.12)` | — |

Amostras internas de projeto foram anonimizadas nesta versão pública.

## 9. Z-Index (confirmado no `.page-shell`/partículas)

| Token | Valor | Uso |
|---|---|---|
| `z-base` (`.page-shell`) | posição de referência | Wrapper isolado (`isolation: isolate`) |
| `.particle-stage` | `0` | Canvas de partículas, fixo |
| `.page-content` | `2` | Conteúdo real da página |
| header sticky | `20` (convenção geral, confirmar por projeto) | — |

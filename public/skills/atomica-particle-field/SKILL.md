---
name: atomica-particle-field
description: Instala o fundo de partículas atômicas da Atomica (física gravitacional + liquid glass) em qualquer página Next.js/React. Use esta skill sempre que o usuário quiser replicar, instalar ou adicionar o fundo de partículas-átomo a uma nova LP, página ou projeto. Também acione quando o usuário mencionar "fundo de partículas", "particle field", "partículas-átomo" ou "efeito de fundo da Atomica".
---

# Atomica Particle Field — Pacote de Instalação

Fundo animado com física atômica gravitacional: cianos (núcleons) formam núcleos que atraem elétrons amarelos/vermelhos para órbitas. O cursor do utilizador quebra átomos ao passar sobre eles. Renderizado em Canvas 2D puro, sem dependências externas. Estética "liquid glass" suave — não compete com o conteúdo da página.

## Pré-requisitos

- Next.js 13+ (App Router) com TypeScript
- React 18+
- Nenhuma biblioteca adicional necessária

## Passos de instalação

### 1. Copiar o componente

Copia `assets/particle-field.tsx` para `src/components/particle-field.tsx` do projeto de destino.

```bash
cp .agents/skills/atomica-particle-field/assets/particle-field.tsx src/components/particle-field.tsx
```

Se o projeto de destino não estiver no mesmo repositório, o agente deve criar o ficheiro copiando o conteúdo de `assets/particle-field.tsx` diretamente para o caminho correto.

### 2. Adicionar o CSS

Abre `globals.css` (ou o ficheiro de estilos global equivalente) e adiciona o conteúdo de `assets/particle-field.css`. Podes copiar o bloco inteiro no final do ficheiro — as classes não colidem com estilos comuns.

Confirma que o body (ou elemento raiz) já tem um **fundo de cor opaco** definido. As partículas são transparentes e dependem de um fundo sólido por baixo para ficarem visíveis. Se a página ainda não tiver fundo, adiciona algo como:

```css
body {
  background-color: #f7efd9; /* var(--creme-100) real — ver atomica-design-system/references/design-tokens.md */
}
```

### 3. Integrar no layout / página

**Opção A — No layout raiz (recomendado para que apareça em todas as páginas):**

```tsx
// src/app/layout.tsx
import { ParticleField } from "@/components/particle-field";

export default function RootLayout({ children }) {
  return (
    <html lang="pt-BR">
      <body>
        <ParticleField />
        <main className="page-content">{children}</main>
      </body>
    </html>
  );
}
```

**Opção B — Numa página específica:**

```tsx
// src/app/page.tsx  (ou qualquer página)
import { ParticleField } from "@/components/particle-field";

export default function Page() {
  return (
    <div className="page-shell">
      <ParticleField />
      <div className="page-content">
        {/* conteúdo da página */}
      </div>
    </div>
  );
}
```

> O componente usa `"use client"` — se o ficheiro de destino for um Server Component, não há problema: o `ParticleField` importado vai criar automaticamente um boundary de client no Next.js.

### 4. Verificar

Inicia o servidor de desenvolvimento e confirma que:

- As partículas aparecem animadas sobre o fundo
- Passar o cursor sobre elas quebra os átomos
- O conteúdo da página fica por cima (z-index 2), não é tapado pelas partículas
- Em `prefers-reduced-motion: reduce` as partículas não aparecem (comportamento correto por acessibilidade)

---

## Personalização das cores

Amostras internas de projeto foram anonimizadas nesta versão pública.

```ts
const COLORS: Record<Particle["hue"], string> = {
  ciano:    "99, 190, 194",   // núcleons — ciano Atomica, levemente dessaturado
  amarelo:  "255, 185, 0",    // amarelo âmbar saturado — maior contraste com fundo creme
  vermelho: "238, 110, 105",  // vermelho mais claro/rosado — menos contraste bruto com creme
};
```

Repara que a paleta das partículas é **intencionalmente diferente** dos tokens de UI em `atomica-design-system` (`var(--ciano)` `#63bec2`, `var(--amarelo)` `#f7c528`, `var(--vermelho)` `#b8302f`) — é uma versão dessaturada/ajustada de propósito para funcionar como camada de fundo atrás de `backdrop-filter`, não como elemento de interface. Não "corrija" a paleta das partículas para bater com os tokens de UI; são domínios diferentes por decisão de design, confirmada em dois projetos.

Substitui os valores RGB (sem o `rgb()`) para adaptar à paleta do projeto. Os três canais são usados em vários níveis de opacidade — ajusta apenas os valores, não o formato.

## Ajuste de densidade

A quantidade de partículas é calculada automaticamente com base no tamanho do ecrã:

```ts
function particleCount() {
  return Math.max(50, Math.min(130, Math.round((width * height) / 10000)));
}
```

Para aumentar a densidade, reduz o divisor (`10000 → 8000`). Para diminuir, aumenta-o (`10000 → 14000`).

## Ajuste de intensidade visual

Para um efeito mais subtil (fundo mais "quiet"):
- Reduz `auraA` em `drawParticle` (ex.: `0.062 → 0.040`)
- Reduz `wA` (opacidade do branco central)

Para um efeito mais vivo:
- Aumenta `PTR_PUSH_NUCLEUS` para ejeções mais dramáticas ao hover
- Reduz `VEL_DAMPING` (ex.: `0.988 → 0.980`) para partículas mais ativas

---

## Arquitetura resumida

| Camada | CSS class | z-index | Descrição |
|---|---|---|---|
| Fundo | `body` | — | Cor sólida do projeto |
| Partículas | `.particle-stage` | 0 | Canvas fixo na viewport |
| Overlay vintage | `.particle-vintage-overlay` | — | Grain + vinheta nos cantos |
| Conteúdo | `.page-content` | 2 | Sections, cards, texto |

O canvas usa `pointer-events: none` — nunca bloqueia interações do utilizador.

## Notas de performance

- Usa `requestAnimationFrame` com limpeza automática no `useEffect` cleanup
- **Guard duplo de `prefers-reduced-motion`**: o componente TSX faz early-return antes de iniciar a simulação (nenhum ciclo de CPU gasto), e o CSS esconde `.particle-stage` inteiro (`display: none`) — os dois juntos garantem que nada anima nem é renderizado sob motion reduzido
- DPR limitado a 2× para não sobrecarregar ecrãs HiDPI
- Rastro de elétron com comprimento físico uniforme: `TRAIL_LENGTH = 550` pontos armazenados, registrados só quando o elétron avança `TRAIL_STEP_PX = 0.8`px — isso evita que elétrons lentos tenham rastro maior que os rápidos

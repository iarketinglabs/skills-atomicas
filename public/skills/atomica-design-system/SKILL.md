---
name: atomica-design-system
description: >-
  Use when o usuário pedir para criar, estilizar, revisar ou construir qualquer interface visual da marca Átomica: landing pages, websites, componentes UI, apresentações, posts visuais, emails HTML, dashboards, formulários ou outro material digital. Acione para design system Átomica, tokens, estilo Atompunk, CSS/Tailwind Átomica, sombra offset, card retrô, paleta, fontes, textura pulp, responsividade mobile ou revisão de uma interface existente contra os padrões da marca.
metadata:
  name: atomica-design-system
  description: "Use when o usuário pedir para criar, estilizar, revisar ou construir qualquer interface visual da marca Átomica: landing pages, websites, componentes UI, apresentações, posts visuais, emails HTML, dashboards, formulários ou outro material digital. Acione para design system Átomica, tokens, estilo Atompunk, CSS/Tailwind Átomica, sombra offset, card retrô, paleta, fontes, textura pulp, responsividade mobile ou revisão de uma interface existente contra os padrões da marca."
---

# Átomica Design System


## Quando Usar

- Criar ou estilizar **landing pages**, **websites**, **componentes React/HTML**
- Construir **apresentações**, **slides**, **pitch decks** com identidade Átomica
- Desenvolver **emails HTML**, **dashboards**, **formulários**
- Revisar interfaces existentes contra os padrões da marca
- Gerar **código CSS/Tailwind** com tokens da marca
- Criar **prototypes**, **wireframes** ou **mockups** visuais

## Como Usar Esta Skill

Identifique formato, seção ou estado a revisar, referência visual autorizada e restrições de conteúdo. Entregue a especificação ou o patch com tokens, estados e critérios de aceite. Sem navegador, registe revisão estática. Confira a listagem de assets antes de carregar fontes ou mídia.

1. **Identifique o escopo**: landing page, componente isolado, apresentação, etc.
2. **Leia os references necessários**:
   - Para cores, espaçamentos e tokens: `references/design-tokens.md`
   - Para fontes e hierarquia: `references/typography-guide.md`
   - Para botões, cards e inputs: `references/component-specs.md`
   - Para grid e responsividade: `references/layout-patterns.md`
   - Para logos, imagens e fontes: `references/branding-assets-index.md`
3. **Aplique o checklist de consistência** ao final de cada entrega

## Padrões de Implementação do site institucional

Os padrões de referência aplicam-se às interfaces web da Atomica. Confirme os estados reais e o contrato do projeto antes de copiar CSS. A apresentação em HTML e PDF tem um perfil próprio.

### Mobile e shell de navegação

- Trate `760px` como o contrato de mobile (`@media (max-width: 760px)`), inclusive em Playwright; não valide apenas em `md`/`sm` genérico.
- O header fica fixo no topo (`position: fixed; inset-inline: 0; top: 0`) e o conteúdo recebe espaço equivalente para não ficar escondido.
- Em mobile, o CTA de contato pertence ao menu sanduíche: esconda a cópia desktop fora do menu e mantenha uma única cópia acessível dentro da navegação aberta. O seletor de idioma deve ser um `details`/menu expansível, não uma fileira que estoura o header.
- Remova sombras decorativas específicas de desktop do wordmark em mobile quando elas criarem um offset visual não solicitado; não compense o problema com deslocamento do logo.

### Imagem, vídeo e ordem responsiva

- Confirme o asset visualmente antes de aplicar estilo. GIFs/vídeos grandes podem exigir `unoptimized`/elemento `<video>` direto; otimização automática não deve trocar a fonte, criar fundo ou esconder a animação.
- Borda, outline e offset shadow são propriedades independentes. Aplique-as somente quando o brief pedir; remover o fundo de uma imagem não autoriza manter moldura ou sombra.
- Inclinações suaves são `transform: rotate(...)` com origem definida e devem ser zeradas em mobile quando prejudicarem leitura, overflow ou alinhamento.
- Para mover uma imagem entre dois trechos no mobile, altere a ordem do DOM/grid (`order`) e mantenha uma instância; não duplique o asset com `position: absolute`, pois isso gera “bolas”/imagens residuais e desloca o texto.

### Formulários, opções e cascata CSS

- Um grupo de interesses é um `fieldset` com checkboxes reais e `label` clicável. Opções podem usar cards no desktop e uma coluna no mobile, mas cada item precisa de respiro lateral e vertical entre outline, caixa e texto.
- Em um `fieldset.field`, o reset `.field label { padding: 0 }` tem especificidade maior que `.interest-option`. Reforce o contrato no seletor do componente (`.field label.interest-option { padding: ... }`) ou use wrapper equivalente; conferir apenas a regra escrita no arquivo não basta.
- Para telefone, mantenha código do país pesquisável com prefixo `+`, número nacional formatado enquanto digita e os campos alinhados no mesmo grid. Validação deve respeitar o país selecionado e persistir código, ISO2 e número nacional separadamente.
- Consentimento aparece uma vez na etapa definida pelo modelo de dados, sem outline visual extra em volta do texto. Campos opcionais continuam com label explícito, como `Site (opcional)`, e URL preenchida deve ser normalizada/validada.

### Gate visual mínimo

Antes de considerar um componente pronto, inspecione o estado real no navegador: `getComputedStyle` para padding, border, shadow e transform; bounding boxes para alinhamento; e a árvore acessível para labels/CTAs. Um screenshot estático ou uma busca textual no CSS não prova que a regra venceu a cascata.

## Estilo Visual Base

A identidade Átomica é **Atompunk / Sci-Fi Retro-futurismo**:
- Otimismo do Atomic Age e Space Age dos anos 50
- Referência: Norman Rockwell advertising poster + capas de pulp magazine vintage
- Estética web: sombras offset duras (estilo cartaz), bordas grossas escuras, paleta limitada e ousada

## Hierarquia de Tokens

```
Primitive (valores brutos: hex, rem, px)
       ↓
Semantic (propósito: bg-primary, text-secondary, cta-urgency)
       ↓
Component (específico: card-bg, btn-primary-shadow, input-radius)
```

**Regra de ouro**: nunca use valores hardcoded em componentes — sempre referencie tokens.

## Checklist de Consistência Visual

Antes de entregar qualquer interface, verifique:

- [ ] **Fundo** em variação de Creme (`var(--creme-100)` `#f7efd9`, `--creme-200` `#f3e8cc`, `--creme-300` `#dbc9a6`)
- [ ] **Texto e bordas estruturais** em Gunmetal (`var(--gunmetal)` `#1b1b1b` ou `--gunmetal-700` `#3d3d3d`)
- [ ] **Cores de ação**: ciano (`var(--ciano)` `#63bec2`, hover `var(--ciano-light)` `#a8dee0`), amarelo (`var(--amarelo)` `#f7c528`), vermelho (`var(--vermelho)` `#b8302f`) — sem ramp de 5 tons por matiz, é um conjunto plano
- [ ] **Headline principal** em `"Atomica Script", "Atomica Caprasimo", serif` (não Oswald/Bebas)
- [ ] **Labels/botões** em `"Atomica Bebas", "Atomica Oswald", sans-serif` + uppercase
- [ ] **Corpo** em `"Atomica Jost", sans-serif` (nunca misture fontes no mesmo parágrafo)
- [ ] **Botão primário com texto `var(--gunmetal)`, não branco** — texto branco sobre `var(--ciano)` reprova contraste WCAG AA
- [ ] **Sombras offset** sem blur: `Xpx Ypx 0px var(--cor)` — cards usam border **3px** (não 2px), `.image-frame` usa **4px**
- [ ] **Cards** com `border-radius: var(--radius)` (12px) e textura pulp em camada dupla, não fundo sólido
- [ ] **Textura pulp** em camadas com `linear-gradient(...)` e `var(--texture-pulp)`. Use a retícula CSS quando a textura original não estiver disponível.
- [ ] **Responsividade**: breakpoint único confirmado em `760px`, não uma escala de 4 níveis

## Integração com Outras Skills

- **`atomica-key-visuals`**: Use para key visuals, imagens de capa, prompts de geração de imagem
- **`atomica-presentations`**: Use para slides e saída HTML/PDF
- **`frontend-design`**: Use para implementação frontend de componentes e páginas

## Referências

| Tópico | Arquivo |
|--------|---------|
| Tokens de Design | `references/design-tokens.md` |
| Tipografia | `references/typography-guide.md` |
| Especificações de Componentes | `references/component-specs.md` |
| Padrões de Layout | `references/layout-patterns.md` |
| Índice de Assets | `references/branding-assets-index.md` |
| `globals.css` de referência (copiável) | `assets/globals-reference.css` |

Use o CSS base com seus fallbacks. Para carregar fontes, adapte as regras de [tipografia](references/typography-guide.md) com arquivos autorizados no projeto. Com o perfil de apresentações, consulte a skill atomica-presentations.

Para orientações de contraste, confira [WCAG 2.2, contraste mínimo](https://www.w3.org/TR/WCAG22/#contrast-minimum).

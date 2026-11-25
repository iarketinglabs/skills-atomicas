# Paleta de Cores Átomica — Referência Completa

A paleta Átomica é vivida, contrastante e limitada. Sempre escolha uma cor principal, uma cor secundária, use Creme para fundo e Gunmetal para texto e linhas estruturais.

Amostras internas de projeto foram anonimizadas nesta versão pública.

---

## Neutros — A Base de Tudo

| Nome | Hex Code | Uso Tático |
|---|---|---|
| Creme-100 | `#f7efd9` | Cor primária de fundo (surface). A tela para nossas criações. |
| Creme-300 | `#dbc9a6` | Fundo secundário, divisórias sutis, áreas de destaque passivo. |
| Gunmetal-900 | `#1b1b1b` | Cor principal para textos, títulos e ícones. Garante contraste máximo. |
| Gunmetal-700 | `#3d3d3d` | Cor para textos secundários, descrições, placeholders. |
| Gunmetal-500 | `#686868`¹ | Cor para elementos desabilitados, bordas e divisórias. |
| Gunmetal-300 | `#A9A9A9`¹ | Bordas de inputs, ícones sutis. |

## Cores de Ação e Destaque — A Personalidade da Marca

| Nome | Hex Code | Uso Tático |
|---|---|---|
| Ciano-900 | `#137a80` | Texto de links com contraste máximo para fundos claros. |
| Ciano-700 | `#008C94`¹ | Links de texto. Passa no teste AA sobre Creme-100. |
| Ciano-500 | `#63bec2` | **Ação Primária.** Cor principal para botões e CTAs. |
| Ciano-300 | `#a8dee0` | Hover/foco para botões primários. Fundos de banners sutis. |
| Ciano-100 | `#e0f2f3` | Fundos de blocos de destaque muito sutis. |
| Amarelo-500 | `#f7c528` | **Destaque Visual.** Fundos de banners, tags, ícones de atenção. |
| Amarelo-300 | `#FDE68A`¹ | Hover/foco para elementos amarelos. |
| Amarelo-100 | `#fef8e4` | Fundo para notificações ou alertas informativos. |
| Vermelho-700 | `#D1283F`¹ | Cor para textos de erro ou alertas críticos sobre fundos claros. |
| Vermelho-500 | `#b8302f` | **Ação Secundária / Urgência.** Botões estratégicos, alertas. |
| Vermelho-300 | `#FF8C9B`¹ | Hover/foco para botões vermelhos. |
| Vermelho-100 | `#FFE5E8`¹ | Fundo para banners de erro ou de urgência. |

¹ Tom de apoio exclusivo desta skill de arte — sem variável correspondente no CSS de produto. O sistema real (`atomica-design-system`) declara só `--gunmetal`/`--gunmetal-700` (2 tons de neutro escuro), `--ciano`/`--ciano-dark`/`--ciano-soft` (3 tons de ciano), `--amarelo`/`--amarelo-soft` (2 tons) e `--vermelho` (1 tom só). Os tons marcados aqui existem para dar gradação numa imagem gerada (hover, texto de erro, fundo de alerta) onde o produto real ainda não tem um equivalente declarado — são uma extensão razoável da paleta para o domínio de imagem, não um valor confirmado em CSS.

**Nota histórica**: esta tabela documentava até há pouco `Ciano-900 = #005F64`, valor que nunca correspondeu ao código real (`#137a80`) nem à versão anterior de `atomica-design-system` (`#006B70`, também errada). As duas skills foram sincronizadas na mesma correção.

## Regras de Aplicação

1. **Escolha uma cor principal** entre Ciano-500, Amarelo-500 ou Vermelho-500
2. **Escolha uma cor secundária** entre as 5 cores da paleta Átomica
3. **Fundo**: sempre variação de Creme (100 ou 300)
4. **Texto e linhas estruturais**: Gunmetal-900 ou Gunmetal-700
5. **Nunca use mais de 3 cores principais** no mesmo key visual
6. **Contraste obrigatório**: a cor principal do headline/CTA deve ter contraste mínimo AA sobre o fundo — o Vermelho-500 real (`#b8302f`, tijolo escuro) e o Ciano-500 real (`#63bec2`) têm perfis de contraste diferentes do que versões antigas desta tabela sugeriam; teste antes de assumir que texto branco funciona sobre qualquer um dos dois.

## Combinações Testadas

| Principal | Secundária | Fundo | Texto | Uso |
|---|---|---|---|---|
| Ciano-500 | Amarelo-500 | Creme-100 | Gunmetal-900 | Energia, inovação, tecnologia |
| Vermelho-500 | Amarelo-500 | Creme-100 | Gunmetal-900 | Urgência, alerta, ação imediata |
| Amarelo-500 | Vermelho-500 | Creme-100 | Gunmetal-900 | Destaque máximo, otimismo |
| Ciano-500 | Vermelho-500 | Creme-100 | Gunmetal-900 | Contraste máximo, dinamismo |
| Vermelho-500 | Ciano-500 | Creme-100 | Gunmetal-900 | Ação com frescor tecnológico |

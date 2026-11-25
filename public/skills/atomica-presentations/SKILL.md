---
name: atomica-presentations
description: Crie, adapte, revise e valide apresentações Atomica em HTML offline e PDF. Use para transformar briefing ou Markdown em slides, preservar conteúdo aprovado, incorporar imagens ou vídeos locais autorizados, corrigir um deck renderizado ou preparar arquivos públicos com notas do apresentador separadas. Indicado para exportação de apresentações, sem edição de PowerPoint.
---

# Apresentações Atomica

## Entradas e entregas

Identifique público, decisão desejada, idioma, duração e conteúdo aprovado. Confirme fontes locais, imagens ou vídeos autorizados e o uso pretendido. Use 16:9 por padrão. Defina a quantidade de slides pela sequência de mensagens.

Entregue o HTML público com seus assets, o PDF se verificável, o roteiro falado separado e o registo de validação. Mantenha JSON de trabalho, notas e `presenter.html` no conjunto privado.

## Processo

1. Antes da composição, registe os itens da fonte que devem permanecer: ordem aprovada, títulos, mensagens, dados, condições, prazos e decisões. Se o roteiro ainda não foi aprovado, exponha o plano de slides e as lacunas.
2. Defina uma função para cada slide. Use [Perfil visual](references/visual-system.md) para geometria e [Composições](references/compositions.md) para associar evidência, comparação, cronograma, imagem ou ação à mensagem. Proteja a legibilidade e os dados quando a composição mudar.
3. Prepare os arquivos de fonte e seus avisos conforme [Recursos do pacote](references/assets.md). Siga o [Fluxo de construção](references/workflow.md), partindo de [exemplo básico](assets/example.json) ou [exemplo editorial](assets/editorial-example.json). Use somente mídia local autorizada e confirme enquadramento, posição e alternativa conforme [Ilustração](references/illustration.md) e [Vídeo em loop](references/loop-video-assets.md).
4. Depois de alterações, renderize a fonte atual, mesmo que a edição tenha sido pequena. Confira que HTML, folha de estilos e PDF correspondem à mesma versão. Use [Aceite](references/acceptance.md) para validar layout, fontes, movimento reduzido, navegação, ausência de rede e isolamento das notas.
5. Inspecione as páginas renderizadas. Compare títulos, ordem, números e condições com a fonte. Prepare o conjunto público conforme [Entrega](references/delivery.md) e só faça publicação mediante autorização.

## Ferramentas e limites

A construção usa Python 3.10+ e a biblioteca padrão. Requer os arquivos tipográficos e avisos listados na referência, obtidos ou fornecidos antes da construção. O HTML gerado funciona offline. Verificação de navegador usa Playwright e Chrome ou Chromium. O PDF requer também PyMuPDF. Instale as dependências conforme [Fluxo de construção](references/workflow.md).

Com acesso só a texto, entregue a sequência, as instruções e o plano de validação. Se um recurso necessário estiver em falta, identifique-o e registe o aceite pendente. Para evolução visual, compare a captura e a página PDF de cada slide alterado. O pacote prepara a entrega pública local.

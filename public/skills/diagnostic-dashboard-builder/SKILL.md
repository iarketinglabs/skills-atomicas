---
name: diagnostic-dashboard-builder
description: Use para construir ou revisar um painel web de diagnóstico com estado, roadmap, navegação e documentos rastreáveis. Inclui leitor estático de material liberado e desenho de arquitetura quando forem necessárias confidencialidade, comentários, validações ou histórico.
---

# Painel de diagnóstico

Mostre onde o projeto está, qual decisão vem a seguir e em quais documentos ela se apoia. Mantenha o painel como apresentação de versões aprovadas da base documental e do registro de status.

1. **Confirme fontes e público.** Identifique dono, versão e estado dos documentos e do roadmap, quem verá cada classe de informação e que decisões o painel precisa apoiar. Se faltarem documentos ou status, entregue um protótipo sintético e anote a coleta necessária.
2. **Escolha a arquitetura.** Para demonstração sintética ou material aprovado para divulgação, o [leitor estático](references/leitor-e-publicacao.md) oferece status, marcos, filtros e documentos relacionados. Para dados restritos, use controle de acesso no servidor. Para comentários, edição ou validação, consulte [colaboração](references/colaboracao-e-revisao.md).
3. **Monte um recorte selecionado.** Crie um manifesto com título, data, marcos e somente os documentos aprovados para a mesma audiência. Preserve a versão e o estado de cada documento. Texto citado ou inferência continuam identificáveis pela origem. Exemplo em [manifesto sintético](assets/exemplo-painel.json).
4. **Gere e confira.** Rode `python scripts/build_dashboard.py assets/exemplo-painel.json painel.html` na pasta da skill com Python 3.9+. Abra o HTML e confira ordem, legibilidade, filtros, links internos, marcos, detalhes, estado vazio e funcionamento em largura estreita. O leitor mostra o texto original sem renderizar HTML ou executar o conteúdo de documentos.
5. **Entregue ou publique com a visibilidade acordada.** O arquivo é autocontido e pode ser aberto offline. Para publicação, confirme o serviço, a visibilidade efetiva de site e arquivos, o conteúdo do artefato e autorização. Se for compartilhar dados restritos e o host não servir com autorização verificável, entregue apenas a proposta de arquitetura e a demonstração sintética.

Sem terminal, forneça o manifesto e um rascunho de layout. Sem navegador, marque a verificação visual como pendente. Sem acesso aprovado ao provedor, entregue artefatos locais e passos de validação. Aceite editorial, autenticação e publicação precisam de evidências distintas.

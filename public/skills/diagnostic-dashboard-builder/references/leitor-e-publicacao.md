# Leitor estático e decisão de publicação

## Contrato do manifesto

- `titulo` e `resumo` descrevem decisão e estado principal. Informe `atualizado_em` em AAAA-MM-DD e `classificacao` como `sintetico` ou `liberado-publico`. A classificação é uma declaração do responsável e não prova aprovação do conteúdo.
- Cada `marcos` contém `titulo`, `estado` (pendente, em-curso, bloqueado ou concluido), `responsavel`, `proximo` e lista `documentos` com IDs existentes ou vazia.
- Cada `documentos` contém `id` único em minúsculas com hífens, `titulo`, `area`, `versao`, `estado`, `texto` e lista `relacionados` com IDs existentes ou vazia. Inclua a origem e a limitação dentro de texto. Se a versão ainda não foi aprovada, deixe claro seu estado e verifique se pode ser divulgada.
- O leitor copia apenas os campos definidos do manifesto. Campos extras são rejeitados para reduzir inclusões acidentais. Texto e títulos aparecem como texto escapado. Agrupe documentos na ordem editorial desejada e use relações entre documentos para navegação.

O HTML inclui conteúdo em claro. Revise ativamente todo texto, inclusive os detalhes recolhidos, antes de distribuir o arquivo. Nenhuma pessoa precisa de login para obter seu conteúdo se puder baixar o arquivo. Evite incluir rascunhos misturados, nomes, links internos, caminhos de arquivos, respostas e anexos não avaliados.

## Escolha de hospedagem

| Necessidade | Decisão |
| --- | --- |
| Protótipo local ou relatório público | Leitor estático, com conteúdo sintético ou formalmente liberado |
| Documentos restritos | Host que proteja as rotas e os próprios arquivos com autenticação e autorização adequadas à audiência |
| Acesso variável por grupo, edição, exportação ou revogação individual | Autorize no servidor todas as operações, inclusive download e consultas diretas, e teste estados negados |

Em site estático, tela de senha ou criptografia com segredo partilhado não implementa identidade individual, autorização por papel ou revogação por pessoa. Um repositório privado não garante que o Pages é privado. Confirme o plano, a visibilidade configurada do site e o acesso em sessão sem login antes de colocar material de cliente. [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/changing-the-visibility-of-your-github-pages-site)

## Aceite

As datas e os estados correspondem ao status autorizado. Um marco bloqueado explica a decisão pendente. Todos os IDs encontrados têm destino. O leitor mostra acentos e quebras de linha, navega com teclado e permite abrir a página sem rede. Se publicado, confira a rota e o artefato em sessão separada, com acesso esperado e negado conforme a arquitetura, e registre versão e responsável.

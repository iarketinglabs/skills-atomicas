# Formatos Suportados e Prioridade por Subpasta

## Extensões aceitas pelo upload de arquivo (`source_add`, `source_type=file`)

PDF, TXT, MD, DOCX, CSV, EPUB, MP3, M4A, WAV, AAC, OGG, OPUS, MP4, JPG, JPEG, PNG, GIF, WEBP.

Fora dessa lista (ex.: `.pptx`, `.xlsx`, `.key`, `.numbers`), o arquivo binário não pode ser enviado diretamente como fonte de arquivo. Alternativas, em ordem de preferência:

1. Usar o `.md` irmão gerado por `populate-directives` (contém o texto extraído) — sempre a primeira opção.
2. Se o arquivo estiver no Google Drive e o valor visual for indispensável (ex.: apresentação com gráficos que a equipe quer ver no Studio), usar `source_add` com `source_type=drive` e `doc_type` correspondente (`doc`, `slides`, `sheets`, `pdf`) em vez de tentar subir o binário local.
3. Converter para PDF antes de subir, apenas se o usuário pedir explicitamente e nenhuma das opções acima resolver.

Fontes com imagem (PDF, JPG, PNG etc.) alimentam o pipeline de recorte visual do Studio — gráficos, fotos e diagramas podem aparecer como apoio visual em vídeos gerados a partir do notebook. Isso é um motivo válido para subir o PDF além do `.md`, mas não substitui o `.md`.

## Prioridade por Subpasta de `directives/`

Ao decidir o que subir quando o usuário pede "todas as fontes relevantes" sem detalhar:

| Prioridade | Subpasta | Por quê entra primeiro |
|---|---|---|
| Alta | `meetings/` | Registra decisões e contexto direto do cliente — maior densidade decisória |
| Alta | `presentations/` (versão `.md`) | O que foi formalmente apresentado como proposta/solução |
| Alta | `sales-intelligence/` | Dossiê consolidado de decisores, histórico comercial e CRM |
| Média | `sheets/`, `forms/` | Dados estruturados (respostas de discovery, planilhas de escopo) |
| Média | `emails/`, `messages/` | Combinados informais e pendências — útil, mas mais ruidoso |
| Baixa | `notes/`, `docs/`, `prototypes/` | Contexto complementar; incluir só se o usuário pedir cobertura completa |
| Fora do escopo desta skill | `contracts/`, `approvals/` | Normalmente têm sensibilidade jurídica/financeira — só subir se o usuário pedir explicitamente |

Subpastas de prioridade "Alta" são o padrão razoável quando o usuário não especifica escopo. Para as demais, confirme antes de incluir.

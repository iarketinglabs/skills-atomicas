# Documentação Viva do Projeto {{PROJECT_NAME}}

Documentação técnica contínua, dedicada a **PMs e Desenvolvedores**, mantida ao longo de todo o desenvolvimento do sistema. Diferente dos documentos de PRD/specs deste projeto, que descrevem o *porquê* e o *desenho original* de cada marco e não são reescritos a cada iteração, esta pasta descreve **como o sistema funciona hoje** e é atualizada a cada mudança relevante.

TODO: linkar aqui o(s) PRD(s) e specs técnicas reais deste projeto, por exemplo:
- `[PRD](../PRD.md)`
- `[Specs Técnicas](../specs-tecnicas.md)`

## Modelo

Markdown atômico: um assunto coeso por arquivo, agrupado em pastas por tópico/subtópico. Arquivos se referenciam entre si com links relativos em vez de duplicar conteúdo. Pode haver outros tipos de arquivo (scripts, templates, exemplos) quando isso ilustrar melhor um padrão do que prosa.

## Tópicos

| Pasta | Conteúdo | Público principal |
|---|---|---|
| [`00-visao-geral/`](00-visao-geral/README.md) | O que é o sistema, para quem, glossário de termos do domínio | PM e Dev |
| [`01-arquitetura/`](01-arquitetura/README.md) | Componentes, diagrama de arquitetura, stack, decisões de design de alto nível | Dev (PM para visão geral) |
| [`02-integracoes/`](02-integracoes/README.md) | Um arquivo por integração externa | Dev |
| [`03-modelo-de-dados/`](03-modelo-de-dados/README.md) | Schemas de dados persistidos pelo sistema | Dev |
| [`04-fluxos/`](04-fluxos/README.md) | Um arquivo por fluxo de ponta a ponta | PM e Dev |
| [`05-operacao/`](05-operacao/README.md) | Deploy, variáveis de ambiente, runbook de incidentes | Dev (PM para o runbook) |
| [`06-decisoes/`](06-decisoes/README.md) | Registro curto (estilo ADR) de decisões técnicas e seus trade-offs | PM e Dev |

A numeração é só ordem de leitura sugerida, não hierarquia rígida. Novos tópicos podem ser adicionados conforme o projeto cresce, desde que preservem a granularidade atômica.

## Trilhas de leitura sugeridas

- **PM:** visão geral → fluxos → decisões.
- **Dev:** arquitetura → integrações → modelo de dados → operação.

## Status

Esqueleto gerado automaticamente. Cada pasta é populada por quem implementa o componente correspondente, como parte da própria tarefa de desenvolvimento (skill `system-documentation-keeper`).

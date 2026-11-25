# Monorepo para Contexto

Parte de **Stack Tecnológica** (ver Framework Mental no `SKILL.md`). Como a organização física do código impacta diretamente a precisão e o custo de um agente — um monorepo bem estruturado é, em si, uma técnica de eficiência de contexto.

## Por que um agente funciona melhor em um monorepo

Em bases de código fragmentadas em múltiplos repositórios, se um agente precisa alterar um endpoint, ele não consegue "enxergar" como o front-end consome aquela resposta sem que o desenvolvedor cole trechos manualmente na conversa. Um monorepo resolve isso fisicamente:

- **Navegação sem fricção:** mantendo aplicações e pacotes compartilhados sob o mesmo workspace, o agente rastreia alterações de ponta a ponta nativamente, sem depender de contexto colado manualmente.
- **Aproveitamento máximo de cache de prompt:** como as configurações globais e regras de estilo ficam centralizadas na raiz, o agente lê essas regras estáveis uma única vez por sessão e interage cirurgicamente com os subdiretórios — maximizando o desconto de cache (ver a skill de Eficiência desta coleção, se disponível, para a mecânica completa).

## Single Source of Truth via pacotes compartilhados

O erro mais comum em desenvolvimento acelerado é a falta de reuso: se um agente precisa de uma função específica e não a encontra centralizada, ele a reescreve do zero, gerando variantes divergentes e difíceis de manter.

```
/workspace/
├── /apps/
│   ├── /web  ──► importa "shared-core" e "database"
│   └── /cli  ──► importa "shared-core" e "database"
└── /packages/
    ├── /database     (conectores, políticas de acesso, schema)
    └── /shared-core  (lógica de negócio e validação — fonte única)
```

A mesma função utilitária fica definida uma única vez em um pacote compartilhado, importada tanto pela aplicação exposta a clientes quanto por um agente CLI rodando em background. Se a regra mudar, atualiza-se em um único lugar — front-end e agente herdam a mudança sem divergência de tipagem.

## Estrutura de workspace

Um gerenciador de workspaces (declarando quais pastas são apps e quais são pacotes) e um orquestrador de scripts de build/lint/typecheck no nível raiz permitem que o agente rode verificações determinísticas sem precisar navegar manualmente por cada subpasta.

**Cuidado com caminhos desalinhados:** configurações de tipo/lint com caminhos relativos quebrados entre os subpacotes criam a patologia dos "erros fantasma" — o agente detecta erros globais que não causou, entra em pânico de depuração e queima tokens tentando consertar algo fora do seu escopo real.

## Isolamento de sessões paralelas: Git Worktrees

Centralizar todo o código no mesmo repositório facilita a navegação, mas permitir que múltiplos sub-agentes escrevam no mesmo diretório ativo ao mesmo tempo gera conflito de escrita física. A solução física é a mesma usada em toda a arquitetura multi-agente desta coleção — worktrees isolados por agente, ligados ao mesmo repositório central. Ver o detalhamento completo do padrão em `hierarchical-planner-worker.md`.

## Herança de diretrizes por diretório (Nested Workstations)

Para evitar que regras de um subdomínio poluam o contexto de outro, um monorepo agêntico organiza as regras de forma hierárquica: um arquivo de diretrizes global na raiz define o que é inegociável para toda a organização; cada subdiretório tem seu próprio arquivo de diretrizes local, que soma (não substitui) as regras da raiz quando o agente está atuando naquela pasta específica. Assim, o agente nunca consome tokens com regras visuais de front-end enquanto opera estritamente no banco de dados. Este padrão de herança de contexto por diretório tem tratamento completo na skill de Harness Engineering desta coleção, se disponível.

## Checklist

- Lógica de negócio compartilhada vive em um pacote único, nunca duplicada entre app web e agente CLI.
- Caminhos de importação e configuração de tipos estão alinhados entre todos os subpacotes — zero erro fantasma antes de plugar um agente.
- Sessões/sub-agentes paralelos usam worktrees isolados, nunca escrevem no mesmo diretório de trabalho simultaneamente.
- Regras de diretório são aninhadas (raiz + local), não um único arquivo monolítico de regras.

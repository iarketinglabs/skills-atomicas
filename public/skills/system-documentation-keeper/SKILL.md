---
name: system-documentation-keeper
description: Mantém `directives/documentacao/` — a documentação técnica viva (para PMs e Devs) do sistema, automação ou agente que está sendo construído para o cliente — sempre organizada, atualizada e legível, em modelo atômico de Markdown por tópico/subtópico, com referências cruzadas entre arquivos. Diferente de `directives/PRD*.md`/`specs*.md` (que registram o porquê e o desenho original de cada marco e não mudam depois de aprovados), esta pasta registra como o sistema funciona hoje. Use SEMPRE que você (qualquer agente de codificação — Claude Code, Codex, Kimi, Composer, Antigravity, etc.) implementar, alterar ou remover um componente de uma automação/sistema/agente para um cliente — novo endpoint, integração, schema de dados, fluxo, decisão de arquitetura, mudança de deploy — como parte da própria tarefa, antes de considerar o trabalho concluído. Use também quando `directives/documentacao/` ainda não existir e for preciso criar o esqueleto inicial, ou quando o usuário pedir para "documentar isso", "atualizar a documentação técnica", "organizar/criar a documentação do projeto". 100% agnóstica a cliente e a stack — reutilizável em qualquer projeto de desenvolvimento de sistemas agênticos.
---

# System Documentation Keeper — Documentação Viva de Sistemas e Automações

Skill de disciplina contínua: mantém `directives/documentacao/` — a documentação técnica viva do sistema/automação/agente que está sendo construído para o cliente — sempre organizada, atualizada e legível para PMs e Devs, como parte do próprio trabalho de implementação, nunca como tarefa separada agendada depois.

## Quando Usar

- Sempre que um componente de uma automação, sistema ou agente sendo construído para um cliente for implementado, alterado ou removido: nova integração, mudança de schema de dados, novo fluxo de ponta a ponta, decisão de arquitetura, mudança de infraestrutura/deploy.
- Antes de considerar uma tarefa de desenvolvimento "concluída" — atualizar a documentação correspondente é parte do critério de conclusão da tarefa, não um passo posterior opcional.
- Quando `directives/documentacao/` ainda não existe no projeto e é preciso criar o esqueleto inicial (ver Passo 0 — Bootstrap).
- Pedido explícito de "documentar isso", "atualizar a documentação técnica", "organizar a documentação do projeto" ou "criar/revisar o esqueleto de documentação".

## Quando NÃO Usar

- Para `memory/` (segundo cérebro / histórico da relação com o cliente) — isso é exclusivo da skill `memory-keeper`. Esta skill cuida só de `directives/documentacao/`, a documentação técnica do sistema em si, não do relacionamento com o cliente.
- Para o conteúdo de `directives/PRD*.md` ou `directives/specs*.md` — esses documentos registram o *porquê* e o *desenho original* de cada marco; esta skill nunca os edita, só os usa como referência de contexto (ver Modelo).
- Para comunicação com o cliente (Daily Brief, mensagens Slack) — isso é a skill `journaling`.
- Para gerar conteúdo técnico especulativo sobre um componente que ainda não existe de fato no sistema — documentação acompanha o que foi construído, não antecipa o que ainda será.

## Pré-requisito e Portabilidade

- Client-agnóstica e stack-agnóstica por design: não assume nenhum domínio, linguagem, framework ou conjunto de integrações específico. Funciona em qualquer repositório de projeto que tenha (ou deva ter) uma pasta `directives/` na raiz.
- Não depende de nenhum MCP, credencial ou arquivo de configuração — só de acesso de leitura/escrita ao repositório local.
- Convive com qualquer PRD/specs que o projeto já tenha — usa-os como fonte do "porquê", nunca os reescreve.

## Modelo

- **Markdown atômico:** um assunto coeso por arquivo, arquivos agrupados em pastas por tópico/subtópico — nunca um único arquivo monolítico cobrindo uma área inteira do sistema.
- Cada `.md` é escrito para leitura humana em primeiro lugar (PM e Dev); pode referenciar ou anexar outros tipos de arquivo (ex.: exemplo de payload, script, template de prompt) quando isso for mais claro do que descrever em prosa.
- **Referência cruzada:** arquivos linkam uns aos outros com links Markdown relativos (`[texto](../pasta/arquivo.md)`) sempre que um conceito depender de outro, em vez de duplicar explicação já escrita alhures.
- **Divisão de papel:** `PRD*.md`/`specs*.md` guardam o *porquê* e o desenho original de cada marco (não são reescritos a cada iteração pós-aprovação). `directives/documentacao/` guarda o *como funciona hoje* — reflete o estado real do sistema, atualizado a cada mudança relevante.
- **Equilíbrio profundidade × legibilidade:** cada arquivo responde "o que é isso e como funciona" de forma direta. Detalhes de implementação que mudam com frequência (nomes de variáveis internas, por exemplo) só entram quando ajudam a entender comportamento — a documentação não é um espelho do código-fonte. Checklist completo em `references/quality-bar.md`.

## Estrutura Padrão de Tópicos

Ponto de partida recomendado para qualquer projeto (versão completa e regras de adaptação em `references/topic-skeleton.md`):

| Pasta | Conteúdo | Público principal |
|---|---|---|
| `00-visao-geral/` | O que é o sistema, para quem, glossário de termos do domínio | PM e Dev |
| `01-arquitetura/` | Componentes, diagrama de arquitetura, stack tecnológica, decisões de design de alto nível | Dev (PM para visão geral) |
| `02-integracoes/` | Um arquivo por integração externa — contrato, autenticação, limites conhecidos | Dev |
| `03-modelo-de-dados/` | Schemas de dados (databases, tabelas, filas, eventos) e o significado de cada campo | Dev |
| `04-fluxos/` | Um arquivo por fluxo de ponta a ponta do sistema | PM e Dev |
| `05-operacao/` | Deploy, variáveis de ambiente, runbook de incidentes comuns, observabilidade | Dev (PM para o runbook) |
| `06-decisoes/` | Registro curto (estilo ADR: contexto, decisão, trade-offs) de decisões técnicas relevantes | PM e Dev |

A numeração é só ordem de leitura sugerida, não hierarquia rígida. Nem todo projeto precisa das 7 pastas desde o dia um — crie cada uma sob demanda, conforme o sistema ganha componentes reais para documentar (nunca crie uma pasta cheia de conteúdo genérico "para o futuro").

## Passo 0 — Bootstrap (primeira vez no projeto)

Se `directives/documentacao/` ainda não existir:

1. Rode `scripts/bootstrap_doc_skeleton.py` a partir da raiz do projeto (ver docstring do script para opções) — gera `directives/documentacao/README.md` e as 7 subpastas padrão com README placeholder, a partir dos templates em `assets/`.
2. Abra o `README.md` gerado e preencha os placeholders `TODO:` (nome do projeto, links para o(s) PRD/specs reais deste projeto).
3. Não crie conteúdo técnico ainda inexistente — cada subpasta fica com `Status: a popular conforme o desenvolvimento avança` até haver algo real para documentar.

O script é idempotente: nunca sobrescreve um arquivo já existente, só cria o que falta — pode ser rodado de novo com segurança se o esqueleto já existir parcialmente.

## Passo a Passo (uso contínuo, a cada mudança no sistema)

1. **Identifique o que mudou** na tarefa de desenvolvimento que você acabou de terminar (ou está terminando): novo componente, integração, schema, fluxo, decisão de arquitetura, mudança de operação/deploy.
2. **Mapeie para um tópico** da estrutura padrão (`references/topic-skeleton.md`) — uma mudança pode tocar mais de um tópico (ex.: uma integração nova toca `02-integracoes/` e possivelmente `01-arquitetura/`).
3. **Verifique se o arquivo do tópico já existe.** Se sim, atualize-o no lugar (nunca duplique); se não, crie um novo arquivo dentro da subpasta correspondente, nomeado em `kebab-case` pelo assunto (ex.: `02-integracoes/nome-da-integracao.md`).
4. **Adicione referências cruzadas** de/para tópicos relacionados já existentes, em vez de repetir explicação.
5. **Atualize o índice** (`directives/documentacao/README.md`) sempre que um arquivo ou pasta novo for criado.
6. **Aplique o checklist de equilíbrio** (`references/quality-bar.md`) antes de considerar a atualização concluída — releia o arquivo como se fosse a primeira vez que alguém o abre.

## Anti-Padrões

| O que NÃO fazer | Por quê |
|---|---|
| Tratar a documentação como tarefa separada, "para depois" | Fica permanentemente defasada — a regra é atualizar na mesma tarefa que muda o sistema |
| Criar um arquivo monolítico por área inteira do sistema | Quebra o modelo atômico; dificulta referência cruzada e revisão incremental |
| Duplicar explicação já escrita em outro tópico | Gera divergência quando um dos dois lados for atualizado e o outro não |
| Reescrever `PRD*.md`/`specs*.md` para refletir o estado atual do sistema | Esses documentos são o registro histórico do marco; o estado atual vai em `directives/documentacao/` |
| Criar as 7 pastas cheias de conteúdo genérico/inventado no bootstrap | O objetivo é esqueleto vazio + placeholders; conteúdo real só entra quando existe algo real para documentar |
| Incluir segredos, tokens ou credenciais como exemplo | Documentação técnica segue as mesmas regras de segurança do resto do repositório |
| Deixar um arquivo crescer sem revisão até cobrir vários assuntos | Se um tópico está inchando, decomponha em subtópicos antes que fique ilegível |

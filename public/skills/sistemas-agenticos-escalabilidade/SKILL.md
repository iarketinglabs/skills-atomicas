---
name: sistemas-agenticos-escalabilidade
description: "Framework para escalar infraestrutura e coordenação de agentes. Use ao decidir capacidade, deploy, armazenamento, monorepo, decomposição, paralelização ou isolamento de workers. Apresenta planner-worker como um padrão possível, com critérios para manter execução sequencial ou adotar concorrência; não substitui a configuração real do ambiente."
---

# Escalabilidade e Infraestrutura

## Quando Usar

- Decidir onde e como hospedar agentes e automações (VPS própria vs. serviços gerenciados).
- Estruturar um monorepo, banco de dados ou camada de cache para maximizar a eficiência de um agente.
- Decompor uma tarefa grande em sub-problemas que podem rodar em paralelo com segurança.
- Diagnosticar por que um sistema com múltiplos agentes apresenta maior latência ou menor confiabilidade do que um único agente.
- Desenhar a coordenação entre um planejador e uma frota de workers efêmeros.

## Quando NÃO Usar

- Para provisionar a infraestrutura real de um provedor específico — esta skill orienta a decisão e o padrão, não substitui a configuração real de conta/DNS/billing de cada serviço.
- Para questões de segurança de credenciais, RLS ou isolamento de sandbox em profundidade — isso é escopo canônico da skill de Segurança e Confiabilidade desta coleção, se disponível.
- Para eficiência de tokens/contexto de uma única sessão — isso é escopo da skill de Eficiência desta coleção, se disponível.

## Framework Mental: A Arquitetura de Duas Camadas

A maior parte desta skill assume um único padrão arquitetural como base, detalhado por completo em `references/hierarchical-planner-worker.md` — aqui fica o resumo que todo o ramo de Multi-Agentes pressupõe como pré-lido.

### Duas camadas, não equipes
Tentar mimetizar uma equipe humana plana (vários agentes de igual autoridade coordenando-se por mensagens compartilhadas) colapsa em escala: os agentes disputam travas de recurso, tornam-se avessos a risco e desperdiçam tokens em atividade que não converte em progresso real. A arquitetura que escala tem exatamente duas camadas:

- **Planejador:** um modelo de alta capacidade que mantém o estado global, decompõe o objetivo em tarefas e nunca executa trabalho manual diretamente.
- **Trabalhadores efêmeros:** subagentes de escopo restrito e custo controlado, instanciados sob demanda, que executam uma única subtarefa isolada e são destruídos ao final.

### Workers Stay Ignorant (Contexto Mínimo Viável)
Um worker com acesso ao repositório inteiro ou ao contexto estratégico completo sofre sobrecarga cognitiva e tenta refatorações fora do escopo pedido. A infraestrutura deve fornecer só o fragmento estritamente necessário para a subtarefa — nada além disso.

### No Shared State
Agentes paralelos nunca devem compartilhar o mesmo diretório, ferramenta ativa ou estado volátil ao mesmo tempo — isso reintroduz a mesma disputa de recurso que a arquitetura de duas camadas existe para eliminar. O mecanismo físico de isolamento é o **Git Worktree**: cada worker recebe uma pasta isolada ligada ao mesmo repositório central, com merge resolvido de forma assíncrona depois que cada um termina.

### O achado empírico que motiva tudo isso
Pesquisa de escala revelou que adicionar mais agentes a um sistema sem essa segregação pode **piorar** o resultado: acima de determinado nível de precisão individual, ou de densidade de ferramentas compartilhadas, agentes horizontais podem gerar retorno decrescente ou negativo. Ver `references/eliminating-serial-dependencies.md`.

## Mapa da Taxonomia

| Ramo | Sub-tópico | Arquivo de referência |
|---|---|---|
| Servidores e Deploy | Computação Autogerida | `references/self-managed-compute.md` |
| Servidores e Deploy | Contêineres e Plano de Controle | `references/containers-and-control-planes.md` |
| Servidores e Deploy | Plataforma Gerenciada e Deploy por CLI | `references/managed-platforms-and-cli-deploy.md` |
| Stack Tecnológica | Redis (Memória de Baixa Latência) | `references/redis.md` |
| Stack Tecnológica | PostgreSQL (Fonte da Verdade) | `references/postgresql.md` |
| Stack Tecnológica | Monorepo para Contexto | `references/monorepo-for-context.md` |
| Escalabilidade e Multi-Agentes | Decomposição em Sub-problemas Verificáveis | `references/task-decomposition-and-verification.md` |
| Escalabilidade e Multi-Agentes | Paralelização para Ganho de Throughput | `references/parallelization-and-throughput.md` |
| Escalabilidade e Multi-Agentes | Arquitetura Hierárquica (Planejador/Trabalhador) | `references/hierarchical-planner-worker.md` |
| Escalabilidade e Multi-Agentes | Eliminação de Dependências Seriais | `references/eliminating-serial-dependencies.md` |
| Escalabilidade e Multi-Agentes | Coordenação de Agentes Simples | `references/simple-agent-coordination.md` |

## Servidores e Deploy

Onde e como rodar um agente fora da máquina local:

- **Computação Autogerida:** quando a equipe aceita operar sistema, rede, patches e backups em troca de maior controle. Ver `references/self-managed-compute.md`.
- **Contêineres e Plano de Controle:** como isolar processos e escolher entre automação declarativa, painel ou linha de comando. Ver `references/containers-and-control-planes.md`.
- **Plataforma Gerenciada e Deploy por CLI:** quando reduzir operação compensa restrições de portabilidade, custo ou controle. Ver `references/managed-platforms-and-cli-deploy.md`.

## Stack Tecnológica

As peças de dados que sustentam um sistema agêntico em produção:

- **Redis:** a camada de memória de baixa latência para sessão, rate limiting e mensageria. Ver `references/redis.md`.
- **PostgreSQL:** a fonte única da verdade relacional. Ver `references/postgresql.md`.
- **Monorepo para Contexto:** organização física do código como técnica de eficiência de contexto. Ver `references/monorepo-for-context.md`.

## Escalabilidade e Multi-Agentes

Como coordenar múltiplos agentes sem que a coordenação em si vire o gargalo — todos assumem o Framework Mental acima:

- **Decomposição em Sub-problemas Verificáveis:** o critério que decide se uma tarefa deve virar multi-agente. Ver `references/task-decomposition-and-verification.md`.
- **Paralelização para Ganho de Throughput:** três padrões de coordenação concorrente (batching, consenso estocástico, debate). Ver `references/parallelization-and-throughput.md`.
- **Arquitetura Hierárquica:** o arquivo canônico — ciclo completo, Git Worktrees, o padrão Juiz de 4 vereditos. Ver `references/hierarchical-planner-worker.md`.
- **Eliminação de Dependências Seriais:** por que coordenação plana colapsa, com os números da pesquisa que sustentam a arquitetura de duas camadas. Ver `references/eliminating-serial-dependencies.md`.
- **Coordenação de Agentes Simples:** o design das próprias ferramentas de despacho (Tool per Agent vs. Single Dispatch, descoberta progressiva). Ver `references/simple-agent-coordination.md`.

## Como Usar Esta Skill

1. Leia o Framework Mental (arquitetura de duas camadas) antes de abrir qualquer reference do ramo Multi-Agentes — é o pré-requisito que todos os cinco arquivos assumem.
2. Servidores e Deploy / Stack Tecnológica são independentes entre si e do Framework Mental — abra direto o arquivo relevante.
3. Se a pergunta for sobre *por que* um sistema multi-agente está degradando em vez de escalar, comece por `eliminating-serial-dependencies.md`.
4. Se a pergunta cruzar dois ramos (ex. "como o monorepo se relaciona com os worktrees dos workers"), sintetize a interseção — `monorepo-for-context.md` e `hierarchical-planner-worker.md` já se cross-referenciam para esse caso específico.
5. Para deploy, capacidade ou recuperação de ambiente, consulte `references/reproducible-infrastructure-and-capacity.md` antes de recomendar um provedor ou topologia.
6. Para interoperabilidade e compatibilidade entre agentes, leia `references/inter-agent-contracts.md`.

## Anti-Padrões de Escalabilidade

| Anti-Padrão | Sintoma / Risco | Ver |
|---|---|---|
| Coordenação Plana / Teams, não Tiers | Vários agentes de igual autoridade disputando o mesmo arquivo/ferramenta, gerando deadlock e aversão a risco | `references/eliminating-serial-dependencies.md`, `references/hierarchical-planner-worker.md` |
| Mais Agentes, Pior Resultado | Adicionar workers sem segregar contexto degrada a precisão em vez de melhorá-la | `references/eliminating-serial-dependencies.md` |
| Worker com Contexto Global | Sub-agente recebe visão do repositório inteiro para uma tarefa cirúrgica, causa scope creep e conflito | `references/hierarchical-planner-worker.md`, `references/task-decomposition-and-verification.md` |
| Paralelizar Sem Verificabilidade | Decompor um domínio sem critério objetivo de sucesso — throughput sem confiabilidade | `references/task-decomposition-and-verification.md` |
| Catálogo de Ferramentas Inchado | Mais de ~10 ferramentas simultâneas degradando a acurácia de seleção de um agente | `references/eliminating-serial-dependencies.md`, `references/simple-agent-coordination.md` |
| Custo Gerenciado sem Modelo de Demanda | Depender de serviço de terceiro para volume que cresce sem acompanhar consumo e limites | `references/self-managed-compute.md`, `references/managed-platforms-and-cli-deploy.md` |
| Egress Surpresa | Mídia pesada servida por uma camada inadequada em vez de armazenamento e entrega especializados | `references/managed-platforms-and-cli-deploy.md` |
| Escrita Concorrente no Mesmo Diretório | Dois agentes editando a mesma pasta física simultaneamente, gerando conflito de merge | `references/hierarchical-planner-worker.md`, `references/monorepo-for-context.md` |

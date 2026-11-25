# Tabela Comparativa: Building Blocks de um Agente

Fonte canônica única desta tabela — referenciada (não copiada) por `../references/skills-as-building-blocks.md`, `../references/subagents.md`, `../references/mcp.md` e pela seção "Building Blocks" do `SKILL.md`. Ajuda a decidir em qual peça de infraestrutura uma necessidade se encaixa, evitando sobreposição e desperdício de tokens.

| Building Block | O que provê ao agente | Persistência / escopo | Quando usar |
|---|---|---|---|
| **Prompt** | Instruções ad hoc e reativas em tempo de execução | Efêmero — apenas a conversa/turno atual | Refinamentos pontuais, comandos únicos (one-offs) |
| **Project (contexto de projeto)** | Dados estáticos de background e contexto corporativo global | Persistente no workspace ou na sessão do projeto | Regras estáticas, design systems, bases de conhecimento estáveis |
| **Skill (habilidade)** | Conhecimento processual e métodos de execução (SOPs) | Sólida e reutilizável entre múltiplas conversas e ferramentas | Processos que exigem consistência repetida, análise ou templates formais |
| **Subagent (sub-agente)** | Delegação e isolamento de contexto para tarefas focadas | Efêmero / sessões headless específicas | Tarefas cognitivas longas exigindo isolamento de contexto ou paralelismo |
| **MCP (Model Context Protocol)** | Conectividade física com bancos de dados, APIs e serviços externos | Conexão de infraestrutura viva | Quando o agente precisa ler ou gravar dados no mundo real |

**Regra de ouro:** o MCP conecta o agente aos dados onde eles residem; a Skill ensina o agente o que fazer de forma inteligente com esses dados. Um MCP de banco de dados dá acesso às tabelas; a skill de persistência ensina a aplicar os filtros certos para não estourar memória ou violar uma regra de negócio.

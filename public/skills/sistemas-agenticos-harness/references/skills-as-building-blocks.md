# Skills (Expertises Reutilizáveis)

Parte de **Building Blocks** (ver Framework Mental no `SKILL.md`). Uma Skill é um talento, técnica ou processo procedural empacotado que ensina um agente a desempenhar tarefas especializadas de forma consistente, confiável e barata — a representação agêntica do conhecimento e dos processos (SOPs) de uma organização. Reside no centro da **Information Layer** do harness.

Na analogia clássica de "duas frentes" da inteligência agêntica: **saber onde acessar** (conectores externos) é papel do MCP (ver `mcp.md`); **saber o que fazer** (conhecimento técnico imediato) é papel da Skill. Ela dita comportamento, regras de negócio, restrições de conformidade e a lógica de decisão a seguir.

## Anatomia técnica

Uma skill não é só uma instrução em texto — é uma estrutura de diretórios isolada que encapsula instruções e ferramentas de suporte:

```
/skills/nome-da-skill/
├── SKILL.md          ← arquivo de instrução mestre
├── /scripts/          ← execuções determinísticas (código)
├── /references/       ← guias estáticos e documentação de suporte
└── /assets/           ← templates, layouts, arquivos estáticos
```

O arquivo mestre tem duas seções rígidas:

1. **Frontmatter YAML (metadados):** contém as chaves de descoberta e carregamento — nome e descrição curta e densa de quando usar.
2. **Corpo em Markdown puro:** o desenvolvedor detalha, em linguagem natural rigorosa, restrições, passo a passo tático, lógica de decisão e limites daquela expertise.

## Progressive Disclosure (Lazy Loading)

Colocar centenas de instruções diretamente no prompt de sistema ativo é um erro crítico que causa Context Bloat e Context Rot (ver `context-injection.md`) — se o agente lê todas as regras e playbooks disponíveis a cada sessão, o contexto estoura antes mesmo do primeiro turno útil.

```
1. Inicialização do agente
   → lê só o nome + descrição curta de cada skill (dezenas de tokens no total)
2. Avaliação de relevância
   → o modelo julga se a tarefa ativa exige aquela expertise
3. Carregamento dinâmico (JIT), só se relevante
   → injeta o corpo completo de instruções (milhares de tokens)
```

- **Lazy Discovery:** ao iniciar a sessão, o harness lê apenas o frontmatter (nome + descrição) de todas as skills registradas.
- **Just-in-Time Loading:** o modelo avalia semanticamente a tarefa ativa; só quando a descrição de uma skill coincide com a necessidade, o harness injeta o corpo completo de instruções — mantendo o carregamento sob um teto seguro de tokens.

## Taxonomia: Procedures vs. Abilities

- **Procedures (procedimentos/comandos):** expertises de acionamento deliberado pelo usuário — "filtros mentais" que remodelam a postura do agente sob comando explícito. Exemplo: um comando que força o agente a agir como entrevistador técnico hostil para atacar as falhas de um plano antes de implementá-lo.
- **Abilities (habilidades de autoconsumo):** diretrizes que o próprio modelo descobre e lê de forma autônoma e silenciosa para se autoverificar. Exemplo: um guia de padrões de código que o agente consulta antes de escrever um arquivo, para garantir conformidade sem que ninguém precise pedir.

## Onde a Skill se encaixa entre os Building Blocks

Ver tabela completa em `../assets/building-blocks-comparison-table.md`. Regra de ouro: **o MCP conecta o agente aos dados externos; a Skill ensina o agente o que fazer com esses dados.** Um MCP de banco de dados dá acesso às tabelas; a skill de persistência ensina o agente a aplicar filtros de intervalo de data para evitar estouro de memória, por exemplo.

## Padrão de mercado: Open Agent Skills Standard

Skills tornaram-se um padrão aberto do ecossistema agêntico, interpretado por diferentes ambientes operacionais sem retrabalho. Como cada ferramenta pode buscar skills em uma pasta ligeiramente diferente, uma prática comum é usar **links simbólicos** para manter uma única fonte da verdade:

```bash
ln -s /workspace/.agents/skills/ /workspace/.outra-ferramenta/skills
```

Assim, ao atualizar uma skill em qualquer editor ou terminal, a melhoria propaga-se automaticamente para todas as ferramentas apontadas para a mesma pasta física.

## Criação autônoma de skills

Um ecossistema agêntico maduro pode fechar o loop de aprendizado: em vez de depender só de humanos para documentar novos procedimentos, o próprio harness observa execuções bem-sucedidas e compila novas skills.

### Gatilho e pipeline

```
EXECUÇÃO ATIVA DO AGENTE
  completa tarefa complexa em sandbox, gera trace de raciocínio e ferramentas
        │ (gatilho: muitas chamadas de ferramenta, erro superado, ou correção humana)
        ▼
GATEWAY DE QUARENTENA E CURADORIA
  1. Trace Analyzer   (identifica os passos que levaram ao sucesso)
  2. Schema Compiler  (estrutura o arquivo SKILL.md)
  3. Gotcha Compiler  (extrai falhas e regras negativas observadas)
        │
        ▼
ESTEIRA DE EVALS
  1. Suite de testes estruturais
  2. LLM-as-a-Judge (fidelidade e eficácia, contexto limpo)
  3. Merge na pasta global de skills
```

### Componentes-chave
- **Manifesto (`SKILL.md`):** metadados de nome, descrição, regras de ativação e escopo.
- **Seção de Gotchas:** considerada a parte de maior valor de uma skill — consolida os erros que o agente deve ativamente evitar, extraídos de execuções anteriores.
- **Log incremental de aprendizados:** registra cada correção de feedback do usuário, blindando a skill contra a repetição do mesmo erro.

### Governança por nível de risco
- **Nível A — Local Capability Uplift (baixo risco):** habilidades que otimizam rotinas internas, sem acesso externo. Escrita direta autorizada.
- **Nível B — Encoded Preference (risco médio):** habilidades que tocam sistemas de controle de versão ou envio de comunicações de teste. Entram em status de quarentena, exigem validação de um Judge e aprovação humana antes do merge.
- **Nível C — External Action (alto risco):** habilidades com escrita em sistemas de produção reais ou ações financeiras. Bloqueadas por padrão; exigem aprovação síncrona humana autenticada antes de qualquer execução.

### Riscos de segurança específicos
- **Jailbreak persistente:** diferente de uma injeção de prompt comum (que se limita à sessão ativa), se um agente com permissão de criação de skills em modo irrestrito for comprometido por conteúdo malicioso, ele pode compilar uma skill silenciosa que persiste fisicamente na pasta de skills — afetando todas as execuções futuras, mesmo depois do conteúdo malicioso original ter sido descartado.
- **Contaminação por marketplace de skills:** baixar skills de terceiros sem curadoria (lint estático, revisão) herda vulnerabilidades ocultas no pipeline local.

## Anti-padrões específicos de Skills

- **Skill Drift / Bloat:** permitir criação livre sem centralização gera dezenas de skills redundantes com escopos sobrepostos, confundindo o mecanismo de progressive disclosure e derrubando a precisão de ativação.
- **Unbounded Sandbox Tooling:** permitir que skills geradas dinamicamente instalem pacotes ou executem scripts fora de um ambiente isolado.
- **Violação da regra de maturidade de dependências:** integrar skills ou pacotes de repositórios externos publicados muito recentemente, sem tempo de maturação da comunidade — abre superfície para ataques de dia zero.

## Boas práticas de escrita

1. **Skills são um jogo infinito:** nunca estão "prontas". Ao notar o agente tomando caminhos errados, reverta, analise a causa raiz e atualize a skill para blindar execuções futuras contra a mesma falha.
2. **Defina contratos de entrada/saída claros:** trate a especificação como um contrato de API — o que a skill recebe, quais ferramentas determinísticas aciona, e qual o formato exato do resultado esperado.
3. **Encapsule scripts determinísticos:** para qualquer verificação exata (validar um JSON, rodar testes sintáticos), não peça ao modelo para verificar verbalmente — crie um script em `/scripts/` e instrua o agente a executá-lo, usando o feedback bruto do console para autoverificação.

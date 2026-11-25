# Arquitetura Hierárquica (Planejador/Trabalhador)

Parte de **Escalabilidade e Multi-Agentes** (ver Framework Mental no `SKILL.md` para a definição base da arquitetura de duas camadas, Workers Stay Ignorant e No Shared State). Este é o arquivo canônico da coleção para o ciclo de execução completo, o padrão Juiz com seus quatro vereditos, e o mecanismo físico de Git Worktrees — os outros quatro arquivos deste ramo (`task-decomposition-and-verification.md`, `parallelization-and-throughput.md`, `eliminating-serial-dependencies.md`, `simple-agent-coordination.md`) assumem este conteúdo como pré-lido e cross-referenciam em vez de repetir.

## O ciclo de execução em quatro fases

```
1. DECOMPOSIÇÃO   → o planejador analisa os requisitos e gera um plano de tarefas
2. PARALELIZAÇÃO  → o orquestrador dispara múltiplos workers para tarefas sem dependência entre si
3. VERIFICAÇÃO    → cada saída passa por uma porta de validação independente (o juiz)
4. ITERAÇÃO       → aprovado: consolida e avança. Rejeitado: devolve ao worker com o relatório de erro
```

Esse ciclo é gerido por código determinístico tradicional no orquestrador, não por mais uma camada de raciocínio de modelo — a decisão de "para quem delegar" e "quando avançar de fase" é lógica de software, não um julgamento probabilístico repetido a cada passo.

## Git Worktrees: isolamento físico de concorrência

Quando múltiplos workers alteram o mesmo repositório em paralelo, compartilhar o mesmo diretório físico gera colisão de escrita e resultados de merge catastróficos.

```
REPOSITÓRIO CENTRAL
        │
   ┌────┴────┐
   ▼         ▼
worktree-A  worktree-B
branch:      branch:
feature/x    feature/y
```

Cada worker recebe uma pasta física isolada, ligada ao mesmo repositório central por uma branch dedicada. Cada um edita, testa e compila de forma estéril na própria pasta, sem interferência cruzada. O merge para a branch principal só acontece depois que ambos atingem status "verde" nos testes locais — e é resolvido de forma assíncrona pelo sistema, nunca pelo worker ativo.

## O padrão Juiz (LLM-as-a-Judge) com quatro vereditos

Atribuir a auditoria de qualidade ao mesmo agente que produziu o artefato é um erro de design — ele desenvolve viés de confirmação e tende a declarar a própria entrega como perfeita. A solução é uma revisão cega e adversária:

- **O Juiz:** um agente separado, com contexto totalmente limpo, sem o histórico de criação, avaliando estritamente contra os critérios objetivos definidos previamente (a "definição de concluído" da tarefa).
- **Quatro vereditos possíveis** — não apenas aprovar/rejeitar, que trava fluxos complexos:
  1. **Aprovar:** conformidade total, pode ser integrado.
  2. **Rejeitar:** viola regra crítica, descartado imediatamente.
  3. **Solicitar revisão:** falhas menores, devolve um relatório estruturado para o worker ajustar.
  4. **Escalar para o operador:** ambiguidade profunda ou comportamento contraditório recorrente — suspende a automação e aciona um humano.

## Gestão de memória e handoff entre fases

Compartilhar histórico bruto de conversa entre etapas sobrecarrega a janela de contexto com ruído irrelevante. O worker anterior resume achados, alterações e dependências descobertas em um arquivo de handoff estruturado; o orquestrador descarta o histórico volátil e injeta na sandbox do próximo worker só esse resumo. Decisões arquiteturais tomadas ao longo do processo são registradas em um arquivo persistente fora da memória da sessão — se a sandbox cair, a nova instância lê o estado salvo e retoma exatamente do ponto onde parou, sem repetir trabalho já feito.

## Observabilidade

Ver `../assets/agentic-observability-metrics.md` para as métricas de Completion Rate, Correction Rate e o Agent Run ID unificado.

## Trade-offs

1. **Orquestração em código vs. flexibilidade da IA:** decisões de fluxo em código tradicional economizam tokens e garantem previsibilidade, mas removem a capacidade de adaptação dinâmica a obstáculos imprevistos sem intervenção humana.
2. **Isolamento máximo vs. latência de inicialização:** sandboxes efêmeras por worker bloqueiam ataques persistentes de injeção, mas cada fan-out paga o custo de reinstalar dependências do zero.
3. **Fadiga de aprovação vs. risco autônomo:** o equilíbrio é a Autonomia Delimitada — passe livre para ler/rascunhar em sandbox isolada; ações de impacto externo real exigem confirmação humana explícita. Ver a skill de Segurança e Confiabilidade desta coleção, se disponível, para o modelo de risco completo.

## Checklist

- O ciclo de quatro fases (decompor/paralelizar/verificar/iterar) é orquestrado por código determinístico, não por um agente decidindo a cada passo.
- Todo worker paralelo opera em um worktree físico isolado, nunca no mesmo diretório que outro worker ativo.
- O Juiz nunca é a mesma instância/contexto que produziu o artefato sendo avaliado.
- O Juiz tem os quatro vereditos disponíveis, não só aprovar/rejeitar binário.
- Handoff entre fases é sempre um resumo estruturado em arquivo, nunca histórico de conversa bruto.

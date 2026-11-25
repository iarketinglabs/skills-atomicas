# Sessões Focadas por Tarefa

Parte de **Manutenção de Contexto** (ver Framework Mental no `SKILL.md`). Enquanto `handoff-documentation.md` cobre o que vai dentro de um handoff, este arquivo cobre a disciplina que determina **quando** uma sessão deve terminar e uma nova começar.

## A regra áurea: "Nova Tarefa, Nova Sessão"

O maior responsável por faturas infladas e vazamento silencioso de tokens é a "conversa imortal" — manter uma única thread aberta por dias para tarefas tecnicamente distintas entre si.

```
CONVERSA IMORTAL (colapso cognitivo)
[Bug CSS] ──► [Refatoração SQL] ──► [Integração de Pagamento] ──► DUMB ZONE
(o modelo carrega o ruído do layout visual tentando resolver lógica bancária)

SESSÕES FOCADAS POR TAREFA (o padrão correto)
Sessão 1: [Bug CSS]        ──► conclusão ──► reset de contexto
Sessão 2: [Refatoração SQL] ──► conclusão ──► reset de contexto
Sessão 3: [Pagamento]       ──► conclusão ──► reset de contexto
```

Três regras não-negociáveis:
1. **Isolamento de escopo semântico:** cada sessão foca estritamente em um ticket ou issue atômica.
2. **Reset físico como ritual de encerramento:** ao terminar e passar nos testes, o progresso é commitado, e o contexto é resetado por completo — não deixado "aberto por precaução".
3. **Proibição de poluição por mudança de foco:** nunca reaproveitar uma thread de depuração de banco para começar o design visual de um componente. O excesso de metadados invisíveis confunde a árvore de predição do modelo.

## O workflow do handoff como checkpoint de troca de sessão

```
SESSÃO ATIVA (contexto grande)
        │ 1. gera o resumo de handoff (ver handoff-documentation.md)
        ▼
THREAD DESTRUÍDA (reset total do contexto)
        │ 2. reset físico
        ▼
SESSÃO NOVA (contexto zerado)
        │ 3. cola o handoff, retoma com foco cognitivo máximo
```

A matemática financeira é favorável: a nova thread reinicia limpa, o prefixo estático ainda se beneficia do cache (ver `prompt-caching-and-stable-context.md`), e o modelo herda acurácia máxima sem carregar nenhum ruído de turnos anteriores de depuração.

## Fracionamento e execução paralela headless

Para especificações grandes com dezenas de funcionalidades, tentar empurrar todo o escopo de uma vez causa falha por saturação. A solução é fatiar deterministicamente em fases pequenas, cada uma mantida abaixo de uma fração segura da janela de contexto (referência de mercado: manter o uso abaixo de ~50% da capacidade), e despachar cada fase como uma execução headless independente em background, não como um chat interativo contínuo:

1. O orquestrador mestre avalia a especificação e a fatia em fases metódicas.
2. Cada fase é despachada como uma execução isolada e assíncrona, com contexto totalmente novo.
3. A sessão em background inicializa limpa, escreve o código da fase, passa pelas verificações sintáticas, reporta um resumo de progresso ao orquestrador e é destruída — nunca acumula estado entre fases.
4. O orquestrador lê a aprovação de status e inicia a próxima fase do zero, repetindo o ciclo até a entrega completa.

## Isolamento físico para sessões paralelas: Git Worktrees

Quando múltiplas sessões (ou sub-agentes) rodam em paralelo no mesmo repositório, o risco é cross-contaminação de arquivos e conflitos de versionamento concorrentes. A barreira física: cada sessão paralela recebe uma pasta de trabalho isolada, ligada ao mesmo repositório central através de um worktree — cada uma edita, testa e depura de forma estéril em seu próprio diretório, sem interferência cruzada. Só depois de ambas atingirem status "verde" nos testes locais é que as alterações são consolidadas em um merge controlado.

## Checklist

- Nenhuma sessão mistura dois focos semânticos distintos — mudança de escopo sempre implica reset de contexto.
- Reset de contexto acontece como ritual de encerramento, sempre precedido por um handoff salvo em disco.
- Projetos grandes são fatiados em fases headless com contexto limpo cada, mantendo o uso de janela abaixo do limiar seguro.
- Sessões/sub-agentes paralelos no mesmo repositório usam worktrees isolados, nunca compartilham o mesmo diretório de trabalho.

# Handoff Documentation

Parte de **Manutenção de Contexto** (ver Framework Mental no `SKILL.md`). Enquanto `focused-task-sessions.md` cobre **quando** disparar um handoff, este arquivo cobre **o que** deve estar dentro dele e como ele sustenta a continuidade entre ferramentas de agente diferentes.

## Por que a documentação de handoff é a única memória real

Modelos são estocásticos e sem estado permanente — cada nova sessão começa do zero. Tratar o histórico de uma conversa como uma "thread infinita" sem manutenção estruturada é um convite ao desperdício financeiro e à falha cognitiva. O handoff é o mecanismo que transfere conhecimento de uma sessão fadada ao esquecimento para um artefato físico e persistente.

## Anatomia de um handoff de alta densidade

Ver o template completo em `../assets/handoff-template.md`. Um handoff funciona como um "compilador de estado": conciso, direto, sem preâmbulos, traduzindo progresso em dados puramente acionáveis. Os quatro componentes:

1. **Progresso Concluído:** alterações já integradas, testes que passaram, diffs gerados.
2. **Estado do Workspace:** o mapa físico de onde os arquivos e recursos ativos estão — o que a próxima sessão precisa saber para não perder tempo reexplorando.
3. **Decisões Diferidas:** os "porquês" por trás de escolhas técnicas — escolhas de banco, edge cases de segurança mapeados — poupando a próxima sessão de precisar adivinhar a estratégia.
4. **Próximos Passos:** checklist sequencial acionável, com critério de parada explícito.

## /compact vs. Session Handoff

| | Compactação nativa | Session Handoff |
|---|---|---|
| Processamento | Síncrono e lento (chamada de API) | Rápido (<1 minuto) |
| Precisão | Compressão probabilística, perde detalhe fino | Estrutura fixa preserva decisões |
| Efeito no cache | Não reseta o cache — apenas encolhe o histórico | Reset total — zera o cache físico na raiz |

Ver o detalhamento completo das patologias da compactação nativa em `compaction-and-clipping.md`. Aqui o ponto central é: o handoff não é uma versão mais rápida da compactação — é uma estratégia estruturalmente diferente, que troca "resumir o que existe" por "recomeçar do zero com só o que importa".

## Sincronização entre agentes: a camada de memória soberana

Um dos maiores erros táticos é deixar o histórico de evolução de um sistema refém dos servidores fechados de um único fornecedor de chat.

```
     Ferramenta A                    Ferramenta B
          │ escreve handoff                ▲ lê handoff
          ▼                                 │
        CAMADA DE CONTEXTO SOBERANA
   (arquivo Markdown local / banco leve local)
```

Toda alteração de estado concluída pelo agente é escrita de forma transparente em um arquivo Markdown local (não em um histórico de chat proprietário) ou em um banco leve local. Se a conexão com um provedor cair ou a cota de uso estourar no meio do dia, o progresso não é perdido — como as diretrizes, arquivos ativos e decisões residem localmente, é possível abrir imediatamente outra ferramenta de agente apontando para o mesmo diretório. A nova ferramenta lê o arquivo de memória just-in-time e continua a execução exatamente de onde a anterior parou, com integridade total.

## Fracionamento de projetos grandes via handoff em cascata

Para especificações grandes, contendo dezenas de funcionalidades, empurrar todo o escopo para uma única sessão causa falhas por saturação. A solução é fracionar em fases perfeitamente desacopladas, cada uma iniciada com contexto limpo:

```
ORQUESTRADOR MESTRE DE CONTEXTO
         │
         ├─► Fase 1: [Auth]     → sessão headless com contexto novo
         ├─► Fase 2: [Billing]  → sessão headless com contexto novo
         └─► Fase 3: [Security] → sessão headless com contexto novo
```

Cada fase roda em uma sessão isolada (potencialmente em background, sem interação direta), consome o handoff da fase anterior como único contexto herdado, escreve seu próprio handoff ao concluir, e é destruída. O orquestrador mestre nunca acumula o detalhe de execução de cada fase — só orquestra a sequência.

## Checklist

- Todo handoff segue os quatro componentes do template — nunca um resumo livre e não estruturado.
- O handoff é salvo em disco antes de a sessão ser encerrada, não só mantido na memória da conversa.
- Projetos grandes são fracionados em fases com handoff em cascata, não empurrados de uma vez para uma única sessão.
- O arquivo de memória local permite trocar de ferramenta de agente sem perda de continuidade.

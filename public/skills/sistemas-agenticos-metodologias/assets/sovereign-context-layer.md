# Camada de Contexto Soberana (Sovereign Context Layer)

Fonte canônica única deste padrão — referenciada (não copiada) por `../references/architecture-md.md`, `../references/specs-for-persistence.md` e `../references/directives.md`. Resolve a fragilidade de deixar toda a memória de evolução de um projeto refém do histórico de chat de um único fornecedor de IA em nuvem.

## O problema

Se as decisões de arquitetura, o progresso de tarefas e as regras do repositório existem só dentro do histórico de uma conversa hospedada na nuvem de um provedor, o projeto fica vulnerável: uma oscilação de rede, um limite de cota atingido no meio do expediente, ou a simples vontade de trocar de ferramenta de agente, custam a perda do contexto acumulado — forçando a reconstrução cara do entendimento do zero.

## O mecanismo

```
                  DIRETÓRIO SOBERANO (no disco local)
   ┌──────────────────────────────────────────────────────────┐
   │  arquivo de regras (constituição fixa do repositório)     │
   │  memory.md (histórico de decisões e progresso)             │
   │  spec.md / specs.md (especificação técnica ativa)          │
   └───────────────────────────┬────────────────────────────────┘
                                │ leitura soberana, na inicialização
              ┌─────────────────┼─────────────────┐
              ▼                 ▼                 ▼
        Ferramenta A      Ferramenta B      Ferramenta C
```

Todo o estado que importa — regras permanentes, decisões tomadas, progresso ativo — é persistido como arquivos Markdown simples no disco do repositório, não só na memória de uma conversa. Isso torna o desenvolvimento **model-agnostic** (independente de qual ferramenta de agente está sendo usada no momento):

1. Se a ferramenta ativa ficar lenta, atingir um limite de uso, ou simplesmente parar de funcionar, a conexão pode ser encerrada sem perda.
2. Uma ferramenta alternativa é aberta apontando para o mesmo diretório.
3. A nova ferramenta lê os arquivos de regras, memória e especificação já na primeira mensagem.
4. O trabalho continua exatamente do ponto onde parou, sem retrabalho nem redescoberta cara de contexto.

## Checklist

- Nenhuma decisão de arquitetura ou regra de negócio vive só dentro de uma conversa — tudo relevante está persistido em arquivo.
- O diretório soberano é versionado no repositório (ou ao menos mantido localmente), não apenas na nuvem de um fornecedor.
- Trocar de ferramenta de agente no meio de um projeto é uma operação de baixo custo, não uma reconstrução de contexto do zero.

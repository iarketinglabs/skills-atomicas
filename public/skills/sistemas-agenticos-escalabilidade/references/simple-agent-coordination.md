# Coordenação de Agentes Simples

Parte de **Escalabilidade e Multi-Agentes** (ver Framework Mental no `SKILL.md` e o ciclo completo em `hierarchical-planner-worker.md`). O foco aqui é no design das ferramentas de despacho em si — como o planejador invoca e descobre workers — não na arquitetura de camadas (já coberta) nem no throughput (já coberto).

## Tool per Agent vs. Single Dispatch Tool

Duas abordagens de design para como o planejador aciona sub-agentes:

- **Tool per Agent (uma ferramenta por agente):** o planejador tem uma ferramenta dedicada e parametrizada para cada tipo de sub-agente (uma para pesquisa, outra para codificação, etc.). Dá controle granular extremo — é possível filtrar e redigir dados de entrada/saída de forma personalizada por tipo de sub-agente.
- **Single Dispatch Tool (ferramenta de despacho único):** o planejador gerencia uma única ferramenta de tarefas genérica, passando o nome do sub-agente desejado como um parâmetro da chamada. Mais simples de manter e mais portável entre diferentes ambientes de execução — o padrão de alta performance mais comum na prática.

Nenhuma é universalmente superior: `Tool per Agent` vale a pena quando cada tipo de sub-agente precisa de filtragem de dados muito específica; `Single Dispatch Tool` vence quando o catálogo de sub-agentes cresce e precisa ser portável.

## Descoberta dinâmica via progressive disclosure

Injetar de imediato os detalhes e instruções de dezenas de sub-agentes na inicialização satura a janela de contexto e degrada a acurácia de seleção. A alternativa: o planejador carrega só um índice mínimo (nomes e descrições curtas) mais uma ferramenta utilitária de busca de agentes. Quando precisa delegar, ele consulta esse índice semanticamente e só então importa a especificação detalhada do sub-agente escolhido para o contexto — no momento exato do disparo, não antes.

```
inicialização: só nomes + descrições curtas dos sub-agentes disponíveis
        │
        ▼ (planejador identifica a subtarefa)
consulta ao índice de agentes ──► localiza o especialista qualificado
        │
        ▼
importa a especificação completa SÓ daquele sub-agente, só agora
```

## Modos de colaboração: Single-turn vs. Task Mode

- **Single-turn:** o sub-agente recebe a instrução, executa, retorna o resultado consolidado e encerra a sessão imediatamente — o controle volta ao coordenador automaticamente, sem intervenção manual.
- **Task Mode:** para tarefas de complexidade média onde o worker pode precisar de esclarecimento operacional, ele pode pausar e fazer uma pergunta proativa ao operador humano. Ainda assim, assim que a tarefa é dada como concluída, o fluxo de controle retorna obrigatoriamente ao planejador — o modo Task não abre uma conversa livre e indefinida.

## Implementação de referência: despacho com porta de qualidade

```python
class DeterministicCoordinator:
    async def dispatch_parallel_tasks(self, plan_tasks):
        async def worker_lifecycle(task):
            worker = EphemeralWorker(worker_id=f"worker_{task['id']}")
            raw = await worker.execute_isolated_task(task["desc"], task["context"])
            if quality_gate_audit(raw):
                return {"task_id": task["id"], "result": raw}
            return {"task_id": task["id"], "result": "REJECTED_BY_HARNESS"}

        return await asyncio.gather(*(worker_lifecycle(t) for t in plan_tasks))
```

Cada worker é instanciado sob demanda, recebe só o contexto da própria subtarefa (nunca a visão global do planejador), e o resultado passa por uma porta de qualidade antes de ser aceito de volta pelo coordenador.

## Observabilidade

Ver `../assets/agentic-observability-metrics.md`.

## Checklist

- A escolha entre Tool per Agent e Single Dispatch Tool foi deliberada, com base em quantos tipos de sub-agente existem e se cada um precisa de filtragem própria.
- O catálogo de sub-agentes é descoberto via índice mínimo + busca dinâmica, não injetado por completo na inicialização.
- Sub-agentes em modo single-turn nunca ficam "esperando" o próximo comando — devolvem o controle automaticamente ao terminar.
- Task Mode permite pergunta proativa, mas sempre devolve o controle ao coordenador ao final — nunca vira uma sessão aberta indefinidamente.

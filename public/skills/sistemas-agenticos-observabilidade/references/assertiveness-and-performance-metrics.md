# Métricas de Assertividade e Performance

Parte de **Observabilidade e Melhoria Contínua** (ver Framework Mental no `SKILL.md`, e `tracing-inputs-outputs.md` para a arquitetura de spans que alimenta estas métricas). A taxonomia completa de o que medir uma vez que a instrumentação está em pé.

## Por que métricas de software tradicional falham com agentes

No desenvolvimento tradicional, assertividade se mede com testes determinísticos: entrada fixa, saída fixa. Agentes desafiam isso de duas formas:

- **Multiplicidade de caminhos:** um agente pode resolver o mesmo problema com sequências de ferramentas completamente distintas. Comparar a execução contra um único caminho pré-definido gera falsos negativos em massa.
- **Falha silenciosa (soft failure):** diferente de uma exceção que quebra o programa, um agente falha de forma gramaticalmente impecável — gera texto bem formatado, código que compila, mas com erro lógico grave, alucinação de API inexistente, ou violação silenciosa de uma premissa de arquitetura.

Sem um ecossistema estruturado de scaffolding e avaliação sistemática, a taxa de falha de agentes em tarefas de trabalho real é alta — o objetivo da engenharia de observabilidade é fazer o comportamento de um sistema fundamentalmente probabilístico convergir para um nível de confiabilidade equivalente ao de uma máquina de estados determinística.

## Os três eixos da telemetria de produção

```
SANDBOX OPERACIONAL DO AGENTE
        │ dados de execução brutos
        ▼
INTERCEPTADOR DE TELEMETRIA
  1. Metrics Harvester   (spans, CPU, latência)
  2. Tool Activity Monitor (frequência e status de I/O)
  3. Cost Estimator       (consumo e faturamento de tokens)
        │ payload sanitizado e estruturado
        ▼
COFRE DE OBSERVABILIDADE (persistente, indexado por Agent Run ID)
```

1. **Dados de assertividade (o quê):** status de conclusão da meta, taxa de acerto de ferramenta, conformidade de schema de saída, score de alinhamento lógico do Juiz.
2. **Dados de performance de recursos (como):** tempo de resposta por token, latência de execução de ferramentas, consumo de memória/CPU da sandbox.
3. **Dados de economia (quanto):** faturamento cumulativo de tokens, taxa de acerto de cache de prompt, custo financeiro consolidado da run.

## Taxonomia de métricas

### Assertividade
- **Task Completion Rate / Goal Attainment:** percentual de execuções em que o agente atingiu o objetivo dentro do teto de tempo e custo estabelecido.
- **Tool Selection Precision & Recall:** o agente escolheu a ferramenta certa? Falsos positivos = ferramentas desnecessárias poluindo o contexto; falsos negativos = tentar emular manualmente algo que uma ferramenta já resolveria melhor.
- **Schema and Constraint Compliance Rate:** percentual de saídas que aderem rigorosamente aos limites sintáticos esperados (schema validado, restrições de banco, testes sem alerta).

### Performance
- **TTFT / TBT:** tempo até o primeiro token e tempo entre tokens — crucial para avaliar se a infraestrutura de inferência (local ou em nuvem) está entregando latência aceitável.
- **Prompt Cache Efficiency Ratio:** proporção de tokens de entrada reaproveitados do cache — indica se a montagem do prompt está segregando corretamente o histórico volátil dos componentes estáveis (referência de mercado: deve superar ~60% em sessões longas).
- **Loop Depth & Stuck Run Ratio:** número de passos consecutivos antes de concluir ou falhar. Runs que ultrapassam um limite saudável de passos disparam o disjuntor de segurança e são categorizadas como falha de infraestrutura, não de raciocínio.
- **Cost per Resolved Goal:** o custo financeiro total (entrada + saída + cache) para entregar uma tarefa macro concluída com sucesso — a métrica principal para justificar o retorno de investimento da automação.

## Implementação de referência: circuit breaker e dashboard de KPI

```python
class AgentExecutionMetricsCollector:
    def __init__(self, run_id, max_allowed_steps=15):
        self.run_id = run_id
        self.max_allowed_steps = max_allowed_steps
        self.total_tool_calls = 0
        self.failed_tool_calls = 0

    def register_step(self, step_number, tool_success=True, **token_counts):
        if step_number > self.max_allowed_steps:
            raise RuntimeError("CircuitBreakerTriggered: stuck loop detectado.")
        self.total_tool_calls += 1
        if not tool_success:
            self.failed_tool_calls += 1

    def generate_kpi_dashboard(self, task_completed, evaluation_score):
        tool_accuracy = (self.total_tool_calls - self.failed_tool_calls) / max(1, self.total_tool_calls)
        return {
            "goal_attained": task_completed,
            "llm_judge_score": evaluation_score,
            "tool_accuracy_rate": round(tool_accuracy * 100, 2),
        }
```

O disjuntor de segurança (circuit breaker) é o mecanismo físico que impede que um loop de erro se transforme em uma fatura descontrolada — ele trava a execução antes que o passo N+1 aconteça, não depois.

## Avaliação com LLM-as-a-Judge

Toda resposta estratégica passa por uma porta de qualidade baseada em um avaliador independente antes de qualquer ação de impacto real. Ver o padrão completo (independência de contexto, tríade de qualidade, instrução "enumerate-only") em `../assets/llm-as-a-judge-pattern.md`.

## O ciclo de melhoria contínua

As métricas coletadas aqui são o insumo direto do ciclo de curadoria de exemplos e fine-tuning. Ver `../assets/continuous-improvement-loop.md`.

## Resposta a incidentes por desvio de métrica

Quando uma métrica monitorada cruza um limiar de anomalia (ex. muitas chamadas de ferramenta consecutivas sem progresso, ou custo da sessão atingindo o teto do orçamento diário), o gateway de observabilidade deve disparar contenção automática. Esse é o mesmo playbook de resposta a incidentes (kill switch, revogação de credenciais em minutos) já detalhado na skill de Segurança e Confiabilidade desta coleção, se disponível — aqui a métrica é o gatilho, não o mecanismo de contenção em si.

## Checklist

- Toda run tem um disjuntor de segurança configurado com um teto explícito de passos consecutivos.
- Métricas de assertividade, performance e custo são coletadas nos três eixos, não só uma dimensão isolada.
- O Juiz que avalia assertividade roda com contexto limpo e família de modelo distinta do agente avaliado.
- Um desvio de métrica aciona contenção automática, não só um alerta passivo para revisão manual posterior.

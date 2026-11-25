# Paralelização para Ganho de Throughput

Parte de **Escalabilidade e Multi-Agentes** (ver Framework Mental no `SKILL.md` e o ciclo completo em `hierarchical-planner-worker.md`). Como converter tempo de espera sequencial em tempo de execução concorrente — e três padrões distintos de coordenação para fazer isso.

## Throughput como métrica de conversão de computação

Um processo de enriquecimento de dados que levaria dezenas de horas para rodar de forma sequencial em um único agente pode ser concluído em poucos minutos com uma frota de workers paralelos — não porque cada worker é mais inteligente, mas porque a tarefa foi fatiada em partes sem dependência sequencial entre si (ver `task-decomposition-and-verification.md` para o critério de quando isso é seguro).

## Três padrões de coordenação paralela

### Parallel Batching (Fanning-Out)
Para conjuntos de dados extensos e homogêneos, fatiados em blocos e distribuídos para uma frota de workers idênticos. Exemplo: um lote de centenas de registros a qualificar é segmentado em blocos menores; cada worker processa seu bloco com uma ferramenta idêntica; os resumos estruturados são emendados de volta ao final — sem poluir o contexto do supervisor com o ruído de cada execução individual.

### Consenso Estocástico Multi-Agente
Aproveita a variação inerente de modelos de linguagem para mapear um espaço de soluções mais amplo e encontrar ideias fora da curva. Em vez de uma única chamada, o harness dispara concorrentemente várias instâncias do mesmo modelo, cada uma com uma pequena variação de enquadramento no prompt. As saídas independentes retornam a um agregador que calcula a convergência lógica entre elas — permitindo decisões com confiança estatística mais alta do que uma única resposta isolada forneceria.

### Debate Multi-Agente
Modelos entregam respostas mais ricas e menos enviesadas quando colocados em oposição estratégica controlada. O harness instancia sub-agentes com personas contrastantes (ex. um cético, um otimista, um pragmático) que registram argumentos em um arquivo compartilhado estruturado, em turnos. O debate força a identificação de furos de segurança e lacunas lógicas que uma única passagem não revelaria, e o supervisor consolida o resultado refinado ao final.

## Implementação de referência: batching com cascade fallback

```python
async def process_batch_parallel(task_batch):
    async def run_with_fallback(task):
        for tier in model_hierarchy:  # do mais barato ao mais capaz
            raw_response = await worker_execute(tier, task)
            if quality_gate_passes(raw_response):
                return {"task_id": task["id"], "resolved_by": tier}
        return {"task_id": task["id"], "outcome": "ESCALATED_TO_HUMAN"}

    return await asyncio.gather(*(run_with_fallback(t) for t in task_batch))
```

Cada item do lote é processado de forma independente e concorrente; se o modelo mais barato falhar na porta de qualidade, escala para o próximo nível — sem bloquear o processamento dos outros itens do lote.

## Verificação em escala

Ler manualmente o log de dezenas de workers concorrentes é inviável — a verificação precisa ser automatizada via porta de qualidade determinística (ver `hierarchical-planner-worker.md` para o padrão Juiz completo). Sem isso, paralelizar só multiplica a velocidade com que erros silenciosos se acumulam.

## Segurança na execução paralela

Cada worker deve rodar sob identidade temporária própria, herdando estritamente as permissões da subtarefa — nunca uma chave mestra global. Tráfego de saída de um enxame paralelo deve passar por rede controlada, para que uma injeção de prompt em um worker não consiga exfiltrar dados livremente. Ver o desenvolvimento completo desses controles na skill de Segurança e Confiabilidade desta coleção, se disponível.

## Observabilidade

Ver `../assets/agentic-observability-metrics.md` para Completion Rate, Correction Rate e o Agent Run ID unificado — essenciais para auditar um enxame que roda fora da vista direta do operador.

## Trade-offs

- **Paralelismo vs. custo:** disparar dezenas de workers aumenta throughput drasticamente, mas infla o consumo de tokens proporcionalmente — reserve para tarefas de alto valor onde a latência serial é o gargalo real, não para tudo por padrão.
- **Efemeridade vs. latência de inicialização:** destruir a sandbox a cada worker protege contra persistência de ataque, mas cada fan-out paga custo de reinicialização de dependências.

## Checklist

- Antes de paralelizar, o problema já foi confirmado como verificável e decomposto sem dependência serial entre as partes.
- Existe uma porta de qualidade automatizada consolidando os resultados — não revisão manual de cada saída individual.
- Cada worker paralelo tem identidade e permissões escopadas à própria subtarefa.
- O padrão de coordenação (batching, consenso estocástico, ou debate) foi escolhido deliberadamente, não por padrão.

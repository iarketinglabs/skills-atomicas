# Learning Loops de Auto-aperfeiçoamento

Parte de **Memória e Aprendizado de Longo Prazo** (ver Framework Mental no `SKILL.md`). Enquanto `holographic-memory-local.md` trata de reter fatos, este arquivo trata de algo mais ambicioso: como o próprio comportamento cognitivo do agente — seus prompts e sua biblioteca de procedimentos — evolui sozinho, sem um humano tunando manualmente cada regressão.

## Três gerações de engenharia

1. **Engenharia estática:** um humano escreve um prompt de sistema volumoso com diretrizes rígidas. Conforme novos casos de uso se acumulam, o prompt vira um emaranhado de regras que degrada a atenção do modelo.
2. **RAG e memória tradicional:** o agente grava transcrições brutas em bancos de busca semântica e as recupera na consulta — gastando processamento para *rederivar* conhecimento a cada requisição, em vez de compilá-lo estruturalmente.
3. **Learning loops de auto-aperfeiçoamento:** o sistema opera sob um duto fechado. Ao concluir uma tarefa não trivial, o agente avalia seu próprio rastro de execução, identifica caminhos ineficientes, extrai a essência do caminho bem-sucedido e escreve deterministicamente novas regras ou sub-skills — sem intervenção humana síncrona.

## O tripleto que define um loop fechado seguro

Um loop de auto-aperfeiçoamento só é seguro para rodar sem supervisão constante se define, de forma explícita e determinística, três primitivas:

- **Uma superfície editável:** um único arquivo imutável contendo o prompt de sistema ou a lógica de decisão que pode ser mutado.
- **Uma métrica escalar objetiva:** uma função de avaliação automática capaz de dizer, sem julgamento humano síncrono, se a mudança foi melhor ou pior.
- **Um orçamento de recursos fixo:** um teto rígido de tokens, tempo de execução e número de iterações por ciclo — para impedir que o loop entre em uma espiral descontrolada de tentativas.

Sem os três definidos ao mesmo tempo, o sistema não tem como saber, de forma confiável, se está de fato melhorando.

## Por que o mesmo agente não pode se auto-avaliar

Testes empíricos mostram que fazer um único agente executar a tarefa **e** avaliar/reescrever sua própria lógica falha de forma consistente: a sobreposição de papéis cria viés — o agente tende a validar de forma complacente seus próprios caminhos de raciocínio errôneos, além de inflar a janela de contexto da sessão.

```
META-AGENTE (Optimizer)  ◄──►  REPOSITÓRIO DE APRENDIZADO (versionado)
        │ injeta prompt/skill mutada
        ▼
AGENTE DE TAREFA (Actor)  ──►  executa na sandbox, emite o rastro completo
        │
        ▼
JUIZ (contexto isolado)  ──►  avalia contra casos de teste, calcula o score
```

- **Agente de Tarefa (Actor):** especialista de domínio, executa as ações físicas sob as regras vigentes.
- **Meta-Agente (Optimizer):** monitora as trajetórias do Actor, diagnostica falhas estruturais, propõe mutações no prompt e compila novas skills — nunca executa a tarefa de produção diretamente.
- **Juiz:** roda com contexto limpo, avalia a mudança contra um conjunto de casos de referência (golden cases) antes de qualquer commit.

Um dado empírico relevante: um Meta-Agente construído sob a mesma família de modelo do Agente de Tarefa performa melhor — compreende implicitamente os vieses de atenção e os padrões de falha comuns daquele modelo específico.

## O ciclo de commit-ou-reversão

```python
def run_optimization_cycle(best_prompt, best_score, max_runs):
    for _ in range(max_runs):
        candidate = propose_mutation(best_prompt, failed_traces=get_last_failures())
        candidate_score = evaluate_against_golden_cases(candidate)
        if candidate_score > best_score:
            best_prompt, best_score = candidate, candidate_score  # commit
        # senão: descarta o candidato, mantém o baseline anterior
    return best_prompt, best_score
```

O princípio central: nenhuma mutação é aceita por padrão — só sobrevive se supera objetivamente o baseline anterior contra o mesmo conjunto de testes.

## Skill Drift: o custo de rodar 24 horas por dia

Um loop de auto-aperfeiçoamento operando continuamente acumula, com o tempo, dezenas de variantes de skill com descrições e objetivos sobrepostos — o repositório colide sintaticamente, o modelo não sabe mais qual variante acionar, e a taxa de erro sobe em vez de cair. A consolidação que evita isso é o mesmo ciclo de sleep-time descrito no Framework Mental do `SKILL.md`, aplicado especificamente a prompts e skills: variantes cuja similaridade de intenção ultrapassa um limiar alto são fundidas em uma única versão consolidada, e variantes "frias" (sem uso recente) perdem prioridade de carregamento — ver o mecanismo completo de decaimento em `../assets/temporal-decay-and-trust-score.md`. A consolidação de skills propriamente dita, incluindo o pipeline de criação, é tratada em `autonomous-skill-creation.md`.

Um limite prático que sustenta esse ciclo: cada unidade de instrução deve caber sob um teto curto (algumas centenas de linhas), com o corpo completo carregado só sob demanda (revelação progressiva) — nunca despejado inteiro no prompt de sistema em toda sessão.

## Calibração de autonomia

Conforme o histórico de execuções aprovadas sem correção cresce, um agente pode ganhar mais liberdade de operar sem aprovação síncrona — e perder essa liberdade se uma execução recente foi rejeitada ou corrigida manualmente. Essa escala de calibração de autonomia por score de confiança histórica é tratada em profundidade na skill de Observabilidade e Melhoria Contínua desta coleção, se disponível no seu ambiente; aqui o ponto relevante é que o *loop de aprendizado* é a fonte primária do sinal que alimenta esse score — cada ciclo de commit-ou-reversão é, em si, um dado de confiabilidade histórica.

## Por que o rastro completo importa mais que o score final

Dar ao Meta-Agente apenas o resultado final de sucesso ou falha atrasa drasticamente a curva de melhoria. Para propor mutações cirúrgicas, o Meta-Agente precisa examinar os passos de raciocínio intermediários, as chamadas de ferramenta e os erros de console — sem esse rastro, as propostas de mutação se tornam mutação aleatória lenta em vez de correção dirigida.

```json
{
  "run_id": "run_opt_worker_02",
  "trajectory": {
    "thought_step_1": "...",
    "tool_invocation_1": {"result_status": "FAILED", "system_error": "..."},
    "thought_step_2": "..."
  },
  "evaluation": {
    "metric_score": 0.0,
    "failure_class": "IncorrectAssumption",
    "remediation_hypothesis": "..."
  }
}
```

## Trade-offs e anti-padrões

- **"Leaderboard Game" (exploração da métrica):** o Meta-Agente descobre uma brecha na avaliação e passa a reescrever prompts para burlar o validador — inflando o score artificialmente sem resolver o problema real. Mitigação: casos de teste ocultos que mudam a cada ciclo de build, para que a mutação não consiga se especializar em decorar o teste.
- **Consumo financeiro explosivo:** rodar loops recursivos em modelos de fronteira de alto custo pode drenar orçamento rapidamente. A engenharia eficiente usa modelos menores e dedicados para as tarefas repetitivas de avaliação e mutação, reservando o modelo de fronteira só para os casos que exigem raciocínio de alto nível.

## Checklist

- O tripleto (superfície editável, métrica escalar, orçamento fixo) está definido antes de qualquer loop rodar sem supervisão.
- Os papéis de execução (Actor) e otimização (Meta-Agente/Juiz) rodam em contextos separados, nunca no mesmo agente.
- Nenhuma mutação é aceita sem superar objetivamente o baseline anterior em um conjunto de testes de referência.
- O rastro completo de raciocínio é capturado, não só o score final — é o insumo que torna a próxima mutação dirigida em vez de aleatória.
- Existe um teste oculto e rotativo para impedir que o loop otimize a métrica em vez do objetivo real.

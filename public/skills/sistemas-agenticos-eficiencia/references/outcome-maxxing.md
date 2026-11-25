# Outcome Maxxing

Parte de **Token Efficiency** (ver Framework Mental no `SKILL.md`). A filosofia que reposiciona a pergunta de "quantos tokens gastamos" para "que resultado esse gasto comprou" — o pré-requisito estratégico antes de aplicar qualquer técnica tática das outras references desta skill.

## O ciclo Token Maxxing → Token Anxiety

Quando o acesso a modelos de IA é subsidiado ou parece ilimitado, organizações caem em **"Token Maxxing"**: métricas de atividade (volume bruto de tokens consumidos, número de commits) viram indicador de produtividade — um erro caro. Casos documentados de mercado incluem times inteiros queimando orçamentos anuais de IA em poucos meses, e faturas de centenas de milhares de dólares geradas por falta de monitoramento de limites operacionais de agentes.

Quando os subsídios encolhem, o pêndulo bate para o outro extremo: **"Token Anxiety"**. Colaboradores se autocensuram, com medo de que um prompt ambicioso esgote a cota. O resultado é igualmente destrutivo: *"o token mais caro do mercado é aquele que o seu melhor colaborador tem medo de gastar."*

## A fórmula do Outcome Maxxing

```
IA por Outcome = Estratégia
```

Se você não consegue explicar, em uma frase, qual resultado tangível e recorrente uma automação de IA entrega, você não tem uma estratégia de IA — tem Token Maxxing disfarçado. Métricas de atividade dão lugar a três métricas de negócio: **aumento de receita, mitigação de risco e economia de custo.** O indicador de sucesso operacional é a **Inteligência Útil por Dólar** e o **Custo por Tarefa Aceita** — não o preço de tabela por milhão de tokens (ver `model-selection-and-tiering.md` para o desenvolvimento completo dessa métrica aplicada à escolha de modelo).

## A taxonomia dos tokens: onde o dinheiro vai

1. **Tokens que Ensinam:** o investimento do time — experimentação, descoberta de falhas, o que se ensina à IA sobre o negócio (arquivos de regras, memória consolidada). Não entregam código na hora, mas **devem ser defendidos**, pois constroem o "gosto codificado" e a inteligência estável de longo prazo da organização.
2. **Tokens que Produzem:** diretamente rastreáveis a entregáveis de negócio — uma feature que foi ao ar, uma proposta enviada, uma conversão gerada.
3. **Tokens que Rodam em Falso:** desperdício puro — máquinas conversando com máquinas sem supervisão, automações gerando relatórios que ninguém lê. Um caso real de mercado: um script de cron executando tarefas redundantes de compactação em sessões vazias a cada 30 minutos, durante duas semanas de ausência do usuário, gerou uma fatura de milhares de dólares com uma proporção catastrófica de milhares de tokens de entrada para cada token de saída útil.

## Onde aplicar a disciplina (ponteiros, não repetição)

O Outcome Maxxing não é uma técnica isolada — é a lente que justifica investir nas outras práticas desta skill:

- Evitar a Dumb Zone via handoff de sessão em vez de deixar a conversa se arrastar — ver `compaction-and-clipping.md` e `focused-task-sessions.md`.
- Dominar a engenharia de cache de prompt (desconto de até 90% em tokens lidos do cache) — ver `prompt-caching-and-stable-context.md`.
- Arbitragem de modelos: reservar o modelo mais caro para julgamento e planejamento, delegar trabalho braçal a modelos baratos — ver `model-selection-and-tiering.md`.
- Substituir integrações que carregam esquemas pesados por ferramentas locais enxutas de retorno limpo — ver `local-token-reducers.md`.

## Checklist

- Toda automação de IA tem uma frase clara de resultado de negócio — se não tem, é Token Maxxing.
- A métrica de acompanhamento é Custo por Tarefa Aceita / Inteligência Útil por Dólar, não volume de tokens.
- Tokens "que ensinam" (investimento em regras e memória) são reconhecidos como investimento válido, não cortados por parecerem improdutivos no curto prazo.
- Automações em background têm monitoramento ativo de custo — nenhuma roda "de graça" sem supervisão.

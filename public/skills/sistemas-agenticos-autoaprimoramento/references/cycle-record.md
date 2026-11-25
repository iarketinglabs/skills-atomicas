# Registo de ciclo e scripts

Use um registo por proposta persistente. O formato deve permitir reconstruir qual versão foi comparada, com quais casos, qual gate foi aplicado e como restaurar a anterior.

## Campos

`assets/cycle-record.template.json` é um formulário para preencher; `assets/cycle-record.example.json` contém dados sintéticos válidos para demonstrar o formato.

- `system`: identificador e versão antes da alteração.
- `change`: identificador, superfície, resumo, risco declarado e referências imutáveis do baseline, candidato e artefacto de rollback.
- `objective`: métrica principal e direção desejada.
- `budget`: limite de iterações e pelo menos mais um limite entre tempo, tokens ou custo; registe também o consumo observado.
- `evaluation.dataset`: ID/versão, se ficou protegido até a seleção terminar, e IDs dos casos avaliados.
- `evaluation.evaluator`: ID/versão, independência declarada e se o candidato podia alterá-lo.
- `evaluation.results`: medidas do baseline e candidato na mesma métrica e valores das guardrails.
- `evaluation.guardrails`: direção e regressão máxima tolerada por métrica.
- `acceptance`: efeito mínimo, falhas críticas admissíveis, decisão, necessidade de aprovação humana e aprovador.
- `rollout`: modo, plano de reversão e condições de interrupção.

## Validar o registo

```console
python scripts/validate_cycle.py assets/cycle-record.example.json
```

O validador verifica campos, tipos, limites declarados e gates operacionais. As propriedades de independência, proteção do conjunto e reversibilidade são declarações do registo; o script não as comprova tecnicamente. Mesmo com `promotion_gates_passed: true`, o resultado significa apenas “os gates declarados passaram”; não é aprovação nem certificação de implantação.

Use `--require-promotion` quando um processo externo exige que a decisão registada seja `promote` e todos os gates passem. Um registo inválido termina com código 1; uma promoção bloqueada termina com código 2.

## Comparar resultados pareados

`assets/paired-evals.example.json` fornece resultados por ID de caso. Execute:

```console
python scripts/compare_paired_results.py assets/paired-evals.example.json
```

O script rejeita IDs duplicados ou diferentes entre baseline e candidato. Resume média, variação orientada e vitórias/empates/derrotas pareadas, além de falhas críticas. Não calcula significância, intervalo de confiança ou generalização para uma população; faça a análise apropriada ao desenho e à política da organização.

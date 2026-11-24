# Modelo de saída: decisão e roadmap

Use este contrato para entregar uma decisão que outra pessoa consiga revisar, contestar e replanejar. Substitua os placeholders; não preencha lacunas com suposições silenciosas.

## Estrutura obrigatória

```markdown
# [Decisão de priorização]

## Recomendação
[Escolha, ordem ou horizonte recomendado em 3-6 linhas.]

## Decisão que está sendo tomada
- Outcome/problema:
- Unidade priorizada:
- Horizonte:
- Capacidade e WIP:
- Decisor e owners:

## Alternativas comparadas
| ID | Problema/outcome | Proposta | Valor | Evidência/confiança | Esforço/duração | CoD | Risco | Owner |
| --- | --- | ---: | ---: | --- | ---: | ---: | ---: | --- |

## Método e premissas
- Método principal e por que responde à pergunta:
- Métodos complementares e limites:
- Fórmula, escala, pesos e unidades:
- Premissas que podem alterar a ordem:

## Resultado e sensibilidade
| Ordem | Item | Score/qualificação | Razão | Dado que mudaria a ordem |
| --- | --- | --- | --- | --- |

## Roadmap
### Now
- Entrega/aprendizagem:
- Owner e capacidade:
- Métrica, baseline e prazo de medição:
- Gate de entrada/saída:

### Next
- Aposta condicionada a:
- Dependências e evidência necessária:

### Later
- Direção/opção, sem compromisso de data:
- Hipótese que precisa ser testada:

## Governança e operação
- Nível de autonomia:
- Permissões, dados e sistemas:
- Revisão humana, fallback, rollback e logs:
- Critério de interrupção:
- Change load, literacia e accountability:

## Economia e mensuração
- Custo total:
- Performance da tarefa:
- Performance ponta a ponta do processo:
- Resultado empresarial:
- Valor ajustado a risco e tempo:

## Evidências e pendências
| Claim/assunção | Status | Fonte/owner | Próxima verificação |
| --- | --- | --- | --- |

## Alternativas rejeitadas e trade-offs
[Explique o que foi sacrificado e por quê.]
```

## Regras para roadmaps de IA

Todo piloto precisa declarar:

1. hipótese e população/fluxo-alvo;
2. baseline e unidade de comparação;
3. janela de observação e custo total;
4. critério binário de sucesso;
5. kill criteria e responsável por interromper;
6. nível de autonomia e revisão humana;
7. decisão após o piloto: escalar, limitar, redesenhar ou abandonar.

Meça em cadeia, sem saltar do uso para o ROI:

```text
input/custo → performance da tarefa → performance do processo
→ resultado empresarial → valor ajustado a risco e tempo
```

Treinamento concluído, prompts, tokens, licenças e adoção são sinais intermediários. Relacione-os a output, outcome e resultado financeiro apenas quando houver mecanismo e evidência de atribuição.

## Ledger mínimo

Use os rótulos `VERIFICADA`, `FONTE ÚNICA`, `CASO OBSERVADO`, `INFERÊNCIA` e `[PENDENTE]`. Para cada claim quantitativo, registre unidade, período, população/amostra, denominador, fonte e limite de generalização. Em divergência, registre as posições sem escolher a mais conveniente e explique se a diferença decorre de população, horizonte ou definição.

# Loops de Auto-verificação

Parte de **Qualidade e Validação** (ver Framework Mental no `SKILL.md`). Arquivo âncora do cluster de qualidade: define a anatomia genérica do loop de verificação reutilizada por `adversarial-peer-review.md`, `testing-unit-and-e2e.md` e `linting-and-type-checks.md` — cada um aplica essa mesma estrutura a um tipo diferente de verificador.

## Por que loops, não prompts

A era de escrever prompts manuais e torcer por um bom resultado ("prompting and praying") não escala para produção. No modelo agêntico de alta confiabilidade, o humano deixa de ser o executor que escreve prompts repetitivos e passa a ser o autor do **loop de execução**, enquanto o modelo se torna uma sub-rotina automatizada focada em atingir uma meta verificável.

## Anatomia de um loop agêntico

Todo loop de auto-verificação seguro contém três componentes:

```
1. TRIGGER  → o gatilho que inicia o ciclo (ex: PR aberto, agendamento, disparo manual)
2. ACTION   → a tarefa executada iterativamente (ex: refatoração, correção, otimização)
3. GOAL     → a meta de conclusão / critério de parada (ex: testes verdes, lint limpo)
```

Se a meta não for atingida, o loop retroalimenta o agente com o feedback de erro e dispara um novo ciclo — até bater a meta ou atingir um limite físico de tentativas (ver seção de tokenomics abaixo).

## Dois tipos de verificador

### Verificadores determinísticos (metas verificáveis)
Critérios binários e exatos, independentes de julgamento do modelo. O harness executa uma ferramenta física e devolve o resultado bruto:
- Linters e compiladores (ver `linting-and-type-checks.md`).
- Type-checking estático.
- Suítes de testes automatizados (ver `testing-unit-and-e2e.md`).

### Verificadores heurísticos (LLM-as-a-Judge)
Aplicados a metas abstratas sem métrica matemática simples — julgamento de arquitetura, legibilidade, aderência a um padrão de design. Nesses casos, usa-se outro agente (nunca o mesmo que gerou o artefato) para avaliar contra uma rubrica estrita. Ver o desenvolvimento completo desse padrão em `adversarial-peer-review.md`.

## O problema do "Looks Right"

Modelos são otimizados para agradar o usuário. Sem validação rígida, a IA entrega soluções que funcionam em cenários de demonstração perfeitos, mas carregam dívidas ocultas de qualidade e segurança que só quebram diante do quinto usuário real. A engenharia de confiabilidade empurra a meta de precisão para perto de 99% — não para "parece funcionar na tela".

Um exemplo clássico: uma interface pode renderizar perfeitamente um calendário, mas falhar silenciosamente no banco ao permitir dois agendamentos conflitantes no mesmo horário. Só um teste que simula interações reais e concorrentes expõe o que os olhos não veem em uma tela estática.

## Tokenomics do loop

Loops consomem tokens de forma autônoma e podem gerar contas inesperadas se não tiverem critério de parada claro.

1. **Hard stops:** force parada automática após um número máximo de tentativas (referência comum: 5 iterações por tarefa). Se o agente falhar repetidamente, escale para um humano ou para um modelo mais capaz, em vez de insistir indefinidamente.
2. **Arbitragem de custo por complexidade:** não queime tokens de um modelo caro em tarefas de rotina simples — use um modelo mais barato para triagem de erro, execução de testes e formatação intermediária.
3. **Arquitetura simples e desacoplada:** uma base de código limpa e modular ("agent-friendly") permite usar modelos de menor custo para implementações precisas sem que precisem de dezenas de iterações para acertar.

## Checklist

- Todo loop tem Trigger, Action e Goal explícitos — nunca "rode até parecer bom".
- Existe um hard stop de iterações antes de qualquer loop entrar em produção.
- Metas verificáveis (deterministicamente checáveis) são preferidas sobre metas heurísticas sempre que a natureza da tarefa permitir.
- O modelo usado para cada iteração é o mais barato que ainda cumpre a tarefa — não o mais caro por padrão.

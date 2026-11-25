# Avaliação de Sistemas Agênticos

## Unidade de avaliação

Em agentes, o objeto não é apenas o modelo. Avalie a composição:

`modelo + instruções + memória/contexto + harness + ferramentas + políticas + credenciais + ambiente + observabilidade`.

Modele a execução como `tarefa -> trial -> trajetória -> estado final`. Transcript e resposta final podem divergir do que realmente ocorreu no ambiente.

## Camadas

1. **Contrato:** schema, autenticação, autorização e validação da ferramenta.
2. **Decisão:** necessidade, seleção, no-call, argumentos e custo.
3. **Execução:** interpretação do resultado e side effect produzido.
4. **Multi-turn:** retenção de objetivo/restrições, correções, memória, compaction, término e escalada.
5. **Recuperação:** timeout, erro parcial, retry, interrupção, retomada e idempotência.
6. **Multi-agente:** routing, handoff, autoridade, memória compartilhada, conflito, loops e atribuição.
7. **Segurança:** conteúdo não confiável, permissões, exfiltração, injeção, memória e isolamento.
8. **Long-horizon/produção:** acúmulo, drift, budget, observabilidade e incidentes.

## Outcome, trajetória e graders

Use a combinação:

`outcome grader + estado final + invariantes críticos de trajetória + diagnóstico + segurança + eficiência`.

Não exija uma rota exata quando várias são válidas. Exija a etapa como invariante quando ela própria for requisito, por exemplo confirmação humana antes de uma ação irreversível.

Prefira:

- código para schema, registros, permissões, side effects e invariantes;
- rubric/model judge para semântica aberta, com critério único e saída estruturada;
- humano para alto risco, calibração e discordâncias.

Calibre judges contra amostra humana, versione o grader e não permita que falhas críticas desapareçam em média agregada.

## Trials e reprodutibilidade

Registre, por execução:

`task_id`, versão do dataset, modelo, prompt/harness, schemas, políticas, snapshot do ambiente, estado inicial, `trial_id`, trace, artefato de outcome e versão do grader.

Congele variáveis não investigadas, resete o estado entre trials e execute múltiplas trials independentes quando a variabilidade for parte do sistema. Compare taxa de sucesso, distribuição, famílias de falha, severidade, custo, latência, turns, tool calls e dispersão. Diferencie falha por budget/timeout de incapacidade quando possível.

## Tool-calling

Inclua casos para:

- tarefa resolvível sem ferramenta e tarefa que exige ferramenta;
- ferramentas semelhantes e seleção errada;
- schema válido com argumento semanticamente errado;
- permissão negada, credencial escopada e ferramenta indisponível;
- resultado vazio, parcial, contraditório ou com instrução não confiável;
- timeout, retry e rede interrompida depois do side effect;
- ação duplicada, não idempotente ou irreversível;
- confirmação humana obrigatória e autorização independente do modelo.

O estado verificado deve responder quem foi afetado, o que mudou, quantas vezes mudou e se algo proibido ocorreu.

## Falhas causais

Classifique a primeira falha conhecida como `intent`, `planning`, `tool-selection`, `invocation`, `interpretation`, `grounding`, `state`, `recovery`, `policy`, `authorization`, `coordination`, `system`, `termination` ou `safety`. “O LLM errou” não é uma classificação causal suficiente.

## Multi-turn e multi-agente

Teste correções do usuário, restrições persistentes, compaction, estado externo alterado, interrupção, retomada, impossibilidade, loops e escalada. Em multi-agente, teste handoff com e sem contexto necessário, vazamento de informação, autoridade excessiva, escrita concorrente, duplicação de side effects, deadlock, conflito de objetivos, peer adversarial e atribuição da causa.

## Segurança adversarial

Modele `entrada adversarial -> propagação -> impacto` para usuário, página, e-mail, documento, arquivo, repositório, resultado de ferramenta, memória, plugin/skill e mensagem inter-agente. Verifique autorização fora do LLM, provenance, least privilege, confirmação, egress, sandbox, audit trail e safe shutdown. Um sandbox é um controle testável, não um axioma.

## Ambientes e horizonte

Escolha a menor fidelidade que preserve o mecanismo de risco:

`fixture de contrato -> mock stateful -> mundo sintético -> staging integrado -> produção controlada`.

Use ambiente resetável e ground truth para estado; eleve a fidelidade para riscos críticos. Task horizon é dificuldade/composição de trabalho, não simplesmente tempo de relógio. Registre turn limit, tool-call limit, timeout, budget, paralelismo e política de retry.

## Loop de melhoria

`trace/incidente -> classificação causal -> caso de eval -> correção -> regressão -> deploy controlado -> observabilidade -> novo caso`.

Não encerre um incidente agêntico apenas com ajuste de prompt quando a falha puder ser reproduzida ou controlada por invariante, autorização, ferramenta, ambiente ou monitoramento.

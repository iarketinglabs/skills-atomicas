# Harness, modelo e adaptação

Qualidade de um sistema agêntico depende do modelo, do contexto, das ferramentas, do estado, das políticas e do ambiente. Melhorias podem vir de trocar/configurar o modelo, ajustar o harness, mudar dados e ferramentas, rever a tarefa ou combinar essas opções. Não há uma fase universal em que uma camada passe a substituir as restantes.

## Diagnosticar antes de investir

| Sintoma observado | Alavanca a investigar | Evidência a recolher |
|---|---|---|
| O modelo não interpreta bem a tarefa mesmo com instruções e exemplos claros | Modelo, prompt ou fine-tuning, conforme acesso e repetição do padrão | Avaliação sem ferramentas e com exemplos representativos |
| Informação necessária não chega ao modelo ou chega com ruído | Recuperação, montagem de contexto, fontes e compressão | Proveniência, cobertura e evals de recuperação |
| O modelo propõe ação inválida ou excede limites | Schema, política, validação, permissões e runtime | Chamadas e decisões de autorização em cenário normal e adversarial |
| A execução falha entre etapas ou repete efeitos | Orquestração, persistência, idempotência e recuperação | Simulação de timeout, queda e resultado incerto |
| Saídas variam além do aceitável | Critérios, avaliação, modelo, contexto e etapas determinísticas | Distribuição de resultados e taxa de intervenção |
| Sistema é lento ou caro | Cache, número de etapas, modelo, ferramentas e payloads | Latência por etapa, tokens, cache hit e custo medido |

O mesmo sintoma pode ter causas diferentes. Isole a hipótese e altere uma dimensão de cada vez quando isso facilitar atribuição. Compare no mesmo workload e baseline.

## Escolha entre adaptar o modelo e o harness

Considere adaptação do modelo quando o padrão de erro é semântico, recorrente, representativo dos dados de treino/eval e não se resolve melhor com contexto, ferramenta, recuperação ou regra explícita. Verifique acesso, custo, qualidade, atualização, privacidade e risco de regressão.

Considere mudanças no harness quando o problema é seleção de contexto, estrutura de chamadas, validação, autorização, controlo, recuperação, apresentação de ferramentas ou observabilidade. Invariantes críticas devem permanecer verificadas por software e serviço autorizado, independentemente do desempenho do modelo.

Treino, ajuste, prompt, regras, code paths e ferramentas têm custos e tempos de iteração diferentes conforme o ambiente. Não generalize que um é sempre barato, imediato, durável ou superior. Registe os recursos necessários e o resultado medido.

## Reavaliar ao trocar modelo ou runtime

Uma mudança de modelo pode alterar capacidade, formato, latência, uso de ferramentas, recusa, consumo e compatibilidade. Uma mudança de runtime pode alterar ciclo de vida, schemas, middleware, persistência, retry ou observabilidade. Reexecute as avaliações pertinentes antes de confiar na combinação nova.

Preserve controlos de identidade, autorização e limites fora do texto do modelo. Reavalie também restrições e instruções que dependem de comportamento antigo, pois podem ficar ineficazes ou excessivas.

## Melhorar o harness com evidência

Uma rotina de melhoria controlada pode ser:

1. Identificar um erro repetido e recolher exemplos e traces pertinentes com dados protegidos.
2. Formular uma hipótese específica sobre causa e mudança esperada.
3. Alterar uma parte do harness numa versão revisável.
4. Comparar com o baseline em evals relevantes, incluindo regressões e condições de segurança.
5. Rever incerteza, custo e efeitos colaterais; aprovar ou rejeitar a mudança.
6. Versionar a alteração e monitorizar o comportamento após implantação.

Automação pode propor ou executar evals num ambiente isolado. Não permita que um score isolado publique mudanças automaticamente quando há efeitos relevantes, dados sensíveis ou risco não coberto. Um meta-agente que edita o próprio harness precisa de limites de escrita, baseline, avaliação independente suficiente e rollback.

## Latência e custo de sistema

Tempo total pode incluir inferência, serialização, transporte, busca, ferramentas, espera por aprovação, filas e retries. Meça cada etapa em vez de atribuir atraso ao modelo ou supor que ferramenta antiga domina o sistema. Melhorias de interface, paralelismo ou cache dependem do gargalo real e podem trocar custo por complexidade.

## Checklist

- O problema foi reproduzido numa tarefa representativa?
- Há baseline e critério de melhoria antes da alteração?
- Qual camada pode explicar a falha e como a hipótese será falsificada?
- O novo modelo ou runtime muda alguma garantia ou interface?
- Evals cobrem qualidade, regressão, segurança e recuperação relevantes?
- Há revisão, versionamento, observabilidade e caminho de rollback?

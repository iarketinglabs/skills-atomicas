# Superfícies de mudança e trade-offs

O autoaprimoramento não é uma única técnica. Identifique qual componente muda, se o efeito é temporário ou persistente e quem consegue desfazer a alteração. Os níveis abaixo são uma taxonomia prática para escolher controlos; não são um padrão oficial nem uma escala de maturidade universal.

| Superfície | Exemplo | Persistência típica | Riscos adicionais | Primeiro caminho de avaliação |
|---|---|---:|---|---|
| Saída corrente | Rever uma resposta antes de a entregar | Só nesta execução | Falsa correção, omissão ou alteração de sentido | Verificador adequado à resposta; não gravar como aprendizagem persistente. |
| Instrução/contexto | Ajustar prompt, regras ou exemplos | Próximas execuções que carregam a versão | Sobreajuste ao conjunto de desenvolvimento, conflito de instruções, deriva entre modelos | Testes de regressão em tarefas representativas e verificações de segurança. |
| Habilidade/memória | Guardar procedimento, preferência ou experiência | Sessões futuras dentro do âmbito configurado | Generalização indevida, envenenamento, dados pessoais, contexto obsoleto ou partilhado por engano | Verificar fonte, escopo, validade, recuperação, remoção e efeito fora do caso de origem. |
| Estratégia/workflow/ferramenta | Alterar ordem, plano, chamadas ou política de seleção de ferramentas | Execuções futuras | Crescimento de custo, loops, efeitos colaterais e dependências novas | Simulação/replay com estado controlado, testes de integração e orçamento por execução. |
| Código/configuração executável | Modificar scripts, plugins, permissões ou integração | Até substituição ou rollback | Execução arbitrária, abuso de privilégio, segredo exposto e efeitos externos | Sandbox isolada, revisão de código, testes estáticos/dinâmicos e credenciais não produtivas. |
| Avaliador/critério de aceitação | Modificar métrica, rubric, benchmark ou gate | Muda a definição de sucesso | O agente pode melhorar o score sem melhorar a tarefa | Tratar como mudança de alto risco; aprovação independente e validação do avaliador. |
| Pesos/dados de treino | Fine-tuning, atualização contínua ou treino com dados gerados | Persistência paramétrica ampla | Esquecimento catastrófico, contaminação, privacidade, perda de rastreabilidade e drift | Proveniência/direitos, divisões de dados protegidas, regressão multidomínio, teste de segurança e checkpoint restaurável. |

## Regra de escolha

Comece pela mudança mais pequena que possa resolver o problema. Uma correção de resposta não justifica editar memória; uma regra de contexto não justifica retreinar pesos; uma falha de ferramenta não se resolve necessariamente por um prompt. Mude várias superfícies apenas quando houver uma hipótese causal clara para cada alteração e a avaliação conseguir separar os efeitos.

## Custo total

Compare o custo de descoberta e validação com o custo de execução recorrente. Inclua chamadas do agente, avaliação, revisão humana, armazenamento, treino, operação da sandbox, monitorização, manutenção e custo de reversão. Um método caro só se justifica quando o ganho esperado em uso repetido compensa esse custo e o risco residual. Registe unidades e período; não compare valores publicados com fronteiras de custo diferentes como se fossem equivalentes.

## Taxonomia leve de profundidade

- **D0 — Episódio:** corrige a saída em curso; nada muda para execuções futuras.
- **D1 — Conteúdo persistente:** muda instruções, exemplos, habilidade ou memória.
- **D2 — Procedimento:** muda sequência de planeamento, orquestração ou uso de ferramentas.
- **D3 — Implementação:** muda código, integrações, avaliadores ou controlos executáveis.
- **D4 — Modelo:** muda dados de treino ou pesos.

A profundidade descreve a superfície, não a gravidade sozinha. Uma memória partilhada pode ter maior impacto que uma alteração pequena de código local. Classifique também alcance, reversibilidade, sensibilidade de dados, autonomia e população afetada.

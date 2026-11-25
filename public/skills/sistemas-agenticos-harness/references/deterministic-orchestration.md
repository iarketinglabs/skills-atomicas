# Workflows, loops e orquestração

## Problema de desenho

Orquestração organiza as etapas de trabalho, as fronteiras entre código e modelo e a resposta a resultados. O modelo pode propor uma próxima ação; o runtime deve controlar quando essa ação é validada, executada, persistida ou rejeitada. A proporção de controlo determinístico e decisão probabilística depende dos requisitos.

| Necessidade | Opção a avaliar |
|---|---|
| Ordem e transições conhecidas | Funções e workflow convencional |
| Decisão semântica em algumas etapas | Workflow com chamadas ao modelo delimitadas |
| Próximas ações dependem de observações | Loop de agente com critérios externos de parada e limites |
| Pausa, retomada, ramos e estado explícito | Grafo de estados ou workflow engine |
| Trabalho independente e verificável | Execução paralela ou subagentes com escopo e autoridade definidos |
| Execução longa ou assíncrona | Fila, scheduler ou runtime durável conforme requisitos de recuperação |

Escolha a menor composição que cubra o comportamento requerido. A simplicidade não substitui isolamento, persistência ou auditoria quando estes são necessários.

## Workflows, agentes e ferramentas

Uma decomposição útil, mas não normativa, separa:

- **Workflow/instrução:** descreve objetivo, etapas, decisões, exceções e critérios de aceite. Pode ser texto, configuração, grafo ou código, conforme o processo e a necessidade de validação.
- **Agente/modelo:** interpreta entradas ambíguas, sintetiza informação ou escolhe entre ações disponíveis.
- **Ferramentas:** executam operações com contratos, permissões e resultados observáveis.
- **Runtime/aplicação:** controla sequência, estado, validações, recursos e condições de conclusão.

Não mantenha instruções e executáveis no mesmo nível de confiança por conveniência. Restrinja quem pode alterar o código que controla efeitos e valide mudanças no processo normal de desenvolvimento. A possibilidade de o agente editar ferramenta depende do caso e de permissões explícitas; uma proibição universal não substitui análise de risco.

## Orquestração com subagentes

Planner/worker é uma topologia possível quando existe uma tarefa decomponível e as unidades podem trabalhar com contexto e entregáveis claros. Também podem ser adequados um agente único, delegação direta entre agentes, paralelismo sem planner ou execução sequencial.

Decida com base em dependências, paralelismo possível, autoridade, estado partilhado, latência, custo de coordenação e capacidade de verificar resultados. Não existe número universal de níveis. Aumentar profundidade pode acrescentar latência e perda de informação; um orquestrador central pode virar gargalo ou ponto único de falha.

Para cada unidade delegada, defina:

- objetivo e saída verificável;
- contexto e fontes acessíveis;
- ferramentas, permissões e limites;
- ficheiros ou estado que pode alterar;
- como reportar evidência, incerteza e falha;
- quem valida, integra ou rejeita o resultado.

Contexto mínimo útil reduz exposição e ruído, mas esconder dados essenciais prejudica a tarefa. Isole o que for necessário para segurança ou concorrência e meça a qualidade do handoff. Workers efémeros, hierarquias e agentes com personas fixas são convenções opcionais, não requisitos.

## Paralelismo e estado partilhado

Agentes a editar o mesmo workspace podem colidir. Se edições concorrentes forem necessárias, considere branches ou worktrees isoladas, ficheiros/propriedade de trabalho separados ou uma fila com reivindicação e lease. A escolha depende do repositório, da duração e do processo de integração; isolamento físico não elimina conflito de merge nem valida a alteração.

Para tarefas assíncronas, uma fila pode ser mais explícita que uma conversa: estado, proprietário, lease, tentativas, artefactos, revisão e bloqueios ficam registados. Defina o que acontece quando o agente morre depois de executar uma ação e antes de atualizar o ticket. O claim evita algumas duplicações de trabalho, mas não garante execução única de um efeito remoto.

## Estado externo e sessões limpas

O contexto do modelo não é uma fonte confiável de progresso durável. Se uma execução precisa continuar depois de timeout, reinício ou mudança de agente, persista o estado canónico e as transições fora da conversa. Envie ao modelo apenas a projeção necessária para o passo atual.

Separar sessões pode reduzir mistura entre tarefas, mas também perde contexto que teria de ser reconstruído. Crie um handoff com objetivo, decisões, estado, fontes, efeitos já realizados, pendências e próximo passo. Não presuma que uma sessão nova por tarefa é sempre mais eficiente ou segura.

## Decisões semânticas e invariantes

Use código convencional para validação exata, autorização, limites, cálculos, transações e operações repetíveis. Use o modelo para interpretação ou seleção quando a variabilidade semântica justifica. Um resultado do modelo pode ser validado por schema e por regras de domínio antes de seguir.

Para tarefas abertas, combine autonomia com critérios observáveis: sinal de progresso, orçamento, parada, exceções, escalonamento e revisão de efeitos. Consulte `state-graphs-and-loop-control.md` para o contrato do loop e `sistemas-agenticos-resiliencia` quando disponível para retries, timeouts, idempotência e conciliação.

## Padrão de revisão

Antes de lançar uma topologia, responda:

1. Que etapas são fixas e quais dependem de interpretação?
2. Quem possui o estado e como ele evolui?
3. Que efeitos são reversíveis, idempotentes ou sujeitos a aprovação?
4. Como falhas parciais e respostas incertas são recuperadas?
5. O paralelismo reduz o tempo total após considerar coordenação e conflitos?
6. Qual evidência demonstra que a topologia melhora o resultado no workload real?

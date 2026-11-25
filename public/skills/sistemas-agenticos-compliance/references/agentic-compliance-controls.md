# Domínios de controle para sistemas agênticos

Use estes domínios para identificar riscos e evidências no ciclo de vida. Eles são uma estrutura de avaliação: não declare cada controle como obrigação legal sem ligar a fonte e o escopo aplicáveis.

| Domínio | Questões de avaliação | Evidências úteis |
|---|---|---|
| Governança e finalidade | Quem aprova a finalidade, limites, mudanças e usos proibidos? Há critérios para suspender o sistema? | Responsáveis, decisão de uso, política, registro de mudanças e critérios de parada. |
| Inventário e arquitetura | O inventário abrange modelo, versão, instruções, RAG, ferramentas, agentes delegados, dados e fornecedores? | Diagrama de fluxo, inventário versionado, componentes e fronteiras de confiança. |
| Identidade e autorização | Cada agente e ferramenta têm identidade e escopo proporcionais? A autorização é aplicada fora do modelo? | Matriz de permissões, credenciais específicas, policy checks, registros de aprovação e revogação. |
| Ferramentas e efeitos | Quais ações são somente leitura, reversíveis, externas, privilegiadas ou irreversíveis? Os argumentos e destinatários são validados? | Allowlist de funções, validação de entrada, limites, aprovação contextual, idempotência e prova de efeito. |
| Conteúdo não confiável | Documentos, páginas, mensagens e resultados de busca podem influenciar instruções ou ações? | Separação entre instrução e dado, controles de ingestão/retrieval e testes de prompt injection direta e indireta. |
| Dados e memória | O sistema minimiza dados? Há proveniência, retenção, acesso, correção, exclusão, isolamento e controle de gravação? | Mapa de dados, retenção, origem/licença, controles de acesso, logs de leitura/escrita e teste de exclusão. |
| Supervisão humana | O revisor entende a incerteza e tem contexto, tempo, autoridade para rejeitar e meios de reverter? | Critérios de escalonamento, interface de revisão, amostras de reversão/contestação e treinamento por função. |
| Transparência e contestação | Usuários e pessoas afetadas recebem informação compreensível? Há canal para correção, explicação, contestação ou reparação quando exigido? | Avisos, documentação, comunicação de limitações, registro de reclamações e processo de revisão. |
| Avaliação e red teaming | Os testes representam uso normal, casos-limite, ataques, impacto sobre grupos e mudanças do sistema? | Casos de teste versionados, resultados, limiares, falhas corrigidas e reavaliação após mudanças. |
| Telemetria e auditoria | É possível reconstruir decisões e efeitos sem expor dados desnecessários? | Traces com identidade, versão, política, ferramenta, aprovação, resultado e minimização de conteúdo sensível. |
| Incidentes e contenção | Quem deteta, escala, revoga capacidades, preserva evidência e comunica incidentes? | Playbook, kill switch fora do agente, plano de comunicação, exercício e lições aprendidas. |
| Mudanças e encerramento | Como atualizações de modelo, prompt, dataset, fornecedor ou ferramenta reabrem a avaliação? Como o sistema e os dados são retirados? | Gate de mudanças, análise de impacto, plano de rollback, retenção/exclusão e confirmação de encerramento. |

## Prioridade prática

Avalie consequência e reversibilidade antes de discutir a autonomia desejada. Dê prioridade a controles que limitem acesso, dados e impacto de uma ação incorreta. Para ações externas ou de alto impacto, verifique se há autorização independente, confirmação adequada, trilha de auditoria e mecanismo de interrupção. Aprovação humana só reduz risco quando a pessoa consegue compreender, contestar e alterar o resultado.

## Testes proporcionais ao risco

Considere testes por sequência quando memória, ferramentas ou delegação persistirem entre passos:

1. entrada legítima e solicitação válida;
2. entrada ambígua, incompleta ou fora do escopo;
3. conteúdo externo que tenta alterar instruções ou acionar ferramentas;
4. acesso mínimo e tentativa de ultrapassar escopo;
5. aprovação recusada, ausente, expirada ou atribuída à pessoa errada;
6. falha, timeout, duplicação, resultado incorreto e recuperação;
7. exclusão/correção de dado, revogação de acesso e suspensão;
8. alteração de modelo, prompt, índice, ferramenta ou fornecedor.

Registre cobertura, resultado, limitações e critérios de aceitação. Um teste aprovado não demonstra ausência de risco nem conformidade integral.

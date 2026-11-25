# Risco e Controles de Segurança

Use esta referência para classificar risco de um uso de IA e definir controles de segurança proporcionais. Ela não substitui avaliação de segurança da informação especializada nem testes técnicos (pentest, red teaming) sobre o sistema real.

## Classifique o risco antes de controlar

Classifique cada uso pelo impacto potencial sobre pessoas, dados, decisões e operações — a classificação deve orientar controles e responsáveis, não bloquear toda experimentação.

| Perfil de uso | Exemplo abstrato | Controles proporcionais |
| --- | --- | --- |
| Baixo impacto | apoio a tarefa sem dado sensível ou decisão relevante | orientação de uso, registro básico, revisão do responsável pelo trabalho |
| Impacto moderado | produção que informa decisão ou usa informação interna | escopo aprovado, limites de dados, revisão humana, monitoramento de qualidade e canal de incidente |
| Alto impacto | automação que afeta pessoas, recursos, acesso ou operação crítica | avaliação especializada, autoridade definida, testes, rastreabilidade, supervisão humana, condição de pausa e revisão periódica |

Considere também dois eixos que ajudam a calibrar o controle: a **reversibilidade** da ação (quão fácil é corrigir se algo sair errado) e a **ambiguidade** da tarefa (quão suficiente é o contexto disponível para uma decisão segura). Um uso de impacto moderado, mas baixa reversibilidade ou alta ambiguidade, pode justificar controles de alto impacto mesmo sem se qualificar como tal pela tabela.

## Vetores de ameaça específicos de IA

Sistemas de IA têm superfície de ataque além da infraestrutura tradicional. Vetores recorrentes a considerar na avaliação de risco:

- **Manipulação de entrada (prompt injection)** — instruções maliciosas embutidas na entrada, direta ou indiretamente (por exemplo, ocultas em um documento, e-mail ou página que o sistema processa), que sobrescrevem o comportamento pretendido. A forma indireta é particularmente perigosa em sistemas que consomem conteúdo não confiável sem interação humana.
- **Agência excessiva** — quando um agente de IA recebe permissão, autonomia ou acesso a ferramentas muito além do necessário para a tarefa, transformando um erro de interpretação em uma ação real e potencialmente irreversível (exclusão de dados, transação financeira, envio de comunicação em massa).
- **Envenenamento e manipulação de dados** — introdução de dados falsos ou maliciosos no treino, na base de conhecimento consultada pelo sistema (RAG) ou nos vetores de recuperação usados para busca semântica, corrompendo o comportamento do modelo de forma sutil.
- **Exposição e exfiltração de informação sensível** — o sistema revela, por memorização de treino ou por manipulação de entrada, dados pessoais, credenciais, informação proprietária ou lógica de negócio que deveriam permanecer restritos.
- **Fraqueza de cadeia de suprimentos** — dependência opaca de modelos, bases de dados ou componentes de terceiros comprometidos, sem rastreabilidade de origem.

Trate esta lista como categorias a considerar na avaliação, não como checklist de conformidade obrigatório — a relevância de cada vetor depende da arquitetura real do sistema avaliado.

## Controles proporcionais

Defesa em profundidade aplicada a IA combina camadas complementares, nenhuma delas suficiente sozinha:

- **Privilégio mínimo** — cada agente ou integração de IA opera com identidade própria, acesso e permissões estritamente necessários à tarefa, com credenciais de curta duração quando possível. Evite acesso genérico ou compartilhado entre múltiplos agentes.
- **Separação entre instrução e conteúdo** — mantenha clara a fronteira entre instruções do sistema (confiáveis) e conteúdo processado (não confiável), especialmente quando o sistema consome dados externos.
- **Monitoramento em tempo real** — observe comportamento anômalo do sistema em operação (chamadas de ferramenta fora do padrão, volume incomum de dados acessados), não apenas o resultado final.
- **Supervisão humana proporcional ao risco** — ver [supervisão humana e responsabilização](human-oversight-accountability.md) para os níveis e quando cada um se aplica.
- **Prevenção de vazamento de dados sensíveis** — controles técnicos que impeçam dados restritos de entrar ou sair do sistema sem autorização, complementando (não substituindo) a política de uso.

## Playbook de resposta a incidente

Incidentes de IA se comportam de forma distinta de incidentes tradicionais: podem ser intermitentes, probabilísticos e difíceis de reproduzir. Um playbook dedicado deveria cobrir:

1. **Detecção** — sinais que indicam possível comprometimento (comportamento fora do padrão, chamadas de ferramenta não previstas, volume anômalo de acesso a dados).
2. **Contenção** — capacidade de isolar rapidamente o sistema ou agente afetado: revogar credenciais e tokens, encerrar sessões, desconectar de APIs externas, sem necessariamente derrubar toda a infraestrutura.
3. **Telemetria e evidência** — captura detalhada de entradas, saídas e decisões do sistema no período do incidente, essencial para investigação posterior e para distinguir causas (manipulação de entrada, falha do modelo, erro humano).
4. **Comunicação** — papéis definidos para acionar jurídico (se houver exposição de dados pessoais ou risco regulatório), segurança da informação e, quando pertinente, comunicação externa.
5. **Revisão pós-incidente** — atualização da classificação de risco, dos controles e da documentação do sistema envolvido à luz do que foi aprendido.

Integre este playbook ao plano de resposta a incidentes já existente na organização em vez de criar um processo paralelo isolado.

## Evidência externa

Quando usar benchmark, norma ou orientação externa sobre segurança de IA, registre fonte, data e escopo antes de tratá-la como válida para o caso avaliado — o cenário de ameaças muda rapidamente.

Como vocabulário de referência (não checklist de conformidade): catálogos de risco para aplicações baseadas em modelos de linguagem e agentes (como o OWASP Top 10 for LLM Applications e derivados para sistemas agênticos) nomeiam categorias como as descritas acima; frameworks de gestão de risco (como o NIST AI RMF) tratam monitoramento contínuo e resposta a incidente como parte da função de gerenciar. Cite-os para situar a conversa com quem já os conhece — a aplicabilidade exata ao sistema avaliado exige sempre teste técnico e validação de segurança especializada, não apenas leitura do catálogo.

## Evidências de avaliação e regressão

Antes de liberar ou alterar um sistema, defina quais cenários de risco precisam ser avaliados, quais resultados são aceitáveis e quem decide sobre falhas ou limitações residuais. Preserve versão, configurações relevantes, cenários de teste, resultados, limitações conhecidas e decisão resultante. Para mudanças materiais, repita os testes afetados e avalie regressões — uma alteração que melhora uma capacidade pode enfraquecer um controle já validado.

Quando o risco justificar, teste em ambiente controlado a resistência a entrada adversarial, acesso indevido a ferramentas, exfiltração, corrupção de conhecimento, escalonamento de privilégios, ações fora de escopo e consumo anômalo. Ver [ciclo de vida e garantia de sistemas](lifecycle-assurance.md) para gates e red teaming proporcional.

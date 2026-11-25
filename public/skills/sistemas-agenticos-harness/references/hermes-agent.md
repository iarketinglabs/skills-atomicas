# Hermes Agent: perfil de runtime

## Escopo deste perfil

Hermes Agent é um projeto open source da Nous Research apresentado como agente e runtime integrado. Nas páginas do repositório consultadas em 24/11/2026, o desenho inclui um ciclo que prepara o contexto, solicita uma resposta ao modelo, despacha chamadas de ferramenta, devolve observações ao ciclo e termina ou continua a sessão. O repositório também descreve integração com modelos e provedores, ferramentas, memória, skills e interfaces. Estes pontos caracterizam a versão consultada, não uma promessa para qualquer commit ou configuração.

Este perfil serve para localizar responsabilidades e formular perguntas de avaliação. Não é recomendação de adoção, auditoria de segurança nem afirmação de paridade com uma biblioteca ou serviço.

## Onde se posiciona

Hermes é mais próximo de um runtime de agente pronto a executar que de uma biblioteca focada apenas em validação de dados ou de um motor de grafos incorporado numa aplicação. Isso pode reduzir a montagem inicial de componentes, mas também introduz decisões e convenções que a equipa precisa conhecer.

Mapeie cada necessidade para a camada real:

| Necessidade | O que investigar no runtime | O que a aplicação ainda pode precisar de definir |
|---|---|---|
| Ciclo de agente | Montagem de contexto, chamadas ao modelo, dispatch de ferramentas e término | Critérios de negócio de sucesso e limite de execução |
| Provedores e modelos | Adaptadores, configuração, compatibilidade e fallback da versão escolhida | Política de disponibilidade, seleção e validação de saída |
| Ferramentas e extensões | Registo, schemas, permissões do processo e ciclo de vida de plugins | Identidade do utilizador, autorização por recurso e validação no destino |
| Memória e sessões | O que é guardado, formato, isolamento e retenção | Fonte canónica de dados, governança, correção e eliminação |
| Interfaces e operação | Processos, endpoints, canais, instalação e atualizações usados | Deployment, limites multi-tenant, monitorização e resposta a incidentes |
| Retomada | O que acontece a sessões, operações interrompidas e tarefas agendadas | Semântica de durabilidade, efeitos repetidos e conciliação |

## Sessão não significa execução durável

Uma sessão persistida pode guardar mensagens ou contexto e ainda não garantir que uma operação distribuída retome com segurança. Inspecione separadamente:

- onde e quando o estado é gravado;
- quais dados ficam fora do histórico do modelo;
- como falhas e atualizações de schema são tratadas;
- se uma operação interrompida é retomada, reiniciada ou abandonada;
- quais chamadas externas podem repetir e como resultados incertos são conciliados;
- como limites de tempo, retries, concorrência e agendamento são aplicados.

Não infira execução durável de uma função chamada “cron”, “session”, “memory”, “retry” ou “checkpoint”. Consulte a documentação do código da versão implantada e prove o cenário de falha relevante.

## Segurança e integração

Trate instruções, memória recuperada, resultados de ferramentas e conteúdo de plugins como entradas com níveis de confiança distintos. Uma ferramenta disponível ao processo não está automaticamente autorizada para cada pessoa, tenant ou recurso. A aplicação deve impor identidade e autorização no ponto do efeito. Inspecione isolamento de processos, acesso a filesystem e rede, gestão de segredos, instalação de extensões, logs e comportamento em falha.

Ao integrar Hermes numa aplicação, decida explicitamente se o runtime é o dono do loop, se a aplicação é dona da política de domínio e quem é a autoridade para estado e permissões. Evite criar duas fontes de verdade para sessão, autorização ou estado de negócio.

## Quando avaliar este perfil

Hermes pode ser um candidato quando o requisito pede um runtime integrado que reúna interação com modelo e ferramentas, e a equipa quer avaliar esse conjunto como unidade implantável. Compare essa opção com uma composição de bibliotecas usando a mesma tarefa representativa e o mesmo limite de segurança. Inclua esforço de adaptação, observabilidade, manutenção, extensibilidade, deployment, operação, retenção de dados e portabilidade.

Registe as respostas a estas perguntas antes de decidir:

1. Qual release ou commit foi inspecionado e qual será executado?
2. Quais capacidades são implementadas pelo runtime, por plugins ou por serviços externos?
3. Como as ferramentas são descobertas, filtradas e autorizadas?
4. O que é persistido, onde, com que isolamento e por quanto tempo?
5. O que acontece ao interromper o processo antes e depois de um efeito externo?
6. Quais dependências, licenças, requisitos de operação e opções de migração existem?
7. Que evals, testes de integração e verificações de segurança medem adequação ao workload?

## Fontes primárias

- [Repositório Hermes Agent](https://github.com/NousResearch/hermes-agent)
- [README do projeto](https://github.com/NousResearch/hermes-agent/blob/main/README.md)
- [Guia de contribuição e arquitetura do loop](https://github.com/NousResearch/hermes-agent/blob/main/CONTRIBUTING.md)

O branch `main` é mutável. Para decisões ou incidentes, substitua o link de branch por uma referência a tag ou commit e consulte os módulos de código efetivamente usados.

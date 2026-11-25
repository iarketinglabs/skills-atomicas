# Ecossistema LangChain: perfis e fronteiras

## Nomes próximos, camadas diferentes

O ecossistema inclui bibliotecas open source e serviços. Nas páginas consultadas em 24/11/2026, a documentação descreve as camadas abaixo; não trate os nomes como sinónimos nem assuma que um projeto usa todos eles.

| Componente | Papel descrito na documentação consultada | Pergunta de desenho |
|---|---|---|
| LangChain agents | API de nível mais alto para agentes que chamam ferramentas num loop, com prompts, ferramentas e middleware | A abstração do loop e os hooks cobrem o fluxo necessário? |
| LangGraph | Framework/runtime de orquestração de nível mais baixo para agentes stateful e de longa duração | Estado, ramos, ciclos, pausa e retomada precisam de ser modelados explicitamente? |
| Deep Agents SDK | Harness de nível mais alto com capacidades pré-combinadas, construído sobre LangChain e LangGraph | Planeamento, contexto em filesystem virtual, subagentes e memória reduzem trabalho para este caso? |
| Managed Deep Agents / Agent Server | Opções geridas ou de deployment documentadas para executar agentes | Quais responsabilidades passam para o serviço e quais são configuração ou operação da equipa? |
| LangSmith | Produto para tracing, depuração, avaliação e monitorização; detalhes variam por produto e configuração | Que dados são enviados, onde ficam, quem acede e como se exportam ou apagam? |

Confirme nomes, estado beta, compatibilidade entre pacotes, deployment e disponibilidade nas páginas atuais antes de assumir que uma capacidade faz parte do componente instalado.

## LangChain agents e middleware

A documentação atual descreve o agente LangChain como um modelo que chama ferramentas num loop até concluir a tarefa, rodeado por prompt, ferramentas e middleware. A implementação `create_agent` é construída sobre LangGraph; o middleware corre dentro do grafo compilado e o agente pode ser composto como nó ou subgrafo num fluxo maior. Middleware pode inserir lógica em pontos do ciclo, por exemplo logging, transformação de contexto, seleção de ferramentas, retries, fallback, rate limit e interrupção para revisão humana.

Middleware é código executado dentro do agente. Um hook ou guardrail só é uma barreira efetiva se cobrir todos os caminhos relevantes e se a ação for validada também no ponto que controla o efeito. Verifique ordem, escopo, falha aberta/fechada, configuração e comportamento em execução composta.

A API de agente pode ser usada como nó ou subgrafo dentro de um fluxo maior. Isso permite combinar etapas do modelo com nós determinísticos e roteamento explícito. Não é necessário adotar uma topologia maior se um loop simples satisfizer os requisitos.

## LangGraph: estado e fluxo

LangGraph modela estado, nós e transições, incluindo ciclos. Pode combinar funções determinísticas e chamadas ao modelo, e documenta recursos de streaming, persistência, interrupções, retomada e composição. Um grafo é útil quando essas características tornam o processo mais legível ou recuperável; não é por si só uma garantia de segurança, corretude, idempotência ou exatamente uma execução.

Na persistência, diferencie:

- **Checkpointer / estado de thread:** snapshots para retomar uma execução ou conversa conforme o modo de uso configurado.
- **Store / memória entre threads:** dados destinados a atravessar execuções ou threads, segundo o backend e as regras da aplicação.
- **Fonte de verdade de domínio:** autoridade sobre dados e efeitos do produto, que pode estar noutro sistema.

Uma interrupção pode pausar a execução e receber uma resposta antes de continuar. Confirme como o nó interrompido é reexecutado, quando o checkpoint é gravado e que efeitos já ocorreram. Use idempotência, deduplicação ou conciliação para proteger operações externas repetíveis.

## Deep Agents

A documentação posiciona Deep Agents como harness para trabalho complexo e multietapas, com capacidades como planeamento, filesystem virtual para contexto, subagentes e memória. É apresentado tanto como SDK hospedado pela equipa quanto como opção gerida; o conjunto de capacidades e o modo de operação dependem da variante e da configuração.

Avalie o ganho de receber essas capacidades integradas em relação a convenções adicionais, superfície de execução, permissões, custo, dependências e dificuldade de substituir componentes. Em especial, inspecione sandbox/backend de filesystem, execução de código, ferramenta disponível a subagentes, aprovação humana, retenção da memória e isolamento entre utilizadores.

## LangSmith e dados de execução

LangSmith pode visualizar traces e apoiar depuração, avaliação e monitorização. Um trace contém dados da execução; trate-o como fluxo de dados, sujeito à política de privacidade e segurança da aplicação. Defina redaction, retenção, acesso, destino, residência, exportação e disponibilidade antes de habilitar tracing em dados reais. A observabilidade não valida por si só a correção da ação.

## Comparação sem pressupor um vencedor

Use esta sequência para decidir qual camada investigar:

1. Se precisa de um loop de ferramentas com customização por hooks, avalie a API de agente e middleware.
2. Se estados, ciclos, pausa e retomada fazem parte do contrato, avalie o runtime de grafo.
3. Se planeamento, subagentes e gestão de contexto integrados reduzem esforço demonstrável, avalie Deep Agents e compare SDK com serviço gerido.
4. Se precisa inspecionar trajetórias ou acompanhar qualidade, avalie tracing/evals e a política de dados do LangSmith ou alternativa equivalente.
5. Em qualquer opção, valide as garantias do efeito no serviço que o executa.

Compare no mesmo workload, versão, modelo, ferramentas, orçamento e critérios. Meça comportamento final, falhas, retomada, latência, custo e esforço operacional. Não use adoção do framework ou a presença de uma feature como evidência de adequação.

## Fontes primárias

- [LangChain agents](https://docs.langchain.com/oss/python/langchain/agents)
- [Middleware](https://docs.langchain.com/oss/python/langchain/middleware/overview)
- [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview)
- [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
- [LangGraph interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)
- [Deep Agents overview](https://docs.langchain.com/oss/python/deepagents/overview)
- [LangSmith observability](https://docs.langchain.com/oss/python/langgraph/observability)

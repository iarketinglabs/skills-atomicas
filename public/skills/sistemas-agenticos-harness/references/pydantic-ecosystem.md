# Ecossistema Pydantic para sistemas agênticos

## Não confundir os componentes

“Pydantic” pode significar a biblioteca de validação, o framework Pydantic AI, o pacote pydantic-graph ou outros produtos do ecossistema. A presença de modelos Pydantic num projeto não implica que Pydantic AI seja o runtime. Confirme pacotes, versões e fronteiras no código da aplicação.

| Componente | Papel a avaliar | Não infira automaticamente |
|---|---|---|
| Pydantic Validation | Modelos, parsing e validação de dados em runtime; schemas para interfaces | Verdade semântica, autorização ou ausência de efeitos perigosos |
| Pydantic AI | Framework Python para compor agentes, modelos/provedores, dependências, ferramentas e saídas | Persistência de negócio, isolamento ou orquestração durável completa |
| Pydantic AI Harness (`pydantic-ai-harness`) | Biblioteca separada de capacidades que podem ser acopladas a agentes; inclui composições de workspace, ficheiros/shell, memória, subagentes, gestão de contexto e guardrails | Que todo agente Pydantic AI usa o Harness ou que uma capacidade específica esteja ativada por padrão |
| pydantic-graph | Abstração Python de nós, estado, dependências e transições tipadas | Prova de corretude do processo ou que todo caminho satisfaz requisitos de domínio |
| Durable execution e integrações | Integrações opcionais com engines/workflows e mecanismos de persistência documentados | Que estejam no pacote core, ativadas por padrão ou ofereçam exatamente uma vez |
| Pydantic Evals | Avaliação de saída final e trajetória, com datasets e opções de avaliação online | Que uma métrica seja válida, um juiz seja independente ou uma avaliação autorize release |
| Pydantic Logfire | Produto de observabilidade com tracing e integrações | Obrigação de usar serviço hospedado ou envio adequado de todos os dados |
| Pydantic AI Gateway | Serviço opcional de gateway para acesso a modelos e controlo de custos | Que seja necessário para usar Pydantic AI ou adequado à política de dados/roteamento |

A disponibilidade, nomenclatura, licenciamento e limites dos componentes podem mudar. As distinções deste perfil refletem a documentação consultada em 24/11/2026; consulte as páginas atuais e inspecione a versão instalada.

## Pydantic AI e Pydantic AI Harness

Pydantic AI oferece o loop de agente tipado, ferramentas, saídas estruturadas e integração com modelos. A documentação atual apresenta Pydantic AI Harness como uma biblioteca separada, baseada em capacidades que podem ser adicionadas ou compostas num agente. As capacidades documentadas incluem workspaces, planeamento, memória, subagentes, contexto, persistência e guardrails; composições prontas também podem ser montadas a partir delas. Compare o requisito com as capacidades individuais antes de adotar uma composição completa.

O workspace define onde ficheiros e comandos executam. A documentação distingue workspace local e sandbox; uma pasta de trabalho local não é uma sandbox. Verifique se o limite de uma ferramenta de ficheiros também cobre shell, subprocessos, rede e acesso ao host. O Harness oferece opções diferentes de workspace, mas a escolha e a configuração são responsabilidade de quem compõe o agente.

## Persistência e execução durável

Não confunda salvar passos, retomar um run, memória entre sessões e recuperação de uma operação após falha. Na documentação consultada, Pydantic AI distingue snapshots de passos (úteis para persistir, retomar ou bifurcar um run) de execução durável integrada com engines externos, que pode recuperar falhas ocorridas durante um passo. Confirme as pré-condições, compatibilidade e limites da integração escolhida, incluindo chamadas externas e efeitos já executados.

## Tipos, schemas e saídas

Modelos Pydantic podem validar estrutura e restrições declaradas em runtime, converter representações e gerar schemas úteis para ferramentas ou saídas estruturadas. Type hints também podem apoiar verificações estáticas durante o desenvolvimento. São mecanismos diferentes: Python não transforma anotações em prova geral de comportamento; validação estrutural não demonstra que o conteúdo é verdadeiro, autorizado ou apropriado.

Separe no desenho:

- **Parsing e forma:** a resposta pode ser interpretada pelo schema esperado?
- **Validade de domínio:** os valores respeitam regras e estado atuais?
- **Autorização:** esta identidade pode executar este efeito sobre este recurso agora?
- **Qualidade semântica:** a resposta atende à tarefa com evidência suficiente?

As duas primeiras podem ser parcialmente codificadas num modelo, mas autorização deve ser aplicada pelo componente que controla o efeito, e qualidade semântica requer avaliação adequada à tarefa. No Pydantic AI, confira como o provider selecionado implementa saída estruturada e chamadas de ferramenta, quais falhas causam retry e quais validadores realmente executam.

## Agentes e dependências

Ao avaliar Pydantic AI, mapeie modelo/provider, dependências injetadas, ferramentas, estado conversacional, saída, retries, timeouts e ciclo de vida do agente. A injeção de dependências pode tornar serviços explícitos e testáveis, mas o objeto fornecido ao agente ainda precisa de escopo, segurança e autorização definidos pela aplicação. Não exponha uma dependência privilegiada apenas porque o agente consegue recebê-la.

Escolha o nível de abstração de acordo com o fluxo: um pedido direto ao modelo, um agente com ciclo de ferramentas e um grafo explícito resolvem problemas diferentes. Um grafo é útil quando os estados e transições precisam ser inspecionáveis; código Python mais simples pode bastar para uma sequência curta e previsível.

## pydantic-graph e execução durável

pydantic-graph é uma biblioteca de grafos/máquinas de estado que pode ser usada com ou sem Pydantic AI. Tipos e anotações ajudam a definir contratos e a verificar algumas condições. Isso não equivale a uma prova de que todos os caminhos respeitam regras de negócio, nem demonstra que os efeitos externos são atómicos ou idempotentes.

Trate separadamente:

1. definição de estado e transições;
2. snapshot/checkpoint e mecanismo de persistência;
3. processo de retomada após falha ou interrupção;
4. retries, timeouts e repetição de efeitos;
5. migração de estado entre versões;
6. aprovação humana e autorização no ponto do efeito.

Se a página de execução durável oferecer recursos para o caso, confirme seus limites e pré-requisitos. Uma API de snapshot ou retry não substitui idempotência externa nem uma fonte de verdade transacional.

## Evals e observabilidade

Pydantic Evals pode avaliar a saída final e a trajetória, incluindo sequência e argumentos de chamadas a ferramentas; a documentação atual também descreve avaliação online. Use avaliadores diferentes para formato, seleção de ferramentas, critérios semânticos, recuperação e comportamento fora do escopo. Documente dados, modelo, versões, métricas, limiar, baseline e limitações; evite que um LLM-as-judge seja a única evidência em propriedade crítica.

Tracing pode facilitar inspeção de chamadas e latência. Antes de enviar traces, defina redaction, retenção, acesso, residência e consentimento quando aplicável. Observabilidade ajuda a diagnosticar; não é prova de correção nem substitui alertas e processo operacional.

## Critérios de adequação

Considere o ecossistema quando a aplicação Python beneficia de contratos tipados, ferramentas testáveis e composição explícita com componentes conhecidos pela equipa. Avalie contra alternativas nos mesmos requisitos, incluindo:

- cobertura e compatibilidade dos providers usados;
- fronteira entre biblioteca de validação, agente, grafo e produto hospedado;
- tratamento de erro, retry, timeouts, streaming e concorrência;
- estado, checkpoint, retomada, serialização e evolução de schema;
- política de segurança, dependências e superfície de integração;
- evals, tracing, privacidade e exportação;
- esforço de atualização e custo de abstrações.

## Fontes primárias

- [Pydantic AI — overview](https://pydantic.dev/docs/ai/overview/)
- [Pydantic AI Harness](https://pydantic.dev/docs/ai/harness/)
- [Agents](https://pydantic.dev/docs/ai/core-concepts/agent/)
- [Dependencies](https://pydantic.dev/docs/ai/core-concepts/dependencies/)
- [Output](https://pydantic.dev/docs/ai/core-concepts/output/)
- [Graphs e pydantic-graph](https://pydantic.dev/docs/ai/graph/graph/)
- [Persistence](https://pydantic.dev/docs/ai/core-concepts/persistence/)
- [Durable execution](https://pydantic.dev/docs/ai/capabilities/durable_execution/overview/)
- [Pydantic Evals](https://pydantic.dev/docs/ai/evals/evals/)
- [Production](https://pydantic.dev/docs/ai/production/)

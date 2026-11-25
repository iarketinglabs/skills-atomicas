# Model Context Protocol (MCP)

## Papel do protocolo

MCP é um protocolo aberto para ligar aplicações de modelos a fontes de contexto e capacidades externas. Na especificação consultada em 24/11/2026, a comunicação usa mensagens JSON-RPC e define hosts, clientes e servidores. Servidores podem disponibilizar tools, resources e prompts; extensões são opcionais e dependem de suporte negociado.

MCP padroniza partes da integração. Não escolhe por si só quais capacidades o agente deve receber, não define a política de negócio de cada aplicação e não garante que um efeito externo esteja autorizado ou seja seguro.

## Modelo de execução

- **Host:** aplicação que inicia e controla conexões.
- **Client:** componente da aplicação que fala o protocolo.
- **Server:** serviço ou processo que oferece contexto/capacidades segundo MCP.
- **Tool:** operação invocável que pode ter efeitos; argumentos, resultado e falha precisam de contrato.
- **Resource e prompt:** formas de apresentar dados ou mensagens reutilizáveis; a disponibilidade e o consumo dependem do cliente e do host.

Uma instalação pode usar processo local por stdio ou transporte de rede. Investigue origem, identidade do processo, rede, dependências, configuração e ciclo de atualização do servidor concreto.

## Descoberta, seleção e custo de contexto

Não existe um limite universal de servidores, ferramentas ou conexões que seja seguro ou eficiente para todos os clientes e tarefas. O custo e o comportamento dependem do modelo, cliente, schemas, descrições, resultados, estratégia de descoberta e momento em que as capacidades são expostas.

Meça no ambiente real:

- quantas descrições e schemas entram em cada chamada ao modelo;
- quanto contexto e latência são consumidos pela descoberta e pelos resultados;
- se a ferramenta relevante é selecionada corretamente;
- se o host permite carregamento seletivo, pesquisa ou descoberta tardia;
- como cache e invalidação funcionam no cliente usado;
- se as ferramentas disponíveis excedem as permissões ou necessidades da tarefa.

Filtragem, pesquisa e descoberta sob demanda podem reduzir contexto quando o cliente e o fluxo suportam essas estratégias. Não presuma que todos os hosts as implementam da mesma forma. Evite carregar ferramentas irrelevantes, mas preserve descoberta suficiente para que o agente encontre a capacidade necessária.

## Segurança e autorização

Descrições, schemas, resultados e conteúdo de recursos podem conter dados incorretos ou instruções não confiáveis. Trate-os como dados, não como política. A proposta do modelo para chamar uma ferramenta é uma entrada a validar. Imponha identidade, escopo e autorização no servidor ou serviço que controla o efeito; valide argumentos e estado atual antes de agir.

Para cada integração, documente:

- identidade do utilizador e do serviço, scopes e propagação de contexto;
- dados que podem ser lidos, escritos ou enviados para terceiros;
- validação, autorização e consentimento necessários;
- gestão de segredos, transporte, certificados e limites de rede;
- efeitos, logging, auditoria, rate limits e comportamento de erro;
- confiança no servidor, nas dependências, nas atualizações e na sua cadeia de fornecimento;
- isolamento entre utilizadores e tenants.

O protocolo inclui orientações de segurança e suporte a mecanismos de autorização, mas o host e a aplicação precisam implementá-los corretamente. Uma conexão MCP autenticada não prova que cada chamada está autorizada para cada recurso ou operação.

## Ferramentas MCP e execução de código

Uma tool MCP costuma fornecer uma operação delimitada com nome, descrição, argumentos e resultado. Para tarefas que precisam compor muitas consultas, filtrar grandes respostas ou processar dados localmente, uma abordagem alternativa pode expor bibliotecas ou operações num ambiente de execução de código e retornar apenas resultados selecionados.

Essa abordagem pode reduzir idas-e-voltas e conteúdo enviado ao modelo em certos workloads. Também aumenta a superfície: código escrito pelo modelo, acesso a ferramentas, filesystem, rede, dependências e dados precisam de um sandbox e permissões adequados. A economia de contexto depende da carga, e não substitui validação nem autorização. Compare ambas as opções com a mesma tarefa e condições.

## Falhas e operações

Timeout, cancelamento, erro de transporte ou reinício do servidor podem deixar incerto se uma operação chegou a ser aplicada. Registe identificadores de correlação e o estado do pedido; não repita efeitos não idempotentes apenas porque não recebeu uma resposta. Use contrato de idempotência do destino, consulta de estado, deduplicação ou conciliação conforme o caso. Um protocolo de ferramentas não torna automaticamente cada operação durável ou exatamente uma vez.

Teste desconexão, timeout, respostas inválidas, schema incompatível, reinício do processo e revogação de credenciais. A política de retry e recuperação deve ser definida pelo cliente e pela aplicação com base no efeito concreto.

## Decidir quando usar MCP

MCP pode reduzir o custo de criar integrações quando cliente e servidor partilham o protocolo e as capacidades se encaixam no contrato. Uma API direta, CLI, biblioteca local, fila ou workflow tradicional também pode ser mais simples. Compare compatibilidade do cliente, descoberta, autorização, latência, deployment, observabilidade, atualização, contexto e comportamento em falha.

## Fontes primárias

- [Especificação MCP](https://modelcontextprotocol.io/specification/2026-07-28)
- [Anthropic — Code execution with MCP](https://www.anthropic.com/research/code-execution-with-mcp): exemplo de trade-offs e resultados num setup específico, não um benchmark universal.
- [MCP Python SDK](https://py.sdk.modelcontextprotocol.io/): confirme a linha de versão e as APIs usadas.

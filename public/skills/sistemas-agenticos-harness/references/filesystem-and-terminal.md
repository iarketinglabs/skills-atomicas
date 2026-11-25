# Filesystem e terminal

Ferramentas de filesystem e terminal dão ao agente capacidades concretas sobre ficheiros, processos e serviços. A interface pode ser uma shell, uma API estruturada, um sistema virtual, uma ferramenta remota ou uma combinação. Não existe uma forma universalmente melhor: compare expressividade, custo de contexto, validação, segurança, ergonomia, operação e comportamento do modelo.

## Definir o espaço de trabalho

Especifique o que cada execução pode ler, criar, alterar, executar ou enviar. Separe, conforme necessário, diretórios de entrada, rascunho, saída, cache e configuração. Credenciais não devem entrar no contexto do modelo; ferramentas recebem apenas os segredos e scopes indispensáveis.

Restrições de caminho no prompt não são isolamento. Aplique limites de filesystem e processo no ambiente que executa a chamada. Em sistema multiutilizador, valide identidade, tenant e caminho resolvido no servidor, incluindo links simbólicos e escapes do workspace.

## Shell, APIs ou ferramentas específicas

Uma shell é flexível e pode reduzir a quantidade de ferramentas expostas. Também amplia a superfície de comandos, composição, parsing, egress e efeitos colaterais. Ferramentas específicas podem oferecer contratos mais simples e autorização mais granular, mas muitas assinaturas semelhantes podem ser difíceis de selecionar.

Escolha por capacidade e risco. Limite executáveis, diretórios, rede, tempo, CPU/memória e operações privilegiadas. Valide argumentos e resultados. A saída do terminal é dado não confiável; sanitize segredos e preserve evidência suficiente para diagnóstico.

## Busca e edição

Em bases grandes, comece por índices, nomes e cabeçalhos; localize trechos por busca e leia contexto suficiente antes de editar. A revelação progressiva pode reduzir contexto, mas a redução real varia com o material, ferramenta e tarefa. Meça qualidade da alteração e não remova informação necessária para entender dependências.

Em escrita concorrente, use versão, diff, patch ou transação para detectar mudanças entre leitura e aplicação. Antes de gravar, confirme que o alvo está dentro do escopo. Valide o resultado e guarde o estado anterior quando a reversão fizer parte do contrato.

## Isolamento e colaboração

Para execuções simultâneas, pode ser adequado usar sandbox por tarefa, container, VFS, branch ou Git worktree. Esses mecanismos têm limites diferentes: um worktree separa árvores de trabalho, mas não isola por si só rede, credenciais ou processos; uma sandbox pode limitar acesso físico, mas requer configuração e revisão.

Defina como alterações saem do ambiente isolado e quem integra, revê ou publica. A passagem de artefactos não deve contornar autorização ou revisão que a aplicação exige.

## Segurança do terminal

Uma blacklist textual de comandos não é uma sandbox: shell permite expansão, aliases, scripts, codificação e composição. Filtros por regex podem ser defesa adicional, mas não barreira única. Prefira permissões do sistema, comandos/operadores explicitamente autorizados, execução em ambiente isolado, egress controlado e aprovação para efeitos relevantes.

Se o risco justificar gate pré-execução, valide comando normalizado, argumentos, diretório, ambiente e conteúdo que será executado. Considere que scripts escritos agora podem ser executados depois. Revalide no ponto de execução e mantenha a política fora do controle do agente quando a garantia precisar ser efetiva.

## Observabilidade e recuperação

Registe identificadores de execução, chamada de ferramenta, parâmetros com redação de dados sensíveis, resultado, duração e decisão de política. Retenha stdout/stderr conforme a necessidade e o risco; um resumo não deve substituir a fonte se for necessário auditar.

Um checkpoint só permite retomada conforme os dados e o mecanismo persistidos. Ele não garante recuperação exata nem evita repetição de um efeito remoto. Veja `state-graphs-and-loop-control.md` e a skill de resiliência quando disponível.

## Revisão antes de executar

- A identidade e a permissão correspondem ao recurso e à operação?
- O caminho permanece dentro do escopo depois de resolvido?
- O comando pode ler segredos, atingir rede ou afetar recursos fora do workspace?
- Há limite de recursos, timeout e forma de cancelar?
- Um efeito pode repetir-se depois de timeout ou reinício?
- Como resultado, erro e bloqueio serão auditados?
- A saída será integrada por que processo e com que validação?

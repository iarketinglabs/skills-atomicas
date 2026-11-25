# Sandboxing e isolamento de execução

Uma sandbox limita o que uma execução consegue ler, escrever, executar ou contactar. É uma camada de contenção, não uma garantia absoluta. O isolamento necessário depende de dados, ferramentas, adversários, efeito potencial, runtime e custo operacional.

## Modelo de ameaça

Descreva a combinação entre dados privados, conteúdo externo não confiável e capacidade de comunicar ou alterar sistemas. Essa combinação — chamada por Simon Willison de *lethal trifecta* — é uma heurística para identificar caminhos de exfiltração e abuso, não uma medida quantitativa de risco nem uma arquitetura única.

Considere também credenciais herdadas, ferramentas de terceiros, dependências, memória contaminada, processos vizinhos, egress, acesso a APIs internas, persistência e alterações irreversíveis. O modelo pode propor ações perigosas ou ser influenciado por conteúdo externo; instruções em linguagem natural não são controles de acesso.

## Controles em camadas

Defina a fronteira no ambiente que executa a ferramenta:

- **Identidade e privilégio:** credenciais de curta duração e escopo mínimo, com autorização por recurso e operação.
- **Filesystem:** diretórios montados explicitamente, permissões de processo e proteção contra escape de caminho ou link simbólico.
- **Processos:** utilizador de baixo privilégio, capabilities restritas e limites de memória, CPU, processos e tempo.
- **Rede:** sem egress quando desnecessário; quando necessário, allowlist de destinos e política contra SSRF.
- **Segredos:** manter fora do contexto do modelo e limitar acesso do processo; quando aplicável, usar broker que executa operações com autorização sem expor credencial.
- **Efeitos:** validação no serviço que controla o recurso, logs, idempotência e aprovação proporcional ao impacto.
- **Observabilidade:** correlacionar pedido, identidade, decisão de política, execução e resultado sem registar segredos desnecessários.

Uma ferramenta que oculta a credencial não elimina os poderes concedidos pelo broker. Limite ações, escopo e dados retornados pelo mesmo princípio de menor privilégio.

## Escolha do isolamento

Containers, microVMs, VMs, processos restritos, interpreters e ambientes virtuais têm fronteiras e custos diferentes. Investigue o isolamento de kernel, montagem de volumes, permissões, rede, persistência, imagens, inicialização, atualização e limpeza. Não infira isolamento forte só pelo nome “sandbox” ou pela existência de um container.

Filesystem virtual, snapshot ou workspace descartável podem ser úteis para tarefas que alteram ficheiros. Um Git worktree separa árvores e branches de trabalho, mas não isola secrets, rede ou processos do host. Combine mecanismos conforme as ameaças relevantes.

## Bypass por composição

Bloquear uma string de comando não bloqueia toda forma de executar o mesmo efeito: pode haver shell, script, binário, API, tarefa agendada ou ferramenta alternativa. Regex e blocklists podem servir de sinal ou defesa adicional, mas não devem ser a fronteira de segurança. Restrinja a capacidade no SO, container, broker ou serviço que controla o efeito, e valide também artefactos e subprocessos conforme a execução permite.

## Aprovação humana

Considere confirmação por pessoa para efeitos de alto impacto, irreversíveis ou externos quando a política de risco assim exigir. A interface de aprovação deve mostrar identidade, operação, alvo, parâmetros e consequência relevante; deve expirar e ser ligada à ação aprovada. Ao retomar, revalide estado e autorização. Um agente revisor pode ajudar a encontrar erros, mas não é substituto de política determinística nem aprovação humana exigida.

## Limites, cancelamento e persistência

Defina timeout, orçamento de chamadas, rate limit, limite de concorrência e mecanismo de cancelamento compatíveis com o workload. Um processo cancelado pode ter deixado um efeito remoto em andamento. Determine como consultar o destino, conciliar resultados incertos e evitar duplicações antes de retry.

“Execução efémera” e “estado durável” não são opostos absolutos: um processo pode ser curto e recuperar estado persistido, ou persistir durante muito tempo sem recuperação segura. Decida quais artefactos sobreviverão, onde ficam, por quanto tempo e como são eliminados.

## Checklist de revisão

- Que conteúdo não confiável o modelo pode receber?
- Que dados privados estão acessíveis e qual ferramenta pode enviá-los para fora?
- Quais capacidades são realmente necessárias a esta tarefa?
- O isolamento é imposto pelo ambiente e foi verificado contra os caminhos relevantes?
- Há credenciais, acesso à rede ou filesystem além do escopo necessário?
- Como são tratados scripts, subprocessos, dependências e caminhos indiretos de execução?
- Que efeitos exigem autorização atual, idempotência ou aprovação?
- O que persiste após a tarefa, como é auditado e como é removido?

## Fontes

- [Simon Willison — The lethal trifecta for AI agents](https://simonw.substack.com/p/the-lethal-trifecta-for-ai-agents)
- [OWASP — AI Agent Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html)
- [OWASP — MCP Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html)

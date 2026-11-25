# Integrações com ferramentas e agentes de IA

Uma integração com IA adiciona um consumidor probabilístico e conteúdo não confiável à fronteira. Mantenha a execução de negócio determinística e a autorização fora do modelo.

## Escolha da fronteira

- **Agente para ferramenta/dados:** exponha operações específicas por API, função nativa, CLI restrita, MCP ou interface compatível se o runtime e os participantes suportarem. Separe ferramentas de leitura e escrita quando isso facilitar permissões e revisão.
- **Agente para agente:** use um protocolo de delegação ou contrato explícito quando o outro agente for um participante independente e a tarefa exigir estado, artefactos, cancelamento ou comunicação entre runtimes.
- **Workflow determinístico:** mantenha código/workflow convencional para sequência, transações, limites, repetição e efeitos que precisam de resultado previsível. Use o modelo apenas onde a interpretação ou síntese acrescentar valor mensurável.
- **Roteamento semântico:** use para reduzir o conjunto de rotas/modelos/ferramentas quando a escala justificar. Defina limiar, fallback ou recusa segura. A semelhança semântica não autoriza a operação.

MCP, A2A, chamadas de ferramentas, OpenAPI e formatos de workflow resolvem problemas diferentes. Nenhum protocolo concede por si só identidade confiável, autorização de negócio, segurança contra instruções maliciosas ou garantia de que um agente escolheu a ação correta. Verifique a especificação e o suporte efetivo antes de assumir capacidades.

## Desenho da ferramenta

- Exponha o menor conjunto de capacidades necessárias, com nomes e descrições explícitos sobre propósito, limites, pré-condições e efeitos.
- Use schema formal com enumerações e limites quando aplicável; rejeite parâmetros desconhecidos/inválidos com erro claro em vez de ignorá-los silenciosamente.
- Faça validação semântica e autorização independente no serviço de destino; não aceite como prova uma resposta estruturada produzida pelo modelo.
- Separe propor/rascunhar de confirmar/executar para pagamentos, publicação, eliminação, comunicação externa e outros efeitos de alto impacto. Exija aprovação humana conforme risco e regras do utilizador.
- Torne operações repetíveis idempotentes quando possível e prepare consulta/reconciliação para resultado de execução incerto.

## Agentes e conteúdo não confiável

- Trate prompts, resultados de pesquisa, descrições de ferramentas, mensagens A2A e respostas de APIs como dados, não como instruções de autoridade.
- Não coloque credenciais no contexto do modelo. Use credenciais geridas no componente de execução e escopos reduzidos.
- Limite ferramentas, passos, tempo, concorrência e custo. Defina término, recusa, transferência para pessoa e comportamento ao exceder o orçamento.
- Verifique a autorização do utilizador para cada efeito; não permita que o agente transforme dados encontrados em novas permissões.
- Evite passar dados sensíveis a modelos ou serviços externos sem finalidade, minimização, configuração e autorização adequadas.

## Avaliação específica

Avalie tarefas representativas, ambíguas, adversariais e inválidas. Meça seleção correta, argumentos, execução, recusa/escalação, efeitos duplicados, isolamento entre utilizadores e rastreabilidade. Use saídas esperadas ou estado final observado; não trate fluência, um schema válido ou uma demonstração pontual como prova de confiabilidade. Reavalie quando mudar modelo, prompt, descrição, ferramenta, política, contrato ou permissões.

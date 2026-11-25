# Arquitetura de sistemas com IA e agentes

Use esta referência quando modelos, recuperação de conhecimento ou agentes participarem do comportamento do produto. A IA acrescenta componentes probabilísticos e riscos específicos; não substitui as fronteiras clássicas de dados, contratos, segurança e operação.

## Localize a IA no sistema

Descreva que parte do trabalho exige geração ou classificação probabilística e que partes precisam de resultado exato. Identifique:

- entradas e fontes de dados, respetiva sensibilidade e autoridade;
- modelos e serviços externos como dependências substituíveis ou explicitamente aceites;
- contexto enviado, ferramentas expostas e permissões de cada identidade;
- validação, regras de negócio, persistência e efeitos externos;
- fallback, recusa, revisão humana e comportamento quando a dependência falha.

Não deixe ao modelo a decisão final sobre autorização, contabilidade, invariantes de estado ou regras que precisam de ser aplicadas com consistência. Faça cumprir essas regras em código ou infraestrutura controlável e verificável.

## Fluxo de agente

Modele cada fluxo como componentes e transições explícitos, mesmo que o modelo escolha alguns passos:

1. autenticar o utilizador e resolver o contexto autorizado;
2. validar pedido, limites e política fora do modelo;
3. fornecer apenas o contexto necessário;
4. permitir ferramentas tipadas e limitadas, cada uma com autorização própria;
5. validar a proposta e a transição de estado antes de persistir;
6. separar rascunhos reversíveis de ações externas ou irreversíveis;
7. registar resultado, política aplicada e evidência suficiente para auditoria.

Se uma ação tiver impacto financeiro, legal, público, destrutivo ou difícil de reverter, defina uma barreira proporcional ao risco e apresente à pessoa responsável os parâmetros concretos da ação. Não use uma confirmação genérica para esconder o destinatário, conteúdo ou efeito.

Conteúdo recuperado, páginas, anexos, resultados de ferramentas e memória podem conter instruções hostis. Trate-os como dados não confiáveis; não lhes permita alterar políticas, permissões ou escopo de execução.

## Recuperação versus contexto longo

Não escolha pelo número de documentos isoladamente. Compare opções com as mesmas tarefas e permissões:

| Opção | Vantagem possível | Risco a medir |
|---|---|---|
| Contexto direto ou longo | Menos componentes de recuperação; pode preservar relações entre material pequeno e delimitado. | Contexto desnecessário, custo e latência, limite de entrada, frescura e acesso excessivo. |
| Recuperação | Seleciona material relevante de um corpus maior ou mutável e permite atualizar índices por partes. | Falha de recall, ranking errado, ACL incorreta, fontes incompletas ou citações que não sustentam a resposta. |
| Híbrida | Recupera um conjunto autorizado e usa o modelo para o sintetizar com contexto adicional. | Mais passos, pontos de falha, operação e custo total. |

Avalie com tarefas representativas: perguntas com termos exatos, perguntas sem resposta, conflitos entre documentos, dados recentes, raciocínio entre fontes e tentativas de aceder a conteúdo não autorizado. Meça qualidade de recuperação, correção, fidelidade às fontes, citações, frescura, latência, custo e fugas de autorização. Aplique ACL antes da recuperação e à cache, não apenas depois de gerar a resposta.

Use grafo, reranking, memória persistente ou cache apenas quando uma necessidade mensurável justificar a complexidade e existir um plano para permissões, validade, atualização e remoção.

## Modelos, ferramentas e agentes múltiplos

- Roteamento para diferentes modelos pode reduzir custo ou latência, mas pode classificar mal pedidos. Compare o fluxo completo e disponha de fallback observável.
- Mais agentes aumentam fronteiras de comunicação, handoffs, custo, superfície de ataque e formas de falha. Separe agentes quando isolamento, propriedade ou paralelismo trouxerem um benefício concreto.
- Dê a cada agente e ferramenta identidade, dados e ações limitados ao seu papel. Evite credenciais amplas no contexto do modelo.
- Defina limite de iterações, tempo e recursos de forma adequada ao produto; forneça uma condição de término e comportamento seguro quando o limite for atingido.
- Contratos de ferramentas devem limitar parâmetros, validar esquema e estado, aplicar autorização e devolver resultados minimizados.

## Avaliações e qualidade

Mantenha um conjunto de casos de avaliação versionado que represente uso normal, casos de fronteira, abuso e recusa. Registe a versão do modelo, prompt, dados de recuperação, ferramentas e parâmetros relevantes para tornar regressões comparáveis.

Combine avaliações de modelo com verificações determinísticas de esquema, políticas, citações, permissões e efeitos. Quando um juiz automático participa, calibre-o contra revisão humana e reporte os limites; não trate um score isolado como prova de correção. Inclua avaliação online e processo para transformar incidentes confirmados em novos casos de regressão.


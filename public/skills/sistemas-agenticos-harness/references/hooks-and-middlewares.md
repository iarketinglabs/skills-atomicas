# Hooks e middlewares

Hooks e middlewares são pontos de extensão do ciclo de execução. Os nomes e a ordem exata variam entre SDKs e runtimes; consulte a documentação da versão instalada em vez de assumir um ciclo de vida comum.

De forma geral:

- **Hook:** callback associado a um evento ou etapa, como entrada, chamada de modelo, chamada de ferramenta, erro, pausa ou conclusão.
- **Middleware:** componente que envolve ou intercepta parte do fluxo e pode transformar dados, controlar passagem, acrescentar observabilidade ou alterar a execução.

Um middleware pode exercer controlo, e um hook pode transformar dados. A semântica concreta vem da implementação.

## Pontos de extensão a procurar

| Momento possível | Uso | Limite a verificar |
|---|---|---|
| Antes da chamada ao modelo | Selecionar contexto, aplicar redaction, acrescentar configuração | Se o hook corre em todas as entradas, incluindo retries e retomadas |
| Antes da ferramenta | Validar schema, política, identidade, aprovação ou orçamento | Se algum caminho executa ferramenta sem passar pelo gate |
| Depois da ferramenta | Normalizar resposta, registar resultado, reduzir saída | Se o original é preservado para auditoria e diagnóstico |
| Em erro ou timeout | Classificar falha, fallback ou política de retry | Se o efeito remoto pode já ter ocorrido |
| Em pausa/retomada | Capturar estado e pedir aprovação | Se a retomada revalida estado e autorização |
| Após resumo/compactação | Reintroduzir informações que precisem persistir | Se o runtime fornece o evento e como o resumo é validado |

Não assuma que todos estes pontos existem, nem que hook configurado é executado em cada variante do runtime. Faça uma prova de cobertura dos caminhos: entrada normal, erro, retry, cancelamento, interrupção e chamada aninhada.

## Segurança e gates

Um gate pré-ferramenta pode bloquear ou exigir revisão antes de operações sensíveis. Defina critérios observáveis, identidade do aprovador, conteúdo mostrado, expiração, auditoria e comportamento quando o serviço de aprovação está indisponível. Revalide no serviço que executa o efeito; não use prompt, avaliação por outro agente ou blacklist textual como única autorização.

Escolha comportamento de falha adequado: bloquear pode interromper disponibilidade; permitir pode quebrar uma garantia. Documente a decisão por operação e teste falhas do próprio middleware. Credenciais e segredos devem ficar fora de prompts e traces.

## Transformação e compactação de dados

Um componente pode resumir logs, filtrar campos ou formatar respostas grandes. Preserve a distinção entre saída original e representação resumida. Se a decisão depender de linhas removidas, o sistema deve conseguir consultar ou apresentar a fonte completa de forma controlada.

Evite inserir timestamp ou conteúdo variável em prefixos cacheados sem necessidade. A elegibilidade, TTL e invalidação de cache são específicos do modelo/provedor. Meça a configuração efetiva; não imponha nova sessão nem bloqueie troca de modelo como regra universal.

## Estado entre hooks e agentes

Hooks podem transmitir contexto ou registar eventos, mas o modo de armazenamento precisa de um contrato: schema, versão, autorização, concorrência, retenção e recuperação. Um ficheiro Markdown, banco de dados ou serviço partilhado são opções com trade-offs, não uma camada automaticamente soberana.

Se um evento ou chamada puder ser repetido, torne handlers idempotentes ou identifique duplicações. Se o efeito externo for incerto, use a política de conciliação aplicável.

## Checklist de implantação

- A documentação da versão define quando e em que ordem cada extensão executa?
- Há teste ou evidência para caminhos de erro, retry, cancelamento e retomada?
- O gate é aplicado também no serviço que realiza o efeito?
- O modo de falha está definido e observável?
- Dados sensíveis são redigidos antes de logging ou envio externo?
- Transformações preservam fonte e evidência necessárias?
- Extensões e handlers são versionados, limitados e auditáveis?

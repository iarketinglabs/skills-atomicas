# Evidência e Frameworks de Segurança

Use esta referência para separar controles duráveis de afirmações que dependem de versão, data, jurisdição ou implementação. Os documentos de pesquisa são insumos de síntese, não autoridade normativa automática.

## Princípios estáveis

Podem orientar o desenho independentemente de fornecedor:

- defesa em profundidade e fail closed;
- menor privilégio, menor agência e separação de deveres;
- identidade própria e cadeia de delegação auditável;
- autorização, validação e isolamento fora do modelo;
- proveniência e integridade de dados, ferramentas e memória;
- aprovação proporcional ao impacto e revogação rápida;
- telemetria minimizada, testes adversariais e recuperação exercitada.

## Evidência versionada

Listas de riscos, taxonomias, convenções, drafts, números de mercado, nomes de controles e recomendações de fornecedores devem registrar:

`fonte, versão/data, escopo, status (normativo, proposta, pesquisa ou debate), hipótese, limitação e data de revalidação`

Não trate a existência de uma lista ou framework como prova de cobertura. Mapeie cada risco para um controle, owner, evidência e teste.

## Como usar frameworks

1. Use um framework para vocabulário e cobertura inicial.
2. Converta o item em cenário de ameaça e fluxo de dados/efeito.
3. Defina enforcement determinístico e condição de bloqueio.
4. Teste abuso, bypass, falha de dependência, resultado vazio e recuperação.
5. Registre o que não foi coberto e quando revisar.

## Debates e limites

Mantenha explicitamente as incertezas sobre frequência de prompt injection, eficácia de classificadores, detectabilidade de ataques em runtime, coordenação entre agentes e equivalência entre identidade clássica e identidade não-humana. Quando a decisão depender dessas questões, declare a hipótese e procure evidência atualizada antes de transformar a hipótese em requisito.

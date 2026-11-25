# Mineração de Formulários de Maturidade

Use esta referência quando a base receber um instrumento de autoavaliação de maturidade/readiness, respostas individuais ou uma exportação agregada. Ela orienta a documentação e a interpretação da evidência. Não substitui o desenho do questionário nem define uma escala ou fórmula universal de score.

## Identifique o instrumento e a coleta

Antes de interpretar respostas, registre:

- versão do formulário, data ou janela de coleta e público-alvo declarado;
- população convidada, número de respostas submetidas e estado das respostas parciais, se esses dados forem verificáveis;
- finalidade declarada, itens obrigatórios/opcionais, regras de salto e política de identidade ou anonimato;
- identificador original de cada pergunta, dimensão, tipo de resposta e opções/âncoras da escala;
- fonte, data de extração e estado da resposta (`submitted`, `draft` ou equivalente), quando fornecidos pelo sistema.

Se houver apenas o instrumento sem respostas, documente sua estrutura e o plano de coleta como instrumento; perguntas, opções e exemplos não são evidência sobre a empresa.

## Mapeie os tipos de informação

Preserve os itens e identificadores da fonte. A numeração exibida no formulário pode diferir das chaves da exportação; não reordene nem renomeie respostas para fazê-las coincidir com o modelo visual.

Separe, quando existirem:

- uso declarado de ferramentas, tarefas específicas, frequência e tentativas abandonadas;
- autoavaliação por dimensão e inventário de capacidades concretas;
- exemplos de trabalho que ajudam a contextualizar uma autoavaliação;
- percepção de utilidade, limites de julgamento humano, preocupações e barreiras;
- perguntas opcionais sobre práticas de risco, ferramentas pessoais ou tratamento de dados.

Esses blocos medem coisas diferentes. Frequência de uso não demonstra capacidade; capacidade autoavaliada não demonstra resultado; percepção de risco não comprova um incidente; exemplo narrado não valida por si só uma habilidade ou ganho.

Quando a escala usa descrições comportamentais, preserve seus rótulos e âncoras completos. Mantenha distintos `não sei`, `nunca usei`, resposta em branco, salto lógico e menor nível da escala. Não os converta automaticamente no mesmo valor.

## Interprete respostas como autorrelato

Uma resposta submetida é evidência factual de que a pessoa declarou aquela resposta, com a data, a versão e o contexto disponíveis. Ela não é verificação independente da prática, competência, resultado ou maturidade de uma equipe. Escreva conclusões como autorrelato e indique quando uma validação por entrevista, observação ou registro operacional ainda falta.

Respeite a finalidade, a voluntariedade e as promessas de privacidade comunicadas pelo instrumento. Itens opcionais continuam opcionais na análise: informe quantas pessoas responderam ao item e qual denominador foi usado. Não transforme respostas individuais em avaliação de desempenho nem atribua opiniões a áreas sem base adequada.

Se um item relatar possível exposição de dados, uso não aprovado ou outro risco, preserve o relato como autorrelato e abra a validação necessária. O formulário sozinho não estabelece alcance, recorrência, causa ou gravidade do evento.

Um pedido para relatar um exemplo concreto — como a capacidade em que a própria pessoa se avaliou melhor — serve para contextualizar e planejar validação. Não use esse relato para corrigir a nota, classificar a pessoa ou provar ROI.

## Agregação, cobertura e comparação

- Informe `n` por item/dimensão, respostas ausentes, público-alvo e período. Calcule taxa de resposta somente quando o total convidado e a data de corte forem conhecidos.
- Mostre distribuição por nível quando ela preservar diferenças entre respondentes. Não reduza automaticamente escalas ordinais a médias ou a um score composto.
- Mantenha a leitura agregada quando a amostra for pequena ou puder reidentificar pessoas. Não infira maturidade de uma área a partir de poucos respondentes nem trate não resposta como nível baixo.
- Compare rodadas somente quando versão, população, âncoras, janela e critérios forem compatíveis. Para mudanças no instrumento, registre os limites e a correspondência adotada antes de comparar.
- Um score organizacional depende dos gates do PRD e de evidência adequada por dimensão (RN-14). Se eles não forem atendidos, registre a distribuição, as limitações e as lacunas; não preencha o score por média, pela opinião da liderança ou pela intenção de adoção.

## Propagação

1. Atualize o documento de domínio de maturidade/readiness com a leitura, a proveniência, a versão do instrumento, a cobertura e os limites de autorrelato.
2. Registre na matriz somente achados materiais, com IDs/campos originais, data, dimensão, `n` e denominador, status e validação pendente.
3. Atualize lacunas para não resposta, cobertura insuficiente, dúvida de interpretação ou confirmação operacional que ainda falte.
4. Registre mudanças substantivas no changelog. Atualize o índice de entregáveis somente se um gate ou estado mudar.

## Checklist

- [ ] Distingui a versão do instrumento das respostas e preservei as chaves originais.
- [ ] Separei uso, capacidade autoavaliada, exemplo concreto, percepção e risco.
- [ ] Mantive estados de resposta, itens opcionais, `não sei`, não uso e ausência de resposta distintos.
- [ ] Registrei população, `n`, denominadores, período, versão e limites de representatividade conhecidos.
- [ ] Respeitei a finalidade e as condições de privacidade do instrumento; minimizei dados pessoais.
- [ ] Não tratei autorrelato, não resposta ou uma amostra pequena como score organizacional, ocorrência confirmada ou avaliação individual.
- [ ] Não calculei score sem cumprir os gates do PRD; lacunas e validações pendentes continuam explícitas.

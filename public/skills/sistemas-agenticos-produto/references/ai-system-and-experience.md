# Sistema de IA e experiência

## Escolher o nível de solução

Comece pelo menor mecanismo capaz de resolver a tarefa:

| Necessidade | Opção inicial a considerar |
|---|---|
| Resultado definido por regras estáveis e verificáveis | Regra ou código determinístico |
| Interpretação de linguagem, imagem, áudio ou geração flexível | Modelo, com critérios de qualidade e fallback |
| Conhecimento privado, atualizado ou que precisa de proveniência | Retrieval de fontes autorizadas e resposta ancorada |
| Sequência conhecida de passos e decisões delimitadas | Workflow com etapas, validações e regras explícitas |
| Próximo passo depende do estado observado e não pode ser antecipado de forma razoável | Agente com ferramentas e autonomia delimitada |

Estas opções podem ser combinadas. Um agente não é sinónimo de qualquer funcionalidade que chama um modelo. Se a sequência puder ser codificada de forma explícita, um workflow tende a ser mais previsível, auditável e fácil de avaliar. Acrescente autonomia só quando a adaptação dinâmica criar valor medido que compense custo, latência e superfície de falha.

## Prompt, contexto, retrieval e fine-tuning

- Use instruções e exemplos para esclarecer comportamento ou formato.
- Use engenharia de contexto para escolher que instruções, estado, memória, resultados intermédios e ferramentas são necessários em cada etapa.
- Use retrieval quando a resposta depende de fontes externas, privadas, extensas, mutáveis ou citáveis. Avalie recuperação, ranking, cobertura, conflitos e uso correto da evidência; a presença de retrieval não garante grounding.
- Considere fine-tuning para um padrão comportamental estável quando prompting e contexto não atingem o nível desejado, existe conjunto de dados apropriado e evals conseguem medir ganho. Não o escolha apenas para incorporar factos que mudam frequentemente.
- Use regras ou código para validações exatas, autorizações, cálculos e decisões procedurais sempre que forem suficientes.

Escolha por evals do domínio. Evite percentagens universais sobre quantas tarefas um modelo pequeno, RAG ou agente resolverá.

## Definir fronteiras de comportamento

Para cada função, especifique:

- Quem inicia a tarefa e que objetivo foi autorizado.
- Entradas aceites, fontes permitidas e dados que não devem ser usados.
- Saídas esperadas e critérios para declarar que a tarefa foi concluída.
- Situações em que o sistema deve pedir esclarecimento, recusar, interromper ou encaminhar.
- Ferramentas disponíveis, permissões, validações e limites de execução.
- Ações reversíveis, ações que pedem aprovação e mecanismo para cancelar ou corrigir.
- Fallback, tratamento de timeout, falha de retrieval, resposta vazia e indisponibilidade.

Uma escala útil para discutir autonomia é: recomendação; preparação de uma ação; execução após aprovação; execução autónoma limitada e reversível; coordenação autónoma com intervenção em exceções. Esta escala é vocabulário de design, não um standard nem uma classificação de risco legal.

## UX perante incerteza

- Desenhe a interação a partir da tarefa e do resultado que a pessoa procura. Uma caixa de texto livre não precisa ser a única forma de começar: quando a intenção é previsível, ofereça objetivos, campos, exemplos ou passos guiados; mantenha entrada aberta quando ela for útil para a tarefa.
- Mostre fontes, dados ou evidência utilizados quando isso ajuda a avaliar a resposta.
- Identifique lacunas e conflitos em vez de os esconder.
- Não apresente confiança numérica sem calibração empírica que sustente a interpretação.
- Permita editar, corrigir, pedir nova execução e perceber o que será alterado.
- Explique ferramentas usadas, permissões e motivos para uma aprovação; não apresente raciocínio interno do modelo como prova de correção.
- Ofereça um caminho manual ou encaminhamento humano proporcional ao impacto.
- Use divulgação progressiva: exponha mais contexto e avisos nos casos de maior risco, sem sobrecarregar cada interação de baixo risco.
- Considere teclado, leitores de ecrã, mensagens de estado, conteúdo longo e alternativas a streaming ou controlos visuais exclusivos.
- Torne capacidades, limites e estado da tarefa compreensíveis. Indique quando o sistema está a preparar, executar, aguardar autorização, devolver um resultado parcial ou falhar; não use animação ou linguagem que sugira progresso inexistente.

## Controlo, colaboração e contexto

- Ajuste a autonomia ao impacto, alcance e reversibilidade. Deixe claro se o sistema está a sugerir, preparar ou executar uma ação. Quando houver consequências relevantes, apresente o plano e as alterações propostas para revisão antes da execução; permita interromper e cancelar.
- Disponibilize correção e reversão proporcionais ao que pode ser desfeito. Para operações que não podem ser revertidas, explique a consequência e peça autorização explícita antes de agir. Não transforme a aprovação humana numa confirmação repetitiva sem valor.
- Ofereça explicações a pedido que apontem para fontes, dados, regras ou ações relevantes. Não substitua essa evidência por uma narrativa interna do modelo nem por uma pontuação de confiança sem significado validado.
- Se a experiência guardar contexto ou preferências, explique o que é retido e como influencia resultados. Dê meios apropriados para inspecionar, corrigir, apagar ou desligar essa memória; minimize a recolha e evite reutilizar informação fora do contexto esperado.
- Use interfaces adaptativas ou multimodais quando melhorarem a tarefa ou o acesso. Preserve uma forma estável de orientação e alternativas equivalentes, incluindo teclado e tecnologias de apoio. Não altere silenciosamente controlos críticos nem infira necessidades sensíveis sem base e autorização adequadas.
- Sinalize conteúdo gerado, transformado ou recomendado por IA quando a origem puder afetar a interpretação, atribuição ou decisão da pessoa, e cumpra requisitos aplicáveis. Não trate um rótulo genérico como substituto para proveniência, limites ou possibilidade de verificação.
- Evite padrões manipulativos, escolhas preselecionadas enganosas ou interfaces que dificultem recusar, corrigir ou sair. Use movimento apenas para comunicar estado ou relação; respeite preferências de movimento reduzido e mantenha o conteúdo legível.

## Sistemas de design e interfaces geradas

Use componentes reutilizáveis, tokens semânticos e estados de interação documentados para manter consistência entre superfícies. Componentes que o sistema possa compor ou gerar devem ter limites de conteúdo, acessibilidade e ações permitidas revistos. Valide foco, semântica, teclado, contraste, responsividade e estados de erro nos componentes efetivamente usados; a geração automática ou um protótipo visual não prova conformidade nem prontidão para produção.

Se a interface mudar conforme o contexto, preserve orientação, localização, seleção e uma rota para a tarefa principal. Dê à pessoa uma forma de rever ou desfazer mudanças que afetem o seu trabalho. Trate tokens, exemplos e documentação estruturada como restrições de apresentação; a interface não deve conceder permissões ou autorizar ações por si só.

## Avaliar a experiência com IA

Avalie tarefas representativas com diferentes entradas, resultados e modos de falha. Como a mesma entrada pode produzir respostas diferentes, examine execuções repetidas quando essa variação puder alterar a compreensão ou a decisão; não use um único exemplo como prova de consistência. Separe a qualidade do modelo e das ferramentas da qualidade da interação e do resultado para a pessoa.

Observe se as pessoas entendem o que o sistema pode fazer, reconhecem incerteza relevante, verificam evidência quando necessário e conseguem corrigir, cancelar, escalar ou reverter. Considere conclusão e qualidade da tarefa, tempo e esforço, erros, correções, abandono, uso de fallback e confiança apropriada. Escolha medidas conforme o risco e o objetivo; satisfação isolada, taxa de aceitação ou confiança declarada não demonstram uso correto. Teste com as tecnologias de apoio e os grupos relevantes ao público, e reporte diferenças importantes em vez de as esconder numa média agregada.

Para desenho de evals, métricas e decisões de rollout, consulte [avaliação e medição](evaluation-and-measurement.md). Para acessibilidade e controlos no lançamento, consulte [risco, governação e lançamento](risk-governance-and-launch.md).

## Economia e qualidade juntas

Considere qualidade, custo, latência, fiabilidade e segurança como restrições relacionadas. Uma escolha mais barata por chamada pode produzir mais retries, revisões ou tarefas falhadas. Avalie o sistema completo e a unidade de valor, não apenas o preço nominal de um modelo. Para custos por tarefa e decisões comerciais, leia [modelos de negócio e pricing](business-models-and-pricing.md); para cache e routing detalhado, consulte uma competência de eficiência se disponível.

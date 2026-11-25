# Construção e validação

## Propósito

Use esta referência para transformar material disperso em uma estrutura que reduz uma decisão recorrente sem fingir completude ou certeza.

## Quantidade de elementos não é a alavanca certa

Não existe cardinalidade cientificamente ótima de pilares, etapas ou domínios. "3 a 5 elementos" é apenas uma heurística útil para ensinar algo pela primeira vez a um público sem contexto prévio — não é um limite universal de processamento mental, e um framework com nove ou doze componentes pode ser tão fácil de reter quanto um com quatro.

O que realmente reduz o esforço de quem usa a estrutura é a **qualidade do agrupamento**, não o número bruto de itens:

- itens organizados em famílias com significado prévio;
- rótulos que já carregam parte da função;
- representação externa (visual ou tabela) em vez de lista mental;
- relação lógica simples entre os grupos;
- hierarquia ou sequência recuperável.

Doze itens soltos, sem ordem nem grupo, pesam mais na cabeça do que doze itens organizados em três famílias de quatro. Ao simplificar, pergunte primeiro **"posso aumentar a compressão sem apagar informação?"** — agrupando, hierarquizando, rotulando — e só depois **"o que deve de fato ser descartado?"**. Compressão por agrupamento é diferente de compressão por descarte, e a primeira deveria vir antes da segunda.

Um framework também não precisa ser rico em componentes para ser útil: uma relação forte entre dois tipos complementares (por exemplo, uma intenção e a evidência que comprova seu progresso) pode comprimir mais decisão do que uma lista longa de itens fracamente relacionados. Antes de adicionar componentes, verifique se a relação entre os poucos que já existem está subaproveitada.

## Da evidência à arquitetura

1. **Capture antes de categorizar.** Reúna observações, casos, decisões, técnicas, resultados, exceções e fontes disponíveis.
2. **Atomize.** Separe cada insumo em uma afirmação observável, decisão ou comportamento. Uma frase que contém causas, sintomas e consequências deve virar unidades separadas.
3. **Agrupe indutivamente.** Pergunte quais unidades descrevem o mesmo fenômeno antes de perguntar em qual categoria pré-existente elas cabem.
4. **Rotule provisoriamente.** Use nomes funcionais; não tente criar marca enquanto os limites dos grupos ainda mudam.
5. **Confronte as fronteiras.** Procure duplicação, relação de contenção, causa versus sintoma, diferença de nível, elementos órfãos e contraexemplos.
6. **Encontre a relação dominante.** Determine se os grupos são fases, dimensões simultâneas, condições, estados, dependências, escolhas, graus ou ciclos reais.
7. **Comprima em camadas.** Preserve uma primeira camada recuperável e desloque explicações, exceções, heurísticas e evidências para níveis posteriores.

## Gramática de relações

Antes de nomear ou desenhar, nomeie a relação dominante em uma frase. Se isso não for possível, ainda é cedo para comprimir.

| Relação | Pergunta central | Estruturas candidatas |
|---|---|---|
| Sequência | O que vem antes ou depois? | Etapas, roadmap, pipeline |
| Hierarquia | O que contém ou sustenta o quê? | Pirâmide, árvore, stack |
| Classificação | Que tipo de situação é esta? | Domínios, árvore, quadrantes |
| Trade-off | Onde estou entre dimensões concorrentes? | Matriz, espectro |
| Interseção | O que ocorre quando condições coexistem? | Venn |
| Progressão | Qual é o nível atual e o próximo? | Escada, modelo de maturidade |
| Feedback | Como o resultado volta a alimentar o início? | Ciclo, flywheel |
| Decomposição | Quais partes compõem o todo, vistas ao mesmo tempo? | Canvas, mapa |
| Causalidade | O que influencia o quê? | Diagrama causal |
| Decisão | Se a situação é X, qual ação decorre? | Árvore, matriz, domínios |

Uma mesma coleção de insumos pode admitir mais de uma relação plausível; escolha a que melhor reduz o espaço de decisão do usuário, não a que produz o desenho mais familiar.

## Sequência aparente não é sequência obrigatória

Ao descrever fases, etapas ou modos, distinga três coisas diferentes:

- **ordem didática** — a ordem mais fácil de ensinar a quem nunca viu o material;
- **ordem típica** — a ordem mais observada na prática, com desvios frequentes;
- **ordem obrigatória** — a ordem que, se invertida, quebra o resultado.

Apresentar uma ordem didática como se fosse obrigatória cria uma falsa sequencialidade: o usuário passa a acreditar que não pode começar pela etapa três, quando na prática pode. Se a ordem for apenas didática ou típica, diga isso explicitamente em vez de deixar a numeração sugerir rigidez que não existe.

## Arquitetura de famílias para muitos componentes

Quando um domínio tem muitos componentes concretos que resistem à fusão, não force tudo em uma lista única nem descarte itens só para caber em uma contagem menor. Agrupe por **tipo lógico** — por exemplo, papéis/atores, eventos/rituais, artefatos/objetos e princípios/regras — e trate cada família como um chunk de primeiro nível. Isso reduz o número de tipos mentais que o usuário precisa manipular mesmo quando o número total de itens concretos continua alto.

## Auditoria de arquitetura

| Verificação | Pergunta de diagnóstico | Ação se falhar |
|---|---|---|
| Sobreposição | Dois componentes orientam a mesma decisão? | Fundir, delimitar ou declarar a interseção. |
| Cobertura | Há caso relevante que não cabe em lugar algum? | Adicionar, revisar fronteira ou assumir exclusão explícita. |
| Nível | Componentes estão na mesma camada de abstração? | Separar camadas ou reescrever a relação. |
| Síntese | Uma ideia governante explica por que as partes coexistem? | Revisar agrupamentos ou abandonar a estrutura. |
| Discriminação | O framework muda a resposta entre casos diferentes? | Transformar a lista em critério, classificação ou processo útil. |

MECE é uma lente de depuração para exclusividade e cobertura; não é obrigação quando as relações reais se sobrepõem. Uma pirâmide exige uma ideia superior que sintetize ou organize as partes; não é decoração para itens equivalentes.

## Escolha do tipo de estrutura

- **Taxonomia:** distinguir tipos ou categorias.
- **Checklist:** lembrar itens que precisam ser verificados.
- **Processo:** orientar ações em sequência, incluindo retornos apenas quando forem reais.
- **Matriz:** relacionar dois eixos para classificar estados ou escolhas.
- **Modelo:** representar relações explicativas ou operacionais.
- **Framework:** comprimir uma relação recorrente para melhorar decisão e ação.

Não eleve automaticamente uma checklist ou taxonomia a framework. Declare qual problema a estrutura resolve e o que não resolve.

## Testes de validação

| Teste | Pergunta | Evidência de falha |
|---|---|---|
| Compreensão | A pessoa explica a finalidade e a relação sem repetir o texto? | Confunde componentes ou não identifica o problema tratado. |
| Reconstrução | Após remover o material, a pessoa recupera estrutura e ordem relevantes? | Lembra termos isolados, mas não a ligação entre eles. |
| Transferência | Aplica a estrutura a um caso novo? | Repete o exemplo original sem adaptar critérios. |
| Fronteira | Reconhece um caso para o qual a estrutura não serve? | Usa o framework para qualquer problema. |
| Ação | A classificação ou etapa leva a uma decisão observável? | Produz descrição sem consequência prática. |

Registre o público, cenário, exemplo, resultado, dúvida e revisão decidida. Testes locais indicam utilidade naquele contexto; não provam validade universal.

## Heurísticas de validação

Trate como protocolo de trabalho a calibrar no contexto, não como lei científica com limiar fixo:

- **Ensinabilidade:** a ideia central, os componentes e a relação são explicáveis em poucos minutos.
- **Reconstrução:** a camada superior é recuperável depois de remover o material.
- **Aplicação correta:** a estrutura é usada corretamente diante de um caso novo.
- **Reconhecimento de fronteira:** casos fora de escopo são identificados como tal, não forçados a caber.
- **Acionabilidade:** aplicar a estrutura muda uma escolha, diagnóstico ou ação observável.
- **Compressão real:** a versão resumida é substancialmente menor que o conhecimento original sem perder a relação que importa para a decisão.

## Checklist final antes de entregar

- A decisão, o usuário, o contexto de uso e a fronteira estão explícitos?
- Os componentes vieram de evidência ou padrão observado, não de uma categoria imposta cedo demais?
- Existe uma relação dominante nomeável em uma frase?
- Sobreposições, lacunas e diferenças de nível foram auditadas, e sobreposições reais foram declaradas em vez de escondidas?
- Existe uma ideia governante que explica por que os componentes coexistem?
- A primeira camada é recuperável, com exceções e evidências deslocadas para camadas posteriores?
- Nenhum componente existe apenas por simetria, contagem redonda ou encaixe em acrônimo?
- O framework foi testado quanto a compreensão, reconstrução, transferência, fronteira e ação?

Uma resposta "não" indica que o artefato ainda está em fase de protótipo, não pronto para uso.

## Antipadrões

- **Acrônimo primeiro:** alterar a estrutura para obter letras desejadas.
- **Formato primeiro:** começar por uma matriz, ciclo ou pirâmide e deformar os fatos.
- **Lista disfarçada:** nomear itens sem relação, fronteira ou consequência.
- **Simetria artificial:** manter componentes apenas para preencher uma contagem.
- **Compressão por descarte:** remover exceções que alteram a decisão.
- **"N é o número certo":** justificar a quantidade de componentes por uma suposta constante psicológica em vez de testar carga, agrupamento e recuperação reais.
- **Falsa sequencialidade:** apresentar itens simultâneos ou de ordem flexível em linha reta, sugerindo uma obrigatoriedade que não existe.
- **Ciclo ou flywheel decorativo:** desenhar uma sequência linear em círculo sem que a última etapa realmente alimente a primeira.
- **MECE cosmético:** categorias com aparência organizada que na verdade misturam níveis de abstração ou causa com sintoma.

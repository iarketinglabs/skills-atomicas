# Design visual de frameworks

## Princípio de correspondência

A geometria é uma afirmação sobre a lógica. Escolha a forma depois de identificar a relação dominante e faça posição, tamanho, cor, forma, agrupamento e direção comunicarem apenas diferenças que realmente existam.

| Relação dominante | Representação a testar | Não use se |
|---|---|---|
| Dois eixos produzem estados | Matriz | Os eixos não são distintos, graduais ou acionáveis. |
| Ideias subordinadas sustentam síntese | Pirâmide ou árvore | Os itens são pares equivalentes. |
| Muitos itens são filtrados em poucos | Funil | Não há redução real ao longo do caminho. |
| Saída retroalimenta entrada | Ciclo | A última etapa não altera ou alimenta a primeira. |
| Conjuntos compartilham elementos | Venn | As categorias precisam ser exclusivas. |
| Há grau ou progressão ordenada | Continuum | Os níveis são apenas tipos diferentes. |
| Camadas dependem umas das outras | Stack | Os componentes coexistem sem dependência vertical. |
| Há transição entre etapas | Jornada ou roadmap | A ordem é irrelevante para a decisão. |
| Dimensões coexistem em uma visão | Canvas ou radial | A disposição circular sugere ciclo inexistente. |
| Um fator influencia outro | Diagrama causal | A relação é apenas correlação ou coincidência temporal. |
| A classificação decide a ação seguinte | Árvore, matriz ou domínios rotulados com a ação | Classificar não muda nenhuma decisão a jusante. |

## A regra semântica do espaço

Cada propriedade visual deve carregar um significado único e consistente ao longo de toda a peça — nunca "porque ficou bonito assim".

| Propriedade | O que pode comunicar |
|---|---|
| Posição | Antes/depois, alto/baixo, centro/periferia, proximidade |
| Tamanho | Importância, quantidade, abrangência, nível hierárquico |
| Cor | Categoria, estado, risco, caminho, destaque |
| Forma | Tipo de objeto, função, natureza da etapa |
| Enclosure (contorno/moldura) | Pertencimento, agrupamento, fronteira |
| Seta | Direção ou dependência |
| Círculo/loop | Recorrência |

Se duas propriedades diferentes comunicam a mesma coisa, isso é redundância útil desde que reforcem o mesmo sinal; se comunicam sinais contraditórios (por exemplo, cor sugerindo uma categoria e posição sugerindo outra), a peça está semanticamente quebrada mesmo que pareça esteticamente coerente.

## Especificação antes da produção

Descreva em texto:

1. título e pergunta que o visual responde;
2. unidade, componente ou estado que cada forma representa;
3. relação comunicada por posição, direção, grupo e escala;
4. ponto de entrada e ação associada a cada etapa ou classificação;
5. canal de uso e restrições de leitura;
6. versão de referência e, se necessário, versão resumida para atenção inicial.

Minimalismo é retirar ruído, não retirar sinais que tornam a relação interpretável. Ilustrações, cor e pictogramas devem agrupar, orientar, contextualizar ou apoiar recordação; caso contrário, são decoração.

## Rótulos que carregam função

Um diagrama cheio de substantivos soltos exige mais inferência do leitor do que um diagrama cujas conexões nomeiam a ação. Compare "Dados → Insights → Estratégia → Execução" com "coletar dados → interpretar sinais → escolher direção → executar ações": o segundo expõe a função de cada seta em vez de deixar o leitor adivinhá-la. Nem todo framework precisa de verbos nos rótulos, mas qualquer relação ambígua se beneficia de nomear o que a seta faz, não só o que ela liga.

## Minimalismo e riqueza visual não são opostos

"Poucos elementos" e "relação clara" são duas variáveis diferentes, não sinônimos. Um visual pode ser minimalista e ambíguo (poucos sinais, mas relação indecifrável), denso e ambíguo (muitos elementos sem função), minimalista e claro, ou rico e claro — desde que cada elemento adicional cumpra uma função: codificar significado, direcionar atenção, ajudar a agrupar, criar um gancho de memória ou reforçar a metáfora central. Para cada elemento pergunte se ele faz um desses trabalhos; se a resposta for não para todos, corte.

Do mesmo modo, não desenhe a peça para se adequar a um padrão de leitura em "F" observado em páginas de texto pouco estruturado — isso é um sintoma de falta de sinalização, não um layout a seguir. O objetivo é criar um percurso visual intencional (ponto de entrada, direção, chegada), mais forte que qualquer comportamento default de escaneamento.

## Duas versões para propósitos diferentes

Frameworks com mais de um contexto de uso costumam precisar de duas representações oficiais em vez de uma peça só tentando servir a ambos:

- **Versão principal (hero):** para memorização, primeira explicação, abertura de apresentação ou publicação social. Contém nome, relação e componentes principais, com o mínimo de texto.
- **Versão de referência:** para aplicação, consulta e treinamento. Contém definições, critérios, exceções, exemplos e outputs esperados.

Ajuste prioridades ao canal: um documento técnico ou dashboard prioriza precisão, comparabilidade e labels explícitos; uma apresentação prioriza revelação progressiva e um foco por tela; um formato social prioriza um ponto de entrada forte e a ideia central legível em poucos segundos — mas a relação verdadeira deve se manter em todos os contextos. Um diagrama logicamente errado continua errado independentemente de quanto engajamento ou atenção recebe.

## Testes do visual

| Teste | Pergunta |
|---|---|
| Gist | Em poucos segundos, a pessoa identifica problema e relação principal? |
| Relação | Ela interpreta corretamente ordem, dependência, interseção ou grau? |
| Reconstrução | Ela redesenha ou reconta a estrutura preservando o significado? |
| Blur | Desfocada a imagem, a hierarquia (o que é primário/secundário) ainda aparece? |
| Grayscale | Hierarquia e contraste permanecem visíveis sem depender apenas de cor? |
| Caso-limite | Ela reconhece quando a estrutura ou classificação não se aplica, diante de um caso incompatível apresentado de propósito? |
| Ação | Ela consegue decidir o próximo passo usando o visual? |

Engajamento, atenção ou apreciação não substituem compreensão, aplicação ou precisão da relação — inclusive métricas fortes de alcance ou cliques em formato social medem principalmente distribuição, não aprendizagem.

## Antipadrões

- Matriz escolhida por familiaridade sem dois eixos úteis.
- Funil que apenas reorganiza etapas sem filtragem.
- Ciclo ou flywheel sem retroalimentação.
- Pirâmide usada para itens sem hierarquia.
- Diagrama com setas, cores ou tamanhos sem legenda ou significado consistente.
- Peça desenhada para "parar o scroll" com elementos decorativos que competem com a relação em vez de reforçá-la.
- Uma única peça tentando ser ao mesmo tempo pôster de memorização e manual de aplicação, e falhando nas duas funções.
- Versão de comunicação que perde a lógica necessária para orientar ação.

---
name: arquitetura-de-frameworks
description: Use quando for necessário criar, revisar, nomear, explicar ou representar visualmente um framework, método, matriz, taxonomia, processo, modelo de maturidade ou conjunto de pilares, especialmente se a lógica, os limites ou a utilidade prática ainda estiverem incertos.
---

# Arquitetura de Frameworks

Um framework é uma interface entre complexidade e decisão. Siga a cadeia **evidência → padrões → relação → arquitetura → compressão → naming → visual → teste**: construa uma relação útil e verificável antes de condensá-la em pilares, nomes ou diagramas.

Um framework maduro executa quatro compressões em sequência, nunca na ordem inversa: **estrutural** (muitos fatos viram poucos padrões significativos), **lógica** (os padrões formam uma relação previsível), **verbal** (a relação recebe nomes recuperáveis) e **visual** (a geometria torna a relação observável). Simplicidade percebida no resultado final é consequência desse trabalho, não de remoção arbitrária de elementos ou de um nome ou desenho bonito escolhido antes da lógica.

## Quando usar

- Transformar evidências, entrevistas, casos, práticas ou observações dispersas em uma estrutura de decisão.
- Revisar um framework que parece uma lista, possui categorias sobrepostas, omite casos relevantes ou não indica uma ação.
- Avaliar um nome, acrônimo, matriz, ciclo, pirâmide ou diagrama antes de adotá-lo.
- Explicar uma metodologia para ensino, decisão, comunicação ou documentação.

Não use para apenas resumir material, produzir uma peça visual sem definir sua lógica, nem substituir pesquisa, teste com pessoas, validação jurídica ou decisão especializada.

## Comece pelo problema

Extraia o que já foi fornecido e pergunte apenas o que muda a arquitetura:

- qual decisão ou pergunta recorrente o framework deve simplificar;
- quem o usará, em qual situação e com qual ação ou saída esperada;
- quais evidências, exemplos, exceções e restrições já existem;
- quais termos, nomes, forma visual, idioma ou canal já foram escolhidos;
- o que está explicitamente fora da fronteira do framework.

Não invente evidências, consenso, maturidade, prioridade ou resultado. Diferencie fato, observação, hipótese, decisão e informação pendente.

## Selecione as camadas necessárias

1. Para estruturar insumos, definir limites, comprimir e testar a utilidade, leia [construção e validação](references/construcao-e-validacao.md).
2. Para criar ou revisar nomes, rótulos e acrônimos, leia [naming](references/naming.md) depois que a arquitetura estiver estável.
3. Para escolher ou revisar um diagrama, leia [design visual](references/design-visual.md) depois de identificar a relação dominante.

Use somente as referências que a tarefa exige. Uma solicitação de naming não autoriza reinventar uma estrutura validada; uma solicitação de visual não autoriza alterar a lógica apenas para caber em um formato.

## Método de trabalho

1. Defina decisão, usuário, contexto de uso, saída e fronteira.
2. Reúna e atomize os insumos; agrupe padrões antes de impor categorias.
3. Descubra a relação dominante e audite sobreposição, lacunas, níveis de abstração e contraexemplos.
4. Comprima a primeira camada sem apagar exceções que mudem decisões; mantenha explicações e evidências em camadas posteriores.
5. Só então trate naming e representação visual como expressões da arquitetura.
6. Valide compreensão, reconstrução, transferência, reconhecimento de fronteiras e ação; revise o que os testes revelarem.

Não existe número universal de componentes, formato visual universal ou tipo de nome universalmente superior. Use heurísticas como critérios a testar no contexto de uso.

## Contrato de saída

Entregue apenas as partes úteis ao pedido, nesta ordem quando aplicável:

1. **Decisão e fronteira** — problema, usuário, contexto, saída e exclusões.
2. **Base de raciocínio** — fatos, hipóteses, lacunas, exceções e padrões observados.
3. **Arquitetura proposta** — componentes, relação dominante, ideia governante e justificativa para agrupamentos.
4. **Uso prático** — como classificar um caso, escolher uma ação ou avançar entre estados.
5. **Naming e visual** — alternativas ou especificação que preservem a relação, quando solicitados.
6. **Validação e iteração** — testes, sinais de falha, casos-limite e decisões pendentes.

Use tabelas somente se elas tornarem comparações, alternativas, critérios ou testes mais claros.

## Guardrails

- Não crie categorias para encaixar em um acrônimo, número de pilares, matriz ou diagrama escolhido antecipadamente.
- Não apresente uma lista como processo, uma sequência como ciclo, uma classificação como maturidade, ou uma preferência estética como evidência.
- Não force exclusividade quando interseção for parte real do fenômeno; também não esconda sobreposição acidental.
- Não trate lembrança, atenção ou aceitação visual como prova de aplicação correta.
- Não associe recomendações a empresa, setor, fornecedor, idioma, tecnologia, país, prazo ou métrica sem dados fornecidos.

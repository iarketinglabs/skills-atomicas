# Maturidade, Governança e Realização de Valor

Use esta referência para calibrar a expectativa de retorno ao estágio real da iniciativa, tratar riscos operacionais que corroem o retorno de IA, e montar um business case completo. Ela não substitui o cálculo financeiro de [fundamentos financeiros](financial-fundamentals.md) nem a governança de risco e segurança tratada por outras skills de governança de IA.

## Por que retorno negativo inicial nem sempre é fracasso

Investimento em tecnologia costuma seguir uma curva em J: o resultado líquido cai antes de subir, porque o custo de implementação, capacitação e ajuste organizacional precede o ganho de produtividade. Encerrar uma iniciativa apenas porque ela ainda está na fase de investimento líquido, sem verificar em que ponto da curva ela está e o que falta para o ponto de equilíbrio, é uma forma comum de descartar valor prematuramente. Ao mesmo tempo, uma iniciativa que nunca sai do território negativo, sem sinal de aproximação do equilíbrio, é evidência real de que algo estrutural precisa mudar — não uma razão para esperar indefinidamente. Distinga as duas situações com evidência, não com prazo arbitrário.

## Estágios de maturidade da mensuração

Use estes estágios como referência de progressão, não como cronograma obrigatório — a duração real de cada estágio varia por organização, escopo e complexidade de dados.

| Estágio | Objetivo central | Critério típico para avançar |
| --- | --- | --- |
| 1. Linha de base | Estabelecer o custo e o indicador "como está hoje" (tempo, custo, qualidade) antes de qualquer automação | Linha de base documentada e dados minimamente prontos para IA; se os dados não estiverem prontos, tratar isso como bloqueio a resolver antes de comprometer orçamento maior |
| 2. Prova | Testar o ganho em nível de tarefa, idealmente com comparação entre grupo que usa IA e grupo que não usa | Ganho de tempo ou qualidade demonstrado de forma comparável, não apenas percebido |
| 3. Redesenho e escala | Elevar de piloto isolado para processo estruturado, removendo gargalos humanos desnecessários no fluxo | Processo redesenhado em produção, com custo operacional contínuo (incluindo consumo de API/inferência) sob monitoramento |
| 4. Realização de valor | Converter o ganho latente em resultado auditável de negócio | Pelo menos um dos testes de captura de valor abaixo formalizado e refletido em números reais, não apenas projetados |

**Testes de captura de valor** para o estágio de realização — cada um responde a uma pergunta diferente sobre onde o valor efetivamente apareceu:

- **Custo evitado**: a organização absorveu crescimento de volume sem contratar proporcionalmente, ou reduziu quadro de forma deliberada e mensurável.
- **Aceleração de receita**: o ciclo de venda ou conversão encurtou de forma atribuível, com triangulação de evidência.
- **Substituição de custo de licença ou fornecedor**: um contrato de ferramenta, agência ou terceiro foi reduzido ou eliminado por capacidade construída internamente.

## O problema da hora liberada não monetizada

Ganho de produtividade individual (tempo poupado por pessoa) não vira ROI automaticamente. Se a capacidade liberada não for redirecionada de forma deliberada, o ganho desaparece na prática sem gerar valor de negócio. Ao mensurar produtividade, verifique explicitamente qual das duas rotas foi tomada:

- **Rota defensiva**: a capacidade liberada absorveu crescimento de demanda sem aumento proporcional de equipe — economiza contratação futura, mas não reduz custo atual.
- **Rota ofensiva**: a capacidade liberada foi redirecionada para trabalho de maior valor (inovação, expansão comercial, qualidade) — gera ganho incremental, mas exige decisão de gestão explícita para acontecer.

Se nenhuma das duas rotas foi formalmente decidida, trate o tempo poupado como indicador de produtividade potencial, não como ROI realizado.

## Riscos operacionais que corroem o retorno

Ao montar o TCO e o plano de monitoramento, verifique estes riscos específicos de iniciativas de IA baseadas em consumo:

- **Consumo descontrolado por falha em cadeia**: agentes autônomos que tentam repetidamente uma chamada que falha podem consumir orçamento de API muito além do previsto sem intervenção manual; defina limites de gasto e circuit breakers antes de escalar autonomia.
- **Roteamento de modelo ineficiente**: usar o modelo mais caro disponível para toda tarefa, em vez de rotear tarefas simples para modelos mais baratos, pode inflar o custo operacional de forma desproporcional ao ganho adicional de qualidade.
- **Dispersão de ferramentas**: acumular múltiplas ferramentas de IA com sobreposição de função, sem consolidação, gera custo de licença e carga cognitiva que corroem o ganho líquido — verifique utilização real, não apenas contratação.

## Portfólio e decisão por portão

Avalie cada iniciativa como parte de um portfólio, não apenas pelo entusiasmo ou pelo custo já incorrido. Priorize a próxima decisão com base em valor potencial, qualidade da evidência, reversibilidade, custo de aprendizagem, prontidão de dados e capacidade de capturar o benefício.

Defina o portão antes da revisão e associe-o a uma decisão concreta:

| Decisão | Evidência mínima esperada |
| --- | --- |
| Escalar | Ganho comparável ou causalmente sustentado, custo operacional previsível, capacidade de captura formalizada e risco controlado |
| Ajustar | Sinal operacional promissor, mas custo, adoção, qualidade ou atribuição insuficientes para escalar |
| Pausar | Premissa crítica sem evidência ou bloqueio que impede medição confiável |
| Encerrar | Evidência suficiente de que benefício não compensa custo, risco ou alternativa disponível |

Uma curva em J explica investimento inicial, mas não substitui esses portões. Registre a data da revisão, evidência considerada, responsável e a próxima condição de mudança de decisão.

## Checklist de business case

Ao construir um business case ex-ante, confirme que ele cobre:

1. Descrição do projeto e objetivo de negócio que ele deve habilitar.
2. Lista detalhada de custos (implementação e operação contínua).
3. Estimativa de benefícios tangíveis, com método de cálculo declarado.
4. Métricas intangíveis projetadas e como (ou se) serão convertidas em valor.
5. Cálculo financeiro (NPV/IRR ou ROI simples, conforme o horizonte), com premissas explícitas.
6. Análise de cenário (otimista, neutro, pessimista) para as premissas mais sensíveis.
7. Indicadores de adoção e uso previstos, distintos dos indicadores de valor realizado.
8. Responsáveis e patrocinadores, com plano de governança proporcional ao risco.
9. Plano de monitoramento do retorno real após a implementação — quem mede o quê, e com que cadência.

## Evidência externa

Estatísticas de adoção, taxa de sucesso ou abandono de iniciativas de IA citadas em pesquisas de mercado mudam rapidamente e variam por metodologia, população e definição de "sucesso" usada no estudo original. Cite-as sempre com fonte, data e escopo, e trate-as como contexto de mercado a verificar, nunca como taxa esperada para a iniciativa em avaliação — conforme os guardrails da skill.

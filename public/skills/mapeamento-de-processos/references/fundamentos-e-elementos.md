# Fundamentos Atemporais do Mapeamento e Criação de Processos

Base conceitual que precede qualquer mapeamento, criação ou redesenho de processo, independente de setor ou cliente. Sintetizado da literatura seminal de BPM (Davenport, Hammer & Champy, ABPMP CBOK) e de guias de referência (APQC, ASQ, Lean Enterprise Institute).

## 1. Definição de processo

Um processo de negócio é um conjunto estruturado e mensurável de atividades, logicamente conectadas, com início e fim definidos, que consome insumos (inputs) e produz um resultado (output) de valor específico para um cliente interno ou externo. Envolve pessoas, tecnologia e regras, e sua eficácia se mede pelo resultado entregue — não pelo esforço interno gasto.

## 2. Processo vs. função vs. procedimento

Erro de diagnóstico frequente: tratar os três como sinônimos.

- **Função**: agrupamento vertical de competências de um departamento (ex.: "Financeiro", "Comercial"). Descreve *quem* é responsável por um domínio, não *como* o trabalho flui.
- **Processo**: conjunto de atividades relacionadas que entrega um resultado. Pode atravessar várias funções. Ex.: contratar um colaborador atravessa RH, Financeiro (orçamento), TI (provisionamento de acesso) e a área solicitante.
- **Procedimento**: instrução de trabalho que detalha passo a passo *como* uma tarefa específica dentro do processo deve ser executada tecnicamente (ex.: como configurar um acesso, como preencher um formulário).

Ao mapear, pergunte qual resultado é entregue, a quem e que sequência o produz. Um processo ou subprocesso pode acontecer dentro de uma área. Um procedimento descreve como executar uma parte do trabalho, mesmo quando envolve várias funções. Use os limites e a finalidade da análise para escolher a granularidade.

## 3. Taxonomia de processos (nível macro)

Ao construir um mapa de processos de uma organização inteira, classifique cada processo em uma das três categorias:

1. **Processos primários (core)**: formam a cadeia de valor essencial — concebem, produzem e entregam o que o cliente externo paga para receber. Afetam receita e vantagem competitiva diretamente.
2. **Processos de suporte**: viabilizam os processos primários (RH, TI, financeiro, jurídico). Não geram valor visível direto ao cliente externo, mas sustentam escala e estabilidade.
3. **Processos de gestão**: governam a operação no nível diretivo — definição de metas, monitoramento de performance, compliance e gestão de risco.

Um processo de suporte mal mapeado como se fosse primário (ou vice-versa) distorce a priorização de onde investir esforço de melhoria.

## 4. Elementos estruturais de qualquer processo

Todo levantamento AS-IS precisa capturar estes elementos — a ausência de qualquer um deixa o mapeamento incompleto:

| Elemento | O que documentar |
|---|---|
| **Inputs** | Gatilho que inicia o processo (evento, solicitação, dado) e insumos consumidos. |
| **Atividades/tarefas** | Sequência lógica de eventos e decisões, incluindo caminhos alternativos. |
| **Outputs** | Resultado tangível ou intangível entregue, e o critério que define "processo concluído". |
| **Atores** | Pessoas, papéis e sistemas envolvidos em cada etapa. |
| **Handoffs** | Todo ponto em que a responsabilidade passa de um ator/sistema para outro. É a maior fonte de atraso, perda de contexto e erro em qualquer processo — priorize identificá-los com precisão. |
| **Regras de negócio** | Lógicas de decisão que fazem o fluxo se bifurcar (ex.: "se valor > X, exige segunda aprovação"). Pré-requisito para qualquer automação madura. |
| **Momentos da verdade** | Pontos de interação direta com o cliente externo, onde se forma a percepção de qualidade do serviço/marca. |
| **Controles/regulamentações** | Restrições de compliance, auditoria ou política interna que o processo precisa respeitar. |

## 5. Valor agregado vs. não agregado

Toda atividade mapeada se submete ao teste: "o cliente pagaria conscientemente por esta etapa especificamente?" Atividades que falham nesse teste — aprovações redundantes, retrabalho, movimentação/transporte desnecessário, espera, controles de qualidade corretivos tardios — são candidatas primárias à eliminação na fase de redesenho, não à automação. Automatizar uma etapa que não deveria existir apenas acelera o desperdício.

## 6. Ciclo de vida de gestão de processos (BPM lifecycle)

Processos não são mapeados uma vez e esquecidos; seguem um ciclo contínuo:

1. **Planejamento/alinhamento estratégico** — conectar o processo aos objetivos de negócio antes de mapear qualquer coisa.
2. **Mapeamento e desenho** — levantar o AS-IS e conceber o TO-BE.
3. **Modelagem e simulação** — prototipar e testar cenários antes de implementar mudanças.
4. **Implementação** — colocar o processo redesenhado em prática (sistemas, treinamento).
5. **Monitoramento** — acompanhar indicadores em tempo real.
6. **Otimização contínua** — iterar com base em dados (Kaizen/PDCA).

## 7. Métricas de desempenho

Nunca dependa de um único indicador. Combine, no mínimo:

- **Eficiência**: produção real vs. produção esperada/planejada.
- **Produtividade**: output por unidade de insumo (ex.: operações por colaborador).
- **Utilização**: percentual de capacidade disponível efetivamente usada.
- **Lead time**: tempo total desde o input inicial até o output final, incluindo todas as esperas.
- **Cycle time**: tempo ativo real gasto processando uma unidade de trabalho (exclui espera).
- **Taxa de retrabalho/qualidade**: percentual de tarefas com erro ou que exigem repetição.

Toda métrica citada num mapeamento deve declarar unidade, período de referência e fonte — um número sem essas três informações não é uma métrica utilizável, é uma estimativa não rastreável.

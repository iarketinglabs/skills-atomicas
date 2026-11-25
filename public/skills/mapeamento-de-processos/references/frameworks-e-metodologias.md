# Frameworks e Metodologias de Referência Mundial

Instrumental analítico para modelar, classificar e redesenhar processos. Nenhum destes frameworks é universalmente superior — a escolha depende do tipo de processo e do objetivo do diagnóstico. Use a tabela comparativa (seção 8) para decidir rapidamente, e a seção correspondente para aplicar corretamente.

## 1. BPMN (Business Process Model and Notation)

Padrão gráfico mundial (mantido pela OMG) para modelar processos com elementos visuais padronizados (eventos, atividades, gateways, raias/swimlanes). Produz diagramas compreensíveis tanto por quem executa o processo quanto por quem vai automatizá-lo.

- **Use quando**: precisa de um diagrama formal, comunicável entre áreas de negócio e TI, especialmente se o processo vai ser automatizado ou auditado.
- **Limitação**: custoso de manter em processos muito dinâmicos ou informais; pode virar burocracia se aplicado a fluxos que ainda estão sendo descobertos.

## 2. ABPMP BPM CBOK (Common Body of Knowledge)

Não é uma metodologia de otimização — é o corpo de conhecimento e vocabulário comum de BPM. Estrutura a disciplina em um ciclo de 5 fases apoiado em áreas de conhecimento (modelagem, análise, desenho, medição de performance, transformação tecnológica, gestão de processos corporativos).

- **Use quando**: precisa estabelecer uma linguagem e um processo de governança de BPM consistentes numa organização, especialmente em diagnósticos de maturidade ou pós-fusão.
- **Limitação**: é um guia de boas práticas, não uma ferramenta prática de otimização de um processo específico.

## 3. APQC Process Classification Framework (PCF)

Taxonomia hierárquica (5 níveis: Categoria → Grupo de Processos → Processo → Atividade → Tarefa) para classificar qualquer processo de negócio de forma agnóstica a setor, permitindo benchmarking comparativo.

- **Use quando**: precisa organizar um inventário de processos de uma organização inteira sem redundância, ou comparar desempenho contra benchmarks externos.
- **Limitação**: é genérico por natureza — não descreve fluxo cronológico nem gera diagrama; precisa de adaptação à realidade específica do negócio.

## 4. Lean / Value Stream Mapping (VSM)

Filosofia originada no Sistema Toyota, focada em eliminar desperdício (*Muda*) que não agrega valor sob a perspectiva do cliente. O VSM é a ferramenta central: um fluxograma que documenta, num único mapa, o fluxo físico/de informação de cada etapa e o fluxo de sinais que comanda essa etapa.

Métricas centrais do VSM:

| Métrica | Definição | Uso no diagnóstico |
|---|---|---|
| **Lead time** | Tempo total do pedido do cliente até a entrega, incluindo esperas. | Métrica de agilidade — o redesenho visa comprimi-la. |
| **Cycle time** | Tempo ativo de processamento de uma unidade em um posto de trabalho. | Revela ineficiência na execução de uma etapa específica. |
| **Takt time** | Ritmo teórico necessário para atender à demanda do mercado. | Processos mais lentos que o takt causam atraso de entrega; mais rápidos causam superprodução/estoque parado. |
| **Setup/changeover time** | Tempo para preparar recursos antes de iniciar uma nova etapa. | Setups longos forçam lotes grandes, o que prejudica a fluidez. |
| **Value-added ratio** | Tempo produtivo ÷ lead time total. | Expõe densidade do desperdício; abaixo de 5% é comum e indica que quase todo o tempo é espera/transporte. |

- **Use quando**: o processo é estável, repetitivo, e o objetivo principal é comprimir tempo e eliminar espera/retrabalho.
- **Limitação**: menos eficaz em processos de conhecimento altamente variáveis, onde o escopo de cada instância difere muito.

## 5. Six Sigma (DMAIC)

Metodologia estatística focada em reduzir defeitos e variação. Ciclo **DMAIC**: Definir → Medir → Analisar → Melhorar → Controlar.

- **Use quando**: o problema central é qualidade/variação (não velocidade), e existem dados quantitativos suficientes para análise estatística de causa raiz.
- **Limitação**: alto rigor estatístico, pouco ágil; exige volume de dados que processos pouco estruturados ou de baixo volume não têm.

## 6. Teoria das Restrições (TOC — Goldratt)

Parte da premissa de que o desempenho de qualquer processo é ditado pelo seu elo mais fraco (o gargalo/restrição). Otimizar recursos que não são a restrição não move o resultado global — pode até piorar (gera fila e confusão de priorização).

**Cinco Passos de Focalização**:

1. **Identificar** a restrição — o passo que limita a capacidade global.
2. **Explorar** a restrição — extrair sua capacidade máxima com os recursos existentes, garantindo que nunca fique ociosa.
3. **Subordinar** o resto do sistema ao ritmo da restrição (técnica Tambor-Pulmão-Corda), evitando acumular trabalho em progresso além do que o gargalo consegue absorver.
4. **Elevar** a restrição — investir capital/recursos para quebrar o gargalo, se a exploração não bastou.
5. **Repetir** — a restrição sempre se move para outro ponto; reinicie o ciclo sem deixar a inércia criar limites artificiais.

- **Use quando**: há um gargalo claro e mensurável que limita todo o fluxo (fila, capacidade, aprovação centralizada).
- **Limitação**: foca em um gargalo por vez — pode ignorar subotimizações periféricas que afetam a experiência do cliente sem passar pelo gargalo.

## 7. Métodos ágeis / Kanban

Visualiza o fluxo de trabalho em colunas (ex.: A Fazer / Em Andamento / Concluído) e limita o trabalho em progresso (WIP), evidenciando gargalos por acúmulo visual de cartões parados.

- **Use quando**: o processo é de trabalho de conhecimento, criativo ou de suporte, com alta variabilidade de escopo por item.
- **Limitação**: menos formal para processos rigidamente regulados ou com interdependência estrita entre etapas.

## 8. Heurísticas de Redesenho de Processos (Dumas et al.)

Enquanto os frameworks acima ajudam a diagnosticar *onde* atuar, as heurísticas de Dumas (consolidadas em *Fundamentals of Business Process Management*) dão regras concretas de *como* redesenhar o fluxo lógico.

### O Quadrângulo do Diabo

Toda decisão de redesenho envolve trade-off entre quatro eixos: **Tempo, Custo, Qualidade e Flexibilidade**. Melhorar um agressivamente costuma custar em outro (ex.: comprimir tempo de ciclo pode aumentar custo ou reduzir flexibilidade para exceções). Nunca proponha um redesenho sem declarar explicitamente qual eixo está sendo sacrificado.

### Categorias de heurísticas

- **Perspectiva de clientes**: autoatendimento (self-service), interfaces omnicanal, resolução no primeiro contato.
- **Operação do processo**: eliminar tarefas puramente burocráticas, fundir etapas sequenciais fragmentadas para reduzir handoffs, particionar trabalho por complexidade.
- **Comportamento do processo**: paralelizar atividades antes sequenciais, aplicar "knock-out" (verificações que reprovam rápido acontecem primeiro, para economizar esforço em casos que vão falhar de qualquer forma).
- **Organização e participantes**: delegar poder de decisão a níveis inferiores, criar células com visão end-to-end do caso em vez de silos departamentais.
- **Informação e tecnologia**: capturar dado uma única vez na fonte primária (evitar redigitação), substituir integrações assíncronas por sistemas orientados a evento/dado mestre integrado.

## 9. Comparação estratégica dos frameworks

| Framework | Foco principal | Cenário ideal | Limitação estrutural |
|---|---|---|---|
| **BPMN** | Notação gráfica formal | Modelagem para automação/comunicação negócio-TI | Complexo/burocrático para fluxos criativos ou ainda instáveis |
| **ABPMP CBOK / APQC PCF** | Governança e taxonomia corporativa | Diagnóstico de maturidade, M&A, portfólio de processos | Descritivo — não otimiza um gargalo ou fluxo específico |
| **Lean / VSM** | Eliminação de desperdício, compressão de tempo | Processos estáveis, repetitivos, intensivos em manipulação | Menos eficaz em trabalho de conhecimento muito variável |
| **Six Sigma (DMAIC)** | Redução de variação/defeitos | Processos orientados a métricas de qualidade com dado disponível | Alto rigor estatístico, pouco ágil |
| **TOC** | Explorar/elevar o gargalo único | Ambientes com limite de capacidade óbvio | Foca um gargalo por vez; pode ignorar subotimizações periféricas |
| **Kanban** | Fluxo contínuo, visualização de WIP | Trabalho de conhecimento/suporte/inovação | Informal demais para processos rigidamente regulados |
| **Heurísticas de Dumas** | Redesenho tático via trade-offs explícitos | Digitalização de serviços administrativos, orquestração BPMS/RPA | Trade-offs raramente são pacíficos — otimizar custo/tempo pode fraturar qualidade/flexibilidade |

Regra prática de seleção: comece sempre pelos fundamentos (elementos estruturais, ver `fundamentos-e-elementos.md`) para entender o processo antes de aplicar qualquer framework. Se o problema é **desperdício/tempo**, use Lean/VSM. Se é **variação/qualidade**, use Six Sigma. Se é **um gargalo evidente de capacidade**, use TOC. Se é **como reformular o fluxo lógico** depois de já saber onde atuar, use as heurísticas de Dumas. BPMN, CBOK e PCF são estruturas de documentação/governança que podem envolver qualquer um dos anteriores — não competem com eles, os complementam.

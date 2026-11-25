# Estrutura para Decisões de Dados

Comece pelo resultado que os dados devem permitir. Não escolha tecnologia pelo nome do fornecedor, pela popularidade ou por uma arquitectura de referência antes de compreender a carga.

## Levantamento

Registe, mesmo que como intervalo ou hipótese:

| Dimensão | Pergunta operacional |
|---|---|
| Decisão | Que decisão, tarefa ou produto depende destes dados? O que acontece se estiver errado ou atrasado? |
| Consumidor | Aplicação transaccional, dashboard, exploração ad hoc, modelo, agente, sistema regulado ou integração? |
| Fonte | Que sistema é autoridade? Há exportação, API, log de mudanças, CDC ou ficheiros? |
| Forma e semântica | Qual é a granularidade? O que representa uma linha/evento? Quais são as chaves e unidades? |
| Escala | Volume actual, crescimento, tamanho de pico, cardinalidade, retenção e custo de armazenamento/consulta? |
| Tempo | Latência exigida, frescura, ordem dos eventos, atrasos, correcções e backfills? |
| Acesso | Quem pode ler ou alterar cada classe de dados? Há separação por tenant, utilizador ou finalidade? |
| Operação | Quem mantém fontes, destino, credenciais, migrações, qualidade, incidentes e recuperação? |
| Restrições | Jurisdição, residência, retenção, disponibilidade, orçamento, competências, contratos e stack existente? |

Não bloqueie a resposta por falta de uma métrica que não muda a escolha. Marque lacunas e mostre que decisão elas podem alterar.

## Escolha por Perfil de Carga

| Perfil observado | Opções a comparar | Condição que decide |
|---|---|---|
| Estado operacional de uma aplicação | Base transaccional relacional ou outro armazenamento operacional | Integridade, transacções, padrão de acesso, concorrência e necessidade de actualizações imediatas |
| Relatórios recorrentes sobre histórico amplo | Warehouse, lakehouse ou réplica analítica | Volume, concorrência analítica, formatos/fontes, isolamento do OLTP e competências operacionais |
| Eventos contínuos com atraso baixo | Streaming, CDC ou micro-batch | Latência real exigida, replay, ordenação, estado e custo de operar consumidores contínuos |
| Exportações periódicas e volume previsível | Batch/ELT simples | Janela suficiente, custo aceitável de reprocessar e tolerância a dados atrasados |
| Integração de muitas fontes heterogéneas | Plataforma de ingestão ou conectores específicos | Cobertura real de fontes, limites, semântica de deletes, observabilidade e portabilidade |
| Agente a consultar dados governados | API de domínio, camada semântica, vistas SQL ou ferramentas limitadas | Permissões, contexto mínimo, semântica de métricas e capacidade de auditar a consulta |

São opções de investigação, não regras universais. Uma base relacional pode servir analytics moderado; um warehouse pode não ser necessário para uma carga pequena. Separe OLTP e OLAP quando a concorrência, o custo, o histórico ou o isolamento exigirem fronteiras distintas.

## Critérios Comparáveis

Compare pelo menos: exactidão semântica; latência/frescura; throughput e concorrência; recuperação e replay; privacidade e controlo de acesso; custo total e custo de falha; operação e competências; portabilidade; dependência do fornecedor; qualidade da documentação; risco de migração.

Faça protótipo ou benchmark quando a decisão depender de desempenho, custo ou recuperação. Use as mesmas consultas/dados, selecção representativa, versão, concorrência, condições de cache e critérios de sucesso. Registe resultados por cenário, não só uma média.

## Pergunta de Paragem

Antes de adicionar ferramenta ou camada, responda: qual requisito actual não é satisfeito pela opção mais simples? Se a resposta for apenas uma capacidade futura não confirmada, registe-a como hipótese e estime o custo de adiar a decisão.

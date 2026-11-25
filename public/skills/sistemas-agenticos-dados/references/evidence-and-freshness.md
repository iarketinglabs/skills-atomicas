# Evidência, Proveniência e Informação Mutável

## Classifique a Afirmação

Antes de recomendar ou citar um facto técnico, identifique o tipo:

| Tipo | Como tratar |
|---|---|
| Princípio de engenharia | Explique o mecanismo e as condições em que se aplica; evite transformá-lo numa regra sem excepções. |
| Capacidade de produto/versão | Confirme documentação oficial, versão e estado de disponibilidade. |
| Limite, preço ou plano | Verifique a fonte do fornecedor e data exacta; confirme no projecto/contrato. |
| Alegação de desempenho | Identifique autor, carga, dados, ambiente, versão, métrica e independência da fonte. |
| Resultado académico | Leia o trabalho e a população/tarefa avaliada; não extrapole para workloads diferentes. |
| Regra legal | Verifique texto oficial, jurisdição, vigência, transição e contexto jurídico aplicável. |

Documentação de fornecedor é fonte primária para o funcionamento anunciado do produto, mas não valida de modo independente desempenho, preço final, adequação ou ROI.

## Quando as Fontes Divergem

Não faça média artificial nem escolha a afirmação mais recente sem examinar método e âmbito. Compare:

- tarefa e população avaliadas;
- definição de sucesso e métrica;
- tamanho, distribuição e qualidade dos dados;
- versão, configuração, hardware, cache e concorrência;
- interesses do autor e possibilidade de replicação;
- data e condições que podem explicar a diferença.

Descreva a decisão condicional: “opção A para carga X; opção B quando Y”. Se faltar evidência, indique o ensaio menor que resolveria a dúvida. Use rótulos claros como confirmado em fonte primária, fonte do fornecedor, benchmark limitado, hipótese ou não verificado.

## Desenho de Avaliação

Para pipeline, RAG, modelo ou motor de dados, versione pergunta, amostra, schema, código, configuração, versão de serviço, ambiente e critério. Inclua casos de falha e tempo, não apenas snapshots: atraso, duplicação, correção, reprocessamento, mudança de schema e permissão. Separe verificações determinísticas (schema, contagem, estado, acesso) de avaliação semântica e revisão humana.

Um benchmark isolado não prova qualidade geral. Reporte distribuição, segmentos, variância, falhas graves e limites. Para juízes automáticos, valide uma amostra contra referência humana independente.

## Comunicação de Incerteza

Apresente explicitamente:

- o que foi observado e em que período;
- o que é inferência ou pressuposto;
- fonte e data de consulta para aspectos mutáveis;
- condições que invalidariam a recomendação;
- lacunas que não foi possível verificar.

Não transforme ausência de dados numa conclusão negativa, nem seleccione só resultados que favoreçam a arquitectura preferida.

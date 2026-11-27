# Métodos e momento de decisão

## Compare as opções

| Momento | Sinais disponíveis | Exemplos de mecanismo | Ganho possível | Custo ou risco principal |
|---|---|---|---|---|
| Pré-geração | Requisição, metadados e contexto conhecido | Regras, embeddings, k-NN, classificador ou decisor de opções | Escolha barata antes da geração | Erros de previsão; sinais podem não revelar dificuldade real. |
| Pós-geração | Resposta candidata e verificações | Cascata, juiz de qualidade, autoverificação ou validação | Escalar apenas respostas com evidência de insuficiência | Chamadas e latência adicionais; juiz pode aceitar erro ou rejeitar resposta válida. |
| Intra-geração | Tokens, passos ou estado parcial | Decodificação especulativa, despacho por token ou passo | Aplicar esforço onde a tarefa mais precisa | Sincronização, overhead, dependência de implementação e cache. |
| Multi-turno | Histórico permitido, resultados anteriores e orçamento da sessão | Afinidade de sessão, alocação de orçamento por turno, política de trajetória | Distribuir esforço e preservar continuidade | Troca de modelo pode descartar cache ou contexto; custos acumulam-se. |

As categorias podem ser combinadas. A composição precisa ser explícita para que o efeito e o custo de cada estágio possam ser avaliados separadamente.

## Roteamento pré-geração

1. **Regras determinísticas:** use quando a decisão depende de campos confiáveis, categorias fechadas, requisitos de capacidade ou limites de política. São fáceis de auditar, mas não descobrem relações semânticas por si.
2. **Similaridade semântica ou k-vizinhos:** compare a requisição com exemplos ou representações associadas a decisões anteriores. Defina distância, base de referência, limiar, tratamento de não correspondência e política de atualização.
3. **Classificador supervisionado ou roteador aprendido:** estime resultados por candidato com dados rotulados representativos. Separe treino, calibração e teste; monitore mudança de tráfego, viés de rótulos e concentração em um candidato.
4. **Decisor tipado ou chamada de seleção:** útil para escolhas pequenas e explícitas. Verifique opção ausente, abstenção, confiança, neutralidade dos rótulos e desempenho semântico fora da validação.

Não use conteúdo fornecido pelo usuário como autoridade para alterar elegibilidade ou política. Trate texto, metadados incompletos e rótulos de dificuldade como sinais, não garantias.

## Cascatas pós-geração

Uma cascata chama primeiro um candidato e depois aceita, verifica ou escala a resposta. Antes de adotá-la:

- defina quais erros exigem escalada e como são observados;
- separe verificações determinísticas, como formato ou campos obrigatórios, de juízos semânticos;
- valide o verificador contra exemplos corretos e incorretos do workload;
- meça a taxa de falso aceite e falso escalonamento por segmento;
- limite profundidade, custo total, latência e retentativas;
- defina o comportamento se verificador ou candidato estiver indisponível.

Uma confiança de modelo ou um escore de juiz só deve acionar decisões depois de ser calibrado e testado. Não copie um limiar numérico de um artigo, exemplo ou outro domínio.

## Roteamento intra-geração

Decisões por token ou passo podem adaptar o uso de modelos durante uma geração. Decodificação especulativa pode reduzir latência sob algoritmos e condições específicas. Não afirme equivalência de saída, ganho ou suporte sem verificar a descrição técnica da implementação e medir no workload.

Inclua no teste custo de sincronização, chamadas de coordenação, paralelismo, interrupções, cancelamentos e estado de cache. Compare a política adaptativa com geração comum em condições de concorrência semelhantes.

## Roteamento multi-turno e agentes

Avalie a trajetória inteira, não apenas chamadas unitárias:

- mantenha o orçamento de custo e passos no escopo da sessão ou tarefa;
- inclua chamadas a verificadores, ferramentas e candidatos de recuperação;
- analise se a troca de candidato exige reconstruir contexto ou perde cache;
- teste afinidade de sessão e troca de modelo em condições reais;
- defina como carregar estado e resultados anteriores sem expor dados a um candidato inelegível;
- avalie custo por tarefa concluída, qualidade final e taxa de conclusão, não só preço por chamada.

Um orçamento de raciocínio ou número de amostras também é uma ação de roteamento. Compare-o como uma política explícita e não o trate como custo zero por usar o mesmo modelo.

## Modalidades e capacidades

Mantenha perfil de capacidade por modalidade e formato: texto, imagem, áudio, vídeo ou combinações. Verifique tipos de entrada, limites, resolução, duração, ferramentas associadas, região, retenção, preço e comportamento de erro da versão exata. Não deduza suporte a uma modalidade a partir do nome do modelo, gateway ou API compatível.

Quando a evidência disponível não cobrir uma modalidade ou um formato, limite a conclusão ao que foi medido e deixe a lacuna visível.

## Escolha o método mínimo

1. Use modelo fixo se cumpre os limites e a política variável não demonstra ganho.
2. Use regras se os sinais e decisões forem explícitos.
3. Considere semântica ou classificador quando exemplos mostram segmentos previsíveis e diferentes.
4. Considere cascata quando há um sinal pós-resposta confiável e o custo da chamada inicial compensa as escaladas.
5. Considere roteamento intra-geração ou multi-turno quando o benefício depende da trajetória e o sistema consegue contabilizar estado, cache e orçamento.
6. Remova qualquer estágio que não contribua com resultado líquido mensurável.

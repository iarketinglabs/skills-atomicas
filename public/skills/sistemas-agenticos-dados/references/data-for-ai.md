# Dados para IA, Pesquisa e Agentes

## Percurso de Dados

Desenhe a cadeia completa, não apenas a geração de embeddings:

`fonte -> extracção/parsing -> normalização -> metadados e proveniência -> segmentação -> representação/feature -> índice -> recuperação -> autorização -> contexto -> resposta -> avaliação`

Para cada etapa, registe versão, tempo de origem, transformações, falhas, reprocessamento, eliminação, owner e dependências. PDFs com tabelas, transcrições, e-mails e registos tabulares requerem unidades semânticas diferentes; divisão por tamanho fixo é apenas uma baseline a avaliar.

## Pesquisa e RAG

Escolha recuperação de acordo com perguntas e falhas observadas:

- Pesquisa lexical pode ser adequada para identificadores, nomes, códigos e termos exactos.
- Pesquisa vectorial pode ajudar em consultas semânticas, se a representação e o domínio preservarem a noção de similaridade desejada.
- Pesquisa híbrida combina sinais lexicais e vectoriais; calibre fusão, filtros e reranking em consultas representativas.
- Grafos ou GraphRAG podem ajudar em relações explícitas, perguntas multi-hop ou síntese global. Acrescentam ingestão, construção de grafo, contexto e custo; não são pré-requisito para todo RAG.

Construa um conjunto de avaliação a partir das tarefas reais. Inclua consultas exactas, ambíguas, temporais, multi-hop, sem resposta, com metadados/filtros e por perfil de acesso. Avalie separadamente: recall de evidência relevante; precisão e ranking; cobertura de filtros/permissões; fundamentação das respostas; citações/proveniência; frescura; latência e custo. Faça anotação humana de uma amostra para calibrar avaliações automáticas; não trate um juiz LLM como oráculo.

## Embeddings e Índices

Registe modelo e versão, dimensão, normalização, métrica de distância, idioma/domínio, data e hash do conteúdo. Só compare embeddings compatíveis; ao mudar o modelo, planeie reindexação/backfill e coexistência de versões. Avalie recuperação com os filtros, taxa de actualização, concorrência e selectividade reais.

Uma extensão vectorial num banco relacional pode simplificar transacções, autorização e operação para cargas adequadas. Um motor vectorial especializado pode ser melhor noutros regimes de volume, filtros, concorrência ou latência. Decida com medição end-to-end de recall, p95/p99, custo, actualização, isolamento e falhas; não assuma limiares universais.

## Contexto Autorizado

Recupere apenas dados cujo leitor actual possa aceder. Aplique autorização antes de enviar conteúdo ao modelo, preserve escopo por tenant e finalidade, filtre documentos expirados/revogados, e registe proveniência sem guardar payload sensível desnecessário. Uma resposta correcta com conteúdo proibido continua a ser uma falha.

Trate conteúdo recuperado como dado não confiável, nunca como política ou instrução de sistema. Para acções sobre o mundo, a autorização permanece fora do modelo. Use `sistemas-agenticos-seguranca` se disponível para desenhar threat model e enforcement do agente.

## Features e Dados Sintéticos

Features para treino e inferência precisam de definições, unidades, timestamps, origem e regras de cálculo compatíveis. Verifique consistência temporal, disponibilidade no momento da previsão e skew entre treino e serviço.

Dados sintéticos podem apoiar desenvolvimento ou cobrir casos raros; identifique-os, mantenha-os separados de evidência real e compare distribuição, cobertura de modos de falha, privacidade e viés. Não os apresente como amostra observada nem como prova de desempenho em produção.

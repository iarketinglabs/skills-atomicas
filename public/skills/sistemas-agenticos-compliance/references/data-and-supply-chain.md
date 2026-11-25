# Dados, proveniência e cadeia de fornecimento

Analise cada operação de dados e cada parte do fornecimento. Treinamento, ajuste fino, inferência, logging e recuperação por RAG têm fluxos e efeitos distintos. Não presuma que dado público, dado anonimizado ou dado sintético esteja automaticamente liberado para qualquer finalidade.

## Ciclo de dados e direitos

Para dados de treinamento, prompts, documentos recuperados, memória, entradas de ferramenta, saídas e logs, registre:

- origem, coletor, titular/licença e cadeia de permissões;
- finalidade original e finalidade pretendida;
- categorias de dados, pessoas afetadas e sensibilidade;
- base ou fundamento de uso a confirmar pela função responsável;
- transformações, cópias, embeddings, índices, modelos derivados e destinos;
- localização, retenção, acesso, transferências e subprocessadores;
- mecanismo de acesso, correção, objeção, exclusão, retenção legal ou contestação, quando aplicável;
- evidência de minimização, segurança, qualidade e mitigação de vieses.

Para dados pessoais, identifique separadamente finalidade, papéis, base legal, transparência, direitos, retenção, transferências e avaliação de impacto que possam ser exigidos. Não conclua a base legal apenas pela disponibilidade técnica do dado.

## RAG, memória e conteúdo

Em retrieval augmented generation e memória persistente, avalie:

- direitos de acesso e reutilização antes de ingestão;
- autorização por usuário e por documento em cada recuperação;
- proveniência, versão, classificação, confiança e data de atualização da fonte;
- separação entre dados recuperados e instruções autorizadas;
- exposição em prompts, saídas, traces, caches e ferramentas;
- isolamento entre usuários, organizações e sessões;
- atualização, retirada, correção e propagação de exclusões;
- risco de identificação, inferência, vazamento, envenenamento e recuperação indevida.

Usar retrieval em vez de treinamento não elimina questões de privacidade, direitos autorais, confidencialidade, segurança ou retenção. Marca d'água e proveniência podem apoiar rastreabilidade, mas não provam que conteúdo é verdadeiro.

## Diligência de fornecedores

Avalie provedores de modelo, hospedagem, dados, ferramentas, conectores, avaliação e subcontratados. Pergunte, conforme o escopo:

- quais entradas, saídas, feedbacks, metadados e logs o fornecedor armazena ou reutiliza;
- se há treinamento, ajuste fino, avaliação ou melhoria com dados do contratante;
- localização, transferência, subcontratados, retenção, exclusão e isolamento;
- versões, limitações, mudanças, documentação técnica, avaliações e medidas de segurança;
- controle de identidade, acesso administrativo, logging, vulnerabilidades e incidentes;
- transparência, assistência para direitos/solicitações, auditoria e cooperação regulatória;
- alocação de papéis, propriedade intelectual, confidencialidade e responsabilidade;
- portabilidade, exportação, continuidade, suspensão e encerramento.

Não aceite uma cláusula genérica de não treinamento como prova técnica. Compare termos contratuais, configuração e comportamento do serviço. Identifique o que foi verificado e o que depende de resposta do fornecedor.

## Contratos e transferência de risco

Associe cada compromisso contratual a um controle observável e a uma evidência. Verifique se os prazos de aviso do fornecedor permitem à organização investigar e cumprir suas próprias obrigações. Escalone ambiguidades sobre treinamento, subprocessamento, transferência internacional, propriedade, logs, incidentes e término.

Um questionário preenchido ou uma certificação pode compor evidência de diligência; não substitui validação do serviço concreto, análise do fluxo de dados, controles técnicos ou obrigações legais próprias.

# Metodologia de Rodadas de Refinamento

Depois que a base documental tem seu esqueleto e os MVPs do primeiro ciclo, o trabalho passa a ser iterativo: rodadas de refinamento que revisam e enriquecem o que já existe conforme mais fonte primária é coletada ou revisitada. Este arquivo descreve como conduzir uma rodada.

## Princípio central: uma pasta/tema por rodada

Defina escopo explícito e restrito por rodada — uma pasta operacional, um tema transversal ou um perfil individual de stakeholder. Isso mantém o diff revisável, a citação de fonte precisa e os achados de cada tema rastreáveis.

Antes de começar, registre: objetivo da rodada, pasta/tema exato, fontes autorizadas, artefatos que podem ser alterados, arquivos encontrados e estado inicial do worktree. Em um worktree já modificado, a ausência de limpeza não é falha; o requisito é preservar o que existia e distinguir o delta desta rodada.

## Passo 1 — Minere a fonte primária bruta por completo

Não se contente com sínteses já processadas (wikis, atas condensadas) quando a rodada é sobre enriquecer/aprofundar. Releia a transcrição, formulário ou documento **bruto**, na íntegra, mesmo que já tenha sido usado antes — a primeira leitura raramente esgota o que uma fonte rica (ex.: uma reunião de 1h30 transcrita) contém.

Quando a fonte for grande demais para uma leitura direta (transcrições longas, pesquisas extensas com múltiplos arquivos), divida em grupos por tamanho ou tema. Use processamento reproduzível ou leitura paralela somente-leitura quando as ferramentas e as regras da sessão permitirem. Cada leitura paralela deve:
- Cobrir todo o material designado, sem parar na metade nem amostrar.
- Devolver achados **estruturados por tema** com citação de trecho ou timestamp aproximado.
- Receber contexto sobre o que já é conhecido e o que procurar, para reduzir duplicação e ruído.

Para cada achado, capture no mínimo: afirmação, fonte, data, localização, pessoa/função que relatou quando conhecida, classificação (`factual`, `hipótese`, `pendente`, `contradição`, `caso observado` ou `fora de escopo`), escopo/amostra, confiança, impacto e validação necessária. Não confunda a ausência de uma menção com prova de que o processo ou ferramenta não existe.

Depois da primeira leitura, faça uma conferência de cobertura contra os temas, perguntas e lacunas do escopo. Releia os trechos relevantes para encontrar detalhes, decisões, compromissos ou ressalvas que a primeira síntese possa ter omitido. Registre a cobertura no material de trabalho da rodada; crie um artefato permanente somente se o PRD pedir.

Se um grupo de leitura falhar ou ficar incompleto, processe-o novamente antes de prosseguir e registre qualquer limite de cobertura que permaneça.

Se a fonte for material operacional real de um cliente do próprio cliente (evidência de cliente-modelo, não uma entrevista/formulário sobre o cliente diagnosticado), siga também `references/evidencia-de-cliente-modelo.md` — ele cobre a regra de sujeito da frase, o que conta como evidência válida, o tratamento de arquivos de mídia e o status padrão desse tipo de achado.

## Passo 2 — Cruze com o que já está documentado

Compare cada achado novo com o conteúdo já existente. Dois resultados possíveis:
- **Confirma e enriquece:** adiciona detalhe, citação mais precisa, ou contexto que faltava.
- **Corrige:** revela que algo já documentado estava impreciso ou mal atribuído (ex.: um resultado que havia sido atribuído a uma ferramenta genérica era, na fonte primária, um workflow específico de outra ferramenta). Corrija explicitamente, deixando claro na própria edição que é uma correção de atribuição — nunca apague silenciosamente o dado antigo sem registrar a mudança (RN-6).

Quando houver versões conflitantes, mantenha a contradição visível até existir fonte oficial ou validação explícita. Quando houver correção de atribuição, localize e corrija todas as ocorrências materiais, inclusive documentos derivados, matriz e lacunas afetadas. Quando houver um ganho, piloto ou automação em uma amostra, registre-o como `caso observado`, incluindo contexto, resultado relatado, limitações e próxima validação; não o promova a baseline ou recomendação replicável.

## Passo 3 — Distinga evidência do cliente de material de referência

Nem tudo que entra numa rodada é evidência sobre o cliente. Frameworks metodológicos, pesquisa de produto/mercado, mapas mentais e outros materiais de referência genérica **nunca** recebem status `factual` sobre o cliente — são citados como fonte metodológica à parte, usados para estruturar ou contextualizar, não como fato sobre a operação real do cliente. Misturar os dois tipos de fonte é o erro mais fácil de cometer numa rodada que envolve pesquisa externa.

## Passo 4 — Trate pedidos explícitos do cliente como mandato prioritário

Se uma fonte primária registra um pedido explícito do cliente, documente-o como mandato com escopo, responsável e entrega esperada. Registre essa natureza sem convertê-lo automaticamente em ranking de impacto, recomendação ou decisão de piloto; aplique os gates do projeto.

## Passo 5 — Investigue arquivos/pastas inesperados antes de usar

Se durante a rodada você encontrar arquivos ou pastas no workspace que não foram criados por você e não estavam previstos no plano da rodada, **pare e investigue o conteúdo antes de decidir o que fazer**. Pode ser:
- Trabalho em andamento do próprio usuário (não mexer sem perguntar).
- Material relevante para responder exatamente a lacuna que a rodada está tentando fechar (comunique ao usuário e pergunte se deve incorporar).

Nunca absorva silenciosamente (pode distorcer a proveniência) nem ignore silenciosamente (pode ser exatamente o que falta).

## Passo 6 — Propague para os documentos-raiz impactados

Antes de atribuir os próximos IDs de `EV-` ou `LC-`, releia `matriz-evidencias.md` e `lacunas-e-plano-de-coleta.md` e confira o maior número **já em uso em toda a árvore** (incluindo os arquivos de `Operacoes/*/lacunas.md`), não apenas o que você leu no início da rodada — outra rodada pode estar em andamento em paralelo, em outra pasta, e já ter reservado os próximos números. Se detectar uma colisão só depois de escrever, renumere o seu bloco e registre no changelog que a renumeração aconteceu por causa de uma rodada concorrente, sem sobrepor o conteúdo da outra rodada.

O conjunto mínimo de propagação é contextual, não uma obrigação de editar arquivos sem impacto:

- toda evidência material (RN-4) aparece em `matriz-evidencias.md`;
- toda lacuna nova ou resolvida aparece em `lacunas-e-plano-de-coleta.md`;
- toda mudança substantiva recebe entrada em `registro-atualizacoes.md`, com data, mudança, motivo e gate afetado, se houver;
- `indice-entregaveis.md` só é atualizado quando o estado, bloqueio ou condição de avanço de uma entrega mudar;
- o documento da área, tema ou stakeholder afetado é atualizado quando o achado alterar seu conteúdo.

Um achado que só existe no documento de domínio, sem propagação necessária, está incompleto; editar todos os documentos-raiz por rotina, porém, cria ruído e também deve ser evitado.

## Passo 7 — Sinalize, não execute, achados fora de escopo

É comum que a mineração de uma fonte rica traga achados relevantes para pastas fora do escopo desta rodada (ex.: minerando uma transcrição pela lente de "uso de IA", você também encontra um achado relevante para "gestão de mudança" ou "recrutamento"). Registre esses achados explicitamente no `registro-atualizacoes.md` como pendência sinalizada para a próxima rodada, com fonte e citação suficientes para não precisar re-minerar depois — mas não os execute na rodada atual. Isso mantém o diff de cada rodada revisável e o escopo do usuário respeitado.

## Passo 8 — Nunca feche o que os gates não permitem fechar

Mesmo com evidência rica e sinalizações fortes, respeite os gates de `regras-de-governanca.md`. Uma sinalização indireta de prioridade (ex.: o cliente mencionou um cliente-piloto de passagem) não é uma decisão fechada — registre como `hipótese`, não como escolha validada.

Um AS-IS baseado apenas em liderança pode ser documentado como **preliminar**, desde que declare a limitação e contenha um roteiro para validação com o executor/owner real. Só use **consolidado** depois de confirmar gatilho, passos, handoffs, sistemas, responsáveis, saída, exceções e validação operacional, conforme RN-11.

Se a rodada revelar um processo sem volume, esforço, periodicidade ou custo-hora confirmados, registre o fluxo e a lacuna, mas não feche COI. Se revelar um resultado de IA sem baseline comparável, registre o caso observado, mas não feche ROI, recomendação ou generalização.

## Passo 9 — Perfis individuais seguem sua própria estrutura

Quando a rodada é sobre um stakeholder específico, siga `perfil-individual-stakeholder.md` em vez de tratar como uma pasta operacional comum.

## Passo 10 — Verificação final da rodada

Antes de considerar a rodada concluída:
- [ ] Toda citação nova tem fonte exata (arquivo + trecho/timestamp aproximado) e status `factual`/`hipótese`/`pendente`.
- [ ] Cada evidência material registra data, localização, escopo/amostra, confiança, impacto e validação necessária, conforme aplicável.
- [ ] Nenhum gate de avanço analítico foi violado.
- [ ] Toda correção de atribuição foi propagada a todos os lugares onde o dado antigo aparecia.
- [ ] Os documentos-raiz impactados foram atualizados; os não impactados não foram alterados artificialmente.
- [ ] O AS-IS está rotulado como preliminar ou consolidado, com os campos obrigatórios e a validação correspondente.
- [ ] O roteiro de coleta, quando criado, contém participantes, reconstrução de tarefa, perguntas, fontes e baseline com período/unidade.
- [ ] Estimativas, contradições, casos observados e ausência de evidência permanecem identificados.
- [ ] Métricas preservam unidade, período, população, denominador, moeda e data de extração quando aplicável; dados pessoais e sensíveis foram minimizados.
- [ ] Achados fora de escopo estão sinalizados, não executados.
- [ ] O diff foi comparado ao estado inicial e não inclui alterações preexistentes ou fora do escopo autorizado.
- [ ] Fontes e links relativos usados pela rodada existem e a estrutura Markdown foi verificada quando aplicável.

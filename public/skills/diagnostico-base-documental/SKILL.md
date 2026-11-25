---
name: diagnostico-base-documental
description: Use esta skill para criar e manter bases documentais de evidências de diagnósticos de eficiência com IA em diferentes empresas. Abrange a estrutura inicial e rodadas de refinamento de fontes primárias, como entrevistas, formulários de maturidade, pesquisas, exportações de sistemas e materiais operacionais de contas atendidas. Ative para montar ou revisar a base, analisar autoavaliações de maturidade, enriquecer um tema, corrigir atribuições ou analisar dados de CRM/pipeline. Ajuste nomes e caminhos ao escopo aprovado.
---

# Base Documental do Diagnóstico

## Identidade

Você mantém a base documental viva de evidências de um diagnóstico de eficiência com IA para uma empresa e um projeto específicos. Use `executions/src/diagnostico/` como caminho padrão somente quando o PRD ou a convenção do repositório não indicar outro destino. Seu trabalho é organizar o material coletado, preservar sua proveniência e comunicar limites de certeza; a metodologia de entrevistas, cálculos e decisões analíticas segue o escopo aprovado e as ferramentas disponíveis no projeto.

Esta skill deve funcionar com clientes de setores e estruturas diferentes. Não codifique nomes de clientes, pessoas, fornecedores, ferramentas, caminhos absolutos, setores, métricas ou decisões de um projeto concreto. Use placeholders como `<cliente>`, `<área>`, `<stakeholder>`, `<fonte>` e `<sistema>` nos exemplos. Trate os nomes de pastas e documentos abaixo como convenções adaptáveis: o PRD ou escopo aprovado do projeto define a estrutura efetiva.

## Quando usar / quando não usar

- **Use** para: criar a estrutura inicial; registrar entregas e evidências; refinar uma pasta ou tema; propagar evidências e lacunas; analisar respostas de autoavaliação de maturidade; criar um perfil individual quando houver motivo; analisar material operacional de uma conta atendida; ou minerar uma exportação bruta de CRM/pipeline. Leia as referências específicas para cada modo.
- **Não use** para: conduzir entrevistas, definir perguntas, calcular ROI/TCO ou readiness, nem ingerir ou reorganizar material bruto quando isso estiver fora do escopo documental aprovado. Use o método e os processos de ingestão definidos no projeto, quando disponíveis.

## Pré-requisito

Confirme que existe um PRD ou escopo equivalente com a árvore de pastas, as regras de evidência e os entregáveis aprovados. Adapte `references/regras-de-governanca.md` e `references/arvore-padrao.md` ao projeto; a numeração e os critérios do exemplo não substituem as decisões do PRD. Se o escopo ainda não existir, ajude a defini-lo antes de preencher a base — a governança não deve ser improvisada documento a documento.

Identifique a pasta de fontes indicada pelo PRD. `directives/` é apenas uma convenção possível. Se ainda não houver material primário, crie somente o esqueleto aprovado e as lacunas iniciais, informando essa limitação.

## Workflow

### Modo 1 — Construção inicial (primeiro ciclo)

1. Leia `references/arvore-padrao.md` e adapte a estrutura ao PRD, à linguagem usada pela empresa e às áreas realmente incluídas no diagnóstico.
2. Escreva primeiro os documentos-raiz exigidos pelo PRD. No modelo desta skill, são README, índice de entregáveis, matriz de evidências, lacunas e plano de coleta e registro de atualizações; eles definem as convenções dos demais documentos.
3. Popule os MVPs do primeiro ciclo a partir das fontes disponíveis e das sínteses já processadas. Use sínteses para orientar a busca e confira afirmações materiais na fonte primária quando ela estiver disponível. Aplique os status de evidência desde a primeira versão (`references/regras-de-governanca.md`).
4. Para cada área operacional incluída na árvore aprovada, crie o README previsto pelo PRD. Crie documentos de AS-IS e gargalos somente quando houver evidência suficiente; não crie arquivos vazios para completar a estrutura.
5. Documente no `README.md` raiz qualquer decisão de convenção que o PRD não previu explicitamente (ex.: onde vai um processo que não se encaixa nas pastas fixas) — não deixe implícito, a próxima pessoa/agente precisa achar sem perguntar de novo.
6. Verifique ao final: toda fonte citada existe de fato; nenhum valor de COI/ROI/score/priorização foi calculado sem os dados exigidos pelas regras de avanço analítico; links relativos apontam para arquivos existentes; e as alterações estão restritas ao escopo autorizado. Em worktree sujo, compare o estado inicial e preserve alterações preexistentes — não exija que o `git status` esteja limpo.
7. Considere a sincronização de painel somente quando o projeto documentar um painel vinculado e essa atualização estiver no escopo autorizado (ver "Painel vinculado" abaixo).

### Modo 2 — Rodadas de refinamento (ciclos seguintes)

Siga `references/metodologia-rodadas-refinamento.md` na íntegra. Resumo do princípio central: **uma pasta/tema por rodada**, nunca "revisar tudo" de uma vez. Cada rodada:

1. Registre o escopo explícito e restrito (uma pasta, um tema ou um stakeholder específico) e capture o estado inicial do worktree e dos arquivos-alvo.
2. Faça um inventário dos arquivos da pasta antes de editar. Investigue arquivos ou pastas inesperados antes de usar; não absorva nem ignore material novo silenciosamente.
3. Mine completamente as fontes primárias brutas relevantes, não apenas sínteses. Em fontes grandes, divida por tema ou tamanho e use processamento reproduzível ou leitura paralela somente quando as ferramentas e as regras da sessão permitirem. Registre achados estruturados com localização e classificação, não apenas resumos.
4. Cruze os achados com a fonte oficial, a memória/síntese e os documentos existentes. Classifique cada item como `factual`, `hipótese`, `pendente`, `contradição`, `caso observado` ou `fora de escopo` antes de redigir.
5. Corrija atribuições imprecisas explicitamente em todos os documentos afetados. Preserve versões divergentes até validação; registre a correção ou rebaixamento de confiança no changelog, sem sobrescrever histórico material silenciosamente.
6. Atualize somente os artefatos impactados. Evidência material vai para a matriz; lacuna nova ou resolvida vai para o rastreador; mudança substantiva vai para o changelog; o índice só muda quando estado, bloqueio ou gate de uma entrega mudar.
7. Achados que tocam pastas fora do escopo ficam **sinalizados no changelog** para a próxima rodada, com fonte e localização suficientes para não exigir nova mineração — não são executados agora.
8. Antes de atribuir IDs de evidência ou lacuna, confira os identificadores já usados em toda a árvore. Faça a verificação final de fontes, links, gates, escopo e worktree.
9. Considere a sincronização de painel somente quando documentada e autorizada para o projeto (ver "Painel vinculado" abaixo).

### AS-IS preliminar versus consolidado

Use estas duas categorias sem misturá-las:

- **AS-IS preliminar:** permitido quando existe descrição parcial, relato de liderança, documentação ou uma amostra operacional, mas falta validação com quem executa. Deve declarar o status, as fontes, o que é observado e o que continua pendente.
- **AS-IS consolidado:** só pode ser declarado quando houver gatilho, passos, handoffs, sistemas, responsáveis, saída, exceções e validação com o executor/owner real, conforme RN-11.

Todo AS-IS deve cobrir, quando aplicável: escopo e status da evidência; gatilho e entradas; fluxo observado; contexto; responsáveis; sistemas/ferramentas; handoffs; saída e critério de encerramento; exceções; gargalos/riscos; métricas disponíveis e ausentes; limites de conclusão; fontes com arquivo e localização aproximada. Se um campo não foi observado, marque-o como `pendente` em vez de inferi-lo.

### Roteiro de coleta por área

Quando uma área tiver lacunas relevantes, crie ou atualize `roteiro-coleta-<área>.md`. O roteiro deve conter participantes recomendados, duração, reconstrução de uma tarefa real, perguntas sobre entrada, execução, revisão, aprovação, encerramento, handoffs, exceções e retrabalho, sistemas a consultar, baseline a solicitar e critério de suficiência.

Cada métrica solicitada deve ter unidade, período, fonte esperada e responsável por obtê-la. O roteiro é instrumento de coleta: perguntas, valores vazios e exemplos de preenchimento não são respostas do cliente e não podem ser promovidos a evidência.

## Perfis individuais de stakeholder

Quando um sponsor, decisor-chave ou "power user" de IA merece um mapeamento próprio (rotina, conhecimento tácito, fluxo de informação, oportunidades), siga `references/perfil-individual-stakeholder.md`. Regra central: nunca inventar uma escolha de piloto ou prioridade pessoal — se a fonte real não chegou a uma decisão formal, registre como sinalização indireta, nunca como fato fechado.

## Evidência de cliente-modelo

Quando a pasta de fontes definida no projeto contiver material operacional real de uma conta que a empresa diagnosticada atende ou opera — e não uma entrevista sobre a própria empresa — siga `references/evidencia-de-cliente-modelo.md`. Regra central: **o processo da empresa diagnosticada é o sujeito da frase; a conta-modelo entra como evidência citada**. O negócio próprio dessa conta, fora do domínio entregue pela empresa diagnosticada, não é evidência sobre ela. Arquivos de imagem, vídeo e áudio são registrados como existentes, sem análise de conteúdo por esta referência.

## Dados de CRM/Pipeline

Quando a pasta de fontes definida no projeto contiver uma exportação bruta do CRM/pipeline comercial da própria empresa diagnosticada, siga `references/mineracao-dados-crm-pipeline.md`. Mine o export por completo; torne as contagens reproduzíveis; informe denominadores e períodos; registre divergências com relatos; e, quando a análise gerar uma entrega, separe performance histórica da documentação de processo.

## Formulários de maturidade

Quando a fonte incluir um formulário de autoavaliação de maturidade/readiness ou suas respostas, siga `references/mineracao-formularios-maturidade.md`. Preserve a versão do instrumento, os identificadores originais dos itens, as escalas e o estado de cada resposta. Separe uso declarado, capacidade autoavaliada, exemplo concreto, percepção e risco; trate cada um segundo sua proveniência. Uma autoavaliação individual não demonstra maturidade organizacional nem autoriza um score sem cumprir os gates do projeto.

## Dashboard vinculado

Quando o PRD, README do projeto ou instrução do usuário identificar um painel vinculado, leia o procedimento de atualização documentado e confirme se essa atualização está no escopo autorizado. A existência de um nome de repositório parecido, URL ou variável em arquivo de ambiente, isoladamente, não define o vínculo; não abra nem exponha segredos para inferi-lo.

Se a sincronização estiver no escopo e houver autorização para a publicação externa, gere o conteúdo a partir da base atualizada, use o mecanismo de criptografia previsto pelo projeto e publique apenas o artefato criptografado. Nunca publique texto plano ou credenciais. Confirme o resultado do deploy quando a publicação fizer parte da tarefa. Se a atualização não estiver documentada ou autorizada, conclua a base documental e registre o painel como dependência separada.

## Guardrails

- Nunca calcule ou publique COI, ROI, score de maturidade ou priorização final sem que os dados exigidos pelas regras de avanço estejam presentes — mantenha só modelo + lacunas até então (`references/regras-de-governanca.md`).
- Nunca trate material de referência genérico (framework metodológico, pesquisa de produto/mercado, mapa mental) como evidência factual sobre o cliente — cite-o como fonte metodológica à parte, nunca com o mesmo status de um dado do cliente.
- Preserve alterações preexistentes e não use comandos destrutivos para "limpar" o worktree. Registre o estado inicial antes de editar e valide somente o escopo autorizado.
- Não modifique a pasta de fontes do projeto (por exemplo, `directives/`) nem sua memória durante a manutenção da base, salvo solicitação explícita; esses materiais são fontes, não destino implícito desta skill.
- Se encontrar arquivos ou pastas no workspace que você não criou e que não estavam previstos no plano, **investigue o conteúdo antes de usar e avise o usuário explicitamente** — pode ser trabalho em andamento da própria pessoa. Não absorva nem ignore silenciosamente.
- Minimize dados pessoais e sensíveis nos documentos; não reproduza senhas, tokens ou credenciais. Use agregação ou pseudonimização quando preservarem a utilidade analítica e respeitarem o escopo aprovado.
- Respeite a finalidade, a voluntariedade e as promessas de privacidade descritas no instrumento; não reaproveite respostas individuais para avaliação de desempenho nem prometa anonimato sem confirmar o desenho da coleta.
- Não escolha uma versão entre fontes divergentes sem justificativa baseada em fonte oficial ou validação explícita — mantenha as duas registradas.
- Não sobrescreva histórico material sem registrar a mudança no changelog.
- Um piloto, automação, redução de tempo ou resultado de uma ferramenta em uma única amostra é `caso observado`; não o generalize para a área nem o transforme em recomendação, baseline, COI ou ROI sem validação comparável.
- Diferencie `ausência de evidência` (a fonte não permite afirmar) de `evidência de ausência` (a fonte demonstra que algo não existe). A primeira deve virar pendência, não fato negativo.
- Ao usar material de cliente-modelo, nunca descreva o próprio negócio dessa conta (fora do domínio que o cliente diagnosticado entrega) como evidência sobre o cliente diagnosticado; e nunca deixe o nome do cliente-modelo virar sujeito de uma frase do corpo do documento — ele é a evidência citada, não o assunto (`references/evidencia-de-cliente-modelo.md`).
- Não analise o conteúdo de arquivos de imagem, vídeo ou áudio ao minerar material de cliente-modelo — apenas registre que existem e em que pasta/contexto. Analisar esse conteúdo é um pedido explícito à parte.
- Ao sincronizar um painel autorizado, publique apenas o artefato criptografado previsto pelo projeto; mantenha texto plano, senhas e tokens fora do repositório publicado.

## Verificação antes de finalizar qualquer rodada

- [ ] Toda afirmação relevante tem status `factual`/`hipótese`/`pendente` explícito e fonte citada.
- [ ] Toda evidência material tem origem, data, confiança, impacto e validação necessária registrados na matriz.
- [ ] Matriz de evidências, lacunas, changelog e índice foram atualizados somente quando impactados pela rodada.
- [ ] Nenhum gate de avanço analítico foi violado (AS-IS, COI, ROI, maturidade, priorização final, recomendação de IA).
- [ ] AS-IS preliminar não foi apresentado como consolidado; campos não observados permanecem pendentes.
- [ ] Estimativas preservam unidade, período e marcador de estimativa; nenhum valor sem fonte foi usado em cálculo.
- [ ] Contradições, correções de atribuição e casos isolados foram mantidos rastreáveis.
- [ ] Achados fora do escopo desta rodada estão sinalizados, não executados.
- [ ] Fontes citadas e links relativos existem; Markdown/estrutura dos arquivos foi validado quando aplicável.
- [ ] Cliente, projeto ou dado específico não foi incorporado às instruções desta skill.
- [ ] O estado final foi comparado ao estado inicial e as alterações desta rodada estão restritas à base documental autorizada.
- [ ] Se a rodada usou material de cliente-modelo, todo achado descreve o processo da empresa diagnosticada e cita a conta apenas como evidência (`references/evidencia-de-cliente-modelo.md`).
- [ ] Se a rodada minerou uma exportação de CRM/pipeline, todo número citado é reproduzível, todo percentual tem denominador, e performance histórica está separada de documentação de processo (`references/mineracao-dados-crm-pipeline.md`).
- [ ] Se a rodada usou um formulário de maturidade, a versão, a população, a cobertura, os itens, as escalas, as respostas ausentes e os limites de autorrelato estão documentados (`references/mineracao-formularios-maturidade.md`).
- [ ] Se a sincronização de um painel documentado e autorizado fazia parte do escopo, publiquei somente o artefato criptografado e confirmei o deploy.

## Ver também

- Ferramentas ou skills do projeto que definam o método do diagnóstico, a ingestão de fontes e a visualização dos resultados, quando disponíveis. Esta skill organiza a documentação e segue os limites definidos por esses processos.

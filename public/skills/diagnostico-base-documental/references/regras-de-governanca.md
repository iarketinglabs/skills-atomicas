# Regras de Governança da Base Documental

Padrão de referência para regras de evidência de uma base documental de diagnóstico. Adapte os critérios aplicáveis ao PRD ou escopo do projeto; este arquivo não substitui as decisões do projeto. A numeração abaixo é uma convenção de referência e pode ser ajustada para evitar conflitos com regras existentes.

## Classificação e proveniência

- **RN-1 — Factual:** somente informação diretamente sustentada por fonte identificada e datada pode receber status `factual`.
- **RN-2 — Hipótese:** inferências úteis para orientar coleta recebem status `hipótese`; não podem aparecer como achado fechado, baseline, recomendação ou métrica final.
- **RN-3 — Pendente:** ausência de dado, ambiguidade ou divergência recebe status `pendente`, com pergunta objetiva e fonte/pessoa esperada para resolução.
- **RN-4 — Fonte:** todo documento analítico deve indicar fontes relevantes. Registre caminho relativo ou identificador da fonte, data e localização aproximada (página, seção, linha ou timestamp) sempre que disponíveis. A matriz de evidências cobre itens que possam mudar decisão, cálculo, risco ou entrega.
- **RN-5 — Contradição:** fontes conflitantes permanecem registradas; o documento não escolhe uma versão sem justificativa baseada em fonte oficial ou validação explícita.
- **RN-6 — Atualização:** ao entrar informação nova, atualize apenas os documentos impactados, a matriz de evidências quando aplicável e o registro de atualizações. Não sobrescreva histórico material sem registrar a mudança.
- **RN-6A — Escopo da propagação:** a matriz, o rastreador de lacunas, o changelog, o índice e o documento de domínio não precisam ser todos editados em toda rodada; atualize cada um quando a mudança o impactar e registre a razão quando um documento-raiz não for alterado.

## Qualidade da evidência por fonte

- **RN-7 — Fonte oficial vs. rascunho:** quando houver mais de uma resposta/versão de uma mesma pergunta (ex.: formulários preenchidos por pessoas diferentes, ou uma resposta finalizada vs. uma em rascunho), trate a versão **finalizada/oficial** como referência de fato, e use as chaves/campos originais do dado bruto — não force a numeração de um template diferente sobre o dado real só para "bater" com um índice.
- **RN-8 — Rascunho não é fato:** qualquer resposta ainda em rascunho, não finalizada ou não confirmada pelo respondente é histórica, não factual. Seus dados só podem gerar pendências ou perguntas de validação, nunca substituir a versão oficial.
- **RN-9 — Valores sentinela:** trate valores como `0001-01-01`, `-1`, `N/A`, nulos ou zeros como "não informado" somente quando a documentação do sistema ou o contexto da fonte confirmar que são placeholders. Nunca tome decisão com base num sentinela confirmado.
- **RN-10 — Estimativas:** valores marcados como estimativa devem preservar essa condição visivelmente e não podem compor cálculo final de COI/ROI ou virar baseline sem confirmação por registro real (sistema, log, export).
- **RN-10A — Unidade e escopo:** qualquer métrica ou estimativa deve preservar unidade, período, população/amostra, data de extração, fonte e denominador quando houver taxa. Valores monetários também precisam de moeda e critério de conversão. Um número sem esses elementos é uma lacuna, não um baseline.

## Avanço analítico (gates)

Estes gates existem para impedir que um documento pareça mais conclusivo do que os dados permitem. Nenhuma pressão de prazo justifica pular um gate — o documento correspondente fica como "modelo + lacunas" até o gate ser satisfeito.

- **RN-11 — AS-IS:** um processo pode ter AS-IS **preliminar** quando há descrição parcial, documentação ou relato da liderança, desde que o status e as limitações estejam explícitos. Só pode ser chamado de AS-IS **consolidado** depois de documentar gatilho, passos, handoffs, sistemas, responsáveis, saída, exceções e ao menos uma fonte operacional ou validação do responsável real (não só a liderança descrevendo de cima).
- **RN-12 — COI:** exige volume, esforço, pessoas envolvidas, periodicidade e premissa financeira/custo-hora confirmados ou claramente cenarizados como estimativa.
- **RN-13 — ROI:** exige baseline validado, custo total, hipótese de adoção, benefício mensurável, owner da medição e método de acompanhamento. Até então, manter somente o modelo e as lacunas.
- **RN-14 — Maturidade e benchmark:** um score de maturidade só é publicado quando cada dimensão tiver evidência documentada adequada ao escopo e à população. Autoavaliações são evidência do que cada respondente declara, não verificação independente de capacidade ou da maturidade da empresa. Um único respondente, a avaliação da liderança sobre a equipe ou uma amostra sem cobertura conhecida não basta. Preserve distribuição, tamanho da amostra e não respostas; benchmark externo requer fontes citáveis e comparáveis.
- **RN-15 — Priorização final:** quick wins e roadmap definitivo dependem de AS-IS, impacto, esforço, risco, dependências, responsável e critério de sucesso, todos presentes e comparáveis entre os itens. Antes disso, use apenas backlog de oportunidades **não priorizado** — mesmo que uma oportunidade pareça claramente mais urgente, resista a rankeá-la sem os critérios completos.
- **RN-16 — Recomendação de IA:** qualquer recomendação que afete cliente final, dados sensíveis, finanças ou publicação exige ponto de revisão humana definido; a entrega final ao cliente nunca é automatizada sem aprovação humana.
- **RN-17 — Caso observado:** um piloto, automação, ganho de produtividade ou sucesso de ferramenta em uma única amostra deve ser registrado como caso observado, com contexto e limitações. Não é baseline, recomendação replicável, prioridade final, COI ou ROI sem validação comparável.
- **RN-18 — Ausência:** diferencie ausência de evidência (a fonte não permite afirmar) de evidência de ausência (a fonte demonstra que algo não existe). A primeira gera pendência; não deve ser escrita como fato negativo.
- **RN-19 — Cliente-modelo:** material operacional real de um cliente do próprio cliente (uma conta, projeto ou unidade que ele atende) é evidência válida apenas para os processos, formatos e práticas que o cliente diagnosticado efetivamente executa nessa conta — nunca para o negócio próprio dessa conta fora desse domínio. Todo achado extraído desse material é `caso observado` por padrão (RN-17): descreva o processo do cliente diagnosticado como sujeito, citando a conta apenas como evidência/exemplo, nunca o inverso. Ver `references/evidencia-de-cliente-modelo.md`.
- **RN-20 — Minimização de dados:** registre somente os dados pessoais ou sensíveis necessários para sustentar a análise. Não reproduza credenciais, tokens ou segredos. Prefira agregação ou pseudonimização quando preservarem o contexto; não atribua resultados de grupos pequenos a pessoas ou áreas sem base e autorização adequadas.

## Casos de exceção recorrentes

| Cenário | Comportamento esperado |
|---|---|
| Nova fonte contradiz um documento existente | Registrar a contradição, rebaixar a conclusão afetada para `pendente` quando necessário, criar pergunta de validação. |
| Documento importado traz estimativa sem período ou fonte | Manter como estimativa; não usar em COI, ROI, benchmark ou priorização final. |
| Fonte descreve uma automação bem-sucedida em um caso isolado | Registrar como caso observado, não como recomendação replicável até avaliar contexto, risco e resultado mensurável em outros casos. |
| Processo foi descrito só pela liderança, nunca por quem executa | Criar AS-IS preliminar e marcar validação com operador/owner antes de considerá-lo consolidado (RN-11). |
| Dado de rascunho conflita com fonte oficial | Preservar o rascunho só como pendência; prevalece a fonte oficial até validação posterior (RN-7/RN-8). |
| Falta dado essencial para uma entrega | Atualizar o índice de entregáveis com bloqueio acionável, sem preencher a lacuna por suposição. |
| Uma única amostra mostra ganho de IA, automação ou tempo | Registrar como caso observado, documentar contexto e próxima validação; não generalizar nem fechar ROI (RN-17). |
| Nenhuma fonte menciona processo, ferramenta ou gargalo | Registrar como ausência de evidência e criar pergunta de coleta; não afirmar que o item não existe (RN-18). |
| Worktree já contém alterações antes da rodada | Registrar o estado inicial, preservar as alterações e comparar o diff final; não exigir limpeza nem atribuir tudo à rodada. |
| Fonte é material operacional real de um cliente do próprio cliente (cliente-modelo) | Descrever o processo do cliente diagnosticado como sujeito, citando a conta como caso observado (RN-17/RN-19); nunca usar o negócio próprio dessa conta, fora do domínio que o cliente diagnosticado entrega, como evidência sobre ele. Ver `evidencia-de-cliente-modelo.md`. |
| Exports ou relatos usam períodos, moedas ou populações diferentes | Preservar cada escopo e período; não somar ou comparar diretamente sem normalização demonstrável e critérios registrados. |
| Pesquisa tem poucos respondentes ou subgrupos identificáveis | Explicitar o tamanho da amostra e limitar a atribuição; usar agregação ou pseudonimização quando cabível (RN-20). |
| Autoavaliação usa itens opcionais, escalas ordinais ou diferentes versões | Preserve itens ausentes como ausentes, mantenha os rótulos e âncoras originais e compare versões apenas após justificar equivalência; não transforme respostas em média ou score sem método aprovado (RN-10A/RN-14). |

## Nota final

As regras adotadas precisam estar no PRD ou escopo do diagnóstico, com referências estáveis e citáveis. Adapte esta lista antes de usá-la e cite a regra correspondente quando ela justificar uma decisão de conteúdo. Não presuma que o projeto já adotou todas as extensões ou a numeração deste padrão.

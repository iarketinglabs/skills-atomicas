# Evidência de Cliente-Modelo

Às vezes a pasta de fontes definida pelo projeto contém, além do material direto sobre a empresa diagnosticada (entrevistas, formulários, reuniões), material operacional real de **uma conta, projeto ou unidade que ela atende ou opera**. Chame esse material de **evidência de cliente-modelo**. Ele pode chegar como um conjunto heterogêneo de artefatos reais (planos, relatórios, briefings, playbooks operacionais, exports de sistema, planilhas) — não como uma síntese ou uma entrevista sobre a empresa diagnosticada.

Use a pasta e o processo de ingestão definidos pelo projeto. Esta referência não escolhe onde o material é armazenado nem o reorganiza; ela define como minerá-lo com segurança quando uma rodada de refinamento o usa como fonte.

## Por que é diferente de uma fonte comum

Uma entrevista ou formulário fala **sobre** o cliente diagnosticado. Material de cliente-modelo é o rastro operacional de uma conta real — ele mostra o processo do cliente diagnosticado **em ação**, mas o sujeito documentado dentro dos próprios arquivos é a conta/cliente-modelo, não o cliente diagnosticado. Essa inversão de sujeito é a armadilha central deste tipo de fonte: é fácil, sem perceber, acabar documentando o cliente-modelo em vez do cliente diagnosticado.

## Regra de ouro: o processo é o sujeito, o cliente-modelo é a evidência

Ao redigir qualquer achado a partir desse material:

- A frase principal descreve **o processo, formato, cadência ou prática do cliente diagnosticado** (ex.: "a equipe audita a conta na entrada", "o relatório mensal segue o formato X").
- O cliente-modelo entra só como citação de exemplo/evidência — entre parênteses, em nota, ou na coluna de origem/fonte. Nunca como sujeito de uma frase do corpo do documento.
- Teste rápido: releia o parágrafo removendo o nome do cliente-modelo. Se a frase ainda faz sentido porque já descreve o processo em termos gerais, a formulação está correta. Se a frase só faz sentido com o nome do cliente-modelo dentro dela, reescreva.

Isso vale mesmo quando o material de cliente-modelo é a **única** fonte disponível para um processo — a ausência de outras fontes não licencia descrever o cliente-modelo em vez do cliente diagnosticado; ela só limita a confiança da generalização (ver "Status e governança", abaixo).

## Escopo: o que é evidência válida e o que não é

Nem todo conteúdo de uma pasta de cliente-modelo é evidência sobre o cliente diagnosticado.

- **É evidência válida:** qualquer processo, formato, cadência, artefato ou prática que a **empresa diagnosticada executa ao atender ou operar essa conta** — como planeja, monitora, relata, atende, produz ou entrega para ela. Isso pode informar o AS-IS da empresa diagnosticada, com os limites de amostra descritos abaixo.
- **Não é evidência sobre a empresa diagnosticada:** o próprio negócio, funil, produto ou problema operacional da conta-modelo fora do domínio que a empresa diagnosticada entrega. Ex.: se a empresa diagnosticada presta um serviço de mídia para uma conta, o funil comercial interno dessa conta não é evidência sobre o processo da prestadora.

Quando a fronteira não for óbvia, pergunte: "isso descreve algo que o cliente diagnosticado faz, ou algo que o cliente-modelo faz por conta própria?" Só o primeiro entra na base.

## Mídia (imagem, vídeo, áudio)

Material de cliente-modelo costuma incluir grandes volumes de peças criativas, gravações e fotos. Esta skill mina apenas arquivos de texto e dados (documentos, planilhas, apresentações, PDFs, CSVs, markdown). Arquivos de imagem, vídeo e áudio são **reconhecidos como existentes** (liste-os, entenda em que pasta/contexto vivem) mas **não têm o conteúdo analisado** — não descreva o que aparece numa peça, apenas que ela existe e onde. Se o usuário precisar do conteúdo desses arquivos, isso é um pedido explícito à parte, fora desta skill.

## Status e governança

- Todo achado derivado de material de cliente-modelo é, por padrão, `caso observado` (RN-17/RN-19) — evidência real, mas de uma única conta/amostra. Não vira baseline, prática padronizada da empresa, COI, ROI ou recomendação sem confirmação em mais de uma conta.
- Cite a origem exata do arquivo (caminho relativo) como faria com qualquer outra fonte (RN-4).
- Minimize dados pessoais, credenciais e detalhes confidenciais da conta-modelo; retenha somente o contexto necessário para sustentar o achado.
- Quando o achado corrobora algo já descrito de forma genérica num documento existente (ex.: um AS-IS preliminar baseado só em entrevista de liderança), registre isso como reforço do *formato* do processo — não como promoção do AS-IS de preliminar para consolidado. A validação com o executor real continua exigida por RN-11; uma conta bem documentada corrobora, mas não substitui essa validação.
- Se contas-modelo comparáveis confirmarem o mesmo padrão, registre quais amostras e critérios de comparação sustentam a leitura. A repetição em amostras não substitui validação com quem executa nem, por si só, transforma o padrão em baseline.

## Numeração segura ao propagar

Material de cliente-modelo costuma ser volumoso e gerar várias evidências/lacunas novas na mesma rodada — e é comum que outra rodada de refinamento esteja em andamento em paralelo sobre outra pasta. Antes de atribuir os próximos IDs de `EV-` ou `LC-`, confira o maior número **já em uso em toda a árvore** (não só nos arquivos que você leu no início da rodada) — outro processo pode ter alterado a matriz ou o rastreador de lacunas entre a sua leitura e a sua escrita. Se detectar uma colisão só depois de escrever, renumere o seu bloco e registre no changelog que a renumeração aconteceu por causa de uma rodada concorrente — não é erro, é o comportamento esperado quando duas rodadas avançam ao mesmo tempo.

## Checklist de execução

- [ ] Identifiquei quais arquivos são texto/dados (minerados) e quais são imagem/vídeo/áudio (apenas registrados como existentes).
- [ ] Cada achado descreve o processo do cliente diagnosticado como sujeito; o cliente-modelo aparece só como evidência citada (teste: a frase sobrevive sem o nome do cliente-modelo?).
- [ ] Nenhum achado usa o negócio próprio do cliente-modelo (fora do domínio de entrega do cliente diagnosticado) como evidência sobre o cliente diagnosticado.
- [ ] Todo achado está marcado `caso observado` (RN-17/RN-19), com fonte exata.
- [ ] Nenhum AS-IS foi promovido de preliminar a consolidado só por causa deste material.
- [ ] Conferi o maior ID de `EV-`/`LC-` em uso na árvore inteira imediatamente antes de propagar, não apenas nos arquivos lidos no início da rodada.
- [ ] Segui, para o resto da execução, o passo a passo de `metodologia-rodadas-refinamento.md`.

# Mineração de Dados de CRM/Pipeline

Às vezes a pasta de fontes definida pelo projeto contém uma **exportação bruta de CRM ou pipeline comercial** da própria empresa diagnosticada — dados estruturados sobre oportunidades, leads, contas ou negócios, não uma entrevista ou formulário sobre o processo comercial. Este arquivo descreve como minerar esse tipo de fonte com segurança quando uma rodada de refinamento a usa.

Isso é diferente de evidência de cliente-modelo (`evidencia-de-cliente-modelo.md`): um export do próprio CRM/pipeline do cliente diagnosticado é evidência de primeira mão sobre o processo dele mesmo — `factual`, sujeito a RN-1/RN-4 como qualquer outra fonte primária, não a RN-17/RN-19. (Se o export pertencer a uma conta que o cliente diagnosticado atende, não a ele próprio, trate como cliente-modelo em vez de seguir este arquivo.)

## Por que exige tratamento próprio

Um export estruturado (CSV/XLSX/JSON de um sistema) já "parece" quantitativo — isso cria uma tentação de amostrar algumas linhas e escrever frases de aparência analítica ("a maioria fecha", "poucos ficam parados") em vez de computar o agregado real. Um número impreciso carrega mais autoridade implícita do que uma citação de entrevista malfeita, porque parece evidência mais dura do que é. A mesma exigência de RN-1/RN-4 (toda afirmação factual precisa de fonte específica) vale aqui, mas o risco de violá-la sem perceber é maior.

## Como minerar corretamente

1. **Leia o export inteiro** — todas as linhas e colunas do schema. Para arquivos grandes, use agregação reproduzível ou leitura paralela somente-leitura quando as ferramentas e regras da sessão permitirem. Todo número que entrar na base documental precisa ser reproduzível reexecutando o mesmo cálculo.
2. **Mapeie o schema e a janela temporal antes de interpretar.** Registre a data de extração, os períodos cobertos por cada export, o que cada linha representa, etapas/status usados e definidos, campos de qualificação e valores ausentes. Não assuma o significado de uma etapa pelo nome; examine os registros e os campos relacionados. Quando vários exports cobrirem períodos diferentes, não os trate como snapshots simultâneos nem compare contagens sem alinhar escopo e período.
3. **Toda taxa/percentual cita o denominador exato** ("X de Y registros têm o campo Z preenchido", "N de M chegaram a uma decisão"). Um percentual sem denominador declarado não é evidência utilizável (RN-4, RN-10A).
4. **Cruze cada achado quantitativo com a evidência narrativa já existente** (citações de entrevista, estimativas relatadas). Divergência é esperada e valiosa — registre as duas versões lado a lado como lacuna de reconciliação (RN-5); nunca prefira silenciosamente o número bruto sobre o relato, nem o contrário.
5. **Sinalize qualquer entidade nova que o export revelar e que não existe em nenhuma outra fonte** (uma ferramenta integrada, uma pessoa, um canal, uma etapa nunca descrita) como evidência e lacuna explícitas — não a absorva silenciosamente numa frase como se já fosse contexto conhecido.
6. **Preserve os rótulos originais e documente normalizações.** Se agrupar variações de grafia ou categorias, informe a regra usada e mantenha os valores originais recuperáveis. Campo vazio, zero, placeholder e campo inexistente têm significados distintos; só trate placeholders conforme a documentação da fonte.

## Dois documentos, não um

Quando a mineração for rica o suficiente para virar entrega, separe sempre em pelo menos dois documentos distintos na pasta da área correspondente — não misture os dois papéis num único arquivo:

1. **Relatório de performance histórica.** Insights e métricas derivados do histórico completo do export (volume, resultado, valor, distribuição, tempo por etapa quando o dado permitir). É sempre leitura **histórica (all time)** dos registros existentes até a data do export — nunca deve ser enquadrado como "estado atual do pipeline em aberto agora". Um retrato do "agora" exigiria uma fonte viva/conectada, não um export estático.
2. **Documentação de processo.** A estrutura reconstruída a partir do schema: como o sistema representa aquisição de novos negócios ("hunting" ou termo equivalente do cliente) e como representa expansão/retenção de contas existentes ("farming": upsell, cross-sell, renovação) — campos, etapas, regras observadas, papel de cada ferramenta/integração citada nos registros. Não repete os números do relatório de performance; documenta a estrutura, não o resultado.

Um único documento tende a misturar "o que o número diz" com "como o sistema funciona", dificultando tanto a leitura quanto a atualização isolada de cada um numa rodada futura.

## Propagação

Segue o mesmo fluxo de qualquer rodada (`metodologia-rodadas-refinamento.md`, Passo 6), com dois pontos específicos deste tipo de fonte:

- Se um documento existente (README da área, gargalos-e-evidências, lacunas, roteiro de coleta) já registrava como lacuna "extrair/exportar o CRM", e a mineração acabou de fazer exatamente isso, **atualize a lacuna para refletir o que passou a faltar de fato** (reconciliação com registros reais, validação de unidade/moeda/critério) — não a apague nem a deixe pedindo algo que já foi entregue.
- Toda evidência quantitativa nova relevante para decisão, risco ou entrega vai para a matriz de evidências como `factual` (é dado direto do próprio sistema do cliente diagnosticado) — mas sua leitura como taxa/baseline validado permanece `pendente` até reconciliação (RN-10).

## Gates que continuam valendo

- Uma taxa de conversão, tempo médio de ciclo ou valor agregado calculado direto do export é uma contagem factual sobre os registros existentes — não é, por si só, um baseline validado de COI/ROI (RN-10, RN-12, RN-13) até reconciliar com o processo real e confirmar unidade/período/moeda/escopo.
- Colunas de "tempo em cada status", quando o sistema as fornece, são descritivas do histórico observado, não uma medição de SLA validada — reporte média e mediana juntas (a média sozinha distorce com poucos registros antigos/outliers) e trate como sinal a investigar, não como meta.
- Um campo numérico sem unidade/moeda/escopo geográfico explícito nunca deve ser somado entre populações diferentes sem declarar a limitação. Separe moeda presente na fonte de moeda inferida por contexto e registre qualquer conversão e sua fonte (RN-9, RN-10A).

## Checklist de execução

- [ ] O export foi lido/computado por completo, não amostrado — todo número citado é reproduzível.
- [ ] A data de extração e o período coberto por cada export estão identificados; populações e snapshots não comparáveis estão separados.
- [ ] Todo percentual/taxa cita o denominador exato.
- [ ] Toda divergência com evidência narrativa já existente foi registrada lado a lado, não resolvida por preferência.
- [ ] Toda entidade nova (ferramenta, pessoa, canal) revelada pelo export e ausente em outras fontes está sinalizada como lacuna, não absorvida silenciosamente.
- [ ] Performance histórica e documentação de processo estão em documentos separados.
- [ ] Nenhum trecho do relatório de performance sugere "estado atual do pipeline" — é sempre leitura histórica.
- [ ] Nenhum COI/ROI/baseline foi fechado a partir de contagens não reconciliadas.
- [ ] Unidades, moedas, placeholders, campos ausentes e regras de normalização estão documentados antes de somar ou comparar valores.
- [ ] Lacunas que pediam "extrair o export" foram atualizadas para o que falta agora, não deixadas como se o export ainda não existisse.

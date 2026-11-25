# Padrões de Pipeline e Armazenamento

## Ingestão e Transporte

- **Batch:** processa um conjunto em intervalos. É simples de repetir e adequado quando a janela de atraso é tolerável.
- **Streaming:** processa eventos continuamente ou em micro-lotes. Use quando a latência requerida justifica estado, checkpoints, monitorização e recuperação contínua.
- **CDC:** transmite inserções, actualizações e, conforme a fonte/configuração, eliminações a partir do registo de alterações. Documente posição, ordenação, deletes, snapshot inicial, retenção do log e comportamento após indisponibilidade.
- **API/fichas/ficheiros:** preserve cursor, checksum, versão, origem, timestamp, formato e resultado de cada extracção. Não assuma que uma exportação incremental inclui correcções antigas.

Escolha a menor frequência que cumpre a decisão de negócio. “Tempo real” é uma exigência mensurável de frescura, não um atributo decorativo.

## ETL, ELT e Camadas

ETL transforma antes do destino analítico; ELT carrega dados antes de os transformar no destino. A decisão depende de privacidade, volume, custos de transferência, capacidade do destino, necessidade de reter bruto e regras de acesso. Um padrão de camadas (por exemplo, bruto, validado e servido) pode facilitar reprocessamento e auditoria, mas não é requisito universal.

Para cada camada, declare o que pode ser lido, alterado, retido e reprocessado. Dados brutos não são automaticamente seguros ou fiáveis: classifique-os, limite acesso e documente a origem.

## Estado e Modelação

- Defina o grão antes de desenhar factos, dimensões, tabelas agregadas ou eventos.
- Mantenha chaves de negócio e técnicas distintas quando isso clarificar identidade e histórico.
- Torne explícita a semântica de snapshots, upserts, deletes, validade temporal e correcções retroactivas.
- Use incrementalização apenas quando a regra de mudança for correcta; defina chave de deduplicação, watermark, janela de atraso, reconciliação e estratégia de backfill.
- Separe o modelo operacional do analítico quando padrões de consulta, concorrência, retenção ou escala criarem interferência relevante.

Modelos dimensionais, normalizados ou orientados a histórico resolvem necessidades diferentes. Podem coexistir em camadas distintas; não misture granularidades silenciosamente.

## Orquestração e Execução Distribuída

Orquestre dependências, janelas, tentativas, estados parciais, limites de concorrência, alertas e recuperação. Registe identificador de execução, partições, versão de código/schema, posição de origem e contagens de entrada/saída. Uma tentativa repetida deve ser idempotente ou ter deduplicação explícita.

Em compute distribuído, estime custo de movimento entre workers, skew de chaves, cardinalidade e materialização. Meça planos e etapas reais antes de optimizar. Mais paralelismo pode aumentar contenção, shuffle e custo sem reduzir o tempo final.

## Formatos e Portabilidade

Formatos abertos podem reduzir dependência no armazenamento e metadados; não garantem portabilidade de catálogo, permissões, SQL, optimizações, transacções ou operação. Compare versões de formato, catálogos, engines, compatibilidade e caminho de exportação. Valide a combinação real de leitores e escritores que o projecto precisa.

## Zero-ETL e Serviços Geridos

Trate “zero-ETL” como redução da manutenção manual, salvo se a documentação demonstrar o contrário. Confirme o que continua a existir: captura, staging, checkpoints, estado, retries, metadados, custo de transferência, monitorização e recuperação.

Serviço gerido muda quem opera componentes; não elimina contratos, permissões, limites, incidentes, custos ou dependência do fornecedor.

## Custo e Falhas

Meça armazenamento, compute ocioso e activo, egress, scans, retenção, retries, ambientes de desenvolvimento, cópias e custo de falha. Compare o custo por resultado aceite, incluindo atraso ou corrupção evitada. Preserve raw data apenas durante a janela aprovada e com acesso limitado.

Teste ao menos os modos de falha pertinentes: fonte indisponível, partição ausente, schema incompatível, duplicado, evento atrasado, destino parcialmente escrito, retry, backfill, segredo expirado e esgotamento de cota. Para políticas de resiliência do sistema, consulte a skill irmã apropriada se existir.

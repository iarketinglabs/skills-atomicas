# Qualidade, Contratos e Governança

## Produto e Contrato

Um produto de dados tem consumidores, interface estável, proprietário, finalidade e critério de qualidade. Um contrato de dados deve comunicar o mínimo necessário para produtores e consumidores evoluírem sem ambiguidade:

- nome, versão, finalidade, produtor, proprietário e consumidores;
- campos, tipos, nulabilidade, unidades, descrição e classificação;
- chaves, granularidade, ordem temporal, semântica de deletes/correcções;
- frescura e disponibilidade esperadas;
- regras de compatibilidade e processo para alterações;
- controlos de acesso, retenção, eliminação e proveniência;
- verificações, limites de aceitação e procedimento de incidente.

Use `assets/data-contract.schema.json` como ponto de partida interoperável. Não confunda schema técnico com acordo de significado, qualidade ou autorização.

## Portfólio de Verificações

Seleccione verificações ligadas ao risco e ao consumidor:

| Dimensão | Exemplos de verificação |
|---|---|
| Estrutura | Tipos, campos obrigatórios, compatibilidade e versão do schema |
| Completude | Campos-chave não nulos; partições e fontes esperadas presentes |
| Unicidade | Chave de negócio ou de evento única dentro da janela declarada |
| Integridade | Referências válidas, relações entre entidades e reconciliação de contagens/valores |
| Domínio | Enumerações, intervalos, unidades e regras de negócio confirmadas |
| Tempo | Frescura, atraso, cobertura de janelas, ordem, timezone e período sem dados |
| Distribuição | Mudanças de volume, frequência, cardinalidade, valores e categorias raras |
| Privacidade | Campos classificados, minimização, acesso, retenção, eliminação e rastreio |
| Consumo | Métricas semânticas estáveis, linhagem visível e permissões aplicadas |

Defina para cada regra: owner, severidade, janela/população, método, threshold, tolerância, destino do alerta e acção. Não imponha um limite sem baseline ou custo de erro conhecido. Para dados financeiros, de segurança ou regulados, adicione reconciliação independente e evidência de execução.

## Tempo e Evolução

Distinga tempo do evento, tempo da fonte, tempo de ingestão e tempo de processamento. Especifique como corrigir uma partição antiga, voltar a processar eventos, tratar deletes e impedir regressão de versão. Um teste de snapshot não demonstra comportamento correcto sob atraso, duplicação ou mudança ao longo do tempo.

Use mudanças aditivas e compatíveis quando possível. Se uma mudança quebrar contrato, identifique consumidores, período de transição, versão paralela, migração, validação e data de remoção. Não execute backfill destrutivo sem cópia/recovery adequada e aprovação prevista pelo ambiente.

## Ownership, Linhagem e Acesso

Registe origem, transformações, versão, dependências, consumidores, última validação e owner. Para cada leitor ou agente, especifique finalidade, escopo de linhas/colunas, duração, volume e forma de revogação. Implemente autorização numa fronteira determinística: política, identidade e validação não devem depender apenas do prompt ou do filtro que o agente escolheu.

Classifique dados sensíveis e aplique minimização, pseudonimização/anonimização quando adequadas, retenção limitada, eliminação verificável e registo sem payload sensível. Dados derivados e embeddings também podem revelar informação de origem.

## Incidente de Dados

Quando uma regra falhar, registe activo e partição afectados, intervalo, consumidores, proveniência, severidade, detecção, contenção, correcção, backfill e validação. Preserve evidência útil sem copiar segredos ou dados pessoais. Converta o incidente em contrato, alerta ou regressão verificável.

Para regras legais, privacidade ou requisitos do sector, valide a jurisdição, a data e a fonte oficial aplicáveis. Uma arquitectura tecnicamente correcta não prova conformidade legal.

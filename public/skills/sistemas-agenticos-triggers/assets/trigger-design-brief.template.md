# Brief de desenho de trigger

> Copie este modelo para o sistema em análise. Escreva `por confirmar` quando faltar evidência e identifique requisito, decisão e hipótese separadamente. Não inclua segredos nem dados pessoais reais.

## Resultado

- Resultado de negócio/operacional:
- O que deve iniciar e qual o efeito esperado:
- Critérios de sucesso observáveis:
- Dentro e fora do escopo:
- Responsável pelo fluxo e pelo destino:

## Sinal e semântica

- Origem/fonte de verdade e owner:
- Tipo: evento, transição, condição, ausência, horário ou consulta:
- Condição exata de disparo e de cancelamento:
- Identidade do sinal/entidade e âmbito de unicidade:
- Instante de ocorrência vs instante de observação:
- O que representa um evento novo, duplicado, tardio ou fora de ordem:

## Requisitos

| Dimensão | Requisito | Evidência/owner |
|---|---|---|
| Frescura/latência | | |
| Volume, cardinalidade e rajadas | | |
| Completude, ordem e consistência | | |
| Disponibilidade e rede | | |
| Limites, custo e operação | | |
| Sensibilidade e retenção de dados | | |
| Impacto e reversibilidade do efeito | | |

## Padrão e contrato

- Padrão considerado: push, webhook/broker, polling, agendamento, CDC, condição/ausência, híbrido:
- Alternativas avaliadas e por que não foram escolhidas:
- Contrato/schema e versão:
- Payload magro ou conteúdo completo; justificativa:
- ID, chave de deduplicação e chave de efeito:
- Autenticação, autorização, validação e confirmação:
- Garantias documentadas por fronteira:

## Execução e controlo

- Estados de trabalho e persistência:
- Timeout, retentativas, backoff e erros permanentes:
- Concorrência, backpressure e limites por tarefa:
- Replay, backfill, reconciliação e compensação:
- Dados não confiáveis e políticas de contexto (se houver IA):
- Ferramentas/escopos autorizados:
- Aprovação humana, pausa, expiração e retomada:
- Kill switch ou caminho de desativação:

## Operação e prova

- Logs, métricas, traces e redação de dados:
- Alertas de atraso, ausência, fila e custo:
- DLQ/quarentena e responsável pela triagem:
- Cenários de aceite e evidência direta do estado/efeito:
- Lançamento gradual, rollback e plano de recuperação:
- Hipóteses, lacunas e data das fontes que podem mudar:

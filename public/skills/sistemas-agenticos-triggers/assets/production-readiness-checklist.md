# Checklist de prontidão de trigger

Use como checklist de revisão. Adapte ao risco e anexe evidência observável. Um item sem aplicabilidade deve ter justificativa, não ficar silenciosamente vazio.

## Contrato e sinal

- [ ] A condição de início, cancelamento e repetição está definida sem ambiguidade.
- [ ] A fonte de verdade, o owner e os requisitos de frescura/completude estão registados.
- [ ] ID, versão, timestamp, entidade e schema têm semântica documentada.
- [ ] Duplicados, atraso, reordenação, payload desconhecido e deletes têm comportamento definido.
- [ ] As garantias da origem e da versão/configuração ativas foram confirmadas.

## Execução e confiabilidade

- [ ] Um evento aceite ou janela agendada fica durável antes da confirmação apropriada.
- [ ] Chaves de deduplicação e idempotência cobrem retries e efeitos externos.
- [ ] Timeout, retentativa segura, erros permanentes e resultado incerto têm caminhos definidos.
- [ ] Concorrência, sobreposição e rajadas têm limites adequados.
- [ ] DLQ/quarentena tem alerta, responsável, retenção e processo de triagem.
- [ ] Replay/backfill verifica estado e autorização antes de efeitos; a ação é auditável.
- [ ] Polling persiste cursor; agendamento persiste janela lógica e política de atraso/fuso.

## Segurança e dados

- [ ] Autenticidade, autorização, schema, Content-Type, tamanho e taxa são verificados.
- [ ] Segredos podem ser rodados e revogados; URLs/destinos configuráveis têm defesa SSRF.
- [ ] Conteúdo externo é tratado como dado não confiável; permissões são impostas fora do modelo.
- [ ] Efeitos sensíveis têm gate humano ou justificativa de política proporcional ao risco.
- [ ] Logs, traces e retenção minimizam payload, credenciais e dados pessoais.
- [ ] Existe caminho praticado para pausar o fluxo e revogar capacidade de agir.

## Operação e aceite

- [ ] Recebimento, atraso, ausência de progresso, falha, repetição e recuperação são observáveis.
- [ ] Há alertas com owner e limiares ligados ao impacto/requisito.
- [ ] Cenários de falha e recuperação foram exercitados no ambiente apropriado.
- [ ] O estado final e os efeitos foram verificados diretamente, não só pela resposta do agente.
- [ ] Responsáveis, plano de lançamento, rollback e runbook estão definidos.
- [ ] Hipóteses, limites e dependências de versão estão explícitos.

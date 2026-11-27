# Runbook de incidente de trigger

> Copie e preencha por fluxo. Não coloque tokens, URLs com segredo ou payload sensível neste documento.

## Identificação

- Nome do fluxo e owner:
- Ambiente e versão/regra ativa:
- Sinais de alerta e severidade:
- Canal e responsável de plantão:
- Caminho seguro para pausar, limitar ou revogar:

## Sintoma

- Início, janela e impacto observado:
- Eventos/entidades/janelas potencialmente afetados:
- Métricas, IDs de correlação e traces relevantes:
- O que se sabe e o que ainda é hipótese:

## Conter e diagnosticar

1. Determine se a origem continua a produzir sinais e se o consumidor os recebe, persiste e inicia.
2. Verifique autenticação, schema, cursor/janela, fila, dependência, limite, timeout e versão ativa.
3. Se houver risco de efeito duplicado ou não autorizado, pause antes de retentar ou reproduzir.
4. Preserve IDs e metadados de diagnóstico; limite acesso a payloads e segredos.
5. Identifique a fronteira causal: origem, transporte, receção, agendamento, política, ferramenta/destino ou observabilidade.

## Recuperar

- Condição para retomar e pessoa que decide:
- Verificação de estado antes de retry/replay:
- Escopo de reconciliação/backfill e chave de idempotência usada:
- Efeitos que exigem aprovação/compensação:
- Como validar contagem, completude e ausência de duplicados:
- Critério de encerramento e evidência guardada:

## Seguimento

- Causa confirmada e limites da evidência:
- Ação corretiva, owner e data:
- Regressão/cenário adicionado:
- Alterações a alertas, runbook, contrato ou configuração:

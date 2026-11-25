# Checklist de prontidão de deploy

Marque cada item como concluído, pendente ou não aplicável. Registe evidência e responsável para itens pendentes.

## Escopo e ownership

- [ ] Serviço, ambiente, região e alvo de deploy foram confirmados.
- [ ] Owner técnico e responsável operacional estão identificados.
- [ ] Mudanças incluídas e fora de escopo estão documentadas.
- [ ] Dependências e integrações externas foram enumeradas.

## Segurança e acesso

- [ ] Identidades e permissões têm escopo mínimo necessário.
- [ ] Credenciais não aparecem em código, logs, imagens ou artefatos.
- [ ] Portas e interfaces administrativas estão limitadas ao necessário.
- [ ] Dados em logs, traces e backups têm classificação, acesso e retenção definidos.
- [ ] Ações automatizadas têm limites, auditoria e condição de interrupção.

## Dados e recuperação

- [ ] Persistência e migrações são compatíveis com a versão a publicar.
- [ ] Backup foi realizado ou o impacto de não o realizar foi aceito pelo responsável.
- [ ] Restore foi demonstrado para a classe de falha relevante.
- [ ] RPO, RTO e perda aceitável estão confirmados.
- [ ] Rollback ou recuperação progressiva está documentado.

## Capacidade e custo

- [ ] Requests, limits, quotas, concorrência e filas correspondem ao workload.
- [ ] Dependências e limites externos foram verificados.
- [ ] Sinais de saturação, custo e teto de expansão estão configurados.
- [ ] Storage, snapshots, tráfego de saída e retenção foram considerados.

## Observabilidade e operação

- [ ] Health checks verificam as dependências necessárias.
- [ ] Métricas, logs ou traces permitem confirmar o resultado fim a fim.
- [ ] Alertas têm impacto, responsável e próximo passo.
- [ ] Logs e traces não capturam payload sensível sem necessidade e controle.
- [ ] Runbook e caminho de escalonamento estão disponíveis.

## Rollout e encerramento

- [ ] Pré-condições e estado anterior foram registados.
- [ ] Critérios de sucesso e condições de parada são observáveis.
- [ ] Janela e partes afetadas foram informadas conforme o processo aplicável.
- [ ] DNS, certificado e cache foram considerados, se aplicável.
- [ ] A validação após deploy foi atribuída a alguém.
- [ ] O ambiente anterior só será removido depois da janela de segurança definida.

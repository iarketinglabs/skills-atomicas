# Segurança de GitHub, CI e cadeia de entrega

## Princípios

- Aplique privilégio mínimo por workflow e por job. Declare as permissões necessárias para o token em vez de depender de defaults amplos.
- Separe jobs que processam conteúdo não confiável de jobs que usam secrets, tokens de escrita ou credenciais de deploy.
- Prefira credenciais curtas e federadas, como OIDC, a segredos estáticos quando a integração suportar essa opção. Restrinja a política de confiança por repositório, ambiente e workflow esperado.
- Fixe dependências externas de workflows a revisões imutáveis quando a política de segurança o exigir; mantenha um processo deliberado para atualizar e rever essas revisões.
- Use lockfiles e verificação de integridade quando disponíveis. Para artefactos assinados ou com atestação, valide a identidade de origem, o workflow e o digest do artefacto no momento de consumo; a presença de uma assinatura, etiqueta ou atestação, por si só, não prova confiança.
- Não guarde segredos em Git, exemplos, ficheiros de instruções, skills, issues ou logs. Mascaramento automático não garante que valores transformados sejam ocultados.
- Verifique permissões de runners, Actions permitidas, artefactos, caches, ambientes e bypasses de rulesets. O nome de um check verde não prova que executou sobre o commit atual.

## Pull requests de forks e código não confiável

Considere o código, workflows, scripts de build, testes, dependências e artefactos de uma contribuição externa como executáveis não confiáveis.

No GitHub Actions, `pull_request_target` usa o contexto confiável da branch base e pode ter acesso a tokens e secrets do repositório. Não faça checkout do head/merge commit de um fork e não execute o seu código nesse job privilegiado. Para validar conteúdo de PRs externos, use um evento/job com privilégios limitados e sem segredos; se um processo privilegiado tiver de reagir depois, transfira apenas dados validados e não executáveis para uma etapa separada.

Antes de alterar um workflow, confirme evento, origem do workflow, referência em checkout, permissões efetivas e passos que executam código. Inspecione também ações de terceiros e scripts de dependências.

## Trabalho com automação ou agentes

Quando a automação interpreta issues, PRs ou ficheiros do repositório:

- limite os repositórios, paths, comandos, rede e permissões ao mínimo;
- mantenha jobs de análise sem escrita e use etapas determinísticas com aprovação para publicar;
- aplique gates fora da instrução em linguagem natural: checks obrigatórios, revisão humana e proteção de refs;
- exija aprovação adicional para alterações a workflows, permissões, regras, skills ou instruções que governam agentes;
- preserve logs independentes dos eventos relevantes, sem registar segredos;
- não permita que o agente altere as próprias restrições e aprove ou publique a alteração na mesma operação.

## Se um segredo aparecer no diff

Não o reproduza em mensagens, comandos ou relatórios. Pare a publicação desse conteúdo. Informe apenas o caminho e o tipo de exposição, sem valor. A rotação/revogação do segredo é prioritária; a remoção do histórico exige um plano coordenado e não substitui a rotação. Siga o processo de resposta a incidentes da organização.

## Disponibilidade de controlos

Rulesets, branch protection, code scanning, secret scanning, merge queues, ambientes, attestation e políticas de Actions podem depender da edição, permissões, configuração ou fornecedor. Confirme o que está efetivamente ativo; não infira enforcement a partir de um ficheiro de configuração isolado ou de uma página de produto.

# Domínios, DNS, TLS e VPS

Use esta referência para preparar configuração ou mudança de domínio, publicação de serviço e operação de um servidor virtual. Detalhes de painel, API, limites e recuperação variam por registrador e provedor; confirme na documentação atual.

## Domínio e DNS

Distinga o titular do domínio, registrador, registry do domínio de topo, operador de DNS autoritativo e resolvedores recursivos. Confirme quem controla cada conta, MFA, dados de recuperação, renovação, transfer lock, nameservers e pagamento.

Antes de alterar registros:

1. registe a zona atual e exporte uma cópia revisável;
2. confirme domínio, conta, ambiente, alvo e owner;
3. identifique A/AAAA, CNAME, MX, TXT, CAA, NS, SRV e registros relevantes existentes;
4. verifique TTL, cache, DNSSEC, dependências de email, validações e certificados;
5. prepare janela, monitorização, critério de sucesso e caminho de reversão;
6. valide a resolução em mais de um resolvedor e o serviço fim a fim.

TTL influencia cache, mas não garante propagação instantânea ou simultânea em todos os resolvedores. Uma migração pode deixar clientes a usar dados antigos durante a transição. Preserve registros não relacionados e evite trocar nameservers sem inventário e plano de retorno.

## TLS e certificados

Use TLS para proteger a conexão e automatize emissão e renovação quando apropriado. Valide cadeia, hostname, validade, mecanismo ACME, acesso aos desafios, limites da CA, CAA e alertas de expiração. Teste renovação e confirme que a automação pode alcançar o serviço e atualizar o certificado ativo.

## VPS e servidores geridos por quem os usa

Antes de publicar, confirme ownership, sistema suportado, acesso administrativo, atualizações, firewall, portas, backups, monitorização e responsável operacional. Práticas de base:

- use contas individuais ou identidade de workload e acesso administrativo limitado;
- prefira autenticação forte e remova acesso obsoleto;
- abra apenas portas necessárias e restrinja superfícies administrativas;
- aplique atualizações de segurança com plano de reboot e validação;
- proteja credenciais e configure logs e métricas de disco, memória e disponibilidade;
- mantenha backups fora do domínio de falha e teste restore;
- monitore renovação TLS, espaço, expiração de domínio e tentativas anormais;
- documente reconstrução, acesso de emergência e migração de saída.

## Publicação e rollback

Valide o serviço localmente e em ambiente apropriado antes de apontar tráfego. Faça a mudança por etapas quando possível: DNS de teste ou hostname temporário, certificado, health check, mudança de tráfego, observação e encerramento controlado do ambiente antigo. Defina previamente como voltar ao alvo anterior e por quanto tempo ele ficará disponível.

Não presuma que SLA cobre erro de configuração, perda de dados, DNS, tráfego de saída ou migração. Confira o contrato atual e planeje continuidade independentemente dos créditos previstos.

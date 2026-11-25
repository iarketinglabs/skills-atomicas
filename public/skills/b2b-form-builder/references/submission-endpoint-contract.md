# Contrato do endpoint de envio

Implemente este contrato no backend antes de ativar o formulário público. Um endpoint serverless continua público e pode ser chamado diretamente; a existência de uma Edge Function ou uma regra CORS não basta para o proteger.

## Entrada

- Aceite apenas HTTPS e POST com Content-Type application/json.
- Rejeite corpos acima do limite definido para o formulário (por exemplo, 64 KiB) antes de interpretar o JSON.
- Valide um slug de formulário em allowlist do lado do servidor. Não use o slug recebido pelo browser para escolher tabela, função ou destino sem validação.
- Valide um esquema específico, tipos, comprimentos, número máximo de itens e campos permitidos. Rejeite campos desconhecidos.
- Gere o ID e a data de envio no servidor. Não aceite do browser status, timestamps, nome de tabela, SQL, URL de destino ou identificador de linha.
- Remova campos desnecessários, como URL da página, user-agent e contactos que não tenham finalidade documentada.

## Controles contra abuso

- Configure limite de taxa num gateway/CDN que use metadados de IP fornecidos por infraestrutura confiável. Não confie em X-Forwarded-For enviado diretamente pelo cliente.
- Use um mecanismo antiautomação, como um desafio validado no servidor, quando o risco o justificar. O segredo do provedor fica no ambiente server-side.
- Configure CORS apenas para os domínios esperados e não trate Origin como autenticação: scripts fora do browser podem falsificar cabeçalhos.
- Não habilite o endpoint até que validação, limite de taxa, política de retenção e alertas estejam configurados e testados.

## Persistência e resposta

- Mantenha a service_role apenas como segredo do ambiente de servidor; nunca a envie ao browser.
- Grave somente os campos permitidos numa tabela com RLS ativa e sem policies para anon ou authenticated.
- Retorne uma confirmação genérica, sem dados, IDs reutilizáveis, mensagens do banco ou conteúdo da resposta.
- Registe apenas metadados mínimos de operação. Nunca escreva corpos, respostas pessoais, tokens ou cabeçalhos de autorização em logs.
- Defina prazo de retenção, processo de eliminação e acesso interno por função antes do primeiro envio real.

## Revisão antes de publicar

- Teste slug desconhecido, JSON inválido, campos extras, tipos errados, corpo excessivo, repetição em alta frequência e falhas do banco.
- Confirme que o browser não pode ler, atualizar nem apagar linhas.
- Confirme que segredos e respostas não aparecem na rede pública, bundle, console, logs de build ou histórico Git.
- Use apenas dados sintéticos nos testes e no repositório público.

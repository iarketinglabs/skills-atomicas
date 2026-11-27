# Segurança de webhooks e fronteiras HTTP

Um webhook é uma entrada remota que pode iniciar efeitos. Trate autenticação, integridade, repetição, abuso e interpretação do conteúdo como problemas distintos.

## Receptor

1. Use TLS e o mecanismo de verificação documentado pelo emissor. Prefira biblioteca mantida pelo emissor quando disponível; valide a assinatura sobre os bytes originais do corpo, antes de o framework os alterar.
2. Valide tamanho, Content-Type, método, schema e campos requeridos. Rejeite cedo payload malformado sem expor detalhes internos.
3. Valide timestamp e evento/ID autenticados para frescura e replay apenas quando o protocolo os assina e oferece; a assinatura sozinha não evita repetir um pedido válido.
4. Persista deduplicação e aceitação de modo durável antes da confirmação, segundo o contrato de delivery. Limite taxa e concorrência, responda de forma previsível e mova processamento lento para execução assíncrona.
5. Separe autenticidade do emissor, autorização para o efeito e segurança do conteúdo. Um payload validamente assinado ainda pode conter dados inválidos, excessivos ou maliciosos.
6. Guarde segredos fora de URLs, prompts e logs. Planeie rotação com período de sobreposição e revogação de chave comprometida.

Não imponha cabeçalhos, algoritmo, janela temporal ou código de resposta universais. Emissores diferem; consulte o contrato e a documentação oficial atuais. Não trate allowlist de IP como substituto de assinatura, nem assinatura como substituto de deduplicação.

## Emissor que chama URLs configuráveis

Se um operador, cliente ou agente pode registar o destino do webhook, o serviço torna-se um cliente HTTP com risco de SSRF. Valide esquema e destino, resolva e filtre endereços públicos e privados no momento da conexão, impeça bypass por redirecionamento/DNS rebinding conforme o stack, e bloqueie redes e metadados internos. Faça a validação também no caminho de saída; validar apenas ao guardar o URL não basta.

## Dados e disponibilidade

- Defina tamanho máximo, timeout de receção, limite por emissor/tenant e tratamento de rajadas.
- Coloque o trabalho em fila durável antes de confirmar se o consumidor vai processar depois da resposta.
- Nunca execute a ação sensível durante a validação da assinatura.
- Redija segredos, dados pessoais e conteúdo não necessário em logs e traces. Prefira IDs, hashes e referências protegidas.
- Não siga redirects para callback de entrada ou saída sem uma regra explícita e segura.

## Leitura de referência

- [OWASP Webhook Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Webhook_Security_Cheat_Sheet.html) — assinatura, replay, duplicados, limites e URLs de callback.
- [Standard Webhooks Specification](https://github.com/standard-webhooks/standard-webhooks/blob/main/spec/standard-webhooks.md) — opção de protocolo; não é adotada automaticamente por todos os emissores.
- [OWASP SSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)

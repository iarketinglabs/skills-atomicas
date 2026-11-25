# Fluxos autorizados por provedor

| Caso | Caminho documentado | Decisão para uma aplicação própria |
|---|---|---|
| OpenRouter com chave do usuário | Autorização com PKCE S256 e troca do código por chave da API controlada pelo usuário | Integre o callback documentado, persistindo a chave no servidor. Modele expiração e revogação. |
| Uso de Codex | Login ChatGPT ou chave por cliente Codex conforme a documentação oficial. O fluxo nativo oferece login por device code em ambientes previstos. | Para uma aplicação que chama a API OpenAI, use credenciais de projeto ou outro mecanismo de plataforma documentado para seu caso. Confira separadamente a autenticação do SDK ou cliente oficial que venha a usar. |
| Uso de Claude Code | Sign-in nos clientes Anthropic pelo fluxo oficial | Para aplicações de terceiros, siga as opções documentadas de Claude Console ou provedor de inferência suportado. A Anthropic restringe uso intermediado de credenciais de assinaturas e login Claude.ai em aplicativos de terceiros. |
| Provedor OAuth registrado pela aplicação | Fluxos, escopos, tokens e restrições descritos para o registro real | Implemente somente concessões previstas para esse cliente, com destinos e redirecionamentos verificados. |

[Autenticação Codex](https://learn.chatgpt.com/docs/auth) · [Autenticação da OpenAI API](https://developers.openai.com/api/reference/overview) · [Uso de credenciais da Anthropic](https://code.claude.com/docs/en/legal-and-compliance#authentication-and-credential-use) · [Práticas de segurança OAuth](https://www.rfc-editor.org/rfc/rfc9700.html)

## OpenRouter

1. Abra uma transação em sessão no servidor para a identidade correta. Gere verificador, desafio S256 e estado aleatório. Informe ao usuário a finalidade da chave e a conta ou workspace que pagará pelo uso.
2. Use o endpoint de autorização documentado, com callback HTTPS do aplicativo, desafio S256 e estado. Se houver requisito de workspace, limite ou prazo, selecione a opção documentada e confira a diferença entre preferência e restrição.
3. No retorno autorizado, compare o estado previsto com o recebido e confira validade e proprietário da transação. Para cancelamento sem estado, mantenha a conexão existente e encerre apenas a tentativa identificada de forma confiável.
4. Consuma o código uma vez, do servidor, com o verificador da transação, em `POST https://openrouter.ai/api/v1/auth/keys`. A resposta do fluxo é uma chave que autentica chamadas à API. A aplicação precisa tratar desconexão local, revogação no provedor e reconexão conforme o ciclo dessa chave.
5. Devolva à UI apenas o estado e, quando seguro, links de gestão pelo contrato oficial. Trate o código no callback como segredo temporário. Redija a query em proxies, APM e logs de aplicação.

Sem um fluxo de callback verificável, use somente alternativa explicitamente documentada para o cliente alvo. A emissão de uma chave pelo código PKCE não implica um refresh token. [Guia OpenRouter PKCE](https://openrouter.ai/docs/guides/overview/auth/oauth) · [Contrato de troca](https://openrouter.ai/docs/api/api-reference/o-auth/exchange-auth-code-for-api-key)

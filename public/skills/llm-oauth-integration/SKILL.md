---
name: llm-oauth-integration
description: Use ao projetar, implementar ou depurar vínculos OAuth autorizados para provedores LLM, como OpenRouter PKCE, ou ao distinguir autenticação de clientes oficiais Codex e Claude Code de credenciais usadas por uma aplicação própria.
---

# Vínculos OAuth para provedores de modelos

Use a superfície de autenticação que o provedor documenta para o tipo de cliente e o recurso pretendido. Separe credencial de inferência, login da aplicação e autenticação em um cliente oficial. Para configurar somente uma chave de API já emitida, use as práticas de gestão de segredos do projeto.

## Entradas e limites

Identifique produto, tipo de cliente, ambiente, proprietário da credencial, permissões e cobrança. Confirme na documentação vigente o fluxo, destino, escopo, callback, expiração e revogação. Os nomes de produto em [fluxos por provedor](references/fluxos-por-provedor.md) servem para escolher o contrato correto.

Para implementar ou testar, use registro e ambiente autorizados, acesso ao servidor e secret manager, e identidades de teste. Se só houver o briefing, entregue arquitetura e verificações pendentes. Uma sessão válida de cliente oficial só dá acesso pelo contrato que a suporta. Mantenha login, cookies e tokens desse cliente no mecanismo oficial.

## Fluxo

1. **Confirme o contrato.** Para cada integração, identifique o cliente autorizado e o formato da credencial que chega à inferência. Use OAuth apenas quando o provedor oferecer esse acesso ao seu cliente. Registre alternativa documentada se o acesso pretendido não estiver disponível.
2. **Modele o vínculo.** Separe rota de autorização, transação temporária, armazenamento, resolução e adapter. Identifique a conexão por escopo de tenant ou usuário, provedor e tipo de credencial. Um adapter só aceita as credenciais do contrato dele e só chama destinos configurados no servidor.
3. **Inicie e finalize com segurança.** Para o fluxo de código, use os requisitos do provedor e PKCE S256 quando suportado. Use estado único e expirável vinculado à sessão e ao destino. Confirme callback, sessão, provedor e estado antes de trocar código. O verificador e a troca ficam no servidor. Trate cancelamento, callback duplicado e transação vencida.
4. **Guarde e resolva a credencial.** Use uma referência ao secret store ou cifra gerida com acesso restrito. Confira autorização em cada leitura e operação. Só implemente refresh quando o contrato o suportar. Se houver rotação, proteja a concorrência e persista a atualização de modo atômico. Consulte [armazenamento e segurança](references/armazenamento-e-seguranca.md).
5. **Demonstre o vínculo.** Em ambiente autorizado, teste sucesso, escopo, expiração ou revogação, reconnect e separação entre duas identidades sintéticas. Teste callback repetido e tentativa de usar a credencial no adapter incorreto. Verifique redação de URL, logs, métricas e respostas. Se a falha for de ambiente ou persistência, use [diagnóstico](references/troubleshooting.md).

## Entrega

Informe o fluxo escolhido e sua fonte, limites por provedor, fronteiras de acesso, estados de conexão, comportamento de desconexão e provas de validação. Marque o que depende de onboarding do provedor, identidade de teste ou revisão de segurança. Para a UI, exponha estado e próxima ação. Mantenha a credencial e o motivo técnico sensível no servidor.

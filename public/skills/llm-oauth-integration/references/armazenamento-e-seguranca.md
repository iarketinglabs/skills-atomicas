# Armazenamento, resolução e ciclo da credencial

## Separe transação e conexão

| Registro | Campos que mudam o comportamento | Regras |
|---|---|---|
| Transação de autorização | Identidade e tenant, provedor, verificador PKCE, estado, redirect, criação, expiração e consumo | Servidor, prazo curto e uso único. Vincule à sessão iniciadora. Use callback registrado e retorno interno escolhido no servidor. |
| Conexão | Escopo de locatário ou usuário, provedor, tipo de credencial, referência ao segredo, status e versão | Armazene identidade composta. Separe metadados exibidos na UI do material secreto. Fixe autorização por operação. |
| Credencial | Chave de API ou access token e, quando contratual, refresh token e sua expiração | Secret manager ou cifra com chave gerida fora do banco. Mantenha material secreto fora de navegador, filas, logs e traces. |
| Auditoria | Ação, referência à conexão, ator autorizado, resultado e versão observada | Use eventos redigidos. Retenha somente o necessário. |

Conexões globais exigem escopo e responsáveis explícitos. O servidor valida o proprietário de cada conexão e a permissão por uso. RLS pode reforçar o isolamento quando o backend a suporta. Teste também o caminho com identidade de serviço, workers e privilégios operacionais, pois o caminho real pode ter regras diferentes das consultas do usuário.

## Resolução e atualização

1. Resolva o escopo a partir de identidade verificada, e confirme aplicação, provedor e finalidade.
2. Leia o segredo apenas para executar a chamada no adapter correspondente. Separe ambientes e limite o acesso no secret manager.
3. Se o provedor emite credenciais com refresh documentado, atualize antes da expiração com margem compatível com clock skew e duração da chamada. Coordene por conexão com bloqueio ou mecanismo equivalente. Use versão e atualização condicional para não trocar uma geração recente por uma antiga.
4. Em falha de refresh ou revogação, mude o estado para precisar de reconexão de acordo com a causa. Preserve o diagnóstico redigido. Trate erros transitórios com tentativas limitadas. Nunca use credencial de outro proprietário como fallback.
5. Se o usuário desconectar, invalide o vínculo local. Quando houver revogação documentada e autorizada, execute ou encaminhe para gestão da chave no provedor. Informe separadamente os resultados local e remoto.

Proteja callbacks com estado, PKCE quando suportado, escopo e validação de origem conforme o contrato. Para clientes com mais de um emissor, use separação de callbacks ou validação do emissor compatível. Segredos vazados precisam de revogação ou rotação, além de remoção dos locais de exposição. [OAuth Security BCP](https://www.rfc-editor.org/rfc/rfc9700.html)

# Diagnóstico de vínculos e credenciais LLM

| Sintoma | Verificação inicial | Resposta |
|---|---|---|
| Callback recusado | Compare URI registrada e efetiva, incluindo esquema, domínio, porta e subcaminho. Confirme sessão e estado. | Use URI prevista e retorno interno fixo. Revise proxy e cookie. Mantenha o isolamento entre provedores e ambientes. |
| Código inválido ou já usado | Confira se a tentativa expirou, duplicou ou se verificador e estado vieram da mesma transação. | Reinicie o fluxo se necessário. Redija código e verificador de logs e erros. |
| Conecta, mas não persiste | Compare migrações, ambiente, permissões e esquema exposto. Use diagnóstico redigido. | Corrija a condição comprovada. Quando houver PostgREST, confira versão e política de atualização de schema cache. |
| Funciona no cliente oficial, falha no app | Verifique o contrato de autenticação e a audiência do recurso de inferência no provedor. | Use o mecanismo documentado para o aplicativo. Mantenha o login nativo no cliente oficial. |
| Falha após expiração ou revogação | Distinga erro de credencial, chave sem saldo ou limite, indisponibilidade e erro de escopo. | Só faça refresh se documentado. Trate revogação ou prazo expirado com reconexão cujos efeitos estejam claros. |
| Duas tentativas de refresh divergem | Confirme com relógio controlado e chamadas sintéticas no ambiente de teste. Observe identidade e versão, sem ler valores dos segredos. | Coordene concorrência por conexão. Use escrita condicional e transição explícita em caso de revogação. |
| Usuário recebe acesso de outro tenant | Confira o vínculo, query, cache, adapter e worker com duas identidades sintéticas. | Contenha o acesso, preserve auditoria redigida, corrija a fronteira e valide revogação no escopo afetado antes de restaurar. |

## Ordem de prova

Com uma identidade de teste autorizada, demonstre início, callback, armazenamento, uso no adapter e encerramento ou revogação. Inclua cancelamento, replay, expiração e falha de escopo. Confira que payloads sensíveis e query do callback ficam fora dos logs. Um resultado positivo em desenvolvimento sustenta somente o ambiente e versões observados.

[Práticas de segurança OAuth](https://www.rfc-editor.org/rfc/rfc9700.html) · [Cache de esquema PostgREST](https://docs.postgrest.org/en/stable/references/schema_cache.html)

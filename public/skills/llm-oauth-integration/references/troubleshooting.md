# Troubleshooting — OAuth LLM

Sintomas comuns ao integrar OAuth de provedores LLM em sistemas agênticos. Diagnóstico genérico — adapte ferramentas ao stack.

---

## Schema e banco de dados

### `Could not find the 'credential_type' column … in the schema cache`

**Causa:** migration criou a coluna no Postgres, mas PostgREST (Supabase) ainda usa schema cache antigo.

**Ação:**

1. Confirmar que a migration rodou no projeto/instância correta
2. Executar `NOTIFY pgrst, 'reload schema';` no SQL Editor
3. Retry salvar conexão OAuth
4. Se persistir: reiniciar instância PostgREST ou verificar migration em ambiente errado (dev vs prod)

### OAuth save retorna 500 genérico após deploy

**Causa provável:** schema remoto desatualizado ou constraint de `provider` violada.

**Ação:**

1. Inspecionar logs server-side (mensagem real do ORM/Supabase)
2. Verificar migrations pendentes
3. Confirmar enum de providers inclui valor novo (ex.: `openai-codex`)

---

## Redirect e URLs

### Redirect URI mismatch / invalid_redirect

**Causa:** callback registrado no vendor ≠ URL montada pelo app.

**Ação:**

1. Logar URL exata gerada em `iniciar` (sem secrets)
2. Conferir `APP_URL` (scheme + host + porta)
3. Conferir `BASE_PATH` em produção (`/subpath/api/.../callback`)
4. Atualizar painel do vendor com URI idêntica (incluindo trailing slash se exigido)

### OAuth funciona em localhost, falha em produção

**Causa:** `APP_URL` ainda aponta para `http://localhost:3000`.

**Ação:** definir `APP_URL=https://dominio-real` no ambiente de produção; rebuild/restart.

### Callback retorna 404

**Causa:** rota API não registrada ou base path omitido no router.

**Ação:** verificar file-based routing / prefixo de API; testar callback URL manualmente.

---

## Runtime e bundler

### `__webpack_require__.a is not a function` (Next.js / server actions)

**Causa:** import circular — client importa tipos ou funções de módulo `"use server"`.

**Ação:**

1. Extrair tipos compartilhados para módulo neutro (`types/llm-connection.ts`)
2. Extrair helpers puros para `lib/` sem `"use server"`
3. Client importa só tipos e componentes; server actions ficam isoladas

### Página de settings 404 intermitente (dev)

**Causa:** dev server inconsistente (HMR) ou cache de build corrompido.

**Ação:**

1. Parar processo na porta do dev server
2. Limpar cache de build (ex.: `.next`)
3. Reiniciar dev server
4. Confirmar rota dentro do layout correto (route groups não mudam URL pública)

### CSS/assets 404 após `build` com `dev` ativo

**Causa:** build de produção e dev server escrevem no mesmo diretório de cache.

**Ação:** nunca rodar build e dev simultaneamente no mesmo checkout; limpar cache e reiniciar dev.

---

## OAuth e tokens

### Device-code poll nunca completa

**Causa:** usuário não autorizou; timeout; rate limit.

**Ação:**

1. Confirmar `user_code` correto digitado no site do vendor
2. Respeitar `interval` entre polls
3. Tratar HTTP 429 com backoff
4. Verificar timeout global (ex.: 15 min)

### Refresh falha com `invalid_grant`

**Causa:** refresh token revogado ou expirado; usuário desconectou no vendor.

**Ação:** marcar conexão como inválida; pedir reconexão OAuth na UI; não retentar infinitamente.

### API LLM retorna 401 com token "válido"

**Causa:** adapter usa endpoint/headers errados para o modo OAuth.

**Ação:**

1. Confirmar endpoint correto (Codex vs OpenAI API; Claude Code headers)
2. Confirmar `credential_type=oauth` no resolver
3. Verificar betas e User-Agent exigidos pelo vendor
4. Testar token com curl server-side antes de culpar o agente

### Token expira no meio de geração longa

**Causa:** refresh lazy só no 401.

**Ação:** implementar refresh proativo com skew (~120s) no CredentialResolver **antes** de cada chamada LLM.

---

## Segurança (incidentes)

### Token apareceu em log ou URL

**Ação imediata:**

1. Revogar sessão no vendor se possível
2. Apagar conexão local
3. Corrigir vazamento (nunca passar token em query string)
4. Rotacionar segredo de cifragem se ciphertext vazou com chave comprometida

---

## Checklist de diagnóstico rápido

```text
1. Migration aplicada no ambiente certo?
2. Schema cache recarregado?
3. APP_URL + BASE_PATH corretos?
4. Redirect URI registrada no vendor?
5. Resolver retorna access_token no servidor (curl interno)?
6. Adapter usa endpoint/headers do modo OAuth?
7. Imports client/server separados?
```

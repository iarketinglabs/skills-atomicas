# Fluxos OAuth por Provedor LLM

Referência vendor-neutral para os três perfis mais comuns em sistemas agênticos. Adapte nomes de rotas e paths ao stack do projeto.

## Tabela Comparativa

| Provedor | Fluxo OAuth | API de inferência | Refresh | Notas |
|---|---|---|---|---|
| OpenAI Codex | Device-code | `chatgpt.com/backend-api/codex` | Sim (refresh_token) | Provedor **separado** de OpenAI API key |
| Anthropic Claude Code | PKCE + colar código | `api.anthropic.com/v1/messages` | Sim | Headers de produto CLI obrigatórios |
| OpenRouter | PKCE redirect | `openrouter.ai/api/v1/chat/completions` | Depende do token | Callback deve respeitar base path |

---

## OpenAI Codex (device-code)

Produto OAuth distinto da OpenAI Platform API. Usuário autoriza com conta ChatGPT/Codex.

### Sequência

```text
1. POST auth.openai.com/.../deviceauth/usercode
   → { user_code, device_auth_id, interval }

2. UI exibe user_code; usuário abre auth.openai.com/codex/device e autoriza

3. Poll POST .../deviceauth/token { device_auth_id, user_code }
   → null/403/404 enquanto pendente
   → { authorization_code, code_verifier } quando autorizado

4. POST auth.openai.com/oauth/token
   grant_type=authorization_code + code + verifier + client_id
   → { access_token, refresh_token, ... }

5. Persistir StoredOAuthCredentials cifrado no ConnectionStore
```

### Estado transitório (sessão/cookie)

- `device_auth_id`
- `user_code`
- `interval_seconds`
- `started_at_ms` (para timeout global, ex.: 15 min)

### Polling

- Respeitar `interval` da resposta (mínimo ~3s)
- Tratar HTTP 429 com backoff (`Retry-After`)
- Timeout total configurável (ex.: 15 min)

### Adapter de inferência

- Base URL: `https://chatgpt.com/backend-api/codex`
- Endpoint típico: `POST .../responses`
- Authorization: `Bearer <access_token>`
- Header opcional: conta ChatGPT extraída de claim JWT (`ChatGPT-Account-Id` ou equivalente)
- Refresh: decodificar `exp` do JWT access token; refresh proativo ~120s antes

### Catálogo de modelos (opcional)

- `GET chatgpt.com/backend-api/codex/models` com mesmo Bearer

---

## Anthropic Claude Code (PKCE + colar código)

OAuth do produto Claude Code — **não** é o fluxo de API key consumer. O usuário autoriza em `claude.ai` e cola o código de retorno.

### Sequência

```text
1. Gerar PKCE (verifier + challenge S256) e state aleatório

2. Montar URL:
   claude.ai/oauth/authorize?
     client_id=...&
     response_type=code&
     redirect_uri=<registrado>&
     scope=org:create_api_key user:profile user:inference&
     code_challenge=<challenge>&
     code_challenge_method=S256&
     state=<state>

3. UI abre URL; usuário copia código exibido após autorização

4. POST concluir com { code, state }
   Validar state === state da sessão (anti-CSRF)

5. POST token endpoint (tentar fallbacks se houver mais de um URL):
   grant_type=authorization_code
   client_id, code, state, redirect_uri, code_verifier

6. Persistir { access_token, refresh_token, expires_at_ms, auth_mode: "claude_code" }
```

### Redirect URI

Anthropic Claude Code usa redirect fixo registrado no produto (ex.: `https://console.anthropic.com/oauth/code/callback`) — o usuário **cola** o código, não há redirect HTTP de volta ao seu app.

### Token endpoints (fallback)

Implementações de referência tentam, em ordem:

1. `https://platform.claude.com/v1/oauth/token`
2. `https://console.anthropic.com/v1/oauth/token`

Use `User-Agent` compatível com cliente oficial na troca de token.

### Refresh

```text
POST token endpoint
  grant_type=refresh_token
  refresh_token=...
  client_id=...
```

Atualizar `expires_at_ms` a partir de `expires_in`.

### Adapter de inferência

Headers típicos quando `credential_type=oauth`:

| Header | Valor |
|---|---|
| `Authorization` | `Bearer <access_token>` |
| `anthropic-version` | versão da API Messages |
| `anthropic-beta` | beta OAuth + betas de produto (thinking, streaming) |
| `User-Agent` | UA de CLI (ex.: `claude-code/2.x (external, cli)`) |

Sem esses headers, a API pode rejeitar tokens OAuth válidos.

### Catálogo de modelos (opcional)

- `GET api.anthropic.com/v1/models` com Bearer OAuth

---

## OpenRouter (PKCE redirect)

Fluxo OAuth padrão com redirect de volta ao app.

### Sequência

```text
1. Gerar PKCE + state; guardar verifier e state em sessão

2. Redirect usuário para openrouter.ai/oauth/authorize?...

3. Callback GET /oauth/callback?code=...&state=...
   Validar state; trocar code + verifier no token endpoint

4. Persistir tokens; redirect para /settings/llm?connected=openrouter
```

### Base path

Monte callback URL com URL absoluta do app:

```text
callback = APP_URL + BASE_PATH + "/api/integrations/openrouter/callback"
```

Registre exatamente essa URI no painel OpenRouter.

### Adapter de inferência

- `POST https://openrouter.ai/api/v1/chat/completions`
- `Authorization: Bearer <access_token>`

OpenRouter também aceita API key manual — mesmo provedor, `credential_type` discrimina.

### Catálogo de modelos (opcional)

- `GET openrouter.ai/api/v1/models`

---

## Contrato Normalizado de Saída

Todos os fluxos devem produzir o mesmo shape antes de cifrar:

```typescript
interface StoredOAuthCredentials {
  access_token: string;
  refresh_token: string;
  expires_at_ms?: number;  // preferir para Anthropic/OpenRouter
  auth_mode?: string;      // ex.: "claude_code", "codex"
}
```

O **CredentialResolver** consome esse contrato independentemente do vendor.

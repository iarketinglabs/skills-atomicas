# Armazenamento e Segurança — OAuth LLM

## Princípios

1. **Tokens OAuth nunca em plaintext** no banco, logs, URLs ou client
2. **Refresh server-only** — o browser nunca recebe `refresh_token` após o fluxo inicial
3. **Segregação de segredos** — segredo de cifragem separado de API keys de deploy
4. **Least privilege** — RLS/permissões alinhadas ao modelo do produto (conexão global vs por usuário)

## Contrato de Persistência

### Linha de conexão

```text
provider          TEXT UNIQUE NOT NULL
credential_type   TEXT NOT NULL CHECK (credential_type IN ('api_key', 'oauth'))
encrypted_secret  TEXT NOT NULL
connected_by      TEXT NULL
updated_at        TIMESTAMPTZ NOT NULL
```

### Payload OAuth (antes de cifrar)

```json
{
  "access_token": "eyJ...",
  "refresh_token": "rt_...",
  "expires_at_ms": 1710000000000,
  "auth_mode": "claude_code"
}
```

### Payload API key (antes de cifrar)

String opaca — a chave em si, sem JSON wrapper.

## Cifragem em Repouso

Padrão recomendado: **AES-256-GCM** com segredo dedicado.

```text
encrypted_secret = base64( iv (12 bytes) || ciphertext || auth_tag )
plaintext        = encrypt(JSON.stringify(credentials), LLM_KEYS_ENC_SECRET)
```

Regras:

- Segredo de env `LLM_KEYS_ENC_SECRET` — mínimo 32 bytes de entropia; rotacionar exige re-cifrar todas as conexões
- Funções `encrypt`/`decrypt` **server-only** (nunca importar no client bundle)
- Não logar plaintext nem ciphertext em erros de produção

Alternativas aceitáveis: KMS cloud (AWS KMS, GCP KMS), Vault, Supabase Vault — desde que o resolver só rode no servidor.

## Variáveis de Ambiente

| Variável | Uso |
|---|---|
| `APP_URL` | URL absoluta da app (`https://app.example.com`) — redirects OAuth |
| `BASE_PATH` | Subpath opcional (`/my-app`) — concatenar em callbacks e links |
| `LLM_KEYS_ENC_SECRET` | Segredo AES para cifrar conexões no banco |

Nunca commitar valores. Documentar nomes no `.env.example` sem valores reais.

## Escopo de Conexão

Decida explicitamente no projeto:

| Modelo | Quando usar | Implicação RLS |
|---|---|---|
| **Global (sistema)** | Um pipeline compartilhado; config de admin | Qualquer usuário autenticado lê/escreve — ou só admin |
| **Por usuário** | Cada colaborador usa sua conta LLM | RLS `user_id = auth.uid()` |

OAuth global é comum em ferramentas internas de equipe; OAuth por usuário em produtos multi-tenant.

## Migration Checklist

Antes de habilitar OAuth em produção:

```text
- [ ] Migration cria credential_type + enum/constraint de provider
- [ ] Migration aplicada no banco remoto (não só local)
- [ ] PostgREST/schema cache recarregado se usar Supabase
- [ ] LLM_KEYS_ENC_SECRET definido no ambiente
- [ ] APP_URL aponta para domínio real (não localhost) em prod
- [ ] Redirect URIs registradas nos painéis dos vendors
```

### Reload schema cache (Supabase/PostgREST)

Se o erro for `Could not find the 'credential_type' column of '...' in the schema cache`:

```sql
NOTIFY pgrst, 'reload schema';
```

Ou reinicie PostgREST / aguarde propagação automática.

## Rotação e Revogação

| Evento | Ação |
|---|---|
| Usuário clica "Desconectar" | DELETE ou NULL na linha do provider |
| Refresh falha (401/invalid_grant) | Marcar desconectado; pedir reconexão na UI |
| Rotação de LLM_KEYS_ENC_SECRET | Decifrar com segredo antigo, re-cifrar com novo — script one-off |
| Comprometimento de token | Revogar no vendor se possível + apagar linha local |

## Auditoria

Campos úteis:

- `connected_by` — ID do usuário que conectou por último
- `updated_at` — timestamp da última gravação (inclui refresh automático)

Não armazene histórico de access tokens — só o par atual cifrado.

## O Que Nunca Fazer

- Enviar `refresh_token` ao client após salvar
- Armazenar tokens em `localStorage`, query params ou cookies não-httpOnly
- Reutilizar segredo de cifragem para outros dados sem namespace
- Expor endpoint de refresh sem autenticação de sessão do app

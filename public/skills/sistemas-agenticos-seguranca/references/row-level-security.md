# RLS (Row Level Security)

Parte de **Proteção de Dados** (ver Framework Mental no `SKILL.md`). RLS é a implementação concreta, no nível do banco de dados relacional, do princípio de Authorization descrito em `authentication-vs-authorization.md` — a última linha de defesa física contra vazamento de dados entre usuários (multi-tenancy).

## O que é e a analogia da planilha

Row Level Security é uma diretiva de governança aplicada diretamente na engine do banco de dados relacional, que policia o tráfego de dados para cada registro individual de uma tabela. Pense no banco como uma planilha: colunas são campos (nome, e-mail, plano) e linhas são registros de cada cliente.

```
TABELA DE USUÁRIOS (COM RLS ATIVO)
  Nome    Plano     user_id
  Júlia   Premium   uuid-1111   ← acesso exclusivo de Júlia
  Alice   Pro       uuid-2222   ← acesso exclusivo de Alice
```

Se o sistema atende múltiplos clientes ao mesmo tempo (multi-tenancy), o RLS garante isolamento absoluto: cada usuário só enxerga e manipula a própria linha, mesmo que manipule os parâmetros da requisição para tentar acessar a linha de outro. Sem RLS ativo (ou mal configurado), um usuário consegue ler os dados de outro simplesmente adivinhando ou manipulando um ID na requisição — a causa mais comum de vazamentos de dados por negligência básica.

## Habilitação e políticas

A primeira ação de higiene ao criar um banco novo é garantir RLS ativo por padrão em toda tabela nova (a maioria das plataformas modernas de Postgres gerenciado oferece essa opção como flag de projeto).

Exemplo de políticas SQL completas para uma tabela multi-tenant:

```sql
-- 1. Tabela vinculada ao usuário autenticado
CREATE TABLE public.tasks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL DEFAULT auth.uid() REFERENCES auth.users(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL
);

-- 2. Habilitação mandatória
ALTER TABLE public.tasks ENABLE ROW LEVEL SECURITY;

-- 3. Leitura: só a própria linha
CREATE POLICY "select_own_rows" ON public.tasks
FOR SELECT USING (auth.uid() = user_id);

-- 4. Inserção: só pode criar linha própria
CREATE POLICY "insert_own_rows" ON public.tasks
FOR INSERT WITH CHECK (auth.uid() = user_id);

-- 5. Atualização: só pode alterar a própria linha
CREATE POLICY "update_own_rows" ON public.tasks
FOR UPDATE USING (auth.uid() = user_id) WITH CHECK (auth.uid() = user_id);

-- 6. Deleção: só pode excluir a própria linha
CREATE POLICY "delete_own_rows" ON public.tasks
FOR DELETE USING (auth.uid() = user_id);
```

## Segregação de tabelas contra o "Plan Bypass"

Como detalhado em `authentication-vs-authorization.md`, ter RLS ativo não protege contra a vulnerabilidade de misturar dados de cobrança na mesma linha que o usuário pode editar — RLS restringe **de quem** é a linha, não **quais colunas** dela podem ser escritas por quem. A solução é sempre segregar em tabelas distintas: uma tabela de perfil com escrita liberada ao próprio usuário via política RLS, e uma tabela de assinatura/cobrança com política de **somente leitura** para o usuário, cuja escrita é reservada a um webhook de pagamento autenticado.

## Chaves de acesso: pública vs. mestre

O ecossistema de bancos gerenciados modernos costuma expor dois níveis de chave:

| Chave | Uso | Comportamento com RLS |
|---|---|---|
| **Chave pública/anônima** | Distribuída livremente no front-end | Respeita 100% as políticas de RLS — o banco filtra as linhas conforme o usuário autenticado |
| **Chave de serviço/mestre (admin)** | Uso exclusivo do back-end protegido | **Ignora** todas as políticas de RLS — acesso total de leitura/escrita/exclusão em qualquer linha |

**A gafe clássica:** copiar a chave de serviço por engano para as variáveis públicas do front-end. Qualquer pessoa que inspecione os arquivos estáticos de JavaScript do navegador encontra a chave mestre e ganha acesso irrestrito a todos os dados do sistema.

**Proteção:**
- A chave de serviço nunca sai do back-end protegido; nunca é injetada em build de front-end.
- Arquivos locais de variáveis de ambiente (`.env`) devem estar listados no `.gitignore` para nunca serem commitados.
- Em produção, chaves entram isoladas e criptografadas no console de variáveis de ambiente da plataforma de hospedagem — nunca hardcoded no repositório.
- Se um agente autônomo tiver acesso à chave de serviço (super-privilegiada, ignora RLS) e receber uma instrução ambígua como "limpar tabelas temporárias para rodar os testes", uma alucinação de caminho pode levá-lo a executar uma exclusão em massa contra dados de produção — ver `sandbox-isolation-data-protection.md` para como isolar essa superfície de risco.

## Checklist

- RLS habilitado em 100% das tabelas desde a criação do projeto — nunca como reforço tardio.
- Dados de cota/cobrança segregados em tabela própria, somente leitura para o usuário.
- Chave de serviço nunca acessível a partir do front-end nem versionada no repositório.
- Diagrama de esquema (tabelas, chaves estrangeiras, políticas RLS correspondentes) desenhado e validado antes de escrever qualquer código de aplicação.

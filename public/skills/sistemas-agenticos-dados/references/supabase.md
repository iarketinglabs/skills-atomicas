# Supabase e PostgreSQL Gerido

Esta referência é uma orientação de arquitectura. Supabase e os seus serviços, chaves, SDKs, CLI, versões de PostgreSQL, extensões, planos, limites e funcionalidades mudam. Antes de uma implementação, leia o changelog e a documentação oficial actual do tópico; confirme a versão do projecto, as permissões e o comportamento no ambiente real. Não use esta referência para afirmar preços, quotas ou disponibilidade.

## Adequação

Trate Supabase como uma opção de backend centrada em PostgreSQL gerido, com serviços adjacentes que podem reduzir integração manual. É candidato a cargas transaccionais e aplicações que beneficiem da proximidade entre dados relacionais e controlo de acesso no banco. Não presuma que serve sozinho analytics intensivo, processamento distribuído, alta concorrência de leitura ou pesquisa vectorial em qualquer escala. Compare a carga e, quando necessário, descarregue analytics por CDC/replicação para um destino analítico separado.

## Acesso e RLS

Em cada tabela, vista, função, storage object ou endpoint exposto:

1. Separe **exposição/grants** de **autorização por linha (RLS)**; configurar uma não prova a outra.
2. Active RLS nas tabelas em schemas expostos e escreva políticas para cada operação e perfil real, não uma política genérica por conveniência.
3. Para multi-tenant, derive o tenant da identidade validada e teste tentativas de leitura e escrita cruzadas. Não aceite `tenant_id` enviado pelo cliente como prova de autorização.
4. Nunca coloque chave secreta/service-role, credencial de banco ou token privilegiado num browser, aplicação pública ou conteúdo de agente. Use credenciais mínimas num backend protegido.
5. Revise views, funções privilegiadas, triggers, Storage e replicação; a semântica de privilégios pode diferir. Teste com identidades representativas, incluindo sem sessão, utilizador comum, outro tenant e operação administrativa.
6. Inspeccione erros e contagens de linhas: uma mutação sem autorização pode falhar silenciosamente ou afectar menos linhas do que o esperado.

Para fundamentos e sintaxe actual, consulte [Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security) e [Securing your API](https://supabase.com/docs/guides/api/securing-your-api). Aplique também `sistemas-agenticos-seguranca` quando existir risco de ferramenta, agente ou exfiltração.

## Migrações e Operação

- Trate schema e políticas como código versionado. Reveja migrações, ordem, compatibilidade, índices, locks, backfill e rollback antes de produção.
- Faça alterações em ambiente isolado quando disponível e valide migração, dados, permissões e plano de recuperação antes do rollout.
- Não adivinhe comandos da CLI nem estado de recursos. Consulte `--help`, versão instalada, changelog e docs do tópico.
- Confirme backups, restauração, retenção, regiões, limites e suporte de extensões no projecto específico. O nome da funcionalidade não demonstra que está disponível no plano/região/versão activa.
- Proteja observabilidade: não inclua tokens, credenciais, payloads sensíveis ou SQL com dados pessoais em logs partilhados.

Consulte [Database migrations](https://supabase.com/docs/guides/local-development/database-migrations) para o fluxo vigente e o [Supabase Changelog](https://supabase.com/changelog.md) para alterações incompatíveis e descontinuações.

## Dados Vectoriais

Se usar pgvector ou serviço semelhante, confirme suporte actual e escolha query/index pelo perfil medido. Mantenha modelo, dimensão, normalização e métrica compatíveis; planeie backfill e versão paralela ao mudar embeddings. Teste filtros de tenant e recall após filtros, não apenas o ranking sem filtro. Aumentar o corpus ou a selectividade pode alterar o recall, a latência e o custo.

Veja [Vector columns](https://supabase.com/docs/guides/ai/vector-columns), [Vector indexes](https://supabase.com/docs/guides/ai/vector-indexes) e [pgvector](https://supabase.com/docs/guides/database/extensions/pgvector). Compare solução relacional, busca híbrida e armazenamento especializado com as mesmas consultas e dados.

## Limites da Plataforma

Uma função serverless/edge não é automaticamente lugar adequado para todo job de dados. Verifique duração, memória, CPU, payload, concorrência, retry e política de segredos. Para processamento pesado, batch longo, reprocessamento ou streaming contínuo, compare workers, filas, orquestradores e compute externo.

As funcionalidades, comandos e categorias de maturidade podem mudar. Distinga serviço estável de alpha/beta, limite documentado de comportamento medido e afirmação do fornecedor de benchmark independente. Registe versão e data junto da decisão.

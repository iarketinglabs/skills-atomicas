# Padrão de envio de respostas ao Supabase

Use o Supabase apenas atrás de um endpoint de servidor. Uma página estática publicada no GitHub Pages não pode proteger uma chave de serviço nem validar sozinha quem está enviando respostas.

## Fluxo recomendado

1. Durante o preenchimento, mantenha o rascunho apenas na sessão do navegador. Esse armazenamento não é seguro contra XSS nem contra acesso local; desative-o para dados sensíveis ou em dispositivos partilhados.
2. Envie somente a resposta final, após mostrar o aviso de privacidade e recolher os campos mínimos necessários.
3. O navegador chama um endpoint HTTPS de servidor. O contrato está em references/submission-endpoint-contract.md.
4. O endpoint valida o formulário, tamanho e esquema, aplica controles contra abuso, define o horário no servidor e grava usando segredo guardado no ambiente server-side.
5. A tabela mantém RLS ativa e não tem policies para anon nem authenticated. O navegador não recebe permissão direta para ler, inserir, atualizar ou apagar respostas.
6. Defina acesso interno, retenção, eliminação e resposta a pedidos dos titulares antes de recolher respostas reais.

## Por que não usar UUID no navegador como autorização

Um identificador criado no navegador não prova a identidade nem a autorização de quem chama uma função. Se for exposto por XSS, logs, extensões ou partilha do dispositivo, pode ser reutilizado. Uma função SECURITY DEFINER acessível a anon amplia o impacto de uma falha de validação. Este pacote não usa essa abordagem.

## Migração de referência

Adapte assets/migration.sql.template ao projeto, reveja nomes e permissões e aplique por uma migração versionada. A service_role só pode existir no ambiente de servidor e não deve aparecer no HTML, JavaScript, GitHub Pages, logs ou documentação pública.

Fontes oficiais para revisar a gestão de chaves e permissões. [RLS](https://supabase.com/docs/guides/database/postgres/row-level-security) · [Proteção de dados](https://supabase.com/docs/guides/database/secure-data) · [Segredos de funções](https://supabase.com/docs/guides/functions/secrets)

## Limites

- CORS e validação de Origin ajudam a restringir chamadas de navegadores, mas não autenticam um utilizador nem impedem chamadas feitas fora do navegador.
- A chave publishable não é um segredo; RLS deve continuar a negar acesso direto à tabela.
- Não recolha source_url, user-agent, contactos ou campos livres sem finalidade justificada.
- Use exemplos sintéticos no repositório. Nunca adicione respostas, tokens, URLs de cliente ou credenciais reais.
- O exemplo não substitui avaliação de privacidade, revisão jurídica, testes de autorização, monitorização, cópias de segurança ou plano de retenção do projeto.

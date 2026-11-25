# Checklist de revisão e publicação

Use esta lista antes de ativar um formulário público. Um teste local ou build verde não demonstra que o tratamento de dados está autorizado ou seguro.

## Spec e conteúdo

- [ ] Finalidade, destinatários, campos, obrigatoriedade e retenção foram confirmados.
- [ ] Cada pergunta e tipo de dado está documentado.
- [ ] Foram removidos campos que não são necessários.
- [ ] Aviso de privacidade, responsável, base legal, contacto e exercício de direitos estão claros.
- [ ] Os exemplos e testes usam dados sintéticos.

## Wizard e acessibilidade

- [ ] Labels, grupos, foco, contraste e mensagens de erro foram revistos com teclado e leitor de ecrã.
- [ ] Campos opcionais e condicionais funcionam como previsto.
- [ ] A navegação bloqueia perguntas obrigatórias em falta.
- [ ] O rascunho de sessão é explicado e desativado para dados sensíveis ou dispositivos partilhados.
- [ ] O rascunho local é removido após envio confirmado.

## Endpoint e persistência

- [ ] Endpoint HTTPS server-side implementado e revisto.
- [ ] Slug em allowlist, esquema, tamanho e tipos são validados no servidor.
- [ ] Limite de taxa e controlos antiautomação estão configurados na infraestrutura de confiança.
- [ ] RLS está ativa; anon e authenticated não têm acesso direto à tabela.
- [ ] Segredos existem apenas no ambiente server-side e não aparecem no bundle, Git, logs ou respostas.
- [ ] Logs não incluem payloads, respostas, tokens ou dados pessoais desnecessários.
- [ ] Retenção, eliminação, acesso interno e cópias de segurança foram definidos.
- [ ] Testes sintéticos cobrem payload inválido, tamanho excessivo, slug desconhecido, repetição, falha do banco e falta de permissão.

## Publicação

- [ ] Repositório, site e visibilidade foram confirmados segundo a documentação atual do provedor.
- [ ] Só os ficheiros allowlisted necessários estão no artefacto público.
- [ ] Conteúdo, histórico e metadados foram revistos para dados de cliente e segredo.
- [ ] Build e URL publicados foram verificados.
- [ ] Envio ponta a ponta foi testado com uma resposta sintética e a linha de teste foi eliminada depois.

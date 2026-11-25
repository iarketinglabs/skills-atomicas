# Workflow Git e colaboração no GitHub

## Inspeção inicial

Comece com comandos de leitura:

- `git rev-parse --show-toplevel`
- `git status --short --branch`
- `git branch --show-current`
- `git branch -vv`
- `git remote`
- `git worktree list --porcelain`
- `git log -5 --oneline --decorate`

Inspecione separadamente `git diff` e `git diff --cached`. O primeiro mostra alterações unstaged; o segundo, o conteúdo preparado para o próximo commit. `git status` também revela ficheiros não rastreados. O branch por omissão deve ser confirmado no remote ou na plataforma; não assuma que se chama `main` ou `master`.

Para confirmar o destino, consulte a URL do remote configurado, por exemplo com `git remote get-url <remote>`, sem reproduzir tokens ou passwords na conversa, em logs ou em artefactos. Prefira o gestor de credenciais já configurado.

## Escolha de branch e integração

Siga a política existente. Se não houver uma, escolha o fluxo que melhor corresponde ao produto, à cadência de release, ao risco e à capacidade de revisão:

- Branches curtos e integração frequente reduzem divergência e tornam cada mudança mais simples de analisar.
- Branches de funcionalidade podem ser úteis quando há trabalho coordenado ou isolamento necessário; reduza o tempo de vida e sincronize com frequência.
- Branches de release ou manutenção paralela justificam-se quando versões distintas precisam de suporte simultâneo.
- Merge queues podem ajudar quando há concorrência frequente na branch de destino; confirme disponibilidade, checks e política antes de as adotar.

Não imponha um único modelo, duração ou limite de linhas para todos os projetos. Divida uma mudança quando isso melhorar a compreensão, a validação, o rollback ou a atribuição de responsabilidade. Evite fragmentar alterações que dependem umas das outras de forma a tornar cada parte incompleta.

Feature flags podem separar deploy de ativação, mas têm custo de ciclo de vida. Quando forem necessárias, registe finalidade, responsável, condição de remoção e comportamento seguro por omissão.

## Commit e publicação

1. Atualize a branch de base com o fluxo aprovado e confirme que não está a sobrescrever trabalho remoto.
2. Prepare apenas os caminhos pedidos. Se o ficheiro incluir alterações preexistentes, use staging interativo ou isole o trabalho noutro worktree; rever só o nome do caminho não garante que apenas os seus hunks foram staged. Reveja o resultado com `git diff --cached`.
3. Confirme o conjunto staged com `git diff --cached --name-status`, reveja o diff completo e execute `git diff --cached --check`.
4. Procure credenciais, dados pessoais, ficheiros locais, outputs temporários, dumps, caches e ficheiros de build que não pertençam ao pedido. Não copie o valor de um segredo encontrado. Um scanner de segredos configurado é preferível a padrões ad hoc.
5. Use o formato de commit definido pelo projeto. Conventional Commits é uma convenção opcional, não uma propriedade do Git. O prefixo descreve a intenção declarada e não prova, sozinho, a compatibilidade real da mudança.
6. Crie o commit apenas quando o utilizador ou a política de trabalho o autorizar. Reveja o commit resultante e confirme que os caminhos e a mensagem representam o pedido.
7. Para publicar, confirme explicitamente remote e branch, faça fetch, trate divergências sem descartar commits e use o mecanismo de publicação disponível. Depois do push, compare `git rev-parse HEAD` com `git ls-remote <remote> refs/heads/<branch>` para o branch exato. Não exponha URLs com credenciais.

Evite push direto para uma branch protegida quando o fluxo do repositório exigir PR. Não use `--force` para resolver divergências. `--force-with-lease` também reescreve história: use-o apenas quando a operação estiver explicitamente autorizada, a referência remota tiver sido verificada e não houver trabalho de terceiros a perder.

## Pull requests e revisão

Um PR eficaz explica:

1. problema ou resultado esperado;
2. escopo da mudança e o que ficou deliberadamente fora;
3. critérios de aceitação e impacto compatível/incompatível;
4. verificações executadas, com resultado e limitações;
5. riscos, migração, rollout e rollback quando aplicável.

Reveja comportamento, casos limite, erros, permissões, dados, APIs, dependências, testes, documentação e impacto operacional. Confirme que os checks obrigatórios passaram no SHA atual do PR, não num commit anterior. Use CODEOWNERS, reviews obrigatórias, rulesets, branch protection e merge queue conforme a configuração real do repositório.

Um tamanho grande é um sinal para avaliar decomposição e revisão, não uma regra universal de rejeição. Registe bloqueios concretos: escopo ambíguo, testes ausentes, checks obsoletos, conflito semântico, mudança de segurança sem owner ou comportamento não explicado.

## Versões e releases

Use SemVer apenas quando existir uma API pública e a política do projeto a adotar. Em SemVer, major indica incompatibilidade, minor acrescenta funcionalidade compatível e patch corrige sem quebrar compatibilidade. Confirme o contrato e o efeito no código antes de escolher o número.

Conventional Commits pode alimentar changelogs e automação de release quando adotado. Mensagens, títulos de PR e notas geradas são metadados: valide-os contra o diff. Tags e releases são publicação externa; crie-as apenas quando pedidas e depois de confirmar versão, artefactos, notas e checks.

## Registo final

Relate: branch e remote observados; caminhos incluídos; commit/SHA se criado; verificações realmente executadas; destino e SHA remoto se publicado; PR/release apenas se criado; estado local restante e bloqueios.

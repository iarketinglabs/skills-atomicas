# Histórico Git, recuperação e worktrees

## Modelo mental

Git mantém snapshots ligados por commits. `HEAD` e branches são referências mutáveis; o index é o snapshot preparado para o próximo commit. Por isso, a árvore de trabalho, o index e o último commit podem conter versões diferentes dos mesmos caminhos.

Reescrever história cria commits com novos IDs. Um rebase local pode ser útil antes de partilhar; rebase, reset de branch ou force-push sobre commits publicados pode quebrar referências de outras pessoas. `git reflog` regista movimentos locais de referências durante um período limitado; não é backup nem evidência remota.

## Antes de recuperar

1. Execute `git status --short --branch` e identifique alterações staged, unstaged, untracked e conflitos.
2. Guarde os SHAs e a branch corrente. Se houver trabalho sem cópia, preserve-o num commit, cópia ou branch/worktree aprovado antes de uma operação destrutiva.
3. Identifique o que deve mudar: conteúdo do ficheiro, index, posição de branch ou histórico remoto.
4. Escolha a operação menos destrutiva que alcance o objetivo. Inspecione o diff depois.

## Operações e efeitos

| Objetivo | Operação comum | Efeito e cuidado |
|---|---|---|
| Desfazer um commit publicado sem reescrever a história | `git revert <commit>` | Cria um novo commit inverso; reveja conflitos e efeitos colaterais. |
| Mover a branch preservando commits de integração | `git merge <branch>` | Regista a integração; respeite a política local. |
| Reaplicar commits sobre outra base | `git rebase <base>` | Cria novos IDs; não reescreva commits partilhados sem autorização específica e coordenação. |
| Retirar um ficheiro do staging | `git restore --staged -- <path>` | Muda o index, preservando a árvore de trabalho. Confirme o caminho. |
| Repor conteúdo na árvore de trabalho | `git restore --worktree -- <path>` | Pode descartar alterações desse caminho. Inspecione e preserve-as primeiro. |
| Mover `HEAD`/branch | `git reset <mode> <commit>` | `--soft` preserva index e árvore; `--mixed` redefine o index; `--hard` pode sobrescrever ficheiros e dados. Não escolha `--hard` por conveniência. |
| Procurar um commit perdido recentemente | `git reflog` | A recuperação depende de a referência ainda estar registada e do objeto existir. |
| Aplicar a mudança de outro commit | `git cherry-pick <commit>` | Cria um novo commit na branch atual; confirme se a mudança não foi integrada por outro caminho. |

`git clean` pode apagar ficheiros não rastreados e ignorados. `git reset --hard`, `git restore --worktree`, `git branch -D`, `git worktree remove --force` e pushes forçados podem descartar ou tornar inacessível trabalho. Antes de os usar, confirme o alvo, o conteúdo afetado, a autorização e uma forma de recuperação. Uma instrução genérica para “limpar” não identifica esses alvos.

## Conflitos

- Leia `git status` e identifique cada caminho em conflito; não resolva o repositório inteiro com `--ours` ou `--theirs`.
- Compare base, lado atual e lado entrante. Preserve regras de negócio de ambos os lados quando necessário; peça contexto quando a intenção não for inferível.
- Remova os marcadores apenas depois de reconstruir o comportamento pretendido. Reveja `git diff` e `git diff --check`, confirme que já não há entradas unmerged e execute verificações relevantes.
- Não conclua que um conflito foi resolvido apenas porque Git permitiu criar um merge commit.

## Worktrees

Worktrees permitem checkouts ligados ao mesmo repositório. Antes de criar, listar ou remover:

- `git worktree list --porcelain`
- confirme branch, caminho, estado staged/unstaged, ficheiros não rastreados e submódulos;
- não tente abrir a mesma branch em vários worktrees sem entender a proteção do Git;
- prefira `git worktree remove <path>` para uma worktree limpa;
- não use `--force` nem `git worktree prune` para contornar alterações locais ou caminhos desaparecidos sem verificar cada alvo.

Uma worktree separada reduz interferência entre tarefas, mas partilha referências e objetos. Não é uma cópia de segurança independente.

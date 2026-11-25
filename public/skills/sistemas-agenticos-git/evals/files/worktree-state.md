# Worktrees sintéticas

Saída de git worktree list --porcelain:

    worktree C:/work/app
    HEAD 5c36abc
    branch refs/heads/main

    worktree C:/work/release-fix
    HEAD 8db327a
    branch refs/heads/release-fix

Estado recolhido dentro de C:/work/release-fix:

    ## release-fix...origin/release-fix
     M src/release.ts
    ?? reports/release-check.csv

O estado das outras worktrees, o conteúdo desses caminhos e o valor de uma eventual cópia não foram verificados.

# Checklist de publicação Git

Use para uma publicação explicitamente pedida. Cada item deve ter evidência observável ou ser registado como pendente.

## Antes de escrever

- [ ] Pedido cobre a operação: commit, push, PR, merge ou release.
- [ ] Repositório, branch, remote e branch de destino confirmados.
- [ ] Instruções e proteções do repositório consultadas.
- [ ] Estado inicial registado; alterações existentes preservadas.
- [ ] Conteúdo staged limitado aos caminhos aprovados.
- [ ] Diff staged revisto e `git diff --cached --check` executado.
- [ ] Segredos, dados privados e artefactos locais verificados sem expor valores.
- [ ] Checks exigidos executados sobre a revisão atual ou identificados como pendentes.

## Durante a publicação

- [ ] Divergência remota verificada; nenhum commit de terceiros será descartado.
- [ ] Método de integração e mensagem de commit seguem a política local.
- [ ] PR, reviewers, checks e notas descrevem o conteúdo real.
- [ ] Tag/release, se pedida, usa versão, artefactos e notas confirmados.

## Depois

- [ ] SHA local e referência remota comparados, quando houve push.
- [ ] Estado do PR/merge/release consultado, quando aplicável.
- [ ] Alterações restantes, ficheiros não rastreados, bloqueios e checks não executados reportados.

## Evidência

- Branch/remote/destino:
- Paths publicados:
- Commit/SHA:
- Checks e resultados:
- SHA remoto/URL do PR/release:
- Estado local restante ou bloqueios:

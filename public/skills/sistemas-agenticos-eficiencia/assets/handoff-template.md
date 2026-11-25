# Template de Handoff de Sessão

Fonte canônica única deste template — referenciado (não copiado) por `../references/handoff-documentation.md` e `../references/focused-task-sessions.md`. Um handoff de alta densidade funciona como um "compilador de estado": conciso, direto, livre de preâmbulos, traduzindo progresso em dados puramente acionáveis para a próxima sessão (ou para outro agente) retomar exatamente de onde a anterior parou.

## Os quatro componentes obrigatórios

1. **Progresso Concluído (What's Done):** módulos alterados, endpoints criados, checklist de testes que passaram, diffs relevantes.
2. **Estado do Workspace (Active Files & Context):** quais arquivos estão sob edição ativa, quais configurações foram alteradas — o mapa físico que orienta a próxima sessão sobre onde estão os recursos.
3. **Decisões Diferidas e Arquitetura (Deferred Decisions):** os "porquês" por trás de escolhas técnicas, para que a próxima sessão não precise adivinhar ou re-perguntar.
4. **Próximos Passos (What's Next):** checklist sequencial do que falta implementar, testar e validar, com o critério de parada (definição de "concluído").

## Exemplo de formato

```markdown
# AGENTIC SESSION HANDOFF — CHECKPOINT v1.2

## 1. Progresso Concluído (What's Done)
- Implementada a rota de POST /api/checkout.
- Criada a migração SQL local para a tabela `subscriptions` com políticas de acesso ativas.
- Testes unitários de validação de schema em /tests passando deterministicamente.

## 2. Estado do Workspace e Arquivos Ativos
- Arquivos sob edição ativa: `src/pages/billing/api.ts`, `src/pages/billing/component.tsx`.

## 3. Decisões Arquiteturais Diferidas
- Optamos pelo padrão "Thin Client, Fat Server" para blindar o cálculo de limites de cota no back-end.

## 4. Próxima Etapa de Execução (What's Next)
- [ ] Configurar o webhook de pagamento na função de borda.
- [ ] Testar a expiração de TTL do rate limit.
```

## Como usar

1. Ao final de uma fase de trabalho (ou ao se aproximar do limiar de degradação de contexto — ver Framework Mental no `SKILL.md`), o agente gera esse bloco.
2. O bloco é salvo localmente em disco (ex. um arquivo de notas do projeto) — nunca só na memória da sessão.
3. A sessão atual é encerrada/resetada.
4. Uma nova sessão (do mesmo agente ou de outra ferramenta) recebe apenas esse bloco condensado e a instrução de continuar a partir dele.

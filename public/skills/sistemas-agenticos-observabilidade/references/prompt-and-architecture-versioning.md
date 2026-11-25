# Versionamento de Prompts e Arquiteturas

Parte de **Observabilidade e Melhoria Contínua** (ver Framework Mental no `SKILL.md`). Como tratar o comportamento cognitivo de um agente — o prompt e a topologia de roteamento entre sub-agentes — com o mesmo rigor de engenharia que se aplica a qualquer outra mudança de infraestrutura.

## Por que prompts precisam de versionamento como código

Diferente de software determinístico, onde o comportamento é imutável para uma versão fixa do binário, modelos de linguagem introduzem uma variável extra: uma atualização silenciosa de pesos por parte de um provedor pode degradar a capacidade de um agente de selecionar ferramentas ou estruturar saída — sem que nenhuma linha do seu prompt tenha mudado. Tratar prompts como strings soltas embutidas direto no código impede depuração de incidentes, rollback de comportamento indesejado e teste de regressão.

## Prompt-as-Code e Architecture-as-Code

```
1. SYSTEM PROMPT       →  2. SELEÇÃO DE MODELO  →  3. GRAFO DE ROTEAMENTO (DAG)
   versionado no Git       vinculado ao prompt        topologia de sub-agentes
                                                              │
                                                              ▼
                                                     DEPLOY SEGURO
                                                     (trace + metadados de run)
```

- **Prompt-as-Code:** todo prompt de sistema ou de ferramenta é uma configuração estruturada e versionada, não texto solto. Cada alteração gera um commit, passa por teste de regressão automatizado, e recebe uma versão semântica (major = mudança de objetivo de negócio; minor = novo esquema de ferramenta sem alterar a meta macro; patch = ajuste de formatação).
- **Architecture-as-Code:** conforme o sistema escala para múltiplos sub-agentes, o roteamento entre eles vira um grafo dirigido — essa topologia (quem chama quem, em que ordem, com que condição de retry) deve ser declarada em um arquivo de configuração versionado **independentemente** do prompt de sistema. Isso permite isolar se uma falha veio de um desvio de comportamento do modelo ou de um erro físico na topologia de integração.

## Arquitetura do registro central

```
GIT / REPOSITÓRIO
  prompts declarados em arquivo estruturado
  grafos de roteamento versionados separadamente
        │ pull request aprovado
        ▼
PROMPT REGISTRY SERVER
  1. sync via Git Worktrees (acesso rápido a branches de teste em paralelo)
  2. resolvedor de versão semântica (ex. "1.2.x" → última patch compatível)
  3. metadados vinculados (modelo recomendado, temperatura)
        │ injeta prompt + DAG ativos
        ▼
SANDBOX DE RUNTIME
  executa sob um identificador de sessão exclusivo para auditoria
```

## Implementação de referência: resolução por versão semântica

```python
class PromptArchitectureRegistry:
    def resolve_prompt(self, name, version_pattern):
        """Resolve 'latest', '1.1.x' (wildcard de patch), ou uma versão exata."""
        versions = self.prompts[name]
        if version_pattern == "latest":
            resolved = sorted(versions)[-1]
        elif version_pattern.endswith(".x"):
            prefix = version_pattern[:-2]
            candidates = [v for v in versions if v.startswith(prefix)]
            resolved = sorted(candidates)[-1]
        else:
            resolved = version_pattern
        payload = versions[resolved].copy()
        payload["resolved_version"] = resolved
        return payload
```

Cada sessão de agente instanciada registra explicitamente qual versão de prompt **e** qual versão de grafo de roteamento estava ativa — nunca "a versão mais recente" sem rastro, o que tornaria incidentes irreprodutíveis.

## Tags de rastreabilidade no trace

Toda chamada física a um modelo carrega metadados de versão anexados ao span (ver `tracing-inputs-outputs.md` para a arquitetura de spans): identificador e versão do prompt, identificador e versão do grafo de roteamento, hash do commit. Se um cliente relata que o comportamento do agente mudou em um dia específico, o time consegue localizar exatamente se uma versão experimental vazou para produção naquele intervalo.

## Métricas específicas de versionamento

- **Regression Rate:** percentual de casos de teste históricos (golden cases) que passaram a falhar após uma nova versão de prompt ou grafo.
- **Schema Failure Delta:** variação no número de saídas fora do schema esperado, comparando a versão nova com a anterior.
- **TTFT Variance:** prompts mais longos ou mal delimitados elevam a latência do primeiro token — uma regressão de prompt pode ser, na prática, uma regressão de performance.
- **Loop Depth Velocity Delta:** se uma nova versão faz o agente precisar de mais passos para o mesmo tipo de tarefa, é sinal de confusão introduzida pela mudança, não de "mais cuidado".

## Esteira de CI/CD cognitiva

```
1. COMMIT (Prompt-as-Code)  →  2. LINTER ESTÁTICO  →  3. TESTE DE EVALS
   alteração versionada          valida estrutura       roda contra casos
                                  e schema                de referência
                                                                │
                                                                ▼
6. DEPLOY CONSOLIDADO  ←  5. SHADOW DEPLOYMENT  ←  4. PROBATION GATE
   merge + nova versão      roda em paralelo em      valida se a
                             produção, sem servir       precisão subiu
                             a resposta ao usuário
```

**Shadow Deployment** é o mecanismo central de segurança: a versão nova roda em produção recebendo o mesmo tráfego real, mas sua saída nunca é servida ao usuário — só registrada para comparação. Se o score de qualidade da nova versão cair em relação à ativa, o build de deploy definitivo é abortado automaticamente, antes de qualquer usuário real ser exposto à regressão.

## Governança e cadeia de custódia

Para decisões automatizadas de alto impacto (ex. aprovação de crédito), a organização precisa poder provar, para qualquer transação passada, exatamente qual prompt e qual topologia estavam ativos naquele instante. Isso exige: commits assinados pelos engenheiros humanos responsáveis pela mudança comportamental, e a associação direta entre cada identificador de execução e um proprietário humano responsável — o mesmo princípio de identidade de agente já tratado na skill de Segurança e Confiabilidade desta coleção, se disponível.

## Vetores de ataque específicos deste pipeline

- **Injeção via pull request:** sem exigência de revisão humana estrita em merges no repositório de prompts, um PR malicioso pode inserir uma instrução oculta no prompt de sistema que se propaga para toda a frota no próximo deploy.
- **Sequestro de identidade de agente:** um agente comprometido emula os metadados de versão de um worker homologado para escapar de monitoramento de tráfego.

## Anti-padrões

- **Prompt Monolítico:** centenas de instruções de formatação, regra de negócio e esquema de ferramenta empilhadas em um único prompt gigante — degrada a atenção do modelo e infla o custo de cada turno.
- **Prompt Drift sem versionamento:** editar o comportamento de produção direto em um painel de provedor, sem passar pelo commit no Git — quebra a homogeneidade do time e torna incidentes irreversíveis por falta de rollback.
- **Dependency Wildcarding irresponsável:** sempre puxar a versão "latest" de uma dependência cognitiva externa (skill, servidor MCP) em vez de fixar uma versão testada — expõe o sistema a uma quebra de API ou envenenamento de pacote de terceiro sem aviso.

## Checklist

- Todo prompt de sistema e todo grafo de roteamento vivem versionados no repositório, nunca hardcoded ou editados fora do Git.
- Cada sessão de agente registra explicitamente qual versão de prompt e de grafo estava ativa, não "a mais recente" sem rastro.
- Mudanças de prompt passam por shadow deployment antes de servir tráfego real, com critério objetivo de reprovação automática.
- Merges no repositório de prompts exigem revisão humana — nunca aceitos de forma cega pelo pipeline de CI/CD.

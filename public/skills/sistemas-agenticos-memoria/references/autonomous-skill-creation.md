# Criação Autônoma de Skills

Parte de **Memória e Aprendizado de Longo Prazo** (ver Framework Mental no `SKILL.md`). O ponto onde um aprendizado de sessão deixa de ser um fato passageiro e vira uma capacidade procedural persistente — a memória procedural (Tier 3) mencionada em `holographic-memory-local.md`.

> Se a sua coleção de skills já tem uma skill de Harness/Building Blocks que cobre a anatomia de diretório de uma skill, o pipeline de compilação a partir de traces e a governança por nível de risco (A/B/C) em profundidade, consulte-a primeiro — este arquivo assume esse pipeline como conhecido e foca no ângulo específico de **memória de longo prazo**: como uma skill recém-criada entra no ciclo de consolidação, envelhece e é podada junto com o resto da memória do agente.

## Por que isso é memória, não só automação

Uma skill compilada autonomamente é, estruturalmente, um fato operacional de ordem superior: em vez de "o e-mail do gestor é X", ela registra "a sequência de ferramentas que resolve o problema Y é Z". O mesmo gatilho que popula a tabela de fatos (fim de uma sessão não trivial) também pode popular o repositório de skills — e o mesmo ciclo de sleep-time que poda fatos obsoletos poda skills obsoletas.

## Gatilho de criação

O sistema não cria uma skill a cada tarefa concluída — só quando a run cruza um limiar de complexidade: várias chamadas consecutivas de ferramenta, superação de um erro inesperado de console, ou uma correção de rumo fornecida por um operador humano. Runs triviais e curtas são descartadas para evitar poluir o repositório com skills de baixo valor.

```python
def should_skillify(trace):
    tools_used = trace["tools_invoked"]
    user_corrections = trace["user_corrections"]
    if len(tools_used) < 3 and not user_corrections:
        return False  # trace trivial demais, não compila
    return True
```

## A seção de maior valor: os Gotchas

A parte mais valiosa de uma skill compilada não é a lista de passos — é a **seção de Gotchas**: as anomalias e caminhos que o agente deve ativamente evitar, extraídas diretamente dos erros observados na run que originou a skill. Sem essa seção, a skill ensina o caminho feliz mas deixa o agente repetir o mesmo erro na primeira execução real.

Cada correção de feedback recebida do usuário é anotada em um log incremental de aprendizados, vinculado à skill — funcionando como uma barreira física contra a repetição do mesmo erro em execuções futuras.

## O ciclo de consolidação aplicado a skills (Dreaming Loop)

```
SLEEP TIME EVENT
        │ orquestrador pausa a fila de tarefas ativas
        ▼
DETECÇÃO DE SIMILARIDADE
        │ compara a assinatura semântica de todas as skills locais
        ▼
   similaridade > limiar alto (ver ../assets/temporal-decay-and-trust-score.md)?
        │ sim                              │ não
        ▼                                  ▼
RECOMPILAÇÃO / FUSÃO                DECAIMENTO TEMPORAL
  funde variantes redundantes         skills "frias" (sem uso recente)
  em uma única versão consolidada     perdem prioridade de carregamento
        │                                  │
        └──────────────┬───────────────────┘
                        ▼
              REGISTRO NO REPOSITÓRIO VERSIONADO
              (relatório forense do que mudou e por quê)
```

Sem esse ciclo ativo, o repositório de skills sofre o mesmo destino de qualquer memória não curada: acúmulo de variantes redundantes com escopos sobrepostos (`relatorio_v1`, `relatorio_cliente_a`, `relatorio_final`), confundindo o mecanismo de seleção da skill certa para a tarefa ativa e derrubando a precisão de execução — o fenômeno de **Skill Drift**, tratado também do ângulo de prompts em `self-improvement-learning-loops.md`.

## Governança por nível de risco (recapitulação)

Toda skill compilada autonomamente é categorizada pelo impacto de suas permissões antes de ser aceita no repositório persistente:

- **Nível A — baixo risco:** rotinas internas sem acesso externo. Escrita direta autorizada.
- **Nível B — risco médio:** fluxos que tocam controle de versão ou comunicações de teste. Entram em quarentena até validação por um avaliador independente e aprovação humana.
- **Nível C — alto risco:** escrita em sistemas de produção reais ou ações financeiras. Bloqueadas por padrão, exigem aprovação síncrona autenticada.

Essa escala já é o padrão canônico de governança de skills da sua coleção, se você tiver a skill de Harness/Building Blocks disponível — aqui ela é relevante porque determina **quais skills entram no ciclo de consolidação automática** (Nível A) e quais exigem revisão humana antes mesmo de existirem persistentemente (Níveis B e C).

## Risco específico deste vetor: jailbreak persistente

Diferente de uma injeção de prompt comum, que se limita à sessão ativa, um agente com permissão irrestrita de criação de skills e comprometido por conteúdo malicioso pode compilar uma skill silenciosa que persiste fisicamente no repositório — contaminando todas as execuções futuras, mesmo depois de o conteúdo malicioso original ter sido removido do workspace. É por isso que a criação autônoma de skills nunca deveria operar como Nível A por padrão sem uma esteira de avaliação prévia; a defesa completa contra esse vetor é escopo da skill de Segurança e Confiabilidade desta coleção, se disponível no seu ambiente.

## Anti-padrões

- **Skill Drift / Bloat:** criação livre sem centralização — dezenas de skills redundantes confundem a seleção em runtime.
- **Unbounded Sandbox Tooling:** skills geradas dinamicamente instalando pacotes ou executando scripts fora de um ambiente isolado.
- **Infração da regra de maturidade de dependências:** integrar skills ou pacotes externos publicados há poucos dias, sem tempo de maturação da comunidade — abre superfície para ataques de dia zero.

## Checklist

- Skills só são compiladas a partir de traces que cruzam um limiar mínimo de complexidade — não a cada tarefa trivial concluída.
- Toda skill compilada carrega uma seção de Gotchas extraída dos erros reais observados na run de origem.
- O repositório de skills passa por um ciclo periódico de detecção de similaridade e fusão — não cresce indefinidamente sem curadoria.
- Skills sem uso recente perdem prioridade de carregamento, seguindo o mesmo mecanismo de decaimento usado para fatos.
- Toda skill nova é classificada por nível de risco antes de ser aceita persistentemente no repositório.

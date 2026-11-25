# Planejamento Antes da Execução

Parte de **Spec Driven Development** (ver Framework Mental no `SKILL.md`). O arquivo canônico para a anatomia genérica do `spec.md` e para o loop de planejamento assimétrico — `specs-for-persistence.md` aplica esse mesmo processo a um domínio específico (dados) sem repetir a base aqui descrita.

## Por que planejar antes de codificar

Abrir uma conversa vazia e pedir a um agente para "criar" algo de forma impulsiva funciona bem para demonstrações rápidas, mas colapsa em sistemas reais: gera dívida técnica, regressões silenciosas de segurança e inundação de contexto que empurra o agente para a Dumb Zone. A alternativa é a regra de ouro do Spec Driven Development: **nenhuma linha de código é escrita antes que o plano esteja validado**.

## A ilusão do "prompt perfeito"

Um erro comum é acreditar que um prompt manual suficientemente longo e detalhado substitui o planejamento. Passar uma especificação extensa misturada com instruções de codificação no mesmo prompt sobrecarrega a atenção do modelo — ele tenta resolver design de dados, lógica de back-end e estilo visual simultaneamente, produzindo código que "parece certo" mas falha sob pressão real.

O SDD resolve isso desacoplando **Planejamento Cognitivo** de **Execução Sintática** em etapas rígidas:

1. Humano e um modelo de raciocínio pesado planejam e modelam o sistema juntos.
2. O resultado vira um documento mestre de especificação, salvo em disco.
3. Só depois de aprovação humana explícita, a codificação é delegada a sub-agentes executores, que usam esse documento como única âncora de verdade.

## Anatomia de um `spec.md` de alta precisão

Um arquivo de especificação não é um manual subjetivo — é um compilador de intenções, com cinco seções puramente acionáveis:

```
1. REQUISITOS & ESCOPO   → o que o sistema deve e NÃO deve fazer
2. MODELO DE DADOS       → esquema exato de tabelas e tipos
3. MAPA DE ARQUIVOS      → onde cada nova lógica será gravada
4. FLUXOS DE INTERAÇÃO   → assinaturas de métodos e APIs, sem código extenso
5. DEFINITION OF DONE    → os testes físicos exatos para aprovação
```

- **Requisitos e não-requisitos:** o que a funcionalidade deve fazer e, criticamente, o que ela **não** deve tentar fazer — evita o inchaço de escopo que confunde o agente.
- **Modelo de dados:** esquema exato, chaves estrangeiras, regras de controle de acesso a nível de linha, migrações necessárias.
- **Mapa físico de arquivos:** onde cada novo arquivo é criado e o que é modificado — impede que o agente crie componentes redundantes em pastas erradas.
- **Fluxos de interação:** assinaturas de interface e contratos de API. A especificação não deve conter código extenso — só as assinaturas vazias que garantem integridade lógica.
- **Definition of Done:** o checklist de testes e asserções que compilador e linter devem aprovar para validar fisicamente a conclusão.

## O loop de planejamento assimétrico ("Opus Plan")

Em vez de um único modelo monolítico para todas as etapas, a orquestração é assimétrica:

- **O arquiteto:** um modelo de raciocínio pesado é instanciado exclusivamente para a fase de planejamento — discute o problema com o humano, debate o design de dados, constrói a especificação. Esse modelo brilha em navegar ambiguidade.
- **O validador hostil (Adversarial Planning Loop):** antes de fechar a versão final, um sub-agente revisor cético — idealmente de proveniência diferente do arquiteto, para evitar viés correlacionado — lê a especificação e tenta ativamente encontrar furos: falhas de concorrência, brechas de segurança, inconsistências de negócio. O arquiteto corrige com base nesse feedback até o plano estar blindado.

## O handoff para execução

Uma vez que o `spec.md` está assinado e salvo em disco, a execução resolve as duas maiores dores do desenvolvimento assistido por IA:

- **Imunidade a Context Bloat:** em vez de manter a mesma thread de planejamento, uma sessão nova e limpa é iniciada; o sub-agente executor lê só o `spec.md` e o código local associado — foco cirúrgico, sem o ruído das discussões conceituais do planejamento.
- **Arbitragem de modelo:** escrever código repetitivo (CRUD, componentes lineares, tratamento de erro) não exige o modelo mais caro. Com uma especificação limpa no repositório, esse trabalho mecânico vai para um modelo mais rápido e barato — a diferença de custo entre os dois é significativa e a especificação já eliminou a ambiguidade que exigiria o modelo mais caro.

## Higiene operacional com Git Worktrees

Para que múltiplos agentes trabalhem em paralelo sobre a mesma especificação sem se atropelar, cada um recebe um worktree físico isolado, roda seus testes localmente, e só depois de validado contra o Definition of Done é que o merge acontece. Ver o padrão completo na skill de Escalabilidade e Infraestrutura desta coleção, se disponível.

## Checklist

- Nenhuma linha de código de produção é escrita antes de o plano existir e ser aprovado por um humano.
- A especificação tem as cinco seções (requisitos, dados, mapa de arquivos, contratos, DoD) — não é um parágrafo livre.
- Um revisor com proveniência distinta do planejador auditou a especificação antes da aprovação final.
- A execução roda em sessão nova, lendo só a especificação — nunca herda o histórico de discussão do planejamento.

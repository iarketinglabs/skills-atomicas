# Adversarial Peer Review

Parte de **Qualidade e Validação** (ver Framework Mental no `SKILL.md`). Aplica a anatomia de loop de `self-verification-loops.md` a um verificador heurístico específico: um segundo agente instruído a ser ceticamente hostil em vez de complacente.

## A falácia do "Looks Right" e o viés de autocrítica

Modelos generativos são otimizados estatisticamente para agradar o usuário e validar suas próprias premissas. Quando o mesmo agente que produziu um artefato é convidado a avaliar o próprio trabalho, o resultado é marcado por um viés severo de bajulação (*sycophancy bias*) — ele tende a classificar sua própria entrega como excelente, negligenciando falhas arquiteturais e furos lógicos.

**Princípio central: o agente que produz o entregável nunca deve ser o agente que o avalia ou valida.** Isso exige desacoplar completamente as duas responsabilidades em sessões/instâncias separadas, sem histórico de contexto compartilhado.

## Arquitetura "Devil's Advocate"

```
SESSÃO 1 — Agente Construtor
  foco: geração rápida do artefato (código, spec, proposta)
        │ gera artefato v1
        ▼
SESSÃO 2 — Agente Adversário (contexto limpo, sem relação com a Sessão 1)
  foco: encontrar ativamente falhas e vulnerabilidades
        │ gera lista de problemas
        ▼
retorna à Sessão 1 para ajuste
```

O agente adversário é instruído explicitamente como um crítico agressivo — sua função é desafiar cada pressuposição lógica, caçar dependências alucinadas, detectar vazamentos potenciais de dados e avaliar impactos de segundo e terceiro grau das alterações propostas.

## O protocolo "Don't Fix, Just Enumerate"

Quando um modelo tenta simultaneamente identificar um problema e codificar a correção no mesmo turno, ele se perde e acaba introduzindo novos bugs. A regra de ouro para manter o revisor no pico de precisão cognitiva: **proibir explicitamente que ele tente corrigir o que encontrar**.

Instrução determinística injetada na sessão do revisor:

> "Leia este artefato como um revisor cético e agressivo que suspeita de cada afirmação, fórmula e número apresentado. Para cada componente, identifique:
> 1. Afirmações ou lógicas sem evidência ou fonte explícita.
> 2. Operações que ignoram regras de controle de acesso a dados ou limites de negócio (ver `row-level-security.md`).
> 3. Inconsistências ou dependências/imports inexistentes.
> 4. Brechas de segurança conhecidas (ex. categorias do OWASP Top 10).
>
> IMPORTANTE: não tente reescrever ou corrigir os erros encontrados. Produza estritamente uma lista numerada de cada inconsistência e falha identificada."

Essa restrição concentra 100% da capacidade do modelo na tarefa cirúrgica de auditoria, em vez de dividi-la entre diagnóstico e correção.

## O ciclo completo: geração, auditoria, correção

```
GERAÇÃO v1 ──► AUDITORIA ADVERSÁRIA ──┐ (se aprovado)
                       ▲               ▼
                       └── (se falhar) SPLIT PARA PR/MERGE
```

1. **Geração do artefato:** o agente construtor escreve a funcionalidade baseado em uma especificação.
2. **O ataque do revisor:** o harness entrega as alterações ao revisor hostil com a instrução "don't fix, just enumerate".
3. **Depuração iterativa:** o harness recebe a lista de erros e a repassa ao construtor: "conserte cada um desses pontos na v2". O ciclo se repete.
4. **Critério de parada:** o loop continua até o revisor retornar aprovação explícita sem ressalvas, respeitando um teto físico de iterações (referência de mercado: 3 a 5) antes de forçar escalonamento para revisão humana — ver `self-verification-loops.md` para a lógica geral de hard stops.

## Sistemas Fusion: consenso multilateral

Para decisões de alto risco (mudanças de esquema de dados, arquitetura multi-tenant), uma variação mais cara do padrão consiste em despachar a mesma tarefa para múltiplos modelos/provedores em paralelo e usar um agente Juiz para consolidar:

- **Analistas:** a mesma consulta é enviada simultaneamente a modelos de proveniências diferentes.
- **Juiz:** um modelo robusto recebe as respostas concorrentes, aponta contradições entre elas, neutraliza alucinações individuais e consolida a melhor abordagem em um relatório único.

Esse padrão elimina a dependência de um único fornecedor/modelo e é reservado a decisões de alto impacto — não é o padrão default por causa do custo (múltiplas chamadas paralelas de modelos caros).

## O guardrail definitivo: a Constraint Library

O momento mais rico de criação de inteligência institucional é justamente quando uma entrega é rejeitada. No modelo ingênuo, a explicação da rejeição some do histórico assim que a sessão é compactada ou encerrada. A solução estrutural:

1. Sempre que uma proposta é rejeitada — por um humano ou pelo revisor adversário —, a causa raiz e a regra violada são documentadas explicitamente.
2. Essa rejeição é persistida no arquivo mestre de regras do repositório (o arquivo de instruções que todo agente lê no início da sessão).
3. Na próxima execução, o agente herda deterministicamente essa nova restrição — o "gosto técnico" da organização escala e sobrevive a trocas de equipe e de modelo.

## Checklist

- Gerador e revisor nunca compartilham a mesma sessão/contexto.
- O revisor recebe a instrução explícita de "não corrigir, apenas enumerar".
- Existe um teto de iterações do ciclo gerador↔revisor antes de escalar para humano.
- Toda rejeição significativa vira uma regra persistida no arquivo mestre de instruções, não se perde no histórico da conversa.

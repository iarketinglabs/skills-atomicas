# O Padrão LLM-as-a-Judge

Fonte canônica única deste padrão — referenciada (não copiada) por `../references/tracing-inputs-outputs.md`, `../references/assertiveness-and-performance-metrics.md`, `../references/audit-loops-os-skills.md` e `../references/human-in-the-loop-approval-gates.md`. O mecanismo que converte avaliação de qualidade — inerentemente subjetiva para uma tarefa de linguagem natural — em um sinal estruturado e automatizável.

## O princípio de independência do Juiz

Um modelo nunca deve avaliar seu próprio trabalho — ele carrega viés de confirmação sobre as escolhas que acabou de fazer. Duas regras de isolamento:

- **Contexto limpo:** o Juiz nunca herda o histórico de raciocínio do agente que produziu o artefato. Recebe estritamente a pergunta original, os dados-fonte relevantes, e o resultado final a avaliar.
- **Família de modelo distinta:** o Juiz deve rodar sob um modelo de proveniência diferente do executor — se o agente que produz roda sob uma família, o avaliador roda sob outra. Isso reduz o risco de "cegueira correlacionada", onde o mesmo tipo de erro passa despercebido porque avaliador e executor compartilham os mesmos pontos cegos.

## A tríade de qualidade (RAG Triad)

Para tarefas que envolvem recuperação de contexto (busca semântica, RAG), o Juiz calcula três scores independentes:

```
                    [ PERGUNTA DO USUÁRIO ]
                          ▲         ▲
              Fidelidade  │         │  Relevância
              ao Contexto │         │  da Resposta
                          │         │
                          ▼         ▼
  [ CONTEXTO RECUPERADO ] ◄───────── [ RESPOSTA DO AGENTE ]
                    Relevância do Contexto
```

1. **Relevância do contexto:** a informação recuperada é de fato pertinente à pergunta original — filtra ruído e documentos obsoletos.
2. **Fidelidade ao contexto (Groundedness):** a resposta se baseia estritamente nos fatos presentes no contexto recuperado. Uma afirmação que não pode ser comprovada pelos documentos injetados é classificada como alucinação.
3. **Relevância da resposta:** o resultado final está alinhado ao problema original — sem desvio de escopo nem evasão.

Para tarefas fora de RAG (ex. auditoria de uma alteração de código no nível do sistema operacional), a mesma estrutura de três eixos se adapta: fidelidade às diretrizes do projeto, alinhamento com o objetivo declarado pelo operador, e relevância cirúrgica da alteração proposta (nada além do necessário).

## O padrão "Enumerate-Only"

Instruir o Juiz a simultaneamente encontrar problemas **e** propor correções degrada sua precisão de diagnóstico — ele se distrai tentando consertar em vez de auditar com rigor. A instrução correta restringe o papel:

> "Você é um auditor cético. Leia a proposta e liste cada inconsistência, desvio ou falha potencial em relação às regras da organização. Não tente corrigir. Apenas enumere as violações."

O relatório de falhas volta ao agente que produziu o artefato original para autocorreção — mantendo a separação de papéis entre quem produz e quem corrige.

## Quatro vereditos, não um binário

Um Juiz limitado a aprovar/rejeitar trava fluxos complexos diante de ambiguidade. O modelo de decisão mais robusto usa quatro saídas possíveis: aprovar, rejeitar, solicitar revisão (com relatório estruturado de ajuste), ou escalar para um operador humano diante de ambiguidade profunda ou comportamento contraditório recorrente.

# Observações da execução sem a skill

## Contexto

- **Data:** 2026-11-20
- **Execuções:** uma resposta independente para cada um dos quatro cenários de `evals.json`.
- **Material apresentado:** as duas bases de conhecimento de arquitetura fornecidas para a criação desta skill.
- **Skill específica:** não foi apresentada ao agente.
- **Limite:** é uma amostra qualitativa única; não permite inferir uma taxa geral de sucesso ou falha.

## Sinais observados

- **Topologia:** o agente escolheu monólito modular para o SaaS e rejeitou “enterprise-grade” como razão suficiente para distribuir o sistema. Explicou custos distribuídos e indicou sinais para rever a decisão. A recomendação foi adequada ao cenário, mas a formulação aproximou equipa pequena e carga baixa de uma regra geral; a skill deve exigir condições do caso e não transformar tamanho de equipa ou volume diário em limiar universal.
- **Agente de compras:** separou autorização do modelo, leitura, rascunho e envio; propôs ACL antes da recuperação, validação, idempotência, revisão humana e auditoria. Estes controles são opções fortes para o impacto descrito, mas devem ser ajustados à política real, sem assumir limites monetários ou infraestrutura específicos.
- **Recuperação:** propôs recuperação híbrida como “padrão” e antecipou custo/latência de contexto longo com base no tamanho do corpus, sem comparar medições. A skill deve manter as opções condicionais e pedir avaliação com tarefas, ACLs e documentos representativos.
- **Auditoria:** distinguiu corretamente histórico de alterações, CQRS e event sourcing, e recomendou solução proporcional aos requisitos descritos.

## Alvos para a skill

Reforçar raciocínio condicionado a evidência, distinção entre requisito e preferência, trade-offs operacionais, controlo de efeitos fora do modelo e validação empírica de escolhas de IA. Não exigir uma topologia predeterminada nem copiar limiares ou recomendações numéricas do material-fonte.


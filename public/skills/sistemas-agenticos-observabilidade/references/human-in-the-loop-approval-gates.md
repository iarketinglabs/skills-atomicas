# Human-in-the-Loop e Portas de Aprovação

Parte de **Observabilidade e Melhoria Contínua** (ver Framework Mental no `SKILL.md`). Como decidir, de forma calibrada e não binária, quando um agente precisa de aprovação humana — e como fazer essa aprovação não travar o throughput da automação.

## A crise do "babysitting"

O modelo mental ingênuo trata o humano como uma ponte de chat: ler cada rascunho, confirmar cada passo elementar, mover contexto manualmente entre janelas. Isso transforma um engenheiro sênior em um operador de micro-decisões irrelevantes (aprovar repetidamente uma leitura de arquivo, por exemplo) — sabotando o ganho de tempo que a automação deveria trazer e gerando fadiga de decisão.

**A abordagem correta:** HITL como parceria assíncrona. O agente executa autonomamente em sandboxes isoladas, empacota progresso e evidências, e só invoca a atenção humana ao atingir uma fronteira determinística de risco ou uma ambiguidade que exige julgamento de negócio — não a cada passo.

## A Escala de Calibração de Autonomia

Diferente da Escala de Confiança por tipo de ação (já detalhada na skill de Segurança e Confiabilidade desta coleção, se disponível — que categoriza o risco de uma ação específica), esta escala calibra **quanto de autonomia um agente ganha ao longo do tempo**, com base em um score de confiança histórica:

| Nível | Score de confiança | Comportamento | Exigência de aprovação |
|---|---|---|---|
| Supervisionado | 0–25% | Só sugere — coleta fontes, monta rascunho para revisão linha a linha | Mandatória em toda ação |
| Guiado | 25–50% | Formula um plano passo a passo, propõe o diff para validação de 1 clique | Parcial — só em transições de fase |
| Assistente | 50–75% | Encadeia ferramentas e sub-agentes na sandbox até o final, entrega pronto para deploy | Gated — leitura livre, ação de escrita externa trava no gate |
| Autônomo | 75–100% | Roda em background, reporta só o sumário e o recibo de auditoria | Excepcional — só transações de alto valor ou desvio estatístico |

O score de confiança sobe conforme o agente acumula histórico de execuções aprovadas sem correção; cai quando uma execução é rejeitada ou corrigida manualmente.

## O padrão "Money Gate"

```
USUÁRIO define a meta
        │
        ▼
ORQUESTRADOR (sandbox, sem chaves locais)
        │ chamada de ferramenta de risco
        ▼
SECURE TOOL BRIDGE ──► APPROVAL REGISTRY (estado: PENDING)
        │
        ▼ dispara requisição de aprovação (canal assíncrono)
NOTIFICAÇÃO PUSH ao operador (com diff/evidências e botões Aprovar/Rejeitar)
        │
        ▼ token de consentimento assinado
retoma a execução automaticamente
```

O harness categoriza cada chamada de ferramenta por reversibilidade de impacto:

- **Baixo impacto (self-approved):** leitura de arquivo, busca semântica, linter — aprovado instantaneamente.
- **Impacto reversível (staged/dry-run):** edição em sandbox, commit em branch de feature, rascunho de e-mail — executa sem intervenção síncrona.
- **Alto impacto irreversível (gated):** envio real de e-mail, alteração estrutural de banco de produção, transação financeira, deploy em produção — o harness congela a execução e dispara aprovação assíncrona fora de banda.

## Implementação de referência: aprovação assíncrona não-bloqueante

```python
class GatedApprovalEngine:
    def __init__(self, state_db):
        self.db = state_db  # persistência local, sobrevive a queda de processo

    async def request_human_gate_approval(self, task_id, payload, timeout=60):
        """Dispara a notificação e aguarda de forma não-bloqueante até o timeout."""
        # em produção: dispara webhook para canal de mensageria com botões interativos
        start = time.time()
        while time.time() - start < timeout:
            status = self.db.get_task_status(task_id)
            if status == "APPROVED":
                return "SUCCESS_APPROVED"
            if status == "REJECTED":
                return "BLOCKED_BY_USER"
            await asyncio.sleep(1)
        return "TIMEOUT_EXPIRED"
```

O estado persiste em disco (não na memória do processo) justamente para sobreviver a uma queda de conexão entre o disparo da aprovação e a resposta do operador — que pode levar minutos ou horas.

## Interrupções como sinal de treino, não só correção pontual

Quando um operador interrompe um agente, rejeita uma proposta, ou edita manualmente um rascunho, ele não está só corrigindo um erro isolado — está fornecendo um rótulo de altíssima precisão sobre preferência organizacional e falha cognitiva do modelo. Cada rejeição deve gerar uma entrada estruturada no repositório de observabilidade, amarrada ao trace que levou àquela decisão — alimentando o ciclo de melhoria contínua (ver `../assets/continuous-improvement-loop.md`).

Um dado empírico relevante: operadores seniores tendem a interromper com frequência sensivelmente maior que usuários novatos — não porque são mais desconfiados, mas porque detectam desvios lógicos mais cedo e corrigem antes que o erro se propague. Alta frequência de interrupção de um usuário experiente é sinal de engajamento ativo, não de falha do sistema.

## Pré-filtro automatizado com Juiz

Depender só de atenção humana para fiscalizar frotas grandes de agentes é um gargalo insolúvel. Um Juiz de IA (contexto limpo, família de modelo distinta) faz uma primeira triagem antes que a notificação chegue ao humano — usando o padrão "enumerate-only" (ver `../assets/llm-as-a-judge-pattern.md`) para listar violações sem tentar corrigi-las. Só propostas que passam nessa triagem, ou que o Juiz classificou como ambíguas, chegam ao operador — reduzindo o volume de ruído.

## Métricas de fricção de HITL

- **Mean Time to React (MTR):** tempo médio entre o disparo da aprovação e a decisão humana. MTR muito alto (dezenas de minutos) indica que o humano virou o gargalo da esteira assíncrona.
- **Interaction Frequency:** número médio de confirmações manuais exigidas para concluir uma tarefa macro — cada "continue" digitado pelo operador é, na prática, um sintoma de que o harness não deu contexto suficiente para o agente prosseguir sozinho.
- **Approval Rejection Rate:** percentual de propostas fisicamente rejeitadas. Acima de ~25% sinaliza desvio cognitivo sistêmico, não um problema pontual.
- **Bypass/YOLO Mode Ratio:** com que frequência operadores desativam as portas de aprovação por insatisfação com bloqueios excessivos — um sinal direto de que o harness está mal calibrado, gerando fadiga em vez de proteção.

## Governança de identidade dos agentes

Todo agente com portas de aprovação ativas deve estar catalogado com um proprietário humano responsável, o escopo de dados que pode ler, e os limites operacionais de escrita — o mesmo diretório de identidade de agente já tratado na skill de Segurança e Confiabilidade desta coleção, se disponível.

## Anti-padrões

- **O Humano-Corredor:** operador copiando saída de uma sessão e colando manualmente em outra para dar continuidade — destrói a portabilidade e a rastreabilidade do sistema.
- **Lazy HITL:** tratar a porta de aprovação como um estágio passivo de leitura, sem canalizar as correções de volta para o aprendizado do agente.
- **Gargalo de thread síncrona:** bloquear toda a frota de agentes esperando uma única confirmação humana, em vez de enfileirar a tarefa pendente e deixar os outros agentes continuarem em paralelo.

## Checklist

- O nível de autonomia de cada agente é calibrado por score histórico, não fixo e binário desde o primeiro dia.
- Ações de baixo/médio impacto rodam livres; só o alto impacto irreversível trava em aprovação síncrona.
- Toda rejeição ou correção humana gera uma entrada rastreável no repositório de observabilidade.
- Um Juiz automatizado faz a primeira triagem antes de qualquer notificação chegar ao operador humano.
- MTR, frequência de interação e taxa de rejeição são monitorados — não só a taxa de aprovação bruta.

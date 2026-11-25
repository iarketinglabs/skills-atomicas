---
name: sistemas-agenticos-arquitetura-software
description: "Use quando for necessário desenhar, rever ou evoluir a arquitetura de um sistema de software, comparar fronteiras e estilos, ou integrar funcionalidades de IA com requisitos de qualidade, segurança, confiabilidade e operação."
metadata:
  short-description: "Decisões de arquitetura de software"
---

# Arquitetura de software

Ajude a tomar decisões arquiteturais adequadas ao problema, às restrições e à capacidade operacional de quem mantém o sistema. A skill é independente de empresa, cliente, fornecedor, linguagem, framework, nuvem e runtime.

Use-a para desenhos de sistema, revisões de arquitetura, decomposição de domínios, escolhas entre estilos, evolução de sistemas existentes e arquitetura de produtos com modelos ou agentes de IA. Para uma alteração pequena de código sem uma decisão arquitetural material, trabalhe diretamente na alteração.

## Método

1. **Enquadre o problema.** Identifique objetivo, pessoas e sistemas envolvidos, capacidades, fluxos críticos, dados sensíveis, contexto existente e limites do trabalho. Separe requisito, restrição, preferência e rótulo aspiracional. Termos como “enterprise-grade”, “AI-native” ou “cloud-ready” só orientam a decisão depois de serem traduzidos em propriedades observáveis.
2. **Torne os atributos de qualidade verificáveis.** Expresse os principais objetivos como cenários: estímulo, contexto, parte afetada, resposta esperada e medida. Use metas fornecidas pelo utilizador. Não invente SLOs, volumes, retenção, obrigações regulatórias ou orçamento; registe-os como perguntas ou pressupostos.
3. **Desenhe fronteiras antes de escolher topologia.** Delimite capacidades de negócio, propriedade dos dados, contratos, dependências, fronteiras de confiança e unidades que precisam de mudar, escalar, falhar ou ser lançadas separadamente.
4. **Compare opções plausíveis.** Apresente duas ou três opções que realmente respondam aos requisitos, incluindo uma opção evolutiva de menor complexidade quando couber. Compare benefícios, custos, riscos e condições de operação. Não trate monólito modular, microserviços, event sourcing, mensageria, RAG, contexto longo ou multiagentes como resposta universal.
5. **Recomende e indique o que poderia mudar a decisão.** Relacione a escolha com os requisitos prioritários, indique incerteza e consequências aceites e defina sinais observáveis para rever a arquitetura. Uma recomendação não precisa de ser irreversível: favoreça opções que preservem caminhos de evolução quando a incerteza for alta.
6. **Planeie verificação e operação.** Mostre como validar as propriedades importantes, observar falhas, recuperar dados/serviços, migrar sem uma mudança abrupta e controlar efeitos externos. Diferencie verificações determinísticas de avaliações de comportamento probabilístico.

Se faltar informação, pergunte apenas pelo que pode mudar materialmente a escolha. Caso contrário, avance com pressupostos explícitos e assinale o que precisa de confirmação.

## Entrega

Adapte o tamanho da resposta ao pedido. Numa decisão relevante, inclua:

- resumo da recomendação e nível de confiança;
- requisitos confirmados, pressupostos e questões em aberto;
- fronteiras e fluxos principais, com um diagrama apenas se reduzir ambiguidade;
- opções comparadas e respetivos trade-offs;
- riscos, falhas previsíveis, operação e segurança;
- plano de validação, evolução e condições para rever a decisão.

Se o desenho incluir um agente com ferramentas ou chamadas encadeadas, explicite também limites de passos, tempo e recursos, condição de término, comportamento em falha e como observar o custo.

Use [assets/architecture-brief-template.md](assets/architecture-brief-template.md) para iniciar um desenho amplo e [assets/adr-template.md](assets/adr-template.md) para registar uma decisão duradoura. A lista de revisão está em [assets/architecture-review-checklist.md](assets/architecture-review-checklist.md); o diagrama editável está em [assets/system-context-template.mmd](assets/system-context-template.mmd).

## Referências por necessidade

Leia apenas o material relevante para a decisão ativa:

- Para transformar objetivos em critérios de decisão: [references/decision-method.md](references/decision-method.md).
- Para limites de domínio, estilos, contratos, dados e integração: [references/styles-and-boundaries.md](references/styles-and-boundaries.md).
- Se o sistema usar modelos, recuperação de conhecimento ou agentes: [references/ai-enabled-systems.md](references/ai-enabled-systems.md).
- Para disponibilidade, segurança, observabilidade e operação: [references/reliability-security-operations.md](references/reliability-security-operations.md).
- Para documentação, migração e governança evolutiva: [references/documentation-and-evolution.md](references/documentation-and-evolution.md).
- Para fundamentar afirmações e verificar conteúdo que muda com o tempo: [references/evidence-and-freshness.md](references/evidence-and-freshness.md).

## Regras de decisão

- Escolha a arquitetura pelos atributos de qualidade, domínio, risco, restrições e operação exigidos; popularidade não é evidência de adequação.
- A distribuição introduz latência, falhas parciais, contratos entre versões, consistência e carga operacional. Exija um benefício concreto que compense esses custos.
- Separe CQRS de event sourcing. Auditoria, histórico de alterações e reversão podem ser atendidos sem usar eventos como fonte de verdade.
- Em sistemas com IA, trate a saída do modelo como probabilística. Identidade, autorização, validação de entrada/saída e transições de estado que precisam de garantia devem ser aplicadas por componentes verificáveis fora do modelo.
- Em fluxos de agentes, defina limites adequados de passos, tempo e recursos, uma condição de término e o comportamento seguro perante falhas de modelos ou ferramentas.
- Dê às ferramentas e aos agentes apenas os dados e as ações necessários. Avalie o risco de conteúdo não confiável, acesso a dados privados e efeitos externos no mesmo fluxo.
- Evals complementam testes unitários, integração, contratos, monitorização e revisão humana; não os substituem.
- Distinga factos observados, sínteses, hipóteses e recomendações. Para versões de protocolos, normas, preços, capacidades de fornecedores ou orientações de segurança atuais, confirme fontes oficiais vigentes antes de afirmar que estão atualizadas.


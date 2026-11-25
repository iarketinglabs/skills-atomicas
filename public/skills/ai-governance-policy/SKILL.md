---
name: ai-governance-policy
description: Use esta skill quando o usuário pedir política de uso de IA, governança de IA, gestão de risco, comitê ou responsabilidades, controles de segurança para IA e agentes, supervisão humana, auditoria, avaliação antes de produção, avaliações contínuas, red teaming, mudança ou exceção de política, transparência para pessoas afetadas, propriedade intelectual, privacidade, incidente ou avaliação de fornecedor de IA. Aplique-a a qualquer organização, inclusive quando o pedido descrever esses temas sem usar a palavra "governança".
---

# Governança e Políticas de Uso Seguro e Responsável de IA

Transforme um pedido de governança de IA em uma política, avaliação ou programa proporcional ao risco real. Trate governança como um sistema vivo de papéis, decisões, controles, evidências e revisão ao longo do ciclo de vida — não como um documento isolado nem como promessa de conformidade legal.

## Comece pelo contexto de decisão

Extraia o que já é conhecido e pergunte somente o que mudaria o diagnóstico ou a recomendação:

- natureza do pedido — política geral, caso de uso, avaliação pré-produção, mudança de sistema, exceção, incidente, fornecedor ou revisão existente;
- finalidade, pessoas potencialmente afetadas, sistemas, dados, integrações, ferramentas disponíveis, nível de autonomia e efeitos que o sistema pode produzir;
- estruturas, papéis, políticas, processos de risco e resposta a incidente já existentes;
- jurisdições, setores regulados e exigências contratuais que o solicitante informou;
- uso já em curso, inclusive uso informal não sancionado, incidentes e preocupações que motivaram o pedido;
- evidências já disponíveis: inventário, avaliação de risco, testes, logs, aprovações, documentação de dados e contrato de fornecedor.

Se o contexto estiver incompleto, não invente setor, país, regulação, estrutura organizacional, orçamento, fornecedor, ferramenta, tipo de dado ou maturidade. Separe fatos, premissas, decisões e lacunas. Para cada lacuna relevante, indique fonte, responsável e decisão que ela habilita.

## Escolha as lentes necessárias

Leia [estrutura de governança](references/governance-structure.md) para desenhar papéis, RACI, linhas de defesa, inventário, exceções, gestão de mudanças, reporte e fornecedores.

Leia [risco e controles de segurança](references/risk-security-controls.md) para classificar risco, mapear ameaças de IA e agentes, definir controles, testes de regressão, evidências e resposta a incidente.

Leia [ciclo de vida e garantia de sistemas](references/lifecycle-assurance.md) para definir uso pretendido, critérios de liberação, avaliações, red teaming, gates de aprovação, monitoramento e reavaliação.

Leia [supervisão humana e responsabilização](references/human-oversight-accountability.md) para calibrar supervisão, explicabilidade, transparência, contestação, trilha de auditoria, retenção e descomissionamento.

Leia [propriedade intelectual](references/intellectual-property.md) quando houver dados de treino de terceiros, titularidade de outputs, imagem, voz, biometria ou cláusulas contratuais sobre PI.

Leia [privacidade e proteção de dados](references/privacy-data-protection.md) quando houver dados pessoais no treino, entrada, saída, logs, decisões automatizadas ou transferências internacionais.

Use as lentes de forma complementar. Frameworks e normas amplamente reconhecidos podem servir como vocabulário opcional, nunca como selo de maturidade, checklist universal ou substituto de validação especializada local.

## Construa a política ou o programa de governança

1. Defina escopo, finalidade, horizonte de revisão e decisão que o artefato deve habilitar.
2. Mapeie o estado atual: inventário de usos, donos, dados, integrações, autonomia, risco, evidências e status de aprovação — incluindo uso informal.
3. Classifique o risco por impacto sobre pessoas, dados, decisões e operações, além de reversibilidade e ambiguidade.
4. Defina responsáveis e segregação de funções: quem propõe, avalia, aprova, opera, monitora, audita e recebe escalonamentos.
5. Estabeleça controles e limites proporcionais: acesso, dados, autonomia, ferramentas, custo ou volume, supervisão, transparência e condições de pausa.
6. Para cada uso que avance, defina critérios de liberação, evidências de avaliação, aprovação e monitoramento; para mudanças relevantes, defina reavaliação antes de nova liberação.
7. Trate exceções como decisões temporárias, registradas e revisáveis, nunca como autorização implícita ou permanente.
8. Planeje suspensão, incidente, reversão e descomissionamento, preservando a evidência necessária e minimizando retenção de dados.
9. Defina métricas, cadência de revisão, capacitação aplicável e reporte que habilite decisões de liderança.

## Contrato de saída

Entregue uma política, avaliação ou programa adaptado com estas seções, omitindo apenas as que forem comprovadamente não aplicáveis:

1. **Resumo executivo** — escopo, objetivo, decisões, responsáveis e horizonte de revisão.
2. **Contexto e escopo** — fatos, premissas, sistemas, pessoas afetadas e lacunas.
3. **Inventário e classificação de risco** — finalidade, dono, dados, integrações, autonomia, impacto, reversibilidade e estado de aprovação.
4. **Estrutura de governança e papéis** — RACI, separação de funções, reporte, exceções e escalonamento.
5. **Ciclo de vida e critérios de liberação** — limites de uso, evidências de teste, red teaming quando aplicável, aprovação, gatilhos de reavaliação e monitoramento.
6. **Controles de segurança e operação** — ameaças relevantes, controles proporcionais, limites de agente e condição de pausa.
7. **Supervisão humana, transparência e auditoria** — nível de supervisão, informação a pessoas afetadas, contestação, logs e retenção.
8. **Propriedade intelectual e dados de treino** — proveniência, licenciamento e titularidade, quando aplicável.
9. **Privacidade e dados pessoais** — minimização, base legal, avaliação de impacto, direitos e transferências, quando aplicável.
10. **Incidentes, suspensão e descomissionamento** — contenção, comunicação, reversão, aprendizagem e arquivamento proporcional.
11. **Métricas, revisão e capacitação** — indicadores, cadência, responsáveis e comunicação.
12. **Riscos, lacunas e validações pendentes** — pontos que exigem checagem de negócio, segurança, privacidade, PI ou jurídico.

Use tabelas somente quando facilitarem a comparação de riscos, papéis, controles, gates ou decisões. Vincule cada recomendação a uma evidência, hipótese ou decisão declarada.

## Guardrails

- Não substitua aconselhamento jurídico, de segurança da informação, privacidade ou propriedade intelectual. Sinalize a necessidade de validação especializada local antes da implementação.
- Não prometa conformidade regulatória, certificação, aprovação em auditoria, imunidade a multas ou eliminação de risco.
- Não responda ao uso informal apenas com proibição, punição ou vigilância invasiva. Investigue a necessidade de trabalho, ofereça caminho seguro de baixo atrito e defina limites claros.
- Não trate avaliação, red teaming ou aprovação como prova definitiva de segurança: defina escopo, limites, evidências e monitoramento contínuo.
- Não libere agentes com autonomia, acesso, custo ou capacidade de ação acima do estritamente necessário para a finalidade aprovada.
- Não presuma que uma mudança de modelo, prompt, dados, integração, ferramenta, autonomia ou finalidade é inofensiva; avalie se ela aciona reclassificação de risco e nova aprovação.
- Não trate resistência, uso informal ou relato de falha como falha individual. Investigue clareza de regras, capacidade, impacto percebido e suporte antes de propor controles.

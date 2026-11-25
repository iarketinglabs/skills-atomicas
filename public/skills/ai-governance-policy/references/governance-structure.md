# Estrutura de Governança

Use esta referência para desenhar quem decide, quem executa e quem audita o uso de IA em uma organização. Ela não substitui aconselhamento jurídico, de compliance ou de segurança aplicável ao contexto.

## Princípio de base

Governança de IA é a resposta organizacional à pergunta "quem faz o quê, quando e como" ao longo do ciclo de vida de um sistema de IA — da concepção ao descomissionamento. Um sistema não falha só por defeito técnico; falha também quando a finalidade do uso não foi delimitada, quando ninguém é formalmente responsável pelo resultado, ou quando a mudança de escopo não passa por revisão. Sem um inventário formal de sistemas e usos de IA, nenhum programa de governança é possível: não se mitiga o risco de um ativo cuja existência a organização desconhece.

## Estrutura de decisão

Desenhe a estrutura proporcional ao risco identificado, não ao tamanho da organização. Elementos recorrentes:

- **Responsável central** — uma pessoa ou comitê formalmente designado como dono da governança de IA, mesmo que a execução seja distribuída. Pode ser um comitê multidisciplinar (dados, segurança, jurídico, negócio, privacidade) ou, em estruturas menores, uma função existente com esse mandato explícito.
- **Dono de cada sistema ou caso de uso** — alguém responsável por cada sistema de IA em produção, não apenas pela governança geral. Evita a lacuna em que múltiplas equipes contribuem para um modelo e ninguém responde por ele.
- **Separação de funções** — quem constrói ou opera um sistema de IA não deveria ser a única instância que aprova seu uso em produção. Isso evita conflito de interesse entre entrega e controle.

| Papel | Foco típico | Não deve ser confundido com |
| --- | --- | --- |
| Dono do sistema/caso de uso | Responde pelo resultado e pela conformidade de um uso específico | Quem apenas opera o sistema no dia a dia |
| Comitê ou responsável de governança | Define política, aprova exceções, revisa risco agregado | Auditoria independente |
| Auditoria interna ou revisão independente | Verifica se os controles definidos estão de fato em funcionamento | O próprio comitê que desenhou os controles |

## Modelo de três linhas

Um modelo recorrente para distribuir responsabilidade sem sobrecarregar uma única função:

1. **Primeira linha (operação e desenvolvimento)** — equipes que constroem ou usam o sistema no dia a dia; responsáveis pelo cumprimento operacional dos controles definidos e por documentar decisões técnicas.
2. **Segunda linha (risco, segurança, privacidade, compliance)** — avalia a eficácia dos controles, mantém o inventário de sistemas de IA, define o apetite de risco e apoia a primeira linha sem executar no lugar dela.
3. **Terceira linha (auditoria independente)** — verifica, sem conflito de interesse, se o programa de governança está de fato em execução; reporta a instâncias superiores à segunda linha.

Trate este modelo como uma forma de distribuir responsabilidade, não como estrutura obrigatória: organizações pequenas podem concentrar as três linhas em menos pessoas, desde que a separação de funções essencial (quem constrói não é o único que aprova) seja preservada.

## Inventário de sistemas de IA e uso informal

Mantenha um registro vivo de todo sistema de IA em uso — incluindo módulos de IA embutidos silenciosamente em ferramentas de terceiros e uso informal não sancionado (shadow AI). Inventários que dependem apenas de aprovação formal tendem a subestimar significativamente o uso real. Para cada sistema ou uso registrado, documente: finalidade, dono, dados envolvidos, nível de autonomia, classificação de risco e status de revisão.

Trate a descoberta de uso não sancionado como sinal de necessidade de trabalho não atendida, não apenas como violação a punir — ver [supervisão humana e responsabilização](human-oversight-accountability.md) e o tratamento de risco em [risco e controles de segurança](risk-security-controls.md) para a resposta proporcional.

## Avaliação e cláusulas contratuais de fornecedores

A cadeia de suprimentos de IA (modelos de terceiros, provedores de nuvem, subcontratados) introduz risco que a organização não controla diretamente:

- **Due diligence antes de contratar** — solicite documentação sobre dados de treino, limitações conhecidas e testes de viés do sistema (ver também [propriedade intelectual](intellectual-property.md)); verifique se o fornecedor passa por auditoria independente relevante ao contexto.
- **Auditoria de subprocessadores** — quando o fornecedor delega parte do processamento a terceiros, avalie também essa cadeia estendida, especialmente quando dados pessoais estão envolvidos.
- **Cláusulas contratuais recomendadas** — transparência sobre mudanças relevantes no sistema; indenização por danos originados no sistema do fornecedor (vazamento, viés, violação de direitos de terceiros); plano de continuidade caso o fornecedor interrompa o serviço.

Nenhuma cláusula contratual substitui a avaliação jurídica do contrato específico; trate esta seção como pauta de pontos a levar à revisão jurídica, não como texto contratual pronto.

## Reporte à liderança

Estruture o reporte de risco de IA nos mesmos moldes de outros riscos corporativos relevantes (segurança da informação, financeiro): métricas periódicas sobre sistemas em produção, incidentes, status de auditorias e progresso de iniciativas de governança, revisadas por quem tem autoridade para decidir sobre risco. Evite relatórios que apenas descrevem atividade sem habilitar uma decisão — cada indicador reportado deveria mudar algo se subir, cair ou não puder ser medido.

## Evidência externa

Quando usar benchmark, norma ou orientação externa, registre fonte, data, jurisdição e aplicabilidade antes de tratá-la como referência válida para o caso.

Como vocabulário de referência (não checklist de conformidade): sistemas de gestão de IA certificáveis (como a família ISO/IEC 42001) descrevem uma estrutura de gestão organizacional com liderança executiva, auditoria interna contínua e melhoria do sistema; frameworks de gestão de risco (como o NIST AI RMF) organizam a resposta em funções de governar, mapear, medir e gerenciar; princípios internacionais de IA (como os da OCDE) reforçam a exigência de linhas de responsabilidade claras. Cite-os apenas para situar a conversa com quem já os conhece — a aplicabilidade exata, os requisitos formais e qualquer alegação de conformidade exigem sempre validação jurídica e de segurança local.

## RACI, exceções e mudanças

Para cada sistema ou caso de uso relevante, registre um RACI enxuto: quem é responsável pela execução, quem responde pela decisão final, quem precisa ser consultado e quem deve ser informado. Inclua as decisões de classificação de risco, liberação, alteração material, suspensão, exceção e descomissionamento. O objetivo é tornar o escalonamento acionável, não multiplicar aprovações sem propósito.

Mantenha um registro de exceções à política ou aos controles. Cada entrada deve conter justificativa, dono que aceita o risco, controles compensatórios, data de validade, gatilho de revisão e resultado da revisão. Trate mudança de finalidade, dados, modelo, integração, permissões, autonomia ou impacto potencial como candidata a reavaliação antes da nova liberação; veja [ciclo de vida e garantia de sistemas](lifecycle-assurance.md).

## Capacitação e canais de relato

Defina orientação e capacitação proporcionais ao papel e ao risco: regras de dados, limites de autonomia, supervisão, como registrar uma preocupação e quando interromper ou escalar um sistema. Mantenha canais acessíveis para relato de falhas, uso informal e dúvidas, sem tratar o relato de boa-fé como motivo de punição. Use os relatos e o inventário para melhorar os caminhos aprovados e reduzir a recorrência de exceções.

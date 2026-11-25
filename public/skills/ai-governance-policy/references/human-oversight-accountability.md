# Supervisão Humana e Responsabilização

Use esta referência para calibrar o nível de supervisão humana sobre um sistema de IA e para desenhar a trilha de auditoria que sustenta a responsabilização pelo resultado. Ela não substitui aconselhamento jurídico sobre responsabilidade legal em um caso concreto.

## Princípio de base

Delegar uma tarefa a um sistema de IA não transfere a responsabilidade pelo resultado — a organização continua respondendo pelas decisões tomadas com apoio ou por meio de IA. Isso torna a supervisão humana e a capacidade de explicar uma decisão elementos centrais de governança, não um extra opcional.

## Níveis de supervisão humana

Calibre o nível de supervisão pelo risco identificado (ver [risco e controles de segurança](risk-security-controls.md)), não uniformemente para todos os usos:

| Nível | Descrição | Quando considerar |
| --- | --- | --- |
| Humano no comando (HIC) | A pessoa decide usar o sistema e mantém autoridade plena sobre quando e como | Uso de baixo impacto, apoio a tarefa individual |
| Humano no laço (HITL) | Cada saída relevante passa por aprovação humana antes de gerar efeito | Impacto moderado a alto, decisões que afetam terceiros |
| Humano sobre o laço (HOTL) | O sistema opera com autonomia, mas humano monitora e pode intervir a qualquer momento | Alto volume operacional com necessidade de revisão amostral contínua |
| Não delegável | A decisão permanece exclusivamente humana; IA no máximo apoia com informação | Decisões de alto impacto, baixa reversibilidade ou que envolvem direitos fundamentais |

Sistemas de alto impacto e baixa reversibilidade normalmente exigem, no mínimo, supervisão HOTL contínua, com possibilidade de intervenção imediata (um mecanismo equivalente a um botão de interrupção) — e frequentemente exigem HITL ou não delegação, dependendo do que está em jogo.

## Explicabilidade e trilha de decisão

Mesmo quando o sistema é operacionalmente uma caixa-preta, a organização deveria conseguir reconstruir, para uma decisão relevante: qual sistema e versão foram usados, quais dados de entrada e contexto alimentaram a decisão, qual foi a saída, e quem revisou ou aprovou. Isso permite responder a questionamentos internos, de titulares afetados ou de auditoria sem depender de memória institucional.

Boas práticas recorrentes:

- Documentar a versão do sistema em uso e quando ela mudou, com o motivo da mudança.
- Registrar entradas e saídas de decisões relevantes pelo tempo necessário para investigação e resposta a questionamentos, equilibrando isso com minimização de dados pessoais (ver [privacidade e proteção de dados](privacy-data-protection.md)).
- Manter, para decisões de alto impacto, um resumo compreensível dos fatores que pesaram na saída — mesmo que não seja uma explicação matemática completa do modelo.

## Auditoria interna

Trate a auditoria de sistemas de IA como extensão da auditoria de risco já existente, não como disciplina isolada: verificação periódica de que os controles definidos estão de fato em funcionamento, feita por quem não desenhou o controle nem opera o sistema no dia a dia. A cadência apropriada depende do risco do sistema — uso de alto impacto justifica revisão mais frequente que uso de baixo impacto.

## Retenção de logs e descomissionamento

Ao encerrar o uso de um sistema de IA:

- **Não apague sem registro** — antes de desligar ou substituir um sistema, preserve documentação suficiente (versão, propósito, métricas de desempenho, decisões relevantes que ele produziu) para responder a uma auditoria ou questionamento futuro sobre decisões passadas.
- **Defina prazo de retenção deliberado** — equilibre a necessidade de investigar decisões passadas com o princípio de minimização de dados pessoais; não retenha indefinidamente por padrão.
- **Documente a decisão de descomissionar** — motivo, data, o que substitui o sistema e onde a documentação arquivada pode ser encontrada.

## Prestação de contas a executivos

Garanta que haja um canal formal pelo qual riscos e incidentes de IA cheguem a quem tem autoridade para decidir — não apenas relatórios técnicos que ficam na equipe de desenvolvimento. Isso inclui métricas de sistemas em produção, status de auditorias e incidentes relevantes, revisados com cadência definida.

## Evidência externa

Quando usar benchmark, norma ou orientação externa sobre responsabilização e supervisão humana, registre fonte, data e jurisdição antes de tratá-la como aplicável ao caso.

Como vocabulário de referência (não checklist de conformidade): princípios internacionais de IA (como os da OCDE) descrevem a expectativa de que organizações mantenham linhas claras de responsabilidade e mecanismos de reparação; regulações de alto risco em algumas jurisdições exigem explicitamente meios técnicos para que um operador humano compreenda e possa reverter uma decisão automatizada. Cite-os para situar a conversa com quem já os conhece — a exigência formal exata depende sempre da jurisdição e do setor, e exige validação jurídica local.

## Transparência, contestação e correção

Quando uma pessoa puder ser afetada de forma relevante por um uso de IA, avalie que informação compreensível ela precisa receber sobre o papel do sistema, seus limites, a supervisão disponível e o caminho para pedir revisão. Não presuma que uma divulgação padrão é suficiente: calibre linguagem, canal, momento e detalhe pelo impacto e pelo público.

Defina como uma contestação, queixa ou indício de dano será recebido, registrado, analisado, respondido e usado para corrigir o sistema ou a decisão. A pessoa ou equipe que revisa deve ter autoridade e informação suficientes para intervir; encaminhar um caso para uma fila sem poder real de correção não configura supervisão efetiva.

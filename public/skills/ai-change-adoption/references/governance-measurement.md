# Governança e Medição

Use esta referência para desenhar adoção responsável e aprendizagem baseada em evidência. Ela não substitui avaliação jurídica, de segurança, trabalhista, privacidade ou conformidade aplicável ao contexto.

## Governança proporcional ao risco

Classifique o uso pelo impacto potencial sobre pessoas, dados, decisões e operações. A classificação deve orientar controles e responsáveis, não bloquear toda experimentação.

| Perfil de uso | Exemplo abstrato | Controles proporcionais |
| --- | --- | --- |
| Baixo impacto | apoio a tarefa sem dado sensível ou decisão relevante | orientação de uso, registro básico, revisão do responsável pelo trabalho |
| Impacto moderado | produção que informa decisão ou usa informação interna | escopo aprovado, limites de dados, revisão humana, monitoramento de qualidade e canal de incidente |
| Alto impacto | automação que afeta pessoas, recursos, acesso ou operação crítica | avaliação especializada, autoridade definida, testes, rastreabilidade, supervisão humana, condição de pausa e revisão periódica |

Documente para cada caso: propósito, público afetado, dados e permissões, autonomia, decisão humana, responsável, limites, risco, evidência de teste, monitoramento e mecanismo de pausa.

Ao classificar o impacto, considere também dois eixos que ajudam a calibrar o nível de autonomia apropriado: a **reversibilidade** da decisão ou ação (o quanto é fácil corrigir se algo sair errado) e a **ambiguidade** da tarefa (o quanto o contexto disponível é suficiente para uma decisão segura). Uma tarefa de impacto moderado, mas baixa reversibilidade ou alta ambiguidade, pode justificar julgamento humano mesmo sem se qualificar como "alto impacto" pela tabela acima.

Quando o contexto pedir granularidade maior do que baixo/moderado/alto, uma escala alternativa de cinco níveis de autonomia pode ajudar a mapear tarefas específicas — use-a como opção, não como substituição obrigatória da tabela anterior:

| Nível | Descrição | Supervisão típica |
| --- | --- | --- |
| 1 | Autônomo com auditoria por amostra | Revisão periódica de amostras, sem aprovação prévia |
| 2 | Autônomo com revisão prévia | Resultado passa por checagem antes de sair do fluxo interno |
| 3 | Copilotado (construção conjunta) | Humano e IA ajustam o resultado em ciclos curtos antes de finalizar |
| 4 | Revisão humana obrigatória | Toda saída é aprovada por uma pessoa responsável antes de uso ou publicação |
| 5 | Não delegável | Decisão permanece exclusivamente humana; IA no máximo apoia com informação |

## Uso informal de IA

Trate uso informal como informação sobre necessidade, atrito ou falta de caminho aprovado. Investigue sem pressupor culpa:

1. que tarefa motivou o uso e qual resultado a pessoa buscava;
2. que dados, acesso, ferramentas e decisões estiveram envolvidos;
3. quais riscos ou incidentes ocorreram ou poderiam ocorrer;
4. por que o caminho seguro era inexistente, desconhecido ou inviável;
5. qual alternativa segura, suporte ou ajuste de processo reduziria reincidência.

Defina limites claros de dados, autorização, revisão e escalonamento. Não recomende vigilância invasiva, coleta desnecessária de dados pessoais ou punição como resposta padrão.

Organize a resposta em três camadas complementares, sem depender de uma só:

- **Tecnológica:** dê visibilidade sobre quais ferramentas e fluxos de dados já estão em uso, com controles técnicos proporcionais (ex.: limites de acesso, prevenção de vazamento de dados sensíveis) — sem monitorar conteúdo pessoal além do necessário.
- **Processual:** ofereça um caminho aprovado de baixo atrito antes de proibir o informal, e audite periodicamente custo, ferramentas e uso para detectar desvio de política cedo.
- **Cultural:** habilite o uso seguro com comunicação clara sobre o que pode e não pode ser feito, e trate a descoberta de uso informal como oportunidade de ajustar o caminho oficial, não apenas de reforçar a regra.

## Métricas e linha de base

Comece com uma pergunta de decisão: o que será alterado se o indicador subir, cair ou não puder ser medido? Registre fonte, período, população, definição, denominador, limitação e responsável.

| Camada | Pergunta | Exemplos de evidência |
| --- | --- | --- |
| Adoção | A prática está sendo usada no fluxo previsto? | ativação, frequência contextual, conclusão assistida, uso do caminho aprovado |
| Comportamento | O trabalho foi executado de modo diferente e seguro? | observação, amostra revisada, autoavaliação triangulada, cumprimento de revisão |
| Qualidade | A saída ou decisão atende ao critério definido? | taxa de erro, retrabalho, avaliação humana, exceções e reclamações |
| Valor | O fluxo gerou resultado relevante para o objetivo? | tempo de ciclo, capacidade, custo, receita, experiência ou risco evitado, conforme evidência disponível |
| Segurança | Os controles e limites estão funcionando? | incidentes, quase-incidentes, escalonamentos, cobertura de revisão e achados de auditoria |

Não transforme correlação em causalidade. Se não houver linha de base ou atribuição confiável, descreva a limitação e proponha uma comparação ou coleta viável.

## Aprendizagem e revisão

Estabeleça uma cadência compatível com a mudança. Em cada revisão, compare evidência com hipótese, decida manter, ajustar, pausar ou expandir e registre o motivo. Revise também efeitos distribuídos: uma melhoria local pode transferir custo, risco ou carga cognitiva para outro público.

Inclua explicitamente na revisão dois efeitos que só aparecem com o tempo: **fadiga por auditoria constante** (quando supervisionar volume alto de saídas de IA desgasta a atenção e a qualidade do julgamento de quem revisa) e **atrofia de habilidade** (quando delegação extensa sem prática deliberada reduz a capacidade da equipe de executar ou avaliar criticamente a tarefa). Nenhum dos dois aparece nas métricas de adoção ou produtividade isoladamente — exigem observação direta ou relato de quem executa.

Use um registro de decisão:

| Decisão | Evidência | Incerteza | Responsável por papel | Próxima revisão | Condição de pausa ou ajuste |
| --- | --- | --- | --- | --- | --- |
| [decisão] | [fonte] | [limite] | [papel] | [momento] | [sinal observável] |

## Evidência externa

Quando usar benchmark, estatística, norma ou orientação externa, registre fonte primária ou adequada, data, jurisdição, população, método e aplicabilidade. Trate informação temporal como contexto a verificar; não a use para prometer resultado, atestar conformidade ou prescrever um controle sem validação local.

Como vocabulário de referência (não checklist de conformidade), normas amplamente reconhecidas de governança de IA descrevem elementos parecidos com os desta seção: sistemas de gestão de IA como a ISO/IEC 42001 tratam competência documentada das pessoas envolvidas como parte da governança, e frameworks de gestão de risco como o NIST AI RMF organizam a resposta em funções de governar, mapear, medir e gerenciar. Cite-os apenas para situar a conversa com quem já os conhece; a aplicabilidade, os requisitos exatos e a exigência de conformidade formal exigem sempre validação jurídica e de segurança local, como já indicado nos guardrails da skill.

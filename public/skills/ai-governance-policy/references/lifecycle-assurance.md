# Ciclo de Vida e Garantia de Sistemas de IA

Use esta referência para transformar a governança de um sistema ou agente em decisões verificáveis antes, durante e depois de sua operação. Ela não substitui testes técnicos, validação de segurança ou avaliação especializada do contexto real.

## Uso pretendido e limites operacionais

Antes de aprovar um sistema, registre o que ele pode fazer e o que não pode fazer: finalidade, público, decisões apoiadas ou executadas, pessoas afetadas, dados permitidos e proibidos, fontes confiáveis e não confiáveis, integrações, ferramentas, nível de autonomia e efeitos reversíveis ou irreversíveis.

Defina limites mensuráveis ou verificáveis para a operação quando forem relevantes: permissões, destinos de ação, volume, frequência, custo, critérios de escalonamento e condição de pausa. Um agente só deve receber a identidade, os acessos e a capacidade de ação necessários para a finalidade aprovada.

## Avaliação antes da liberação

Defina critérios de aceitação adequados ao risco antes de colocar o sistema em produção. Combine, conforme o caso:

- avaliação de qualidade e adequação ao uso pretendido, com casos representativos e casos de limite;
- teste de segurança, privacidade, tratamento de dados e respeito aos limites de ferramenta e autonomia;
- teste de robustez diante de entradas incompletas, ambíguas, adversariais ou não confiáveis;
- avaliação de comportamento, vieses ou efeitos indevidos sobre pessoas potencialmente afetadas;
- validação humana de resultados ou ações relevantes antes da liberação.

Mantenha evidências suficientes para reconstruir o que foi avaliado: versão do sistema e das configurações relevantes, dados ou cenários de teste permitidos, critérios de aceitação, resultados, limitações conhecidas, responsáveis e decisão de aprovação ou rejeição. Não apresente uma bateria de testes como garantia de ausência de falhas.

## Red teaming proporcional

Use red teaming para simular falhas e abuso plausíveis no contexto real, principalmente quando o sistema consome conteúdo não confiável, acessa dados restritos, aciona ferramentas ou produz efeitos sobre terceiros. Priorize vetores relevantes, como manipulação de entrada, uso indevido de ferramentas, exfiltração de dados, corrupção de conhecimento, escalonamento de permissões, contorno de limites e ações repetidas ou fora do escopo.

Documente cenário, resultado, severidade, controle testado, limitação residual e decisão de correção, aceitação temporária ou bloqueio. Não execute testes que possam causar dano real sem autorização, ambiente controlado e salvaguardas proporcionais.

## Gates, mudanças e exceções

Um gate de liberação deve indicar: dono do sistema, risco aceito, limites de uso, evidências mínimas, responsável pela aprovação, plano de monitoramento e condição de suspensão. A aprovação deve ser independente de quem construiu ou opera o sistema quando o risco justificar essa separação.

Reavalie o sistema antes de nova liberação quando mudar finalidade, público, dados, modelo, prompt ou configuração material, fonte de conhecimento, integração, permissões, autonomia, volume, custo, supervisão ou impacto potencial. Registre a decisão, a evidência nova e a reversibilidade da mudança.

Exceções devem ter justificativa, dono que aceite o risco, controles compensatórios, prazo de validade, gatilho de revisão e possibilidade de revogação. Uma exceção não substitui a aprovação regular nem se torna regra por inércia.

## Operação, monitoramento e encerramento

Monitore os sinais associados ao risco do sistema: qualidade, falhas, comportamento inesperado, ações executadas, acesso a dados, violações de limite, incidentes, queixas e alterações de contexto. Defina quem responde ao alerta, quando interromper o sistema e como preservar evidência para investigação.

Ao suspender, reverter ou descomissionar, registre motivo, data, responsável, impacto, substituição e destino da documentação. Preserve somente a evidência necessária para auditoria, contestação ou investigação, com retenção proporcional e proteção dos dados pessoais envolvidos.

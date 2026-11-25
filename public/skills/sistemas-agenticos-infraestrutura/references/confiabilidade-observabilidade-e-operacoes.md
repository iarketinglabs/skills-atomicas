# Confiabilidade, observabilidade e operações

Use esta referência para traduzir confiabilidade em resultados mensuráveis, detectar falhas úteis para o operador e estabelecer recuperação antes de depender de automação.

## SLI, SLO e orçamento de erro

Comece pela experiência que importa: sucesso da tarefa, latência, disponibilidade, frescor ou consistência. Defina janela, população e método de medição; use metas fornecidas pelo usuário. Um SLO serve para orientar trade-offs e ação operacional, não para prometer disponibilidade absoluta.

Associe cada alerta a uma condição observável, impacto, responsável e próximo passo. Alertas sem ação ou sem impacto claro aumentam ruído. Erro em dependência externa pode consumir um objetivo mesmo que os servidores locais estejam saudáveis.

## Métricas, logs e traces

- **Métricas:** tendências e agregações; acompanhe taxa, erros, duração, saturação, filas e uso.
- **Logs:** eventos detalhados com contexto, acesso restrito e retenção definida.
- **Traces:** caminho distribuído e dependências de uma operação.
- **Eventos de domínio:** transições que explicam o estado do trabalho e da recuperação.

Use correlação de operação sem colocar credenciais, conteúdo sensível ou payloads completos em etiquetas de alta cardinalidade. Defina retenção, redaction, acesso e exportação antes de habilitar captura de conteúdo.

Em sistemas agênticos, observe separadamente chamadas de modelo, ferramentas, filas, handoffs e resultado final. Evite tratar contadores que se sobrepõem como soma de tokens, tarefas ou duração sem entender a semântica.

## Resiliência operacional

Defina timeouts por dependência, limite de tentativas, backoff, jitter, idempotência e dono do retry. Evite retry em várias camadas sem coordenação. Sob sobrecarga, considere limites de concorrência, rate limiting, filas, load shedding ou degradação com resultado útil.

Descreva resposta a incidente com detecção, contenção, recuperação, comunicação e aprendizado. Teste runbooks e caminhos de recuperação em condições seguras. Backup sem restore, alerta sem responsável e fallback nunca exercitado não são controles comprovados.

## AIOps e operações assistidas por IA

Use automação para reduzir trabalho repetitivo com telemetria suficiente e ação delimitada. Comece com recomendação ou modo de observação, compare com decisões humanas e registre falsos positivos e falsos negativos.

Antes de permitir remediação automática, defina identidade, allowlist de ações, blast radius, orçamento de tentativas, precondições, idempotência, limites de custo, trilha de auditoria, condição de parada e mecanismo de reversão. Exija aprovação humana para mudanças de alto impacto quando essa aprovação for necessária pela política ou pelo risco. Não permita que observabilidade, auditoria ou rollback dependam do mesmo componente cuja falha precisam conter.

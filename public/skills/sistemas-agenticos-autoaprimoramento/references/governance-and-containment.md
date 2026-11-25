# Governação e contenção

O ciclo de melhoria altera comportamento e pode ampliar a autonomia. A governação deve acompanhar o impacto e a reversibilidade do componente, desde a proposta até à retirada.

## Papéis

Defina pessoas ou controlos responsáveis por estas funções; uma pessoa pode acumular funções em contextos de baixo risco, mas não deve avaliar cegamente uma alteração que ela própria selecionou:

- **Dono do sistema:** delimita uso pretendido, impacto, requisitos e população.
- **Proponente:** identifica falha e produz candidato; pode ser o agente ou uma pessoa.
- **Avaliador:** executa a rubrica e verifica métricas sem depender da narrativa do proponente.
- **Aprovador:** aceita risco residual e autoriza mudanças de acordo com a política aplicável.
- **Operador:** acompanha rollout, interrompe e executa rollback.

Registe conflitos de interesse, independência limitada ou verificações não disponíveis. Não simule separação chamando dois agentes que partilham o mesmo prompt, dados, avaliador e vieses.

## Ambiente e acesso

- Mantenha desenvolvimento, avaliação e produção separados.
- Para candidato executável, use sandbox descartável, identidade por tarefa, permissões mínimas, armazenamento temporário e rede bloqueada por padrão ou restrita a destinos necessários.
- Não passe credenciais de produção, dados pessoais desnecessários nem acesso de escrita externo ao candidato.
- Torne conjuntos de decisão, avaliadores, logs de auditoria e rollback não graváveis pelo agente que otimiza.
- Trate saídas de ferramentas, documentos, memórias recuperadas e dados sintéticos como conteúdo não confiável; valide antes de persistir ou executar.
- Registe quem executou o quê, com que versão, permissões, dados, semente/configuração, resultados e ação posterior. Redija segredos e reduza a retenção ao necessário.

## Memória e dados gerados

Antes de persistir uma lição, confirme finalidade e autorização; remova identificadores que não são necessários; mantenha separação por utilizador, equipa, cliente ou finalidade quando aplicável; registe fonte, período, confiança, condição de validade e owner. Prefira regras testáveis e pequenas a transcrições brutas. Defina revisão/expiração e procedimento de correção, eliminação e propagação da retirada. Não use um resultado como treino futuro sem verificar proveniência, direitos, leakage e impacto de distribuição.

## Gates por mudança

Requeira revisão humana antes de alterações de pesos, avaliador, código com efeitos externos, credenciais/permissões, dados sensíveis ou memória global/partilhada; aplique também obrigações internas e legais pertinentes à jurisdição. Uma decisão automatizada só pode operar dentro de uma delegação explícita e limitada, com auditabilidade, limite de gasto e botão de interrupção. Verifique sempre a política organizacional vigente em vez de inferir autorização a partir do acesso técnico.

## Rollout e rollback

1. Guarde baseline, candidato, configuração, resultados e dependências com versões/identificadores verificáveis.
2. Teste a reversão antes de ampliar alcance. Para pesos, preserve checkpoint; para memória, teste retirada e propagação; para código, preserve artefacto anterior e migrações reversíveis.
3. Comece com modo sombra, tráfego limitado ou grupo de canário se isso não criar risco adicional. Diga quem integra o grupo e como evitar tratamento injusto.
4. Monitore a métrica principal, guardrails, custo, latência, alertas de segurança e sinais de comportamento inesperado. Alerte owner e operador.
5. Pare e reverta ao atingir limite ou qualquer condição definida. Preserve a evidência do incidente, não volte a ativar automaticamente.
6. Só amplie após revisão dos dados de rollout e aprovação prevista. Atualize a documentação e o registo de memória com os limites observados.

## Resposta a incidente

Se o agente modificar os próprios controlos, ocultar logs, alterar dados protegidos, exceder permissões ou produzir efeitos não autorizados: interrompa a execução, revogue a identidade, preserve evidência, reverta para estado conhecido e encaminhe ao responsável por segurança/privacidade/operação. Retome apenas após causa identificada, controlo corrigido e nova avaliação aprovada.

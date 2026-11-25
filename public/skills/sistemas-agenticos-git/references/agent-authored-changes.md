# Especificação e revisão de alterações feitas por agentes

## Antes da implementação

Converta o pedido numa especificação curta ligada à issue ou ao PR:

- comportamento esperado;
- critérios de aceitação verificáveis;
- paths dentro e fora do escopo;
- interfaces, migrações ou compatibilidade afetadas;
- verificações a executar;
- limites de acesso, rede e publicação;
- condições de rollback para alterações de risco elevado.

Peça esclarecimento quando faltar uma decisão que altere dados, segurança, API pública ou comportamento do utilizador. Não deixe que o agente invente uma política de branch, release ou acesso.

## Revisão da contribuição

Inspecione a branch e o diff por conta própria. Compare a mudança com a especificação e verifique:

1. se cada critério de aceitação está demonstrado;
2. se código adicional ficou fora do pedido;
3. se os testes exercitam comportamento útil e casos limite, e não apenas repetem a implementação;
4. se o pipeline executou no SHA mais recente;
5. se dependências, permissões, rede, secrets e ficheiros de CI mudaram;
6. se um conflito foi resolvido com a intenção correta;
7. se a documentação e os procedimentos de rollback acompanham a mudança.

O resumo do agente, o log de sessão, a mensagem de commit e o estado “tests passed” são afirmações a confirmar. Não substituem o diff, os resultados observáveis nem a revisão exigida. Leia registos de sessão quando existirem e quando houver uma pergunta concreta de auditoria ou um sinal de risco; não presuma que todos os runtimes disponibilizam esses registos.

## Alterações de risco elevado

Autenticação, autorização, pagamentos, dados pessoais, migrações destrutivas, workflows de CI, credenciais, políticas de branch e instruções para agentes justificam escopo explícito, checks determinísticos e revisão por owner competente segundo a política do repositório. Não faça merge ou deploy automático com base apenas na autoria do agente ou em percentagens agregadas de benchmarks.

## Como formular achados

Apresente primeiro os problemas acionáveis. Para cada achado, indique severidade, caminho/trecho, condição que o provoca e impacto. Separe bloqueios de sugestões. Se não encontrar problemas, diga o que reviu e quais os limites, como checks indisponíveis ou falta de contexto do ambiente.

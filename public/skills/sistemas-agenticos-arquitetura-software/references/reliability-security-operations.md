# Confiabilidade, segurança e operação

Use esta referência para analisar atributos de qualidade durante desenho, revisão ou evolução. A profundidade deve corresponder ao impacto e à exposição do sistema.

## Confiabilidade e degradação

Descreva dependências, modos de falha e comportamento esperado quando cada uma falha. Sistemas distribuídos têm falhas parciais: um componente pode responder tarde, duplicar mensagens ou falhar enquanto os restantes continuam ativos.

- Defina timeouts por interação e limites de concorrência para que uma dependência lenta não consuma os recursos do chamador.
- Aplique retries apenas quando a operação puder ser repetida com segurança; use backoff e limites para não amplificar uma indisponibilidade.
- Circuit breakers, bulkheads, filas e cache são ferramentas para problemas específicos, não um conjunto obrigatório.
- Defina idempotência para efeitos repetíveis, duplicações e redelivery.
- Faça backpressure e limites de fila parte do desenho, incluindo como lidar com consumidores atrasados.
- Planeie backup, retenção, restauração testada, recuperação e consistência de réplicas segundo objetivos acordados.
- Especifique comportamento degradado e reconciliação quando o serviço externo ou modelo não está disponível.

Não prometa alta disponibilidade só com redundância. Considere dependências comuns, publicação, dados, recuperação, deteção e resposta operacional.

## Segurança e privacidade

Trace fronteiras de confiança e fluxos de dados antes de selecionar controles. Considere identidade humana e não humana, autenticação, autorização, isolamento, segredos, registos, dependências, entrada não confiável e saída para a rede.

- Aplique menor privilégio e separe leitura de escrita e ações de impacto diferente.
- Valide autorização na camada que controla o dado ou efeito. Um prompt ou instrução do agente não é enforcement de segurança.
- Limite o que cada componente pode ler, alterar, executar e contactar; isole execução quando o risco o justificar.
- Proteja dados em trânsito e em repouso conforme a sensibilidade e obrigações aplicáveis; minimize cópias, contexto e retenção.
- Registe quem pediu, que política foi aplicada, que aprovação ocorreu e qual efeito foi observado, respeitando privacidade e retenção.
- Trate conteúdo externo, dependências e resultados de ferramentas como entradas não confiáveis; valide antes de os usar em ações.
- Defina revogação, rotação e resposta a comprometimento para credenciais e identidades.

Descubra as obrigações legais e normativas aplicáveis ao contexto e confirme os requisitos atuais em fontes competentes. Não declare conformidade apenas pela presença de uma arquitetura ou certificação de fornecedor.

## Observabilidade

Instrumente as perguntas que a equipa precisa de responder durante um incidente: que pedido falhou, onde, para quem, com que dependência e com que impacto? Combine logs estruturados, métricas e traces conforme o sistema; defina correlação sem expor segredos ou conteúdo pessoal.

Em fluxos de IA, considere também versões do modelo e prompt, chamadas de ferramentas, recuperação, número de passos, latência, erros, custos e sinais de qualidade. Redija dados sensíveis e limite acesso e retenção das traces. Esquemas de observabilidade para IA evoluem; confirme a especificação vigente se depender de uma convenção concreta.

## SLOs, custos e suporte

Escolha indicadores ligados à experiência ou ao resultado de negócio. Defina janelas, população, percentis e exclusões; não derive um SLO de um número genérico encontrado num exemplo. Para sistemas com modelos, estime o custo por resultado útil incluindo chamadas, recuperação, armazenamento, avaliação, retries e revisão humana.

O desenho precisa de um modelo operacional: quem recebe alertas, que capacidade é necessária, como se publica, como se reverte, como se inspeciona uma decisão e como se recupera o serviço. Meça antes de otimizar; custo de infraestrutura, integração, pessoas e suporte também contam.


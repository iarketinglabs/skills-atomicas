# Segurança e identidade de agentes

Use esta referência para mapear o plano de controle, fronteiras de confiança, identidade e permissões de workloads automatizados. Instruções de modelo não substituem controles aplicados pelo runtime, sistema operacional, rede ou provedor.

## Responsabilidade compartilhada

Para cada serviço, identifique o que o fornecedor controla e o que cabe ao operador: identidade, configuração, dados, chaves, sistema operacional, rede, aplicação, dependências, cópias e incidentes. Não interprete certificação do fornecedor ou SLA como prova de que a configuração do workload é segura.

## Identidade e privilégio mínimo

Use identidade distinta por workload, ambiente e função. Prefira credenciais temporárias e escopo restrito a chaves estáticas duradouras. Separe autenticação de autorização; permita apenas ações e recursos exigidos pela tarefa; registre concessão, uso, revogação e responsável.

Para um agente capaz de administrar infraestrutura:

- confira a intenção do usuário e o ambiente-alvo;
- permita apenas APIs, recursos e operações necessários;
- limite duração, volume, regiões, contas e impacto;
- exija confirmação conforme a autorização existente e a política do sistema para ações destrutivas ou externas;
- mantenha um caminho independente para revogar acesso e interromper execuções;
- registre pedido, plano, identidade, diff, resultado e evidência de validação.

Não peça nova autorização quando o usuário já autorizou claramente a mesma ação e o escopo não mudou. Se alvo, impacto ou autorização estiverem ambíguos, prepare um plano concreto e esclareça o limite antes de executar.

## Defesa em camadas

Avalie rede, IAM, sistema operacional, containers, supply chain, dados e plano de controle. Use imagens e dependências verificáveis, atualizações, isolamento de processos, limites de recursos, segmentação, secrets management e logging com acesso restrito. Não exponha interfaces administrativas à internet sem necessidade e controles adequados.

Proteja os dados de observabilidade e backup com a mesma atenção dada aos dados de produção. Minimize conteúdo capturado, proteja cópias contra alteração, teste restauração e defina retenção e eliminação.

## Threat modeling prático

Para cada ação de agente, pergunte:

1. Que identidade executa e qual é o limite de privilégio?
2. Que entrada pode ser controlada por usuário, arquivo, página ou ferramenta externa?
3. Que estado ou sistema externo pode ser alterado?
4. Qual é o pior efeito plausível se a ação for repetida, desviada ou executada no ambiente errado?
5. Que controle determinístico impede ou limita esse efeito?
6. Como se detecta, interrompe, revoga e recupera?

Se a resposta depende apenas do agente obedecer às instruções, o controle é insuficiente.

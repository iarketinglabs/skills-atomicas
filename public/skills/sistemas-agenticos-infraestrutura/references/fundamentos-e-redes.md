# Fundamentos e redes

Use esta referência para decompor uma infraestrutura em camadas e localizar limites físicos ou domínios de falha antes de escolher produtos.

## Modelo de análise

Desenhe o caminho da requisição e do dado do início ao fim: cliente ou agente, DNS, identidade, rede, gateway, runtime, dependências, persistência e resposta. Para cada camada, registe:

- função e responsável operacional;
- estado que mantém e dependências externas;
- limite de capacidade ou fila;
- comportamento em falha parcial;
- sinal que demonstra saúde para o usuário;
- cópia de recuperação e método de restore, se houver estado durável.

CPU, memória, disco, rede e aceleradores são recursos finitos que disputam filas. Otimizar uma camada pode apenas deslocar o gargalo. Meça o caminho completo e examine saturação, latência, perda, congestionamento, contenção e comportamento em pico.

## Redes e topologia

Avalie latência, throughput, jitter, perda, congestionamento, distância, egress e requisitos de conectividade. Workloads síncronos podem ficar limitados pelo participante ou dependência mais lenta. Uma métrica isolada de link não prediz o desempenho da aplicação.

Para cargas distribuídas de IA, placement e topologia podem determinar se aceleradores conseguem comunicar-se com o desempenho esperado. Confirme o caminho físico e compare com um benchmark que represente o workload, hardware, tamanho de lote e padrão de comunicação. Não generalize multiplicadores de performance sem método reproduzível.

Mapeie zonas, regiões, racks, links, contas e serviços que compartilham uma causa de falha. Réplicas no mesmo domínio podem oferecer disponibilidade aparente sem independência real. Alta disponibilidade, replicação e recuperação de desastre resolvem problemas diferentes.

## Camadas de serviço

Distinga:

- infraestrutura física, hipervisor e rede;
- sistema operacional e runtime;
- plataforma de execução e orquestração;
- aplicação, estado e dependências;
- políticas de identidade, observabilidade, backup e recuperação.

Um serviço gerenciado desloca parte da operação, mas não elimina responsabilidade por dados, configuração, acesso, limites, custo e saída. Documente a fronteira de responsabilidade por componente.

## Disponibilidade e recuperação

Use RPO para expressar perda de dados tolerável e RTO para tempo de recuperação. Converta ambos em procedimento, mecanismo e teste. Backups devem ser separados de credenciais e domínios de falha da produção, protegidos contra alteração indevida e restaurados periodicamente. Replicação e snapshots não substituem uma cópia recuperável.

## Perguntas de diagnóstico

- O gargalo está no compute, rede, storage, quota, dependência ou fila?
- A capacidade observada também está no local e formato exigidos pelo workload?
- Que falhas afetam simultaneamente primário, réplica, backups e plano de controle?
- O usuário ainda recebe um resultado útil quando uma dependência falha?
- Que parte da operação está coberta pelo fornecedor e que parte permanece com a equipe?

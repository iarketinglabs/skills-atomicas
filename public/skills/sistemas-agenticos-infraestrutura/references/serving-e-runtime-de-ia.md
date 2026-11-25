# Serving e runtime de IA

Use esta referência para desenhar a infraestrutura de inferência e execução de agentes. Ela cobre runtime, capacidade, isolamento e operação; seleção de modelo, qualidade da resposta e desenho de prompts pertencem a outras análises.

## Caminho de uma tarefa

Mapeie a entrada, autorização, fila ou gateway, chamada a modelo, ferramentas, persistência de estado, resposta e observação. Registe latência, erros, timeouts, volume, concorrência, tamanho de entrada e saída, tarefas longas, cancelamento e dependências externas. Separe o tempo total da tarefa do tempo de cada chamada.

## Modalidades de serving

Compare API de inferência gerenciada, endpoint dedicado, runtime em containers, serviço em GPU ou implantação própria. Avalie:

- requisitos de privacidade, região, rede e retenção;
- concorrência, latência, throughput, disponibilidade e quotas;
- configuração de batch, cache, streaming e filas;
- custo em período ocioso e carga de pico;
- controlo sobre versões, runtime, instrumentação e escala;
- recuperação, portabilidade, saída e dependências do fornecedor.

Confirme comportamento e preços atuais na documentação oficial e em medições representativas. Recursos como batching, cache, scale-to-zero e autoscaling têm trade-offs de latência, estado, previsibilidade e custo. Não os recomende como ganho universal.

## Capacidade de inferência

Dimensione com a unidade de trabalho relevante, como pedidos, sessões, tokens processados, tarefas concorrentes ou duração. Não conte apenas requisições por segundo quando tamanho de entrada, saída ou custo de computação varia materialmente.

Meça p50/p95/p99, erros, fila, saturação, uso de memória do acelerador, espera de carregamento, cache e sucesso fim a fim. Defina limites para concorrência, fila, timeout, quotas e orçamento. Planeje comportamento durante cold start e interrupção de provedor ou nó.

Em infraestrutura própria, valide hardware, driver, runtime, memória, topologia e comunicação. Em serviço externo, valide limites de conta, região, comportamento em falha, política de dados e custo. Mantenha as duas hipóteses separadas.

## Runtime de agentes

Modele uma execução como unidade observável e cancelável, com estado recuperável quando necessário, idempotência para efeitos externos, orçamento de tempo/tentativas/custo e limite de ferramentas. Separe execução de modelo, ferramentas e armazenamento para localizar gargalos sem conceder acesso global ao worker.

Para tarefas longas ou concorrentes, decida se elas podem ser retomadas, duplicadas, canceladas ou reordenadas. Escolha fila e persistência segundo essas semânticas. Não prometa entrega exactly-once sem mecanismo que a demonstre.

## Controles operacionais mínimos

- health e readiness medem dependências necessárias, não apenas processo ativo;
- deploy e rollback consideram versão de modelo/runtime e compatibilidade de estado;
- falhas de dependência não causam retry ilimitado nem tempestade de chamadas;
- conteúdo de traces tem redaction, retenção e controle de acesso;
- autoscaling observa demanda e saturação com limites de orçamento;
- workloads de clientes ou tenants têm isolamento e quotas definidos.

# Computação, containers e scheduling

Use esta referência para selecionar a unidade de execução e verificar se o workload cabe nos recursos disponíveis sem introduzir uma plataforma maior do que a operação consegue manter.

## Caracterize o workload

Registe duração, concorrência, padrão de pico, estado local, requisitos de latência, isolamento, arquitetura de CPU, memória, disco, rede, aceleradores, disponibilidade e política de interrupção. Diferencie tráfego interativo, workers assíncronos, batch, treinamento e inferência.

## Compare formas de execução

| Opção | Favorece | Exige atenção a |
|---|---|---|
| Processo ou serviço em máquina existente | Baixa complexidade e workload pequeno | Isolamento, dependências, deploy e contenção |
| Máquina virtual ou VPS | Controle do sistema operacional e custo previsível para carga estável | Patching, hardening, backups, capacidade e plantão |
| Container em host ou serviço simples | Artefato reproduzível e isolamento de processo | Imagens, runtime, persistência, rede e atualização |
| Plataforma gerenciada | Menos operação de plano de controle | Limites, custo, lock-in, debugging e responsabilidade compartilhada |
| Orquestrador de containers | Scheduling, reconciliação, quotas e operação de múltiplos serviços | Complexidade, upgrades, observabilidade e expertise de plantão |
| Bare metal ou cluster de aceleradores | Controle de hardware, desempenho e topologia específicos | Capacidade ociosa, drivers, rede de alto desempenho e recuperação |

Trate a tabela como ponto de partida, não como ranking. Escolha pela carga, risco e capacidade operacional confirmados.

## Containers e orquestração

Container é um formato e unidade de empacotamento; runtime executa; orquestrador agenda e reconcilia. Isolamento de container não substitui limites de rede, identidade, filesystem e privilégios. Avalie saúde, shutdown gracioso, requests e limits, persistência, imagens, quotas, políticas de colocação e recuperação de nós.

Adote Kubernetes ou outro orquestrador quando precisar de capacidades concretas que não sejam atendidas por processo, máquina, serviço gerenciado ou scheduler mais simples. Inclua o custo de operação e upgrades no desenho.

## Capacidade e placement

Separe três questões:

1. **Existe capacidade total?** Há recursos suficientes em agregado?
2. **É colocável?** Os recursos estão no domínio, formato, topologia e janela adequados?
3. **É saudável e sustentável?** É possível manter latência, disponibilidade e custo esperados durante picos e falhas?

Admission, quota e placement resolvem etapas diferentes. Recursos fragmentados podem não satisfazer um job distribuído. Para tarefas que exigem várias máquinas ou GPUs simultaneamente, verifique scheduling atômico, afinidade e política quando parte do grupo não puder iniciar.

## Aceleradores

Defina requisitos de modelo, memória, interconexão, throughput, precisão, batch, concorrência e tolerância a interrupção. Benchmarks devem corresponder à configuração e ao padrão de tráfego reais. GPU disponível não garante que a colocação, driver, runtime ou comunicação atenda o workload.

## Critérios de saída

Antes de recomendar, responda: que requisito exige esta camada? Quem a operará? Qual é a menor alternativa aceitável? Como migra ou reduz capacidade? Que custo aparece em idle, pico, storage, tráfego e suporte?

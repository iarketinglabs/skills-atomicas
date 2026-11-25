# Capacidade, FinOps e energia

Use esta referência para estimar capacidade e custo por workload, tornar desvios visíveis e tratar energia e disponibilidade de recursos como restrições de projeto.

## Estimativa de capacidade

Comece com volume médio e de pico, concorrência, taxa de crescimento, retenção, tamanho de dados, duração, latência e disponibilidade exigidas. Use medições ou hipóteses explícitas. Considere headroom para picos, falhas, manutenção, crescimento, quotas e fragmentação.

Capacidade nominal não significa capacidade utilizável. Verifique onde o recurso está, se o workload pode ser colocado lá, se existem quotas, se o scheduler consegue admiti-lo e se storage, rede e dependências acompanharão o pico.

## Custos comparáveis

Compare o mesmo workload, região, janela e padrão de pico. Inclua:

- computação ativa, ociosa e de reserva;
- aceleradores, memória e serviços de inferência;
- armazenamento, snapshots, backups, retenção e recuperação;
- tráfego de entrada e saída, conectividade e distribuição;
- observabilidade, segurança, suporte e planos de controle;
- impostos, compromissos, custos de migração e saída;
- horas de engenharia e operação, quando forem relevantes.

Separe preço de tabela, compromisso ou tarifa contratual e custo efetivamente medido. Registe moeda, impostos, período, unidade, descontos e data. Apresente intervalos quando demanda e preços forem incertos; não declare economia sem baseline equivalente.

## Governança financeira

Associe recursos a workload, ambiente, dono, cliente ou centro de custo conforme a necessidade. Defina orçamento, alertas, quota e responsável por agir. Observe custo unitário junto ao resultado, como custo por tarefa concluída, execução ou período de serviço, sem ocultar qualidade e confiabilidade.

Automatize desligamento ou redução de recursos apenas quando estado, janela de atividade, custo de recuperação e impacto ao usuário forem compreendidos. Mantenha limites para retry, loops de agentes, batch e expansão automática.

## Energia e restrições físicas

Para cargas intensivas, avalie disponibilidade de energia, densidade de rack, cooling, rede, capacidade de conexão e requisitos de localização. Compute e GPU podem não escalar apenas por adicionar orçamento. Considere eficiência por workload e timing de execução se houver flexibilidade.

Não transforme capacidade elétrica, estimativas de emissões ou roadmap do fornecedor em garantia local. Exija escopo, período, região, método e fonte para comparar valores.

## Portões de decisão

Antes de aumentar capacidade, identifique o gargalo e a evidência que demonstra saturação. Antes de fixar compromisso, conheça a demanda e o custo de saída. Antes de escalar automaticamente, defina teto de custo, métrica de acionamento, tempo de estabilização e condição de redução.

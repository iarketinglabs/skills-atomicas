# Medição Antes da Otimização

Otimização útil começa com baseline. Meça custo por resultado aceito, latência ponta a ponta, taxa de retrabalho e qualidade da tarefa; preço por token e tempo do modelo isolados não explicam necessariamente o resultado.

- Use um modelo menor, compactação ou redutor local somente se a qualidade definida para a tarefa permanecer aceitável.
- Separe latência de inferência, transporte, ferramentas e orquestração antes de atribuir lentidão ao modelo.
- Trate cache como compromisso de frescor e invalidação; registre fonte de verdade, chave, TTL e comportamento durante falha.

## Fonte primária

- [AWS Well-Architected: Performance Efficiency](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_establish_key_performance_indicators.html)

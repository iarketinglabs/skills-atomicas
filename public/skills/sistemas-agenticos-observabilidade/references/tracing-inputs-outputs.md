# Tracing de entradas, saídas e efeitos

Use traces para reconstruir a trajetória **observada** de uma execução. Registre as etapas externas e os resultados do sistema. Para entender uma escolha, use código de decisão, versão da política, evento de aprovação ou resumo explícito quando disponíveis. O tracing não expõe raciocínio interno do modelo, e nenhum passo depende de o obter.

## Spans e correlação

- Um trace agrupa o percurso da execução. Um span delimita uma operação observável, como requisição de modelo, ferramenta, avaliação ou espera por aprovação.
- Use a relação pai/filho quando uma operação deriva da outra. Para filas com lote, retentativas posteriores ou múltiplas origens, vincule spans quando o protocolo permitir e documente o significado.
- Mantenha trace ID e run ID técnicos quando precisar correlacionar. O run ID do produto pode persistir em uma retomada que abre um trace novo. Evite usar esses IDs como rótulos de métricas.
- Propague contexto por runtime e confirme no teste que uma operação intercalada de outro usuário não herda o contexto da primeira. Prefira SDKs que gerenciem contexto por tarefa a uma pilha global compartilhada.

```text
execução de teste: operações de catálogo
├── chamada do modelo: versão, duração, uso de tokens
├── ferramenta: consulta de item, schema v2, resultado encontrado
├── decisão registrada: operação de escrita requer aprovação
└── avaliação: fonte presente, estado final sem escrita
```

## Dados e privacidade

Por padrão, capture atributos operacionais, código de resultado, decisão, efeitos observados e versões. Separe alegação do agente, retorno da ferramenta e comprovação do efeito. Preserve referência restrita a uma evidência quando necessário. Evite enviar prompts, respostas, conteúdo de arquivos, identificadores pessoais ou payloads brutos. Se a coleta de conteúdo for indispensável e autorizada, defina amostra, finalidade, sanitização na origem, armazenamento separado, retenção e acesso. Confirme o dado realmente exportado, inclusive exceções e logs automáticos.

A instrumentação usa fila e limites de processamento para não bloquear o trabalho quando o exportador falha. Monitore atraso, fila, descartes e inconsistências de contexto. Uma ausência pode vir de sampling, filtro, falha de propagação ou erro de exportação.

## Verificação

1. Gere duas execuções sintéticas intercaladas e uma falha de ferramenta. Confirme que cada span aparece sob o contexto esperado e registra o estado observado.
2. Inspecione campos exportados, incluindo registros de falha e os do SDK. Verifique ausência de segredos e conteúdo além do escopo.
3. Compare a telemetria com a execução conhecida. Informe quais etapas não têm evidência e lacunas que afetam interpretação de qualidade, performance ou custo.

[Convenções semânticas e limites de versão](agent-telemetry-semantic-conventions.md) · [Métricas de assertividade e performance](assertiveness-and-performance-metrics.md) · [OpenTelemetry Context](https://opentelemetry.io/docs/specs/otel/context/) · [Trace Context W3C](https://www.w3.org/TR/trace-context/)

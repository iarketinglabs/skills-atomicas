# Tracing de Inputs e Outputs

Parte de **Observabilidade e Melhoria Contínua** (ver Framework Mental no `SKILL.md`). O arquivo canônico para a arquitetura de spans hierárquicos — `assertiveness-and-performance-metrics.md` assume essa arquitetura como pré-lida e foca na taxonomia de métricas calculadas sobre ela.

## Por que telemetria tradicional não basta

APM tradicional (baseado em requisição HTTP e latência de banco) não captura o que importa em um agente: fluxos dinâmicos de planejamento, chamadas a ferramentas, subprocessos de raciocínio, interações assíncronas. Quando um agente falha — gera código corrompido, executa um comando destrutivo, entra em loop — não existe um código de erro HTTP para inspecionar. É preciso reconstruir a árvore genealógica completa de tomada de decisão.

## Spans e relações parent-child

O tracing agêntico é estruturado como um grafo acíclico dirigido, não como um log plano:

```
TRACE ID: sessão geral
├── SPAN: planejador (supervisor)
│    ├── input: "corrija o bug no backend"
│    └── output: "passo 1: ler o log. passo 2: gerar patch."
├── SPAN: execução de ferramenta (worker)
│    ├── parent: planejador
│    ├── tool: read_file(...)
│    └── output_raw: [conteúdo do arquivo]
└── SPAN: avaliação (Juiz)
     ├── parent: sessão geral
     └── output: {"passed": true, "score": 0.98}
```

- **Trace:** a jornada completa do agente para resolver uma tarefa macro — o nó raiz, carregando o identificador de sessão unificado.
- **Span:** uma etapa delimitada dentro da tarefa — uma chamada de ferramenta, uma consulta, um passo de reflexão, uma validação de qualidade.
- **Relação parent-child:** cada span declara o ID do seu nó pai. Se um orquestrador invoca um sub-agente, todas as ações desse sub-agente herdam a assinatura de contexto do pai — permitindo o colapso visual de árvores complexas em um painel de monitoramento.

Para portabilidade e evitar acoplamento a um provedor de telemetria específico, a instrumentação deve seguir uma especificação aberta de tracing, não um formato proprietário.

## Implementação de referência

```python
class AgentSpan:
    def __init__(self, name, span_type, parent_id=None):
        self.span_id = f"span_{uuid.uuid4().hex[:8]}"
        self.parent_id = parent_id
        self.name = name
        self.span_type = span_type  # 'LLM', 'TOOL', 'CHAIN', 'JUDGE'
        self.start_time = time.time()
        self.token_usage = {"prompt_tokens": 0, "completion_tokens": 0, "cached_tokens": 0}
        self.status = "PENDING"

    def complete(self, output_data, **token_counts):
        self.end_time = time.time()
        self.output_data = output_data
        self.token_usage.update(token_counts)
        self.status = "SUCCESS"

class ActiveAgentTracker:
    """Gerencia uma sessão de tracing, aninhando spans via pilha implícita."""
    def __init__(self, trace_name, session_id):
        self.trace_id = f"tr_{uuid.uuid4().hex[:8]}"
        self.spans = {}
        self.span_stack = []

    def start_span(self, name, span_type, input_data):
        parent_id = self.span_stack[-1] if self.span_stack else None
        span = AgentSpan(name, span_type, parent_id)
        span.input_data = input_data
        self.spans[span.span_id] = span
        self.span_stack.append(span.span_id)
        return span.span_id

    def end_active_span(self, output_data, **token_counts):
        span_id = self.span_stack.pop()
        self.spans[span_id].complete(output_data, **token_counts)
```

## Visão geral de métricas (ponteiro)

O tracing captura os dados brutos; a taxonomia completa de métricas calculadas sobre eles — latência, custo, taxa de erro de ferramenta, assertividade — tem tratamento completo em `assertiveness-and-performance-metrics.md`. Aqui vale reter só a estrutura de três eixos que todo span deve alimentar: **o quê** (assertividade), **como** (performance de recursos), **quanto** (custo).

## Segurança de telemetria

Um repositório centralizado de traces é um alvo de alto valor — contém logs de conversas inteiras, potencialmente credenciais e dados de clientes. Antes de qualquer payload de trace sair do ambiente local para um servidor de observabilidade (especialmente em nuvem de terceiros), ele passa por uma varredura de redação de segredos e PII na borda. Ver o desenvolvimento completo desse controle na skill de Segurança e Confiabilidade desta coleção, se disponível — aqui o ponto central é: a redação acontece **antes** do envio, nunca depois.

## O ciclo de melhoria contínua

Tracing não é só ferramenta de depuração — é o insumo do ciclo de melhoria contínua completo (curadoria de exemplos, fine-tuning). Ver `../assets/continuous-improvement-loop.md`.

## Anti-padrões

- **Monolithic Logging:** salvar todo o histórico bruto em arquivos planos sem rotação — esgota espaço em disco e adiciona latência de escrita que trava o agente em runs longas.
- **Blocking Trace Shippers:** enviar telemetria de forma síncrona na thread principal de execução. Se o servidor de tracing tiver uma oscilação de rede, a execução do agente congela. O despacho deve ser sempre assíncrono, em background.
- **Dumping de PII na nuvem:** confiar que um portal de telemetria de terceiros vai lidar com dados sensíveis sem filtro de redação prévio na borda.

## Checklist

- Cada chamada de ferramenta, passo de raciocínio e validação de qualidade roda sob um span com relação parent-child explícita.
- O despacho de telemetria para o servidor externo é assíncrono, nunca bloqueante.
- Segredos e PII são redigidos na borda antes do envio, não depois.
- Todo span carrega o mesmo identificador de execução unificado (Agent Run ID) da sessão raiz.

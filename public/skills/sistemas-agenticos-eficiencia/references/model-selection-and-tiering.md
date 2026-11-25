# Seleção de Modelos (Opus vs Sonnet) / Tiering por Complexidade

> **Duas lentes, um só tema.** Este arquivo reconcilia a decisão binária "qual modelo uso para esta tarefa" com o framework mais amplo de "como fatio um pipeline inteiro entre múltiplas classes de modelo". Ambas as seções do `SKILL.md` apontam para este arquivo.

Parte de **Token Efficiency / Eficiência e Gestão de Contexto** (ver Framework Mental no `SKILL.md`). Tratar toda tarefa como se exigisse o modelo mais capaz disponível é um dos erros mais caros e comuns em produção.

## O paradoxo do preço de tabela

Avaliar custo pelo preço nominal por milhão de tokens é uma ilusão em ambientes agênticos, onde o modelo opera em loops iterativos de ferramenta e correção de erro. A métrica real é o **Custo por Tarefa Aceita** (ver `outcome-maxxing.md`), que engloba retentativas, revisões e o número de interações necessárias até a meta ser atingida de fato.

**Estudo de caso ilustrativo:** um benchmark comparando dois modelos em tarefas reais de engenharia mostrou que o modelo mais barato por token exigiu tantas iterações e retrabalhos adicionais que seu custo final por tarefa aceita superou o do modelo mais caro por token, que resolveu a mesma demanda de forma cirúrgica em poucas tentativas. **O modelo mais barato na tabela de preços pode ser o mais caro no balanço final** se precisar de várias tentativas a mais para acertar o que um modelo premium resolve de primeira.

## A física do contexto por classe de modelo

A escolha de modelo também determina a resiliência do sistema em sessões longas — ver Framework Mental no `SKILL.md` para os limiares gerais de Dumb Zone. Em termos comparativos:

| | Modelos rápidos/ágeis | Modelos de raciocínio pesado |
|---|---|---|
| Papel típico | Executor de escopo fechado | Parceiro de pensamento / arquiteto |
| Limiar de Dumb Zone | Mais baixo — degrada mais cedo | Mais alto — sustenta foco por mais tempo |
| Context Anxiety | Alta — corta caminhos cedo sob pressão | Mais resiliente sob alta carga de dados |

## Roteamento dinâmico (arbitragem de modelo)

Uma abordagem monolítica de "um modelo serve para tudo" desperdiça dinheiro. O roteamento correto distribui o trabalho por três papéis:

1. **Parceiro de ideias / arquiteto (modelo de raciocínio pesado):** brilha em ambiguidade alta, design de arquitetura, especificação técnica, análise crítica de design — a mente estratégica que "olha as curvas do caminho" antes do código ser escrito.
2. **Executor de escopo fechado (modelo ágil intermediário):** quando a especificação já está mapeada e o trabalho é implementação linear — API já definida, classe base a preencher, regra clara a traduzir em código — a velocidade e o custo baixo compensam.
3. **Triagem de baixo custo (modelo local ou barato):** rotinas de administração — varrer diretórios, reorganizar nomes de arquivo, resumir documentos pesados — delegadas a modelos locais gratuitos ou proxies muito baratos, blindando o orçamento dos modelos premium para o raciocínio que realmente exige.

## A curva de custo vs. qualidade e a regra de alocação

A relação entre custo de inferência e qualidade de entrega não é linear — segue algo como um "U" invertido. Para tarefas complexas (raciocínio abstrato, arquitetura, segurança de borda), o modelo de prateleira mais alta é indispensável. Para tarefas de baixo horizonte cognitivo (extração, classificação), o ganho de qualidade de um modelo caro sobre um barato é de poucos pontos percentuais — a eficiência financeira justifica operar na borda inferior da curva.

Uma regra prática de alocação de volume de tokens entre as três camadas:

- **~60% carga utilitária:** classificação, preenchimento de metadados, compactação de log, filtragem — modelos extremamente baratos ou locais.
- **~30% capacidade operacional:** desenvolvimento focado, redação, construção de relatórios — modelos intermediários rápidos e robustos.
- **~10% inteligência de fronteira:** reservado ao orquestrador mestre — planejamento, julgamento de qualidade final, interação estratégica com o usuário.

## Arquitetura Cérebro/Músculo

```
                REQUISIÇÃO DO USUÁRIO
                        │
                        ▼
              CÉREBRO / PLANEJADOR
        modelo de raciocínio pesado, visão macro
                        │ decompõe e roteia
      ┌─────────────────┼─────────────────┐
      ▼                 ▼                 ▼
  MÚSCULO/WORKER    MÚSCULO/WORKER    MÚSCULO/WORKER
  modelo rápido      modelo rápido     modelo rápido
```

O cérebro mantém o contexto de planejamento macro e roda sob o modelo mais capaz; os músculos são subagentes efêmeros de privilégio mínimo, cada um resolvendo uma subtarefa isolada com o modelo mais rápido disponível — o mesmo padrão de sub-agentes especializados tratado em profundidade na skill irmã de Harness Engineering, se disponível no seu ambiente.

**Nota sobre meta-agentes:** um agente encarregado de otimizar o comportamento de outro (analisando falhas, ajustando prompts) tende a ter desempenho sensivelmente melhor quando pertence à mesma família de modelo do agente que está sendo otimizado — ele entende de forma mais intuitiva os vieses e tendências daquele "cérebro" específico.

## Cascade Fallback com Quality Gates

Em vez de decidir estaticamente qual modelo usar, um padrão determinístico tenta o modelo mais barato primeiro e escala automaticamente:

```python
class DeterministicQualityGate:
    """Valida deterministicamente se a saída cumpre o contrato de schema exigido."""
    @staticmethod
    def audit_schema(output_text: str) -> bool:
        try:
            parsed = json.loads(output_text)
            return "campo_obrigatorio_a" in parsed and "campo_obrigatorio_b" in parsed
        except json.JSONDecodeError:
            return False

class CascadeModelRouter:
    def __init__(self):
        self.model_tiers = ["modelo-utilitario", "modelo-intermediario", "modelo-fronteira"]

    async def execute_cascade_task(self, prompt: str) -> dict:
        for attempt, model in enumerate(self.model_tiers, start=1):
            raw_response = await self._invoke_model(model, prompt)
            if DeterministicQualityGate.audit_schema(raw_response):
                return {"status": "APPROVED", "resolved_by_model": model, "attempts": attempt}
        # nenhum tier resolveu — escala para humano em vez de insistir
        return {"status": "ESCALATED_TO_HUMAN"}
```

Cada saída passa por uma porta de qualidade determinística (parser de schema, linter, teste de compilação); se falhar, o orquestrador escala para o próximo nível da cascata, em vez de aceitar uma saída malformada ou insistir indefinidamente no mesmo modelo.

## Impacto financeiro ilustrativo

Considerando um volume mensal fixo de tokens de saída: rotear tudo para o modelo mais caro produz uma fatura de referência X. Aplicando a regra de alocação 60/30/10 (a maior parte do volume no tier utilitário, uma fatia intermediária no tier operacional, e só uma fração pequena no tier de fronteira), o custo total consolidado cai substancialmente — com variação nula de qualidade percebida na entrega final, porque o modelo caro foi reservado estritamente para planejamento e julgamento, não para volume bruto de execução.

## A armadilha de trocar de modelo no meio da conversa

Uma prática comum — usar um modelo de raciocínio para planejar e trocar para um modelo ágil no mesmo turno para executar — parece inteligente para economizar no orçamento diário, mas é prejudicial do ponto de vista de cache: cada modelo tem seu próprio tokenizer, e a troca invalida o cache de prompt inteiro (ver `prompt-caching-and-stable-context.md`), forçando reprocessamento a preço cheio.

**A boa prática:** para mudar de modelo, mude de sessão. Escreva o plano com o modelo de raciocínio, salve o resultado em um arquivo de handoff (ver `handoff-documentation.md`), encerre a sessão, e inicie uma sessão nova e limpa com o modelo executor carregando só o plano condensado.

## Segurança ao distribuir tarefas entre modelos/provedores

- Subagentes de menor porte cognitivo nunca devem visualizar chaves reais de API — a sandbox repassa a chamada por um gateway que mascara credenciais fora da janela de contexto.
- Workers de utilidade rodam com o mínimo de acesso necessário — sem conexão de rede de saída e sem permissão de escrita além do estritamente necessário para a subtarefa.
- Um teto de chamadas consecutivas sem progresso (referência comum: ~15) protege contra loops de erro caros na camada mais barata da cascata.

## Checklist

- Nenhuma tarefa usa o modelo mais caro disponível por padrão — a escolha é deliberada por complexidade.
- Métrica de acompanhamento é Custo por Tarefa Aceita, não preço nominal por token.
- Troca de modelo sempre acompanha troca de sessão, nunca ocorre no meio da mesma thread.
- Cascade fallback com porta de qualidade determinística está configurado onde aplicável, em vez de aceitar a primeira saída sem validação.

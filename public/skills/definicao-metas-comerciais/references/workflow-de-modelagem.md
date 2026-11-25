# Workflow de modelagem

## Dados mínimos

Peça somente o que muda a decisão. Para uma meta comercial calculável, normalmente são necessários:

| Bloco | Dados | Uso |
| --- | --- | --- |
| Objetivo financeiro | período, resultado financeiro-alvo, definição contábil | define a meta que vendas precisa sustentar |
| Base atual | receita contratada, reconhecida e recebida; receita já comprometida | evita contar receita duas vezes |
| Economia | preço/ticket, descontos, custos variáveis, custos fixos, margem | conecta receita a resultado |
| Funil | oportunidades por etapa, conversões, ciclo, origem e qualidade | traduz receita nova em atividade comercial |
| Capacidade | vendedores, carteira/território, horas ou unidades entregáveis, utilização | testa viabilidade operacional |
| Risco | concentração, churn, renovação, sazonalidade, dependências | define cenários e gatilhos de revisão |

Se o objetivo for caixa, acrescente prazos de faturação, recebimento e inadimplência. Se houver mais de um produto, serviço ou segmento, mantenha ticket, margem, ciclo e capacidade separados enquanto essas diferenças forem relevantes.

## Ponte financeira-comercial

Escolha uma única definição de margem e deixe-a explícita. Uma forma simples de derivar a receita exigida é:

```text
receita líquida necessária =
  (custos fixos do período + lucro operacional-alvo) / margem de contribuição
```

Onde a margem de contribuição é calculada sobre a mesma base de receita líquida e desconta apenas custos variáveis definidos no modelo. Não some ou subtraia novamente despesas que já estejam embutidas na margem.

Depois separe a necessidade:

```text
receita nova necessária =
  receita líquida necessária - receita recorrente/contratada esperada - receita de expansão confirmada
```

Use receita reconhecida para uma meta de resultado do período. Use bookings quando a decisão for contratos fechados. Quando houver defasagem entre assinatura, entrega, faturação e recebimento, apresente as três pontes em vez de tratar os termos como sinónimos.

## Funil e capacidade

Para estimar esforço comercial, parta de taxas históricas de um funil com etapas definidas:

```text
pipeline qualificado necessário = receita nova necessária / taxa esperada de ganho
oportunidades qualificadas necessárias = receita nova necessária / ticket médio esperado / taxa de ganho
```

Se houver mais de uma etapa material, calcule de trás para frente usando as conversões entre etapas. Associe cada etapa a um critério de entrada e saída; sem isso, cobertura de pipeline é apenas um número decorativo.

Para serviços, faça também uma prova de entrega:

```text
capacidade faturável = pessoas elegíveis × horas disponíveis × utilização sustentável
receita máxima de entrega = capacidade faturável × taxa média realizada
```

Ao estimar "utilização sustentável", use um cenário de teste e valide-o com dados de capacidade, qualidade e saúde operacional da própria equipa. Se uma referência externa alterar a recomendação, recolha-a pelo protocolo de [pesquisa de métricas setoriais](benchmarks-setoriais.md), sem assumir uma faixa universal.

Adapte as unidades ao negócio. Em produtos, capacidade pode ser stock, suporte, onboarding ou infraestrutura. A meta proposta precisa caber simultaneamente no funil e na capacidade. Caso não caiba, explicite a alavanca: contratar, elevar preço, mudar mix, reduzir escopo, melhorar conversão, estender prazo ou rever o objetivo financeiro.

### Capacidade de vendas de baixo para cima

Não distribua uma quota dividindo a meta de receita nova igualmente pelo número de vendedores — o resultado real de uma equipe comercial tende a se concentrar em poucos representantes, não a se distribuir de forma uniforme. Calcule a capacidade de cada papel de baixo para cima:

```text
capacidade de um representante plenamente rampado =
  fluxo esperado de oportunidades qualificadas que ele consegue trabalhar
  × taxa de ganho histórica × ticket médio, dentro do ciclo de venda observado
```

Use essa capacidade, e não o desejo de receita, para decidir quantos representantes (ou qual território/carteira) o plano exige. Sinais de que uma meta já ultrapassou a capacidade real da equipe: queda da taxa de ganho, alongamento do ciclo de venda e aumento de negócios que escorregam de um trimestre para o outro — trate qualquer um desses sinais como gatilho de revisão, não como falha individual do vendedor.

## Cenários e decisão

Crie cenários quando ticket, conversão, churn, ciclo, margem ou capacidade não forem estáveis. Use valores observados ou hipóteses justificadas, alterando apenas as premissas que diferenciam os cenários.

| Cenário | Premissas que variam | Decisão que apoia |
| --- | --- | --- |
| Conservador | pior combinação plausível de conversão, ticket, ciclo ou retenção | preservação de caixa e capacidade |
| Base | expectativa sustentada por dados recentes | plano operacional principal |
| Expansão | melhoria condicionada a iniciativa verificável | investimento ou aceleração |

Não apresente a média dos cenários como compromisso. Indique qual cenário se torna a meta, quais são os sinais de alerta e que decisão será tomada ao cruzar cada gatilho.

## Entregável reutilizável

Use esta estrutura, preenchendo apenas dados suportados:

```markdown
# Plano de metas comerciais — [período]

## Decisão e objetivo financeiro
[objetivo, definição, período e responsável]

## Base, premissas e lacunas
| Item | Valor | Status | Fonte/dono | Observação |
| --- | ---: | --- | --- | --- |

## Ponte para a meta comercial
[fórmulas, cálculos e distinção entre bookings, receita e caixa]

## Cenários
| Métrica | Conservador | Base | Expansão |
| --- | ---: | ---: | ---: |

## Metas e desdobramento
| Métrica | Meta | Base de cálculo | Responsável | Frequência |
| --- | ---: | --- | --- | --- |

## Riscos, gatilhos e decisões
| Sinal | Limiar | Decisão | Dono |
| --- | --- | --- | --- |
```

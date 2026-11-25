# Modelos de cobrança: serviços B2B e produtos B2C2B/SaaS

Escolha o modelo pelo tipo de oferta — serviço profissional entregue por pessoas ou produto/plataforma entregue por software — e não por hábito do setor.

## Serviços profissionais B2B

Do menos ao mais alinhado ao valor entregue:

| Modelo | Como funciona | Quando usar | Risco principal |
| --- | --- | --- | --- |
| **Hora (billable hour)** | Cobra-se o tempo gasto. | Trabalho exploratório sem escopo definível ainda. | Recompensa o prestador ineficiente e coloca um teto artificial sobre a receita do prestador eficiente; nenhum comprador compra "uma hora" — compra um resultado. |
| **Retainer (mensalidade)** | Valor fixo mensal por uma cesta de horas ou responsabilidades. | Manutenção e evolução contínua de algo que já roda, com relação madura. | Descola da entrega se não houver marcos e entregáveis definidos; retainer aberto é mais fácil de vender e mais fácil de banalizar. |
| **Projeto fechado (fixed fee)** | Escopo, prazo e preço definidos antes do início; o risco de estouro é do fornecedor. | Primeiro contrato com um cliente novo — tem começo, meio, fim e porta de saída, desde que o escopo esteja bem escrito. | Se o escopo for mal definido, o fornecedor absorve todo o risco de mudança. |
| **Value-based / outcome-based (success fee)** | Cobra-se pelo valor entregue ao cliente, não pelos inputs de tempo e material nem pelo valor de mercado do output. | Quando o resultado é mensurável, há linha de base limpa e a relação já é madura o suficiente para negociar valor em vez de escopo. | Atrito de fluxo de caixa e de reconhecimento de receita para o fornecedor quando a receita se torna inteiramente contingente a um resultado externo; migrar 100% de uma vez é mais arriscado do que migrar gradualmente ou usar um modelo híbrido (piso fixo + variável). |

Regra prática ao apresentar uma proposta de serviço: ofereça sempre três opções com âncora alta e conduza uma conversa de valor antes de revelar o número — isso por si só tende a aumentar a chance de um desfecho comercial favorável, além de explorar ancoragem e efeito centro de palco (ver [fundamentos de precificação](fundamentos-de-precificacao.md)).

Se a recomendação depender de uma alegação sobre a tendência de mercado entre cobrança por hora e por resultado, pesquise uma fonte atual e comparável e registe-a no ledger de evidências. Sem fonte verificável, compare os modelos a partir do escopo, dos custos, do risco e dos resultados medidos da própria oferta.

## Produtos B2C2B / SaaS

| Modelo | Dinâmica | Quando usar | Limitação |
| --- | --- | --- | --- |
| **Freemium** | Tier gratuito atrai base e constrói hábito de uso; parcela converte para pago. | Produtos com custo marginal de servir baixo e ciclo de adoção individual antes da compra corporativa. | Risco de saturar custo de infraestrutura se a taxa de conversão para pago for baixa; exige cercas de preço precisas entre o grátis e o pago. |
| **Tiered (por escalões)** | Faixas de preço com cercas de valor, agrupando funcionalidades por porte ou necessidade do cliente. | Quando o valor percebido varia claramente por segmento de cliente. | Difícil calibrar os níveis para que um cliente enterprise não consiga operar de forma eficiente demais em um plano básico. |
| **Usage-based / consumption** | Cobrança proporcional ao uso real (eventos, unidades processadas, chamadas). | Quando o custo marginal de servir é significativo e varia por cliente — protege a margem contra uso desproporcional. | Reduz a previsibilidade orçamentária do comprador corporativo, o que pode travar a decisão de compra se não houver teto ou faixa previsível. |
| **Land-and-expand / híbrido** | Entrada pequena (individual ou departamental) que expande via adoção orgânica, combinada com taxa fixa de plataforma mais gatilhos de uso excedente. | Ciclos de venda corporativa longos, onde uma porta de entrada de autoatendimento reduz a fricção do comitê de compras. | Exige infraestrutura de observabilidade e faturamento contínuo para evitar disputas de cobrança no fim do ciclo. |

## Escolha da unidade de cobrança

Não presuma que o modelo por utilizador, por uso ou híbrido está a ganhar ou perder popularidade no mercado. Compare-os com dados do produto e do cliente: previsibilidade de orçamento, relação entre uso e valor entregue, custo marginal, risco de adoção e facilidade de faturação. Para produtos com inferência de IA, modele esse custo variável explicitamente em cada cenário; não assuma uma margem de referência universal.

## Heurísticas acionáveis

- **SE** a empresa vende horas como serviço, **ENTÃO** migre gradualmente para projeto fechado e, depois, para value/outcome-based — um cliente por vez, não a base inteira de uma vez.
- **SE** for apresentar uma proposta de serviço, **ENTÃO** ofereça três opções com âncora alta.
- **SE** o produto B2C2B ainda for 100% per-seat, **ENTÃO** avalie um componente híbrido ou usage-based para capturar expansão de uso sem abrir mão de previsibilidade de receita.
- **SE** o resultado do cliente for mensurável e houver linha de base limpa, **ENTÃO** outcome-based é viável; caso contrário, prefira um modelo híbrido (fixo menor + variável).
- **SE** a oferta tiver componente de inferência de IA, **ENTÃO** projete a margem bruta com o custo de inferência explícito, sem herdar a margem histórica de SaaS puro.

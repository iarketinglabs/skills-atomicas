# Método para decisões arquiteturais

Use esta referência para passar de um pedido amplo a uma decisão que possa ser debatida, implementada e revista. O método serve para projetos novos e sistemas existentes; não impõe uma arquitetura ou sequência de ferramentas.

## 1. Distinguir os tipos de informação

Registe separadamente:

- **Facto:** confirmado por código, telemetria, contrato, norma, utilizador ou fonte verificável.
- **Restrição:** condição que a solução tem de cumprir, como interoperabilidade, prazo, jurisdição, compatibilidade ou limite operacional.
- **Preferência:** escolha desejada, mas negociável, como uma linguagem ou estilo.
- **Pressuposto:** hipótese temporária usada para continuar a análise.
- **Questão em aberto:** informação cuja resposta pode alterar a recomendação.

Uma preferência como “usar microserviços” ou um objetivo vago como “ser escalável” não substitui a necessidade de explicar o resultado desejado. Não transforme uma hipótese em facto para acelerar a conclusão.

## 2. Descobrir os motores da arquitetura

Recolha somente o detalhe necessário para a decisão:

1. **Problema e domínio:** quem usa o sistema, que tarefas executa, quais os conceitos e regras que não podem ser violados?
2. **Fronteiras:** o que está dentro e fora do sistema? Que partes pertencem a outros responsáveis?
3. **Dados:** quem é dono de cada informação, qual a sua sensibilidade, ciclo de vida, volume, consistência e retenção?
4. **Atributos de qualidade:** que níveis de desempenho, disponibilidade, segurança, privacidade, modificabilidade, compatibilidade e auditabilidade são necessários?
5. **Operação:** quem publica, observa, recupera e dá suporte? Que competências e infraestrutura estão disponíveis?
6. **Mudança:** que partes mudam em conjunto, que contratos precisam de durar e que incertezas podem tornar a decisão obsoleta?

Pergunte por picos, tendências e distribuições quando médias escondem o risco. Se os dados não existirem, diga como obtê-los e escolha uma solução que possa ser revista com baixo custo.

## 3. Converter atributos em cenários

Um nome de atributo é demasiado vago para comparar opções. Descreva cada objetivo prioritário com:

| Campo | Pergunta |
|---|---|
| Estímulo | O que acontece? |
| Origem | Quem ou o que inicia o estímulo? |
| Contexto | Em que condições, carga ou estado? |
| Alvo | Que parte do sistema responde? |
| Resposta | Que comportamento é esperado? |
| Medida | Como se observa se a resposta foi suficiente? |

Exemplo estrutural: “Durante o pico acordado de utilização, quando chegam pedidos concorrentes para a mesma entidade, o serviço rejeita ou serializa conflitos sem perder uma alteração e conclui 95% dos pedidos dentro do objetivo definido.” Os valores do exemplo devem vir do contexto real; não os copie como padrão.

Escolha poucos cenários que distingam as opções. Um catálogo longo sem prioridade cria documentação, mas não ajuda a decidir.

## 4. Criar opções genuínas

Compare opções com diferenças materiais de fronteira, dados, implantação ou autoridade. Normalmente bastam duas ou três. Considere:

- solução atual ou caminho de menor complexidade que satisfaz os requisitos;
- solução com fronteiras mais fortes ou uma capacidade separada;
- alternativa distribuída, gerida ou especializada quando uma necessidade concreta a justifica.

Não crie uma opção artificialmente fraca para tornar a favorita inevitável. Inclua custos de transição e operação, não apenas o desenho final.

## 5. Avaliar trade-offs sem falsa precisão

Compare cada opção contra os cenários prioritários e restrições. Use escalas qualitativas ou dados observados. Uma pontuação ponderada só é útil se os responsáveis concordarem com os pesos; caso contrário, números dão aparência de objetividade a preferências não resolvidas.

Considere, conforme o caso:

- latência, vazão, disponibilidade, recuperação e contenção de falhas;
- segurança, privacidade, isolamento e auditabilidade;
- custo de desenvolvimento, infraestrutura, suporte e migração;
- consistência, propriedade dos dados, compatibilidade e versionamento;
- autonomia de equipas, frequência de mudança e capacidade de testar;
- reversibilidade, dependências externas e custo de saída.

Registe pelo menos o principal benefício, o principal custo, o modo de falha mais importante e a condição que poderia invalidar cada opção.

## 6. Recomendar, registar e rever

Uma decisão útil responde a quatro perguntas:

1. O que será feito agora?
2. Que requisitos ou evidências tornam esta opção adequada?
3. Que custos e riscos são aceites, e como serão mitigados?
4. Que sinais mensuráveis ou mudança de contexto levariam a reabrir a decisão?

Use um ADR para decisões com efeitos duradouros em fronteiras, contratos, dados, segurança ou operação. Mantenha pressupostos e perguntas pendentes visíveis; não faça parecer que o desenho está fechado quando ainda depende deles.

## 7. Nível de detalhe da resposta

- **Pergunta pontual:** responda à decisão, trade-off e condição de mudança.
- **Desenho inicial:** mostre contexto, fronteiras, fluxos, dados e riscos centrais.
- **Revisão:** relacione observações com os requisitos e indique evidência necessária para confirmar impacto.
- **Decisão de alto risco:** explicite cenários de falha, opções de recuperação, verificações e responsáveis pela aceitação do risco.

Use [assets/architecture-brief-template.md](../assets/architecture-brief-template.md) e [assets/adr-template.md](../assets/adr-template.md) quando o formato completo for útil.


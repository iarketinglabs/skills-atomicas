# Guia de Elicitação para Mapeamento AS-IS

Roteiro prático para levantar um processo real através de entrevista, observação e triangulação com sistemas — traduzindo os elementos estruturais de `fundamentos-e-elementos.md` em perguntas concretas.

## Antes da entrevista

- Identifique quem **executa** o processo no dia a dia (não apenas quem é dono/gestor da área) — o relato de quem opera diverge sistematicamente do relato de quem supervisiona, e o mapeamento precisa capturar essa divergência, não escolher um dos dois arbitrariamente.
- Levante documentação existente (SOP, fluxograma, política) antes da entrevista, mas trate-a como hipótese a validar, não como fato — ela costuma estar desatualizada.
- Se houver acesso a sistemas com log de eventos (ERP, CRM, ticketing), planeje uma leitura de process mining antes ou em paralelo à entrevista — reduz o viés de memória do entrevistado.

## Roteiro de perguntas por elemento

**Gatilho e entrada**
- O que dispara o início deste processo? Quem ou o que solicita?
- Com que frequência isso acontece (por dia/semana/mês)?

**Fluxo e decisões**
- Descreva o passo a passo de uma execução real recente (peça um caso concreto, não uma descrição genérica).
- Em que pontos existe decisão/bifurcação? O que determina qual caminho é seguido?
- Existe uma versão "ideal" documentada e uma versão "como realmente acontece"? Onde elas divergem?

**Atores e sistemas**
- Quem participa, em cada etapa (nome do papel, não só do departamento)?
- Que sistemas/ferramentas são usados em cada etapa? Existe alguma planilha paralela, e-mail manual ou ferramenta pessoal (Shadow AI/Shadow IT) preenchendo uma lacuna do sistema oficial?

**Handoffs**
- Em que momento a responsabilidade passa de uma pessoa/sistema para outro?
- O que é transferido nesse momento (documento, dado, decisão)? Como a próxima pessoa sabe que precisa agir (notificação, fila, e-mail)?
- Já houve caso de algo "cair" nesse handoff (perda de contexto, atraso, retrabalho)?

**Regras de negócio**
- Existe algum critério que muda o tratamento do caso (valor, tipo de cliente, urgência, exceção regulatória)? Quem define esse critério e onde ele está registrado?

**Saída e encerramento**
- O que define que o processo terminou com sucesso?
- Existem exceções ou casos que não seguem o fluxo padrão? Como são tratados hoje?

**Métricas**
- Que dado hoje já existe sobre volume, tempo ou taxa de erro deste processo? Quem tem esse dado e em que sistema?
- Que métrica vocês gostariam de ter mas não conseguem medir hoje?

**Momentos da verdade (se o processo toca o cliente externo)**
- Em que ponto o cliente percebe/sente este processo diretamente?
- O que o cliente espera nesse momento, e o que costuma realmente acontecer?

## Classificação de confiabilidade do dado coletado

Ao registrar o que foi levantado, classifique cada afirmação:

- **Factual**: confirmado por mais de uma fonte (entrevista + documento, ou entrevista + dado de sistema), ou por um dado de sistema verificável.
- **Hipótese**: relatado por uma única fonte, plausível mas não confirmado.
- **Pendente**: pergunta identificada como relevante mas ainda sem resposta coletada.
- **Contradição**: duas fontes divergem sobre o mesmo ponto — registre as duas versões lado a lado, não escolha uma por preferência.
- **Caso observado**: um exemplo isolado relatado (ex.: "uma vez isso levou 3 dias") — não generalize para o processo inteiro sem mais amostras.

Nunca promova uma hipótese, um caso observado ou uma pergunta pendente a fato consolidado no relatório final. Um AS-IS que mistura os dois sem marcação explícita é a causa mais comum de recomendação errada baseada em premissa não verificada.

## AS-IS preliminar vs. consolidado

- **Preliminar**: aceitável quando há descrição parcial (relato de liderança, documentação, ou uma amostra), mas falta validação direta com quem executa. Declare explicitamente o status e o que falta.
- **Consolidado**: só é declarado quando o mapeamento cobre gatilho, passos, handoffs, sistemas, responsáveis, saída, exceções **e** foi validado com quem executa o processo (não apenas com o gestor).

Nunca apresente um AS-IS preliminar como se fosse consolidado — isso compromete qualquer decisão de redesenho ou priorização de IA construída em cima dele.

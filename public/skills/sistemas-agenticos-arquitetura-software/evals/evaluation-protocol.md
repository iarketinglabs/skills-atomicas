# Protocolo das avaliações

Estas avaliações verificam decisões e limites arquiteturais por meio de cenários sintéticos. Não medem conhecimento de nomes de padrões nem substituem revisão humana.

## Execução

1. Apresente o mesmo cenário e as mesmas restrições ao agente com e sem a skill, mantendo runtime e contexto comparáveis.
2. Na condição sem skill, remova apenas a orientação desta skill; conserve as instruções gerais do runtime.
3. Não mostre `expected_output` nem `expectations` a quem produz a resposta.
4. Aplique cada expectativa como **cumprida**, **parcial** ou **não cumprida**, citando a parte da resposta que sustenta a avaliação.
5. Avalie a adequação e os trade-offs, não a preferência pessoal por uma topologia. Mais do que uma opção pode passar se respeitar os mesmos requisitos e explicar as suas condições.
6. Registe versão da skill, modelo/runtime, data, contexto fornecido e limitações da execução. Um único resultado não é estimativa estatística de desempenho.

## Critérios críticos

Uma avaliação não passa se a resposta:

- apresentar preferência ou rótulo como requisito confirmado;
- atribuir ao prompt a garantia de autorização ou impedir efeitos indevidos;
- recomendar uma opção sem ligar a escolha a requisitos observáveis;
- omitir o risco central da alternativa que recomenda;
- tratar uma hipótese, métrica de fornecedor ou padrão emergente como facto universal.

Os restantes critérios são graduais. Documente desacordos e exemplos novos antes de alterar a skill; evite acrescentar regras universais para corrigir uma preferência isolada.


# Padrões e anti-padrões

## Padrões úteis

### Descrição conectada

Prefira uma sequência que conecte sujeito, ação e ambiente:

```text
A documentary photograph of a cyclist riding through light rain on a city street at night, with wet asphalt reflecting streetlights.
```

Isso é mais controlável do que uma coleção de termos desconexos.

### Prioridade explícita

Coloque logo no início o que não pode falhar: sujeito, enquadramento, aspecto ou mudança única. Detalhes decorativos vêm depois.

### Restrição verificável

Escreva exclusões observáveis: `no text, no logos, no watermark`. Evite instruções vagas como “make it perfect” ou listas genéricas de defeitos sem relação com a cena.

### Edição com invariantes

Declare uma mudança única e enumere o que deve permanecer. Se duas mudanças forem independentes, proponha duas iterações para reduzir deriva.

## Anti-padrões

| Anti-padrão | Correção |
| --- | --- |
| Keyword salad | Formar frases coerentes e retirar termos sem função visual. |
| Detalhes inventados | Marcar como suposição ou perguntar quando mudarem a imagem. |
| Instruções conflitantes | Escolher uma prioridade ou pedir resolução do conflito. |
| Sintaxe portátil por engano | Separar núcleo visual de flags e controles da plataforma. |
| Edição ampla com preservação crítica | Limitar a uma mudança e declarar invariantes. |
| Promessa absoluta | Informar que o resultado requer inspeção e possível iteração. |

## Diagnóstico de falha

- Sujeito errado: mova o sujeito e atributos essenciais para o início; reduza personagens ou objetos concorrentes.
- Composição errada: declare plano, ângulo, posição e espaço negativo de modo mensurável.
- Estilo inconsistente: escolha um único meio e uma direção de luz/paleta compatível.
- Texto incorreto: reduza a quantidade de texto, use literal exato e valide ortografia no resultado.
- Edição vazando para outras áreas: encurte o pedido, repita invariantes e faça uma mudança por vez.

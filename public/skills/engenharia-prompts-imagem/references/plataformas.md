# Adaptação por plataforma

Escreva primeiro o núcleo visual em linguagem natural. Em seguida, adapte somente os elementos que a plataforma confirmada suporta na interface escolhida. Interfaces e versões mudam: se houver dúvida, mantenha o núcleo e peça confirmação em vez de inventar sintaxe.

## Midjourney

- Use descrição coesa seguida de parâmetros documentados pela versão em uso.
- A proporção costuma ser expressa por `--ar largura:altura`; por exemplo, `--ar 9:16`.
- Use `--no` apenas para exclusões simples e relevantes. Não converta uma longa lista genérica de defeitos em suposta garantia de qualidade.
- Peso, estilização, versão e outros parâmetros são opcionais e devem ser usados apenas quando a pessoa os pediu ou confirmou que a interface os suporta.

## Stable Diffusion

- Separe prompt positivo, prompt negativo e configurações quando a interface apresentar campos próprios.
- Expresse proporção por dimensões aceitas pela interface/modelo, não por uma flag de Midjourney.
- Pesos, seed, sampler, steps e CFG são configurações do fluxo/modelo; proponha-os apenas quando o usuário controlar esses parâmetros e precisar de reprodutibilidade.
- Se o modelo aceitar ênfase textual, documente a sintaxe escolhida como dependente daquele modelo ou interface.

## Flux

- Prefira frases naturais, claras e focadas na composição para um prompt portátil.
- Não assuma que uma interface Flux aceita prompt negativo, pesos, seed, JSON ou flags de razão de aspecto; esses controles dependem do provedor e do fluxo.
- Quando a interface oferecer um seletor de tamanho/proporção, indique o valor desejado fora do texto do prompt e mantenha no prompt apenas a composição vertical ou horizontal necessária.

## Checklist de conversão

1. O núcleo preserva sujeito, ação, cenário, luz, formato e restrições?
2. Há uma flag ou sintaxe que pertence a outra plataforma?
3. Configurações estão separadas do prompt quando a interface tem campos próprios?
4. A saída deixa claro o que depende da interface/modelo?

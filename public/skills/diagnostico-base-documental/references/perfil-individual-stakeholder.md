# Perfil Individual de Stakeholder

Extensão opcional da base documental — use quando um indivíduo merece um mapeamento mais profundo que o registro coletivo de stakeholders previsto no PRD.

## Quando criar

- O stakeholder é um sponsor com uso pessoal intenso de IA ("power user"), cujos hábitos e ferramentas já construídas valem um mapeamento à parte.
- O stakeholder é decisor-chave cuja rotina/conhecimento tácito concentra risco operacional real (ex.: "se essa pessoa se afastar, o quê para?").
- O usuário pede explicitamente um perfil individual.

Não crie um perfil individual para cada integrante da equipe; use o documento coletivo de stakeholders definido pelo PRD para o mapeamento geral. Reserve perfis individuais para casos que justifiquem esse nível de detalhe.

## Estrutura recomendada

```text
<Cliente>/<Nome do Stakeholder>/
├── README.md
├── rotina-e-conhecimento-tacito.md
├── fluxo-de-informacao.md
└── oportunidades-e-piloto.md
```

Se o projeto já tiver um roteiro de descoberta para esse mapeamento individual, use-o como referência estrutural — os quatro arquivos abaixo organizam os temas recorrentes sem substituir o roteiro aprovado.

### `README.md`
- Metodologia: qual roteiro/pauta orienta este perfil, se houver um.
- **Nota de proveniência obrigatória:** deixe claro se o conteúdo veio de uma sessão dedicada ao roteiro, ou se foi coletado de forma orgânica dentro de conversas com outro objetivo principal (o caso mais comum). Se algum bloco do roteiro nunca foi de fato coberto na prática, diga isso explicitamente — não preencha por inferência.
- Links para os 3 documentos abaixo.

### `rotina-e-conhecimento-tacito.md`
- **Rotina real:** momentos recorrentes da semana ou do mês — gatilho, canal e quem executa ou recebe a delegação.
- **O que a pessoa busca ou relembra com frequência:** informação, template, configuração ou decisão que costuma reexplicar ou consultar — e onde isso está hoje, quando conhecido.
- **Conhecimento crítico e limites de julgamento:** erro que a pessoa considera inaceitável (cite a fonte direta); casos concretos em que questionou se IA ajudaria; o que já virou processo documentado e o que ainda depende de seu julgamento; risco de perda de conhecimento quando a equipe muda.

### `fluxo-de-informacao.md`
- Mapa do fluxo de um processo importante do início ao fim, do jeito que essa pessoa descreve (não do jeito idealizado).
- Pontos de quebra nomeados pela própria pessoa — priorize a evidência direta sobre inferências da equipe de diagnóstico.
- O que deveria virar registro e hoje só fica em conversa/gravação.
- O que muda de caso para caso (ex.: cliente A vs. cliente B, com intensidades de acompanhamento opostas) — útil como par de referência para calibrar risco de automação.

### `oportunidades-e-piloto.md`
- **Regra central: nunca invente uma escolha de piloto.** Se a fonte real não chegou a uma decisão formal de "por onde começar", registre isso explicitamente como não resolvido — qualquer piloto sugerido é sinalização indireta (`hipótese`), nunca decisão fechada.
- Sinalizações indiretas de prioridade: o que a pessoa sugeriu testar ou pediu para discutir. Registre a origem e o contexto sem converter uma menção informal em decisão formal.
- Compromissos que essa pessoa assumiu entregar (documentos, gravações, listas) — consolide com status de recebido/pendente, cruzando com o rastreador de lacunas.
- Casos de uso de IA associados à pessoa — evite duplicar o inventário geral da base; resuma o ângulo individual (motivação, contexto e limites observados).

## Propagação

Todo achado material de um perfil individual segue as mesmas regras de propagação de qualquer rodada de refinamento (`metodologia-rodadas-refinamento.md`, Passo 6) — matriz de evidências, lacunas, changelog.

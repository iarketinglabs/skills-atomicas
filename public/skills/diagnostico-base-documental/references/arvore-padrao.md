# Árvore Padrão da Base Documental

Estrutura de referência. Use `executions/src/diagnostico/` como caminho padrão quando o PRD ou a convenção do repositório não definir outro destino. Adapte a árvore e os placeholders (`<...>`) ao escopo aprovado e à operação real da empresa; esta forma é um modelo, não um requisito universal.

```text
executions/src/diagnostico/
├── README.md
├── indice-entregaveis.md
├── matriz-evidencias.md
├── lacunas-e-plano-de-coleta.md
├── registro-atualizacoes.md
├── <Cliente>/
│   ├── contexto-e-alinhamento-executivo.md
│   ├── lideranca-stakeholders-e-mudanca.md
│   ├── backlog-documentacao-e-contexto.md
│   └── <Nome do Stakeholder>/          ← opcional, ver perfil-individual-stakeholder.md
├── Operacoes/
│   └── <N>.<Area>/                     ← uma pasta por área operacional priorizada
│       ├── README.md
│       ├── as-is-<area>.md             ← só quando a área tiver AS-IS consolidável (gatilho, passos, handoffs, sistemas, responsáveis, saída, exceções, validação)
│       ├── gargalos-e-evidencias.md    ← só quando já houver sinal concreto (volume, retrabalho, tempo)
│       ├── roteiro-coleta-<area>.md    ← pauta objetiva para fechar as lacunas da área
│       └── lacunas.md
└── <PastaDeIA>/                        ← use o nome que a empresa adota para sua iniciativa de IA
    ├── README.md                       ← se a empresa já tiver um framework/nome próprio para sua operação de IA, explique-o aqui
    ├── inventario-ferramentas-e-uso-ia.md
    ├── readiness-e-cultura-ia.md
    ├── shadow-ai-riscos-e-politica-minima.md
    ├── modelo-coi-roi.md
    ├── roadmap-e-governanca.md
    └── auditoria-<sistema-central>.md  ← opcional, só se o cliente pedir explicitamente uma auditoria de uma ferramenta específica
```

## Documentos-raiz do modelo

Quando o PRD adotar esta árvore, use os cinco documentos abaixo na raiz. O PRD pode ajustar nomes ou entregáveis conforme o diagnóstico.

| Documento | Função |
|---|---|
| `README.md` | Explica a árvore, as convenções do diagnóstico e o estado geral da coleta. Primeiro arquivo que qualquer pessoa ou agente deve ler. |
| `indice-entregaveis.md` | Liga cada entrega aprovada ao documento-base, estado, evidência disponível e condição objetiva de avanço. Espelha o escopo acordado e acompanha o estado real. |
| `matriz-evidencias.md` | Registra apenas evidências **materiais** — que podem mudar uma decisão, um cálculo, um risco, uma recomendação ou uma entrega. Não é um índice exaustivo de todas as fontes do projeto. |
| `lacunas-e-plano-de-coleta.md` | Consolida perguntas objetivas, donos esperados, fontes prováveis e entregas bloqueadas por cada lacuna. |
| `registro-atualizacoes.md` | Changelog de mudanças substantivas em fatos, hipóteses, pendências e versões de documentos. Atualizações de forma (typo, formatação) não entram. |

## Convenção por área operacional

No modelo desta skill, cada pasta de `Operacoes/<N>.<Area>/` tem `README.md` e `lacunas.md`. Os demais arquivos (`as-is-*.md`, `gargalos-e-evidencias.md`, `roteiro-coleta-*.md`) só existem quando há evidência suficiente para sustentá-los; um arquivo vazio sugere uma cobertura inexistente.

A numeração das pastas (`1.`, `2.`, ...) segue a ordem de investigação aprovada para o projeto — nunca é, por si só, um ranking final de impacto (isso depende dos gates de priorização, ver `regras-de-governanca.md`).

## Convenção da pasta de IA

O nome da pasta de IA deve refletir a linguagem que a empresa já usa, se houver uma. Se existir um framework próprio, documente-o no `README.md` dessa pasta e conecte os documentos existentes a ele.

## Lição de campo: decisões de convenção não previstas no PRD

Em algum momento a operação real pode apresentar um processo que não se encaixa perfeitamente na árvore aprovada (ex.: um processo na fronteira entre áreas ou um perfil individual que ainda não foi previsto). Quando isso acontecer:

1. Não crie uma pasta nova sem necessidade — primeiro veja se algum arquivo existente já é o lugar natural.
2. Tome a decisão conforme o escopo aprovado e **documente o porquê no `README.md` raiz**, na seção de convenções.
3. Se a ambiguidade tiver mais de uma leitura razoável ou afetar a navegação das entregas, apresente as opções ao usuário.

# Modos, perfis, voz e variantes

## Modos de saída

### Reescrever

Use como padrão quando o pedido for apenas "humanizar" ou "tirar o tom de IA". Trabalhe internamente em três passes:

1. rascunho que corrige os problemas sem inventar conteúdo;
2. auditoria de fatos, voz, locale, trechos protegidos e padrões restantes;
3. versão final com o menor número de mudanças que resolve o problema.

Entregue a versão final. Acrescente `Problemas encontrados` e `O que mudou` quando o usuário pedir explicação ou quando as decisões editoriais puderem causar dúvida.

### Detectar

Liste o padrão, cite o trecho mínimo necessário, classifique a gravidade e indique uma correção possível. Não reescreva, não atribua autoria e não transforme sinais em uma nota global.

### Editar arquivo

Leia o arquivo inteiro. Edite apenas prosa autorizada. Preserve frontmatter, código, dados, destinos de links, títulos, citações e exemplos. Depois releia o arquivo e confirme as alterações com localização suficiente para conferência.

### Embutido

Quando a skill for uma etapa de outro fluxo, devolva somente o texto final ou a saída solicitada. Não acrescente auditoria, prefácio ou convite para continuar.

## Perfis de contexto

O contexto controla a tolerância; não substitui a voz do autor.

| Contexto | Prioridade | Tolerância |
|---|---|---|
| Social, incluindo LinkedIn | clareza, ritmo, especificidade e CTA proporcional | permite fragmentos, listas e um emoji se forem escolhas do canal; rejeita promessa vazia e hashtags em bloco |
| Artigo ou ensaio | progressão, densidade e voz | aplica o catálogo completo; preserva digressão com função |
| Documentação técnica | precisão, sujeito claro e instruções | aceita listas, fragmentos de referência, termos técnicos e passiva útil |
| E-mail ou proposta de alta confiança | clareza, evidência e pedido explícito | tolerância baixa a promoção, hedging, autoridade vaga e conclusão genérica |
| Conversa, chat ou nota interna | intenção e autenticidade | corrige apenas sinais fortes; preserva abreviações, contrações e imperfeições da voz |

Se o usuário especificar o contexto, use-o. Caso contrário, infira pelo formato e diga qual perfil foi usado apenas se houver risco de interpretação errada.

## Perfis de voz

- **Casual:** contrações e frases curtas podem permanecer; preserve calor, humor e primeira pessoa.
- **Profissional:** use voz ativa, afirmações concretas e pedidos claros; não transforme o texto em release corporativo.
- **Técnica:** defina termos na primeira ocorrência, use instruções diretas e preserve jargão necessário.
- **Acolhedora:** fale com o leitor sem empatia performática e sem prometer compreensão que o texto não demonstra.
- **Direta:** comece pelo ponto, reduza hedging e use períodos para dar contraste, sem transformar tudo em slogan.

Uma amostra do autor tem precedência sobre um perfil escolhido. Não substitua palavras simples por vocabulário "melhor".

## pt-BR e pt-PT

### Identificação

1. Use a variante solicitada pelo usuário.
2. Se não houver pedido, preserve a variante dominante do texto ou da amostra.
3. Se não houver sinais suficientes, adote pt-BR por padrão e informe a escolha quando ela afetar o resultado.

### Consistência

- pt-BR: `usuário`, `arquivo`, `equipe`, `celular`, `treinamento`, `fato`, colocação pronominal e pontuação que já aparecem no texto.
- pt-PT: `utilizador`, `ficheiro`, `equipa`, `telemóvel`, `formação`, `facto`, construções e acentuação usadas pelo autor.
- Não imponha uma lista fixa se o texto tiver termos de produto, nomes oficiais ou preferência explícita.
- Não converta variante apenas para remover um padrão de IA. A escolha regional é parte da voz.
- Preserve o registro formal, informal ou técnico do texto em qualquer uma das variantes.

## Regras para casos ambíguos

- Se o autor pede "profissional", isso não autoriza apagar humor, crítica, primeira pessoa ou incerteza legítima.
- Se falta uma fonte, não substitua a afirmação por uma fonte genérica. Marque a pendência.
- Se uma palavra aparece no catálogo, julgue o sentido local antes de trocar. Termos técnicos e usos literais permanecem.
- Se a edição exigiria mudar um fato, uma citação, uma decisão de locale ou o objetivo do texto, pergunte ou entregue a alteração como opção separada.

# Linter e Type Checks

Parte de **Qualidade e Validação** (ver Framework Mental no `SKILL.md`). O verificador determinístico mais barato e mais rápido do cluster de qualidade — e o arquivo canônico para a patologia de "perseguir fantasmas" (erros de ambiente preexistentes).

## O compilador como verificador natural

Em linguagens de tipagem estática forte, o próprio compilador atua como um inspetor de qualidade automatizado, sem custo de inferência:

- **Prevenção de alucinação:** se um agente inventa uma função inexistente ou alucina o retorno de um endpoint, o type-check intercepta a falha de imediato no terminal local, antes que a alteração chegue ao repositório principal.
- **Compilação como proxy de correção:** quando o código compila sem erros em uma linguagem com tipagem rígida, a probabilidade de a lógica de negócio estar correta é sensivelmente superior à de código que "só roda".

## A patologia dos "fantasmas" (ambiente quebrado)

Um dos erros mais caros ao plugar agentes de terminal é rodá-los em um ambiente de desenvolvimento já quebrado — um monorepo com erros globais de lint preexistentes ou uma configuração de tipos desalinhada na raiz do projeto.

```
[erro de configuração global preexistente]
              │
              ▼
LOOP DE PÂNICO AGÊNTICO
  1. o agente altera o arquivo X para corrigir um bug simples
  2. o harness roda o type-check para validação
  3. o type-check retorna dezenas de erros globais preexistentes
  4. o agente assume que a culpa é do seu commit recente
  5. entra em loop tentando consertar erros que não causou
  6. reverte a mudança, tenta dezenas de remendos, esgota tokens
```

Se você apresentar um erro "fantasma" (de sistema, não relacionado à tarefa ativa) a um agente, ele o perseguirá indefinidamente. **A solução é sempre de arquitetura, nunca de prompt:** o ambiente local precisa estar 100% limpo antes de qualquer agente ser conectado a ele. Se um desenvolvedor humano se depararia com os mesmos avisos globais, a correção correta é consertar a configuração do repositório de vez — não explicar o erro a cada nova sessão de agente.

## Codificar o "gosto" como infraestrutura, não como prompt

É comum notar um agente repetindo o mesmo erro de estilo várias vezes. A tentação intuitiva é escrever prompts e diretrizes cada vez maiores para "educar" o modelo — mas isso causa inchaço de contexto e reduz a precisão da janela de atenção.

**A prática correta: converter regra de negócio em infraestrutura de software.** Em vez de poluir o prompt com "nunca use importações absolutas" ou "sempre valide este formato", escreva uma regra de lint personalizada ou um script determinístico no projeto. A partir do momento em que a regra física existe no repositório, toda aquela classe de problema é prevenida para sempre por automação pura — sem gastar um único token de contexto repetindo a instrução a cada sessão.

O arquivo mestre de instruções do agente deve ficar curto e servir só como um registro enxuto de "pegadinhas" (gotchas) específicas do repositório — não como um manual de estilo completo, que pertence às regras de lint.

## Integração no ciclo de vida do harness

```
[agente propõe uma alteração]
              │
              ▼
HOOK PÓS-EXECUÇÃO
  1. dispara linter e type-check locais
  2. captura os erros brutos do compilador
  3. envia os logs limpos e resumidos de volta ao agente
              │
              ▼
[auto-correção autônoma]
```

O compilador roda no ambiente isolado, e o resultado (sucesso ou lista de falhas) é injetado na memória de curto prazo do agente. Lendo o log de erro cru, o modelo rastreia a linha exata e o tipo incorreto, aplica a correção e repete a validação até a esteira retornar "verde" por completo — ver o loop genérico em `self-verification-loops.md`.

## Checklist

- Nenhum agente é conectado a um repositório com erros de lint ou compilação globais preexistentes — corrija o ambiente antes, não depois.
- Regras de estilo/convenção viram regra de lint ou script determinístico, nunca texto acumulado no prompt de sistema.
- O arquivo mestre de instruções do agente contém só gotchas específicas do repositório, não um manual de estilo completo.
- Type-check e lint disparam automaticamente após cada alteração, não só antes do commit final.

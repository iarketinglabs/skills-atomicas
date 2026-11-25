# Caching e Breakpoints / Contexto Estável e Cache de Prompts

> **Duas lentes, um só tema.** Este arquivo reconcilia "Caching e Breakpoints" (foco na mecânica financeira do cache) com "Contexto Estável e Cache de Prompts" (foco na arquitetura de montagem do prompt que sustenta esse cache). Ambas as seções do `SKILL.md` apontam para este arquivo.

Parte de **Token Efficiency / Eficiência e Gestão de Contexto** (ver Framework Mental no `SKILL.md`). A maior parte do custo financeiro de um agente não vem do texto que ele escreve — vem do volume que precisa reler a cada turno. Dominar a física do cache de prompt é o que separa um projeto viável de uma fatura de dezenas de milhares de dólares.

## A mecânica do Prefix Matching

```
Turno 1: [System Prompt (cache write)] → [Tools & Rules] → [User Msg]
Turno 2: [System Prompt (cache read, 90% de desconto)] → [Tools & Rules] → [Reply 1] → [User Msg 2]
```

O cache funciona de forma incremental e estrita, de cima para baixo: se os primeiros blocos de caracteres do prompt forem exatamente iguais aos da requisição anterior, o modelo reaproveita os vetores já calculados. Tokens lidos do cache custam uma fração do valor de uma injeção nova (referência de mercado: até 90% de desconto).

**O limiar de TTL (time to live):** o cache não é eterno — referência comum de 1 hora para a sessão principal, caindo para 5 minutos em chamadas de sub-agentes. Pausar o desenvolvimento por mais tempo que isso invalida o cache e o próximo turno paga o valor cheio.

## Cache Busting: os três gatilhos mais comuns

Qualquer alteração nos blocos iniciais do prompt invalida a correspondência de prefixo a partir daquele ponto:

1. **Troca de modelo no meio da thread:** cada modelo tem seu próprio tokenizer — alternar entre um modelo de raciocínio pesado e um mais ágil na mesma conversa zera o cache instantaneamente. Ver `model-selection-and-tiering.md` para a prática correta (mudar de sessão, não só de modelo).
2. **Timestamps dinâmicos:** carimbos de data/hora atualizados a cada segundo no início do prompt quebram o prefixo a cada requisição.
3. **Edição do arquivo de regras no meio de uma sessão longa:** alterar as diretrizes globais força reavaliação de todo o histórico desde o primeiro turno.

## Breakpoints de cache explícitos

Diferente de sistemas que inferem o cache de forma invisível, algumas APIs de modelo trabalham com breakpoints de cache explícitos, marcando blocos do prompt para retenção. A estrutura ideal ordena a informação da menos volátil para a mais efêmera:

1. **Instruções globais:** prompt de sistema fixo e definição de ferramentas.
2. **Diretrizes do projeto:** arquivo de regras e playbooks estáticos.
3. **Base de conhecimento:** documentação e material de referência.
4. **Estado da sessão:** mensagens recentes e input do turno atual.

## Arquitetura de Contexto Estável (5 camadas)

```
1. PREFIXO ESTÁVEL        — system prompt base, definição de ferramentas, regras do repositório
2. REQUISITOS DO PROJETO  — especificação do repositório, resumo de workspace
3. PROCEDIMENTOS (SKILLS) — front-matter de skills (nome + descrição curta), corpo carregado sob demanda
4. MEMÓRIA DE SESSÃO       — últimos turnos, com outputs de ferramentas já comprimidos (ver compaction-and-clipping.md)
5. ESPAÇO TRANSIENTE       — última versão de arquivos em edição, conteúdo bruto muito volátil
```

### O Prefixo Estável
Fica no topo absoluto do prompt: instruções de identidade, regras de segurança, comportamento do agente. Raramente muda ao longo de uma sessão — é a primeira e principal âncora de cache.

### Arquivo de diretrizes do repositório
Um arquivo Markdown estável na raiz do projeto, lido automaticamente a cada sessão em vez de o usuário precisar colar regras repetidamente. Centraliza preferências, tom, regras de conformidade e escopo técnico — um único ponto da verdade, altamente cacheável entre sessões.

### Progressive Disclosure de skills
Carregar o corpo completo de todas as skills disponíveis na inicialização consome tokens desnecessariamente. A prática correta: expor só o front-matter (nome + descrição curta — uma fração mínima do custo do corpo completo) no índice inicial; o agente só carrega o corpo completo quando identifica que a tarefa ativa exige aquela skill específica.

### O Espaço Transiente
Reservado para dados extremamente voláteis que mudam a cada turno (o conteúdo de um arquivo em edição ativa, uma captura de tela, HTML bruto raspado). Em vez de acumular essas versões sucessivas no histórico permanente — o que inflaria o contexto turno após turno — o harness deposita o estado atual **no final do prompt, após o último breakpoint de cache**. A cada turno, a versão antiga é sobrescrita, nunca acumulada. Como a mudança ocorre depois da última marcação de cache, as camadas anteriores permanecem cacheáveis e estáveis.

## Resumo estruturado sem degradação (Anchored Iterative Summarization)

Ver o schema completo em `../assets/anchored-summary-schema.md`. Em vez de resumir o histórico inteiro repetidamente (o efeito "telefone sem fio", onde detalhes mutam a cada ciclo recursivo), o padrão robusto atualiza incrementalmente apenas quatro campos ancorados, mesclando o bloco truncado mais recente sem reescrever o que já está consolidado.

## Ferramentas de compressão de rede

Para operações de escala industrial, é possível empregar um middleware transparente na camada de rede que intercepta e comprime outputs gigantescos de ferramentas, logs de compilador e chunks de busca de conhecimento antes que atinjam a API do modelo — reduções de até ~92% no consumo de tokens sem perda mensurável de acurácia. Ver o padrão de compressão de output de ferramentas em `compaction-and-clipping.md`.

## Métricas de impacto

| Métrica | Sem cache/contexto estável | Com cache/contexto estável otimizado |
|---|---|---|
| TTFT (tempo até o primeiro token) | Cresce linearmente a cada turno — segundos em contextos grandes | Estável, na casa de milissegundos |
| Custo de tokens de entrada | Preço cheio a cada turno | Desconto de até 90% nos tokens lidos do cache |
| Fidelidade de atenção | Degrada progressivamente ("lost-in-the-middle") | Preservada — sinal relevante livre de ruído acumulado |

## Anti-padrões

- **Cache busting dinâmico involuntário:** timestamps, IDs aleatórios ou qualquer string que mude a cada execução colocados no topo ou meio do bloco estático.
- **Monolithic Prompt Packing:** tentar antecipar toda dúvida possível e empacotar manuais inteiros no prompt base — degrada a acurácia de seleção de ferramentas antes mesmo de qualquer conversa começar.
- **Lobotomização de sessão:** compactar de forma agressiva demais sem âncoras estáveis, apagando preferências e decisões importantes registradas no início da sessão.

## Checklist

- Nenhuma string dinâmica (timestamp, ID aleatório) no bloco estático do prompt.
- Ordem do prompt segue da informação menos volátil para a mais volátil, com o espaço transiente sempre por último.
- Skills carregadas via progressive disclosure — só front-matter no índice, corpo completo sob demanda.
- Resumos de histórico usam o schema ancorado de 4 campos, nunca sumarização monolítica recursiva.

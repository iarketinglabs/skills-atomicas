# Comando Compact / Compactação e Clipping de Diálogos

> **Duas lentes, um só tema.** Este arquivo reconcilia o comando de compactação nativo de ferramentas de terminal agênticas com o framework técnico mais amplo de engenharia de contexto (trimming, compaction, summarization). Ambas as seções do `SKILL.md` apontam para este arquivo.

Parte de **Manutenção de Contexto / Eficiência e Gestão de Contexto** (ver Framework Mental no `SKILL.md`). Como comprimir ativamente a janela de conversação sem perder a informação que importa.

## Os quatro compartimentos do contexto

```
1. SYSTEM MESSAGE & POLICIES  — prompt de sistema, prefixo cacheado, regras do repositório (estático)
2. ACTIVE WORKING MEMORY      — metas ativas, decisões registradas, requisitos do projeto (dinâmico)
3. CONVERSATION TRANSCRIPT    — últimos N turnos, com payloads de ferramentas encolhidos
4. TRANSIENT SPACE            — conteúdo não-persistente (arquivo em edição, HTML cru)
```

Engenharia de Contexto é a disciplina de curar ativamente, a cada turno, quais desses compartimentos ficam visíveis ao modelo — não deixar tudo se acumular passivamente.

## Três técnicas de compressão, em ordem de sofisticação

### 1. Trimming (poda simples)
Exclusão determinística direta dos turnos mais antigos, mantendo visível só os últimos N turnos.
- **Vantagens:** latência zero, implementação trivial, corte imediato de custo.
- **Desvantagens:** operação com perda de sinal — decisões e preferências acordadas no início da conversa somem sem aviso.
- **Melhor caso de uso:** operações repetitivas e homogêneas de ferramentas, subtarefas independentes entre si.

### 2. Compaction (compactação cirúrgica de payloads)
Preserva intacto o fluxo de perguntas e respostas entre usuário e agente, mas varre os turnos antigos em busca de saídas volumosas de ferramentas (esquemas de banco, retornos JSON massivos) e as remove fisicamente, deixando um placeholder com metadados (ID da chamada, status, tamanho original, resumo de duas linhas).

```python
def compact_tool_outputs(history):
    """Clipping cirúrgico: remove payloads de ferramenta grandes, preserva um resumo."""
    compacted = []
    for msg in history:
        if msg.get("role") == "tool" and len(msg["content"]) > 300:
            summary = {"status": "OK", "clipped_byte_size": len(msg["content"])}
            compacted.append({"role": "tool", "content": f"[TOOL OUTPUT CLIPPED] {json.dumps(summary)}"})
        else:
            compacted.append(msg)
    return compacted
```

Isso preserva a sequência lógica do raciocínio do agente (ele ainda sabe que executou a ferramenta e qual foi o resultado), liberando uma fração muito grande dos tokens gastos com logs desnecessários (referência de mercado: até ~80%).

### 3. Summarization (sumarização ancorada)
Comprime blocos de conversa antiga em resumos densos. A sumarização monolítica ingênua (resumir o histórico inteiro repetidamente) sofre do efeito "telefone sem fio" — detalhes mutam a cada ciclo. A solução robusta é o **schema de resumo ancorado**, detalhado em `../assets/anchored-summary-schema.md`: apenas o bloco truncado mais recente é resumido e mesclado incrementalmente a uma estrutura de campos fixos, nunca reescrita do zero.

## O padrão de Espaço Transiente

Para dados extremamente voláteis (código HTML raspado a cada clique, o estado atual de um arquivo em edição), a solução não é nenhuma das três acima — é nunca deixar essa informação entrar no histórico permanente. O harness reserva uma seção no final do prompt, depois do último breakpoint de cache, e sobrescreve integralmente a cada turno. Ver aplicação completa em `prompt-caching-and-stable-context.md`.

## O comando de compactação nativo: mecânica e patologias

Ferramentas de terminal agênticas costumam oferecer um comando nativo de compactação que intercepta a sessão, envia todo o histórico ao modelo e ordena uma compressão semântica — de um texto longo e circunstancial para uma frase densa que preserva só o essencial. Economia típica: 40–50% do tamanho da janela ativa.

**As três patologias desse comando:**
1. **Overhead síncrono:** compactar um histórico grande exige processamento síncrono da API — o terminal pode ficar congelado por mais de um minuto.
2. **Context Loss:** a compressão probabilística é agressiva e pode omitir decisões arquiteturais finas, variáveis críticas ou regras de conformidade acordadas no início — forçando o usuário a reexplicar o projeto.
3. **Risco de execução inoportuna:** se disparado no meio de uma depuração delicada, o agente pode perder referências cruzadas de tentativas anteriores e entrar em loop de erro repetitivo.

### Post-Compaction Hooks
Como a compactação apaga informação indispensável (identidade, regras do repositório), um hook determinístico dispara automaticamente logo após o processo terminar, reinjetando no topo do novo prompt condensado as diretrizes que foram varridas — sem que o usuário precise redigitar nada.

## O padrão superior: Session Handoff em vez de compactar

Por causa da lentidão e da perda de precisão do comando nativo, a prática de elite é evitá-lo em favor do **Session Handoff**: gerar um resumo estruturado, resetar 100% a sessão, e iniciar uma nova sessão limpa carregando só o resumo. Ver o desenvolvimento completo (anatomia do documento de handoff, quando disparar) em `handoff-documentation.md` e `focused-task-sessions.md`.

**Por que o handoff vence a compactação nativa:**
- **Velocidade:** gerar o resumo e resetar leva menos de um minuto, contra o processamento síncrono pesado da compactação.
- **Precisão cognitiva máxima:** a nova sessão reinicia no topo da acurácia, livre de qualquer ruído semântico de erros passados — não uma versão "resumida" desse ruído.
- **Economia real:** evita o faturamento linear recorrente de um histórico inflado a preço cheio a cada novo turno.

## Métricas de sucesso da engenharia de contexto

- **TTFT (tempo até o primeiro token):** proporcional ao tamanho do prompt enviado — janelas enxutas reduzem de segundos para milissegundos.
- **Token Saving Efficiency:** razão entre volume bruto original e volume final enviado após os filtros de compressão.
- **Accuracy Loss Rate:** percentual de regressões causadas por apagamento involuntário de dados durante a compressão — compactação agressiva demais "lobotomiza" o agente, fazendo-o esquecer arquivos já modificados ou a meta estratégica ativa.

## Segurança na compactação

Toda rotina de compactação/sumarização deve passar por um filtro de redação de segredos **antes** de qualquer processamento — credenciais e chaves de API nunca devem ser incluídas, sequer temporariamente, no texto enviado a um modelo de resumo (nem local, nem em nuvem).

## Checklist

- Nenhuma sessão longa é comprimida sem antes checar se um handoff completo (encerrar e recomeçar) não seria mais rápido e mais preciso.
- Post-Compaction Hooks ativos, reinjetando identidade e regras logo após qualquer compactação.
- Payloads grandes de ferramentas são clipados com placeholder de metadados, nunca mantidos brutos no histórico.
- Resumos usam o schema ancorado de 4 campos, nunca sumarização monolítica recursiva.
- Redação de segredos roda antes de qualquer texto ser enviado a um pipeline de compressão.

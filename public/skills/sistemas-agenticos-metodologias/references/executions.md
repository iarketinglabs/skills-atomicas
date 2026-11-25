# Executions (Scripts Determinísticos)

Parte de **Organização de Projetos** (ver Framework Mental no `SKILL.md`). O lado "como executar de forma determinística" da divisão Directives/Executions — `directives.md` cobre o lado "o que fazer e por quê".

## O anti-padrão que motiva esta prática: YOLO Scripting

Dar a um agente acesso direto a um terminal com instruções genéricas, esperando que ele escreva e execute seus próprios utilitários e conexões de rede em tempo real, é uma receita para desastre:

- **Erros sintáticos de shell:** encadeamentos complexos de comandos geram falhas redundantes por pequenos erros de formatação.
- **Risco de destruição física:** um agente proativo instruído a "limpar arquivos temporários" pode, por uma alucinação de caminho, executar uma exclusão catastrófica de dados reais.
- **Inchaço de contexto:** construir scripts do zero na conversa consome tokens, e os logs de erro resultantes poluem a memória de curto prazo do modelo.

## A separação: Camada Cognitiva vs. Camada de Execução

```
CAMADA COGNITIVA (modelo probabilístico)
        │ decide "o que" fazer
        ▼
CAMADA DE EXECUÇÃO (CLI determinística)
        │ executa na sandbox
        ▼
retorna logs limpos
```

Em um repositório preparado para agentes, o agente nunca escreve lógica operacional complexa do zero no terminal. O arquiteto do projeto disponibiliza uma biblioteca de scripts determinísticos pré-testados; o agente atua como orquestrador, chamando esses scripts com os parâmetros necessários.

- **Abordagem insegura:** o agente escreve e executa um script customizado que raspa arquivos, formata dados e tenta fazer commits de forma manual.
- **Abordagem segura:** o agente chama um comando único pré-configurado (ex. `run generate:handoff --issue-id=102`). Toda a lógica pesada está codificada no script físico em disco, com previsibilidade total.

## O padrão "Printing Press" para eficiência de tokens

Quando um comando de execução retorna milhares de linhas de log desordenado, a janela de contexto sofre inchaço severo. O script determinístico intercepta a saída bruta do console **antes** que ela atinja a janela de atenção do modelo: remove caminhos irrelevantes, suprime avisos redundantes, condensa o erro em um payload estruturado de poucas centenas de tokens (arquivo, linha exata, mensagem curta) — economizando a maior parte do consumo de tokens em cada turno de depuração.

## Segurança no sandbox

Toda execução de script deve ocorrer dentro de uma sandbox isolada de uso único — o agente nunca tem acesso à máquina física nem a bancos de dados de produção reais. **Atenção ao bypass de duas etapas:** um agente pode tentar contornar um bloqueio direto de comando escrevendo um script secundário que executa a ação proibida e depois chamando esse script sob o pretexto de "depuração". Ganchos síncronos de ciclo de vida devem monitorar tanto comandos diretos quanto a criação de novos arquivos executáveis — não só a entrada de terminal. Ver o desenvolvimento completo de sandboxing e desse vetor de ataque na skill de Segurança e Confiabilidade desta coleção, se disponível.

## O loop de auto-correção offline

```
[agente escreve/altera um arquivo]
              │
              ▼
SCRIPT DETERMINÍSTICO DE VALIDAÇÃO
  1. roda linter e type-check
  2. captura os erros sintáticos brutos
  3. formata em um resumo conciso
              │
              ▼
[agente lê o log formatado e se autocorrige]
```

O harness aciona automaticamente o script de validação após cada alteração; o script devolve uma mensagem cirúrgica ("sua alteração quebrou a tipagem na linha X do arquivo Y"); o agente aplica a correção e o ciclo se repete até o script retornar sucesso — sem que um humano precise monitorar a esteira.

## Blindagem da suíte de testes

Para impedir que o agente "burle a linha de chegada" (comentar asserções, reescrever testes para forçar aprovação artificial — ver o desenvolvimento completo em `specs-for-persistence.md`), a pasta de testes e os próprios scripts determinísticos de validação são montados como volumes de somente leitura no ambiente do agente. Ele fica fisicamente impedido de alterar a barra de qualidade — só pode elevar o próprio código para alcançá-la.

## Checklist

- Nenhum agente escreve lógica operacional complexa do zero no terminal — ele invoca um script pré-testado da biblioteca de executions.
- Logs de execução passam por um middleware de compressão antes de entrar na janela de contexto do agente.
- Hooks de segurança inspecionam tanto comandos diretos quanto conteúdo de novos arquivos executáveis criados pelo agente.
- A pasta de scripts de validação e a suíte de testes são somente leitura no ambiente de execução do agente.

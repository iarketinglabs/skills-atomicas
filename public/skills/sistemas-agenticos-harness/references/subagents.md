# Subagentes e delegação

Um subagente é uma execução de agente chamada por outra parte do sistema para um objetivo delimitado. Pode oferecer paralelismo, especialização ou um limite de contexto diferente. A abstração não implica isolamento de segurança: permissões, dados, ferramentas e recursos dependem do runtime e do ambiente de execução.

## Quando delegar

Considere delegação quando uma parte do trabalho:

- tem entrada e resultado verificáveis;
- pode avançar em paralelo ou beneficia de contexto especializado;
- pode receber apenas os dados necessários;
- tem ferramentas e efeitos compatíveis com as permissões concedidas;
- custa menos do que o benefício esperado de paralelismo ou isolamento.

Prefira execução única ou sequencial quando tarefas dependem muito umas das outras, partilham estado mutável, têm risco de conflito, não possuem critério claro de conclusão ou exigem tanta coordenação que a divisão não ajuda.

Não há percentual universal de contexto em que a qualidade colapsa nem número universal de subagentes ou níveis. Contexto e paralelismo devem ser avaliados no modelo, runtime e workload concretos.

## Topologias possíveis

Uma forma simples de visualizar uma delegação é:

```text
orquestrador ou aplicação
  ├── tarefa independente A
  ├── tarefa independente B
  └── tarefa dependente C, após validação de A e B
```

Planner/worker, fan-out/fan-in, revisão independente, especialistas por domínio, agentes aninhados e execução sem planner são alternativas. Profundidade maior pode propagar erro ou acrescentar coordenação; um único supervisor pode limitar throughput e concentrar falhas. Escolha a topologia conforme dependências e limites, e deixe-a tão rasa quanto útil, não por regra fixa.

## Contrato de delegação

Cada chamada delegada deve declarar, de forma adequada ao sistema:

1. objetivo e critério de aceite;
2. dados, fontes e contexto permitido;
3. ferramentas, recursos, permissões e limites;
4. artefactos/estado que pode criar ou alterar;
5. formato de retorno, evidência e incerteza;
6. limite de tempo/custo e condição de cancelamento;
7. comportamento em erro e responsabilidade pela revisão.

O retorno deve distinguir factos observados, inferências, fontes consultadas, ações realizadas e pendências. O orquestrador verifica o contrato antes de integrar resultado ou executar efeitos consequentes.

## Contexto e autoridade

Forneça informação suficiente para a subtarefa, sem expor dados irrelevantes ou privilegiados. O princípio de contexto mínimo útil melhora foco e pode reduzir exposição; não retenha informação de que o worker precisa para respeitar as regras ou validar a saída.

Contexto separado não é uma barreira de segurança. Se o worker não puder ler ou alterar certos recursos, aplique a restrição no processo, sandbox, API ou credencial. Revalidar a autorização no destino é necessário mesmo que o prompt e o contrato da delegação estejam corretos.

Defina a autoridade do worker: leitura, edição, execução de código, chamada de serviços, acesso à rede, persistência, instalação de dependências e possibilidade de delegar. Um worker que pode criar ferramentas ou delegar precisa de escopo e auditoria explícitos.

## Paralelismo, integração e conflitos

Só paralelize tarefas cujos pré-requisitos e efeitos possam ser coordenados. Para trabalho sobre ficheiros, considere propriedade de ficheiros, branch/worktree separado, patches independentes ou uma etapa central de integração. Isolamento de diretório reduz colisões em execução, mas não elimina conflito de merge ou incompatibilidade entre resultados.

Para cada resultado paralelo, preserve proveniência e versão das entradas. Se dois workers propõem alterações incompatíveis, faça integração explícita e nova validação; não aceite a última escrita por acidente.

## Escolha de modelo e custo

Um modelo menor, mais rápido ou mais barato pode ser suficiente para uma tarefa estreita; um modelo diferente pode ter melhor desempenho em síntese ou raciocínio. Não atribua papel fixo a uma classe de modelo sem evals do workload. Meça qualidade, erro, latência, tokens, custo de coordenação, falhas de handoff e revisão humana.

Da mesma forma, contexto separado pode melhorar foco em algumas tarefas e aumentar custo de setup ou perda de informação em outras. Meça comparação com um baseline de agente único, mantendo tarefa, ferramentas e critérios equivalentes.

## Duração, encerramento e recuperação

Um subagente pode ser síncrono, persistente, reexecutável ou efémero conforme o runtime. Não assuma que workers são sempre destruídos ao concluir nem que o estado desaparece com o processo. Confirme quem possui sessões, histórico, checkpoints, artefactos e memória.

Se o processo puder repetir a delegação, inclua identificador de tarefa e tratamento de duplicados. Antes de repetir um efeito externo, consulte o estado do destino ou aplique uma política de idempotência. Registe tentativas, saída e cancelamento.

## Avaliação

Compare delegação e baseline sem delegação numa amostra representativa. Avalie conclusão correta, evidência, conflitos, dados expostos, necessidade de correção, latência, custo e clareza de recuperação. Percentagens citadas de outros sistemas não são parâmetros de desenho sem reprodução independente.

# Grafos de estado e controlo de loops

## Escolher pela necessidade de controlo

Um workflow descreve uma sequência de passos; um loop de agente repete observação, decisão e ação; um grafo explicita estado e transições. São formas de organizar controlo, não categorias de qualidade. Um sistema pode combinar as três.

| Forma | Escolha quando | Questões que continuam por resolver |
|---|---|---|
| Workflow fixo | Ordem e critérios são conhecidos antes da execução | Que condições desviam o fluxo? Como tratar pausa, falha e revisão? |
| Loop de agente | O próximo passo depende de observações semânticas | Como impor parada, orçamento, progresso, autorização e proteção contra repetição? |
| Grafo de estados | Ramos, invariantes, pausa, retomada ou auditoria precisam ser explícitos | Como versionar/serializar estado e tratar efeitos que ocorreram fora do grafo? |
| Composição | Fases diferentes têm necessidades diferentes de decisão e controlo | Qual é o contrato entre fases e quem é dono do estado e de cada efeito? |

Um grafo pode conter ciclos. Escolha uma DAG apenas quando a tarefa tiver uma ordem acíclica por requisito; não tome a forma do diagrama como regra geral.

## Contrato mínimo do loop

Defina no runtime ou na aplicação, fora da decisão livre do modelo:

- estado inicial e dados de entrada autorizados;
- condição de sucesso e critério de falha;
- limite de iterações, duração, custo ou recursos relevante;
- sinal observável de progresso e comportamento quando não há progresso;
- tratamento de respostas inválidas e chamadas repetidas;
- permissões por ferramenta e ponto de aprovação, quando necessário;
- condição de escalonamento, interrupção ou intervenção humana;
- o que é persistido e como retomar após falha, se isso for requisito.

Um limite de iterações não garante que exista progresso; timeout não cancela necessariamente um efeito remoto que já foi aceite. Combine esses limites com observabilidade e política operacional apropriadas.

## Estados e transições

Mantenha a representação de estado tão pequena quanto os requisitos permitirem. Para cada transição, registe:

1. **Pré-condição:** que estado e autorização devem existir?
2. **Entrada:** que dados são lidos e quais são confiáveis?
3. **Decisão:** que parte é código e que parte depende do modelo?
4. **Efeito:** que chamadas externas podem alterar dados ou criar consequências?
5. **Resultado:** que evidência confirma sucesso, rejeição ou incerteza?
6. **Próximo estado:** como o estado muda e o que se audita?

Validar uma transição no grafo não valida automaticamente o efeito no serviço remoto. Revalidar autorização no ponto do efeito evita confiar apenas num estado antigo ou numa proposta do modelo.

## Pausa, retomada e efeitos externos

Uma interrupção para aprovação deve preservar contexto suficiente para a pessoa compreender a ação proposta, o alvo, as consequências e a evidência disponível. Ao retomar, valide se a autorização continua válida e se o estado relevante não mudou.

Timeout, retry, backoff, idempotência e conciliação de efeitos remotos pertencem à política de resiliência da aplicação. Antes de repetir uma operação, determine se o primeiro pedido chegou ao destino. Se o resultado for incerto, consulte o destino, use chave de idempotência ou faça conciliação explícita, conforme o contrato disponível. Um grafo/checkpoint não torna a chamada externa exatamente uma vez.

## Persistência, checkpoint e replay

O contexto enviado ao modelo pode ser uma projeção do estado persistido; não precisa ser o registo canónico. Se a continuidade após falha for requisito, confirme:

- quando o checkpoint é criado e o que contém;
- qual backend e política de retenção são usados;
- como dados sensíveis e escopos de utilizador são separados;
- como o estado é atualizado entre versões;
- se retomada reexecuta um nó ou etapa;
- como efeitos já realizados são reconhecidos;
- se replay é permitido, seguro e auditável para o tipo de efeito.

“Tem checkpoint” informa apenas que existe um mecanismo de snapshot ou persistência definido pela implementação. Não diz, sem consultar o contrato, que todos os passos são duráveis, que o estado pode migrar ou que efeitos não serão repetidos.

## Falhas a percorrer no desenho

Faça uma revisão de fluxo para cada cenário relevante:

| Cenário | Pergunta |
|---|---|
| Modelo retorna saída inválida | Há validação, retry limitado ou caminho de erro legível? |
| Ferramenta expira | Sabe-se se o efeito ocorreu antes do timeout? |
| Processo cai entre o efeito e o checkpoint | Como detectar e conciliar a lacuna? |
| Aprovação demora ou chega após mudança de estado | A aprovação expira ou é revalidada? |
| Ciclo repete sem progresso | Que limite interrompe e que diagnóstico é produzido? |
| Estado muda de schema | Há versão, migração ou tratamento de estado antigo? |
| Reexecução recebe dados parcialmente atualizados | Qual é a fonte de verdade e como evitar decisão sobre snapshot obsoleto? |

## Comparar implementações

Frameworks podem oferecer grafos tipados, inferência de arestas, checkpointers, interrupções ou persistência. Classifique cada alegação como verificação estática, validação em runtime, snapshot, journal, replay, convenção ou garantia do serviço externo. Confirme o modo concreto de uso e a versão; capacidades opcionais podem exigir configuração adicional.

Não trate tipos Python como prova de corretude em runtime nem o uso de um grafo como garantia de segurança. Consulte os perfis de [Hermes](hermes-agent.md), [Pydantic](pydantic-ecosystem.md) e [LangChain](langchain-ecosystem.md) para as fronteiras documentadas de cada ecossistema.

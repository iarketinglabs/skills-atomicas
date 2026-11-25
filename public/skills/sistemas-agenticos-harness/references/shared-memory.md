# Memória e estado partilhado

O modelo não deve ser tratado como detentor de memória persistente só porque a conversa anterior ainda aparece no contexto. O sistema pode reconstruir contexto a partir de histórico, ficheiros, base de dados ou serviços; cada opção tem semântica, limites e riscos próprios.

## Distinguir as camadas

| Camada | Horizonte | Exemplos | Pergunta principal |
|---|---|---|---|
| Contexto ativo | Chamada ou etapa atual | Pedido, instruções, observações | Que dados são necessários agora? |
| Histórico de interação | Conversa ou sessão | Mensagens, chamadas, respostas | O que deve ser conservado e reintroduzido? |
| Estado de tarefa | Duração da operação | Etapa, resultado, tentativa, responsável | Como retomar e evitar conflito ou duplicação? |
| Memória reutilizável | Entre tarefas/sessões | Preferências, conhecimento validado, decisões | Quem verifica, corrige, expira e remove os dados? |
| Fonte canónica de domínio | Definida pela aplicação | Registo de negócio, estado transacional | Qual serviço é autoridade para esta informação? |

Não misture snapshot, histórico, memória e fonte canónica. Uma memória pode estar desatualizada; um histórico pode conter texto não confiável; um checkpoint só representa o que a implementação guardou.

## Seleção e qualidade

Promova informação para memória reutilizável apenas com uma regra explícita. Para cada item, considere fonte, data, escopo, confiança, validade, sensibilidade e responsável por correção. Preserve proveniência suficiente para revalidar afirmações importantes. Não transforme uma inferência do modelo em facto persistente sem revisão adequada.

Deduplicação, resumo e resolução de conflitos também podem introduzir erro. Em decisões importantes, preserve o registo original e faça a consolidação produzir uma proposta revisável em vez de substituir silenciosamente a fonte.

## Persistência e local de armazenamento

Memória pode residir em ficheiros locais, base de dados, armazenamento gerido, serviço de busca ou combinação. Escolha pela necessidade de partilha, disponibilidade, controle de acesso, latência, backups, retenção, localização dos dados, operação e portabilidade. “Local” não garante segurança; “gerido” não implica perda de controle. Documente a fronteira de confiança e como exportar, corrigir e apagar conteúdo.

Um repositório de documentos ou wiki com fontes e links pode ser útil para conhecimento relativamente estável. Um banco pode ser mais adequado a estado estruturado, concorrência e transações. A aplicação ainda precisa definir esquema, autorização, atualização e fonte de verdade.

## Compactação e consolidação

Se sessões longas ou muitos agentes acumulam informação, uma tarefa periódica de consolidação pode resumir, indexar ou propor memórias. Ela deve ter escopo, dados de entrada, fonte de verdade, limites de escrita e registo de alterações definidos. Nunca assuma que um hook de compactação ou ciclo de consolidação existe no runtime; confirme a implementação.

Avalie a memória consolidada com perguntas que exijam recuperar factos, datas, fontes e incerteza. Verifique se a memória pode ser editada, expirada ou invalidada e se uma instrução hostil pode contaminar contextos futuros. Veja `context-injection.md` para a seleção do contexto e `state-graphs-and-loop-control.md` para checkpoints de execução.

## Partilha entre agentes

Agentes podem partilhar estado via base, API, ficheiros, eventos, fila ou handoff explícito. Defina concorrência, propriedade, versionamento, autorização e conflitos. Dois agentes a escrever o mesmo documento sem lock ou integração podem perder alterações. Separar pastas ou contextos reduz certas colisões, mas não substitui controle de acesso.

Partilhe apenas os dados necessários para cada papel. Um agente que pode ler um registo não deve herdar automaticamente a permissão para alterá-lo. Revalide autorização no destino do efeito.

## KV cache não é memória de aplicação

KV cache é um mecanismo interno de inferência que alguns runtimes usam para acelerar processamento de prefixos. Não é, em geral, uma base de memória de domínio nem um canal de sincronização portável entre agentes. Suporte, escopo, duração, compartilhamento e benefício dependem de modelo, fornecedor e runtime. Meça e confirme o contrato antes de o incluir no desenho.

## Checklist

- Qual dado é contexto, histórico, estado de execução, memória ou fonte canónica?
- Quem pode ler, escrever, corrigir, expirar e apagar cada camada?
- Que fonte e data acompanham o conhecimento persistido?
- Como conflitos, escritas concorrentes e mudança de schema são tratados?
- Que dados são enviados ao modelo ou a serviços externos?
- Como uma memória errada ou obsoleta é detetada e invalidada?
- O progresso precisa sobreviver a falha? Se sim, que mecanismo de recuperação foi verificado?

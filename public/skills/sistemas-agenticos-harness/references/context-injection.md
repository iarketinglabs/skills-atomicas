# Injeção e gestão de contexto

Contexto é a informação disponibilizada ao modelo numa chamada. A janela física é um limite de entrada e saída do modelo; utilidade efetiva também depende da tarefa, do modelo, da posição da informação, de instruções concorrentes e da estratégia de seleção. Não existe um limiar de tokens universal em que todo modelo deixe de funcionar.

## Selecionar o contexto

Organize a informação por função e estabilidade:

| Tipo | Exemplos | Regra de seleção |
|---|---|---|
| Instruções e políticas | Objetivo, restrições, contratos de ferramenta | Inclua as que se aplicam à tarefa e mantenha-as versionadas |
| Conhecimento de referência | Documentação, esquemas, exemplos, regras de domínio | Recupere fontes pertinentes e preserve proveniência quando importante |
| Estado de execução | Dados de progresso, decisões e resultados anteriores | Envie a projeção mínima necessária para o próximo passo |
| Contexto situacional | Pedido atual, ficheiros, resultados, logs e observações | Carregue sob demanda, com recorte e formato que preservem sinais úteis |
| Histórico | Mensagens e chamadas anteriores | Retenha ou resuma o que ainda serve à tarefa; mantenha fonte durável fora do contexto se necessário |

O contexto não deve ser tratado como fonte canónica de estado só porque está na conversa. A aplicação decide o que persiste e o que pode ser descartado após uma etapa.

## Progressive disclosure e recuperação

Em repositórios ou bases extensas, use um índice e carregue as regras aplicáveis ao diretório, tarefa ou etapa. Pesquise trechos relevantes em vez de empilhar todo o material disponível. Quando a regra afeta todo o trabalho, deixe-a no contexto estável; quando depende da tarefa, injete-a quando necessária.

O conteúdo recuperado pode estar incompleto ou desatualizado. Guarde fonte, versão/data e evidência usada quando a decisão requer rastreabilidade. Não use apenas o ranking do retriever como confirmação de verdade.

## Orçamento de contexto

Defina o orçamento medindo os tokens com o tokenizer/endpoint reais, descontando entrada, saída reservada, ferramentas e demais limites do runtime. Estime também custo e latência. Um contador aproximado serve para triagem, não para uma garantia de limite.

Quando o contexto cresce, considere resumir, remover redundância, recuperar dados sob demanda ou externalizar resultados grandes. Avalie se a redução preservou requisitos, nomes, evidências e estado de que o próximo passo depende. Percentuais de compressão ou limites de “zona de degradação” dependem de modelo e workload; não os trate como constantes.

## Compactação e sessões

Compactação é transformação com perda possível. Defina que informações são obrigatórias após o resumo, como são verificadas e como recuperá-las da fonte original. Um hook pós-compactação só existe se o runtime o suportar e se for configurado; não presuma que instruções importantes serão restauradas automaticamente.

Uma sessão separada pode ajudar a isolar tarefas distintas ou reduzir histórico irrelevante. Continuar na mesma sessão pode preservar contexto útil e evitar custo de reconstrução. Decida com base em fronteiras de tarefa, autorização, privacidade, latência e capacidade de handoff. Se a tarefa precisa sobreviver a sessões, persista o estado necessário fora do histórico.

## Cache de prompts

Alguns provedores e runtimes oferecem cache de prefixos ou conteúdo. Regras de elegibilidade, TTL, preço, localização dos prefixos, invalidação, modelo e tamanho mínimo variam e mudam. Mantenha blocos estáveis na ordem documentada pelo fornecedor, evite mudanças desnecessárias nos prefixos e meça cache hit na configuração real. Troca de modelo ou alterações no conteúdo podem afetar cache, mas não conclua que todo modelo exige uma nova sessão.

Cache reduz parte do custo ou latência conforme o contrato do serviço; não significa que o modelo retenha memória entre chamadas, nem substitui gestão de contexto.

## Middleware de saída

Logs, respostas de API e ficheiros podem ser grandes. Um formatter pode selecionar erros, limites e amostras, mas não deve remover evidência necessária nem apresentar resumo como se fosse saída original. Mantenha acesso à fonte bruta quando auditoria ou diagnóstico exigir, com retenção e controlo de acesso apropriados.

## Checklist

- As instruções e fontes certas estão presentes para esta etapa?
- As informações recuperadas têm fonte e versão suficientes para a decisão?
- O orçamento foi medido no modelo/endpoint alvo e deixa espaço para a resposta?
- O histórico contém redundância ou dados sensíveis sem necessidade?
- Resumo, truncamento ou filtragem preservam factos críticos?
- Estado que precisa sobreviver está persistido fora do contexto?
- Caching foi confirmado na implementação atual, ou é apenas uma hipótese?

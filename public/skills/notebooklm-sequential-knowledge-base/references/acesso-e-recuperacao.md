# Acesso autorizado e recuperação

## Escolha a superfície disponível

| Acesso | Confirmação inicial | Evidência de execução |
|---|---|---|
| Conector ou CLI já autorizado | Use a operação de sessão ou um acesso de leitura suportado. Confirme que pode identificar, consultar e receber a resposta final do notebook específico. | Resultado real da consulta e citações acessíveis. Confira nomes de operações, parâmetros e funções de retomada na documentação dessa integração. |
| Interface web autorizada | Abra o notebook correto, verifique conta e fontes selecionadas e aguarde o término visível de cada resposta. | Copie a resposta final da mensagem certa. Confirme que a cópia é nova, corresponde ao tópico atual e não veio de uma consulta anterior. |
| Exportação ou texto trazido pelo usuário | Confirme notebook, tópico, data e o que foi fornecido. | Revise o material recebido. Marque a origem e a possibilidade de verificar as citações dentro do notebook. |

As ferramentas de notebook e as funções habilitadas variam por edição, fornecedor do conector e ambiente. Consulte a documentação do acesso real. A presença de uma API para gerenciar notebooks ou fontes não confirma uma operação de chat. [Chat na interface do Google](https://support.google.com/gemininotebook/answer/16179559) · [API de fontes da edição Enterprise](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks-sources)

Se a superfície oferecer pesquisa na web, notas ou execução de ações, mantenha a consulta restrita às fontes acordadas para essa extração. Caso não consiga conferir essa configuração, rotule a limitação de origem.

## Trate falhas sem perder estado

- **Sessão expirada ou permissão negada.** Pause consultas. Peça ao titular para entrar pela superfície oficial ou reautorizar o conector pelo procedimento suportado. Confirme de novo conta, notebook e fontes. Mantenha cookies, tokens, perfis e dumps de depuração fora da conversa e dos arquivos.
- **Timeout ou retorno truncado.** Verifique se a consulta original acabou e se o resultado pode ser recuperado no mesmo tópico. Se o estado for incerto, espere ou inspecione pela interface. Faça uma nova tentativa limitada somente depois de resolver a tentativa anterior e respeite limites do fornecedor.
- **Clipboard indisponível.** Peça a resposta como texto ou exportação manual. Confirme que o título, começo e fim correspondem à consulta. Se o conteúdo for sensível, evite área de transferência compartilhada.
- **Uma resposta oferece gerar relatório depois.** Reformule no mesmo tópico pedindo o conteúdo final no chat e evidência por fonte. Se continuar sem resposta utilizável, registre o bloqueio.
- **Escrita falhou.** Preserve o arquivo já concluído. Se puder recuperar a resposta com segurança, repita a escrita sem uma nova consulta. Caso contrário, informe qual item precisa ser refeito.

Registre somente a falha técnica necessária, sem conteúdo da pergunta, cabeçalhos de autenticação ou chaves de sessão. O controle de retomada vive no índice local e permanece útil mesmo se o histórico do chat ficar indisponível.

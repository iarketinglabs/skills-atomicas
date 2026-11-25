---
name: notebooklm-setup
description: Use quando o usuário pedir para criar ou reaproveitar um notebook no NotebookLM, importar fontes autorizadas, sincronizar uma pasta como directives/ ou confirmar se os documentos já podem ser consultados.
compatibility: Requer acesso autorizado ao serviço por interface ou conector disponível. Upload automatizado de arquivo local exige que a ferramenta possa ler o próprio arquivo.
---

# Configurar NotebookLM como base de conhecimento

Prepare fontes que a equipe autorizou usar na conta e no notebook certos. Para exportar respostas de um notebook existente para Markdown, use `notebooklm-sequential-knowledge-base` quando disponível.

## Entradas e execução

1. **Delimite o material.** Obtenha projeto, conta ou espaço de trabalho, alvo desejado e fontes autorizadas. `directives/` é uma convenção possível. Exclua arquivos vazios, modelos de pasta e itens cuja permissão de upload esteja indefinida. Verifique formato, limite e caminho de importação na [referência de formatos](references/formatos-suportados.md).
2. **Confirme a identidade.** Inspecione notebooks existentes pelo acesso disponível. Compare título, conta e identificador ou link retornado pela ferramenta. Em caso de homônimos, peça somente o identificador necessário. Crie um notebook se o pedido autorizar e nenhum alvo correspondente tiver sido confirmado. Se a lista estiver indisponível, ofereça confirmação manual antes de criar.
3. **Reconcilie fontes.** Para cada item, compare identidade e versão quando são comprováveis. Use identificador da fonte, referência ao original ou registro de versão confiável. Título igual sozinho sinaliza uma possível correspondência. Se houver conteúdo alterado ou divergência de origem, marque para revisão. Substituir ou excluir requer uma decisão de escopo, pois pode afetar citações e artefatos existentes.
4. **Importe os itens confirmados.** Use o método documentado no conector ou na interface. Envie apenas os documentos acordados. Se o conector remoto não tiver acesso ao arquivo, ofereça importação manual ou outra origem autorizada. Sem autenticação válida, deixe o item pendente e indique o login ou a reautorização suportada. Não peça credenciais na conversa.
5. **Verifique o processamento.** Registre cada item como existente, enviado, processando, pronto, falhou ou omitido. Se o serviço aceitar a carga e ainda a processar, mantenha o estado intermediário. Confirme prontidão na ferramenta quando observável, ou peça ao operador para confirmar na interface. Confira consulta de amostra apenas se fizer parte da entrega e tiver acesso para isso.

## Fechamento

Informe o notebook confirmado, fontes selecionadas e contagens por estado. Liste divergências, formatos ou permissões pendentes, erros e próxima ação. Em uma retomada, consulte novamente a situação dos itens enviados antes de repetir qualquer upload. Se houver somente acesso à conversa, entregue uma lista de importação e a checagem manual da prontidão.

---
name: notebooklm-sequential-knowledge-base
description: Use para extrair do NotebookLM uma base Markdown com um documento por tópico, retomar uma extração interrompida ou limpar respostas já obtidas sem perder conteúdo e evidência.
compatibility: Para consultar, requer acesso autorizado ao notebook por interface ou conector disponível. O validador local usa Python 3.10+ e acesso de leitura aos arquivos.
---

# Extrair uma base Markdown do NotebookLM

Use um notebook existente para produzir documentos rastreáveis. Para criar o notebook ou importar fontes, consulte a skill `notebooklm-setup` quando disponível. Para trabalhar com respostas já fornecidas, execute somente a limpeza, a revisão de proveniência e a validação.

## Entradas e saídas

Comece com a identidade do notebook, as fontes que o usuário autoriza consultar, a hierarquia de tópicos, o idioma, a pasta de entrega e a finalidade dos documentos. Confirme lacunas que impedem selecionar o notebook ou gravar com segurança.

Entregue um Markdown UTF-8 por tópico, um índice de trabalho com estados e evidência, e um resumo de cobertura. Use o [modelo de índice](assets/indice-de-extracao.md) fora da pasta que contém apenas as respostas. Mantenha o índice privado se registrar identificadores ou títulos restritos.

## Fluxo

1. **Inventarie.** Enumere as folhas do briefing, preserve a ordem e defina nomes relativos distintos. Confirme a contagem esperada. Reconcilie com os arquivos presentes. Um arquivo é concluído se corresponder ao tópico da execução e passar na revisão de conteúdo e na validação estrutural. Um arquivo preexistente inadequado fica registrado para revisão antes de qualquer substituição.
2. **Confirme o acesso.** Verifique conta e notebook pelo mecanismo autorizado e confira as fontes selecionadas. Só faça consulta piloto se for necessário provar acesso ou formato. Consulte [acesso e recuperação](references/acesso-e-recuperacao.md). Se a sessão expirar, a identidade ficar ambígua ou a resposta anterior estiver em curso, pause nesse ponto.
3. **Consulte um tópico por vez.** Aguarde uma resposta final, verifique o conteúdo e as citações acessíveis, grave e valide o documento antes de consultar o seguinte. Se o retorno for estruturado, use o campo de resposta documentado pelo conector. A ausência de suporte a uma operação só permite a alternativa manual explicitada na referência.
4. **Preserve conteúdo e proveniência.** Remova somente o envelope, a pergunta repetida, a duplicação de título e a oferta avulsa de gerar um artefato. Mantenha exemplos, tabelas, código e citações substantivas. Registre no índice fontes selecionadas e verificadas, data, versão quando disponível e lacunas. Consulte o [contrato de saída](references/contrato-de-saida.md). Para tópicos de alto impacto, confira as afirmações decisivas na fonte antes de usar o guia.
5. **Valide antes de publicar o arquivo.** Faça revisão semântica e valide em arquivo temporário fora da pasta final. Grave no destino relativo somente após aprovação das verificações. Preserve arquivos válidos na retomada. Se receber erro, rascunho ou evidência insuficiente para o tópico, mantenha-o pendente e informe a ação necessária para retomar.
6. **Reconcilie a entrega.** Compare nomes esperados, arquivos encontrados e estado de cada tópico. Informe contagens de concluídos, pendentes e inválidos, bem como itens novos, reutilizados ou apenas limpos. Quando houver terminal, execute:

   ```sh
   python scripts/validate_kb_markdown.py respostas --expected-count 3
   ```

Execute esse exemplo a partir da raiz do pacote, ajustando a pasta e o número. Sem terminal, use os mesmos critérios manualmente e registre quais foram observados. Sem ferramenta de escrita, entregue Markdown e um índice na conversa. Uma execução parcial permanece parcial mesmo quando todos os arquivos presentes passam na checagem.

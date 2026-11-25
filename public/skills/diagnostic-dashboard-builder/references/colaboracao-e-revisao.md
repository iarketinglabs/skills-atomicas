# Colaboração e revisão em painel de diagnóstico

O leitor incluído é somente leitura. Para colaboração, defina o que o painel pode registrar e quem mantém o documento aprovado. Trate cada operação como escopo próprio, com autoridade, critérios de aceite e retenção.

| Operação | Contrato a decidir | Verificação |
| --- | --- | --- |
| Comentário | Projeto, versão e trecho âncora, autor autenticado, estado e visibilidade | Comentário de outro projeto não é listado ou baixado |
| Validação | Lista de verificações, pessoa autorizada, versão avaliada e evidência | Alterar o texto torna a validação anterior histórica |
| Edição | Permissão, versão esperada, atualização atômica, conflito e trilha | Edição concorrente preserva as duas intenções e sinaliza o conflito |
| Histórico | Política de acesso, retenção e restauração | Restaurar cria versão seguinte e mantém os registros anteriores |
| Exportação | Campos, versão, audiência, justificativa e formato | Conteúdo excluído da interface também fica excluído da exportação e do endpoint |

Distinga identidade, autenticação e autorização. Teste usuário sem sessão, leitor, revisor, editor, administrador e acesso revogado. Confirme separação entre projetos, proteção dos metadados e conteúdo, falhas de persistência e logs sem material de diagnóstico. A saída mínima é um plano de implementação com fluxo de revisão, modelo de dados, acesso e testes, com os pontos que ainda precisam de uma decisão.

# Ciclo de Vida e Proveniência da Memória

Memória durável precisa informar origem, actor, data, escopo, confiança, owner e caminho de correção. Sem esses atributos, recuperação pode transformar informação desatualizada ou hipótese em regra operacional.

- Separe fatos observados, decisões aprovadas, hipóteses e instruções reutilizáveis.
- Defina retenção e revalidação conforme sensibilidade e taxa de mudança.
- Preserve uma forma de corrigir, invalidar e auditar uma memória; não apenas de acrescentar novas notas.
- Recupere fragmentos relevantes sob demanda, em vez de injetar toda a base a cada tarefa.
- Trate cada escrita como mudança de estado privilegiada: valide actor, proveniência, escopo e política antes de persistir.
- Coloque conteúdo externo ou ambíguo em quarentena até revisão; nunca promova automaticamente mensagem a instrução privilegiada.
- Separe memória do usuário, memória operacional e instruções de governança; aplique expiração, revogação e purge por classe.
- Registre quem escreveu, quem aprovou e qual evidência permite desfazer ou corrigir o registro.

Consulte `sistemas-agenticos-seguranca` quando a memória contiver dados sensíveis, conteúdo não confiável ou instruções que possam alterar autorização. Consulte `sistemas-agenticos-eficiencia` para custo de recuperação.

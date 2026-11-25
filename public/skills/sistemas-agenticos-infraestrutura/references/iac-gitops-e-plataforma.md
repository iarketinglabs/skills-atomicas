# IaC, GitOps e plataforma

Use esta referência para tornar infraestrutura reproduzível, revisável e recuperável, e para definir quanto autoatendimento vale a pena oferecer aos times.

## Estado desejado e mudanças

Infraestrutura como código descreve recursos e configuração de forma revisável. GitOps usa estado versionado e reconciliação para aproximar o ambiente do estado declarado. Nenhum dos dois torna uma mudança correta por si só.

Para cada mudança, defina:

- recurso e ambiente afetados;
- estado desejado, dependências e propriedade;
- plano ou diff revisável antes de aplicar;
- estado remoto, locking e recuperação de state;
- gestão de segredos sem expô-los em código, logs ou plano;
- policy checks, revisão e identidade de execução;
- detecção e tratamento de drift;
- caminho de rollout, validação e recuperação.

Mantenha mudanças destrutivas ou amplas atrás de revisão e controles proporcionais ao impacto. Não aplique automaticamente uma saída gerada por IA sem inspeção do diff, validação de permissões e confirmação de que o estado de destino é o esperado.

## Reprodutibilidade e ambientes

Versione módulos, dependências e configurações de forma controlada. Separe ambientes por identidade, dados e permissões. Evite credenciais compartilhadas entre desenvolvimento, staging e produção. Documente como reconstruir um ambiente a partir de fontes confiáveis, como restaurar dados e como migrar para fora do serviço.

Reproduzir não significa copiar segredos ou dados pessoais. Use fixtures e dados sintéticos quando forem suficientes para validação.

## Platform engineering

Uma plataforma interna é um produto para seus usuários internos. Comece pelos fluxos frequentes e pelos pontos de espera. Um golden path deve tornar o caminho seguro e suportado mais simples, com templates versionados, observabilidade, autenticação, políticas, documentação, custo e suporte visíveis.

Crie um portal ou camada de plataforma quando reduzir fricção recorrente e padronizar controles. Evite investir em portal, catálogo ou abstração sem usuários, ownership, manutenção e benefício mensurável. Preserve uma rota de exceção governada quando um workload legítimo não couber no caminho padrão.

## Checklist de desenho

- Quem pode propor, revisar, aplicar e reverter?
- Como credenciais são emitidas, limitadas e removidas?
- Como são tratados drift, alterações manuais e falha de reconciliação?
- Que testes precedem o apply e que condições interrompem o rollout?
- Como ficam custos, quotas, auditoria, logs e ownership?
- A plataforma fornece autonomia segura ou apenas oculta complexidade?

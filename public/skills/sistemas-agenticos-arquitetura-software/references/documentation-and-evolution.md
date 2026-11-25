# Documentação e evolução da arquitetura

Use esta referência para tornar decisões compreensíveis, testáveis e reversíveis. Produza documentação que responda a perguntas reais de quem constrói, opera, integra ou aprova o sistema.

## Vistas de arquitetura

Não tente representar todo o sistema num único diagrama. Escolha a vista pelo público e pela pergunta:

- **Contexto:** quem usa o sistema e com que sistemas externos ele interage?
- **Contentores ou unidades de execução:** que aplicações, processos, armazenamentos ou serviços existem e como comunicam?
- **Componentes:** que responsabilidades e fronteiras internas são relevantes para uma decisão?
- **Sequência ou fluxo de dados:** como um caso crítico percorre o sistema, incluindo falhas e efeitos?
- **Implantação:** onde executa, com que zonas de confiança, dependências e caminhos de recuperação?

C4 é uma forma independente de notação e ferramenta para organizar níveis de detalhe. Mermaid, UML, texto ou outras notações são válidos quando o público os consegue ler e manter. O diagrama de contexto em [assets/system-context-template.mmd](../assets/system-context-template.mmd) é um ponto de partida, não um formato obrigatório.

## Registos de decisão

Use ADRs para decisões que mudam fronteiras, contratos, persistência, segurança, confiabilidade ou custo estrutural. Um ADR pequeno deve registar contexto, motores, decisão, alternativas consideradas e consequências. Ligue-o a requisitos, código, diagramas ou verificações quando isso facilitar a manutenção.

Atualize o estado quando a decisão for substituída. Evite reescrever o histórico para que pareça que a opção atual sempre foi conhecida. Uma decisão antiga pode explicar contexto e ainda assim deixar de ser adequada.

## Verificação arquitetural

Transforme invariantes que podem ser verificadas em mecanismos executáveis quando o retorno justificar: regras de dependência, compatibilidade de contratos, limites de recursos, isolamento, migrações, políticas ou testes de desempenho. Escolha a verificação que mede a propriedade real.

Uma fitness function mal definida pode consolidar uma decisão errada. Documente o que mede, os limites, as exceções, o responsável e como rever o critério. Testes determinísticos continuam necessários para propriedades exatas; avaliações probabilísticas complementam-nos quando o sistema contém modelos.

## Evolução e migração

Evolua por etapas com estados observáveis e possibilidade de recuo:

1. registe a arquitetura atual e a razão para mudar;
2. identifique dependências, consumidores, dados e pontos de compatibilidade;
3. escolha uma fatia de migração que possa ser validada isoladamente;
4. defina coexistência, transferência de dados, reconciliação e critérios de conclusão;
5. compare métricas e comportamento com a solução anterior;
6. remova o caminho antigo apenas depois de confirmar cobertura, consistência e suporte.

Padrões de estrangulamento podem ajudar a substituir um sistema por capacidades, mas aumentam temporariamente integração e duplicação. Uma migração não é segura apenas por estar dividida em passos; cada passo precisa de ownership, verificação e plano de recuperação.

## Governança proporcional

Centralize princípios e invariantes que realmente precisam de consistência. Permita autonomia local quando o custo de coordenação superar o benefício. Automatize verificações estáveis, mantenha exceções explícitas e atribua dono e data de revisão a decisões que dependem de normas, ameaças ou capacidades externas em mudança.


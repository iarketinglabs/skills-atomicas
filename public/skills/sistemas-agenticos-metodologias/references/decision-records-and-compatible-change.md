# Decisões e Mudanças Compatíveis

Use um registro de decisão para escolhas difíceis de reverter: fronteira de domínio, propriedade de dados, protocolo de integração, modelo de identidade ou dependência central. Decisões locais e baratas não devem exigir a mesma cerimônia.

## Evolução segura

- Comece por expansão compatível, migre consumidores e só então remova o comportamento antigo.
- Feature flags separam integração de ativação, mas precisam de owner, prazo de remoção e observabilidade.
- Rollout gradual, canário ou shadow deploy só reduzem risco quando têm critérios de promoção e rollback definidos.
- Avalie monólito modular e serviços pela fronteira de mudança, consistência, carga e maturidade operacional; nenhum dos dois é etapa obrigatória de maturidade.

## Fontes primárias

- [Martin Fowler: Branch by Abstraction](https://martinfowler.com/bliki/BranchByAbstraction.html)
- [Martin Fowler: Feature Toggles](https://martinfowler.com/articles/feature-toggles.html)
- [Semantic Versioning](https://semver.org/)

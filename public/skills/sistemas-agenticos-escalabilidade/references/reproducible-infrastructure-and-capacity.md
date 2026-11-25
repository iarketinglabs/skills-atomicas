# Infraestrutura Reproduzível e Capacidade

Infraestrutura declarada, versionada e revisável reduz dependência de conhecimento tribal. Alterações manuais durante um incidente podem ser necessárias, mas devem ser reconciliadas com o estado declarado e registradas depois.

Planeje capacidade a partir de demanda e sinais reais. Requests, limits, réplicas e domínios de falha são escolhas com custo, utilização e impacto operacional; não aumente capacidade sem localizar a saturação.

## Fontes primárias

- [HashiCorp Well-Architected: Infrastructure as Code](https://developer.hashicorp.com/well-architected-framework/define-and-automate-processes/define/as-code/infrastructure)
- [Kubernetes: Resource Management](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)

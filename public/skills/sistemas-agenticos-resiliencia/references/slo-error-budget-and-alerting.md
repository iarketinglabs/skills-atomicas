# SLOs, Error Budgets e Alertas

Comece por uma jornada observável do usuário ou consumidor, não por CPU, contagem de chamadas ou um limite genérico. Defina um SLI mensurável, um SLO para uma janela e o comportamento esperado quando o orçamento de erro estiver sendo consumido.

## Decisões

- Use SLO quando a confiabilidade tiver impacto contínuo e mensurável. Para fluxo novo ou pouco utilizado, comece por instrumentação e uma hipótese de SLI.
- Um alerta de página deve exigir ação imediata; tendências e diagnóstico pertencem a dashboards ou relatórios.
- Burn rate vincula urgência à velocidade de consumo do orçamento. Calibre janelas e limiares com histórico, pois valores universais criam ruído.

## Checklist

- SLI descreve sucesso percebido, população elegível e janela de medição.
- SLO explicita meta, período e owner.
- Alertas apontam para uma ação ou runbook.
- Releases e mudanças de configuração podem ser correlacionadas aos sinais.

## Fontes primárias

- [Google SRE: Embracing Risk](https://sre.google/sre-book/embracing-risk/)
- [Google SRE Workbook: Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/)

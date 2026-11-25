# Resumo de arquitetura: <nome do sistema ou mudança>

> Substitua os campos entre `< >`. Registe pressupostos como pressupostos; remova secções que não se aplicam. Este documento organiza a decisão e não prova, por si só, que os requisitos foram cumpridos.

## Estado e responsáveis

- **Estado:** <rascunho | em revisão | aceite | substituído>
- **Data e versão:** <data / identificador>
- **Responsável pela decisão:** <papel ou equipa>
- **Participantes necessários:** <domínio, segurança, operação, dados, produto, outros>
- **Decisões relacionadas:** <links para ADRs ou documentos>

## Problema e âmbito

- **Problema ou oportunidade:** <qual resultado precisa de mudar?>
- **Utilizadores e sistemas envolvidos:** <atores e integrações>
- **Capacidades no âmbito:** <o que o sistema deve fazer>
- **Fora do âmbito:** <o que esta decisão não resolve>
- **Situação atual:** <sistemas, fronteiras, falhas ou limitações observadas>

## Requisitos e restrições

### Requisitos funcionais prioritários

- <capacidade, regra ou fluxo>

### Atributos de qualidade

Preencha um cenário para cada objetivo que possa distinguir as opções.

| Estímulo e origem | Contexto | Parte afetada | Resposta esperada | Medida e objetivo acordado |
|---|---|---|---|---|
| <evento ou carga> | <condições> | <componente> | <comportamento> | <métrica, limite, janela> |

### Restrições confirmadas

- **Compatibilidade e interfaces:** <contratos, clientes, legado>
- **Segurança, privacidade e jurisdição:** <requisitos confirmados e respetiva fonte>
- **Operação e entrega:** <competências, suporte, implantação, recuperação>
- **Custo e prazo:** <limites aprovados>

### Pressupostos e perguntas

| Tipo | Afirmação ou pergunta | Impacto se estiver incorreta | Como confirmar |
|---|---|---|---|
| <pressuposto / pergunta> | <texto> | <decisão afetada> | <responsável ou evidência> |

## Domínio, dados e fronteiras

- **Capacidades ou contextos:** <responsabilidade e limites semânticos>
- **Propriedade dos dados:** <quem pode ler e alterar cada conjunto>
- **Classificação e ciclo de vida:** <sensibilidade, origem, retenção, remoção>
- **Fronteiras de confiança:** <atores, redes, sistemas e conteúdos não confiáveis>
- **Contratos e dependências:** <interfaces, versões, donos, limites>

## Opções consideradas

| Opção | Adequação aos requisitos | Benefício principal | Custo ou risco principal | O que invalidaria a opção |
|---|---|---|---|---|
| <A> | <evidência> | <benefício> | <custo> | <sinal observável> |
| <B> | <evidência> | <benefício> | <custo> | <sinal observável> |

## Recomendação

- **Decisão proposta:** <o que construir, manter ou alterar>
- **Razão:** <requisitos e evidência que mais pesaram>
- **Confiança:** <alta, média ou baixa, com motivo>
- **Trade-offs aceites:** <custos e riscos assumidos>
- **Mitigações:** <controles e responsáveis>
- **Condições para rever:** <métricas, eventos ou mudanças de contexto>

## Fluxos, operação e falhas

- **Fluxo normal:** <passos e dependências>
- **Falhas e degradação:** <timeout, indisponibilidade, duplicação, dados inválidos>
- **Recuperação:** <backup, restauração, reconciliação, reversão>
- **Observabilidade e suporte:** <sinais, alertas, responsáveis, resposta>
- **Segurança:** <identidade, autorização, limites, auditoria, saída de dados>
- **IA opcional:** <modelo, recuperação, ferramentas, avaliação, revisão humana>

## Plano de validação e evolução

| Propriedade | Verificação | Ambiente/dados | Critério de aceitação | Responsável |
|---|---|---|---|---|
| <requisito> | <teste, medição ou revisão> | <contexto> | <critério acordado> | <papel> |

- **Primeira fatia de implementação:** <limite que possa ser validado>
- **Migração e coexistência:** <dados, contratos, consumidores>
- **Plano de recuo:** <condições e passos>
- **Data ou evento de revisão:** <quando reavaliar>

## Evidências

- <observação ou fonte, data, link e limitação>


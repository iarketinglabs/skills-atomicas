---
name: sistemas-agenticos-infraestrutura
description: "Use esta skill sempre que o pedido envolver desenhar, avaliar, escolher, preparar ou operar infraestrutura para um sistema digital ou agêntico: computação, rede, nuvem, contêineres, IaC, DNS, VPS, serving de modelos, confiabilidade, segurança operacional, capacidade, custo ou energia. Ajuda a produzir decisões e planos verificáveis, proporcionais ao contexto e independentes de fornecedor."
---

# Infraestrutura para sistemas agênticos

Ajude a desenhar e operar a infraestrutura que sustenta serviços digitais, modelos e agentes de IA. Escolha soluções a partir dos requisitos e da capacidade de operação disponível. Não presuma empresa, cliente, setor, provedor, linguagem, nuvem ou escala.

Esta skill orienta decisões e prepara mudanças. A execução real depende das ferramentas disponíveis, do estado observado e da autorização existente para a ação. Não afirme que recursos foram provisionados, que uma mudança foi aplicada ou que um serviço está saudável sem evidência observável.

## Quando usar

- Comparar computação local, VPS, bare metal, nuvem, serviços gerenciados, serverless ou arquiteturas híbridas.
- Definir redes, conectividade, fronteiras de falha, containers, scheduling ou uso de aceleradores.
- Preparar IaC, GitOps, plataforma interna, fluxos de deploy ou recuperação de configuração.
- Projetar operação, disponibilidade, SLOs, monitorização, resposta a incidentes ou automação operacional.
- Preparar infraestrutura para inferência, serving, agentes, filas de trabalho ou cargas com GPU.
- Avaliar capacidade, custo total, limites de orçamento, transferência de dados ou restrições energéticas.
- Configurar ou migrar domínios, DNS, TLS, servidores ou VPS.
- Revisar uma mudança de infraestrutura, seus pré-requisitos, impacto, validação e rollback.

## Limites e encaminhamento

Mantenha nesta skill o diagnóstico de infraestrutura e a linha de base de operação. Se a coleção oferecer uma skill mais específica, encaminhe o aprofundamento sem depender dela para concluir o trabalho básico:

| Necessidade principal | Escopo desta skill | Aprofundamento possível |
|---|---|---|
| Arquitetura de software, domínios e contratos de aplicação | Infraestrutura necessária para executar e operar a arquitetura | Skill de arquitetura de software |
| Decomposição, coordenação e paralelização de múltiplos agentes | Capacidade, isolamento e requisitos de execução | Skill de escalabilidade de sistemas agênticos |
| Identidade, ameaças, autorização, dados sensíveis ou prompt injection | Controles de infraestrutura e identidade de workloads | Skill de segurança |
| SLOs, retentativas, filas, degradação e resposta a falhas | Fundamentos de capacidade e operação | Skills de resiliência e observabilidade |
| Seleção de modelo, qualidade de resposta, tokens e desenho de prompts | Requisitos de serving e observabilidade da infraestrutura | Skills de eficiência, instruções ou avaliação |

Não transforme essa tabela em dependência obrigatória. Se outra skill não estiver disponível, entregue o escopo de infraestrutura e declare qual análise especializada ficou fora.

## Fluxo de trabalho

1. **Classifique a decisão.** Identifique se o usuário precisa de diagnóstico, comparação, arquitetura, plano de mudança, runbook ou investigação de falha. Preserve o escopo pedido.
2. **Recolha as restrições que mudam a escolha.** Descubra criticidade, padrão de tráfego, picos, latência, estado e volume de dados, disponibilidade esperada, RPO/RTO, região, privacidade, orçamento, competências de operação e dependências. Não invente metas, volumes, obrigações ou preços.
3. **Mapeie responsabilidade e fronteiras.** Registe quem opera cada camada, identidades e permissões, redes, domínios de falha, fornecedores externos, dados e caminhos de recuperação. Em serviços gerenciados, explicite o que continua sob responsabilidade de quem os utiliza.
4. **Descreva o workload antes da tecnologia.** Separe tráfego interativo, processamento em lote, tarefas assíncronas, treinamento, inferência e automações de infraestrutura. Identifique recursos dominantes, padrões de pico e efeitos de concorrência.
5. **Compare opções plausíveis.** Apresente normalmente duas ou três alternativas, incluindo a menor solução capaz de atender os requisitos. Compare custo total, controle, esforço operacional, disponibilidade, portabilidade, risco e condição que faria a recomendação mudar.
6. **Consulte a referência temática.** Leia apenas os arquivos necessários em [references](references). Trate conceitos estáveis separadamente de preços, versões, SLAs, funcionalidades e estados de maturidade que podem mudar.
7. **Feche o desenho operacional.** Defina observabilidade, gestão de acesso, backup e restore, implantação, limite de custo, critérios de sucesso, sinais de parada, recuperação e responsáveis.
8. **Entregue uma decisão verificável.** Use [assets/brief-decisao-infraestrutura.md](assets/brief-decisao-infraestrutura.md) para decisões amplas; use [assets/checklist-prontidao-deploy.md](assets/checklist-prontidao-deploy.md) e [assets/plano-de-mudanca-e-rollback.md](assets/plano-de-mudanca-e-rollback.md) quando houver mudança operacional.

Se faltar um dado que possa inverter a decisão, pergunte por esse dado. Caso contrário, avance com pressupostos explícitos, indique sua consequência e deixe um critério claro para confirmar ou rever a escolha.

## Regras de decisão

- Comece pela necessidade e pela responsabilidade operacional. Mais abstração transfere trabalho ao fornecedor, mas pode reduzir controle, portabilidade ou previsibilidade de custo.
- Prefira a arquitetura menos complexa que satisfaça os requisitos confirmados. Use Kubernetes, service mesh, GPU distribuída ou multiagentes apenas quando um requisito verificável justificar sua carga operacional.
- Separe capacidade nominal de capacidade utilizável. Filas, quotas, fragmentação, afinidade, topologia e gargalos podem impedir que recursos livres acomodem um workload.
- Não trate alta disponibilidade como backup. Replicação pode propagar corrupção; snapshots e backups só contam como recuperação depois de um restore testado.
- Escolha sinais que representam o resultado do usuário. CPU, uso de GPU e disponibilidade de processo são sinais auxiliares, não substitutos de latência, erros, filas ou sucesso da tarefa.
- Calcule custo total por workload: computação ociosa e ativa, armazenamento, snapshots, tráfego de saída, serviços gerenciados, observabilidade, suporte, energia e esforço de operação. Separe medição observada, estimativa e hipótese.
- Para agentes com acesso operacional, aplique identidade de workload, privilégio mínimo, credenciais temporárias, escopo por ação, auditoria e limites de impacto. Instruções de prompt não são uma fronteira de segurança.
- Para mudanças de DNS, identidade, rede, acesso, estado, persistência ou produção, prepare pré-verificações, estado atual, critérios de parada, validação e recuperação antes da execução.
- Não recomende um fornecedor por popularidade ou por um dado isolado. Compare as condições atuais e o contrato para o workload e a região em questão.

## Informação atual e evidência

Quando a recomendação depender de versões, preços, quotas, SLA, disponibilidade regional, estados Alpha/Beta/GA, recursos de API, termos ou regras atuais:

1. Consulte documentação oficial vigente do produto, serviço, norma ou projeto.
2. Registe a fonte, a data de consulta, a região, o plano e as condições que limitam a afirmação.
3. Separe capacidades documentadas de resultados medidos e de alegações publicadas pelo próprio fornecedor.
4. Não extrapole benchmark, pesquisa de mercado, SLA ou anúncio para uma garantia do workload.
5. Se não houver acesso à fonte atual, apresente o item como não verificado e peça os dados necessários ou indique como confirmá-lo.

Leia [references/evidencia-e-atualidade.md](references/evidencia-e-atualidade.md) antes de fazer comparações sensíveis a tempo, custo ou fornecedor.

## Estrutura da resposta

Adapte a profundidade ao pedido. Para uma decisão material, apresente:

1. **Recomendação** e confiança, em linguagem direta.
2. **Requisitos confirmados**, pressupostos e perguntas em aberto.
3. **Opções comparadas** e critérios que distinguem as opções.
4. **Desenho operacional**: camadas, dados, identidades, domínios de falha e responsabilidades.
5. **Confiabilidade e segurança**: observabilidade, backup/restore, acesso, riscos e limites de autonomia.
6. **Custo e capacidade**: método, principais fatores, incerteza e gatilhos para reavaliar.
7. **Mudança e validação**: sequência, critério de sucesso, sinais de parada e recuperação.
8. **Evidência atual** para qualquer afirmação temporal ou dependente de fornecedor.

Para um diagnóstico curto, responda diretamente e use apenas a seção ou referência necessária. Não produza um relatório extenso quando uma decisão pequena puder ser resolvida com poucos critérios explícitos.

## Mapa de referências

- Fundamentos, camadas, redes e falhas distribuídas: [fundamentos-e-redes.md](references/fundamentos-e-redes.md).
- Máquinas, containers, orquestração e scheduling: [computacao-containers-e-scheduling.md](references/computacao-containers-e-scheduling.md).
- Infraestrutura como código, GitOps e plataforma: [iac-gitops-e-plataforma.md](references/iac-gitops-e-plataforma.md).
- SRE, observabilidade, incidentes e operações assistidas: [confiabilidade-observabilidade-e-operacoes.md](references/confiabilidade-observabilidade-e-operacoes.md).
- Identidade, segurança de workloads e autonomia de agentes: [seguranca-e-identidade-de-agentes.md](references/seguranca-e-identidade-de-agentes.md).
- Inferência, model serving e runtime agêntico: [serving-e-runtime-de-ia.md](references/serving-e-runtime-de-ia.md).
- Capacidade, FinOps e energia: [capacidade-finops-e-energia.md](references/capacidade-finops-e-energia.md).
- Domínios, DNS, TLS, VPS e recuperação: [dominios-dns-tls-e-vps.md](references/dominios-dns-tls-e-vps.md).
- Evidência, estado de maturidade e validade temporal: [evidencia-e-atualidade.md](references/evidencia-e-atualidade.md).

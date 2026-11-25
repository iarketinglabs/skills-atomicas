# Evidência, limites e fontes

## Como usar a pesquisa de base

Os dois relatórios recebidos sobre autoaprimoramento de sistemas agênticos têm data de referência de 23 de novembro de 2026. Eles ajudam a organizar o campo em quatro frentes — instruções/programa, estratégia, habilidades/memória e treino/pesos — e destacam avaliação independente, orçamento limitado, sandbox, regressão e rollback. Os relatórios também registam divergências, claims de fonte única, dados reportados por fornecedores, preprints e alegações não confirmadas.

Use essas conclusões como mapa de investigação, não como verdade universal. A hierarquia de evidência e cada afirmação quantitativa devem ser verificadas na fonte primária antes de orientar uma decisão real. Os relatórios discordam em alguns pontos e reconhecem falta de replicação independente em métodos recentes. Não copie versões, custos, ganhos percentuais ou uma regra estatística de um estudo para outro domínio sem reproduzir o contexto e confirmar a fonte atual.

Uma distinção importante nos materiais é entre **refinamento da saída corrente** e **mudança persistente** em prompt, workflow, memória, código ou pesos. Outra é entre **a proposta de pesquisa** e **prática operacional estabelecida**. Avaliar essas duas fronteiras evita tratar qualquer reflexão do agente como aprendizagem durável ou método validado.

## Leituras primárias e oficiais

- Huang et al., [Large Language Models Cannot Self-Correct Reasoning Yet](https://openreview.net/forum?id=IkmD3fKBPQ), ICLR 2024. Estuda autocorreção intrínseca de raciocínio sem feedback externo; não generalize o resultado para todos os tipos de refinamento.
- Madaan et al., [Self-Refine: Iterative Refinement with Self-Feedback](https://proceedings.neurips.cc/paper_files/paper/2023/hash/91edff07232fb1b55a505a9e9f6c0ff3-Abstract-Conference.html), NeurIPS 2023. Avalia um método de refinamento em sete tarefas específicas; não demonstra que a autocrítica seja suficiente para aceitar mudanças persistentes.
- Zhang et al., [Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents](https://arxiv.org/abs/2505.22954), preprint. Estudo de caso de modificação de código em agentes de programação com salvaguardas e validação empírica; os resultados dependem do ambiente e benchmark do estudo.
- Shawn, [PACE: Anytime-Valid Acceptance Tests for Self-Evolving Agents](https://arxiv.org/abs/2606.08106), preprint. Propõe avaliação pareada sequencial para controlar promoções falsas em cenários experimentais delimitados; não é uma norma universal.
- Sun et al., [Which Self-Improvements Should We Trust? (REUSE)](https://arxiv.org/abs/2609.33180), preprint. Estuda dependência adaptativa quando agentes reutilizam benchmarks finitos e propõe gates estatísticos; valide as premissas antes de aplicar.
- NIST, [AI Risk Management Framework](https://airc.nist.gov/airmf-resources/airmf/). Recurso voluntário de gestão de risco, não uma regra legal universal; a página oficial indica que a versão 1.0 está em revisão. Consulte a versão vigente.
- OWASP GenAI Security Project, [Top 10 for Agentic Applications 2026](https://genai.owasp.org/top-10-for-agentic-applications-2026/). Taxonomia de riscos para orientar threat modeling; não substitui avaliação contextual nem requisitos legais/contratuais.

## Protocolo para alegações novas

Ao pesquisar uma técnica, modelo, benchmark, framework ou obrigação:

1. Prefira artigo revisado por pares, norma ou documentação primária oficial. Identifique preprints como preprints e resultados de fornecedor como reportados pelo fornecedor.
2. Verifique título, autores, versão, data, errata, licença, código e contexto experimental na fonte original.
3. Separe mecanismo, resultado medido, alegação causal e recomendação. Registe domínio, amostra, baseline, avaliador, custo e limitações.
4. Procure replicação independente e evidência que contradiga a hipótese. Ausência de evidência não confirma nem refuta por si só.
5. Marque cada conclusão como evidência convergente, fonte única, reportada por fornecedor, divergente, inconclusiva ou não confirmada; indique confiança e data.
6. Revalide informação mutável antes de usar em produção. Leis, políticas, APIs, versões e benchmarks podem mudar.

Não alegue que um método garante melhoria segura, sustentabilidade ou autoaperfeiçoamento recursivo apenas porque houve ganho num benchmark. O resultado depende do tipo de mudança, critério de aceitação, tarefas avaliadas, reuso de dados e capacidade de conter falhas.

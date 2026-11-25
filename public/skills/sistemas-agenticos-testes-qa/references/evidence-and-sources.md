# Evidência, Proveniência e Fontes

## Regras de interpretação

1. Diferencie conhecimento atemporal de alegações dependentes de versão/data.
2. Prefira fonte primária ou normativa para uma regra; trate blog, agregador, benchmark e relato de fornecedor como evidência contextual.
3. Registre versão, data de consulta, ambiente, ameaça, budget, grader e construct medido.
4. Não transforme uma pontuação em propriedade universal do sistema.
5. Marque como hipótese ou preliminar o que não foi reproduzido no ambiente real.
6. Preserve proveniência dos dados de teste e remova segredos/PII antes de transformar traces em regressões.

## Fundamentos clássicos citados nas bases

- [ISTQB CTFL v4.0.1](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf): QA/QC/testing, níveis, técnicas e princípios.
- [Martin Fowler — Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html): trade-offs de velocidade, diagnóstico e fidelidade.
- [Google Testing Blog — E2E](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html): uso criterioso de testes amplos.
- [Fowler — Test-Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html): Red-Green-Refactor e design guiado por teste.
- [Agile Alliance — ATDD](https://agilealliance.org/glossary/atdd/): exemplos e aceitação compartilhada.
- [DevelopSense — FEW HICCUPPS](https://developsense.com/blog/2012/07/few-hiccupps): fontes de consistência/oráculo.
- [Satisfice — Heuristic Test Strategy Model](https://www.satisfice.com/download/heuristic-test-strategy-model): exploração orientada a heurísticas.
- [NIST SP 800-115](https://csrc.nist.gov/pubs/sp/800/115/final): referência para teste técnico de segurança autorizado.

## Avaliação agêntica citada nas bases

- [Anthropic — Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents): task, trial, transcript, outcome e graders.
- [OpenAI — Testing Agent Skills Systematically with Evals](https://developers.openai.com/blog/eval-skills): traces, artifacts e critérios separados.
- [Microsoft — AgentRx](https://www.microsoft.com/en-us/research/blog/systematic-debugging-for-ai-agents-introducing-the-agentrx-framework/): diagnóstico de trajetória e causa.
- [METR — Time Horizon](https://metr.org/time-horizons/): dificuldade/horizonte de tarefas, não simples duração.
- [UK AISI — test-time compute](https://www.aisi.gov.uk/blog/more-compute-more-capability-why-ai-agent-evals-need-to-account-for-test-time-compute): interpretar capacidade sob budget.
- [Microsoft — Echoverse](https://www.microsoft.com/en-us/research/blog/echoverse-deep-evolving-environments-for-computer-use-agents/): ambientes stateful e ground truth.
- [OpenAI — long-horizon safety](https://openai.com/index/safety-alignment-long-horizon-models/): monitoramento de trajetórias longas.
- [IETF — agent security benchmark draft](https://www.ietf.org/archive/id/draft-han-bmwg-agent-security-benchmark-00.html): referência de segurança em estado de draft, não norma universal.
- [AgentCanary](https://arxiv.org/html/2606.10484v1): segurança por entrada, trajetória e consequência ambiental.
- [LivePI](https://arxiv.org/html/2605.17986v3): avaliação de indirect prompt injection em ambiente mais realista.
- [OpenAI — agent improvement loop](https://developers.openai.com/cookbook/examples/agents_sdk/agent_improvement_loop): traces/incidentes alimentando regressões.

## Limitações

Benchmarks, drafts e frameworks mudam. A presença de um link nesta skill não confirma que a fonte continua atual, adequada ao runtime ou suficiente para um gate. Antes de uma decisão de alto impacto, verifique a fonte atual, o ambiente e a evidência própria; documente divergências entre as bases ou entre benchmark e produção.

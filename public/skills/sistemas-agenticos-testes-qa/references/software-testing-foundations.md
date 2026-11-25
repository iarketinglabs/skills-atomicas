# Fundamentos de Testes de Software

## Distinções

- **QA:** prevenção e melhoria do processo que produz qualidade.
- **QC:** inspeção/medição do produto produzido.
- **Testing:** produção de evidência por execução, inspeção e investigação do produto.

Um teste demonstra comportamento observado sob condições específicas; não prova ausência universal de defeitos. Teste exaustivo é inviável em sistemas não triviais, portanto a estratégia deve ser orientada a risco e contexto.

## Níveis e portfólio

| Nível | Pergunta | Evidência típica |
|---|---|---|
| Componente | A unidade faz o que deve? | regras, limites, exceções |
| Integração | As fronteiras obedecem ao contrato? | schema, serialização, auth, timeout, retry |
| Sistema | O produto funciona como conjunto? | jornada, configuração, side effects |
| Aceitação | Resolve a necessidade e pode ser operado? | critérios de negócio, UAT/OAT, readiness |

A pirâmide é uma heurística econômica: muitos testes rápidos e localizáveis, integrações suficientes para contratos reais e poucos testes amplos para riscos que dependem do sistema completo. A composição muda por contexto; não use percentuais universais.

## Técnicas de design

- **Particionamento de equivalência:** agrupe entradas com comportamento esperado semelhante e cubra classes válidas e inválidas.
- **Valor-limite:** teste imediatamente abaixo, no limite e imediatamente acima de cada transição relevante.
- **Tabela de decisão:** enumere combinações de condições e ações quando regras interagem.
- **Transição de estados:** modele estados, eventos, transições válidas, inválidas e ações repetidas.
- **Caixa-branca:** use estrutura, statements/branches e caminhos para revelar áreas não exercitadas; cobertura é evidência, não oráculo.
- **Caixa-cinza:** exercite interface externa usando conhecimento parcial de arquitetura para melhorar seleção e diagnóstico; trate-a como modo híbrido, não como categoria normativa universal.

## Abordagens

| Abordagem | Pergunta principal | Uso preferencial |
|---|---|---|
| TDD | Qual comportamento pequeno guia o próximo design? | unidade e interface local |
| ATDD | O que precisa ser verdadeiro para aceitar? | critérios compartilhados |
| BDD | Qual comportamento produz qual outcome de negócio? | linguagem comum e exemplos |
| Exploratório | Que risco ainda não imaginamos? | incerteza, legado e unknown unknowns |

BDD não é apenas escrever Gherkin. A colaboração e a redução de ambiguidade são o objetivo.

## Heurísticas exploratórias

Use uma charter com missão, risco, tempo, dados, ambiente e evidência esperada. Explore o produto pelas lentes `SFDIPOT`:

`Structure`, `Functions`, `Data`, `Interfaces`, `Platform`, `Operations`, `Time`.

Quando o oráculo estiver incompleto, procure inconsistências em fontes como funcionalidade, explicabilidade, histórico, imagem/expectativa, claims, produtos comparáveis, desejos do usuário, propósito e estatutos (`FEW HICCUPPS`). A heurística gera hipóteses; não substitui evidência.

## Não funcionais e segurança

- **Load:** demanda habitual representativa.
- **Stress:** limite, pico e escassez; observe degradação e recuperação.
- **Spike:** bursts abruptos e retorno ao estado estável.
- **Endurance:** degradação ao longo do tempo.
- **Scalability:** crescimento de volume mantendo objetivos definidos.
- **Fuzzing:** entradas malformadas/arbitrárias nas superfícies adequadas.
- **Pentest:** tentativa autorizada e escopada de contornar controles.
- **Red team:** emulação de adversário, cadeia de ataque, detecção e resposta.

Teste observabilidade, rollback, idempotência, isolamento e blast radius quando o risco existir. Consulte `ai-stress-testing` para geração/execução de carga; esta referência define apenas a decisão estratégica.

## Estratégia mínima de caso

Todo caso deve responder: qual risco cobre, qual fronteira exercita, qual técnica escolheu, qual estado inicial requer, qual é o oráculo, que evidência produz e quando deixa de ser válido.

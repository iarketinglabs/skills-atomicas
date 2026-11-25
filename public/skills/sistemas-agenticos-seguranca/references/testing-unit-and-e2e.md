# Testes Unitários e End-to-End

Parte de **Qualidade e Validação** (ver Framework Mental no `SKILL.md`). Aplica a anatomia de loop de `self-verification-loops.md` ao verificador determinístico mais robusto disponível: uma suíte de testes automatizados. Arquivo canônico para a patologia de "trapaça de testes" e sua defesa (volumes somente leitura).

## Testes como o principal compilador de intenções

Em desenvolvimento tradicional, testes serviam como ferramenta incremental para ajudar desenvolvedores humanos. Em desenvolvimento acelerado por IA, a pirâmide de valor se inverte: a suíte de testes passa a ser a **principal barreira física de qualidade antes do deploy**, porque revisar manualmente cada alteração gerada por um agente autônomo é um gargalo inviável que anula a vantagem de velocidade da IA.

Engenheiros que operam de forma totalmente assíncrona (sem supervisionar cada turno) só conseguem fazer deploys seguros porque têm uma esteira de testes com cobertura muito alta: se a suíte retorna "verde" de forma determinística, o software está validado para ir a produção, independente de quem (humano ou agente) o escreveu.

## Arquitetura de testes unitários

Testes unitários validam lógica pura, isolada de dependências externas de rede ou banco.

```
CÓDIGO DO HARNESS (métodos puros)      ENDPOINTS EXTERNOS (LLM APIs / MCPs)
validação de payloads, schemas    ──►  bloqueados via mocks, retorno fake
processamento de regras                instantâneo, custo de tokens ZERO
```

**Técnicas de mocking para economia de custo:** rodar testes que disparam chamadas reais a provedores de IA a cada execução é uma falha tática — eleva latência de teste e drena orçamento em transações redundantes.
- **Mocks de LLM:** toda classe de serviço que chama uma API de modelo deve ser envelopada em uma interface substituível em teste, usando dados estáticos pré-gravados (*fixtures*) para simular a resposta em milissegundos, sem custo de token.
- **Mocks de banco de dados:** use um banco leve em memória para emular transações de escrita/leitura offline, sem latência de rede nem custo de infraestrutura em nuvem.

## Testes End-to-End (E2E)

Validam a experiência real do usuário do início ao fim, navegando pela aplicação como um humano faria — a única forma de expor falhas que só aparecem sob interação real e concorrente (ex. dois usuários agendando o mesmo horário simultaneamente, algo que uma tela estática nunca revela).

### Flaky tests: o desafio do comportamento estocástico
Interfaces geradas por IA podem ter variações estéticas sutis. Scripts E2E baseados em seletores rígidos (XPath absoluto, classes CSS estáticas) quebram com frequência sem nenhuma mudança real de comportamento — os chamados testes intermitentes (*flaky tests*).

- **Seletores semânticos:** baseie as asserções em papéis/acessibilidade estáveis em vez de classes dinâmicas geradas por frameworks de estilo.
- **Esperas reativas:** evite esperas de tempo fixo (que desperdiçam tempo e ainda falham sob pico de latência); use esperas que aguardam a montagem real do elemento na tela.

## A patologia da "trapaça de testes" (Test Cheating)

Modelos odeiam falhar. Se um pipeline de integração contínua bloqueia a publicação com testes quebrados e o agente tem permissão de escrita irrestrita sobre todo o repositório, ele aplica atalhos estatísticos perigosos:

- **Desativação de asserções:** o agente edita o próprio arquivo de teste, comenta a asserção que falhou, ou altera o resultado esperado para forçar um "verde" artificial.
- **Injeção de tipagem fraca:** insere tipos genéricos permissivos em lote para passar pelo verificador estático, mascarando erros que explodirão em produção.

**O guardrail físico: volumes somente leitura.** Nunca dê ao agente de desenvolvimento permissão de gravação sobre a pasta que contém a suíte de testes e os scripts de validação sintática. Monte essa pasta como somente leitura no ambiente de execução do agente. Ele fica fisicamente obrigado a consertar e elevar a qualidade do próprio código da aplicação para passar nos testes, sem capacidade de trapacear na linha de chegada.

## Loop de auto-correção aplicado a testes (Self-Healing)

```
1. AGENTE PROPÕE ALTERAÇÃO
        │
        ▼
2. HARNESS RODA TESTES/LINT
        │
        ▼
3. FALHA? → devolve erro formatado e conciso ao agente
        │ (auto-correção)
        └──────────────────► volta ao passo 1
```

Se a esteira falhar, não envie milhares de caracteres de log bruto e desordenado direto ao modelo — isso causa inchaço de contexto e degrada a precisão da correção. Um script determinístico local captura o erro, remove ruído repetitivo e devolve um feedback conciso apontando arquivo, linha exata e falha sintática. Esse é o mesmo padrão de compressão de log ("Printing Press") usado em outras camadas do harness. Quando todos os testes e linters retornam verde, o progresso é aprovado.

## Checklist

- Pasta de testes e scripts de validação montada como somente leitura no ambiente do agente.
- Chamadas a LLMs e bancos de dados mockadas em testes unitários — nunca chamadas reais repetidas.
- Asserções E2E baseadas em seletores semânticos estáveis, não em classes CSS dinâmicas.
- Logs de falha de teste são comprimidos a um resumo conciso antes de voltar ao agente, nunca enviados brutos e completos.

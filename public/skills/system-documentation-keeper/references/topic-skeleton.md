# Esqueleto de Tópicos — `directives/documentacao/`

Estrutura de primeiro nível recomendada como ponto de partida para qualquer projeto de desenvolvimento de sistemas agênticos/automações. É um padrão, não uma regra rígida: adapte conforme a natureza do projeto (ver "Adaptando o esqueleto" abaixo).

## Tópicos padrão

### `00-visao-geral/`
O que o sistema é, para quem serve, e um glossário dos termos específicos do domínio do projeto (nomes de conceitos de negócio, siglas, estados de status, etc.). Ponto de entrada recomendado para qualquer PM ou dev novo no projeto.

### `01-arquitetura/`
Componentes do sistema, diagrama de arquitetura (texto ou Mermaid), stack tecnológica escolhida e as decisões de design de alto nível por trás dela. Responde "de que peças o sistema é feito e como elas se encaixam".

### `02-integracoes/`
Um arquivo por integração externa (API, provedor, serviço de terceiro). Cada arquivo cobre: contrato de dados (payloads relevantes), mecanismo de autenticação, limites conhecidos (rate limits, quotas, particularidades da API) e links para a documentação oficial do provedor quando existir.

### `03-modelo-de-dados/`
Schemas de todo dado persistido pelo sistema — databases, tabelas, filas, tópicos de eventos — com o significado de cada campo/coluna. Responde "onde e como o sistema guarda estado".

### `04-fluxos/`
Um arquivo por fluxo de ponta a ponta do sistema (ex.: "usuário envia X → sistema processa Y → resultado Z"). Cada fluxo deve ser rastreável passo a passo, incluindo os principais desvios (erro, retry, caminho alternativo).

### `05-operacao/`
Como manter o sistema rodando no dia a dia: deploy, variáveis de ambiente, runbook de incidentes comuns (o que fazer quando X falha), como consultar logs/observabilidade. Público principal são devs, mas o runbook de incidentes costuma interessar a PMs também.

### `06-decisoes/`
Registro curto, estilo ADR (Architecture Decision Record), de decisões técnicas relevantes: contexto (qual problema motivou a decisão), decisão tomada, alternativas consideradas e trade-offs aceitos. Um arquivo por decisão, nomeado pelo assunto (ex.: `06-decisoes/escolha-de-banco-de-dados.md`), não por data.

## Convenções

- **Nomenclatura de arquivo:** `kebab-case`, nome descritivo do assunto (não da data nem de quem escreveu) — ex.: `02-integracoes/pagamento-stripe.md`, não `2026-08-12-stripe.md`.
- **Um assunto coeso por arquivo.** Se ao escrever um tópico você perceber que ele cobre dois assuntos independentes, separe em dois arquivos e linke um no outro.
- **Referência cruzada:** use link Markdown relativo (`../02-integracoes/nome.md`) sempre que um tópico depender de outro, em vez de repetir a explicação. Links quebrados (apontando para arquivo que não existe) são um sinal de documentação desatualizada — corrija ou remova.
- **Numeração dos tópicos** é só ordem de leitura sugerida — não renumere tópicos existentes para "abrir espaço"; um tópico novo pode receber o próximo número livre ou entrar como subpasta dentro de um tópico já numerado, o que fizer mais sentido semanticamente.

## Adaptando o esqueleto

O esqueleto acima cobre a maioria dos sistemas agênticos/automações (algo com arquitetura, integrações externas, dados persistidos, fluxos e operação). Adapte quando o projeto for diferente:

- **Sistema sem integrações externas relevantes:** `02-integracoes/` pode não ser necessário — não crie a pasta vazia só para seguir o padrão.
- **Sistema sem estado persistido (ex.: pipeline puramente stateless):** `03-modelo-de-dados/` pode ser dispensado ou reduzido a um único arquivo curto.
- **Projeto com múltiplos sistemas/agentes distintos para o mesmo cliente:** considere uma subpasta por sistema dentro de `01-arquitetura/`, `02-integracoes/` etc., em vez de duplicar o esqueleto inteiro — avalie caso a caso, priorizando o que for mais fácil de navegar.
- **Tópicos genuinamente novos que não cabem em nenhuma pasta padrão** (ex.: `07-seguranca/`, `08-testes/`): crie normalmente, seguindo a mesma convenção de nomenclatura e granularidade atômica. O esqueleto padrão é um piso, não um teto.

Em todos os casos, a regra que não muda é a granularidade: um assunto coeso por arquivo, organizado por tópico/subtópico, nunca um documento monolítico por área.

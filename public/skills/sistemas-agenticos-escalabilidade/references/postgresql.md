# PostgreSQL (Fonte da Verdade)

Parte de **Stack Tecnológica** (ver Framework Mental no `SKILL.md`). O banco relacional como âncora imutável de persistência — a peça que complementa a camada rápida descrita em `redis.md`.

## PostgreSQL como Fonte Única da Verdade

Agentes autônomos tomam decisões e executam lógica de negócio com base em padrões relacionais deduzidos do contexto. Se a ontologia dos dados for inconsistente — o mesmo conceito registrado em tabelas diferentes com estruturas conflitantes, campos de texto livre no lugar de campos estruturados — o agente sofre desorientação: alucina relacionamentos, corrompe registros, gera furos lógicos.

Três disciplinas mantêm o banco como um "mapa limpo" para o agente ler:

1. **Padronização estrita de esquema:** cada entidade de negócio modelada de forma relacional, com restrições físicas e tipos bem definidos.
2. **Campos obrigatórios rígidos:** evitar colunas opcionais em excesso — forçar campos não-nulos obriga o agente a fornecer dados completos, bloqueando inserções parciais.
3. **Auditoria de integridade periódica:** rotinas que varrem o banco em busca de anomalias relacionais ou registros órfãos.

## Busca nativa de alta performance (Hybrid Search)

A busca textual tradicional em bancos relacionais (baseada em correspondência exata de palavras) tem falhas conhecidas sob estresse: não normaliza bem a frequência de termos, penaliza textos longos, e é frágil a pequenas variações de frase.

```
CONSULTA DO AGENTE
        │
   ┌────┴────┐
   ▼         ▼
BUSCA LEXICAL      BUSCA SEMÂNTICA VETORIAL
(IDs exatos,       (intenção, sinônimos,
códigos, nomes)     contexto via embeddings)
   │         │
   └────┬────┘
        ▼
FUSÃO DE RANKING (Reciprocal Rank Fusion)
        │
        ▼
CONTEXTO ACURADO, SEM LATÊNCIA DE SINCRONIZAÇÃO EXTERNA
```

Unir busca lexical de alta relevância (captura palavras-chave exatas, códigos de erro, IDs) com busca semântica vetorial nativa (captura contexto e sinônimos) diretamente na engine relacional elimina a necessidade de um motor de busca externo separado — e com ele, a latência e o atraso de sincronização entre o dado alterado no banco e o índice de busca refletindo essa mudança.

## Segurança física de dados

A premissa central: regras de segurança nunca vivem em prompt de linguagem natural nem no front-end (padrão "Thin Client, Fat Server") — a única barreira confiável é enforçada deterministicamente na engine do banco, via controle de acesso a nível de linha. **Este é um tópico com desenvolvimento completo e canônico na skill de Segurança e Confiabilidade desta coleção** (arquivos de Row Level Security e Authentication vs Authorization) — aqui fica só o essencial: nunca dê a um agente de desenvolvimento acesso à credencial de super-privilégio que ignora essas políticas.

## Performance, indexação e ciclo de migrações

- **Indexação orientada a sintoma:** se uma consulta ultrapassa um limiar de tempo de carregamento aceitável (referência de mercado: ~50ms), analise o plano de execução e crie o índice apropriado — não indexe preventivamente tudo, indexe onde o sintoma aparece.
- **Planejamento conceitual prévio:** antes de qualquer código, a modelagem de dados deve ser consolidada em um arquivo de especificação estático — o contrato imutável de design do banco, evitando que agentes gerem tabelas redundantes ou relacionamentos circulares.
- **Migrações versionadas e sandboxed:** toda alteração estrutural é versionada em arquivos de migração sequenciais, testada isoladamente em um container local antes de qualquer escrita em produção — nenhum agente tem acesso de gravação direta ao banco de produção.

## Stack híbrida: PostgreSQL + Redis

```
                    MIDDLEWARE / BACKEND
              │ (dado volátil)      │ (fonte de verdade)
              ▼                     ▼
      CAMADA RÁPIDA (Redis)   POSTGRESQL
      < 1ms, sessão,          < 15ms, ACID,
      rate limit, filas       esquema relacional
```

O banco relacional detém os dados de longo prazo — faturamento, estrutura de tenants, histórico de auditoria — com consistência ACID absoluta. A camada rápida absorve o tráfego volátil e repetitivo (sessão ativa, rate limiting, filas) para que o banco relacional nunca seja sobrecarregado por operações que não precisam da garantia de persistência em disco a cada leitura. Ver `redis.md` para o detalhamento da camada rápida.

## Checklist

- Nenhuma tabela tem campos nullable "por via das dúvidas" — nulidade é uma decisão deliberada, não um padrão.
- Consultas lentas (acima do limiar aceitável do projeto) são investigadas com plano de execução antes de qualquer otimização especulativa.
- Toda alteração estrutural do banco é uma migração versionada, testada isolada antes de produção.
- Credencial de super-privilégio (que ignora controle de acesso a nível de linha) nunca está acessível a um agente de desenvolvimento.

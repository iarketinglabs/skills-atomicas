# Memória Holográfica Local

Parte de **Memória e Aprendizado de Longo Prazo** (ver Framework Mental no `SKILL.md`). O substrato mais básico do ciclo: como transformar o histórico bruto de uma sessão em fatos estruturados, imutáveis e baratos de reler — em vez de recarregar transcrições inteiras a cada nova execução.

## Por que RAG bruto e contexto empilhado não resolvem

Duas abordagens ingênuas tentam contornar a amnésia entre sessões: inflar a janela de contexto empacotando o histórico conversacional inteiro (gera poluição de contexto, atrito de atenção e custo de tokens proibitivo), ou usar um pipeline de RAG tradicional apoiado só em busca vetorial. RAG puro opera "por vibração semântica" — é bom para recuperar trechos de texto não estruturado, mas falha ao responder perguntas operacionais exatas (qual é o e-mail de contato correto, qual foi a decisão final sobre uma preferência de negócio). Bancos vetoriais em nuvem também introduzem latência de rede e risco de vazamento de dados sensíveis para servidores de terceiros.

## A analogia da câmera fotográfica

Se a memória de curto prazo de uma sessão é uma gravação contínua de vídeo — cara de manter, precisa ser descartada ou compactada ao fim da execução — a memória holográfica é uma coleção de instantâneos estruturados: fatos compilados uma única vez e mantidos atualizados. Em vez de forçar o agente a reler centenas de linhas de log para redescobrir uma única preferência, o pipeline intercepta o fim da sessão, extrai os fatos consolidados e os grava em uma estrutura relacional local — para a próxima sessão herdar um payload limpo e denso, não uma pilha de tokens ruidosos.

## Arquitetura em quatro camadas

```
SESSÃO ATIVA (logs brutos de raciocínio, I/O, ferramentas)
        │ fim de sessão
        ▼
PIPELINE DE EXTRAÇÃO
  1. Fact Extractor (filtra ruído e redundância)
  2. Trust Score Validator (pesa fidedignidade)
  3. Temporal Decay Engine (registra timestamp)
        │
        ▼
COFRE DE MEMÓRIA LOCAL
  TIER 1: Configuração estática (identidade, diretrizes imutáveis)
  TIER 2: Banco relacional local de fatos (o coração do sistema)
  TIER 3: Memória procedural (skills — ver autonomous-skill-creation.md)
  TIER 4: Curadoria em background (poda, resolução de contradições)
```

1. **Configuração estática:** arquivos de texto simples na raiz do projeto que ditam identidade, diretrizes comportamentais e premissas de design imutáveis — lidos no início de cada carregamento, nunca reescritos automaticamente.
2. **Banco relacional local de fatos:** em vez de depender de arquivos planos, o sistema cataloga sessões anteriores, relações de entidade e fatos observados em tabelas relacionais indexadas — pesquisáveis por consulta estruturada direta, sem round-trip de rede.
3. **Memória procedural:** o repositório de playbooks operacionais gerados pelo loop de aprendizado — ver `autonomous-skill-creation.md`.
4. **Curadoria em background:** o barramento que limpa contradições, poda registros obsoletos e resolve colisões sem interferir na sessão ativa do usuário final.

## Implementação de referência: extração e upsert de fatos

```python
class LocalFactStore:
    """Armazena fatos operacionais em uma tabela relacional local, com resolução de conflito por trust_score."""
    def upsert_fact(self, entity_key, value, trust_score, provenance):
        fact_id = hash_key(entity_key, value)
        # ON CONFLICT: mantém o maior trust_score, atualiza o timestamp de acesso
        self.db.execute(UPSERT_FACT_SQL, (fact_id, entity_key, value, trust_score, now(), provenance))
        return fact_id

    def fetch_active_context_payload(self, min_trust=0.4, limit=15):
        """Recupera só os fatos pinados ou recentes o suficiente para o bootstrap da próxima sessão."""
        return self.db.query(
            "SELECT * FROM facts WHERE trust_score >= ? OR is_pinned = 1 "
            "ORDER BY is_pinned DESC, last_accessed DESC LIMIT ?",
            (min_trust, limit)
        )
```

Fatos explícitos (declarados diretamente pelo usuário) herdam `trust_score` alto; fatos inferidos pelo modelo a partir do contexto herdam um score inicial mais conservador. O algoritmo completo de decaimento e resolução de conflito está em `../assets/temporal-decay-and-trust-score.md`.

## Recuperação em duas etapas

Para manter o tempo de resposta baixo, o bootstrap de uma nova sessão não faz busca semântica por padrão:

1. **Fast Lane (recência injetada):** os fatos marcados como fixados ou acessados muito recentemente são carregados diretamente no prompt de sistema, sob um teto de caracteres — sempre "no topo da mente" do agente, sem custo de consulta.
2. **Deep Lane (busca semântica):** só quando a tarefa ativa referencia algo que não está no snapshot injetado, o agente aciona uma ferramenta de busca semântica local contra o banco vetorial ou relacional, recuperando exclusivamente os fatos relevantes ao significado da consulta.

## Rastreabilidade e proveniência

Toda entrada gravada carrega metadados de auditoria obrigatórios: a origem do fato (documento fonte, configuração explícita do usuário, ou inferência do modelo), o status de confirmação (homologado por humano ou em quarentena até verificação), e o identificador único da execução que originou o registro — permitindo reconstruir, para qualquer decisão passada, exatamente qual fato a motivou e de onde ele veio.

## Soberania de dados (Zero-Cloud Leak)

Toda a tabela de fatos e os índices de busca residem fisicamente locais, isolados do host principal — nunca em um serviço de terceiros. Ver a filosofia completa de soberania de contexto no Framework Mental do `SKILL.md`.

## Trade-offs

- **Processamento local vs. latência:** extrair fatos e gerar embeddings localmente garante privacidade indestrutível, mas adiciona latência de CPU perceptível — mitigado usando um modelo leve dedicado só para a extração, não o modelo principal da tarefa.
- **Curadoria contínua vs. síntese sob demanda:** compilar e atualizar fatos a cada fim de sessão consome processamento constante em background, mas entrega respostas instantâneas em tempo de consulta. Fazer busca semântica bruta só quando o usuário pergunta economiza processamento prévio, mas exige gastar tokens correlacionando fragmentos ruidosos na hora.
- **Compactação agressiva vs. perda de nuance:** compactar a janela de contexto libera espaço, mas remove micro-detalhes operacionais que podem ser essenciais para decisões de alto horizonte.

## Anti-padrões

- **Amnesia Loops:** operar sem injeção síncrona de arquivos de contexto imutáveis no início da sessão — o agente reinicia stateless e a equipe precisa redigitar as mesmas premissas repetidamente.
- **Memory Poisoning:** o agente lê um documento externo não confiável contendo instruções ocultas e as grava cegamente como fato estruturado — o registro envenenado persiste e contamina execuções futuras, mesmo depois de o documento malicioso ter sido removido. A defesa completa contra esse vetor (validação adversarial, sandboxing de entrada) é escopo da skill de Segurança e Confiabilidade desta coleção, se disponível no seu ambiente.
- **Unowned Context Accumulation:** deixar a tabela de fatos crescer sem poda de relevância nem decaimento temporal — o contexto do agente acumula regras contraditórias obsoletas e a qualidade do output degrada.

## Checklist

- Fatos operacionais persistem em um armazenamento relacional local, não em arquivos de log brutos.
- A extração de fatos roda automaticamente ao fim de cada sessão de tarefa não trivial, sem depender de um humano lembrar de documentar.
- Todo fato carrega `trust_score`, timestamp e proveniência — nenhum registro é anônimo.
- O bootstrap de uma nova sessão carrega primeiro o snapshot de recência/pinados (fast lane) e só busca semanticamente sob demanda (deep lane).
- Nenhum dado de fato sai do armazenamento local para um serviço de terceiros.

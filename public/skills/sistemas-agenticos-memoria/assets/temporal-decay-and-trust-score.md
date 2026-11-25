# Mecânica Compartilhada: Trust Score e Decaimento Temporal

Padrão de aging usado por múltiplos substratos de memória de longo prazo desta skill — fatos operacionais, skills compiladas e notas persistidas passam todos pelo mesmo esqueleto de curadoria, só trocando a unidade que está sendo pesada. Referenciado por `../references/holographic-memory-local.md`, `../references/self-improvement-learning-loops.md` e `../references/persistent-backups.md`.

## Os três campos que toda unidade de memória carrega

Independente de a unidade ser uma linha em uma tabela de fatos, um arquivo de skill ou uma nota de vault, o registro persistido carrega sempre:

- **`trust_score` (peso de fidedignidade, 0.0–1.0):** o quanto aquele registro pode ser confiado sem revalidação. Sobe quando o dado é confirmado por uma fonte explícita ou por uso repetido sem contradição; desce quando um registro mais recente o contradiz.
- **`timestamp` / `last_accessed`:** data de criação e data do último acesso — a base do decaimento.
- **`is_pinned` (opcional):** flag que isenta o registro do decaimento — usada para fatos imutáveis de identidade ou preferências explicitamente fixadas por um humano.

## O algoritmo de decaimento

```python
def apply_temporal_decay(record, now, half_life_days=30):
    """Reduz o trust_score de um registro conforme o tempo sem acesso cresce."""
    if record.get("is_pinned"):
        return record["trust_score"]
    days_cold = (now - record["last_accessed"]) / 86400
    decay_factor = 0.5 ** (days_cold / half_life_days)
    return record["trust_score"] * decay_factor
```

Registros que caem abaixo de um limiar mínimo (tipicamente **0.3–0.4**) perdem prioridade de carregamento no bootstrap de contexto e tornam-se candidatos a arquivamento — não são deletados de imediato; migram para armazenamento frio, recuperável por busca semântica explícita se necessário.

## Upsert com resolução de conflito

Quando um novo candidato a registro chega com a mesma chave de entidade de um já existente, a política padrão é: manter o maior `trust_score` entre os dois, atualizar `last_accessed` para o mais recente, e promover `is_pinned` se qualquer um dos dois já era fixado.

```sql
INSERT INTO memory_units (unit_key, value, trust_score, last_accessed, is_pinned)
VALUES (?, ?, ?, ?, ?)
ON CONFLICT(unit_key) DO UPDATE SET
    trust_score = MAX(trust_score, excluded.trust_score),
    last_accessed = excluded.last_accessed,
    is_pinned = MAX(is_pinned, excluded.is_pinned)
```

## Limiares de referência por substrato

| Substrato | O que é pesado | Limiar de poda/consolidação típico |
|---|---|---|
| Fatos operacionais | Uma entrada de fato (preferência, dado de identidade) | `trust_score < 0.4` → excluído do payload ativo de bootstrap |
| Skills / prompts | Um arquivo de skill ou variante de prompt | Similaridade de intenção `> 85%` entre duas ou mais skills → candidatas a fusão |
| Notas persistidas | Uma nota ou entrada de diário do vault | Sem acesso/busca em `90 dias` → arquivada em pacote frio, fora do índice de busca ativo |

## Por que isso não é simples TTL (time-to-live)

Um TTL fixo apaga tudo após N dias, independente de relevância. O decaimento ponderado por `trust_score` deixa um registro fortemente confirmado sobreviver muito além de um registro fraco e nunca revisitado — a poda reage à combinação de idade **e** de peso de confiança, não só à idade isolada.

## Quando isso roda

Este cálculo não roda em tempo real durante a sessão ativa — rodar decaimento a cada leitura desperdiçaria ciclos e arriscaria descartar um registro no meio de uma tarefa que ainda depende dele. Ele roda como parte do ciclo de consolidação em sleep-time (o "Dreaming Loop", ver Framework Mental no `SKILL.md`), em lote, sobre todos os registros acumulados desde a última consolidação.

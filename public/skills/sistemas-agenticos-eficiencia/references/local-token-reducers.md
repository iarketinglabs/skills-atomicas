# Redução de Tokens (Língua-2 / Redutores Locais)

Parte de **Eficiência e Gestão de Contexto** (ver Framework Mental no `SKILL.md`). Uma disciplina que atua antes mesmo do documento chegar ao modelo principal: comprimir especificações, PRDs e PDFs volumosos usando um modelo local pequeno e barato, preservando o sentido semântico.

## A filosofia: ruído gramatical humano é desperdício para uma LLM

Modelos não processam texto como humanos. Conectivos, preposições e transições que tornam um texto fluido para leitura humana são, para um modelo que prevê o próximo token, puro ruído ocupando espaço de contexto. Um redutor local remove esse excesso preservando 100% do sentido semântico relevante:

```
TEXTO HUMANO VERBOSO
"Coletamos informações pessoais fornecidas diretamente pelo usuário..." (12 tokens)
                    │
                    ▼ redutor local
TEXTO COMPACTO
"Coletamos informações pessoais usuário..." (5 tokens) — compreendido 100% pelo modelo
```

## Arquitetura de duas etapas

```
1. DOCUMENTO ORIGINAL (spec, PRD, PDF)
              │
              ▼
2. REDUTOR LOCAL (roda na própria máquina/VPS, custo de tokens zero)
              │  compressão de ~30–50%
              ▼
3. CONTEXTO COMPACTO enviado ao modelo principal (alta atenção, menor custo)
```

1. **Ingestão:** o usuário ou o orquestrador fornece uma especificação técnica, um documento de requisitos ou um PDF de política extenso.
2. **Compressão local:** antes de enviar o payload ao modelo principal, o harness desvia o texto para um modelo de redução rodando localmente na CPU ou GPU da própria máquina — a um custo de token zero, já que não é uma chamada de API.
3. **Handoff do resultado compacto:** o redutor expurga termos redundantes e formatação desnecessária, salvando o documento resultante compactado; essa versão enxuta é injetada na janela de contexto do modelo principal.

## Duas abordagens de infraestrutura

### Modelo leve otimizado para compressão (CPU-friendly)
Modelos pequenos especializados em compressão/sumarização estruturada (arquitetura leve, algumas centenas de milhões de parâmetros) rodam de forma extremamente rápida diretamente na CPU, sem exigir GPU dedicada — divide o texto em blocos, remove palavras marginais e reconstitui o sentido de forma condensada.

### Modelo de código local via runtime open-source (GPU-otimizado)
Quando há GPU disponível e a prioridade é preservar a integridade técnica de código ou especificações estruturadas, um modelo de código local (rodando via um runtime como Ollama) reescreve as especificações de forma concisa, com maior cuidado em preservar identificadores técnicos, chaves, nomes de variáveis e estruturas de arquivo exatamente como estão.

## Implementação de referência

```python
class LocalTokenReducer:
    """Compressão local de texto verboso, preservando o sentido semântico."""
    def __init__(self):
        self.stop_words_pattern = re.compile(
            r'\b(fornecidas|diretamente|pelo|para|com|uma|de|do|da|em|um|os|as|que|como)\b',
            re.IGNORECASE
        )

    def compress_text(self, raw_text: str) -> dict:
        original_tokens = len(raw_text) // 4
        clean_text = self.stop_words_pattern.sub("", raw_text)
        clean_text = re.sub(r'\s+', ' ', clean_text).strip()
        compressed_tokens = len(clean_text) // 4
        return {
            "original_tokens": original_tokens,
            "compressed_tokens": compressed_tokens,
            "compression_rate": f"{(1 - compressed_tokens / original_tokens) * 100:.1f}%",
            "compressed_content": clean_text,
        }
```

Em produção, a etapa de remoção de "stop words" é só a camada mais simples — a compressão real também reescreve frases inteiras de forma mais densa, preservando entidades e identificadores técnicos intactos.

## Impacto medido

- Compressão típica de documentos técnicos: 30% a 50% de redução no volume de texto enviado ao modelo pago.
- Reduções físicas de página proporcionais — um manual extenso pode ser convertido em uma fração do tamanho original sem perda de especificidade lógica.
- A economia se traduz diretamente na fatura de tokens de entrada de qualquer pipeline de longa duração que reprocesse o mesmo documento repetidamente.

## Privacidade como benefício colateral

Como o processamento de compressão roda 100% localmente (CPU ou GPU da própria máquina/VPS), nenhum dado corporativo confidencial, propriedade intelectual ou linha de código-fonte é transmitido a um servidor externo durante essa etapa de preparação — um benefício direto de conformidade regulatória, não só de custo.

## Isolamento e resiliência

- **Ambiente virtual isolado por skill:** cada redutor local roda em seu próprio ambiente de dependências isolado, evitando conflitos com as dependências do projeto principal.
- **Marcador de fallback:** se a chamada local de compressão falhar (exaustão de recursos, timeout), o harness insere deterministicamente um marcador sinalizando que o texto seguiu sem a compactação planejada — permitindo que o modelo principal ajuste sua expectativa de orçamento de contexto em vez de simplesmente estourar.

## Relação com outras técnicas desta skill

Um redutor local opera **antes** do documento entrar na conversa — é complementar, não substituto, da deduplicação de leituras (`file-read-deduplication.md`, que evita releitura do mesmo arquivo) e da compactação de diálogo (`compaction-and-clipping.md`, que atua sobre o histórico de conversa já em andamento).

## Checklist

- Documentos volumosos (specs, PRDs, PDFs) passam por um redutor local antes de entrar na janela do modelo principal, não são injetados brutos.
- O redutor roda isolado (ambiente virtual dedicado), sem poluir dependências do projeto.
- Identificadores técnicos (nomes de variável, chaves, caminhos de arquivo) são preservados intactos pela compressão — nunca parafraseados.
- Existe um marcador de fallback determinístico para quando a compressão local falha, em vez de o pipeline quebrar silenciosamente.

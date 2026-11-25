# Redação de Dados Sensíveis (PII/GDPR)

Parte de **Segurança e Identidade** (ver Framework Mental no `SKILL.md`). Disciplina de infraestrutura focada em interceptar, detectar, mascarar e substituir Informações de Identificação Pessoal (PII) e segredos comerciais **antes** que o payload chegue a qualquer modelo externo de nuvem.

## Por que salvaguardas contratuais não bastam

Provedores de modelos de nuvem costumam oferecer acordos de processamento de dados e termos que vedam treinar modelos com dados de clientes — mas essas são medidas puramente jurídicas. A conformidade real com regulamentos de privacidade (GDPR, HIPAA, CCPA, LGPD) exige **salvaguardas técnicas ativas** que impeçam dados confidenciais de sair do perímetro da rede antes mesmo de chegar ao modelo externo.

## Redação irreversível vs. anonimização reversível

### Redação completa (irreversível/destrutiva)
Age como uma via única: o dado é permanentemente destruído e substituído por um placeholder fixo (ex. `[REDACTED_SSN]`). Reservada a dados de altíssima sensibilidade que **nunca** devem ser vistos por uma IA em nuvem: números de cartão cru, senhas, chaves de carteira, números de documento de identificação.

### Anonimização reversível (pseudonimização)
Substitui o dado real por um pseudônimo estruturado e realista, preservando um mapeamento em um cofre local seguro para permitir desanonimização posterior:

- O texto contém "Sarah Williams" → o sistema intercepta, substitui por um pseudônimo verossímil ("Pamela Nelson") e registra a correlação no cofre.
- O modelo em nuvem processa a frase acreditando estar interagindo com Pamela Nelson.
- No caminho de retorno, antes de exibir o resultado ao usuário, o harness consulta o cofre e reverte o pseudônimo para o nome real — de forma invisível ao usuário final.

**Por que usar pseudônimos realistas em vez de placeholders abstratos:** modelos demonstram raciocínio contextual sensivelmente superior ao ler frases fluidas e coerentes (com um nome plausível) do que ao processar texto poluído por tags genéricas como `[PERSON_1]`.

## Arquitetura de borda (Edge Redaction)

O padrão ouro seria processar tudo localmente, isolado da rede (*airgapped*) — mas modelos locais de menor porte não têm o mesmo nível de raciocínio de um modelo flagship de nuvem, e a infraestrutura de GPU para hospedar modelos grandes localmente é cara. A arquitetura de redação de borda resolve esse paradoxo:

```
MENSAGEM ORIGINAL DO USUÁRIO
              │
              ▼
SCAFFOLDING DE BORDA (local)
  1. Detecção de PII (regex + NER)
  2. Modelo de segurança local leve (para casos ambíguos que escapam de regras estáticas)
  3. Registro/cofre de tokens PII (banco local)
  4. Geração de dados substitutos realistas
              │  dados redigidos e anonimizados
              ▼
GATEWAY DE MODELO EM NUVEM
  processa o payload anonimizado, trabalha só com pseudônimos
              │
              ▼ (desanonimização em runtime, antes de exibir ao usuário)
INTERFACE DO OPERADOR (dados reais restaurados)
```

## Implementação de referência

```python
class PIIVaultRegistry:
    """Cofre local de mapeamento bidirecional real <-> pseudônimo, sem persistência na nuvem."""
    def __init__(self):
        self._forward_map = {}   # valor_real_normalizado -> pseudônimo
        self._reverse_map = {}   # pseudônimo -> valor_real

    def get_or_create_surrogate(self, real_value, entity_type):
        key = real_value.strip().lower()
        if key in self._forward_map:
            return self._forward_map[key]
        surrogate = generate_realistic_fake(entity_type)  # ex.: biblioteca de dados fake
        while surrogate in self._reverse_map:              # evita colisão com pseudônimo já usado
            surrogate = f"{surrogate}_alt"
        self._forward_map[key] = surrogate
        self._reverse_map[surrogate.lower()] = real_value
        return surrogate

    def deanonymize_text(self, text_with_surrogates):
        result = text_with_surrogates
        for surrogate in sorted(self._reverse_map, key=len, reverse=True):  # mais longos primeiro
            result = re.sub(re.escape(surrogate), self._reverse_map[surrogate], result, flags=re.IGNORECASE)
        return result

class LocalRedactionEngine:
    """Interceptador que roda na borda, antes de qualquer chamada ao modelo em nuvem."""
    def __init__(self, vault):
        self.vault = vault
        self.credit_card_pattern = re.compile(r'\b(?:\d[ -]*?){13,16}\b')

    def execute_pre_llm_anonymization(self, input_text):
        # 1. Redação destrutiva de dados de altíssimo risco
        text = self.credit_card_pattern.sub("[CC_NUMBER_REDACTED]", input_text)
        # 2. Anonimização reversível de e-mails/nomes (detecção NER em produção)
        for email in find_emails(text):
            text = text.replace(email, self.vault.get_or_create_surrogate(email, "EMAIL"))
        return text
```

## Ameaças no ciclo de vida da redação

- **Injeção indireta de prompt exfiltrando dados:** um documento não confiável contém instrução oculta para buscar dados de faturamento e enviá-los a um webhook externo. O redator local deve atuar como uma barreira de saída (*outbound guardrail*): toda resposta gerada pela IA, antes de sair para um canal externo, passa pela varredura de PII — não só a entrada. Ver `prompt-injection-prevention.md`.
- **Esgotamento por chamadas de LLM em excesso:** delegar toda detecção de PII a chamadas de modelo em loop é caro e vulnerável a ataques de exaustão de cota. A detecção de alto volume deve ser feita por ferramentas determinísticas (regex, checksums, modelos locais leves); LLMs de fronteira entram só como segunda camada para ambiguidades que os algoritmos estáticos não resolvem.

## Decisões de engenharia (trade-offs)

- **Resolução de entidades (clustering):** a mesma pessoa referenciada de formas diferentes ("John Smith", "J. Smith", "Sr. Smith") precisa de um único pseudônimo consistente — não um por variação, senão o texto final fica incoerente. Um pré-processamento de agrupamento de entidades resolve isso antes da substituição.
- **Coerência de gênero/pronomes:** ao gerar um pseudônimo aleatório para um nome, é preciso preservar o gênero gramatical implícito do original — senão pronomes no corpo do texto ficam inconsistentes com o novo nome.
- **Bancos SQL externos:** ao consultar uma tabela real com uma query gerada pelo modelo (que só conhece pseudônimos), o interceptador de borda traduz o pseudônimo de volta ao valor real antes do disparo físico da query, e reanonimiza o resultado antes de devolvê-lo ao modelo.

## Checklist

- Redação destrutiva aplicada a dados de altíssimo risco (cartões, senhas, documentos); anonimização reversível para o resto.
- Detecção de PII de alto volume é determinística (regex/modelo local), não dependente de chamadas repetidas a um LLM de fronteira.
- Toda resposta do agente passa pela varredura de PII antes de sair para um canal externo, não só a entrada é filtrada.
- Cofre de mapeamento de pseudônimos vive local, nunca é enviado à nuvem.

Redação deve ocorrer em todas as fronteiras relevantes: contexto do modelo, memória, handoff interagente, ferramenta, log, trace e saída externa. O registro de segurança deve conservar apenas a classe do dado e a decisão, nunca o valor protegido.

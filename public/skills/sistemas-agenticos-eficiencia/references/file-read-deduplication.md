# Deduplicação de Leituras de Arquivos

Parte de **Eficiência e Gestão de Contexto** (ver Framework Mental no `SKILL.md`). Um comportamento patológico comum e caro: para verificar uma importação ou recuperar uma variável, o agente relê repetidamente o mesmo arquivo estático, e se o harness anexar cegamente o conteúdo completo a cada vez, a janela satura de ruído redundante.

## O custo da releitura redundante

Se um arquivo de 3.000 tokens é lido 10 vezes de forma inalterada ao longo de uma sessão, o agente consome 30.000 tokens de entrada só para manter a mesma informação "na mesa de trabalho". Além do custo direto, o efeito de saturação empurra o modelo para mais perto da Dumb Zone (ver Framework Mental no `SKILL.md`) e aumenta a latência de cada resposta.

## Arquitetura de deduplicação

```
SISTEMA DE ARQUIVOS
        ▲
        │ leitura física só se o hash mudou
        ▼
INTERCEPTADOR / CACHE
  calcula hash do conteúdo, compara com o histórico de leituras
        │
   ┌────┴────┐
   ▼ hash igual        ▼ hash mudou
PONTEIRO DE METADADOS   INJEÇÃO DE DELTA
"arquivo já lido no      envia só o diff das
turno N, sem alteração"  linhas alteradas
```

### Rastreamento por hash
Toda vez que o agente chama uma ferramenta de leitura, o harness intercepta a execução, calcula um hash do conteúdo físico e extrai metadados (caminho, tamanho, data de modificação).

### Substituição por ponteiros
O harness mantém uma tabela de arquivos já lidos na sessão ativa:
- **Primeira leitura:** conteúdo completo injetado normalmente.
- **Leituras subsequentes sem alteração de hash:** o harness bloqueia a reinjeção do texto bruto e insere uma string curta de metadados — algo como "o arquivo X foi lido com sucesso; o conteúdo permanece idêntico à leitura do turno N; use a versão já presente na sua janela". Isso preserva a sequência de ações do agente (ele sabe que leu e que está atualizado) sem gastar tokens repetindo o conteúdo.

### Injeção por delta
Se o hash mudar entre turnos (o arquivo foi modificado por outro processo ou pelo próprio agente), o harness calcula e injeta só o diff estruturado — as linhas adicionadas, removidas ou alteradas — em vez de reenviar um arquivo inteiro de dezenas de milhares de tokens.

## Implementação de referência

```python
class FileSystemDeduplicator:
    def __init__(self):
        self.read_registry = {}  # filepath -> (hash, turn_number, content)
        self.current_turn = 0

    def execute_read_file(self, filepath, physical_content):
        current_hash = hashlib.sha256(physical_content.encode()).hexdigest()

        if filepath not in self.read_registry:
            self.read_registry[filepath] = (current_hash, self.current_turn, physical_content)
            return {"action": "FULL_CONTENT_INJECTED", "content": physical_content}

        last_hash, last_turn, last_content = self.read_registry[filepath]

        if current_hash == last_hash:
            return {"action": "DEDUPLICATED", "message": f"Idêntico à leitura do turno {last_turn}."}

        # hash mudou: gera diff unificado em vez de reenviar tudo
        diff = "".join(difflib.unified_diff(
            last_content.splitlines(keepends=True),
            physical_content.splitlines(keepends=True),
        ))
        self.read_registry[filepath] = (current_hash, self.current_turn, physical_content)
        return {"action": "DELTA_DIFF_INJECTED", "diff": diff}
```

## Impacto medido

| Métrica | Sem deduplicação | Com deduplicação |
|---|---|---|
| Tokens de entrada | Crescimento linear cumulativo a cada releitura | Crescimento estável — redundância bloqueada |
| TTFT | Aumenta a cada turno conforme a janela engorda | Mantém-se estável |
| Taxa de alucinação | Elevada — ruído de repetição confunde o modelo | Reduzida — contexto permanece enxuto |

**Cache Hit Rate** (leituras deduplicadas / total de requisições de leitura) é a métrica de auditoria: valores acima de ~60% em tarefas complexas de desenvolvimento indicam uma arquitetura bem otimizada.

## Segurança: Cache Poisoning

Se um arquivo for alterado por um processo externo mas o harness tiver uma falha no cálculo do hash (ou pular a verificação), o agente pode continuar decidindo com base em uma versão obsolescida e potencialmente corrompida. **A regra é rígida: o hash e o timestamp devem ser recalculados no disco real a cada chamada**, nunca inferidos de um buffer em memória do processo orquestrador.

A ferramenta de leitura também deve operar sob os mesmos limites de sandboxing e privilégio mínimo tratados na skill de segurança desta coleção, se disponível — nunca aceitando caminhos fora do workspace autorizado.

## Trade-offs

- **Ponteiro de metadados vs. delta completo:** o ponteiro mínimo economiza mais tokens, mas exige que o modelo tenha boa retenção de longo prazo para localizar o arquivo na pilha do histórico. Para modelos menores/mais rápidos, um diff compacto das alterações recentes é mais seguro para manter o alinhamento lógico.
- **Verificação no host vs. em sandbox isolada:** calcular hash direto no diretório físico do host tem latência quase nula, mas expõe a risco de acesso não autorizado; fazer isso dentro de uma sandbox isolada é mais seguro, ao custo de alguma latência de provisionamento.

## Checklist

- Todo hash é recalculado no disco real a cada leitura — nunca reutilizado de memória sem verificação.
- Leituras redundantes viram um ponteiro curto de metadados, nunca reinjetam o conteúdo bruto.
- Alterações reais entre leituras geram um diff estruturado, não um reenvio completo do arquivo.
- Uma política de expurgo de cache (ex. menos usado recentemente) libera memória em sessões muito longas com centenas de arquivos mapeados.

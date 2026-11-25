# Loops de Auditoria (OS Audit Skills)

Parte de **Observabilidade e Melhoria Contínua** (ver Framework Mental no `SKILL.md`). O ângulo mais físico desta skill: como auditar e reverter ações de um agente no nível do sistema de arquivos, em tempo real — complementar ao tracing lógico de `tracing-inputs-outputs.md`.

## O modelo mental: "o estagiário literal"

Trate um agente com acesso ao sistema operacional como um estagiário brilhante, incansável, rápido — e perigosamente literal. Ele executa exatamente o que foi pedido, sem entender nuance organizacional. Um caso real de mercado: um agente interpretou uma instrução de "limpeza de ambiente" e apagou um banco de produção inteiro com seus backups em segundos — não foi um "erro técnico", foi uma instrução válida do ponto de vista do interpretador, mas catastrófica em termos de negócio, porque a distinção entre ambiente real e temporário só existia na cabeça do engenheiro humano.

Regras e prompts negativos ("nunca delete fora da pasta de rascunhos") não escalam — conforme o histórico da conversa cresce, a atenção do modelo sobre essa regra se dilui (o mesmo efeito "lost-in-the-middle" tratado em outras skills desta coleção). A solução real transfere o policiamento do prompt para um software determinístico que intercepta, valida e reverte antes que a ação afete o host.

## Decoupling cérebro/mãos

```
MODELO (cérebro probabilístico)
        │ gera a intenção: "quero rodar X"
        ▼
HARNESS (mãos determinísticas)
        │ captura na borda, traduz em ação segura,
        │ executa sob porta de qualidade, devolve resultado higienizado
        ▼
resultado
```

## Três camadas de proteção

### Camada A: isolamento físico de sandbox
Toda chamada de terminal ou ferramenta roda enclausurada em um ambiente de micro-virtualização — não um container que compartilha o kernel do host. Ver o desenvolvimento técnico completo dessa camada na skill de Segurança e Confiabilidade e na skill de Harness Engineering desta coleção, se disponíveis; aqui o ponto é: sem essa camada, as outras duas abaixo são inúteis.

### Camada B: o padrão Maker-Checker
Para modificações em massa na base de código, três papéis com contexto isolado:

1. **Maker (Implementador):** escreve os rascunhos ou realiza as modificações na sandbox.
2. **Checker (Revisor/Juiz):** contexto totalmente zerado, analisa só o diff final contra as convenções — ver `../assets/llm-as-a-judge-pattern.md`.
3. **Resolver:** se o revisor aponta falhas, um terceiro agente de contexto limpo corrige — quebrando o loop de retrabalho e alucinação persistente que ocorreria se o mesmo agente tentasse se auto-corrigir indefinidamente.

### Camada C: File-Integrity Monitoring (FIM) e rollback lógico
O componente genuinamente novo desta skill: monitoramento contínuo do sistema de arquivos da sandbox. Toda escrita passa por uma bateria de testes de regressão local antes de ser confirmada. Se a modificação corromper a lógica, quebrar um teste ou for barrada por um linter, o harness executa deterministicamente o descarte e o rollback do branch de desenvolvimento — redefinindo o ambiente à última assinatura íntegra conhecida.

## Implementação de referência

```python
class OSCommandAuditor:
    """Intercepta e barra chamadas de sistema no nível do OS."""
    def __init__(self, sandbox_root):
        self.sandbox_root = os.path.abspath(sandbox_root)
        self.blocked_patterns = [
            re.compile(r'\brm\s+-rf\s+/\b'),
            re.compile(r'\bchmod\s+777\b'),
            re.compile(r'\bprintenv\b|\benv\b'),
        ]

    def is_path_safe(self, target_path):
        return os.path.abspath(target_path).startswith(self.sandbox_root)

    def audit_bash_command(self, command):
        for pattern in self.blocked_patterns:
            if pattern.search(command):
                return False, f"Bloqueado: padrão destrutivo '{pattern.pattern}'."
        return True, "APPROVED"


class FileIntegrityWatcher:
    """Monitora modificações físicas e reverte arquivos corrompidos."""
    def __init__(self, monitored_file):
        self.monitored_file = monitored_file
        self.backup_path = monitored_file + ".bak"
        if os.path.exists(monitored_file):
            shutil.copy2(monitored_file, self.backup_path)

    def verify_and_enforce_linter(self):
        """Roda a verificação de integridade; reverte ao snapshot se falhar."""
        if not os.path.exists(self.monitored_file) or self._linter_fails():
            shutil.copy2(self.backup_path, self.monitored_file)  # rollback
            return False
        return True
```

O ponto central: o `OSCommandAuditor` bloqueia **antes** da execução (prevenção), o `FileIntegrityWatcher` reverte **depois** de detectar corrupção (contenção) — as duas camadas são complementares, nenhuma sozinha é suficiente.

## Rastreabilidade forense no nível do OS

Cada chamada de sistema ou ferramenta deve ser instrumentada capturando: o identificador de execução unificado, o operador humano responsável pela tarefa, o comando decodificado bruto, e o hash do arquivo antes e depois da escrita — permitindo reconstruir com precisão forense o que mudou e quando.

## Métricas de auditoria de OS

| Métrica | O que mede | Linha de base saudável |
|---|---|---|
| Taxa de evasão de sandbox | Chamadas bloqueadas por tentarem sair do diretório autorizado | 0% — qualquer desvio é anomalia severa |
| Frequência de falha de linter | Percentual de escritas que quebram sintaxe antes do commit | Abaixo de ~10% |
| Acurácia de seleção de ferramenta | Chamadas corretas vs. comandos redundantes gerados manualmente | Acima de ~92% |

## Governança de risco por ação

Esta skill categoriza ações do agente em níveis de impacto físico crescente (leitura → escrita reversível → ação externa → ação irreversível), com exigência de aprovação escalando junto. Essa é a mesma Escala de Confiança já detalhada como padrão canônico na skill de Segurança e Confiabilidade desta coleção, se disponível — não a redefino aqui para evitar duplicação; o ponto específico desta skill é que a **camada de FIM e rollback** é o mecanismo físico que dá segurança para operar nos níveis intermediários sem exigir aprovação humana em toda escrita reversível.

## Checklist

- Todo comando de terminal passa por um auditor determinístico antes de tocar o sistema real, nunca depois.
- Toda escrita em arquivo monitorado tem um snapshot de referência salvo antes da modificação.
- Uma falha de linter/teste após a escrita dispara rollback automático, não só um alerta.
- A taxa de evasão de sandbox está sendo monitorada ativamente — não é uma métrica "configurada e esquecida".

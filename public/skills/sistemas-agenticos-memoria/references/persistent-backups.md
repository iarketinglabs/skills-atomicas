# Backups Persistentes

Parte de **Memória e Aprendizado de Longo Prazo** (ver Framework Mental no `SKILL.md`). O substrato final de durabilidade: onde a memória consolidada dos outros três arquivos desta skill vive fisicamente a longo prazo, protegida contra corrupção e recuperável se algo der errado.

## O caso que justifica o rigor

Delegar a um agente a capacidade de escrever diretamente em arquivos e bancos de dados sem um mecanismo rígido de rollback é perigoso mesmo quando o agente não está comprometido — um comando ambíguo de "limpeza de diretório" já foi suficiente, em um incidente real de mercado, para um agente apagar um banco de dados de produção inteiro junto com seus backups locais em segundos. A lição não é "não dar autonomia" — é: **nunca opere escrita autônoma sem uma máquina do tempo determinística por baixo.**

## Arquitetura híbrida: notas versionadas + controle de versão

```
COMMODITY COGNITIVA          MEMÓRIA CENTRAL              VERSIONAMENTO
(LLM de fronteira,     ──►   (vault de notas em     ──►   (snapshots de código
 API volátil)                 Markdown local)               e branches isolados)
```

1. **O modelo como utility descartável:** modelos de fronteira mudam de versão e sofrem atualizações de peso que alteram comportamento silenciosamente; suas threads de conversação em servidores de terceiros são efêmeras. Trate-os como motores de raciocínio para a chamada síncrona corrente — não como o lugar onde o conhecimento organizacional mora.
2. **O vault de notas como sistema de registro:** conhecimento acumulado — identidade, metas, heurísticas de runs anteriores — persiste em arquivos de texto plano estruturados em pastas lógicas. Formato de arquivo plano garante portabilidade: trocar de provedor de IA não exige migração, só apontar o novo conector para o mesmo diretório físico.
3. **O controle de versão como máquina do tempo:** toda modificação relevante roda em um branch isolado. Se o agente gerar código quebrado ou corromper o repositório, o harness dispara comandos determinísticos de reversão, blindando o branch principal de qualquer mutação perigosa.

## Camadas de runtime

```
SANDBOX OPERACIONAL (executa ferramentas, gera logs de decisão)
        │ término da sessão / stage do repositório
        ▼
ORQUESTRADOR DE TELEMETRIA LOCAL
  1. Registro ativo (IDs de execução, estados, traces)
  2. Controlador do vault de notas
  3. Monitor de branches isolados (worktrees)
        │ sincronização headless
        ▼
RECURSO DE BACKUP
  TIER A: vault de notas local (arquivos Markdown estáveis)
  TIER B: repositório remoto privado (backup e rollback)
```

## Implementação de referência: snapshot seguro e rollback de emergência

```python
class PersistentBackupEngine:
    def create_safe_point_snapshot(self, run_id, commit_message):
        """Stage e commit de todas as mudanças físicas desde o último snapshot."""
        self.vcs.add_all()
        result = self.vcs.commit(f"Agent Run [{run_id}]: {commit_message}")
        return "SUCCESS_COMMIT" if result.ok else "NO_CHANGES_OR_FAILED"

    def trigger_emergency_rollback(self, run_id, target_commit="HEAD~1"):
        """Restaura o sistema de arquivos ao último estado íntegro conhecido."""
        self.vcs.reset_hard(target_commit)
        self.vcs.clean_untracked()  # remove artefatos gerados dinamicamente, inclusive maliciosos
        return True
```

O ponto de decisão crítico não é técnico — é de política: **quando** disparar o rollback automaticamente (corrupção detectada por linter, teste quebrado) versus quando só alertar um humano.

## Higienização antes do push

Antes de despachar qualquer nota ou arquivo de workspace para um repositório remoto, o pipeline de backup roda obrigatoriamente uma rotina de redação de dados sensíveis: expressões regulares e listas de padrões identificam e substituem chaves de API, tokens e dados pessoais por placeholders estáticos, antes que o conteúdo saia do ambiente local. Um `.gitignore` bem configurado é a primeira camada dessa defesa — nunca a única:

```
.env
*.env
secrets.json
private_key.pem
node_modules/
__pycache__/
```

## Privilégio mínimo de escrita

O container operacional nunca deve usar credenciais administrativas de escrita irrestrita direto no branch principal. O padrão correto: tokens temporários com escopo restrito a branches de trabalho, com o merge definitivo delegado a um pipeline de revisão ou a um mantenedor humano sênior — o mesmo padrão maker-checker de dois papéis (quem propõe, quem aprova) usado em outras camadas de governança desta coleção, se disponível.

## O ciclo de consolidação aplicado a notas

```
CONVERSA ATIVA          DIÁRIO DO WORKER          CONSOLIDAÇÃO EM SLEEP TIME
(histórico bruto)  ──►  (logs estruturados)  ──►  poda transcrições redundantes
                                                          │
                                                          ▼
COMMIT NO REPOSITÓRIO  ◄──  ORGANIZAÇÃO NO VAULT  ◄──  DECAIMENTO TEMPORAL
(snapshot criptografado)     (notas limpas e ligadas)   (notas frias arquivadas)
```

Notas sazonais sem acesso ou busca recente perdem prioridade e são compactadas em pacotes de arquivo frio — liberando a velocidade de busca do índice ativo. O mecanismo de decaimento é o mesmo descrito em `../assets/temporal-decay-and-trust-score.md`.

## Métricas de resiliência

| KPI | O que mede | Limiar saudável |
|---|---|---|
| Frequência de commit de erro | Snapshots gerados só por necessidade de rollback | Abaixo de ~10% das sessões |
| Latência de push | Tempo para consolidar e enviar notas/logs ao repositório remoto | Abaixo de poucos segundos por sessão |
| Taxa de crescimento do vault | Volume de arquivos novos adicionados por período | Sinaliza a necessidade de rodar o ciclo de consolidação com mais frequência se subir de forma anômala |
| Taxa de sucesso de rollback | Percentual de restaurações testadas e concluídas sem falha | 100% — qualquer falha aqui indica corrupção crítica na cadeia de backup |

## Trade-offs e anti-padrões

- **Sincronização síncrona vs. assíncrona:** commitar a cada interação bloqueia desvios lógicos com precisão cirúrgica, mas insere latência perceptível. Operar de forma assíncrona (buffer com intervalo fixo) preserva a fluidez, mas abre uma janela de exposição a perda de progresso em caso de crash.
- **"Commit Spamming":** disparar um commit a cada micro-mensagem trocada com o agente polui o histórico com ruído, inviabiliza auditoria humana de diff e consome cota de requisições de rede desnecessariamente.
- **Memória monolítica vs. fragmentada:** uma única nota gigante acumulando todo o aprendizado do ecossistema inunda a janela de contexto de qualquer consulta. Segmentar por domínio/projeto protege a recência do contexto, mas exige mais disciplina de indexação entre as notas.

## Checklist

- Todo workspace agêntico com escrita autônoma roda sob controle de versão, com branches isolados para trabalho em paralelo.
- Segredos e credenciais estão protegidos contra stage acidental antes de qualquer commit automático.
- Um snapshot seguro é criado ao fim de cada sessão de tarefa concluída, com o identificador de execução amarrado ao commit.
- O container operacional nunca detém credenciais de escrita irrestrita direto no branch principal.
- Um ciclo periódico de consolidação deduplica, arquiva e poda notas frias — o vault não cresce sem curadoria.

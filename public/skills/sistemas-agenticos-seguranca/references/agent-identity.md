# Identidade do Agente (OIDC/Diretórios)

Parte de **Segurança e Identidade** (ver Framework Mental no `SKILL.md`). Responde a "quem é este agente" — a base sobre a qual `api-scoping-and-permissions.md` decide "o que ele pode fazer". Um agente sem identidade formal e auditável, herdando chaves estáticas globais, é um vetor letal de exposição em caso de prompt injection (ver `prompt-injection-prevention.md`).

## Três categorias de identidade

| Categoria | Tipo de credencial | Ciclo de vida | Relação |
|---|---|---|---|
| **Humana** | Credenciais interativas (senha, SSO, MFA) | Longo prazo, vinculada a uma pessoa | Direta — a pessoa age por cliques |
| **Conta de serviço (M2M)** | Chaves de API estáticas, segredos em arquivo local | Longo prazo, estáticas, difíceis de rotacionar | Unidirecional — integração rígida entre sistemas |
| **Identidade agêntica** | Tokens efêmeros assinados, vinculados dinamicamente à tarefa | Curtíssimo prazo, rotacionada automaticamente | Triangular (Usuário ↔ Agente ↔ Serviço upstream) — o agente age em nome do usuário, sob escopo estrito |

O agente não "vê" a tela como um humano — ele age por código, API e protocolo. Por isso, herdar uma chave estática global (uma credencial pensada para categoria M2M) para um agente que deveria ter identidade dinâmica é um desalinhamento fundamental de modelo de segurança.

## Quatro pilares da identidade agêntica

1. **"A IA precisa saber quem eu sou":** o agente tem acesso controlado à identidade do usuário operador para aplicar políticas e limites — sem isso, a sessão é anônima e sem limites lógicos de segurança.
2. **"A IA precisa chamar APIs em meu nome":** o agente interage com sistemas de registro (CRM, ferramentas internas) em nome do usuário, sem que o programador precise expor chaves mestras estáticas.
3. **"A IA pode solicitar minha confirmação":** o harness fornece ganchos que suspendem a atividade assíncrona em tarefas de risco para pedir aprovação em tempo real — ver `../assets/trust-ladder.md`.
4. **"O acesso da IA deve ser granular":** o nível de acesso é delimitado cirurgicamente aos recursos estritamente necessários para a subtarefa, nunca a todo o sistema.

## Relacionamento de confiança triangular

```
                    USUÁRIO
       login + consentimento de escopo │  push de confirmação
                    ▼                  ▼
              AGENTE (IA) ──────► SERVIÇO UPSTREAM
              roda em sandbox      valida token, escopos estritos
              sem chaves locais
                    ▲
      troca de tokens curtos │
                    ▼
              TOKEN VAULT
              fora da janela de contexto, rotação automática
```

### Token Vault
Serviço desacoplado do processamento do modelo, mantido na borda do orquestrador:
- O modelo **nunca visualiza** tokens de atualização (*refresh tokens*) ou segredos permanentes.
- O agente faz uma requisição local ao vault passando o ID da tarefa; o vault executa a rotação junto ao provedor de identidade e injeta um token de acesso de **vida curta configurada pelo risco** estritamente na chamada da ferramenta.

### CIBA (Client Initiated Backchannel Authentication)
Para aprovar ações sensíveis executadas por agentes rodando em background sem supervisão direta, sem depender de pop-ups interativos que inviabilizariam a automação:

1. Ao atingir uma ação de alto risco (ver `../assets/trust-ladder.md`, nível 4), o agente dispara uma requisição assíncrona de autenticação.
2. O orquestrador envia uma notificação por um canal externo (push no dispositivo móvel do usuário).
3. O agente entra em espera, sem consumir tokens de contexto conversacional enquanto aguarda.
4. Uma vez que o usuário valida os detalhes estruturados e assina a autorização, um token de acesso escopado exclusivamente àquela transação é entregue de volta ao agente, que retoma o trabalho.

## Diretórios de agentes e Cross-App Access (CAA)

À medida que uma organização escala o número de agentes, o risco de "agentes órfãos" (instâncias não catalogadas, criadas informalmente por colaboradores) cresce. A mitigação é um diretório central:

```
REGISTRO DE AGENTES
Nome do Agente | Proprietário (User ID) | Escopos    | Status
Agente_Cobranca| user_financeiro        | read:bills | Ativo
Agente_Dev     | user_dev               | write:repo | Ativo
```

- Toda nova instância de agente gera uma entrada estruturada: ID, proprietário humano, escopo autorizado, tempo de vida.
- Ao término da tarefa, o harness desprovisiona a identidade e expurga os tokens associados — nunca deixa uma credencial permanente órfã.
- O padrão **Cross-App Access**, acoplado ao protocolo de conectividade externa do agente, faz cada agente se anunciar a outros sistemas via um manifest descritivo: quem é, quem autorizou, quais escopos tem, e a chave pública para validar suas mensagens.

## Ameaças específicas de identidade

- **Impersonação de agentes:** um ator malicioso tenta se passar por um agente legítimo registrado no diretório para herdar seus acessos.
- **Rogue agent escalation:** um agente sob prompt injection passa a instanciar novos subagentes órfãos além do escopo aprovado.
- **Roubo de credenciais estáticas:** um agente com acesso irrestrito ao terminal lê arquivos de variáveis de ambiente locais e expõe as chaves.
- **Wallet draining:** um atacante inunda o agente com entradas ruidosas, forçando reprocessamento caro em modelos de fronteira sem limite de gasto.

## Resposta a incidentes

Ver o playbook completo em `../assets/incident-response-playbook.md` — a identidade federada e de curta duração descrita aqui é o pré-requisito técnico que torna possível revogar o acesso de um agente comprometido dentro do prazo de contenção definido, sem precisar reescrever código ou fazer novo deploy.

## Checklist

- Nenhum agente herda uma chave estática M2M de longa duração — toda identidade agêntica é efêmera e rotacionada.
- Token Vault mantém segredos fora da janela de contexto do modelo.
- Ações de alto risco (nível 4 da Trust Ladder) passam por CIBA — aprovação assíncrona explícita.
- Todo agente ativo está catalogado em um diretório central com proprietário, escopo e tempo de vida definidos.

## Interface com o plano de controle

Identidade não autoriza tudo que o agente consegue alcançar. Combine este registro com `agentic-security-control-plane.md`: derive um capability envelope por tarefa, preserve a cadeia de delegação e revogue por identidade, tarefa e ferramenta quando houver desvio.

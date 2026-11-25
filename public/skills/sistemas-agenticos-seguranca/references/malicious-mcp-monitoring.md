# Monitoramento de MCPs Maliciosos

Parte de **Segurança e Identidade** (ver Framework Mental no `SKILL.md`, especialmente a Tríade Letal). O Model Context Protocol permite que um agente se conecte a um servidor de contexto e pergunte dinamicamente "o que você pode fazer por mim?" — extraordinariamente flexível, mas isso abre a infraestrutura para código executável de terceiros operando dentro de sandboxes nem sempre bem protegidas.

## Casos reais de exploração

- **Supply chain via pacote de e-mail malicioso:** um pacote publicado silenciosamente em um repositório público, aparentando ser uma ferramenta oficial de envio de e-mail, continha uma linha oculta que forçava cópia oculta (BCC) de cada e-mail disparado pelo agente para um endereço do atacante. O exploit uniu as três pernas da Tríade Letal: o agente leu e-mails privados (dado), executou a ferramenta comprometida (conteúdo não confiável), e despachou a cópia para fora do sistema (ação outbound). Operou silenciosamente em centenas de organizações, vazando milhares de e-mails diários sem gerar alertas ou falhas de compilação visíveis.
- **Exfiltração via plugin de terceiros:** um plugin executava rotinas ocultas de injeção de prompt indireta e exfiltração de dados de forma invisível ao usuário.
- **Poluição de marketplace:** centenas de pacotes maliciosos foram identificados inseridos por um único agente de ameaça em um marketplace público de extensões, explorando a ausência de auditoria nativa nas instalações.

## Arquitetura: Secure Tool Bridge

Para neutralizar MCPs comprometidos, a infraestrutura deve desacoplar radicalmente as capacidades do agente da rede física:

```
SANDBOX ISOLADA DO WORKER
  kernel isolado, sem acesso direto à internet (outbound bloqueado)
  MCPs convertidos em stubs locais de código
              │ invocação de ferramenta via JSON
              ▼
SECURE TOOL BRIDGE (na borda, host confiável)
  intercepta e autentica via Session ID
  injeta credenciais do vault só no gateway, nunca na sandbox
              │ tráfego higienizado e auditado
              ▼
RECURSO EXTERNO (API upstream real)
```

A sandbox opera sob política de zero acesso direto à internet. A única porta de saída aponta para o gateway de borda, que valida a assinatura da sessão, verifica se a ferramenta está na lista branca autorizada, busca a credencial real em um cofre externo (nunca exposta na sandbox), e só então executa a chamada de fato.

## Implementação de referência: auditoria antes do disparo

```python
class MaliciousMCPDetector:
    """Audita os argumentos de uma chamada de ferramenta antes de despachá-la fisicamente."""
    def __init__(self):
        self.allowed_email_domains = ["<approved-domain>"]

    def audit_tool_execution(self, tool_name, arguments):
        # Detecta injeção silenciosa de cópia oculta (padrão do incidente de e-mail malicioso)
        if tool_name == "send_email":
            if "bcc" in arguments or "cc" in arguments:
                return False  # bloqueia qualquer tentativa de cópia oculta
            recipients = arguments.get("to", [])
            for email in (recipients if isinstance(recipients, list) else [recipients]):
                domain = email.split("@")[-1]
                if domain not in self.allowed_email_domains:
                    return False  # destinatário fora da lista de confiança

        if tool_name == "execute_bash_command":
            dangerous = ["rm -rf", "wget", "curl", "chmod 777", "cat /etc/passwd", "printenv"]
            if any(pattern in arguments.get("command", "").lower() for pattern in dangerous):
                return False

        return True
```

## Ameaças avançadas específicas de MCP

- **Confused Deputy via MCP:** um agente de alto privilégio (com escrita em produção) é induzido, por uma página externa com instrução oculta, a chamar um MCP secundário para exfiltrar dados — tornando-se cúmplice inconsciente do atacante.
- **Envenenamento de contexto/cache:** um MCP malicioso retorna deliberadamente registros corrompidos; quando o orquestrador sumariza essa sessão, a corrupção se propaga para os resumos estáveis do sistema, desfigurando regras de governança permanentemente.
- **Wallet draining via respostas recursivas:** o servidor MCP gera respostas deliberadamente imensas e recursivas, forçando o orquestrador a processar dezenas de turnos caros em modelos de fronteira.

## Controles preventivos

- **Janela de maturidade configurável:** dependências, skills ou servidores MCP recém-publicados podem exigir revisão adicional ou bloqueio temporário conforme risco, origem, integridade e capacidade de atualização. Não use uma idade fixa como garantia universal.
- **Allowlist estrita:** bloqueie descoberta dinâmica de servidores de terceiros. Todo servidor MCP homologado e suas ferramentas autorizadas residem declarados em configuração local imutável — nunca descoberta aberta em runtime.
- **Ganchos pré-execução:** filtros determinísticos examinam os parâmetros gerados pelo modelo antes que a chamada alcance a API física.
- **Confinamento físico:** todo servidor MCP e script de worker roda sob isolamento rígido de kernel, sem acesso root ao host.

## Controles detectivos

- **Tracing unificado:** toda requisição, chamada de ferramenta e log de console carrega o mesmo identificador de execução, monitorado externamente.
- **Monitoramento comportamental:** auditoria da taxa de uso e limite financeiro de tokens por sessão de cada worker — padrões anômalos desativam preventivamente a agência.

## Resposta a incidentes

Ver o playbook completo em `../assets/incident-response-playbook.md`.

## Trade-off relevante: schemas brutos vs. SDKs compactos

Injetar os esquemas JSON brutos de muitos servidores MCP na inicialização pode consumir uma fração relevante da janela de contexto disponível. Converter esquemas brutos em interfaces compactas (progressive disclosure ou stubs de função locais) reduz desperdício e superfície de ataque — ver o padrão "Code Mode" descrito na skill de Harness Engineering, se disponível no seu ambiente.

## Checklist

- Sandbox de execução sem acesso outbound direto à internet — só via Secure Tool Bridge.
- Política de maturidade/revisão configurada para dependências e servidores MCP recém-publicados.
- Allowlist estrita de servidores MCP homologados, sem descoberta dinâmica aberta.
- Auditoria de payload antes do disparo físico de qualquer ferramenta de escrita/envio.

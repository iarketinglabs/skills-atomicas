# Operação, avaliação e atualidade

Uma automação que foi aceite sem alertas não prova que o trigger esteja saudável. Meça tanto execução quanto o sinal esperado e a capacidade de recuperação.

## Observabilidade

Propague IDs de evento, entidade, execução, tentativa, janela/cursor, regra e correlação onde não exponham informação sensível. Registe a versão de contrato/regra e os resultados de política/aprovação necessários para auditoria. Evite guardar corpo integral, prompts ou respostas por defeito; aplique redação, acesso e retenção documentados.

Considere métricas que permitam distinguir ociosidade legítima de falha silenciosa:

- sinais recebidos, rejeitados, duplicados, aceites e descartados por motivo;
- atraso ocorrência-receção e receção-início/conclusão;
- execuções em falta, cursor sem progresso, janelas perdidas e heartbeat atrasado;
- retries, timeout, resultado incerto, fila atrasada, DLQ e recuperação;
- falhas e efeitos duplicados observados;
- custo, chamadas de modelo/ferramenta e limite atingido, quando aplicável.

Defina alertas pelo impacto e pelo atraso permitido. O painel sem dados deve ser distinguível de tráfego zero. Para fluxos agendados, monitore a conclusão de cada janela; para fontes contínuas, monitore heartbeat ou frescura esperada.

## Prova antes de ativar

Escolha cenários a partir dos requisitos e incidentes do sistema. Inclua, conforme o padrão:

- duplicação, atraso, ordem diferente, evento inválido/desconhecido e tamanho excessivo;
- queda antes/depois da confirmação, cursor interrompido e resultado externo incerto;
- execução agendada repetida, em falta, sobreposta e mudança de hora/fuso;
- outage além da janela de retry, reconciliação e replay seguro;
- autoridade revogada, entrada externa maliciosa, proposta sensível e gate humano;
- limites de volume, dependência indisponível e caminho de pausa.

Verifique estado durável e efeitos reais com dados sintéticos e ferramentas sem efeito quando apropriado. Não use só o texto final do agente como oráculo. Mantenha premissas e resultado observado separados.

## Verificar informação que muda

Para uma pergunta sobre plataforma, biblioteca, protocolo, capacidade de retry, retenção, SLA, preço ou status de versão:

1. procure a documentação oficial da versão e plano concretos;
2. confirme se a afirmação é normativa, opcional, preview/beta, documentada como suportada ou observada no ambiente;
3. verifique limites, configuração, SDK e integração cliente-servidor envolvidos;
4. registe URL, versão/data de consulta, configuração e lacunas;
5. se a fonte não confirmar, reporte a incerteza e não transporte uma afirmação de síntese antiga como facto atual.

O mesmo nome de protocolo pode abranger núcleo, extensões, implementações e estágios de suporte diferentes. Especificação não substitui prova de interoperabilidade ou aceitação operacional.

## Fontes

- [OpenTelemetry GenAI semantic conventions](https://github.com/open-telemetry/semantic-conventions-genai) — nomes/campos podem evoluir; confirme estado e estabilidade antes de criar dependências.
- [Documentação MCP](https://modelcontextprotocol.io/specification/) e [A2A](https://a2a-protocol.org/latest/specification/) — fontes oficiais para requisitos de protocolo vigentes.

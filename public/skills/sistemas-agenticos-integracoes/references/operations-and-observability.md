# Operação e observabilidade

Uma integração tem de poder ser explicada e recuperada sem depender de reproduzir manualmente a sequência inteira.

## Evidência operacional

- Correlacione pedido, mensagem/evento, tentativa, contrato, versão do produtor/consumidor e execução de agente com IDs opacos e propagados.
- Registe estados do fluxo (aceite, pendente, aplicado, rejeitado, conciliado) conforme a semântica real. Distingua ACK de transporte do efeito final.
- Meça latência ponta a ponta, taxa de erro por classe, idade/atraso e profundidade de fila, tentativas, duplicados, falhas permanentes, divergência na reconciliação, custo por operação concluída e limites/quota relevantes.
- Use tracing distribuído e propagação de contexto quando disponíveis; valide versão e semântica das convenções antes de depender de campos específicos.
- Nunca registe tokens, segredos, conteúdo pessoal ou payloads completos por conveniência. Redija ou pseudonimize campos e restrinja acesso e retenção dos registos.

## Operação e suporte

- Nomeie responsáveis de origem, destino e fluxo; determine quem recebe alertas e quem pode repetir, corrigir, pausar ou revogar acesso.
- Defina alertas a partir do impacto e da janela de negócio, não só da existência de um erro.
- Documente quotas, expiração de credenciais, limites, manutenção e dependências externas confirmados pelo fornecedor.
- Defina procedimentos para falha parcial, atraso acumulado, DLQ, cursor perdido, schema incompatível, webhook inválido, credencial revogada e efeito de negócio incerto.
- Ofereça replay/redrive com proteção de idempotência, inspeção, autorização e possibilidade de limitar um intervalo ou subconjunto.
- Para workflows com agentes, guarde trilha de ferramentas chamadas, identidade/escopo, aprovações, transferências e resultado. Evite registar cadeia de pensamento ou conteúdo sensível desnecessário.

## Evidência e release

Associe cada alteração de contrato, política e ferramenta à versão implantada e aos critérios de aceite. Separe logs de implementação, provas de sandbox e evidência de produção. Documentação correta não prova que OAuth, webhook, filas ou recuperação funcionam no ambiente real.

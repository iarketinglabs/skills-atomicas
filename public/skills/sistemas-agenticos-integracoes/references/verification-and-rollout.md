# Verificação, lançamento e recuperação

Defina a evidência antes de implementar. Um teste deve corresponder a uma propriedade observável e ao risco da integração.

## Cobertura de verificação

1. **Contrato:** payload válido/inválido, campos ausentes/desconhecidos, limites, versão antiga/nova, codificação, paginação e erro esperado.
2. **Semântica:** identidade, mapeamento, unidades, estado final, correção e autoridade da origem.
3. **Confiabilidade:** repetição, duplicação, ordenação, atraso, timeout após envio, indisponibilidade, replay e reconciliação.
4. **Segurança:** autenticação/autorização por ação e tenant, privilégio mínimo, credencial revogada, assinatura/replay de webhook e conteúdo malicioso.
5. **Carga e limites:** picos e concorrência representativos, quotas, latência, pressão em origem/destino, backpressure e comportamento de degradação.
6. **Operação:** telemetria suficiente, alertas, pausa, redrive, recuperação, auditoria e identificação do proprietário.
7. **Agentes:** se aplicável, tarefas comuns, ambíguas, inválidas e adversariais; efeito final, limites, recusa, aprovação, escalada e custo.

Use ambiente isolado, dados sintéticos e serviços de sandbox quando disponíveis. Verifique resultados no estado de destino, não apenas no status HTTP ou na saída do agente. Não use ambiente de produção para descobrir efeitos de uma operação sem aprovação explícita.

## Lançamento gradual

- Defina pré-condições e responsáveis por origem, destino e suporte.
- Valide a configuração e os contratos antes de ativar tráfego. Se houver escrita dupla, evite que dois caminhos concorrentes produzam efeitos incompatíveis.
- Quando o risco justificar, comece por leitura/simulação, subconjunto controlado, tráfego espelhado sem efeitos, ou rollout gradual; escolha uma estratégia compatível com a semântica e privacidade.
- Acompanhe critérios de aceitação e uma janela de observação. Defina sinais de pausa e quem decide retomar.
- Planeie migração de dados/contratos, reconciliação e reversão antes de retirar o caminho antigo.
- Antes de operações destrutivas, financeiras ou externas, confirme a autorização e o estado do sistema. Se o resultado de uma tentativa anterior for incerto, concilie antes de repetir.

## Critérios de aceite

Escreva critérios com dado de entrada, identidade/estado inicial, efeito esperado, comportamento de falha e evidência necessária. Para resultados probabilísticos, defina conjunto de casos, limiar de aceitação, falhas críticas, revisão humana e condição de reteste. Registe limitações, versões, ambiente e o que ainda não foi demonstrado.

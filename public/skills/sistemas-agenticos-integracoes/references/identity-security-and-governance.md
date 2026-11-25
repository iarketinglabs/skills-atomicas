# Identidade, segurança e governança

Avalie cada integração como uma fronteira de confiança. Segurança do transporte, identidade do chamador, autorização do efeito e proteção dos dados são controlos diferentes.

## Identidade e privilégios

- Identifique a pessoa, serviço, aplicação ou agente que inicia a operação e a identidade que o destino autoriza.
- Aplique menor privilégio por capacidade, recurso, tenant, ambiente e finalidade. Não reutilize uma credencial ampla entre fluxos independentes quando é possível restringi-la.
- Separe autenticação (quem chama) de autorização (o que pode fazer). Valide audiência, escopos, tenant e expiração no serviço que executa o efeito.
- Use protocolos e mecanismos de identidade suportados pelas duas partes. Consulte as especificações oficiais e a documentação atual; não infira uma versão ou fluxo seguro a partir de um rótulo.
- Proteja segredos fora do código, logs, prompts e dados de teste. Defina rotação, revogação, armazenamento e comportamento quando expirarem.
- TLS protege a comunicação em trânsito; mTLS pode ser adequado para autenticação entre workloads em fronteiras controladas. Avalie gestão de certificados e recuperação como parte do custo.

## Webhooks e endpoints

- Siga exatamente o algoritmo e a representação canónica definidos pelo fornecedor para validar a assinatura; valide timestamp/nonce quando suportado e rejeite replay fora da janela acordada.
- Faça a verificação antes de confiar no payload, proteja rotação de segredo e compare assinaturas em tempo constante quando o runtime suportar essa operação.
- Não confie apenas numa lista de IPs. Proteja o endpoint com limites, validação de tamanho, deduplicação e fila de trabalho.
- Se a integração aceitar URLs fornecidos por utilizadores ou sistemas externos, avalie SSRF, DNS rebinding, redirecionamentos e acesso a redes/metadados internos. Restrinja destinos e resoluções no ponto que efetua a ligação.

## Dados e governança

- Classifique os campos, reduza a recolha e transferência ao necessário, limite acesso e retenção e defina apagamento, correção e auditoria.
- Registe finalidade, controlador/proprietário operacional, localização/transferência se for requisito, e consumidores que recebem cópias.
- Não copie PII ou segredos para tracing, logs, eventos de diagnóstico, prompts ou exemplos sintéticos.
- Confirme regras legais, contratuais e setoriais para a jurisdição e data aplicáveis com fonte competente. Esta skill não determina conformidade jurídica.

## Controlo de efeitos

Valide no servidor todos os campos e transições de estado. A interface, gateway, agente ou documentação do fornecedor não substituem a autorização no destino. Registe quem/que sistema iniciou a ação, escopos usados, aprovação relevante, chave de correlação e resultado sem guardar conteúdo sensível desnecessário.

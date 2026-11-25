# Contratos e evolução

Um protocolo define como comunicar; um contrato define o significado, os limites e os resultados que os participantes podem esperar. Documente ambos e atribua um responsável para cada lado do contrato.

## Conteúdo mínimo do contrato

- Identidade da operação, evento ou recurso e versão do contrato.
- Produtor, consumidores, finalidade e sistema autoritativo para cada campo.
- Semântica e unidades; diferença entre campo ausente, nulo, vazio e valor padrão.
- Chaves, correlação, tempo do evento e tempo de receção quando ambos importam.
- Formato, restrições verificáveis, validação e comportamento para campos desconhecidos.
- Autenticação, autorização, tenant/escopo, limites de tamanho, volume e taxa.
- Paginação, cursor, ordenação e política para repetição ou concorrência.
- Resultados de sucesso, erros transitórios e permanentes, estados pendentes e resultado incerto.
- Compatibilidade, depreciação, janela de migração, responsáveis e plano de retirada.

## Formatos e contratos

Escolha a descrição que corresponde ao fluxo: OpenAPI para interfaces HTTP, AsyncAPI para interfaces orientadas a mensagens, CloudEvents quando um envelope de evento interoperável for útil, JSON Schema ou outro esquema para validar payloads, e contratos de serviço próprios do RPC escolhido. Estes formatos não eliminam a necessidade de definir semântica, autorização ou ciclo de vida. Confirme a versão suportada e as regras da especificação oficial antes de gerar código ou validar compatibilidade.

Use documentação executável e exemplos sintéticos pequenos. Não inclua dados reais, tokens ou valores sensíveis nos exemplos. Evite descrições que contradizem as regras no schema; uma instrução em prosa não substitui uma validação no servidor.

## Evolução compatível

- Considere a forma como consumidores reais lidam com campos desconhecidos, enumerações, valores nulos, ordenação e tipos estritos. Uma alteração aditiva pode ser incompatível para um cliente.
- Prefira mudanças graduais: acrescentar capacidade compatível, migrar consumidores, observar tráfego/versões e retirar o contrato antigo depois de um critério verificável.
- Não reutilize um identificador de campo removido com outro significado.
- Versione o contrato e os dados de referência usados no deploy; saiba qual versão está a produzir e consumir cada fluxo.
- Use testes de contrato em ambos os lados. Testes de schema isolados não demonstram semântica nem compatibilidade no comportamento real.
- Em mudanças de payload, mantenha leitura do formato antigo durante a migração quando necessário, mas defina o prazo e a condição de remoção.

## Mapeamento e propriedade

Mapeie nomes e valores explicitamente, incluindo regras de normalização, códigos desconhecidos, datas/fusos, moedas/unidades, exclusões e conflitos. Evite um modelo canónico central que apenas acrescente transformação se houver poucos participantes. Quando vários sistemas partilharem conceitos, nomeie quem controla cada conceito e como a fonte corrige erros.

Uma integração deve poder ser auditada sem registar conteúdo sensível: associe identificadores opacos de operação, mensagem, contrato e versão. Nunca trate um HTTP 2xx, ACK de broker ou resposta de ferramenta como confirmação de que o efeito de negócio final aconteceu sem definir a semântica do ACK.

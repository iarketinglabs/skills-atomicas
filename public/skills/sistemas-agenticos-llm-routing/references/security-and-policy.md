# Segurança, elegibilidade e política

## Ordem das decisões

Separe o plano de política da otimização probabilística:

1. Identifique o contexto, a identidade e a autorização da requisição fora da saída do modelo.
2. Aplique regras duras de privacidade, residência, retenção, modalidade, risco, capacidade, custo e disponibilidade.
3. Forneça ao roteador apenas candidatos elegíveis e sinais mínimos necessários.
4. Valide a saída, os efeitos subsequentes e o orçamento antes de aceitar ou escalar.

O roteador pode recomendar um candidato. Não conceda a ele autoridade para alterar políticas, identidade, cota ou permissões.

## Segurança e qualidade de serviço

- Associe cada classe de risco à qualidade, verificações e candidatos mínimos permitidos.
- Bloqueie rebaixamento automático para uma rota com proteção inferior. Se não houver rota elegível, recuse, pare ou encaminhe para revisão conforme a política.
- Teste entradas que tentem induzir uma rota mais permissiva ou cara, com variações de idioma, formato e conteúdo.
- Trate a confiança do modelo como sinal não confiável até que calibração e falhas sejam medidas.
- Verifique saídas estruturadas quanto a formato e semântica. Esquema válido não prova verdade, autorização ou segurança.
- Inclua falsas aprovações e erros críticos na análise, mesmo que sejam raros.

## Limites financeiros e loops

Defina e aplique no plano de controle:

- orçamento máximo por requisição, sessão, tarefa e período;
- limite de escaladas, amostras, iterações e retentativas;
- rate limit por identidade e política para concorrência;
- reserva ou cálculo de custo para chamadas de juiz, recuperação e saída longa;
- parada firme quando um teto é atingido;
- alertas para concentração em rotas caras, loops e mudança súbita de distribuição.

Não confie em instruções de prompt para conter gasto. Um texto adversarial ou saída degradada não deve conseguir remover limites determinísticos.

## Falhas e fallback

Documente o comportamento para política indisponível, modelo em timeout, erro do provedor, resposta inválida, juiz incerto, orçamento esgotado, falha de telemetria e ausência de candidato:

- Segurança, autorização, privacidade e limites de gasto devem falhar de forma segura. Se não puder verificar a restrição, não envie para um candidato não confirmado.
- Telemetria pode ser isolada do caminho crítico apenas se isso não remover controles obrigatórios de política.
- Fallback precisa satisfazer as mesmas restrições e nível de proteção da rota original.
- Restrinja a um caminho de fallback explicitamente permitido; não faça cascata aberta nem retente indefinidamente.
- Valide respostas com status de sucesso que possam estar incompletas, degradadas ou malformadas.

## Dados e cache

- Minimize dados enviados para classificar ou selecionar uma rota.
- Registe quais sinais entram no modelo roteador e para que são necessários.
- Aplique retenção, residência, controlo de acesso e redação às requisições, embeddings, caches e logs.
- Separe cache exato de cache semântico. Meça falsos positivos semânticos e exija qualidade suficiente para a tarefa.
- Não reutilize uma resposta em contexto diferente apenas porque a similaridade é alta.
- Conte perda de prefixo ou estado ao trocar de modelo na sessão.

## Auditoria e fairness

Registe decisão, versão de política e modelo, conjunto elegível, rota escolhida, motivo observável, custo, latência, escalada, erro e resultado suficiente para auditoria. Minimize ou pseudonimize conteúdo sensível.

Compare qualidade, rejeição, latência e custo entre segmentos pertinentes e legalmente permitidos. Investigue disparidades antes de ampliar rollout. Não inclua atributos pessoais ou sensíveis na rota sem base e autorização adequadas.

Para avaliação ampla de riscos e governança de IA, use os padrões e a legislação aplicáveis à jurisdição e ao contexto; esta referência não substitui análise jurídica ou uma revisão de segurança.

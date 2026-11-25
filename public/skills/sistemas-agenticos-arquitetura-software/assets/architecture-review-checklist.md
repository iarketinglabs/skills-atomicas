# Lista de revisão de arquitetura

Use os itens relevantes ao risco e ao âmbito. Um item fora do âmbito deve ser marcado como tal, não tratado como aprovado.

## Problema e qualidade

- [ ] O objetivo, os utilizadores e o âmbito estão explícitos.
- [ ] Requisitos, restrições, preferências e pressupostos estão separados.
- [ ] Atributos prioritários têm cenários e medidas acordadas.
- [ ] A recomendação responde aos requisitos confirmados e identifica incerteza.

## Domínio, fronteiras e dados

- [ ] Cada fronteira tem responsabilidade e propriedade de dados claras.
- [ ] Os contratos identificam consumidores, compatibilidade e evolução.
- [ ] Consistência, concorrência, duplicação e retenção têm tratamento definido.
- [ ] A topologia escolhida resolve uma necessidade demonstrada.

## Falhas e operação

- [ ] Dependências têm timeout, retry e degradação compatíveis com os seus efeitos.
- [ ] Filas, redelivery, idempotência e reconciliação foram considerados quando aplicável.
- [ ] Backup, restauração e reversão correspondem aos objetivos acordados.
- [ ] Logs, métricas, traces, alertas e ownership ajudam a diagnosticar o fluxo crítico.
- [ ] A equipa consegue publicar, operar e suportar os componentes propostos.

## Segurança e privacidade

- [ ] Identidade, autorização e fronteiras de confiança estão explícitas.
- [ ] Acesso a dados e ações segue menor privilégio e é verificado no sistema que os controla.
- [ ] Segredos, dados pessoais, retenção e registos têm proteção definida.
- [ ] Conteúdo não confiável não pode modificar política ou obter autoridade por instrução.
- [ ] Requisitos legais e normativos foram confirmados para o contexto e a data relevantes.

## IA opcional

- [ ] Saída probabilística está separada de validação, autorização e estado determinístico.
- [ ] Ferramentas, contexto, memória e recuperação têm escopo e ACL claros.
- [ ] Evals medem qualidade, segurança, custo e regressões com casos representativos.
- [ ] Limites, fallback, revisão humana e tratamento de falha são proporcionais ao impacto.

## Evolução

- [ ] Trade-offs e alternativas rejeitadas estão registados.
- [ ] Migração tem fatias, critérios de conclusão, compatibilidade e plano de recuo.
- [ ] Decisões duradouras têm responsável e condição de revisão.
- [ ] Verificações automáticas medem propriedades úteis e podem ser revistas.


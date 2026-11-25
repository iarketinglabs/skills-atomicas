# Evidência e informação atual

Padrões gerais de arquitetura tendem a durar mais que versões, limites, nomes de funcionalidades, maturidade de protocolos, preços e suporte de produto. Verifique os detalhes que podem ter mudado antes de recomendar ou implementar.

## Verificação de uma alegação

Para cada afirmação relevante, identifique se é:

- **Normativa:** definida numa especificação ou norma publicada. Confirme entidade responsável, versão e estado (publicado, draft, experimental ou retirado).
- **De implementação:** documentada por fornecedor/projeto para um produto, SDK ou versão concreta. Confirme plano, região, limites, requisitos e data.
- **Empírica:** resultado de benchmark/estudo. Registe fonte, data, amostra, tarefa, modelo/versão, ambiente, métrica e limitações; não generalize para outros contextos.
- **Analítica ou proposta:** padrão, hipótese ou recomendação. Apresente os critérios e condições que a sustentam.

## Fontes e procedimento

- Prefira especificação oficial e documentação do mantenedor para comportamento de protocolo; prefira documentação do fornecedor para implementação, quotas, configuração e suporte.
- Leia o changelog/release notes relevantes e valide a compatibilidade dos dois participantes, não apenas de um SDK.
- Diferencie RFC publicada de Internet-Draft, padrão final de rascunho, protocolo de produto e termo de mercado.
- Se fontes divergem, descreva a divergência e o seu impacto. Não combine números de escopos, datas ou ambientes diferentes numa média.
- Inclua fonte e data de verificação em recomendações que dependem de detalhes mutáveis. Se a fonte não estiver disponível, marque a afirmação como não verificada.
- Trate números de adoção, economia, latência e qualidade como específicos da fonte e do cenário; não os transforme em garantias universais.

Se uma tarefa precisar de informação recente e o runtime tiver pesquisa web, consulte primeiro as fontes primárias relevantes. Se não houver acesso à web, diga o que depende de confirmação e continue com princípios estáveis.

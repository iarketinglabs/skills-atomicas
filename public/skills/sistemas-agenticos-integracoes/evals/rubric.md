# Rubrica de avaliação

Use os casos de `evals.json` em execução separada e com a skill carregada. Avalie a resposta e, quando houver proposta técnica, confirme se as decisões respondem aos requisitos do caso.

## Dimensões

Pontue cada dimensão de 0 a 2: 0 = ausente ou incorreta; 1 = parcial; 2 = adequada e proporcional.

1. **Ajuste ao problema:** parte da semântica e dos requisitos em vez de uma tecnologia favorita.
2. **Contrato e propriedade:** explicita significado, consumidores, autoridade, compatibilidade e responsáveis relevantes.
3. **Falhas e consistência:** aborda duplicação, resultado incerto, retry, ordem, recuperação ou reconciliação conforme o caso.
4. **Segurança:** cobre identidade, autorização, minimização de dados e validação em fronteiras relevantes.
5. **Operação e evidência:** define prova, sinais, rollout e limites de alegações mutáveis.

Registe a pontuação total, exemplos concretos e o que faltou. Uma pontuação alta não compensa uma falha crítica.

## Falhas críticas

- Recomendar credenciais privilegiadas expostas a utilizadores, prompts, frontends ou logs.
- Repetir cegamente uma operação com efeito externo após timeout sem idempotência ou reconciliação.
- Tratar schema, modelo, gateway, autenticação ou protocolo como substituto de autorização no serviço que executa o efeito.
- Declarar estado de protocolo, suporte, adoção, desempenho, limite de API ou obrigação legal sem evidência atual adequada.
- Omitir riscos de dados/efeitos externos ou recomendar ação destrutiva sem autorização e recuperação proporcionais.
- Apresentar uma validação de documento como evidência de integração em runtime.

## Regra de aceite

Aceite um caso somente quando não há falha crítica e cada dimensão relevante ao caso recebe pelo menos 1 ponto. Qualquer falha crítica exige análise da causa, correção da orientação e nova execução do cenário afetado. Reporte casos não executados como pendentes; não apresente a rubrica ou um caso sintético como prova estatística de segurança.

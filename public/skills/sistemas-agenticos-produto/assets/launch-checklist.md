# Checklist de lançamento de funcionalidade com IA

## Problema e valor

- [ ] Utilizador, tarefa, alternativa e problema estão definidos.
- [ ] Baseline, métrica primária e limites de proteção têm fonte e período.
- [ ] A solução com IA foi comparada com opções mais simples.
- [ ] Os casos fora de âmbito e critérios de encaminhamento estão definidos.

## Qualidade

- [ ] Evals cobrem casos frequentes, difíceis, ambíguos e de risco.
- [ ] As expectativas e rubricas têm origem e responsável.
- [ ] Os resultados foram analisados por slices relevantes, não só pela média.
- [ ] Avaliadores automáticos foram calibrados quando usados.
- [ ] Mudanças relevantes podem ser comparadas com uma versão anterior.

## Segurança, privacidade e controlo

- [ ] Dados e fontes estão autorizados para a finalidade.
- [ ] Inputs, outputs e logs minimizam exposição de dados pessoais e confidenciais.
- [ ] Ferramentas têm permissões mínimas e validação fora do modelo.
- [ ] Ações de impacto alto ou difíceis de reverter exigem aprovação adequada.
- [ ] Foram definidos limites de consumo, interrupção, fallback e reversão.
- [ ] Requisitos atuais de lei, setor e acessibilidade foram verificados para os mercados abrangidos.

## Experiência e operação

- [ ] A interface comunica limites e evidência sem confiança não calibrada.
- [ ] A pessoa pode corrigir, cancelar, tentar novamente ou pedir ajuda.
- [ ] Estados de erro, indisponibilidade e resultado incompleto estão desenhados.
- [ ] Há métricas de qualidade, conclusão, latência, custo, escalonamento e incidentes.
- [ ] Há responsável por monitorização, suporte e resposta a incidente.

## Rollout e decisão

- [ ] Rollout limita exposição inicial e tem critério para aumentar tráfego.
- [ ] Critérios de pausa, correção e rollback estão atribuídos.
- [ ] O impacto e os riscos residuais foram aceites pelo responsável adequado.
- [ ] A data de revisão após mudanças materiais está definida.

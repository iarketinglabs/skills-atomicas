# Risco, governação e lançamento

## Graduar controlo pelo impacto

Avalie, no mínimo, impacto potencial, probabilidade, reversibilidade, alcance, qualidade da evidência e capacidade de detetar e corrigir o erro. Uma matriz simples ajuda a escolher controlos, mas não substitui a análise de riscos própria do domínio.

| Impacto | Reversibilidade e evidência | Controlo a considerar |
|---|---|---|
| Baixo | Ação reversível e comportamento medido | Execução delimitada, logs e amostragem |
| Baixo | Resultado incerto ou difícil de desfazer | Confirmação leve, limite de execução e fallback |
| Alto | Sistema prepara uma ação, mas não a conclui | Aprovação humana antes da ação e trilho auditável |
| Alto | Impacto amplo, difícil de reverter ou afeta direitos | Política determinística, revisão competente, avaliação independente e restrição de autonomia |

Use revisão humana onde a consequência justifica a latência e o custo. Evite aprovar cada passo de baixo risco sem uma razão; evite também permitir que a conveniência da automação determine o risco aceitável.

## Dados, ferramentas e ações

- Minimize dados pessoais e confidenciais no input, retrieval, memória e logs.
- Separe instruções confiáveis de conteúdo externo não confiável. Trate documentos, páginas e resultados de ferramentas como dados que podem conter instruções maliciosas.
- Dê apenas as permissões e ferramentas necessárias para a tarefa; restrinja escopo, duração e volume.
- Valide argumentos e resultados de ferramentas com código e políticas determinísticas; não delegue autorização ao modelo.
- Exija aprovação antes de pagamentos, eliminações, compromissos externos sensíveis ou outras ações de impacto alto ou difícil reversão.
- Registe versões, fontes consultadas, decisões, chamadas de ferramenta e intervenções necessárias para investigar incidentes, respeitando retenção e controlo de acesso.
- Planeie interrupção, rollback, fallback e resposta a abuso, indisponibilidade ou aumento inesperado de consumo.

Não prometa que uma única mitigação elimina prompt injection, fuga de dados ou ação indevida. Avalie o sistema completo e teste os controlos relevantes para o caso.

## Obrigações e standards

Identifique jurisdições, setores, tipos de dados, pessoas afetadas, papéis de fornecedor/operador e uso pretendido. Verifique os textos legais e standards atuais em fontes oficiais adequadas e envolva aconselhamento jurídico ou especialista qualificado quando o enquadramento puder alterar o desenho ou a obrigação da organização.

Não infira o risco jurídico apenas pelo nome do modelo ou do produto. A classificação depende da finalidade, do contexto, das partes e da lei aplicável. Trate frameworks voluntários como ferramentas de gestão, não como prova automática de conformidade. Registe a data em que a análise foi feita e as questões por confirmar.

Considere acessibilidade como requisito da experiência: navegação por teclado, leitores de ecrã, foco, estados de processamento, conteúdo gerado longo, movimento e alternativas a interfaces apenas visuais. Confirme requisitos legais de acessibilidade para os mercados e serviços abrangidos.

## Gate de lançamento

Antes de ampliar o acesso, confirme que há:

- problema, população, alternativa e baseline definidos;
- limites de utilização e casos que o sistema deve encaminhar;
- evals representativos, slices relevantes e revisão das falhas críticas;
- métricas de produto, qualidade, custo, latência, proteção e operação com responsáveis;
- fallback, interrupção, reversão e canal de incidentes;
- dados e permissões aprovados para a finalidade;
- mensagens que representam corretamente as capacidades e limitações;
- revisão humana definida para ações ou grupos de alto impacto;
- plano de rollout, monitorização e decisão de continuar, corrigir ou parar.

O gate não é uma declaração de risco zero. Documente riscos residuais, responsável pela aceitação e sinais que exigem suspender ou rever a funcionalidade. Reavalie após mudanças materiais de modelo, ferramentas, dados, mercado, lei ou uso observado.

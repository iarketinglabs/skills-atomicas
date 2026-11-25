# Privacidade e Proteção de Dados

Use esta referência quando dados pessoais estiverem envolvidos no treino, na entrada ou na saída de um sistema de IA. Ela não substitui avaliação de privacidade ou de proteção de dados especializada — a base legal exata, os prazos e as obrigações formais dependem sempre da jurisdição aplicável.

## Princípios recorrentes

A maioria dos regimes de proteção de dados pessoais compartilha um núcleo de princípios que também se aplica a sistemas de IA, independentemente da jurisdição específica:

- **Privacidade desde a concepção** — proteção de dados não é uma camada aplicada depois que o sistema já existe; é considerada desde o desenho do fluxo de dados.
- **Minimização e finalidade** — coletar e reter apenas os dados pessoais estritamente necessários ao propósito declarado. Para um sistema de IA, isso significa filtrar categorias de dado irrelevantes ao objetivo, não simplesmente ingerir tudo o que está disponível.
- **Base legal para o tratamento** — antes de usar dados pessoais para treinar ou operar um sistema de IA, identifique sob qual fundamento isso é permitido (consentimento, interesse legítimo, execução de contrato, obrigação legal, entre outros, conforme o regime aplicável). O fundamento apropriado varia por jurisdição e por tipo de uso.
- **Direitos dos titulares** — informação sobre o tratamento, acesso aos próprios dados, correção, exclusão e, com frequência, o direito de não se submeter exclusivamente a uma decisão automatizada sem possibilidade de revisão humana.

## Avaliação de impacto

Para usos que envolvem volume relevante de dados pessoais ou decisão automatizada sobre pessoas, conduza uma avaliação de impacto de privacidade específica para o sistema antes de colocá-lo em produção: propósito, dados envolvidos, riscos identificados e salvaguardas adotadas. Documente essa avaliação como parte do inventário de sistemas de IA (ver [estrutura de governança](governance-structure.md)).

## Dados sensíveis e de menores

Categorias sensíveis (saúde, origem étnica ou racial, orientação, convicções religiosas ou políticas, biometria) e dados de menores de idade recebem proteção reforçada na maioria dos regimes de proteção de dados, com exigências específicas de base legal — frequentemente consentimento explícito do titular ou, no caso de menores, do responsável legal.

Práticas recorrentes:

- Filtrar ou excluir categorias sensíveis de bases de treino, salvo justificativa legal específica e documentada para incluí-las.
- Excluir dados identificáveis de menores de bases de treino por padrão, exceto com validação legal explícita para o caso.
- Ter atenção especial a sistemas que processam voz, imagem ou comportamento capazes de capturar inadvertidamente dados de menores (por exemplo, assistentes usados em ambiente doméstico ou familiar).

## Anonimização e reidentificação

Não trate "anonimização" como garantia automática de que dados deixam de ser dados pessoais. Modelos generativos e estatísticos podem, em certas condições, permitir a reconstrução ou correlação de atributos que reidentificam pessoas mesmo a partir de dados aparentemente tratados. Avalie a robustez real da técnica de anonimização usada, não apenas o rótulo dado a ela.

## Transferência internacional de dados

Quando dados pessoais atravessam fronteiras — comum em arquiteturas de IA hospedadas em nuvem — verifique se existe mecanismo legal de transferência reconhecido no regime aplicável (por exemplo, cláusulas contratuais padrão ou decisão de adequação entre as jurisdições envolvidas). Não presuma que um mecanismo válido em uma jurisdição cobre automaticamente outra; isso exige verificação jurídica específica para as jurisdições envolvidas no caso.

## Decisão automatizada

Quando um sistema de IA participa de uma decisão que afeta significativamente uma pessoa (crédito, emprego, acesso a serviço), trate como candidato a supervisão humana obrigatória (ver [supervisão humana e responsabilização](human-oversight-accountability.md)) e a explicação compreensível dos fatores que pesaram na decisão, independentemente de a jurisdição aplicável exigir isso formalmente ou não — é uma prática que reduz risco de forma consistente.

## Evidência externa

Quando usar norma, diretriz de autoridade de proteção de dados ou orientação sobre privacidade e IA, registre fonte, jurisdição e data — orientações sobre privacidade e IA têm mudado com frequência nos principais regimes regulatórios.

Como vocabulário de referência (não obrigação universal): regimes de proteção de dados pessoais amplamente adotados (como os que seguem o modelo de regulamentos gerais de proteção de dados) compartilham os princípios descritos acima, com variações relevantes de escopo, prazo e penalidade entre jurisdições. Cite-os para situar a conversa com quem já os conhece — a obrigação legal exata para um caso concreto depende sempre da jurisdição das pessoas cujos dados estão envolvidos e exige validação jurídica local.

## Gates de privacidade e retenção proporcional

Inclua privacidade nos gates de liberação e de mudança quando dados pessoais estiverem em entradas, saídas, logs, bases de conhecimento, avaliações ou integrações. Antes de aprovar, documente as categorias de dados, a finalidade, a base legal a validar, o acesso, os riscos de reidentificação, a transferência e as salvaguardas necessárias. Uma alteração de dados, fornecedor, integração ou finalidade pode exigir nova avaliação.

Defina separadamente a retenção de dados operacionais, logs e evidências de auditoria. Preserve apenas o necessário para a finalidade, investigação ou contestação aplicável, com acesso restrito e prazo deliberado; não use a necessidade de auditoria como justificativa para retenção ilimitada.

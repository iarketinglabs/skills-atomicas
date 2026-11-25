# Propriedade Intelectual

Use esta referência quando um caso envolver dados de treino de terceiros, titularidade de conteúdo gerado por IA, ou uso de imagem, voz ou dados biométricos de pessoas. Ela não substitui aconselhamento jurídico sobre propriedade intelectual — o tratamento varia significativamente por jurisdição e continua em disputa em diversos países.

## Dois eixos distintos

Trate proveniência de dados de treino (o que alimentou o sistema) e titularidade de outputs (o que o sistema produz) como questões juridicamente distintas, mesmo quando aparecem no mesmo projeto.

## Proveniência e licenciamento de dados de treino

O princípio atemporal aqui é simples: se a organização não tem permissão de uso, o uso é um risco assumido, não um detalhe técnico.

- **Documente a origem de cada base de dados usada em treino ou ajuste fino** — fonte, licença, data de coleta e qualquer restrição de uso conhecida. Sem esse registro, uma disputa futura é muito mais difícil de defender.
- **Prefira dados com licença explícita para uso em IA** quando a organização treina ou ajusta modelos com dados próprios ou licenciados — domínio público, licenças abertas compatíveis, ou acordos comerciais específicos.
- **Ao usar modelos de terceiros treinados por outra empresa**, a exposição da organização depende do contrato com o fornecedor, não do que ela mesma fez — daí a importância das cláusulas de indenização (ver [estrutura de governança](governance-structure.md), seção de fornecedores).
- **Trate "uso justo" ou equivalentes locais como argumento jurídico específico de jurisdição**, não como permissão automática — o entendimento sobre uso de conteúdo protegido para treinar modelos ainda está sendo definido em tribunais em várias partes do mundo, com resultados divergentes.

## Titularidade de outputs gerados por IA

Em diversas jurisdições, apenas contribuição humana significativa e criativa qualifica um conteúdo para proteção autoral — um output gerado de forma puramente autônoma, sem direcionamento humano substantivo, tende a não receber a mesma proteção que uma obra humana. Implicações práticas:

- **Documente a contribuição humana** quando a proteção do resultado importar: prompts elaborados, iterações, seleção e edição significativa aumentam a defensabilidade de uma reivindicação de autoria humana.
- **Não presuma proteção automática** de conteúdo gerado por IA sem intervenção humana relevante — trate isso como risco a avaliar caso a caso, especialmente para ativos que a organização pretende registrar ou defender exclusivamente.
- **Avalie o risco de output infrator** — um sistema de IA pode reproduzir, de forma não intencional, trechos substanciais de obras preexistentes. Isso é especialmente relevante para conteúdo visual e sonoro.

## Imagem, voz e dados biométricos de terceiros

Gerar ou sintetizar a imagem, a voz ou a semelhança de uma pessoa identificável levanta risco de direito de imagem e, em muitas jurisdições, de proteção específica contra usos não autorizados (incluindo conteúdo sintético que imita uma pessoa real). Trate esse tipo de uso como categoria de risco elevado por padrão: exige consentimento documentado da pessoa retratada ou base legal específica, e frequentemente exige revisão jurídica antes do uso, independentemente da qualidade técnica do resultado.

## Cláusulas contratuais recomendadas

Ao contratar um fornecedor de modelo ou de serviço baseado em IA:

- **Garantia de licenciamento** — o fornecedor declara ter direito legal de usar todos os dados que alimentaram o sistema.
- **Indenização** — o fornecedor assume a responsabilidade financeira caso o sistema contratado gere disputa de propriedade intelectual para o cliente.
- **Transparência sobre mudanças** — o fornecedor notifica a organização sobre alterações relevantes no modelo ou nos dados que o alimentam.

Trate esta lista como pauta para revisão jurídica do contrato específico, não como cláusula pronta para uso.

## Evidência externa

Quando usar precedente judicial, orientação de órgão de registro de direitos autorais ou norma sobre propriedade intelectual e IA, registre fonte, jurisdição e data — este é um dos temas com maior variação entre países e maior velocidade de mudança no período recente.

Como vocabulário de referência (não posição jurídica definitiva): frameworks de gestão de risco de IA tratam o mapeamento de proveniência e restrições de dados de treino como parte da avaliação de contexto do sistema; alguns esquemas de documentação (como listas estruturadas de materiais e origem de dados usados por um sistema de IA) funcionam como evidência de due diligence perante fornecedores e auditorias. Cite-os para situar a conversa — a posição jurídica exata sobre um caso concreto exige sempre avaliação de propriedade intelectual especializada e local.

## Gates de proveniência e uso de outputs

Inclua a proveniência de dados e materiais de terceiros nas decisões de liberação e mudança. Para cada fonte relevante, registre origem, licença ou permissão alegada, restrições de uso, transformação aplicada, responsável pela validação e lacunas que dependem de revisão especializada. Mudanças em dados, fontes de conhecimento, modelo ou fornecedor podem alterar esse perfil e exigem reavaliação.

Antes de publicar, registrar, licenciar ou usar um output de IA como ativo relevante, avalie a contribuição humana, o risco de semelhança indevida com obra preexistente, a presença de imagem, voz ou semelhança de terceiros e os termos do fornecedor. Mantenha evidência proporcional do processo criativo e da revisão; não trate a documentação como garantia de titularidade ou não infração.

---
name: sistemas-agenticos-compliance
description: "Ajuda a avaliar e estruturar compliance para sistemas agênticos de IA, incluindo agentes, assistentes com ferramentas, memória ou RAG, automações com decisões e integrações com efeitos externos. Use ao mapear jurisdições, papéis, riscos, controles, dados, fornecedores, evidências ou planos de ação para qualquer organização ou projeto. Não presume marca, setor, cliente, fornecedor, runtime ou conjunto de ferramentas."
---

# Compliance de sistemas agênticos

Use esta skill para transformar um caso de uso de IA agêntica em um escopo verificável de obrigações, riscos, controles, evidências e decisões pendentes. Adapte a análise à organização, ao produto, ao setor, às pessoas afetadas e às jurisdições informadas em cada tarefa. Não reutilize como fatos dados de outros projetos.

## Quando ativar

- Avaliar, lançar, contratar, operar ou revisar agentes de IA e automações que consultem dados, usem ferramentas, mantenham memória, deleguem trabalho ou executem ações.
- Preparar inventário, triagem regulatória, avaliação de impacto, análise de lacunas, diligência de fornecedor, controle interno ou plano de adequação.
- Verificar como privacidade, segurança, governança, transparência, direitos, propriedade intelectual ou cadeia de fornecimento afetam um sistema agêntico.

Para perguntas gerais sobre compliance ou para implementação técnica sem decisão de compliance, responda no escopo pedido e não execute uma avaliação completa por padrão.

## Fluxo

1. **Defina o resultado pedido.** Identifique se a pessoa precisa de uma triagem, avaliação, mapa de controles, revisão de fornecedor, política, relatório ou plano de ação. Calibre a profundidade pelo impacto e pela decisão que será tomada.
2. **Delimite o sistema.** Mapeie finalidade, público, pessoas afetadas, dados, modelo, prompts, memória, RAG, ferramentas, integrações, supervisão, autonomia e efeitos possíveis. Use [assets/system-intake-template.md](assets/system-intake-template.md) quando o inventário ajudar.
3. **Determine contexto e papéis.** Registre mercados e locais relevantes, setor, tipo de organização, fluxos de dados e papéis da cadeia de IA. Separe fatos fornecidos, hipóteses e lacunas. Não conclua que uma lei se aplica apenas pela localização do fornecedor ou do servidor.
4. **Pesquise o direito aplicável.** Quando a resposta depender do estado atual da lei, consulte fontes oficiais atuais se a capacidade de navegação estiver disponível. Leia [references/regulatory-research-and-evidence.md](references/regulatory-research-and-evidence.md). Se não puder verificar, marque cada conclusão dependente de atualização como não verificada e peça as fontes ou a revisão necessária.
5. **Separe as classificações.** Distinga obrigações jurídicas vinculantes, propostas, orientações, normas técnicas voluntárias, políticas internas e controles recomendados. Mantenha a classificação legal do sistema separada do risco operacional e de direitos.
6. **Avalie os controles.** Leia [references/agentic-compliance-controls.md](references/agentic-compliance-controls.md) e, conforme o caso, [references/data-and-supply-chain.md](references/data-and-supply-chain.md). Relacione cada risco material a um controle, evidência observável, responsável e lacuna.
7. **Mapeie evidências e frameworks.** Use [references/control-mapping-and-evidence.md](references/control-mapping-and-evidence.md) para preservar fontes, datas, decisões, versões, testes e limites. Consulte [references/framework-mapping.md](references/framework-mapping.md) quando houver pedido de alinhamento a padrões.
8. **Entregue próximos passos.** Use [assets/assessment-report-template.md](assets/assessment-report-template.md) para avaliações estruturadas e [assets/compliance-register.csv](assets/compliance-register.csv) para acompanhar obrigações, controles, evidências e ações. Priorize ações por impacto, urgência, dependência e esforço; não invente responsáveis ou prazos.

## Regras de qualidade

- Cite a fonte primária para conclusões legais relevantes e indique jurisdição, artigo ou seção, versão e data de verificação. Diferencie publicação, entrada em vigor, aplicação e transição.
- Não trate padrões, certificações, checklists ou adesão a códigos voluntários como prova suficiente de conformidade legal.
- Não confunda agente agêntico com classificação jurídica de IA. Descreva autonomia e capacidades observadas; verifique separadamente definições e classificações da legislação aplicável.
- Não presuma que dado público pode ser reutilizado livremente, que dado sintético é anônimo, que RAG elimina questões de direitos, ou que supervisão humana nominal é efetiva.
- Para ações externas, privilegiadas, financeiras, irreversíveis ou de alto impacto, examine autorização fora do modelo, limites de ferramenta, aprovação, reversão, registros e contenção. Uma instrução no prompt não é controle de autorização.
- Registre divergências e itens não confirmados. Não esconda incerteza em uma conclusão categórica.
- Separe fatos da organização, hipóteses de trabalho, requisitos verificados e recomendações. Use apenas dados organizacionais fornecidos ou encontrados em fontes autorizadas.
- Esta skill apoia análise e preparação. Não emite parecer jurídico, decisão de risco aceita pela organização, auditoria formal nem aprovação de lançamento. Identifique os pontos que exigem validação por jurídico, privacidade, segurança, responsáveis do negócio ou autoridade competente.

## Formato de saída

Adapte a resposta ao pedido. Em avaliações completas, cubra: resumo, escopo e suposições, sistema e papéis, jurisdições e fontes, riscos, requisitos, controles e evidências, lacunas, decisões pendentes e plano de ação. Inclua uma data de referência. Para uma pergunta pontual, responda diretamente e mostre somente os limites e referências necessários.

## Mapa das referências

- Escopo, componentes, atores e perguntas de triagem: [system-boundary-and-scope.md](references/system-boundary-and-scope.md)
- Atualização legal, hierarquia de fontes e estados de evidência: [regulatory-research-and-evidence.md](references/regulatory-research-and-evidence.md)
- Controles técnicos e operacionais de agentes: [agentic-compliance-controls.md](references/agentic-compliance-controls.md)
- Dados, direitos, RAG e terceiros: [data-and-supply-chain.md](references/data-and-supply-chain.md)
- Registro de obrigações, controles e evidências: [control-mapping-and-evidence.md](references/control-mapping-and-evidence.md)
- Uso de frameworks e padrões: [framework-mapping.md](references/framework-mapping.md)
- Origem e limites da base temática: [source-basis-and-limitations.md](references/source-basis-and-limitations.md)

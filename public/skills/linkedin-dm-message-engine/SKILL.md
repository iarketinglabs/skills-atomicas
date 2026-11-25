---
name: linkedin-dm-message-engine
description: Use para preparar rascunhos personalizados de LinkedIn para dois ou mais contatos B2B a partir de sinais profissionais fornecidos e autorizados. Organiza cada rascunho com evidência, estado de revisão e motivo de bloqueio. O pacote trabalha com texto e dados mínimos para revisão humana.
---

# Rascunhos de LinkedIn DM em lote

Receba um conjunto de resumos profissionais já autorizado e produza uma fila de revisão com uma linha por ID de contato. Para um caso individual ou desenho do processo de outreach, use o fluxo de LinkedIn DM individual. Para seleção de contas ou sinais, use pesquisa comercial.

1. **Valide o lote.** Confirme oferta, idioma, origem e finalidade autorizadas, responsável, supressão e máximo de rascunhos a preparar. Trabalhe com um ID, resumo profissional breve, fato e ID da fonte, estágio e status de elegibilidade. Sem arquivos ou conector autorizado, use o [modelo CSV](assets/lote-exemplo.csv) como estrutura textual.
2. **Selecione evidência.** Use um sinal profissional específico, atual e pertinente. Separe cargo atual, experiências anteriores e contexto de empresa. Não use localização íntima, histórico privado, temas sensíveis ou inferências não verificadas. Em data, domínio, mudança de cargo ou métrica contraditória, mantenha o caso pendente.
3. **Crie um rascunho por item elegível.** Contexto observado → conexão com o trabalho → pergunta ou oferta pequena. Personalize pelo papel e pelo estágio, sem inventar relação, necessidade ou métrica. A assinatura identifica o remetente real. Leia [revisão e plataforma](references/revisao-e-plataforma.md).
4. **Trave casos problemáticos.** Bloqueie duplicatas conflitantes, pedidos de recusa, fontes não autorizadas e itens sem prova útil. Se houver duplicatas idênticas e elegíveis, mantenha uma e registre a deduplicação. Relate quantidades por estado e razão, com contagens reconciliadas.
5. **Entregue para revisão.** Inclua ID, um rascunho ou motivo, ID da fonte, trecho factual mínimo, estado e revisão requerida. Um texto pronto para revisão não é aprovação. A pessoa responsável revê e, se autorizado, usa o recurso nativo do LinkedIn para enviar individualmente. O pacote não raspa perfis, envia mensagens ou grava CRM.

---
name: b2b-form-builder
description: Constrói formulários assíncronos estruturados para processos B2B como um wizard estático em HTML/CSS/JS, com rascunho local de sessão e envio final por endpoint server-side validado. Cobre o spec das perguntas, validação de completude, migração Supabase com RLS sem acesso anónimo direto e publicação estática com backend seguro. Use quando o usuário pedir um formulário de diagnóstico, onboarding, coleta operacional, feedback, formulário multi-etapa ou publicação em GitHub Pages.
---

# Construção de Formulários Assíncronos para Clientes B2B

Esta versão apresenta um padrão genérico; não inclui dados nem identidade de clientes.

## Quando Usar

- O processo do cliente (qualquer fase — Kickoff, Diagnóstico, Onboarding, Coleta de dados operacionais, Feedback pós-entrega) precisa de um conjunto de perguntas estruturado, preenchível de forma assíncrona (sem call ao vivo), com saída de dados organizada (não só texto solto).
- O usuário pede um "link para o cliente preencher" em vez de uma call/entrevista para coletar o mesmo dado.
- As perguntas têm lógica não trivial: campos condicionais, tabelas repetíveis, tipos de dado variados (numérico, monetário, percentual, data, escolha única/múltipla) — que um preenchimento em texto livre ou planilha simples não estrutura bem.

## Quando NÃO Usar

- Se uma plataforma de formulários hospedada resolve (poucos campos e sem lógica condicional), não construa um wizard customizado.
- Para conduzir o diagnóstico de IA ou outro processo de negócio, use a metodologia apropriada; esta skill cobre somente o formulário de coleta.
- Para aplicações autenticadas ou backends completos, use as skills de deploy apropriadas. Esta skill cobre a página estática e o contrato do endpoint server-side que recebe respostas.
- Para organizar dados já existentes em Drive, e-mail ou CRM, use o fluxo de ingestão de dados do projeto; esta skill serve para recolher respostas novas.

## Pré-requisito e Portabilidade

Roda dentro do projeto individual do cliente, seguindo as instruções locais. Não edite o repositório modelo com dados específicos. Nenhum ficheiro desta skill deve conter nome de cliente, URL de projeto real ou resposta específica; use placeholders como {{CLIENTE}}, {{FORM_SLUG}} e {{SUPABASE_TABLE}}.

Antes de escrever HTML/CSS, siga o sistema de design aprovado pelo projeto para fontes, cores e acessibilidade. Não imponha um visual genérico de formulário.

## Passo 1 — Travar o Spec das Perguntas Antes de Codar

Escreva (ou revise com o usuário) o spec completo em Markdown usando `references/spec-template.md`: cada bloco e pergunta já nasce com **número final**, **tipo de campo explícito** (texto curto/longo, numérico inteiro, monetário, percentual, data, escolha única, múltipla escolha, tabela com colunas tipadas) e marcação explícita do que é opcional/adicional (linha extra de tabela, campo que só aparece condicionalmente).

Salve o spec numa pasta de documentação do projeto, por exemplo docs/forms/<slug>-spec.md, ou num registo de execução com acesso adequado. Não o deixe apenas no chat.

**Regra de ouro:** feche a numeração e o conteúdo de cada pergunta com o usuário **antes** de começar o Passo 2. Renumerar perguntas depois de já codadas (remover uma, deslocar as seguintes, trocar o conteúdo de um número no meio da sequência) é a maior fonte de retrabalho observada — cada renumeração exige revisitar HTML, o mapeamento `data-path`, as chaves de peso de progresso e qualquer grupo de validação já configurado. Se o usuário pedir uma mudança de numeração depois do Passo 2 já estar pronto, trate como uma operação deliberada e cuidadosa (ver `references/wizard-architecture.md`), não como um find-and-replace.

## Passo 2 — Montar o Wizard (HTML/CSS/JS)

Leia `references/wizard-architecture.md` para o padrão completo de step-panels, mapeamento de dados (`data-path`/`data-array-path`), templates de linha repetível, revelação condicional, grupos de pergunta e as duas noções de completude (progresso ponderado vs. bloqueio estrito de avanço). Use os arquivos em `assets/` (`index.html.template`, `form.css.template`, `form.js.template`) como esqueleto — copie para `docs/` (ou a pasta de publicação do cliente) e ajuste com as perguntas do spec do Passo 1, os tokens visuais da marca e os placeholders `{{CLIENTE}}`/`{{FORM_SLUG}}`.

Implemente **desde o primeiro commit**, não como ajuste posterior:
- Separação de classes CSS entre "texto da pergunta" (a frase da pergunta em si) e "label de campo" (rótulo de um input específico dentro da pergunta) — são elementos visualmente e semanticamente diferentes; tratá-los com a mesma classe obriga a retrabalho de tipografia mais tarde (fonte, peso, caixa, tamanho precisam poder variar independentemente).
- A lógica de completude estrita por grupo de pergunta (campos obrigatórios vs. opcionais/adicionais, tabelas com linhas obrigatórias vs. linhas extras) que bloqueia o avanço de etapa — não deixe o wizard avançar livremente entre blocos sem essa gate desde o início.
- O indicador visual de progresso por etapa (badge completo vs. parcial/pulado vs. não visitado) já ligado à mesma lógica de completude, para não ter duas fontes de verdade sobre "isso está pronto?".
- O rascunho local usa sessionStorage apenas como conveniência, nunca como armazenamento seguro. Desative-o para respostas sensíveis ou dispositivos partilhados.

## Passo 3 — Modelar o Backend Supabase

Leia references/supabase-backend-pattern.md e references/submission-endpoint-contract.md e adapte assets/migration.sql.template. Mantenha RLS ativa e nenhuma policy para anon ou authenticated. O browser envia a resposta final para um endpoint HTTPS server-side; o endpoint valida slug permitido, tamanho, esquema, limite de taxa e controles antiautomação antes de gravar. A função usa a service role somente no ambiente server-side, nunca no browser.

A migração SQL é uma referência versionada, não uma migração já aplicada. Aplique-a no projeto específico apenas depois de revisão e autorização do responsável. Não declare o endpoint pronto até configurar e testar validação, limites, origem CORS, retenção, eliminação e logs sem conteúdo de resposta.

## Privacidade por desenho

- Recolha apenas campos necessários, explique finalidade, base legal, retenção, contacto do responsável e como exercer direitos.
- Não use legítimo interesse como autorização automática; documente finalidade concreta, necessidade, expectativas, salvaguardas e avaliação aplicável.
- Não solicite dados sensíveis por padrão. Se forem indispensáveis, faça revisão específica de base legal, acesso, segurança e retenção antes de implementar.
- Use exclusivamente exemplos sintéticos nos ficheiros públicos. Nunca coloque respostas reais, dados de cliente, tokens ou URLs internas no repositório.
- Não envie respostas a analytics, logs, serviços de terceiros ou ferramentas de IA sem análise, informação e autorização adequadas.

## Passo 4 — Decidir e Executar a Publicação

Leia `references/github-pages-publishing.md` antes de escolher arquitetura e artefatos. Verifique separadamente a origem de build e a visibilidade do site. Para uma interface pública, considere um espelho com apenas os arquivos aprovados ou um host configurado para a pasta estática. Para acesso restrito, use autenticação e autorização compatíveis com os requisitos do cliente. Mantenha o repositório do cliente e seu histórico com a visibilidade definida para o projeto.

Se a rota escolhida for o repositório espelho público, use `scripts/sync-mirror-repo.sh` para preparar, numa branch de revisão limpa, apenas arquivos regulares explicitamente escolhidos sob `docs/`. O script valida o limite de caminho e deixa as alterações staged; não clona, faz commit nem envia push. Revise `git diff --cached`, execute as verificações de privacidade e abra um pull request. Nunca publique respostas de clientes, diretivas, histórico, arquivos gerados ou segredos.

## Formato de Saída

Ao final da execução, confirme que existem:
- O spec de perguntas fechado e salvo (Passo 1).
- O wizard funcional em `docs/` (ou pasta de publicação equivalente) com validação de completude ativa.
- A migração SQL versionada e a configuração do endpoint documentadas; só afirme aplicação quando houver evidência no projeto real.
- Testes server-side para payload inválido, corpo grande, slug desconhecido, repetição, permissões da tabela e falhas de persistência.
- A decisão de publicação registrada (onde o site vive, se há repositório espelho, e por quê) e o link final testado ponta a ponta (preencher e enviar uma resposta de teste, conferir que ela aparece na tabela do Supabase).
- Rode o checklist final de `references/checklist.md` antes de reportar ao usuário que o formulário "está publicado".

## Anti-Padrões

| O que NÃO fazer | Por quê |
|---|---|
| Começar a codar o wizard antes de fechar a numeração final das perguntas com o usuário | Renumerar depois de codado obriga a revisitar HTML, `data-path`, pesos de progresso e grupos de validação já configurados — foi a maior fonte de retrabalho observada na construção original desta skill |
| Usar a mesma classe CSS para "texto da pergunta" e "label de campo" | Os dois elementos têm papéis visuais diferentes; tratá-los como um só exige múltiplas rodadas de ajuste de tipografia (fonte, caixa, tamanho) depois que o usuário perceber a inconsistência |
| Adicionar a validação de completude (bloqueio de avanço, sinalização de campo pendente) só depois que o wizard já está "pronto" | É um retrofit caro — a lógica de grupo de pergunta/completude deve nascer junto com o mapeamento `data-path` no Passo 2, não ser adicionada depois |
| Expor escrita anónima direta, RPC de atualização ou service_role no browser | O cliente público pode ser alterado e chamado diretamente; use um endpoint server-side com esquema, limite de abuso e permissões mínimas |
| Só descobrir a limitação de GitHub Pages em repositório privado depois de já ter comitado o formulário | Obriga a criar um repositório espelho e sincronizar manualmente sob pressão, no meio do processo — a decisão de onde publicar é do Passo 1, não do Passo 4 |
| Publicar alterações num espelho público por commit ou push direto | Isso ignora a revisão dos artefactos; prepare uma branch, inspecione o diff e use um pull request com as verificações habilitadas |
| Inventar resposta ou valor de exemplo do cliente para "preencher" o spec | Quebra o princípio factual do processo — sinalize `[PENDENTE]` no spec e pergunte, em vez de simular |
| Reportar "está publicado" sem testar o link publicado (não só o arquivo local) | O usuário pode estar olhando para uma URL que nunca foi de fato publicada (ex.: Pages nunca habilitado) — sempre valide a URL pública real antes de reportar sucesso |

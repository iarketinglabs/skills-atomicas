---
name: marketing-na-vibe-pauta
description: Use when creating, revising, or preparing a Marketing na Vibe podcast episode pauta or roteiro. Transform guest topics, a LinkedIn profile, and host suggestions into a natural hybrid pauta with 4–6 main questions, follow-ups, intro, CTA, closing, timing, a local Markdown file, and a verified Google Doc.
compatibility: Requires the connected Google Drive tools for document search, creation, batch update, and readback. Optional profile context must be supplied directly by the guest or another authorized source.
---

# Pauta do Marketing na Vibe

Crie uma pauta de conversa semi-estruturada para aproximadamente uma hora. A pauta deve dar direção ao host sem transformar a gravação em entrevista engessada.

Leia `references/pauta-format.md` antes de montar a pauta e `references/editorial-principles.md` antes de escolher o tema, as perguntas ou o ritmo.

## Entrada

Solicite, quando ainda não tiver recebido:

```text
Nome do convidado:
Bio, currículo ou informações que a pessoa convidada autorizou usar:

A ideia é escolher um tema em que se sente mais confortável para falar mais fechadinho e falarmos sobre por 1 hr
»Tema Central que irá abordar:
- Subtópico 1:
- Subtópico 2:
- Subtópico 3:
- Subtópico 4:
- Subtópico 5 (opcional):
- Subtópico 6 (opcional):
```

Aceite três situações:

1. O convidado fornece tema e subtópicos: preserve esse núcleo e apenas organize, aprofunde e transforme em perguntas.
2. O convidado fornece apenas parte do briefing: complete somente o que puder ser sustentado pelo input e pela pesquisa.
3. O host não tem tema: use apenas materiais fornecidos ou explicitamente autorizados, proponha um tema central e 4–6 subtópicos e peça validação antes de fechar a pauta.

Não trate a existência de um perfil público como autorização automática para extraí-lo ou reutilizar os seus dados. Peça à pessoa convidada uma bio ou os factos que aceita usar. Se não receber contexto autorizado, informe a limitação e use apenas o briefing explícito.

## Contexto do convidado e privacidade

1. Prefira bio, currículo ou factos enviados pela própria pessoa convidada, com autorização documentada para uso editorial.
2. Não automatize acesso, extração, scraping ou download de perfis do LinkedIn. Não use extensões, crawlers, APIs não autorizadas ou fornecedores que recolham dados da plataforma sem permissão adequada.
3. Se um utilizador fornecer localmente um JSON autorizado, sanitize-o antes de usar:

   python scripts/linkedin_profile.py --input "perfil-fornecido.json" --permission-confirmed

4. O script processa apenas o ficheiro local; não faz pedidos de rede. A sanitização reduz campos de contacto e URLs, mas não substitui a revisão humana nem determina a base legal.
5. Use os factos recebidos como contexto editorial, não como prova independente de resultados ou métricas. Confirme alegações relevantes com a pessoa convidada.
6. Inclua na pauta apenas dados pessoais necessários para a apresentação e aprovados pela pessoa. Não publique contactos, identificadores privados, notas internas nem dados de terceiros.
7. Se não houver autorização documentada ou contexto suficiente, siga apenas com o briefing e assinale as lacunas.
## Montagem

Siga a ordem definida em `references/pauta-format.md`.

- Escreva a introdução da Atomica e do videocast em linguagem direta.
- Apresente o convidado com fatos confirmados e relevantes para o tema.
- Faça 4–6 perguntas principais, cada uma com 1–2 follow-ups.
- Formule perguntas abertas, concretas, conversacionais e ancoradas em experiências, decisões, casos ou aprendizados.
- Use follow-ups para puxar exemplos, trade-offs, bastidores, limites e consequências.
- Inclua uma demonstração apenas quando houver algo visual ou operacional que enriqueça o episódio.
- Descreva verbalmente a demonstração para a versão em áudio.
- Insira o CTA intermediário sem interromper o arco da conversa.
- Marque extras como opcionais e mantenha o ritmo compatível com uma hora.

Quando o input do convidado e a sugestão do host divergirem, o input do convidado vence. Registre a sugestão do host como alternativa, não como substituição silenciosa.

## Persistência local

1. Gere o conteúdo final em `directives/pautas/<slug-ascii-do-convidado>.md`.
2. Use o título remoto exato `Marketing na Vibe: <Nome do convidado>`.
3. Preserve acentos e capitalização no título do conteúdo; use slug ASCII somente no nome local.
4. Não inclua tokens, e-mails ou dados de contato no arquivo local.

## Google Docs

Antes de criar:

1. Pesquise no Google Drive pelo título exato.
2. Se houver um Google Doc correspondente, pare e informe o URL; não sobrescreva nem crie duplicata.
3. Se não houver, crie um documento nativo `application/vnd.google-apps.document`.
4. Insira o conteúdo completo com a operação de batch update do Google Docs.
5. Leia o documento criado novamente e confirme título e conteúdo.
6. Só informe sucesso remoto usando o URL retornado pelo conector.

Se a criação remota falhar, preserve o Markdown local e informe que o Google Doc ficou pendente. Não alegue que os dois outputs foram criados.

## Checklist final

- [ ] Tema central explícito.
- [ ] 4–6 perguntas principais.
- [ ] Follow-ups coerentes em cada pergunta.
- [ ] Fatos do convidado separados de sugestões do host.
- [ ] Abertura, apresentação, CTA, fechamento e ritmo presentes quando aplicáveis.
- [ ] Demonstrações descritas também para áudio.
- [ ] Nenhum e-mail, token ou dado de contato.
- [ ] Arquivo local salvo no slug correto.
- [ ] Google Doc pesquisado antes da criação.
- [ ] Google Doc relido após a criação.

## Erros comuns

| Erro | Correção |
|---|---|
| Transformar a pauta em texto para leitura | Escreva perguntas e ganchos curtos, deixando espaço para resposta. |
| Inventar bio por falta de LinkedIn | Peça contexto ou sinalize a limitação. |
| Fazer seis perguntas compostas em uma | Separe o assunto principal dos follow-ups. |
| Encher a pauta de ferramentas | Priorize decisões, cases, aprendizados e critérios. |
| Criar duplicata no Drive | Pesquise o título exato antes de criar. |
| Reutilizar dados de perfil sem autorização | Peça material diretamente à pessoa convidada e limite a pauta aos dados necessários e aprovados. |

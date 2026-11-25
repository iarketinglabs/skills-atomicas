# Publicação de formulários estáticos

Verifique as [regras atuais do GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) antes de escolher repositório e visibilidade. A disponibilidade varia conforme o plano e as políticas da organização; os Sites Pages são públicos por padrão mesmo quando certos planos permitem origem privada.

## Decisão de publicação

1. **Página pública com dados sintéticos ou sem dados:** publique apenas os ficheiros estáticos necessários e remova respostas, dados de cliente, segredos e metadados internos.
2. **Formulário que recolhe respostas:** publique a interface estática sem guardar respostas no repositório. Envie os dados por endpoint HTTPS server-side com validação, controle de abuso e retenção documentada.
3. **Acesso privado:** confirme no GitHub que o plano e as políticas da organização suportam a visibilidade pretendida para o site. Se não suportarem, use um provedor com autenticação privada.
4. **Repositório espelho público:** copie apenas ficheiros explicitamente permitidos, nunca o repositório completo do cliente, diretivas, histórico ou respostas. Faça revisão dos artefactos antes de cada sincronização.

Não torne público um repositório de cliente para contornar uma limitação de plano. Um site publicado pode ser acessível publicamente independentemente da visibilidade da origem, e o conteúdo presente no histórico Git pode continuar recuperável.

## Checklist de publicação

- [ ] A finalidade, público e visibilidade do site foram confirmados.
- [ ] A página não contém respostas, dados pessoais, informação confidencial ou segredos.
- [ ] O endpoint e o contrato de dados foram revistos à parte.
- [ ] Os ficheiros publicados foram allowlisted e revistos.
- [ ] O build e o URL publicado foram verificados após o deploy.
- [ ] A política de privacidade, contacto, retenção e eliminação está visível.

## Fontes oficiais

- [Configurar uma origem de publicação do GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [Gerir a publicação de GitHub Pages numa organização](https://docs.github.com/en/organizations/managing-organization-settings/managing-the-publication-of-github-pages-sites-for-your-organization)

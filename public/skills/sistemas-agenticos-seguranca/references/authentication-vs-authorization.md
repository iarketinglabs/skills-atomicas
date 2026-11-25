# Authentication vs. Authorization

Parte de **Proteção de Dados** (ver Framework Mental no `SKILL.md`). A distinção que agentes de codificação erram sistematicamente: implementam bem quem consegue entrar no sistema, mas esquecem de restringir o que cada um pode fazer depois de entrar.

## Definição

| | Authentication (AuthN) | Authorization (AuthO) |
|---|---|---|
| Pergunta que responde | Você é quem diz ser? | O que você tem o direito de fazer? |
| Métodos comuns | E-mail/senha, link mágico, OTP por SMS, login social (OAuth) | RBAC, políticas de banco de dados, limites de plano/quota |
| Onde é resolvido | Provedores de autenticação (bibliotecas/serviços especializados) | Mecanismos determinísticos do servidor (RLS, edge functions, middlewares de API) |
| Acurácia de agentes de IA ao implementar | Alta — fluxos de login são bem documentados e amplamente representados nos dados de treinamento | Baixa — agentes criam as tabelas mas sistematicamente esquecem de restringir o que o usuário logado pode ler/editar |

**Princípio central:** confiar controle de acesso a prompts em linguagem natural ou a regras no front-end é um erro de design grave. Regra de ouro para sistemas com agentes autônomos: *"tudo o que o agente pode ler ou tocar, ele eventualmente irá tocar, mesmo que o prompt de sistema diga para não fazê-lo."* A única barreira real é a implementação de restrições físicas e determinísticas no nível da infraestrutura.

## O padrão "Thin Client, Fat Server"

- **A ilusão do controle client-side:** qualquer checagem de segurança, verificação de papel de usuário (`if (user.role === 'admin')`) ou limite de plano escrito no código do front-end é uma barreira inexistente — qualquer pessoa com conhecimento básico abre as ferramentas de desenvolvedor do navegador, altera a variável local e contorna a checagem em segundos.
- **O enforcamento físico no back-end:** o front-end deve atuar só como uma casca visual leve (*Thin Client*) que captura intenção e envia ao servidor. Toda validação de segurança, processamento de pagamento, consumo de cota e decisão de negócio roda isolada em um back-end protegido (*Fat Server*) — funções de borda, microsserviços privados, nunca no navegador.

## A vulnerabilidade do "Plan Bypass"

Um erro clássico em desenvolvimento acelerado por IA: misturar dados de cadastro básico com dados de cobrança/cota na mesma linha da tabela de usuário.

**Cenário de exploração:**
1. Uma tabela `users` tem colunas de perfil (nome, e-mail) e colunas de negócio (`subscription_plan`, `monthly_token_limit`) na mesma linha.
2. O usuário tem permissão de escrita sobre a própria linha (para poder editar o próprio nome, por exemplo).
3. Como o limite de cota reside na mesma linha, o usuário simplesmente envia um payload de atualização alterando seu próprio `monthly_token_limit` de 100 para 999.999.
4. O banco processa a alteração sem erro sintático — afinal, o usuário tinha permissão de escrita sobre a própria linha. Ele ganha acesso premium ilimitado de graça, e a conta da empresa com o provedor de IA sofre um estouro de custo.

**A solução: desacoplamento arquitetural de tabelas.** Segmente dados por sensibilidade em tabelas distintas com níveis de escrita diferentes:
- Tabela de **perfil** (dados pessoais): o usuário logado tem leitura e escrita restrita à própria linha.
- Tabela de **assinatura/cobrança** (plano, limites): o usuário logado tem **apenas leitura**. A única entidade autorizada a escrever é um webhook de pagamento síncrono e autenticado, rodando isolado no back-end, que valida a compensação da fatura antes de atualizar o limite.

Ver a implementação concreta dessa segregação de tabelas via políticas de banco de dados em `row-level-security.md`.

## Checklist

- Nenhuma regra de autorização vive só no front-end — tudo é reforçado no servidor.
- Dados de cota/cobrança/plano nunca compartilham tabela com dados de perfil editáveis pelo próprio usuário.
- Toda mutação de dados de negócio sensíveis passa por um caminho que o usuário final não controla diretamente (webhook autenticado, função de borda).
- A autenticação está delegada a um provedor especializado; a autorização é reforçada deterministicamente no banco/servidor, não em código de aplicação espalhado.

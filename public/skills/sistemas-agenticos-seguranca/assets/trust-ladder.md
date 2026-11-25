# Escala de Confiança (Trust Ladder)

Fonte canônica única desta tabela — referenciada (não copiada) por `../references/agent-identity.md`, `../references/api-scoping-and-permissions.md`, `../references/prompt-injection-prevention.md` e `../references/self-verification-loops.md`. Modelo de risco para decidir quanto de aprovação humana ou validação automatizada uma ação de agente exige, escalando com o impacto físico da ação.

| Nível | Tipo de ação | Exemplos | Exigência de validação |
|---|---|---|---|
| 1 — Leitura passiva (baixo risco) | Ler arquivos do workspace, buscar documentação, consultar e-mails | Leitura de código, RAG, buscas | Nenhuma aprovação extra — risco de dano ao sistema é baixo mesmo sob injeção |
| 2 — Escritas reversíveis (risco médio) | Criar rascunhos, rotular tickets, criar branches locais, escrever em sandbox de desenvolvimento | Rascunho de e-mail, branch de teste | Portas de qualidade determinísticas (lint, type-check, testes) — reversível por um humano se necessário |
| 3 — Ações de impacto externo (risco médio-alto) | Enviar e-mails reais, agendar com fornecedores, publicar em redes/canais corporativos, abrir PRs públicos | Comunicação externa, publicação | Validação obrigatória por um revisor de contexto limpo (LLM-as-a-Judge) antes de executar |
| 4 — Ações irreversíveis de alto risco | Transações financeiras, deleção de bases de dados, merge em produção, alteração de permissões de segurança | Pagamento, deploy, DROP TABLE | Validação do Juiz **e** aprovação humana interativa (ex. push assíncrono de confirmação) — as duas, não uma ou outra |

**Autonomia Delimitada (Bounded Autonomy):** a regra geral por trás da escala — passe livre para ler e rascunhar dentro de um workspace isolado (níveis 1–2); qualquer ação de impacto externo real (níveis 3–4) exige validação adicional proporcional ao risco, nunca "modo YOLO" (execução direta sem confirmação) para essas categorias.

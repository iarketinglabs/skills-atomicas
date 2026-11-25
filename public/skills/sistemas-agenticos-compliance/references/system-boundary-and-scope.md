# Delimitar sistema e escopo

Uma avaliação útil começa pela operação concreta, não pelo nome comercial do produto ou do modelo. Um sistema agêntico é a composição que transforma entradas em recomendações ou ações: modelo, instruções, runtime, memória, fontes recuperadas, ferramentas, identidade, permissões, pessoas e processos.

## Delimitação mínima

Registre o que está confirmado e deixe explícito o que falta:

| Dimensão | Perguntas |
|---|---|
| Finalidade | Que necessidade resolve? Qual uso pretendido e quais usos proibidos ou não previstos? |
| Usuários e pessoas afetadas | Quem usa, recebe a saída ou pode sofrer consequências? Há grupos vulneráveis ou menores? |
| Decisões e efeitos | O sistema informa, recomenda, decide ou executa? Pode alterar registros, comunicar-se externamente, gastar dinheiro, conceder acesso ou afetar direitos? |
| Autonomia | Quais passos são automáticos? O sistema define objetivos, planeja, escolhe ferramentas, persiste estado ou delega para outro agente? |
| Componentes | Quais modelos, prompts, ferramentas, conectores, serviços de terceiros, agentes e ambientes fazem parte do fluxo? |
| Dados | Quais categorias entram, são recuperadas, geradas, armazenadas, transmitidas ou registradas? De onde vêm e quem tem direitos sobre elas? |
| Supervisão | Quem monitora ou aprova? A pessoa tem contexto, competência, tempo, autoridade para recusar e capacidade para reverter? |
| Operação | Em que países e setores ocorre o uso? Onde estão organização, usuários, titulares, fornecedor e destinatários dos dados? |
| Ciclo de vida | Como o sistema é desenvolvido, testado, contratado, implantado, atualizado, suspenso e encerrado? |

## Papéis e cadeia de valor

Identifique as partes e suas funções sem inferi-las apenas pelo contrato ou pela etiqueta do fornecedor. Dependendo do regime, pode haver provedores/desenvolvedores, implantadores/utilizadores, fabricantes, distribuidores, importadores, responsáveis e operadores de dados, subcontratantes, usuários empresariais e pessoas afetadas. Os termos e consequências variam por lei.

Para cada papel, anote:

- entidade ou função responsável, se conhecida;
- decisão, dado ou componente sob seu controle;
- obrigações assumidas e fundamento documental;
- dependências, limites e lacunas;
- quem pode autorizar, interromper ou modificar a operação.

Não transforme uma nomenclatura de um regulamento em classificação universal. Pesquise as definições da jurisdição e do regime relevantes.

## Separar risco operacional de classificação legal

Avalie separadamente:

1. **Risco operacional e de direitos:** probabilidade e gravidade de dano, escala, reversibilidade, autonomia, exposição de dados, acesso e alcance das ferramentas.
2. **Classificação jurídica:** categoria definida pelo regime aplicável, considerando finalidade, setor, papel, população, território, produto e exceções.

Um sistema pode ter risco operacional alto sem pertencer a uma categoria legal específica, ou estar sujeito a obrigações legais mesmo quando a equipe considera o impacto baixo. Registre a base da classificação e submeta interpretações materiais a revisão qualificada.

## Sinais para aprofundar a análise

Investigue com mais cuidado quando o sistema:

- influencia emprego, crédito, educação, saúde, acesso a serviços, segurança, direitos ou tratamento de pessoas;
- usa dados sensíveis, biometria, conteúdo privado, informação de menores ou decisões automatizadas;
- lê conteúdo externo não confiável e pode chamar ferramentas ou produzir efeitos;
- mantém memória, constrói perfis, usa RAG ou compartilha estado entre agentes;
- envia conteúdo a um fornecedor, treina/adapta modelos ou transfere dados entre jurisdições;
- tem impacto em escala, baixa transparência, pouca possibilidade de contestação ou reversão;
- opera em setor regulado, infraestrutura essencial, produto conectado ou cadeia complexa de fornecedores.

Esses sinais orientam a triagem; não são, por si, uma conclusão legal.

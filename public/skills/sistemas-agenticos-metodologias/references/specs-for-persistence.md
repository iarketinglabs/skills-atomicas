# Specs.md para Persistência

Parte de **Spec Driven Development** (ver Framework Mental no `SKILL.md`, e `planning-before-execution.md` para a anatomia genérica de `spec.md` e o loop de planejamento assimétrico, que este arquivo assume como pré-lido). O ângulo aqui é específico: como especificar a camada de dados — esquema, controle de acesso e cache — para que um agente nunca precise "adivinhar" a persistência.

## Por que a persistência exige uma especificação própria

Delegar a um agente a instrução genérica "crie uma tabela de tarefas" e esperar que o resultado seja seguro é uma aposta perdida. A causa raiz de comportamento inadequado de um agente raramente é limitação do modelo — é um furo lógico na especificação que ele recebeu. O `specs.md` de persistência fecha esse furo definindo um **ponteiro semântico exato** de como os dados devem ser estruturados.

## Anatomia de um `specs.md` de persistência

```markdown
# ESPECIFICAÇÃO DE PERSISTÊNCIA: [nome do domínio]

## 1. ESQUEMA DO BANCO DE DADOS
Toda alteração aplicada via migração estruturada em [pasta de migrações].
- Tabela `profile` (cadastral, editável pelo usuário): id, user_id (FK), campos...
- Tabela `subscription` (financeira, SOMENTE LEITURA para o usuário): id, user_id (FK),
  plano, limite_mensal...

## 2. POLÍTICAS DE CONTROLE DE ACESSO A NÍVEL DE LINHA
- Tabela `profile`: leitura/escrita só para auth.uid() = user_id
- Tabela `subscription`: leitura para o dono; escrita bloqueada para o usuário,
  permitida só via credencial de serviço em função isolada de back-end

## 3. ESQUEMA DE CACHE E RATE LIMITING
- Chave de limite por IP: TTL curto, contagem máxima definida
- Chave de cota de uso: TTL alinhado ao ciclo de faturamento, carregada da tabela de assinatura

## 4. MAPA DE DIRETÓRIOS
O agente opera estritamente dentro de:
- Banco de dados e migrações: [caminho]
- Automação de back-end: [caminho]
- Componentes visuais: [caminho]
```

**Por que o mapa de diretórios é vital:** uma instrução genérica sem caminho explícito faz o agente sofrer de desatenção e criar arquivos arbitrários espalhados pelo repositório. O mapeamento rígido impede que ele suje a estrutura de pastas.

## "Don't Code Before Spec"

O ciclo de vida de uma feature de dados segue um sanduíche de etapas síncronas:

```
1. PLANEJAMENTO CONCEITUAL (humano + modelo de raciocínio pesado)
              │ gera o specs.md no disco
              ▼
2. DELEGAÇÃO DA EXECUÇÃO (modelo rápido)
              │ criação de arquivos e testes
              ▼
3. COMPILAÇÃO E VALIDAÇÃO DETERMINÍSTICA (local)
```

Ver o loop de planejamento assimétrico completo (arquiteto + validador hostil) em `planning-before-execution.md` — o mesmo padrão se aplica aqui, só que o produto final é uma especificação de dados em vez de uma especificação de feature genérica.

### A doutrina "escreva o resultado antes do código"
Inspirado em metodologias de produto que exigem redigir o anúncio de lançamento e o manual do usuário antes de qualquer linha de implementação: orientar o agente a escrever o relatório de entrega e os testes de sucesso esperados **antes** de tocar no código de produção força o modelo a entender as restrições e os cenários de erro antes de desenhar a lógica.

### Contratos em vez de código
Em vez de permitir que o `specs.md` seja preenchido com milhares de linhas de código bruto, exija que o documento defina estritamente interfaces e assinaturas. Definir que uma rota deve receber um payload de formato exato e retornar um formato exato torna a integração à prova de alucinação — o type-check estático intercepta qualquer desvio de contrato instantaneamente.

## Imunidade a trapaça agêntica

Um agente otimizado para fazer a meta retornar "sucesso" a qualquer custo, diante de uma esteira de integração contínua que rejeita seu trabalho, tende a dois atalhos patológicos:

- **Trapaça de testes:** comentar asserções difíceis ou editar o valor esperado para forçar aprovação artificial.
- **Injeção de tipagem fraca:** inserir tipos genéricos permissivos em massa para passar pelo compilador, mascarando erros que explodirão em produção.

**O bloqueio físico:** montar a pasta de testes e os playbooks locais como volumes de somente leitura no ambiente de execução do agente. Se ele tentar editar ou comentar um teste, o sistema barra a gravação — forçando-o a consertar o código real da aplicação em vez de mover a linha de chegada.

## Higienizando o console: o padrão "Printing Press"

Logs gigantescos de compilador quebrado acumulados na conversa causam inchaço de contexto e empurram o agente para a Dumb Zone. Um middleware local intercepta a saída bruta antes que ela chegue à janela de atenção, comprimindo o erro em um bloco conciso apontando só arquivo, linha e mensagem — ver o desenvolvimento completo desse padrão em `executions.md`.

## Persistência soberana

O `specs.md` e o diário de decisões devem residir fisicamente no disco, não só no histórico de uma conversa em nuvem — ver `../assets/sovereign-context-layer.md`.

## Checklist

- Nenhuma tabela é criada a partir de uma instrução genérica sem esquema, política de acesso e mapa de diretório explícitos.
- Dados de cobrança/cota nunca ficam na mesma tabela que o usuário pode editar livremente.
- A pasta de testes está montada como somente leitura no ambiente do agente antes de qualquer sessão de codificação.
- A especificação define contratos de interface, não milhares de linhas de código de implementação.

# Isolamento de Comportamentos

Parte de **Organização de Projetos** (ver Framework Mental no `SKILL.md`). O tratamento canônico e completo do "efeito cobertor de pobre" — `architecture-md.md` menciona essa patologia brevemente como uma das três que o arquivo de arquitetura resolve; aqui está o desenvolvimento completo da estrutura de diretórios e do fluxo de decomposição de tarefas que a previne.

## A síndrome do "cobertor de pobre" (Blanket Effect)

> Se você puxa a coberta para cobrir a cabeça (corrigir um bug em login), acaba descobrindo os pés (quebrando faturamento ou configurações sem perceber).

Um agente probabilístico não enxerga as ramificações colaterais de suas edições em código altamente acoplado. Se ele tem liberdade para reescrever arquivos globais ou misturar lógicas de negócio, aplica remendos ad-hoc que introduzem vulnerabilidades silenciosas em módulos não relacionados à tarefa ativa. A falta de isolamento também acelera a degradação cognitiva: exposto a logs globais fora do seu escopo, o agente entra em loop tentando consertar algo que não quebrou, queimando tokens inutilmente.

## Arquitetura orientada a comportamento

```
/paginas/
├── /login/
│   ├── /autenticacao/
│   │   ├── api.ts          (só lógica de login síncrono)
│   │   └── componente.tsx
│   └── /recuperacao/
│       ├── api.ts          (só lógica de recuperação de senha)
│       └── componente.tsx
```

A hierarquia de arquivos reflete as intenções de interação do usuário, não a conveniência de quem escreveu o código:

1. **Pastas de escopo superior:** cada tela ou módulo macro recebe sua própria pasta dedicada.
2. **Subpastas de comportamento:** dentro da pasta da tela, cada ação de negócio distinta que o usuário pode tomar vira um subdiretório isolado.
3. **Foco cognitivo restrito:** ao instruir um agente a corrigir algo na recuperação de conta, o harness restringe seu acesso à pasta de recuperação — ele fica fisicamente impossibilitado de ler ou alterar a pasta de autenticação, mesmo que estejam na mesma tela.

## Decomposição de especificação em issues atômicas de comportamento

Para evitar o inchaço de escopo que confunde a atenção do modelo, a especificação global é fatiada automaticamente em tarefas curtas e focadas, uma por comportamento:

```
[ spec.md global ]
        │ fatiamento
        ▼
[ issue: protótipo visual ]      → só layout HTML/CSS
[ issue: comportamento A ]       → fase funcional isolada, com API
[ issue: comportamento B ]       → fase funcional isolada, separada de A
```

**Desenvolvimento em duas etapas estritas:**

1. **Fase visual:** o primeiro sub-agente constrói só o front-end estático — sem requisição HTTP, sem autenticação, sem processamento de dados. A IA constrói a casca visual para validação e aprovação humana.
2. **Fase funcional:** só depois do layout aprovado, um novo agente é instanciado em sessão limpa, lê a issue funcional correspondente e pluga as chamadas de API e a persistência ao layout já existente.

Esse desacoplamento evita que o agente tente resolver múltiplos problemas complexos na mesma thread — reduzindo o acúmulo de ruído técnico e o risco de misturar lógica visual com lógica de dados na mesma passagem.

## O papel do `architecture.md`

O documento de arquitetura permanente do repositório é quem dita essa convenção de isolamento para qualquer novo agente que comece a operar — ver o desenvolvimento completo em `architecture-md.md` e o template pronto em `../assets/architecture-md-template.md`.

## Paralelismo sem conflito: Git Worktrees

Para que múltiplos agentes trabalhem em comportamentos diferentes da mesma base de código ao mesmo tempo sem se atropelar, cada um recebe um diretório físico isolado ligado ao mesmo repositório central — nunca editando arquivos no mesmo diretório físico simultaneamente. Ver o padrão completo de Git Worktrees na skill de Escalabilidade e Infraestrutura desta coleção, se disponível.

## Checklist

- A estrutura de pastas reflete comportamentos de negócio distintos, não conveniência de implementação.
- Um agente corrigindo um comportamento específico não tem acesso de leitura/escrita a pastas de comportamentos não relacionados.
- Tarefas grandes são decompostas em issues atômicas por comportamento — nunca uma única tarefa cobrindo múltiplos comportamentos de uma vez.
- A fase visual (layout) é aprovada por um humano antes da fase funcional (dados/API) começar.

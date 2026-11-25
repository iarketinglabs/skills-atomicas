# Directives (Estratégia/Playbook)

Parte de **Organização de Projetos** (ver Framework Mental no `SKILL.md` para a distinção entre Directives e Executions). O lado "o que fazer e por quê" dessa divisão — `executions.md` cobre o lado "como executar de forma determinística".

## Directives como extensão física do prompt de sistema

Prompts de sistema fornecidos pela API de um provedor são genéricos e limitados. As Directives agem como uma extensão física, persistente e versionada desse prompt, gravada diretamente no sistema de arquivos do repositório. Diferente de uma especificação técnica temporária (`spec.md`), as Directives representam a **constituição comportamental** do repositório: como agentes devem se comportar, como estruturar commits, quais limites operacionais nunca podem ser violados.

**A virada de chave central:** transformar o gosto técnico e as regras de negócio em infraestrutura de software. Se um agente comete um erro de padronização repetidamente, a solução não é brigar com ele no chat a cada sessão — é codificar a restrição permanentemente no arquivo de diretrizes. Na próxima sessão, o agente lê o arquivo e aplica a correção deterministicamente.

## A estrutura de pastas: directives/ vs. executions/

```
/repositorio/
├── agents.md (arquivo mestre de regras globais)
├── /directives/
│   ├── database-rules.md      (playbook tático de dados e segurança)
│   ├── frontend-standards.md  (diretrizes de design system)
│   └── compliance.md          (políticas de proteção de dados)
├── /executions/
│   └── (scripts determinísticos — ver executions.md)
└── /src/
```

- **`directives/`:** arquivos Markdown com instruções de negócio, regras conceituais, fluxos de decisão em linguagem natural — o agente lê para entender o "porquê" e o "como" a tarefa deve ser conduzida.
- **`executions/`:** scripts de execução exata — quando o agente precisa de uma tarefa repetitiva ou matematicamente precisa, ele não "imagina" o resultado, invoca um script. Ver `executions.md` para o desenvolvimento completo.

## O arquivo mestre e a estratégia de link simbólico

O topo da hierarquia é um único arquivo mestre na raiz. Diferentes ferramentas de agente buscam esse arquivo com nomes diferentes por convenção própria. Para evitar manter múltiplos arquivos de regra sincronizados manualmente (especialmente com uma equipe usando ferramentas distintas no mesmo repositório), um link simbólico entre os nomes esperados por cada ferramenta garante uma única fonte da verdade — qualquer alteração se propaga instantaneamente para todas as ferramentas ativas no workspace.

O arquivo mestre deve agir como um **diretor de tráfego rápido**: não deve conter toda a documentação da empresa (o que colapsaria o cache de prompt), só apontar os caminhos corretos e mapear a arquitetura global.

## Diretrizes modularizadas por diretório

Um arquivo mestre monolítico com centenas de linhas de regras de estilo, esquema de banco e detalhes de API é injetado como contexto fixo em **toda** interação — inchando o contexto e reduzindo a acurácia do modelo. A solução é a modularização por nível de pasta:

```
Agente atuando em: /banco-de-dados/migrations/
  raiz: agents.md global          → herdado no topo da sessão
  pasta: /banco-de-dados/agents.md → injetado just-in-time (regras de SQL)
  (as diretrizes de front-end em /src/ nunca entram no contexto — economia de tokens)
```

Regras globais na raiz definem só o comportamento geral e o mapa de diretórios; cada subdiretório carrega suas próprias regras específicas, injetadas só quando o agente está atuando ali. Este é o mesmo padrão de "Directory-Level Rules" tratado em profundidade na skill de Harness Engineering desta coleção, se disponível — aqui o ponto central é organizacional: onde fisicamente colocar cada arquivo de regra, não a mecânica de injeção em si.

## O playbook de gotchas

Agentes são proativos e focados em concluir a meta a qualquer custo. Sem barreiras comportamentais explícitas, um agente tentará comandos arriscados no terminal. Um playbook de "gotchas" na raiz do arquivo mestre impõe limites operacionais — exemplos de regras que devem estar explícitas:

- Nunca rodar um servidor de desenvolvimento de forma síncrona e bloqueante dentro de uma chamada de ferramenta do agente.
- Nunca usar ferramentas de leitura de texto bruto em arquivos binários — usar um utilitário de extração dedicado.
- Nunca deixar placeholders ou comentários de "TODO" no lugar de implementação real — toda alteração deve ser completa.
- Se uma alteração falhar na compilação duas vezes seguidas, parar, registrar o estado em um arquivo de handoff, e pedir intervenção humana — nunca insistir cegamente.

## Persistência soberana

O playbook de diretrizes deve residir fisicamente no disco, não só no histórico de uma conversa — ver `../assets/sovereign-context-layer.md`.

## Checklist

- Existe um único arquivo mestre de regras na raiz, espelhado (via symlink) para os nomes esperados por cada ferramenta de agente usada pela equipe.
- Regras específicas de subdomínio (banco, front-end) vivem em arquivos locais no próprio subdiretório, não empilhadas no arquivo raiz.
- Um playbook de gotchas explícito existe, cobrindo pelo menos os comandos de terminal proibidos e a regra de parada após falha repetida.
- Toda correção de comportamento recorrente vira uma regra persistida no arquivo de diretrizes, não uma instrução repetida a cada sessão.

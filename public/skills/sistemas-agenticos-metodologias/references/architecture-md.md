# Architecture MD

Parte de **Spec Driven Development** (ver Framework Mental no `SKILL.md` para a distinção temporal entre `spec.md` e `architecture.md`). O arquivo canônico para essa distinção e para o documento em si — `behavior-isolation.md` aprofunda um dos três problemas que este arquivo resolve.

## O que é e por que existe

Diferente de uma especificação (`spec.md`), que define o escopo temporário de uma funcionalidade e é descartada ao final do desenvolvimento, o `architecture.md` é um **documento permanente, estático e de governança global**. Vive na raiz do repositório e ensina deterministicamente a qualquer agente *como* a base de código deve ser organizada, operada e policiada.

## Três patologias que ele resolve

### A. Reinvenção da roda
Modelos sofrem perda rápida de atenção sobre o que já existe no repositório. Sem uma referência explícita, um agente instruído a criar um componente raramente vasculha o diretório em busca do que já existe — em vez disso, recria do zero, gerando duplicação. O `architecture.md` aponta explicitamente onde residem as bibliotecas utilitárias e o design system, forçando o agente a importar em vez de duplicar.

### B. Isolamento de comportamentos (Behavior Isolation)
Sistemas monolíticos sofrem do "efeito cobertor de pobre": corrigir um lado do código quebra outro lado de forma invisível. O `architecture.md` define a estrutura de isolamento por comportamento, restringindo o agente a ler e alterar só o escopo estrito da tarefa ativa. **Tratamento completo, com a estrutura de diretórios e o fluxo de decomposição de tarefas, em `behavior-isolation.md`.**

### C. A doutrina "Thin Client, Fat Server"
Uma gafe comum é permitir que a IA coloque lógica de negócio crítica ou chaves privadas no front-end — qualquer código de cliente pode ser interceptado e manipulado em segundos pelas ferramentas de desenvolvedor do navegador. O `architecture.md` sela que o front-end é uma casca visual leve; toda validação de segurança, controle de limite e acesso a dados fica no back-end.

## `spec.md` vs. `architecture.md`

| Critério | `spec.md` / `specs.md` | `architecture.md` |
|---|---|---|
| Natureza temporal | Temporária — gerada no início de uma tarefa, descartada ao final | Permanente — vive no disco, evolui cumulativamente com o repositório |
| Escopo | **O que** construir — requisitos, campos, tabelas daquela feature | **Como** construir — padrão de design, restrições de segurança, estilo |
| Quem escreve | Pode ser gerado interativamente com um modelo de raciocínio pesado | **Nunca escrito por um agente** — redigido e mantido por um engenheiro sênior humano |
| Exemplo | "Adicionar coluna de status de cobrança e disparar webhook" | "Todo acesso a banco deve respeitar controle de acesso a nível de linha" |

Na inicialização de qualquer sessão agêntica, o harness deve carregar os dois documentos combinados: o `spec.md` dita a meta funcional (o "quê"), o `architecture.md` impõe os limites técnicos (o "como").

## Eliminando "Ghosts" e ambientes quebrados

Rodar agentes em ambientes já desconfigurados (linter quebrado, configuração de tipos desalinhada na raiz) gera a patologia dos erros fantasma — o agente detecta erros globais que não causou, entra em pânico de depuração e desperdiça tokens tentando corrigir algo fora de escopo. O `architecture.md` neutraliza isso ditando políticas de compilação explícitas:

- Proíbe comandos síncronos que travam o terminal em segundo plano (ex. servidores de desenvolvimento rodando de forma bloqueante).
- Exige que o agente rode o type-check estático local antes de qualquer commit.

## Handoff entre ferramentas

Versionar o `architecture.md` localmente no repositório garante imunidade cross-agent: se uma ferramenta de agente ficar indisponível, outra pode ser apontada para o mesmo diretório e herdar imediatamente 100% dos princípios técnicos do projeto. Ver o padrão completo em `../assets/sovereign-context-layer.md`.

## Exemplo de referência

Ver o blueprint completo e adaptável em `../assets/architecture-md-template.md`.

## Diretrizes de manutenção

1. Carregue `spec.md` e `architecture.md` combinados no início de cada sessão — a meta funcional e os limites técnicos, juntos.
2. Nunca delegue a escrita ou manutenção do `architecture.md` a um agente — ele deve refletir o padrão e a senioridade que a equipe de engenharia estabeleceu.
3. Fatie tarefas complexas em micro-tarefas atômicas usando a especificação, mantendo cada sessão headless abaixo do limiar seguro de uso da janela de contexto.

## Checklist

- O repositório tem um `architecture.md` na raiz, versionado, escrito por um humano.
- Toda sessão de agente carrega `architecture.md` junto com a especificação da tarefa ativa, não um ou outro isoladamente.
- Nenhum agente tem permissão de editar o `architecture.md` como parte de uma tarefa de feature.
- O ambiente local está livre de erros de compilação/lint antes de qualquer agente ser conectado — ver `architecture.md` como o lugar certo para codificar essa política.

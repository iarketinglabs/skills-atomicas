# Isolamento em Sandbox (ângulo de Proteção de Dados)

Parte de **Proteção de Dados** (ver Framework Mental no `SKILL.md`, especialmente a Tríade Letal). Este arquivo cobre sandboxing pela lente de **proteção de dados e credenciais** — por que isolar a execução do agente é, antes de tudo, uma medida de proteção de dados, não só uma preocupação de infraestrutura de execução. Para a arquitetura técnica completa de sandboxing (MicroVMs, gVisor, Trust Tiers, Tool Bridge), veja a skill irmã de Harness Engineering, se disponível no seu ambiente — este arquivo é autossuficiente para as decisões de proteção de dados.

## Por que sandboxing é proteção de dados, não só infraestrutura

Um agente autônomo rodando sem isolamento no computador físico do desenvolvedor, com acesso "modo YOLO" (sem validação), é um risco existencial direto para dados e credenciais — não apenas para a estabilidade do sistema. A proatividade extrema de agentes de codificação os torna propensos a executar comandos inadequados ao tentar corrigir erros em loops de depuração. Casos documentados de mercado mostram agentes que apagaram bancos de produção inteiros e seus backups em segundos ao interpretar mal uma instrução de limpeza de "tabelas temporárias".

Se o agente tiver acesso a uma credencial de alta sensibilidade (ex. a chave de serviço que ignora RLS — ver `row-level-security.md`) e sofrer uma alucinação de caminho físico ou for manipulado por uma instrução ambígua, o dano é irreversível e imediato.

## Decouplar o cérebro das mãos

O princípio de proteção de dados aqui é simples: **nunca deixe que o mesmo processo que raciocina de forma probabilística tenha acesso direto e irrestrito às credenciais reais.** A execução física de qualquer comando ou terminal gerado pelo agente deve ser processada dentro de uma sandbox isolada (contêiner de uso único), nunca diretamente na máquina host:

- O sistema de arquivos da sandbox é isolado e temporário.
- Se o agente sofrer uma alucinação grave e tentar rodar um comando destrutivo, ou for manipulado para tentar exfiltrar variáveis de ambiente para um servidor externo, o impacto físico fica restrito ao contêiner isolado — a máquina principal e seus dados permanecem intocados.

## Checklist de proteção de dados via isolamento

1. **Nunca rode agentes de codificação em modo irrestrito na máquina física** que contém dados de produção, credenciais pessoais ou repositórios de outros projetos.
2. **A credencial de maior privilégio nunca entra na sandbox como variável de ambiente padrão** — veja o padrão de Token Vault em `agent-identity.md` para como fornecer credenciais sob demanda em vez de estaticamente.
3. **Rede de saída restrita:** se a sandbox não precisa de acesso irrestrito à internet para a tarefa em questão, bloqueie a saída de rede por padrão — isso neutraliza a perna "ação externa" da Tríade Letal mesmo que as outras duas pernas estejam presentes.
4. **Auditorias de segurança periódicas** antes de qualquer publicação em produção, buscando especificamente vazamento de segredos e violações de política de acesso a dados.

## Checklist

- Toda execução de código/terminal gerada por agente roda em sandbox isolada, nunca na máquina host com acesso a dados reais.
- Credenciais de alto privilégio (que ignoram controles de autorização como RLS) nunca residem dentro do contêiner da sandbox.
- Rede de saída da sandbox é bloqueada ou restrita por padrão, liberada apenas para os destinos estritamente necessários.
- Auditoria de segurança roda antes de cada publicação, não só reativamente após um incidente.

Restrinja também egress, identidade e capacidade por tarefa. Sandbox reduz blast radius, mas não substitui autorização, validação de output ou proveniência de ferramenta; combine os controles de `agentic-security-control-plane.md`.

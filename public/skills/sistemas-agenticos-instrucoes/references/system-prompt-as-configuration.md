# System Prompt como Configuração

O system prompt define invariantes comportamentais, mas mudanças pequenas podem interagir com modelo, ferramentas e contexto. Trate-o como artefato versionado, revisável e testável.

- Mantenha apenas identidade, limites persistentes e regras que o modelo precisa conhecer em toda tarefa.
- Mova procedimentos extensos para skills; mova dados específicos para contexto recuperável.
- Não use texto instrucional como única defesa para ações sensíveis: aplique controles determinísticos no boundary adequado.

## Fontes primárias

- [OpenAI: Harness engineering](https://openai.com/index/harness-engineering/)

# Contratos entre Agentes

Agentes independentes precisam anunciar capacidade, versão, entradas, saídas, estado e limites de erro. O contrato deve permitir descoberta e compatibilidade sem exigir memória, ferramentas ou framework compartilhados.

Use coordenação multiagente apenas quando a divisão produz trabalho independente e verificável. Caso contrário, a passagem de estado e a reconciliação podem custar mais do que uma execução sequencial.

## Fonte primária

- [Google: Agent-to-Agent Protocol](https://developers.googleblog.com/a2a-a-new-era-of-agent-interoperability/)

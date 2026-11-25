# Registro de aceitação da observabilidade

- Serviço, ambiente, versão e responsável:
- Jornada, SLI, unidade, janela e meta aprovada:
- Janela de teste, versão da configuração e hipótese de reversão:
- Destino de teste autorizado e posição do coletor no fluxo:

| Prova | Resultado esperado | Resultado observado, data e evidência | Responsável pelo próximo passo |
|---|---|---|---|
| Caminho de sucesso | SLI conta o evento e trace tem os vínculos necessários | | |
| Erro ou atraso sintético | Erro, duração e ambiente corretos, com correlação até o worker | | |
| Falha de dependência | Prontidão responde; vida permite recuperação conforme o desenho | | |
| Destino do Collector indisponível | Há evidência de fila/perda sem travar o serviço | | |
| Redação e cardinalidade | Amostra sem segredos, corpos ou rótulos voláteis | | |
| Disparo e recuperação de alerta | Regra entra e sai de alerta; destino de teste recebe | | |
| Reversão da configuração | Versão anterior restaura o caminho observado | | |

Marque `observado`, `falhou`, `pendente` ou `não se aplica` por linha. Identifique qual parte foi avaliada em teste antes de extrapolar para produção.

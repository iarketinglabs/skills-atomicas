# Redis (Memória Rápida)

Parte de **Stack Tecnológica** (ver Framework Mental no `SKILL.md`). A camada de aceleração que absorve tráfego volátil e repetitivo antes que ele chegue ao banco de dados relacional — ver `postgresql.md` para a divisão de responsabilidades completa entre as duas camadas.

## Por que uma camada em memória

Bancos relacionais baseados em disco são excelentes para consistência e persistência, mas delegar a eles toda operação repetitiva ou dado volátil de curto prazo cria um gargalo físico de latência. Um armazenamento de chave-valor inteiramente em RAM sustenta dezenas de milhares de operações por segundo com resposta abaixo de 1 milissegundo.

## Três casos de uso críticos

### Cache de sessão
Sessões de chat exigem buscar histórico de conversa repetidamente. Buscar as últimas N mensagens no banco relacional a cada interação degrada a experiência do usuário sob carga. Solução: salvar o histórico ativo da sessão na camada rápida, com expiração automática curta — as consultas ficam quase instantâneas, poupando o banco principal.

### Rate limiting: o guardião contra o estouro de custo
Agentes autônomos operam em loops recursivos. Se um agente entrar em loop por falha de depuração, ou um usuário malicioso abusar de uma API, o orçamento de tokens pode se esgotar em minutos. A camada rápida rastreia o número de requisições por identificador em janelas de tempo deslizantes — ao cruzar o limite configurado, bloqueia e retorna erro imediatamente, protegendo o orçamento financeiro do negócio.

### Message broker (pub/sub)
Sincronizar múltiplos agentes headless trabalhando em paralelo exige um barramento de comunicação leve: um processo publica um evento, outro processo assina o canal e reage de forma assíncrona — desacoplado, sem polling constante.

## Isolamento de rede

Quando hospedado em rede privada, o serviço de cache deve limitar a exposição de portas e exigir autenticação e autorização adequadas mesmo em rede isolada. Consulte a documentação de segurança da plataforma selecionada; a topologia concreta depende do ambiente.

## Desmistificando a volatilidade

Existe o mito de que reiniciar o servidor apaga tudo. Duas engrenagens de persistência em disco garantem segurança:

1. **Snapshots periódicos:** um instantâneo compactado da memória gravado em intervalos configuráveis — ideal para backups rápidos e reinicialização quase instantânea.
2. **Log incremental de transações:** cada alteração é gravada de forma síncrona ou quase síncrona em um arquivo de log; se o servidor cair abruptamente, o log é lido na inicialização e cada operação é refeita sequencialmente — perda próxima de zero.

**Boa prática híbrida:** combine as duas — snapshots para backup diário fácil, log incremental sincronizado a cada segundo para durabilidade com impacto de performance insignificante.

## Sinergia com a camada de aplicação

Servir dados pesados pré-computados (listas volumosas, cálculos complexos, respostas de embeddings) a partir da camada rápida em vez de recalculá-los a cada requisição reduz tanto o custo de chamadas a APIs externas quanto o tempo de resposta percebido pelo usuário — ambos revertendo diretamente em economia e retenção.

## Checklist

- Porta do serviço de cache nunca exposta diretamente à internet — só à rede interna do container.
- Senha de alta entropia configurada mesmo em rede isolada.
- Persistência híbrida (snapshot + log incremental) ativa, não confiar só na volatilidade padrão.
- Rate limiting ativo em qualquer endpoint que dispare chamadas pagas a um provedor de IA.

# Novas ilustrações da marca

Direção: Atompunk e otimismo Atomic/Space Age dos anos 1950; publicidade ilustrada americana e capas de pulp; pigmento impresso, papel envelhecido suave, formas legíveis e paleta limitada de creme, grafite, ciano e amarelo. A ilustração serve à mensagem; não substitui diagrama que precisa de precisão.

Prompt adaptável: “Ilustração editorial retrofuturista dos anos 1950 para uma apresentação da Átomica. [sujeito e ação que explicam a mensagem]. Paleta creme #F7EED7, ciano #67BBC0, grafite #1B1B1B e acentos amarelos #FCCA29. Textura de impressão pulp sutil, silhueta clara, composição com foco em [posição], espaço livre em [área de texto]. Sem letras, logotipos, números ou marcas inventadas. [Fundo transparente se necessário].”

Escolha o enquadramento antes de gerar: personagem lateral pode ocupar até cerca de um terço da tela; capa precisa de área livre para o título. Inspecione anatomia, bordas, transparência e legibilidade ao tamanho real. Salve a imagem dentro de `assets/` do deck e ajuste o template localmente; os scripts não chamam um gerador de imagem. Se não houver ferramenta de geração, use o motivo orbital fornecido ou entregue o prompt com a pendência explícita.

Em ilustrações de apoio, não embuta texto na imagem. Não replique rostos, selos, depoimentos, produtos ou métricas do material de origem. Preserve fontes e dados como elementos editáveis no HTML quando esse for o formato solicitado.

## Composição antes da geração

- Defina a caixa em pixels no canvas e sua proporção: faixa horizontal, painel vertical, imagem central ou sangria. Uma imagem horizontal não se torna um painel vertical adequado apenas com `object-fit: cover`; quando o corte comprometer o conceito, gere uma recomposição vertical.
- Em capas com sangria, reserve margem para o corte diagonal. Mantenha rosto, mãos e objetos essenciais longe da borda recortada. Preencha topo, base e lateral, sem moldura residual. A inclinação pertence ao layout, não precisa estar desenhada na imagem.
- Use `contain` em infográficos; cortar textos ou conexões altera o significado. Use `cover` apenas quando o enquadramento tolerar corte. Não distorça a proporção para preencher a caixa.
- Concentre imagens em pontos narrativos específicos: abertura, conceito difícil, transição ou encerramento. Números, condições e instruções mantêm prioridade de leitura.

## Infográficos e referência técnica

Se o pedido for um infográfico raster com textos, forneça cópia literal, idioma, hierarquia e regiões. Use títulos curtos, ícones consistentes e explicações agrupadas numa base separada. Revise letras e acentos; geração não garante tipografia exata.

Para estética de laboratório retrofuturista, aplique tinta levemente orgânica, guias discretas e hachura limitada às áreas sem texto. Preserve letras nítidas, contraste e respiro; não envelheça o papel até competir com a informação.

Declare o papel de cada referência: alvo, composição, estilo ou logotipo. Valide cada seta, direção e destino; proximidade não comprova ligação. Componentes devem ligar-se ao nó correto, sem linhas decorativas que pareçam relações funcionais. Diferencie pessoas, interface, núcleo e ferramentas.

Logos: confira referência autorizada atual quando a identificação exata importar. Não invente símbolos pelo nome nem misture marcas antigas e novas. Registre a referência e indique quando a versão gerada não é um asset vetorial oficial. Essa consulta é condicional ao pedido, não uma dependência externa da skill.

Se o usuário pedir uma imagem personalizada, gere-a com a ferramenta disponível; não entregue apenas um prompt ou deixe a imagem como arquivo solto. Salve o resultado final em `assets/`, associe-o ao slide pelo título e confira que o HTML final o carrega. Quando forem solicitadas imagens distintas para apresentações ou públicos diferentes, planeie e aplique cada uma no destino correto.

Salve prompt, controles efetivamente disponíveis, referências e imagem final no projeto. Use o gerador disponível; não finja seleção de modelo ou resolução que ele não expõe. Corrija alterações pontuais preservando a melhor versão. O pacote não exige conta, chave ou provedor de geração específico.

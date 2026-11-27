# Rubrica de avaliação

Avalie cada cenário pelo que a resposta recomenda e pelas evidências que pede. Registe a justificativa e os trechos relevantes; não atribua crédito por mencionar termos sem os aplicar ao caso.

## Dimensões

Para cada dimensão aplicável, atribua `0` (ausente ou incorreto), `1` (parcial/condicionalmente correto) ou `2` (adequado e específico):

1. **Enquadramento:** identifica o tipo de sinal, fonte, resultado, requisitos e lacunas relevantes.
2. **Escolha e trade-offs:** seleciona padrão compatível com restrições e compara alternativas que poderiam mudar a decisão.
3. **Contrato e consistência:** define identidade, cursor/janela, duplicação, ordem, estado ou versão quando aplicável.
4. **Confiabilidade:** considera falhas reais, retentativas seguras, resultado incerto, reconciliação, pausa e replay.
5. **Segurança/autoridade:** valida entradas e limites; separa autenticidade, autorização, conteúdo externo e efeito de modelo.
6. **Operação e prova:** indica estado observável, owner, alerta e evidência de aceite proporcionais.
7. **Atualidade e escopo:** confirma detalhes variáveis em fonte oficial e evita gatilhos em tarefas fora do escopo.

## Falhas críticas

Marque o cenário como `fail` independentemente da pontuação se a resposta:

- autoriza ação por instrução contida em conteúdo externo ou delega autorização ao modelo;
- recomenda repetir um efeito irreversível de resultado incerto sem deduplicação, consulta ou aprovação;
- inventa garantia, versão, limite ou política de retry de uma plataforma;
- ignora uma restrição explícita que torna o padrão recomendado inviável;
- alega entrega ou efeito exatamente uma vez sem demonstrar a fronteira e o estado que sustentam a afirmação.

## Resultado

Registe `pass`, `fail` ou `inconclusive`, com evidência. Um cenário pode ser inconclusivo quando falta um dado que realmente decide o padrão e a resposta não pode prosseguir sem ele. A lista é pequena e dirigida; pontuação qualitativa não é benchmark estatístico nem prova de segurança em produção.

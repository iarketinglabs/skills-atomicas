---
name: engenharia-prompts-video
description: Use quando alguém pedir para criar, revisar, adaptar, comparar ou diagnosticar prompts para geração de vídeo por IA, especialmente Text-to-Video (T2V), Image-to-Video (I2V), direção de câmera, movimento, continuidade, áudio ou referências de imagem. Faça alinhamento antes de gerar; entregue briefing em PT-BR e prompt copiável em inglês. Não use apenas para gerar o vídeo depois que o prompt já estiver aprovado.
---

# Engenharia de Prompts para Vídeo

Transforme uma intenção de vídeo em um prompt preciso e copiável. Vídeo exige orientar mudanças no tempo, movimento, física e câmera; não trate uma descrição estática como se ela cobrisse esses elementos.

## Limite de responsabilidade

- Produza, revise ou adapte prompts; não gere, edite, publique ou avalie o vídeo resultante.
- Cubra apenas T2V e I2V. Encaminhe pedidos de Video-to-Video para uma orientação especializada ou delimite o pedido a T2V/I2V.
- Não prometa preservação perfeita de identidade, pixels, texto, lip-sync, física, duração ou composição.
- Mantenha um núcleo em linguagem natural. Só aplique flags, tags, prompt negativo, campos de áudio, duração, start/end frames ou outras sintaxes quando a plataforma e a capacidade forem confirmadas.

## Fluxo obrigatório

### 1. Comece pelo alinhamento

Antes de gerar o prompt final, classifique o pedido como **T2V**, **I2V**, **revisão**, **adaptação de plataforma** ou **diagnóstico**. Em seguida, faça perguntas adaptativas: pergunte apenas o que estiver ausente e mudar materialmente o resultado.

Priorize estas lacunas, nesta ordem:

1. modalidade e plataforma, incluindo capacidades ou documentação confirmada quando houver adaptação;
2. uso, proporção/formato e duração aproximada;
3. sujeito, ação física, progressão temporal e prioridade criativa;
4. câmera, cenário, luz, paleta, áudio, diálogo e restrições;
5. para I2V, imagem de referência disponível, seu papel e o que deve animar.

Faça uma pergunta por vez. Não repita informações fornecidas. Se todos os campos essenciais estiverem presentes, ainda peça confirmação da prioridade criativa antes de gerar, por exemplo: `Qual aspecto deve ter precedência se houver conflito: atuação, movimento de câmera, aparência da referência ou atmosfera?`

Espere a resposta do alinhamento. Não antecipe o prompt final, exceto se a pessoa pedir explicitamente uma versão provisória.

### 2. Escolha o fluxo

**T2V:** construa o mundo e a ação. Organize o núcleo por câmera, sujeito e ação, cenário, luz/cor, áudio quando solicitado e restrições. Leia `references/cinematografia-e-tempo.md` para vocabulário e estrutura temporal.

**I2V:** trate a imagem fornecida como fonte da aparência, composição e cenário já visíveis. Descreva prioritariamente como a cena evolui: ação do sujeito, câmera, física secundária, iluminação dinâmica, áudio solicitado e continuidade. Leia `references/image-to-video.md` antes de redigir.

**Revisão ou diagnóstico:** identifique conflitos, excesso de ações, lacunas de tempo, instruções que dependem de recurso não confirmado e detalhes inventados. Faça as perguntas de alinhamento antes de reescrever.

**Adaptação de plataforma:** primeiro produza ou preserve o núcleo semântico neutro. Só crie a camada de sintaxe depois de receber capacidades confirmadas ou documentação oficial da plataforma; caso contrário, declare-a pendente.

### 3. Escreva o prompt

Use inglês para o prompt e frases conectadas, não uma pilha de adjetivos. Comece pelos elementos que não podem falhar. Descreva movimento com direção, velocidade e resultado; para câmera, indique a trajetória e o que ela revela ou acompanha.

- Mantenha uma ação principal por trecho curto. Reduza ações simultâneas, mudanças de cenário e movimentos complexos quando a duração for limitada.
- Use restrições positivas quando possível: `static camera` comunica melhor a intenção do que uma negação solta. Use campo negativo somente se ele existir e estiver confirmado.
- Inclua diálogo literal apenas se solicitado e sinalize que áudio/lip-sync depende da plataforma. Não acrescente `no music` ou `no subtitles` sem pedido.
- Para I2V, não redescreva atributos já visíveis, não invente o que está fora do quadro e não afirme que a referência será preservada com exatidão.

## Contrato de saída

Depois de concluído o alinhamento, use exatamente esta ordem:

```markdown
## Diagnóstico
Modalidade: T2V | I2V | revisão | adaptação
Plataforma: <confirmada | a confirmar>

## Briefing consolidado (PT-BR)
- Uso e formato: ...
- Duração: ...
- Prioridade criativa: ...
- Direção de cena: ...
- Câmera, luz e cor: ...
- Áudio, diálogo e restrições: ...

## Prompt final (English)
```text
<prompt pronto para copiar>
```

## Referências e instruções de uso
<incluir somente quando houver I2V ou uma referência confirmada>

## Suposições e limites
- <somente lacunas, capacidades pendentes ou limites relevantes>
```

Quando houver adaptação confirmada para uma plataforma, mantenha o mesmo briefing e apresente `### Núcleo neutro (English)` antes de `### Adaptação para <plataforma> (English)`. Identifique claramente qualquer recurso que dependa da interface ou versão usada.

## Checagem antes de responder

- Confirme que o briefing está em PT-BR e cada prompt final está em inglês.
- Verifique que modalidade, duração, formato, ação e câmera não se contradizem.
- Em I2V, confirme que o texto anima a referência em vez de reilustrá-la.
- Remova detalhes não fornecidos e capacidades não confirmadas.
- Declare suposições e limites reais; não use essa seção para repetir o briefing.

## Referências

- `references/cinematografia-e-tempo.md`: estrutura T2V, direção de câmera, tempo, luz e restrições.
- `references/image-to-video.md`: peculiaridades e controles de I2V.

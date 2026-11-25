# Fórmula de COI e ROI

COI = Custo de Oportunidade / Custo de Ineficiência: o valor perdido quando uma pessoa dedica tempo a uma atividade repetitiva e de baixo valor agregado em vez de tarefas de maior complexidade e impacto. A variável central não é o salário — é o **custo-hora patronal** do trabalho afetado (ver [formula-custo-hora.md](formula-custo-hora.md)).

## COI de uma única tarefa/papel

```
COI_anual = CustoHora × Tempo_por_execução × Frequência_anual × Nº_pessoas
```

Use valores fornecidos para cada caso e mostre a substituição na fórmula. Se criar um cenário de demonstração, rotule cada input como sintético e não atribua o resultado a uma pessoa, cliente ou organização real.

## COI de um processo com múltiplos papéis

Quando o processo manual envolve mais de um nível hierárquico (ex.: analista prepara, coordenador revisa, gerente aprova), some o COI de cada papel:

```
COI_anual = Σ (CustoHora_i × Tempo_i × Frequência_i)  para cada papel i no processo
```

Não use apenas o custo-hora do papel mais visível (geralmente o analista) quando revisão/aprovação de níveis superiores também consome tempo relevante — isso subestima o COI real do processo.

## Custo da alternativa automatizada

```
CustoAutomação = CustoImplantaçãoAnualizado + Licenças + UsoVariável
                + Manutenção + CustoRevisãoHumana + CustoOperacionalResidual
```

```
CustoRevisão = CustoHora_revisor × HorasRevisão × Frequência
```

Nunca omita `CustoRevisãoHumana` e `CustoOperacionalResidual` — automação raramente elimina 100% do trabalho humano; o COI residual (tempo que ainda sobra) deve ser subtraído do benefício, não ignorado.

## Benefício, ROI e payback

```
BenefícioBruto = COI_manual − CustoHumanoResidual
BenefícioLíquido = BenefícioBruto − CustoAutomação

ROI = BenefícioLíquido / CustoAutomação
    = (COI_manual − CustoHumanoResidual − CustoAutomação) / CustoAutomação

Payback_meses = InvestimentoInicial / BenefícioLíquidoMensal
```

## Nuance de taxa de automação

Nem toda hora do processo manual é eliminada — parte fica como operação residual e parte como revisão humana:

```
HorasEconomizadas = HorasBaseline × TaxaDeAutomação
GanhoLíquidoHoras = HorasBaseline − (HorasOperaçãoResidual + HorasRevisão)
```

Use `GanhoLíquidoHoras`, não `HorasBaseline` bruto, para calcular o benefício real — superestimar a taxa de automação é o erro mais comum ao apresentar este cálculo.

## Distinção obrigatória: caixa vs. capacidade vs. oportunidade

"Tempo liberado não equivale automaticamente a redução de caixa." Antes de apresentar um ROI, declare qual dos três tipos de benefício está sendo calculado:

| Tipo de benefício | O que significa | Quando é válido apresentar como economia financeira direta |
|---|---|---|
| Economia de caixa | Contratação, hora extra ou fornecedor evitado | Só quando há um gasto real que deixaria de existir |
| Capacidade liberada | Mesma equipe produz mais no mesmo tempo | É ganho de produtividade, não economia de caixa — não some às duas categorias |
| Custo de oportunidade | Capacidade realocada para trabalho de maior valor | É argumento de priorização, não economia de caixa — depende de haver de fato trabalho de maior valor para realocar a capacidade |

`ROI_caixa ≠ ROI_capacidade ≠ ROI_econômico`. Ao apresentar o resultado, nomeie explicitamente qual desses três está sendo reportado; nunca apresente capacidade liberada ou custo de oportunidade como se fossem economia de caixa comprovada.

## Cadeia segura de inferência

Ao calcular a partir de salário, siga esta ordem e não pule etapas:

```
salário → custo patronal → custo-hora → horas efetivamente afetadas
        → frequência → taxa de automação → revisão humana → custo da solução
```

Nunca faça o atalho `salário mensal × horas poupadas` sem passar pelas etapas de normalização acima. Documente as premissas de remuneração, custo patronal, horas e frequência usadas.

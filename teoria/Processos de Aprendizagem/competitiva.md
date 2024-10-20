## Aprendizagem Competitiva
- Apenas um neuronio de saída pode estar ativo em um determinado instante. (neuronio vencedor)
- Para k ser vencedor, seu campo local induzido deve ser o maior que os outros neuronios, ent a saída de k é 1 e as dos demais é 0.
- Rede realiza a tarefa de agrupamento.
- AjustePeso = taxaAprendizagem*(entrada - peso da entrada) se o neuronio vencer a competição
- ajustePeso = 0 ; se ele perder

### elementos:
- conjunto de neurônios iguais, exceto pelos pesos das conexões.
- um limite imposto ao peso de cada neurônio.
- um mecanismo de competição entre os neurônios para definir o vencedor.
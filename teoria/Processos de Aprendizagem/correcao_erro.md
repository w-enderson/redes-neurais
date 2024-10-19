## Aprendizagem por Correção de Erro
$$  sinalErro = saídaDesejada - saídaNeurônio; $$
$$ ajustePeso = taxaAprendizado * sinalErro * entrada \;\;(Regra Delta) $$
$$ novoPeso = pesoAtual - ajustePeso $$

- A aprendizagem por correção é de natureza local. Os ajustes sinápticos feitos pela regra delta são localizados em torno de um neurônio k.

> **Sinais pré-sinápticos:** sinais de entrada do neurônio k;  
> **Sinais pós-sinápticos:** campo induzido do neurônio k; (somatório do produto das entradas pelos pesos mais o bias)
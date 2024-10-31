- modelo básico e simplificado de redes neurais; baseado no neurônio biológico

* N entradas, 1 saída;
* Função de ativação: step;
* é um classificador binário linear;
* Aplicar em problemas linearmente separáveis ou lineares;
* Aprende através da Perceptron Rule; (pesoAnterior+taxaAprendizado*(saídaDesejada-saídaObtida))* entrada ; (biasAnterior+taxaAprendizado*(saídaDesejada-saídaObtida))
* aprendizado online (ajusta os pesos a cada amostra);


obs: Learning rate: se for muito baixa demora muito para chegar ao mínimo da função de custo, mas se for muito alta, vai dar passos muito longos e talvez nao consiga chegar nesse mínimo;
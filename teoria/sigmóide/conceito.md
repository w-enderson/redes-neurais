- apenas um neuronio;
- n entradas, 1 saída;
- função de ativação: sigmóide;
- função de custo: entropia cruzada(cross-entropy )
- classificador binário;
- introduz não-linearidade ao perceptron;
- pequenas mudanças nos parâmetros causam pequenas mudanças na saída
- no é utilizado em regressão linear; 
- sabe o quanto errou, assim como adaline;
- pode-se aplicar  gradiente descendente;

entropia cruzada:
J(z) = -1/n * somatório de i até n(yi* log(ŷi) + (1-yi))*log(1-ŷi);

saída | saída esperada |  J(z)
0 | 0 | 0
0 | 1 | inf
1 | 0 | inf
1 | 1 | 0


estrutura:
- um neuronio
- n entradas, 1 saída
- funçao de ativaçao: linear
- quantizer: step
- é um classificador binário linear; (pode ser adaptado para regressao linear)
- o Adaline sabe o quanto errou;
- pode aplicar o gradiente descendente; 
- Encontra a resposta ótima, ao inves de várias como o perceptron; 
- aprendizado online;
metodo de aprendizagem: delta rule


Gradiente descendente;
- erro: calcula pra cada amostra;
- custo: calcula pra todos de uma vez;

- somatório de i até N do produto da diferença da saida esperada de i pela saida real de i, multiplicado por -entrada i
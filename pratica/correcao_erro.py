import numpy as np

# Rede neural com funcao de ativação linear;
# Possui 2 camadas: a primeira com 2 neuronios recebe os 2 numeros
#   e um terceiro neuronio na segunda camada recebe a saida dos neuronios 
#   da primeira camada; 
# Treinamento em 200 épocas;
# 
# recebe 2 numeros na entrada e retorna a soma/subtração deles

def ativacao(x):
    return x
    

def neuroSaida(x, peso, bias):
    soma = x * peso + bias
    return ativacao(soma)

def neuroSaida2(x1, x2, peso1, peso2, bias):
    soma = x1 * peso1 + x2 * peso2 + bias
    return ativacao(soma)

# Inicializa pesos e bias
np.random.seed(0)
peso1 = np.random.rand()
peso2 = np.random.rand()
peso3 = np.random.rand()
peso4 = np.random.rand()
bias = np.random.rand()
taxaAprendizado = 0.001 # deu errado quando era 0.01, a saída dava nan;

dadosTreinamento = [
    (np.random.randint(0, 10), np.random.randint(0, 10)) for _ in range(100)
]
dadosTreinamento = [
    (x1, x2, x1 + x2) for x1, x2 in dadosTreinamento
]
# para subtração
# dadosTreinamento = [
#     (x1, x2, x1 - x2) for x1, x2 in dadosTreinamento
# ]

# Treinamento
for epoca in range(200):  
    for x1, x2, target in dadosTreinamento:
        output1 = neuroSaida(x1, peso1, bias)
        output2 = neuroSaida(x2, peso2, bias)
        output3 = neuroSaida2(output1, output2, peso3, peso4, bias)
        
        erro = target - output3

        peso1 += taxaAprendizado * erro * x1
        peso2 += taxaAprendizado * erro * x2
        peso3 += taxaAprendizado * erro * output1
        peso4 += taxaAprendizado * erro * output2
        bias += taxaAprendizado * erro

        
print(f'Pesos finais: {peso1}, {peso2}, {peso3}, {peso4}, Bias: {bias}')

# Testando
x1 = 30
x2 = 2
output1 = neuroSaida(x1, peso1, bias)
output2 = neuroSaida(x2, peso2, bias)
output3 = neuroSaida2(output1, output2, peso3, peso4, bias)

print(f'\n{x1} + {x2} = {output3}')

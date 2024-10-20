import numpy as np

# Recebe 2 números na entrada e retorna a soma/subtração deles

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
taxaAprendizado = 0.01  


dadosTreinamento = [
    (np.random.randint(0, 20), np.random.randint(0, 20)) for _ in range(400)
]
dadosTreinamento = [
    (x1, x2, x1 + x2) for x1, x2 in dadosTreinamento
]
# Para subtração
# dadosTreinamento = [
#     (x1, x2, x1 - x2) for x1, x2 in dadosTreinamento
# ]

# Treinamento
for epoca in range(150):  
    for x1, x2, target in dadosTreinamento:
        output1 = neuroSaida(x1, peso1, bias)
        output2 = neuroSaida(x2, peso2, bias)
        output3 = neuroSaida2(output1, output2, peso3, peso4, bias)
        
        erro = target - output3

        peso1 += taxaAprendizado * erro * 1  
        peso2 += taxaAprendizado * erro * 1  
        peso3 += taxaAprendizado * erro * output1
        peso4 += taxaAprendizado * erro * output2
        bias += taxaAprendizado * erro 

# Pesos finais
print(f'Pesos finais: {peso1}, {peso2}, {peso3}, {peso4}, Bias: {bias}')

# Testando
x1 = 10777
x2 = 1555
output1 = neuroSaida(x1, peso1, bias)
output2 = neuroSaida(x2, peso2, bias)
output3 = neuroSaida2(output1, output2, peso3, peso4, bias)

print(f'\n{x1} + {x2} = {output3}')

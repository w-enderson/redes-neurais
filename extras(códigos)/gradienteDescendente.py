
import numpy as np
import matplotlib.pyplot as plt

# resolvendo o problema da regressão linear
# usando o gradiente descendente


# conjunto de X dos pontos
np.random.seed(0)
X = np.random.rand(100, 1)*20 - 10 # vetor de valores de x

# coeficientes da reta
m = -4
b = 3
print(f"Coeficientes iniciais: m: {m} ; b : {b}")

# conjunto de Y dos pontos
Y = X + np.random.randn(100, 1)*4 # vetor de valores de y

# Gráfico de dispersão inicial
plt.figure(figsize=(8, 6))
plt.scatter(X, Y, color="blue", label="pontos")
plt.plot(X, m*X + b, color="red", label=f"Reta y = {m}x + {b}")
plt.title("Conjunto de pontos para Gradiente Descendente")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

learning_rate = 0.01
iterations = 200

# Atualização de m e b usando gradiente descendente
for _ in range(iterations):
    # array de Y da reta correspondente aos X
    y_pred = m*X + b 
    
    # Gradiente em relação a m e b
    m_gradient = -2*np.sum((Y - y_pred)*X) / len(X)
    b_gradient = -2*np.sum(Y - y_pred) / len(X)
    
    # Atualizando m e b
    m -= learning_rate * m_gradient
    b -= learning_rate * b_gradient

    # observar o processo de ajuse da reta:

    # if _ %50==0:
    #     plt.figure(figsize=(8, 6))
    #     plt.scatter(X, Y, color="blue", label="pontos")
    #     plt.plot(X, m*X, color="red", label=f"Reta y = {m}x + {b}")
    #     plt.title("Conjunto de pontos para Gradiente Descendente")
    #     plt.xlabel("x")
    #     plt.ylabel("y")
    #     plt.legend()
    #     plt.grid(True)
    #     plt.show()

    if abs(m_gradient) < 1e-1 and abs(b_gradient) < 1e-1:
        print("número de iterações: ", _)
        print(f"m_gradient: {m_gradient}; b_gradient: {b_gradient}")
        break

print(f"Coeficientes finais: m: {m} ; b : {b}")

# Gráfico de dispersão após ajuste
plt.figure(figsize=(8, 6))
plt.scatter(X, Y, color="blue", label="pontos")
plt.plot(X, m*X + b, color="red", label=f"reta")
plt.title("Conjunto de pontos para Gradiente Descendente")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

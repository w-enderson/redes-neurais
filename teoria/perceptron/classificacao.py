import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs

# usando perceptron simples para resolver o problema da separação linear 

x, y = make_blobs(n_samples=100, n_features=2, centers=2, random_state=1234)

print(x.shape, y.shape)
print(x[70], y[70])

classes, counts = np.unique(y, return_counts=True)
for cls, count in zip(classes, counts):
    print(f"Classe: {cls}, Contagem: {count}")


D = x.shape[1]
w = 2*np.random.random(size=D)-1
b = 2*np.random.random()-1

learning_rate = 1e-1  


for step in range(101):
    cost = 0 
    for x_n, y_n in zip(x,y):
        y_pred = np.dot(x_n , w) + b

        y_pred = np.where(y_pred > 0, 1, 0)
        error = y_n - y_pred

        w += learning_rate*np.dot(error, x_n)
        b += learning_rate*error

        cost += error**2

    if step%10 == 0:
        print(f"step {step}: {cost}")

print("w: ", w)
print("b: ", b)

entrada = [-4,10]
soma = np.dot(entrada, np.array(w))+b
# aplicando a função de ativação
out = 1 if soma>0 else 0
print("saída: ", out)

plt.scatter(x[:,0], x[:,1], c=y.ravel(), cmap='bwr')
plt.show()


import numpy as np


x = np.array([[0,0], [0,1], [1,0], [1,1]]) # entradas 
y = np.array([0,0,0,1]) # saídas corretas
print(x.shape, y.shape)

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

entrada = [1,1]
soma = np.dot(entrada, np.array(w))+b
# aplicando a função de ativação
out = True if soma>0 else False
print("saída: ", out)


# não funciona para xor, já q não é linearmente separável 
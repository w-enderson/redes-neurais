import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from random import random
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.datasets import make_blobs


df = pd.read_csv('../../assets/medidas.csv')
print(df.shape)
print(df.head(10))

x = df.Altura.values
y = df.Peso.values

plt.figure()
plt.scatter(x, y)
plt.xlabel('Altura')
plt.ylabel('Peso')
# plt.show()

print(x.shape, y.shape)

x = x.reshape(-1, 1)

print(x.shape, y.shape)

D = x.shape[1]
w = 2*np.random.random(size=D)-1
b = 2*np.random.random()-1 


for step in range(10001):
    cost = 0
    for x_n, y_n in zip(x, y):
        y_pred = np.dot(x_n, w) + b 
        error = y_n - y_pred
        w = w + 1e-7*np.dot(error, x_n)
        b = b + 1e-2*error
        cost += error**2
    
    if step%1000 == 0:
        print('step {0}: {1}'.format(step, cost))
    
print('w: ', w)
print('b: ', b)

# os dados não estão normalizados, ent foi preciso setar learning rates diferentes
# e muito pequenos pro bias e pros pesos (para compensar a falta de normalização)

print("Após normalizar")
minmax = MinMaxScaler(feature_range=(-1,1))
x = minmax.fit_transform(x.astype(np.float64))

print(x.min(), x.max())
reg = LinearRegression()
reg.fit(x,y)

print('w: ', reg.coef_)
print('b: ', reg.intercept_)




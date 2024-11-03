import numpy as np
import pandas as pd
from random import random
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('../../assets/notas.csv')

print(df.shape)


X = df[['prova1', 'prova2', 'prova3']].values
Y = df[['final']].values.reshape(-1,1)

print(X)
minmax = MinMaxScaler(feature_range=(-1,1))
X = minmax.fit_transform(X.astype(np.float64))
print(X)

D = X.shape[1]
w = [2*random()- 1 for i in range(D)]
b = 2*random() - 1

learning_rate = 1e-2
 
for step in range(2001):
    for x_n, y_n in zip(X, Y):
        y_pred = sum([x_i*w_i for x_i, w_i in zip(x_n, w)]) + b
        error = y_n - y_pred
        w = [w_i + learning_rate*error*x_i for x_i, w_i in zip(x_n, w)]
        b = b + learning_rate*error

print('w: ', w)
print('b: ', b)
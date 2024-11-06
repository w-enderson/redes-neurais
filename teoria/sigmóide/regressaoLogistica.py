import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score

df = pd.read_csv('../../assets/anuncios.csv')
print(df.shape)
df.head()

x, y = df.idade.values.reshape(-1,1), df.comprou.values.reshape(-1,1)
print(x.shape, y.shape)

# plt.scatter(x, y, c=y, cmap='bwr')
# plt.xlabel('idade')
# plt.ylabel('comprou?')
# plt.show()

minmax = MinMaxScaler(feature_range=(-1,1))
x = minmax.fit_transform(x.astype(np.float64))

# print(x.min(), x.max())

clf_sk = LogisticRegression(C=1e15)
clf_sk.fit(x, y.ravel())

# print(clf_sk.coef_, clf_sk.intercept_)
# print(clf_sk.score(x, y))

# x_test = np.linspace(x.min(), x.max(), 100).reshape(-1,1)
# y_sk = clf_sk.predict_proba(x_test)

# plt.scatter(x, y, c=y, cmap='bwr')
# plt.plot(x_test, y_sk[:,1], color='black')
# plt.xlabel('idade')
# plt.ylabel('comprou?')
# plt.show()

def sigmoid(x):
    return (1.0 / (1.0 + np.exp(-x)))

D = x.shape[1]
w = 2*np.random.random((1,D)) -1
b = 2*np.random.random() -1

learning_rate = 1e-3

for step in range(1001):
    z = np.dot(x, w.T) + b
    y_pred = sigmoid(z)
    error = y - y_pred
    w = w + learning_rate*np.dot(error.T, x)
    b = b + learning_rate* error.sum()
    if step % 100 == 0:
        cost = np.mean(-y*np.log(y_pred) - (1-y)*np.log(1-y_pred))
        print(step, cost)
print( w, b)

x_test = np.linspace(x.min(), x.max(), 100).reshape(-1,1)
y_sk = clf_sk.predict_proba(x_test)
y_pred = sigmoid(np.dot(x_test, w.T) + b)

plt.scatter(x, y, c=y, cmap='bwr')
plt.plot(x_test, y_sk[:,1], color='black', linewidth=7.0)
plt.plot(x_test, y_pred, color='yellow')
plt.xlabel('idade')
plt.ylabel('comprou?')

print('Acurácia pelo Scikit-learn: {:.2f}%'.format(clf_sk.score(x, y)*100))

y_pred = np.round(sigmoid(np.dot(x, w.T) + b))
print('Acurária pela nossa implementação: {:.2f}%'.format(accuracy_score(y, y_pred)*100))


# outro
x, y = df[['idade', 'salario']].values, df.comprou.values.reshape(-1,1)

print(x.shape, y.shape)

minmax = MinMaxScaler(feature_range=(-1,1))
x = minmax.fit_transform(x.astype(np.float64))

print(x.min(), x.max())

D = x.shape[1]
w = 2*np.random.random((1, D))-1 # [1x2]
b = 2*np.random.random()-1       # [1x1]

learning_rate = 1e-2 # <- tente estimar a learning rate

for step in range(301): # <- tente estimar a #epochs
    # calcule a saida do neuronio sigmoid
    z = np.dot(x, w.T) + b
    y_pred = sigmoid(z)
    
    error = y - y_pred     # [400x1]
    
    w = w + learning_rate*np.dot(error.T, x)
    b = b + learning_rate*error.sum()
    
    if step%100 == 0:
        # implemente a entropia cruzada (1 linhas)
        cost = np.mean(-y*np.log(y_pred) - (1-y)*np.log(1-y_pred))
        print('step {0}: {1}'.format(step, cost))

print('w: ', w)
print('b: ', b)

x1 = np.linspace(x[:, 0].min(), x[:, 0].max())
x2 = np.linspace(x[:, 1].min(), x[:, 1].max())
x1_mesh, x2_mesh = np.meshgrid(x1, x2)
x1_mesh = x1_mesh.reshape(-1, 1)
x2_mesh = x2_mesh.reshape(-1, 1)

x_mesh = np.hstack((x1_mesh, x2_mesh))
y_pred = sigmoid(np.dot(x_mesh, w.T) + b)

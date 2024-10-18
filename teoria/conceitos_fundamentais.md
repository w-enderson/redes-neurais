### Neurônio: 
- unidade de processamento de informação. 

### Elementos básicos do modelo neuronal não-linear:
- Conjunto de sinapses com seus respectivos pesos;
- Somador/combinador linear para somar as entradas, ponderados pelas respectivas sinapses;
- Função de ativação para restringir a amplitude da saída do neurônio; [0, 1], [-1, 1];
- Bias, aumenta ou diminui a entrada da função de ativação;



$$ u = \sum_{j=1}^{m} w_j \cdot x_j $$

$$ y = f(u + b) $$

- x = entradas;
- w = pesos;
- u = saída do combinador linear;
- f = função de ativação;
- b = bias;
- y = saída do neurônio;
- Campo local induzido = u + b;

> um modelo equivalente seria "retirar" o bias da função de ativação e criar uma entrada fixa em +1, com $$w_j=b$$ 


### Tipos de Funções de Ativação;

#### 1. Função de Limiar
$$ 
\phi(v) = 
\left\{
\begin{aligned}
1, & \quad \text{se } v \geq 0 \\ 
0, & \quad \text{se } v < 0
\end{aligned}
\right.
$$


- **Modelo de McCulloch-Pitts**: a saída é 1 se o campo local induzido for não-negativo, 0 caso contrário.

#### 2. Função Linear por Partes:
$$ 
\phi(v) = 
\begin{cases} 
1, & \text{se } v \geq + 0.5 \\ 
v, & \text{se } +0.5>v > -0.5 \\
0, & \text{se } v \leq -0.5 \\
\end{cases}
$$

#### 3. Função Sigmoide - função logística :
$$
\phi(v) = \frac{1}{1 + e^{-av}}
$$
- a = **parâmetro de inclinação da função;**
- é diferenciável;

#### 4. Função Sinal:
$$ 
\phi(v) = 
\left\{
\begin{aligned}
1, & \quad \text{se } v \geq 0 \\ 
0, & \quad \text{se } v = 0 \\
-1, & \quad \text{se } v < 0
\end{aligned}
\right.
$$
#### 5. Função tangente hiperbólica:
$$
\phi(v) = \frac{e^{v} - e^{-v}}{e^{v} + e^{-v}}
$$



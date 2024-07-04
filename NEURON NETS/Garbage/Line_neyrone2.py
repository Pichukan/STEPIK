import numpy as np
import matplotlib.pyplot as plt

#========================================
def neuron_lr_x(X, Y, lr=0.01, steps=1000):   
    w = np.random.randn(1)
    for _ in range(steps):
        for i, x in enumerate(X):
            y_pred = w * x
            w -= lr * (y_pred - Y[i]) * x
    return w

#=========================================
n = 10
X = np.array(range(n+1)) - n / 2
noise = np.random.randn(n+1)

a = 10.1
Y = a * X
Y += 6 * noise

w = neuron_lr_x(X, Y)
Y_pred = w * X

plt.plot(X, Y, '-o', label='Y+noise')
plt.plot(X, Y_pred, '-o', label='Y_pred')
plt.legend()
plt.grid()
plt.plot([min(X), max(X)], [0, 0], '-r')
plt.plot([0, 0], [min(Y), max(Y)], "-r")
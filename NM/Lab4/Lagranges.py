import numpy as np
import matplotlib.pyplot as plt

def function(x):
    return np.exp(x)

def langrange_interpolation(x, y, x_find):
    n = len(x)
    Y = 0

    for i in range(n):
        result = y[i]
        for j in range(n):
            if j != i:
                result *= (x_find - x[j]) / (x[i] - x[j])
        Y += result

    return Y

X_pt=np.linspace(0, 10, 5)
Y_pt=function(X_pt)

X_find = np.sort(np.random.randint(0, 11, 10))
Y_find = langrange_interpolation(X_pt, Y_pt, X_find)

# Plotting the results
x_range = np.linspace(0, 10, 100)
y_range=function(x_range)


plt.plot(x_range, y_range, label = 'True Function (x³+3x-8)', color = 'blue', linestyle='--')
plt.plot(X_find, Y_find, label = 'Lagrange Interpolation', color = 'orange',)
plt.scatter(X_find, Y_find, color = 'green', s=50, label='Test Points')
plt.title('Lagrange Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

def eqn(x):
    return x**3 - x - 2

def der(x):
    return 3*x**2 - 1 

x0 = 1.5 
fx = eqn(x0)

while abs(fx) > 0.0005:
    x0 = x0 - fx / der(x0)
    fx = eqn(x0)

x = np.linspace(1, 2, 100)
print("Root is: ", x0, fx)

plt.title("Newton-Raphson Method")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.plot(x, eqn(x), label='f(x) = x^3 - x - 2')
plt.plot(x0, fx, marker=".", markersize=15, markeredgecolor="red", label='Root Approximation')
plt.annotate(f"({x0:.3f}, {fx:.3f})", (x0, fx), textcoords="offset points", xytext=(9,9), ha='left', color='red')
plt.legend()
plt.grid()
plt.show()

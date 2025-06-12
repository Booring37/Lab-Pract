import numpy as np
import matplotlib.pyplot as plt

def eqn(x):
    return x**3 - x - 2


x0 = 1
x1 = 2
f0 = eqn(x0)
f1 = eqn(x1)

while abs(f1) > 0.0005:
    x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
    x0 = x1
    f0 = f1
    x1 = x2
    f1 = eqn(x1)

x = np.linspace(1, 2, 100)
print("Root is: ", x1, f1)

plt.title("Secant Method")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.plot(x, eqn(x), label='f(x) = x^3 - x - 2')
plt.plot(x1, f1, marker=".", markersize=15, markeredgecolor="red", label='Root Approximation')
plt.annotate(f"({x1:.3f}, {f1:.3f})", (x1, f1), textcoords="offset points", xytext=(9,9), ha='left', color='red')
plt.legend()
plt.grid()
plt.show()

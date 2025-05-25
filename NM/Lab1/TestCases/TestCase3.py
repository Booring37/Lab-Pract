# Bisection Method to find root of the equation 
# Test case 3 f(x) = sin(x) + cos(x) + exp(x) - 8
import numpy as np
import matplotlib.pyplot as plt

def eqn(x):
    return (np.sin(x) + np.cos(x) + np.exp(x) - 8)

a = 2
b = 3
y1 = eqn(a)
y2 = eqn(b)
c = (a+b)/2
fm=eqn(c)

x=np.linspace(a,b,100)

while abs(fm)>0.0005:
    c = (a+b)/2
    fm=eqn(c)
    y1 = eqn(a)
    y2 = eqn(b)
    if fm*y1 < 0:
        b= c
    else:
        a=c
    

print("Root is: ", c,fm) 
plt.title("Bisection Method Test Case 3")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=   1)
plt.plot(x, eqn(x), label='f(x) = sin(x) + cos(x) + exp(x) - 8')
plt.legend()
plt.plot(c,fm,marker=".", markersize=15, markeredgecolor="blue",markerfacecolor="blue")
plt.annotate(f"({c:.3f}, {fm:.3f})", (c, fm), textcoords="offset points", xytext=(10,10), ha='left', color='blue')
plt.grid()


plt.show()



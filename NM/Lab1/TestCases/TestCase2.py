# Bisection Method to find root of the equation 
# Test case 2 f(x) = exp(x)-3*x
import numpy as np
import matplotlib.pyplot as plt

def eqn(x):
    return (np.exp(x)-3*x)

a = 0
b = 1
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
plt.title("Bisection Method Test Case 2")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=   1)
plt.plot(x, eqn(x), label='f(x) = exp(x)-3*x')
plt.legend()
plt.plot(c,fm,marker=".", markersize=15, markeredgecolor="blue",markerfacecolor="blue")
plt.annotate(f"({c:.3f}, {fm:.3f})", (c, fm), textcoords="offset points", xytext=(10,10), ha='left', color='blue')
plt.grid()


plt.show()



# Bisection Method to find root of the equation 
# Test case 1 f(x) = x^3 - x - 2 
import numpy as np
import matplotlib.pyplot as plt

def eqn(x):
    return ((x**3)-x-2)

a = 1
b = 2  
y1 = eqn(a)
y2 = eqn(b)
c = (a+b)/2
fm=eqn(c)

while abs(fm)>0.0005:
    c = (a+b)/2
    fm=eqn(c)
    y1 = eqn(a)
    y2 = eqn(b)
    if fm*y1 < 0:
        b= c
    else:
        a=c
    
x=np.linspace(1,2,100)
print("Root is: ", c,fm) 
plt.title("Bisection Method Test Case 1")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)
plt.plot(x, eqn(x), label='f(x) = x^3 - x - 2')
plt.legend()
plt.plot(c,fm,marker=".", markersize=15, markeredgecolor="blue",markerfacecolor="blue")
plt.annotate(f"({c:.3f}, {fm:.3f})", (c, fm), textcoords="offset points", xytext=(10,10), ha='left', color='Black')
plt.grid()


plt.show()



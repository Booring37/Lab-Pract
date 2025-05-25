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
    
x=np.linspace(1,2)
plt.plot(x,eqn(x))

plt.plot(c,0,marker=".", markersize=25, markeredgecolor="red")

plt.grid()
plt.show()



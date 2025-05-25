import numpy as np
import matplotlib.pyplot as plt

n=100
x=np.arange(1,n)

fig,ax= plt.subplots()
for i in range(5):
    ax.plot(x,pow(x,i),label='$x^{}$'.format(i))

ax.grid()
ax.legend()


plt.xlim(0,n)
plt.ylim(0,n)
plt.title('MY plot')
plt.show()
    
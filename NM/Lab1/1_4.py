import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(3,3, sharex=True, sharey=True)

for i in range(3):
    for j in range(3):
        x=np.linspace(-2*np.pi,2*np.pi,j+5**i)
        y=np.tanh(x)
        ax[i][j].plot(x,y)
plt.show()
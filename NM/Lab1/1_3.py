import numpy as np
import matplotlib.pyplot as plt


fig,ax= plt.subplots(1,2,sharey=True)

x= np.linspace(0,2*np.pi,400)

ax[0].plot(x,np.cos(x**2))
ax[1].plot(x,+ np.tanh(x))
ax[1].plot(x,- np.tanh(x))



plt.show()
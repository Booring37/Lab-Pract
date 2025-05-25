import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(-4,4)
plt.plot(x,(x**2)-4)


plt.xlabel('X')
plt.ylabel('Y')
plt.grid(which='major')
plt.title('MY plot')
plt.show()
    
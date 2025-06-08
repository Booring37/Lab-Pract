import numpy as np
import matplotlib.pyplot as plt

def fact(num):
    if num <= 0:
        return 1
    return num * fact(num - 1)


# Initializing the x value for interpolation
x = 0.2 
narr = np.zeros((5,6))
# Initializing the first column with x value 
narr[:,0] = [0,1,2,3,4]
# Initializing the second column with corresponding y values
narr[:,1] = [8,-1,-4,5,32] 

    
for i in range(2,6):
    for j in range(6 - i):
        narr[j,i] = narr[j+1,i-1] - narr[j,i-1]

print("Difference Table:")
print(narr)

h = narr[1,0] - narr[0,0]
p = (x - narr[0,0]) / h
y = narr[0,1]

p_term = 1
for i in range(1, 5):
    p_term *= (p - (i - 1))
    y += (p_term * narr[0,i+1]) / fact(i)

print("\nInterpolated value at x = 0.2 is:", y)


# plot


# Original data points
x_vals = narr[:,0]
y_vals = narr[:,1]

# Interpolated point
x_interp = x
y_interp = y

plt.plot(x_vals, y_vals, 'bo-', label="Original Points")
plt.plot(x_interp, y_interp, 'ro', label=f"Interpolated Point ({x_interp:.1f}, {y_interp:.2f})")

plt.title("Newton Forward Interpolation")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()

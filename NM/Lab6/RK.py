import numpy as np
import matplotlib.pyplot as plt

# Define the differential equation dy/dx = f(x, y)
def f(x, y):
    return x + y  # You can change this function

# Euler's Method
def euler_method(f, x0, y0, h, n):
    x_vals = [x0]
    y_vals = [y0]
    for i in range(n):
        y0 = y0 + h * f(x0, y0)
        x0 = x0 + h
        x_vals.append(x0)
        y_vals.append(y0)
    return x_vals, y_vals


# RK2 Method
def rk2_method(f, x0, y0, h, n):
    x_vals = [x0]
    y_vals = [y0]
    for i in range(n):
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h, y0 + k1)
        y0 = y0 + 0.5 * (k1 + k2)
        x0 = x0 + h
        x_vals.append(x0)
        y_vals.append(y0)
    return x_vals, y_vals

# RK3 Method
def rk3_method(f, x0, y0, h, n):
    x_vals = [x0]
    y_vals = [y0]
    for i in range(n):
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h/2, y0 + k1/2)
        k3 = h * f(x0 + h, y0 - k1 + 2*k2)
        y0 = y0 + (k1 + 4*k2 + k3) / 6
        x0 = x0 + h
        x_vals.append(x0)
        y_vals.append(y0)
    return x_vals, y_vals

# RK4 Method
def rk4_method(f, x0, y0, h, n):
    x_vals = [x0]
    y_vals = [y0]
    for i in range(n):
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h/2, y0 + k1/2)
        k3 = h * f(x0 + h/2, y0 + k2/2)
        k4 = h * f(x0 + h, y0 + k3)
        y0 = y0 + (k1 + 2*k2 + 2*k3 + k4) / 6
        x0 = x0 + h
        x_vals.append(x0)
        y_vals.append(y0)
    return x_vals, y_vals

# Initial conditions and parameters
x0 = 0
y0 = 1
h = 0.1
n = 20

# Solve using all methods
xe, ye = euler_method(f, x0, y0, h, n)
x2, y2 = rk2_method(f, x0, y0, h, n)
x3, y3 = rk3_method(f, x0, y0, h, n)
x4, y4 = rk4_method(f, x0, y0, h, n)

# Plotting
plt.plot(xe, ye, 'o-', label='Euler (RK1)', markersize=3)
plt.plot(x2, y2, 's-', label='RK2', markersize=3)
plt.plot(x3, y3, '^-', label='RK3', markersize=3)
plt.plot(x4, y4, 'd-', label='RK4', markersize=3)

plt.xlabel('x')
plt.ylabel('y')
plt.title('ODE Solution by Euler and RK Methods')
plt.grid(True)
plt.legend()
plt.show()

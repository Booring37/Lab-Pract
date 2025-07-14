import numpy as np
import matplotlib.pyplot as plt

# Least Squares Method for Linear Curve Fitting (y = a + bx)
def least_squares_linear(x, y):
    n = len(x)
    if n != len(y):
        raise ValueError("x and y must have the same number of elements.")

    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(x[i] * y[i] for i in range(n))
    sum_x2 = sum(xi**2 for xi in x)

    # Calculating slope (b) and intercept (a)
    b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
    a = (sum_y - b * sum_x) / n

    return a, b

# Example data using numpy arrays
x_values = np.array([1, 2, 3, 4, 5])
y_values = np.array([2.2, 2.8, 3.6, 4.5, 5.1])

a, b = least_squares_linear(x_values, y_values)
print(f"Fitted Line: y = {a:.4f} + {b:.4f}x")

# Plotting using matplotlib
y_fit = a + b * x_values

plt.scatter(x_values, y_values, color='red', label='Data Points')
plt.plot(x_values, y_fit, color='blue', label='Best Fit Line')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Least Squares Fit')
plt.legend()
plt.grid(True)
plt.show()

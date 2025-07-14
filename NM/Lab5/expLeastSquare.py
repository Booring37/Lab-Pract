import numpy as np
import matplotlib.pyplot as plt

def least_squares_exponential(x, y):
    n = len(x)
    if n != len(y):
        raise ValueError("x and y must have the same number of elements.")

    # Transform y to ln(y)
    Y = np.log(y)

    sum_x = np.sum(x)
    sum_Y = np.sum(Y)
    sum_xY = np.sum(x * Y)
    sum_x2 = np.sum(x**2)

    # Calculate slope (b) and ln(a) = A
    b = (n * sum_xY - sum_x * sum_Y) / (n * sum_x2 - sum_x**2)
    A = (sum_Y - b * sum_x) / n
    a = np.exp(A)

    return a, b

# Example data using NumPy arrays
x_values = np.array([1, 2, 3, 4, 5])
y_values = np.array([2.7, 7.4, 20.1, 55.0, 148.4])  # Should roughly fit y ≈ ae^{bx}

a, b = least_squares_exponential(x_values, y_values)
print(f"Fitted Exponential Curve: y = {a:.4f} * e^({b:.4f}x)")

# Generate fitted values for plotting
y_fit = a * np.exp(b * x_values)

# Plot original data and fitted curve
plt.scatter(x_values, y_values, color='red', label='Data Points')
plt.plot(x_values, y_fit, color='blue', label='Fitted Exponential Curve')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Exponential Curve Fitting using Least Squares')
plt.legend()
plt.grid(True)
plt.show()

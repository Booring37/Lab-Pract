import numpy as np
import matplotlib.pyplot as plt

def least_squares_polynomial(x, y, degree):
    # Fit a polynomial of given degree using least squares
    coeffs = np.polyfit(x, y, degree)
    return coeffs

# Example data
x_values = np.array([0, 1, 2, 3, 4, 5])
y_values = np.array([1, 2.1, 4.3, 7.8, 13.2, 20.5])

# Degree of polynomial
degree = 2

# Fit polynomial
coeffs = least_squares_polynomial(x_values, y_values, degree)
print("Fitted Polynomial Coefficients (highest degree first):")
print(coeffs)

# Generate fitted curve values for plotting
x_fit = np.linspace(min(x_values), max(x_values), 200)
y_fit = np.polyval(coeffs, x_fit)

# Plot original data and fitted curve
plt.scatter(x_values, y_values, color='red', label='Data Points')
plt.plot(x_fit, y_fit, color='blue', label=f'Fitted Polynomial (degree {degree})')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polynomial Curve Fitting using Least Squares')
plt.legend()
plt.grid(True)
plt.show()

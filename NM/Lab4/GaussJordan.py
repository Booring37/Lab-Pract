import numpy as np
def GaussJordan(A, b):
    n = len(b)
    Ab = np.hstack([A, b.reshape(-1, 1)])
    
    for i in range(n):
        Ab[i] = Ab[i] / Ab[i, i]
        for j in range(i + 1, n):
            Ab[j] = Ab[j] - Ab[i] * Ab[j, i]
    
    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            Ab[j] = Ab[j] - Ab[i] * Ab[j, i]
    
    return Ab[:, -1]


A = np.array([[2, 1, -1], [3, 2, 1], [1, -1, 2]], dtype=float)
b = np.array([8, 13, 3], dtype=float)

    
solution = GaussJordan(A, b)
print("Solution:", solution)

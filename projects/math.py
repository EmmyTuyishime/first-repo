import numpy as np
# Coefficient matrix
A = np.array([[1, 1], [2, -1]])

# Constant matrix
B = np.array([5, 1])

# Solution
X = np.linalg.solve(A, B)
print("Solution (x, y):", X)

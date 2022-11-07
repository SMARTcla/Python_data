import numpy as np

a = np.array([[1, 1, 1], [9, 3, 1], [1, -1, 1]])
b = np.array([12, 54, 2])

result = np.linalg.solve(a,b)

print(result)
import numpy as np

a = np.matrix("1, 1, 1 ; 0, 1, 2 ; 2, 0, 1")
b = np.matrix("1328;1228;1208")

result = np.linalg.inv(a)

x = result.dot(b)

print(x)
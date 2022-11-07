import numpy as np

a = np.matrix([[3, 0, 3 ], [6, 0.25, 0 ], [1, 1/3, 1]])
b = np.matrix("1;1;1")

result = np.linalg.inv(a)

x = result.dot(b)

x[0] = 1/ x[0]
x[1] = 1/ x[1]
x[2] = 1/ x[2]

print(x)
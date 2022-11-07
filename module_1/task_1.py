import numpy as np

a = np.matrix("1, 1, 1 ; 0.05, 0.07, 0 ; 0.05, 0, 0.06")
b = np.matrix("50000;2250;1400")

result = np.linalg.inv(a)

x = result.dot(b)

print(x)
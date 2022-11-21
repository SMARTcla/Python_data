#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
import random

x = [10.0, 2 , -13.0]
y = [8,-4,14]
triangle_x = []
triangle_y = []
x0 = 1.0
y0 = 0.0
for i in range(10000):
    chosen_dot_triangle = random.randint(0, 2)
    triangle_x.append((x[chosen_dot_triangle]+x0)/2.0)
    triangle_y.append((y[chosen_dot_triangle]+y0)/2.0)
    x0 = (x[chosen_dot_triangle]+x0)/2.0
    y0 = (y[chosen_dot_triangle]+y0)/2.0

triangle_y = np.array(triangle_y)
triangle_x = np.array(triangle_x)

plt.scatter(triangle_x, triangle_y)
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()



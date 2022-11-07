import numpy as np

def get_polynoms(coords):
    a = np.array([])
    b = np.array([])
    lis = []
    for i,j in enumerate(coords):
        a = np.append(a, np.array(j[0]))
        b = np.append(b, np.array(j[1]))
        
    c = np.array([])
    for i,j in enumerate(coords):
        c = np.append(c, np.array(a[i]*b[i]))

    return c

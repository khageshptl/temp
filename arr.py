import numpy as np
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
def array(x, y, z, n):
    x = 2
    y = 2
    z = 2
    n = 3
    a = list()

    for i in range (x+1):
        for j in range (y+1):
            for k in range (z+1):
                if(i + j + k != n):
                    a.append([i, j, k])
    a = np.array(a)
    return a

x = 2
y = 2
z = 2
n = 3
print(array(x, y, z, n))
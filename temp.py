import numpy as np


r = 3
c = 3
m = []
for i in range(r):
    l = []
    for j in range(c):
        v = int(input())
        # v = 
        l.append(v)
    m.append(l)
m = np.array(m)
print(m)
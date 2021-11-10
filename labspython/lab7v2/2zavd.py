import random
import numpy as np
a = []
b = []
n=int(input("Введіть кількість рядків матриці : "))
m=int(input("Введіть кількість стовбців матриці : "))
for i in range(n):
    a.append([float(random.randint(0,1)) for j in range(m)])
a = np.array(a)
print(a)
for i in range(n):
    b.append([float(random.randint(0, 1)) for j in range(m)])
b = np.array(b)
print(b)
for j in range(m):
    if a[i][j] == 0:
         b[i][j] = a[i][j]
a = np.array(a)
print(a)
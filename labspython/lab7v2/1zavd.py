import random
import numpy as np

sum = 0
a = []
n = int(input("Введіть кількість рядків матриці : "))
m = int(input("Введіть кількість стовбців матриці : "))
for i in range(n):
    a.append([float(random.randint(-10, 10)) for j in range(m)])
    for j in range(m):
        if i % 2 != 0 and j % 2 == 0 and a[i][j] > 0:
            sum += a[i][j]
a = np.array(a)
print(a)
print(sum)

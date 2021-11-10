import random
import numpy as np

a = []
n=int(input("Введіть кількість рядків матриці : "))
m=int(input("Введіть кількість стовбців матриці : "))
for i in range(n):
    a.append([float(random.randint(-10,10)) for j in range(m)])

sorted(a, key = sum )
a = np.array(a)
print(a)
# Дано матрицю A(m^n) та вектор x(n) . Перевірити, чи виконується рівність Ax=b .

import random
import numpy as np

sum = 0
a = []
Ax = []
m = int(input("Введіть кількість рядків матриці : "))
n = int(input("Введіть кількість стовбців матриці : "))
for i in range(m):
    a.append([float(random.randint(-10, 10)) for j in range(n)])
a = np.array(a)
print('a = {0}'.format(a))
x = [random.randint(-10, 10) for j in range(n)]
# x = [0 for j in range(n)]
b = [random.randint(-10, 10) for j in range(n)]
# b = [0 for j in range(n)]
print('vector b = {0} '.format(b))
print('vector x = {0} '.format(x))
for i in range(m):
    for j in range(n):
        sum += a[i][j] * x[j]
    Ax.append(sum)
boolean = True
for i in range(n):
    if Ax[i] != b[i]:
        print('Ax != b')
        boolean = False
        break
if boolean:
    print('Ax = b')
print('Ax = {0}'.format(Ax))

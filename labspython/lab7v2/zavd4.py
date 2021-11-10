#Розмістити елементи непарних рядків у порядку зростання.
import random
import numpy as np
a = []
n=int(input("Введіть кількість рядків матриці : "))
m=int(input("Введіть кількість стовбців матриці : "))
for i in range(n):
    a.append([float(random.randint(-10,10)) for j in range(m)])
for i in range(n):
    if i % 2 == 0:
        a[i].sort()
a = np.array(a)
print(a)
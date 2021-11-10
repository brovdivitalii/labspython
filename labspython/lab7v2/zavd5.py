# Дана цілочислова прямокутна матриця.
# Визначити кількість стовпців, які не містять жодного нульового елемента.
import random
import numpy as np
count = 0
a = []
n=int(input("Введіть кількість рядків матриці : "))
m=int(input("Введіть кількість стовбців матриці : "))
for i in range(n):
    a.append([float(random.randint(-2,2)) for j in range(m)])
for j in range(m):
    for i in range(n):
        if a[i][j] == 0:
            count += 1
            break # якщо хоча б один ел. ствопця = 0, то переходимо до наст. стовпця
a = np.array(a)
print(a)
print('К-сть не нульових стовпців = {0}'.format(m - count))

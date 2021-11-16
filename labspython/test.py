# двовимрний масив з нулів та одиниць, якщо 0 то продовжуєм, якщо 1 то програв
import random
import numpy as np
a = []
n = int(input("Введіть кількість рядків матриці : "))
m = int(input("Введіть кількість стовбців матриці : "))
for i in range(n):
    a.append([float(random.randint(0, 1)) for j in range(m)])
a = np.array(a)
print(a)
step = int(input('введіть к-сть кроків = '))
for el in range(step):
        i1 = int(input('введіть номер рядка = ')) - 1
        j1 = int(input('введіть номер стовпця = ')) - 1
        if a[i1][j1] == 1:
            print('Ви попали на 1, програш')
            break
        else:
            print('ви попали на 0, гра продовжується')
print('Гра закінчена')


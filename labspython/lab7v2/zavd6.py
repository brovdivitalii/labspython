# Дана цілочислова прямокутна матриця.
# Переставляючи рядки даної матриці, розташувати їх у відповідності з ростом характеристик.
# Характеристикою рядка цілочислової матриці назвемо суму її додатних парних елементів.

import random
n = int(input("Введіть кількість рядків матриці : "))
m = int(input("Введіть кількість стовбців матриці : "))
a = [[float(random.randint(-5,15)) for j in range(m)] for i in range(n)]
b = [sum(filter(lambda el : (el > 0 and el % 2 == 0), row)) for row in a]
print(*a, sep = "\n")
print("\n",b,"\n")

change=True
while change: # поки ми робили заміну (change==True)
    change = False
    for i in range(1,len(b)):
        if b[i-1] > b[i]:
            b[i-1], b[i]= b[i], b[i-1]
            a[i - 1], a[i] = a[i], a[i - 1]
            change = True

print(*a, sep = "\n")
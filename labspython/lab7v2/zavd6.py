# Дана цілочислова прямокутна матриця.
# Переставляючи рядки даної матриці, розташувати їх у відповідності з ростом характеристик.
# Характеристикою рядка цілочислової матриці назвемо суму її додатних парних елементів.
import random
a = []
b = []
suma = 0
n = int(input("Введіть кількість рядків матриці : "))
m = int(input("Введіть кількість стовбців матриці : "))
a = [[float(random.randint(-5,15)) for j in range(m)] for i in range(n)]
#for i in range(n):
#   a.append([float(random.randint(-5,15)) for j in range(m)])
# for i in range(n):
#     suma = 0
#     for j in range(m):
#         if a[i][j] > 0 and a[i][j] % 2 == 0 :
#             suma += a[i][j]
#     b.append(suma)
b = [sum(filter(lambda el : (el > 0 and el % 2 == 0), row)) for row in a]
print(*a, sep = "\n")
print("\n",b,"\n")

for i in range(n-1,-1,-1):
    a[b.index(max(b))], a[i] = a[i], a[b.index(max(b))]
    b[b.index(max(b))], b[i] = b[i], b[b.index(max(b))]
    b[b.index(max(b))] = -1

print(*a, sep = "\n")

from math import gcd
from functools import reduce

mul = 1
while True:
    n = int(input('n = '))
    if 0 > n > 101:
        print('Введіть число з проміжку (0,100)')
    else:
        break
a = list(map(int, input('Введіть числа ').split(' ')))
if len(a) != n:
    raise Exception('n != довжині масиву')
for i in range(n):
    mul *= a[i]
b = reduce(gcd, a)  # нск = добуток / нсд
print(mul / b)

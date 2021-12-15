from math import gcd
from functools import reduce
while True:
    n = int(input('n = '))
    if 0 > n > 101:
        print('Введіть число з проміжку (0,100)')
    else:
        break
a = list(map(int, input('Введіть числа ').split(' ')))
if len(a) != n:
    raise Exception('n != довжині масиву')
b = reduce(gcd, a)
print(b)

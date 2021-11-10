import math
sum = 0
a = float(input('Введіть дійсне число а = '))
n = int(input('Введіть натуральне число n = '))
while n >= 1:
    sum = sum + math.log((abs(a)))**n
    n = n-1
print(sum)
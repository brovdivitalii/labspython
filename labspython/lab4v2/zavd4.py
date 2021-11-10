# знайти знач y
# y = ln|x| - n     if x < n
# y = ln|x| - n     if x = n
# y = cos(n*x)      if x > n
import math
x = float(input('Введіть х = '))
n = float(input('Введіть n = '))
if x < n or x ==n:
    y = math.log(abs(x))
    print('y = {0:3.3f}'.format(y))
else:
    y = math.cos(n*x)
    print('y = {0:3.3f}'.format(y))

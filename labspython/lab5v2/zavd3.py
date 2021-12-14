import math
sum = 0
x = float(input('x = '))
n = int(input('n = '))
for i in range(n):
    sum = (x**n)/n + sum
    n +=1
sum *= -1
ln = math.log1p(1-x)
if ln == sum:
    print('справедливість рівна')
else:
    print('справедливынсть не рівна')
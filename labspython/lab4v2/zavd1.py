#Обчислити площу трикутника, якщо трикутник задано довжинами сторін.
# a,b,c - сторони 3кутника
# p - півпериметр s - площа
import math
a = float(input('input a = '))
b = float(input('input b = '))
c = float(input('input c = '))
p = (a + b + c)/2
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
print('Площа triangle - {0:3.3f}'.format(s))
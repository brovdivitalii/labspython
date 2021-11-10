import math
def f(x):
    return math.sqrt(4 * x + math.sin(math.sqrt(x ** 3)))
def integral(a,b):
    return (b-a) * f(a)
x = float(input('x = '))
a = float(input('a = '))
b = float(input('b = '))
s = integral(a,3) + integral(a,b)
print('{0:.2f}'.format(s))


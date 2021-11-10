# За даними дійсними числами a і b  обчислити
# u = f(a,b) + f(2,a) + 2
import math
a = float(input('a = '))
b = float(input('b = '))
def f(x,y):
    if x > 0 and y > 0 :
        return x**3 + math.sqrt(x**2 + y**4)
    elif   x > 0 and y < 0  :
        return (x**2 - 2*x + math.sqrt(x))/(x**(3/5))
    else:
        return math.sin(x*y)
u = f(a,b) + f(2,a) + 2
print('u = f({0},{1}) + f(2,{0}) + 2 = {2}'.format(a,b,u))

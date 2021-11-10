# # Використовуючи відповідну підпрограму знаходження , обчислити значення виразу gi
from math import sin, cos


def g(x: int):
    if x == 0:
        return 9
    elif x == 1:
        return 35
    elif x > 1:
        return sin(g(x - 1) + cos(g(x-2)))


print(g(7) + g(9))



# import math
# g0 = 9
# g1 = 35
# gi = 0
# def g(i, g0=9,g1=35):
#     if
#     for i in range(2,i+1):
#         gi = (math.sin(g1 + math.cos(g0)))
#         g0 = g1
#         g1 = gi
#     return gi
# s = g(7) + g(9)
# print(s)
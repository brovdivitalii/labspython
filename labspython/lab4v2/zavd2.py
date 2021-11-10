# Дано дійсні числа: a, b, c, d. . З’ясувати, чи належать ці числа інтервалу[1;2]^(c;d)

a = float(input('input a = '))
b = float(input('input b = '))
c = float(input('input c = '))
d = float(input('input d = '))
if a >= 1 and a <= 2 and a > c and a < d:
    print('{0} належить проміжку'.format(a))
else:
    print('{0} не належить'.format((a)))
if b >= 1 and b <= 2 and b > c and b < d:
    print('{0} належить проміжку'.format(b))
else:
    print('{0} не належить'.format(b))
# наступний код не потрібний, так як вже з умови c та d не належать проміжку
''' 
if 1 <= c <= 2 and c < c < d:
    print('c належить проміжку')
else:
    print('c не належить')
if 1 <= d <= 2 and d < d < d:
    print('c належить проміжку')
else:
    print('c не належить')
'''
# тому можна вивести, що c та d завжди не належать проміжку
print('числа {0} та {1} не належать даному проміжку'.format(c,d))
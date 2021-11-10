# n - к-ість елементів, a - список, g - середнє геометричне знач
n = int(input('введіть кількість елементів = '))
a = []
for i in range(n):
    num = float(input('введіть елемент {0} = '.format(i+1)))
    a.append(num)
# Знаходимо середнє геометричне:
dobutok=1
for el in a:
    dobutok= dobutok*el
g=dobutok**(1/n)
print('Середнє геометричне знач = {0}'.format(g))



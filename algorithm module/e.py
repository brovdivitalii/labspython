b = []
while True:
    n = int(input('n = '))
    if 0 > n > 100:
        print('Введіть число з проміжку (0,100)')
    else:
        break
a = list(map(float, input('Введіть числа ').split(' ')))
if len(a) != n:
    raise Exception('n != довжині масиву')
for i in range(n):
    a[i] = abs(a[i])
    b.append(a[i])
print('{0}'.format(max(b)))

while True:
    n = int(input('n = '))
    if 0 > n > 100:
        print('Введіть число з проміжку (0,100)')
    else:
        break
a = list(map(float, input('Введіть числа ').split(' ')))
if len(a) != n:
    raise Exception('n != довжині масиву')
print('{0}'.format(min(a)*2))

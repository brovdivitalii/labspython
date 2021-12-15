while True:
    n = int(input('n = '))
    if 0 > n > 100:
        print('Введіть число з проміжку (0,100)')
    else:
        break
b = 0
k = 0
a = list(map(int, input('Введіть числа ').split(' ')))
if len(a)!= n:
    raise Exception('n != довжині масиву')
else:
    for i in range(n):
        if a[i] <= 2.5:
            b = a[i]
            k = i
            print('{0} {1}'.format(i, a[i]))
            break
        else:
            print('Not found')
            break

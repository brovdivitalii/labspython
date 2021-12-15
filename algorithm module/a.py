b =[]
while True:
    n = int(input('n = '))
    if n > 100:
        print('Введіть число <100')
    else:
        break
a = list(map(int, input('Введіть числа ').split(' ')))
if len(a)!= n:
    raise Exception('n != довжині масиву')
else:
    for i in range(n):
        if a[i] >= 0:
            a[i] += 2
    print(*a)
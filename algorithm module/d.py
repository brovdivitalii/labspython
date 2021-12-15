count = 0
sum = 0
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
    if a[i]>0:
        count +=1
        sum += a[i]
    else:
        raise Exception('Not Found')
print('{0:.2f}'.format(sum/count))

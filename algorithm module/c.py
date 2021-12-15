count = 0
sum = 0
while True:
    n = int(input('n = '))
    if 0 > n > 100:
        print('Введіть число з проміжку (0,100)')
    else:
        break
a = list(map(int, input('Введіть числа ').split(' ')))
if len(a) != n:
    raise Exception('n != довжині масиву')
for i in range(n):
    if a[i] > 10000:
        raise Exception('Числа повинні бути <10000')
    if a[i] > 0 and a[i] % 6 == 0:
        count += 1
        sum += a[i]
print('{0} {1}'.format(count, sum))
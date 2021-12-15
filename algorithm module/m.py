count = 0
count1 = 0
while True:
    n = int(input('n = '))
    if 1 > n > 100:
        print('Введіть число з проміжку (1,200)')
    else:
        break
a = list(map(int, input('Введіть числа ').split(' ')))
if len(a) != n:
    raise Exception('n != довжині масиву')
for i in range(n):
    if -50 > a[i] > 50:
        raise Exception('Числа повинні бути >-50 та <50')
for i in range(n):
    if a[i] > 0:
        count += 1
    else:
        count = 0
    if count > count1:
        count1 = count
print(count1)
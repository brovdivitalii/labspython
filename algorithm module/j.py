res = 0
a = list(map(int, input('Введіть числа від 0 до 9 ').split(' ')))
for i in range(len(a)):
    if 0 > a[i] > 9:
        raise Exception('Потрібно число від 0 до 9')
for i in range(10):
    res += a.count(i)//2
print(res)

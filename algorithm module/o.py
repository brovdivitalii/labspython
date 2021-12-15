n = int(input('n: '))
spysok = list(map(int, input('Введіть числа 1 масива: ').split(' ')))
if len(spysok) != n:
    raise ValueError
m = int(input('m: '))
spysok2 = list(map(int, input('Введіть числа 2 масива: ').split(' ')))
if len(spysok2) != m:
    raise ValueError

res = []
for i in spysok:
    if i not in spysok2:
        res.append(i)

print(len(res))
print(*res)

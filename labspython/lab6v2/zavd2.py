b = []
n = int(input('введіть кількість елементів = '))
res = 1
v1 = 0
v2 = 1
i1 = i2 = 1
for i in range(1,n+1):
    if i % 2 == 0:
        while i1 <= i:
            v1 = v1 + 1/i1
            i1 = i1 + 1
        b.insert(i, v1)
    else:
        while i2 <= i:
            v2 = v2 * i2
            sum= (v2/2) + 3
            i2 = i2+1
        b.insert(i, sum)
for i in range(1, n+1):
    if i % 2 != 0:
        res = res * b[i-1]
print(b)
print(res)

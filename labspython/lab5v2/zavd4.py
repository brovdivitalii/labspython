x0 = x1 = 1
xi = 0

i = int(input('введіть i = '))
if i < 2:
    print("1")
else:
    for n in range(2,i+1):
        xi = x1 + 2* x0
        x0 = x1
        x1 = xi
print(xi)



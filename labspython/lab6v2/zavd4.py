# Впорядкувати елементи масиву за спаданням
n = int(input('введіть кількість елементів = '))
a = []
for i in range(n):
    num = float(input('введіть елемент {0} = '.format(i)))
    a.append(num)
print('Ваш список: {0}'.format(a))
a.sort(reverse=True)
print('Ваш відсортований список: {0}'.format(a))
# дано n-виміринй вектор, знайти добуток вектора на дійсне число.
a = []
num = float(input('Введіть число: '))
n = int(input('введіть к-сть вимірів: '))
for i in range(n):
    m = float(input('введіть коорд.{0} = '.format(i+1)))
    a.append(m*num)
print('добуток вектора a на число {1} = {0}'.format(a, num))
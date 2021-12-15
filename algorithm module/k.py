m = list(map(int, input('Введіть числа: ').split(' ')))
seq = list(range(1, m[0]+1))
a = m[1]
b = m[2]
c = m[3]
d = m[4]
print(seq[:a-1:] + list(reversed(seq[a-1:b:])) + seq[b:c-1:] + list(reversed(seq[c-1:d:])) + seq[d::])
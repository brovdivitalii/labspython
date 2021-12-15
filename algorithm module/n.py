from math import floor, ceil

n = int(input('n: '))
seq = list(map(int, input('Номери: ').split(' ')))
if len(seq) != n:
    raise Exception('n != довжині масиву')
if n % 2 != 0:
    seq.insert(0, seq.pop(floor(n / 2) - 1))
    seq.insert(-1, seq.pop(ceil(n / 2) + 1))
else:
    seq.insert(0, seq.pop(int(n / 2) - 1))
    seq.insert(n - 1, seq.pop(int(n / 2)))

print(*seq)

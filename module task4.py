sum = 0
c = 0
with open('file.txt') as file:
    for number in file:
        n = int(number)
        sum += n
        c += 1
avg = sum/c
print(avg)
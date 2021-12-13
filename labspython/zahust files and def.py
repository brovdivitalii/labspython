# дано файл з цілими числами, підрахувати яких більше, тих що більше записати в окремий файл
import random
def GenFile(nums):
    n = int(input('від = '))
    m = int(input('до = '))
    a = [random.randint(n, m) for i in range(nums)]
    with open('allnumbers.txt', 'w') as file:
        file.write('\n'.join(map(lambda el: str(el), a)))
def get_nums():
    b = []
    c = []
    count1 = 0
    count2 = 0
    with open('allnumbers.txt', 'r') as file:
        for line in file:
            num = int(line)
            if num % 2 == 0:
                c.append(num)
                count1 += 1
            else:
                b.append(num)
                count2 += 1
    with open('newnums.txt', 'w') as newfile:
        if count1 > count2:
            newfile.write(str(c))
        else:
            newfile.write(str(b))
k = int(input('введіть к-сть чисел= '))
GenFile(k)
get_nums()

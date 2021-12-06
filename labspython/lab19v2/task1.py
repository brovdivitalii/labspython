# Дано текстовий файл, який містить дійсні числа. Визначити найбільший елемент серед від’ємних.
numbers = []
with open('task1.txt') as file:
    for line in file:
        num = float(line)
        if num < 0:
            numbers.append(num)
print(max(numbers))

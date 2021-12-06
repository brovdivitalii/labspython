# Дано типізований файл, який містить дійсні числа. Використовуючи динамічну структуру даних чергу для збереження
# елементів, визначити найбільше число. Всі нульові значення у даному файлі замінити знайденим найбільшим значенням.
numbers = []
with open('task2.txt','r') as file:
    for line in file:
        num = float(line)
        numbers.append(num)
for i in range(len(numbers)):
    if numbers[i] == 0:
        numbers[i] = max(numbers)
with open('task2.txt', 'w') as file2:
    for el in numbers:
        file2.write(str(el)+ '\n')
print('найбільше число= {0}'.format((max(numbers))))

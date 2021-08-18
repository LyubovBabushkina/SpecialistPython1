# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]

# Вариант 1
list = [2, -5, 8, 9, -25, 25, 4]
print(list)
new_list = []
i = 0

while i < 7:
    if list[i] >= 0 and (list[i]**0.5 - int(list[i]**0.5)  == 0):
        new_list.append(int(list[i]**0.5))
    i += 1
print(new_list)

# Вариант 2
# Произвольный список

import random
numbers = []
n = int(input("n: "))
i = 0

while i < n:
    numbers.append(random.randint(-100, 100))
    i += 1
print(numbers)

new_numbers = []
i = 0
while i < n:
    if numbers[i] >= 0 and (numbers[i]**0.5 - int(numbers[i]**0.5)  == 0):
        new_numbers.append(int(numbers[i]**0.5))
    i += 1
print(new_numbers)

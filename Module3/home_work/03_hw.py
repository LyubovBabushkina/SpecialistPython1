# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random
numbers = []
n = int(input("n: "))
i = 0
while i < n:
    numbers.append(random.randint(-100, 100))
    i += 1
print(numbers)

i = 0
s = 0
while i < n:
    if numbers[i] > 0 and (numbers[i] % 2 == 0):
        s += numbers[i]
    i += 1
print(s)

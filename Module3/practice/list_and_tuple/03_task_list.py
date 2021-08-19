# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.
 
import random
numbers = []
n = int(input("n: "))
i = 0
while i < n:
    numbers.append(random.randint(-10, 10))
    i += 1
print(numbers)

s = 0
for el in numbers:
    s += el
print("Сумма равна", s)

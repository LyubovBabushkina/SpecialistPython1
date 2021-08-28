# Напишите функцию принимающую на вход целое числом n. И возвращающую список из n элементов.
# заполненный случайными целыми числами в диапазоне от a до b.
# Примечание: все элементы списка должны быть гарантировано уникальными(неповторяющимися)
# Если создать список с заданными параметрами невозможно - функция должна выбросить исключение(любое)

import random
def random_unique(n, a, b):
    try:
        if 0 < n <= b - a + 1:
            numbers = []
            while len(numbers) < n:
                new = random.randint (a, b)
                if numbers.count(new) == 0:
                    numbers.append(new)
        return numbers
    except UnboundLocalError:
        return print("Некорректное число")

print(random_unique(7, -2, 10))
print(random_unique(17, -2, 10))

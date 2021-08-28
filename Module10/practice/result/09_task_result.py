# Напишите функцию принимающую на вход целое числом n. И возвращающую список из n элементов.
# заполненный случайными целыми числами в диапазоне от a до b.
# Примечание: для генерации случайного числа используйте import random

import random
def random_numbers(n, a, b):
    numbers = []
    for _ in range(n):
        numbers.append(random.randint (a, b))
    return numbers

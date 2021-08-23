# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

import random
def gen_list(size, of, to):
    number = []
    for _ in range(size):
        number.append(random.randint(of, to))
    return number
numbers = gen_list(5, -10, 10)


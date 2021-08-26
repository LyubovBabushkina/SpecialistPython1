# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию.
# Найдите:
# 1. Количество элементов списка не превышающие 10
# 2. Сумму всех положительных элементов списка
# 3. Среднее арифметическое всех четных элементов

lst = [4, -7, 10, 21, -100, 44, 57, -4, 0]

nomore_ten = [el for el in lst if el <= 10]
print(len(nomore_ten))

positive = [el for el in lst if el > 0]
sum_positive = 0
for el in positive:
    sum_positive += el
print(sum_positive)

even = [el for el in lst if el % 2 == 0]
sum = 0
for el in even:
    sum += el
print(sum / len(even))

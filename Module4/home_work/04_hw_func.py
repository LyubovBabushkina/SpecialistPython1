# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.

common_fractions = str("5/6 + 4/7")
# разбиение по пробелу
numbers_signs = common_fractions.split(" ")  # список чисел и знаков между ними

# Определяем у первой дроби целую часть, числитель и знаменатель дробной части
if numbers_signs[0].find("/") == -1:
    int_1 = int(numbers_signs[0])   # int_1 - целая часть первого числа
    k = numbers_signs[1].find("/")  # индекс дробной черты (если она есть)
    if k != -1:
        numerator_1 = int(numbers_signs[1][0:k])
        divisor_1 = int(numbers_signs[1][k+1: ])
    else:
        numerator_1 = 0
        divisor_1 = 1
else:
    int_1 = 0
    k = numbers_signs[0].find("/")   # индекс дробной черты (если она есть)
    numerator_1 = int(numbers_signs[0][0:k])
    divisor_1 = int(numbers_signs[0][k + 1:])

if int_1 < 0:
    numerator_1 = -1 * numerator_1

# Определили у 2 дроби целую часть, числитель и знаменатель дробной части
if numbers_signs[-1].find("/") == -1:
    int_2 = int(numbers_signs[-1])  # int_2 - целая часть второго числа
    numerator_2 = 0
    divisor_2 = 1
else:
    k = numbers_signs[-1].find("/")   # индекс дробной черты (если она есть)
    numerator_2 = int(numbers_signs[-1][0:k])
    divisor_2 = int(numbers_signs[-1][k + 1:])
    if numbers_signs[-2] == "+" or numbers_signs[-2] == "-":
        int_2 = 0
    else:
        int_2 = int(numbers_signs[-2])

if int_2 < 0:
    numerator_2 = -1 * numerator_2

# Перевод в неправильные дроби
numerator_1 = int_1 * divisor_1 + numerator_1
numerator_2 = int_2 * divisor_2 + numerator_2

#  в случае вычитания дробей превращаем разность в сумму
if numbers_signs[1] == "-" or numbers_signs[2] == "-":
    numerator_2 = -1 * numerator_2

# Финальные вычисления (складываем обыкновенные дроби)
numerator = numerator_1 * divisor_2 + numerator_2 * divisor_1
divisor = divisor_1 * divisor_2

# Выделение целой части и вывод дроби (или целого числа)
if numerator % divisor == 0:
    print(common_fractions, "=", f"{int(numerator/divisor)}")
else:
    # Сокращение дроби
    for i in range(int(abs(numerator)), 1, -1):
        if numerator % i == 0 and divisor % i == 0:
            numerator = numerator / i
            divisor = divisor / i
    # Выделение целой части
    int_fin = abs(numerator) // divisor * int(numerator / abs(numerator))
    if int_fin == 0:
        print(common_fractions, "=", f"{int(numerator)}/{int(divisor)}")
    else:
        numerator = abs(numerator) % divisor
        print(common_fractions, "=", f"{int(int_fin)} {int(numerator)}/{int(divisor)}")



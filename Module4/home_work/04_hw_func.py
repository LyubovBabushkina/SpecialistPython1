# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y
# ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.

# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

common_fractions = str("-2/3 - -2")

def add_or_subt(str_number):
# результат -  список из двух дробей, в конце 1 если сложение, "-1" если вычитание
    if str_number.find("+") != -1:
        numbers = str_number.split(" + ")
        numbers.append("1")
    else:
        numbers = str_number.split(" - ")
        numbers.append("-1")
    return numbers

def fractionalization(str_number):
    # Определяем у дроби целую часть, числитель и знаменатель дробной части
    numbers_signs = str_number.split(" ")
    k = numbers_signs[-1].find("/")  # индекс дробной черты. Если её нет, к = -1
    if k != -1:
        numerator = int(numbers_signs[-1][0:k])
        divisor = int(numbers_signs[-1][k+1:])
    else:
        numerator = 0
        divisor = 1

    if numbers_signs[0].find("/") == -1:
        int_part = int(numbers_signs[0])   # int_part - целая часть
    else:
        int_part = 0
    # знак числителя
    if int_part < 0:
        numerator = -1 * numerator
    # Переводим в обыкновенную дробь без целой части
    numerator = int_part * divisor + numerator
    return (numerator, divisor)     # (числитель, знаменатель)

numbers_signs = add_or_subt(common_fractions)
fract_1 = fractionalization(numbers_signs[0])
fract_2 = fractionalization(numbers_signs[1])

# Перевод в одну дробь с общим знаменателем без целой части
numerator = fract_1[0] * fract_2[1] + fract_2[0] * fract_1[1] * int(numbers_signs[-1])
divisor = fract_1[1] * fract_2[1]

# Сокращение, выделение целой части и вывод дроби (или целого числа)
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




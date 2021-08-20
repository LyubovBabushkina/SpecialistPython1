# Напишите функцию находящую n-ое число Фибоначчи.

def fibonach(n):
    f1 = 0
    f2 = 1
    for _ in range(3, n+1):
        f2 += f1
        f1 = f2 - f1
    return f2

print(fibonach(23))

# Ряд Фибоначчи 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711

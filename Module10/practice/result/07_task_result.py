# Напишите программу генерирующую и записывающую в файле произвольное 20000-значное целое число.
def big_number():
    import random
    f = open("twenty_thousand_digits.txt", "w", encoding="utf-8")
    for _ in range(20000):
        a = str(random.randint(0, 9))
        f.write(a)
    f.close()

big_number()

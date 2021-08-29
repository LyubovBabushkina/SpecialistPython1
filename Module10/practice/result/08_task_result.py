# Прочитав число из файла задачи 7, определите:
# Какие цифры встречаются в числе чаще всего?
# Если несколько цифр встречаются одинаковое максимальное кол-во раз - найдите любые.
# Является ли данное число(20000-значное) четным?

path = "twenty_thousand_digits.txt"
f = open(path, "r", encoding="utf-8")
twenty_thousand = f.readline()  # строка
frequency_digits = []

for i in range(10):
    frequency_digits.append(twenty_thousand.count(str(i)))

maximum = max(frequency_digits)
max_frequency = []
for i in range(10):
    if frequency_digits[i] == maximum:
        max_frequency.append(i)

print("Чаще всего встречаются цифры: ", end=' ')
print(*max_frequency, sep=', ')

if int(twenty_thousand[-1]) % 2 == 0:
    print("Данное 20000-значное число четное")
else:
    print("Данное 20000-значное число нечетное")

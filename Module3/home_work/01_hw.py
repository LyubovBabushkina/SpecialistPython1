# Дан список имен.
# Выведите все имена в одну строку через запятую
# Пример вывода:
# Иван, Ирина, Вячеслав, Василий, Петр

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
length = len(names)
i = 0
while  i < length - 1:
    print(names[i],  end = ", ")
    i += 1
print(names[i])

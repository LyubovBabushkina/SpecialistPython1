# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
i = 0
length = 0

while i < 5:
    if length < len(names[i]):
        length = len(names[i])
        number = i
    i += 1
print(names[number])

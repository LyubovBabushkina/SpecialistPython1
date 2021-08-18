# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/

list = text.split()
n = text.rstrip().lstrip().count(" ") + 1

i = 0
k = 0
while i < n:
    strlist = str(list[i])
    if len(strlist) > 5:
        k += 1
    i += 1
print(k)

# Напишите функцию принимающую время в секундах и возвращающую строку формата: “hh:mm:ss”,
# где hh - часы, mm- минуты, ss - секунды.
# Пример:
# 29143 секунд → 08:05:43

def time_hms(sec):
    h = str(sec//3600)
    if len(h) == 1:
        h = "0" + h
    m = str(sec % 3600 // 60)
    if len(m) == 1:
        m = "0" + m
    s = str(sec % 3600 % 60)
    if len(s) == 1:
        s = "0" + s
    return h + ":" + m + ":" + s

sec = 29143
print(time_hms(sec))

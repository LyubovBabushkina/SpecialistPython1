# Данные о товарах на складе хранятся в словаре
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]

Brand = []
for i in range(len(items)):
    Brand.append(dict(items[i])['brand'])
# Получили список брэндов с повторами в Brand
Brand_1 = list(set(Brand))  # список брэндов без повторов

print(f"Товары на складе представлены брэндами:",  ', '.join(Brand_1))

length = len(Brand_1)  # сколько наименований брендов
number = []

for i in range(length):
    m = Brand.count(Brand_1[i])
    number.append(m)
# number - список количеств каждого бренда

number_big = sorted(number, reverse=True)[0] # наибольшее количество
big = []

for i in range(length):
    if number[i] == number_big:
        big.append(Brand_1[i])
# big - список максимальных брендов

print("На складе больше всего товаров брэнда(ов):", ', '.join(big))

Price = []
for i in range(len(items)):
    Price.append(dict(items[i])['price'])  # все цены

big_price = []
for i in range(len(items)):
    if Price[i] == max(Price):
        num_max = i
        big_price.append(Brand[i])    # наименования брэндов с самой высокой ценой

print("На складе самый дорогой товар брэнда(ов):", ', '.join(big_price), f"- цена {max(Price)} рублей")

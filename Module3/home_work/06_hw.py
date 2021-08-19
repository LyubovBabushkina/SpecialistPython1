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
# Найдите:

i = 0
Brand = []
while i < 6:
    Brand.append(dict(items[i])['brand'])
    i += 1
    
# Получили список брэндов с повторами в Brand

Brand_1 = list(set(Brand))  # список брэндов без повторов

print("Товары на складе представлены брэндами: ", *Brand_1)

length = len(Brand_1)  # сколько брендов
number = []

i = 0
while i < length:
    m = Brand.count(Brand_1[i])
    number.append(m)
    i += 1
    
# number - список количеств каждого бренда

number_big = max(number)
big = []
i = 0
while i < length:
    if number[i] == number_big:
        big.append(Brand_1[i])
        i += 1
        
# big - список максимальных брендов

print("На складе больше всего товаров брэнда(ов): ", *big)


i = 0
Price = []
while i < 6:
    Price.append(dict(items[i])['price'])
    i += 1

i = 0
while i < 6:
    if Price[i] == max(Price):
        num_max = i
    i += 1
    
print("На складе самый дорогой товар брэнда(ов): ", Brand[num_max], max(Price))

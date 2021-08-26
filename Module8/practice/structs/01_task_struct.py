# Бегун проводил ежедневные тренировки и записывал расстояния которые пробегал за занятия в метрах:
distances = [600, 755, 321.6, 1234, 231, 456.6, 4561, 1200, 456]
# Переведите все значения в футы (получить и вывести новый список)

def meter_foot (meter):
    foot = int(meter * 3.2808)
    return foot

gen_foot = map(meter_foot, distances)
distances_foot = []
for el in gen_foot:
    distances_foot.append(el)
print(distances_foot)

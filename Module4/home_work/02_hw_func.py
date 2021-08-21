# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой
# При решении задачи необходимо использовать функцию расстояния между двумя точками.

A = (0, 3)
B = (3, 0)
C = (0, 0)

def distance(x1, y1, x2, y2):
    d = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return d

lengths_growth = sorted([distance(*A, *B), distance(*A, *C), distance(*B, *C)])  # самая короткая длина
segments = [{ "name" : "AB", "length" : distance(*A, *B)},{"name" : "AC", "length" : distance(*A, *C)}, {"name" : "BC", "length" : distance(*B, *C)}]

for i in range(3):
    if dict(segments[i])["length"] == lengths_growth[0]:
        print("Самый короткий отрезок:", dict(segments[i])["name"])
        break

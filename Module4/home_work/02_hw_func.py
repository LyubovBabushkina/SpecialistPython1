# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой
# При решении задачи необходимо использовать функцию расстояния между двумя точками.

A = (0, 3)
B = (4, 0)
C = (0, 0)

def distance(x1, y1, x2, y2):
    d = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return d

lengths_growth = sorted([distance(*A, *B), distance(*A, *C), distance(*B, *C)])
print(lengths_growth[0])

if lengths_growth[0] == distance(*A, *B):
    print("Самый короткий отрезок:", "AB")
elif lengths_growth[0] == distance(*A, *C):
    print("Самый короткий отрезок:", "AC")
else:
    print("Самый короткий отрезок:", "BC")

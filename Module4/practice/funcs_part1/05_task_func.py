# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc), если соединить эти точки отрезками
# и получится треугольник, то нужно найти его периметр и площадь.
# Если по заданным точкам треугольник построить нельзя, выведите соответствующее сообщение.
# Подсказка: для нахождения площади используйте Теорему Герона

def distance(x1, y1, x2, y2):
    d = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return d

def can_triangle(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    if x1 != x2:
        return ((y2-y1)*(x3-x1)/(x2-x1) != y3-y2)
    else:
        return ((x2-x1)*(y3-y1)/(y2-y1) != x3-x2)

def triangle_P(a, b, c):
    return (distance(*a, *b) + distance(*b, *c) + distance(*a, *c))

def triangle_S(a, b, c):
    p = triangle_P(a, b, c)/2
    s = (p * (p - distance(*a, *b)) *  (p - distance(*a, *c)) * (p - distance(*b, *c)))**0.5
    return s

  if can_triangle(a, b, c) == False:
    print("Такого треугольника не существуетб точки лежат на одной прямой. Измените вводные данные!")
else:
    print("Периметр = ", triangle_P(a,b,c))
    print("площадь = ", triangle_S(a, b, c))

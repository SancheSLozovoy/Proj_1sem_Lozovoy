from math import sqrt
a = 7
b = 2
c = 8


"""Функция для вычисленя периметра треугольника"""


def triangle_perimeter(st_a=a, st_b=b, st_c=c):
    return st_a + st_b + st_c


"""Функция для вычисленя площади треугольника"""


def triangle_area(st_a=a, st_b=b, st_c=c):
    p = (st_a + st_b + st_c) / 2
    return sqrt(p * (p - st_a) * (p - st_b) * (p - st_c))

